#!/usr/bin/env python3
"""Prepare the first Biomed Basics article publication and related-link cleanup."""

from __future__ import annotations

import argparse
import datetime
import hashlib
import html
import json
import os
import re
import tempfile
from pathlib import Path

from analyze_biomed_basic import ROOT, SITE_URL, parse_input, slugify


RELATED = {
    "biomed-bmet-clinical-engineering-htm": ["how-to-become-a-biomedical-equipment-technician", "biomed-translation-problems-medical-equipment-names", "biomed-resume-basics", "biomed-work-order-notes-ccr-method", "functional-testing-vs-calibration-vs-verification"],
    "electrical-safety-testing-medical-equipment": ["ground-neutral-and-hot-in-medical-equipment", "voltage-current-resistance-and-continuity-in-plain-english", "how-to-use-a-multimeter-in-biomed", "fuses-breakers-and-power-supplies-in-medical-equipment", "functional-testing-vs-calibration-vs-verification"],
    "functional-testing-vs-calibration-vs-verification": ["pass-fail-limits-and-why-the-test-point-matters", "tolerance-vs-accuracy", "how-to-read-device-specifications", "how-to-verify-a-repair-before-returning-equipment-to-service", "when-to-trust-the-device-s-internal-self-test"],
    "biomed-work-order-notes-ccr-method": ["what-unable-to-duplicate-should-actually-mean", "what-to-do-when-a-medical-device-is-involved-in-an-incident", "preserving-device-logs-after-a-serious-event", "how-to-reproduce-a-clinical-complaint-on-the-bench", "when-to-remove-medical-equipment-from-service"],
    "medical-equipment-battery-basics": ["how-medical-device-batteries-charge-and-communicate", "medical-device-batteries-runtime-capacity-and-state-of-health", "how-to-troubleshoot-charging-problems", "fuses-breakers-and-power-supplies-in-medical-equipment", "voltage-current-resistance-and-continuity-in-plain-english"],
    "basic-networking-for-medical-equipment": ["how-patient-monitors-communicate-with-central-stations", "how-to-troubleshoot-communication-failures", "how-to-isolate-device-vs-accessory-vs-infrastructure-problems", "hospital-emrs-and-medical-device-integration", "what-hl7-means-in-plain-english"],
    "hospital-emrs-and-medical-device-integration": ["how-patient-monitors-communicate-with-central-stations", "basic-networking-for-medical-equipment", "what-dicom-means-in-plain-english", "what-hl7-means-in-plain-english", "nurse-call-integration-basics"],
    "what-dicom-means-in-plain-english": ["hospital-emrs-and-medical-device-integration", "basic-networking-for-medical-equipment", "what-hl7-means-in-plain-english", "biomed-work-order-notes-ccr-method", "biomed-translation-problems-medical-equipment-names"],
    "biomed-resume-basics": ["how-to-become-a-biomedical-equipment-technician", "biomed-bmet-clinical-engineering-htm", "biomed-translation-problems-medical-equipment-names", "biomed-work-order-notes-ccr-method", "when-to-remove-medical-equipment-from-service"],
    "biomed-translation-problems-medical-equipment-names": ["biomed-bmet-clinical-engineering-htm", "biomed-work-order-notes-ccr-method", "basic-networking-for-medical-equipment", "biomed-resume-basics", "when-to-remove-medical-equipment-from-service"],
    "when-to-remove-medical-equipment-from-service": ["how-to-verify-a-repair-before-returning-equipment-to-service", "what-to-do-when-a-medical-device-is-involved-in-an-incident", "preserving-device-logs-after-a-serious-event", "how-to-reproduce-a-clinical-complaint-on-the-bench", "functional-testing-vs-calibration-vs-verification"],
    "how-to-think-before-calling-a-vendor": ["how-experienced-biomeds-think-through-a-new-problem", "how-to-avoid-confirmation-bias-while-troubleshooting", "what-known-good-actually-means", "how-to-read-a-medical-equipment-service-manual", "how-to-reproduce-a-clinical-complaint-on-the-bench"],
    "what-hl7-means-in-plain-english": ["hospital-emrs-and-medical-device-integration", "basic-networking-for-medical-equipment", "what-dicom-means-in-plain-english", "nurse-call-integration-basics", "biomed-work-order-notes-ccr-method"],
    "nurse-call-integration-basics": ["medical-device-alarm-troubleshooting-fundamentals", "relays-and-contact-closures-in-plain-english", "what-hl7-means-in-plain-english", "basic-networking-for-medical-equipment", "hospital-emrs-and-medical-device-integration"],
    "how-to-read-a-medical-equipment-service-manual": ["how-to-read-device-specifications", "how-to-read-a-troubleshooting-flowchart", "how-experienced-biomeds-think-through-a-new-problem", "software-firmware-and-configuration-problems-in-medical-equipment", "error-codes-what-they-tell-you-and-what-they-don-t"],
    "how-to-reproduce-a-clinical-complaint-on-the-bench": ["environmental-causes-of-medical-equipment-failures", "what-unable-to-duplicate-should-actually-mean", "why-changing-one-thing-at-a-time-matters", "how-to-avoid-confirmation-bias-while-troubleshooting", "what-known-good-actually-means"],
    "how-to-use-a-multimeter-in-biomed": ["tolerance-vs-accuracy", "how-to-read-a-troubleshooting-flowchart", "medical-equipment-cables-and-connectors-inspection-and-isolation", "voltage-current-resistance-and-continuity-in-plain-english", "electrical-safety-testing-medical-equipment"],
    "what-known-good-actually-means": ["medical-device-batteries-runtime-capacity-and-state-of-health", "medical-equipment-cables-and-connectors-inspection-and-isolation", "why-changing-one-thing-at-a-time-matters", "how-to-avoid-confirmation-bias-while-troubleshooting", "how-to-reproduce-a-clinical-complaint-on-the-bench"],
    "fuses-breakers-and-power-supplies-in-medical-equipment": ["ac-vs-dc-power-basics", "medical-equipment-power-troubleshooting-outlet-to-internal-supply", "ground-neutral-and-hot-in-medical-equipment", "voltage-current-resistance-and-continuity-in-plain-english", "how-to-use-a-multimeter-in-biomed"],
    "voltage-current-resistance-and-continuity-in-plain-english": ["how-defibrillators-charge-and-deliver-energy", "analog-vs-digital-signals", "ac-vs-dc-power-basics", "how-to-use-a-multimeter-in-biomed", "relays-and-contact-closures-in-plain-english"],
    "sensors-and-transducers-basics": ["how-infusion-pump-occlusion-detection-works", "how-oxygen-sensors-work-in-ventilators-and-anesthesia-machines", "how-invasive-blood-pressure-monitoring-works", "how-medical-equipment-measures-flow", "how-medical-equipment-measures-pressure"],
    "relays-and-contact-closures-in-plain-english": ["nurse-call-integration-basics", "voltage-current-resistance-and-continuity-in-plain-english", "how-to-use-a-multimeter-in-biomed", "fuses-breakers-and-power-supplies-in-medical-equipment", "basic-networking-for-medical-equipment"],
    "preserving-device-logs-after-a-serious-event": ["how-to-read-and-use-medical-device-event-logs", "what-to-do-when-a-medical-device-is-involved-in-an-incident", "when-to-remove-medical-equipment-from-service", "biomed-work-order-notes-ccr-method", "how-to-reproduce-a-clinical-complaint-on-the-bench"],
    "what-to-do-when-a-medical-device-is-involved-in-an-incident": ["preserving-device-logs-after-a-serious-event", "when-to-remove-medical-equipment-from-service", "biomed-work-order-notes-ccr-method", "how-to-reproduce-a-clinical-complaint-on-the-bench", "how-to-think-before-calling-a-vendor"],
    "how-to-avoid-confirmation-bias-while-troubleshooting": ["the-difference-between-a-symptom-cause-and-root-cause", "how-to-reproduce-a-clinical-complaint-on-the-bench", "what-known-good-actually-means", "how-to-think-before-calling-a-vendor", "functional-testing-vs-calibration-vs-verification"],
    "when-to-trust-the-device-s-internal-self-test": ["error-codes-what-they-tell-you-and-what-they-don-t", "functional-testing-vs-calibration-vs-verification", "sensors-and-transducers-basics", "what-known-good-actually-means", "how-to-read-a-medical-equipment-service-manual"],
    "why-changing-one-thing-at-a-time-matters": ["the-troubleshooting-process-observe-isolate-test-verify", "what-known-good-actually-means", "how-to-reproduce-a-clinical-complaint-on-the-bench", "how-to-avoid-confirmation-bias-while-troubleshooting", "how-to-think-before-calling-a-vendor"],
    "ground-neutral-and-hot-in-medical-equipment": ["ac-vs-dc-power-basics", "medical-equipment-power-troubleshooting-outlet-to-internal-supply", "electrical-safety-testing-medical-equipment", "voltage-current-resistance-and-continuity-in-plain-english", "how-to-use-a-multimeter-in-biomed"],
    "error-codes-what-they-tell-you-and-what-they-don-t": ["the-difference-between-a-symptom-cause-and-root-cause", "how-to-read-and-use-medical-device-event-logs", "software-firmware-and-configuration-problems-in-medical-equipment", "how-to-read-a-medical-equipment-service-manual", "when-to-trust-the-device-s-internal-self-test"],
    "what-unable-to-duplicate-should-actually-mean": ["how-to-reproduce-a-clinical-complaint-on-the-bench", "biomed-work-order-notes-ccr-method", "why-changing-one-thing-at-a-time-matters", "error-codes-what-they-tell-you-and-what-they-don-t", "when-to-remove-medical-equipment-from-service"],
    "medical-equipment-cables-and-connectors-inspection-and-isolation": ["how-ecg-lead-off-detection-works", "how-parameter-modules-communicate-with-host-monitors", "how-smart-batteries-communicate-with-medical-equipment", "how-to-troubleshoot-medical-device-accessories", "what-known-good-actually-means"],
    "how-to-troubleshoot-medical-device-accessories": ["how-ecg-lead-off-detection-works", "how-mainstream-co2-monitoring-works", "how-sidestream-co2-monitoring-works", "how-to-isolate-device-vs-accessory-vs-infrastructure-problems", "medical-equipment-cables-and-connectors-inspection-and-isolation"],
    "how-to-isolate-device-vs-accessory-vs-infrastructure-problems": ["how-anesthesia-waste-gas-scavenging-works", "the-troubleshooting-process-observe-isolate-test-verify", "how-to-troubleshoot-communication-failures", "environmental-causes-of-medical-equipment-failures", "how-to-troubleshoot-medical-device-accessories"],
    "medical-equipment-power-troubleshooting-outlet-to-internal-supply": ["how-to-troubleshoot-charging-problems", "fuses-breakers-and-power-supplies-in-medical-equipment", "ground-neutral-and-hot-in-medical-equipment", "how-to-use-a-multimeter-in-biomed", "medical-equipment-cables-and-connectors-inspection-and-isolation"],
    "medical-device-alarm-troubleshooting-fundamentals": ["how-ecg-lead-off-detection-works", "how-infusion-pump-occlusion-detection-works", "how-a-ventilator-measures-tidal-volume", "how-oxygen-sensors-work-in-ventilators-and-anesthesia-machines", "how-ventilator-pressure-sensors-work"],
    "environmental-causes-of-medical-equipment-failures": ["how-to-isolate-device-vs-accessory-vs-infrastructure-problems", "medical-equipment-power-troubleshooting-outlet-to-internal-supply", "medical-equipment-cables-and-connectors-inspection-and-isolation", "how-to-reproduce-a-clinical-complaint-on-the-bench", "what-unable-to-duplicate-should-actually-mean"],
    "software-firmware-and-configuration-problems-in-medical-equipment": ["how-parameter-modules-communicate-with-host-monitors", "error-codes-what-they-tell-you-and-what-they-don-t", "when-to-trust-the-device-s-internal-self-test", "how-to-read-a-medical-equipment-service-manual", "why-changing-one-thing-at-a-time-matters"],
    "how-to-read-and-use-medical-device-event-logs": ["error-codes-what-they-tell-you-and-what-they-don-t", "preserving-device-logs-after-a-serious-event", "medical-device-alarm-troubleshooting-fundamentals", "what-unable-to-duplicate-should-actually-mean", "software-firmware-and-configuration-problems-in-medical-equipment"],
    "how-to-verify-a-repair-before-returning-equipment-to-service": ["how-to-compare-your-test-result-to-manufacturer-specification", "how-to-read-device-specifications", "the-troubleshooting-process-observe-isolate-test-verify", "functional-testing-vs-calibration-vs-verification", "when-to-remove-medical-equipment-from-service"],
    "how-to-troubleshoot-communication-failures": ["how-patient-monitors-communicate-with-central-stations", "how-parameter-modules-communicate-with-host-monitors", "how-smart-batteries-communicate-with-medical-equipment", "analog-vs-digital-signals", "how-to-isolate-device-vs-accessory-vs-infrastructure-problems"],
    "how-to-troubleshoot-charging-problems": ["how-medical-device-batteries-charge-and-communicate", "how-defibrillators-charge-and-deliver-energy", "medical-device-batteries-runtime-capacity-and-state-of-health", "medical-equipment-battery-basics", "medical-equipment-power-troubleshooting-outlet-to-internal-supply"],
    "the-troubleshooting-process-observe-isolate-test-verify": ["how-to-read-a-troubleshooting-flowchart", "how-experienced-biomeds-think-through-a-new-problem", "the-difference-between-a-symptom-cause-and-root-cause", "how-to-isolate-device-vs-accessory-vs-infrastructure-problems", "why-changing-one-thing-at-a-time-matters"],
    "the-difference-between-a-symptom-cause-and-root-cause": ["the-troubleshooting-process-observe-isolate-test-verify", "error-codes-what-they-tell-you-and-what-they-don-t", "how-to-avoid-confirmation-bias-while-troubleshooting", "why-changing-one-thing-at-a-time-matters", "how-to-reproduce-a-clinical-complaint-on-the-bench"],
    "how-experienced-biomeds-think-through-a-new-problem": ["the-troubleshooting-process-observe-isolate-test-verify", "how-to-read-a-medical-equipment-service-manual", "what-known-good-actually-means", "how-to-avoid-confirmation-bias-while-troubleshooting", "how-to-think-before-calling-a-vendor"],
    "how-to-read-a-troubleshooting-flowchart": ["how-to-read-a-medical-equipment-service-manual", "the-troubleshooting-process-observe-isolate-test-verify", "how-to-use-a-multimeter-in-biomed", "what-known-good-actually-means", "when-to-trust-the-device-s-internal-self-test"],
    "ac-vs-dc-power-basics": ["voltage-current-resistance-and-continuity-in-plain-english", "ground-neutral-and-hot-in-medical-equipment", "fuses-breakers-and-power-supplies-in-medical-equipment", "how-to-use-a-multimeter-in-biomed", "medical-equipment-power-troubleshooting-outlet-to-internal-supply"],
    "analog-vs-digital-signals": ["how-ecg-acquisition-works", "how-spo2-measurement-works", "sensors-and-transducers-basics", "voltage-current-resistance-and-continuity-in-plain-english", "how-to-use-a-multimeter-in-biomed"],
    "medical-device-batteries-runtime-capacity-and-state-of-health": ["how-smart-batteries-communicate-with-medical-equipment", "how-medical-device-batteries-charge-and-communicate", "medical-equipment-battery-basics", "how-to-troubleshoot-charging-problems", "what-known-good-actually-means"],
    "how-to-read-device-specifications": ["how-nibp-works-in-a-patient-monitor", "how-to-compare-your-test-result-to-manufacturer-specification", "tolerance-vs-accuracy", "how-to-read-a-medical-equipment-service-manual", "functional-testing-vs-calibration-vs-verification"],
    "tolerance-vs-accuracy": ["pass-fail-limits-and-why-the-test-point-matters", "how-to-compare-your-test-result-to-manufacturer-specification", "how-to-read-device-specifications", "functional-testing-vs-calibration-vs-verification", "how-to-use-a-multimeter-in-biomed"],
    "how-to-compare-your-test-result-to-manufacturer-specification": ["pass-fail-limits-and-why-the-test-point-matters", "how-to-read-device-specifications", "tolerance-vs-accuracy", "functional-testing-vs-calibration-vs-verification", "how-to-verify-a-repair-before-returning-equipment-to-service"],
    "pass-fail-limits-and-why-the-test-point-matters": ["how-to-compare-your-test-result-to-manufacturer-specification", "tolerance-vs-accuracy", "how-to-read-device-specifications", "functional-testing-vs-calibration-vs-verification", "how-to-verify-a-repair-before-returning-equipment-to-service"],
    "how-nibp-works-in-a-patient-monitor": ["how-invasive-blood-pressure-monitoring-works", "how-medical-equipment-measures-pressure", "how-sidestream-co2-monitoring-works", "how-spo2-measurement-works", "sensors-and-transducers-basics"],
    "how-spo2-measurement-works": ["how-ecg-acquisition-works", "how-nibp-works-in-a-patient-monitor", "sensors-and-transducers-basics", "analog-vs-digital-signals", "how-to-troubleshoot-medical-device-accessories"],
    "how-ecg-acquisition-works": ["how-ecg-lead-off-detection-works", "how-spo2-measurement-works", "how-nibp-works-in-a-patient-monitor", "analog-vs-digital-signals", "sensors-and-transducers-basics"],
    "how-sidestream-co2-monitoring-works": ["how-medical-gas-sampling-systems-work", "how-mainstream-co2-monitoring-works", "how-oxygen-sensors-work-in-ventilators-and-anesthesia-machines", "sensors-and-transducers-basics", "how-to-troubleshoot-medical-device-accessories"],
    "how-ventilator-flow-sensors-work": ["how-a-ventilator-measures-tidal-volume", "how-medical-equipment-measures-flow", "how-ventilator-pressure-sensors-work", "sensors-and-transducers-basics", "how-to-compare-your-test-result-to-manufacturer-specification"],
    "how-ventilator-pressure-sensors-work": ["how-peep-is-generated-and-controlled", "how-medical-equipment-measures-pressure", "how-ventilator-flow-sensors-work", "sensors-and-transducers-basics", "how-to-compare-your-test-result-to-manufacturer-specification"],
    "how-medical-equipment-measures-pressure": ["how-an-anesthesia-machine-performs-a-leak-test", "how-infusion-pump-occlusion-detection-works", "how-an-anesthesia-machine-breathing-system-works", "how-invasive-blood-pressure-monitoring-works", "how-medical-equipment-measures-flow"],
    "how-medical-equipment-measures-flow": ["how-infusion-pumps-measure-or-control-flow", "how-a-ventilator-measures-tidal-volume", "how-an-anesthesia-machine-breathing-system-works", "how-oxygen-sensors-work-in-ventilators-and-anesthesia-machines", "how-ventilator-flow-sensors-work"],
    "how-invasive-blood-pressure-monitoring-works": ["how-medical-equipment-measures-pressure", "how-nibp-works-in-a-patient-monitor", "sensors-and-transducers-basics", "analog-vs-digital-signals", "medical-equipment-cables-and-connectors-inspection-and-isolation"],
    "how-oxygen-sensors-work-in-ventilators-and-anesthesia-machines": ["how-an-anesthesia-machine-breathing-system-works", "sensors-and-transducers-basics", "how-sidestream-co2-monitoring-works", "how-medical-equipment-measures-flow", "medical-device-alarm-troubleshooting-fundamentals"],
    "how-an-anesthesia-machine-breathing-system-works": ["how-an-anesthesia-machine-performs-a-leak-test", "how-anesthesia-waste-gas-scavenging-works", "how-oxygen-sensors-work-in-ventilators-and-anesthesia-machines", "how-medical-equipment-measures-flow", "how-medical-equipment-measures-pressure"],
    "how-anesthesia-waste-gas-scavenging-works": ["how-an-anesthesia-machine-performs-a-leak-test", "how-medical-gas-sampling-systems-work", "how-an-anesthesia-machine-breathing-system-works", "how-to-isolate-device-vs-accessory-vs-infrastructure-problems", "medical-device-alarm-troubleshooting-fundamentals"],
    "how-a-ventilator-measures-tidal-volume": ["how-peep-is-generated-and-controlled", "how-ventilator-flow-sensors-work", "how-medical-equipment-measures-flow", "how-ventilator-pressure-sensors-work", "how-to-compare-your-test-result-to-manufacturer-specification"],
    "how-peep-is-generated-and-controlled": ["how-ventilator-pressure-sensors-work", "how-a-ventilator-measures-tidal-volume", "how-ventilator-flow-sensors-work", "how-medical-equipment-measures-pressure", "medical-device-alarm-troubleshooting-fundamentals"],
    "how-infusion-pump-occlusion-detection-works": ["how-infusion-pumps-measure-or-control-flow", "how-medical-equipment-measures-pressure", "sensors-and-transducers-basics", "medical-device-alarm-troubleshooting-fundamentals", "how-to-troubleshoot-medical-device-accessories"],
    "how-infusion-pumps-measure-or-control-flow": ["how-infusion-pump-occlusion-detection-works", "how-medical-equipment-measures-flow", "how-to-compare-your-test-result-to-manufacturer-specification", "how-to-troubleshoot-medical-device-accessories", "how-to-read-device-specifications"],
    "how-defibrillators-charge-and-deliver-energy": ["voltage-current-resistance-and-continuity-in-plain-english", "fuses-breakers-and-power-supplies-in-medical-equipment", "medical-equipment-cables-and-connectors-inspection-and-isolation", "how-to-troubleshoot-charging-problems", "how-to-verify-a-repair-before-returning-equipment-to-service"],
    "how-medical-device-batteries-charge-and-communicate": ["how-smart-batteries-communicate-with-medical-equipment", "medical-device-batteries-runtime-capacity-and-state-of-health", "medical-equipment-battery-basics", "how-to-troubleshoot-charging-problems", "medical-equipment-cables-and-connectors-inspection-and-isolation"],
    "how-smart-batteries-communicate-with-medical-equipment": ["how-medical-device-batteries-charge-and-communicate", "medical-device-batteries-runtime-capacity-and-state-of-health", "how-to-troubleshoot-communication-failures", "medical-equipment-cables-and-connectors-inspection-and-isolation", "software-firmware-and-configuration-problems-in-medical-equipment"],
    "how-parameter-modules-communicate-with-host-monitors": ["how-mainstream-co2-monitoring-works", "how-patient-monitors-communicate-with-central-stations", "how-to-troubleshoot-communication-failures", "medical-equipment-cables-and-connectors-inspection-and-isolation", "how-ecg-acquisition-works"],
    "how-patient-monitors-communicate-with-central-stations": ["basic-networking-for-medical-equipment", "how-to-troubleshoot-communication-failures", "hospital-emrs-and-medical-device-integration", "how-parameter-modules-communicate-with-host-monitors", "medical-equipment-cables-and-connectors-inspection-and-isolation"],
    "how-ecg-lead-off-detection-works": ["how-ecg-acquisition-works", "medical-equipment-cables-and-connectors-inspection-and-isolation", "how-to-troubleshoot-medical-device-accessories", "how-parameter-modules-communicate-with-host-monitors", "medical-device-alarm-troubleshooting-fundamentals"],
    "how-mainstream-co2-monitoring-works": ["how-sidestream-co2-monitoring-works", "how-to-troubleshoot-medical-device-accessories", "how-parameter-modules-communicate-with-host-monitors", "how-an-anesthesia-machine-breathing-system-works", "medical-device-alarm-troubleshooting-fundamentals"],
    "how-medical-gas-sampling-systems-work": ["how-sidestream-co2-monitoring-works", "how-mainstream-co2-monitoring-works", "how-an-anesthesia-machine-breathing-system-works", "how-anesthesia-waste-gas-scavenging-works", "how-to-troubleshoot-medical-device-accessories"],
    "how-an-anesthesia-machine-performs-a-leak-test": ["how-an-anesthesia-machine-breathing-system-works", "how-anesthesia-waste-gas-scavenging-works", "how-medical-equipment-measures-pressure", "how-medical-gas-sampling-systems-work", "how-to-verify-a-repair-before-returning-equipment-to-service"],
    "how-to-become-a-biomedical-equipment-technician": ["biomed-bmet-clinical-engineering-htm", "biomed-resume-basics", "voltage-current-resistance-and-continuity-in-plain-english", "basic-networking-for-medical-equipment", "how-to-read-a-medical-equipment-service-manual"],
    "what-degree-do-you-need-to-become-a-biomed": ["how-to-become-a-biomedical-equipment-technician", "biomed-bmet-clinical-engineering-htm", "biomed-resume-basics", "voltage-current-resistance-and-continuity-in-plain-english", "basic-networking-for-medical-equipment"],
    "what-entry-level-biomeds-should-learn-first": ["how-to-become-a-biomedical-equipment-technician", "what-degree-do-you-need-to-become-a-biomed", "the-troubleshooting-process-observe-isolate-test-verify", "how-to-use-a-multimeter-in-biomed", "how-to-read-a-medical-equipment-service-manual"],
    "what-electronics-knowledge-does-a-biomed-actually-need": ["voltage-current-resistance-and-continuity-in-plain-english", "how-to-use-a-multimeter-in-biomed", "ac-vs-dc-power-basics", "fuses-breakers-and-power-supplies-in-medical-equipment", "analog-vs-digital-signals"],
}

ARTICLE_CONFIG = {
    "when-to-remove-medical-equipment-from-service": {
        "description": "A practical guide to deciding when medical equipment should be removed from clinical service and what must be verified before it is returned.",
        "category": "Safety & Risk",
        "badge": "Core Concept",
        "cardNote": "Removal and return-to-service decisions",
    },
    "how-to-think-before-calling-a-vendor": {
        "description": "A practical guide to gathering evidence, narrowing symptoms, and preparing for a productive medical-equipment vendor support call.",
        "category": "Troubleshooting",
        "badge": "Core Concept",
        "cardNote": "Vendor escalation and support-call basics",
    },
    "what-hl7-means-in-plain-english": {
        "description": "A practical introduction to HL7 messages, ADT and ORU workflows, interface engines, acknowledgements, and medical-device data exchange.",
        "category": "Integration",
        "badge": "Core Concept",
        "cardNote": "Device data and messaging basics",
    },
    "nurse-call-integration-basics": {
        "description": "A practical introduction to nurse call interfaces, contact closures, alarm signals, cables, room connections, and common failure patterns.",
        "category": "Integration",
        "badge": "Core Concept",
        "cardNote": "Alarm and nurse call interface basics",
    },
    "how-to-read-a-medical-equipment-service-manual": {
        "description": "A practical guide to finding troubleshooting steps, warnings, diagrams, specifications, service modes, parts, and verification procedures in medical-equipment manuals.",
        "category": "Troubleshooting",
        "badge": "Core Skill",
        "cardNote": "Service documentation and manual navigation",
    },
    "how-to-reproduce-a-clinical-complaint-on-the-bench": {
        "description": "A practical guide to recreating clinical failure conditions, isolating intermittent problems, using original accessories, and documenting meaningful bench testing.",
        "category": "Troubleshooting",
        "badge": "Core Skill",
        "cardNote": "Complaint reproduction and bench testing",
    },
    "how-to-use-a-multimeter-in-biomed": {
        "description": "A practical introduction to measuring voltage, resistance, and continuity safely while troubleshooting medical equipment.",
        "category": "Testing & Verification",
        "badge": "Core Skill",
        "cardNote": "Multimeter safety and measurement basics",
    },
    "what-known-good-actually-means": {
        "description": "A practical guide to validating known-good parts, accessories, test equipment, and comparison devices before relying on substitution testing.",
        "category": "Troubleshooting",
        "badge": "Core Concept",
        "cardNote": "Reliable substitution testing",
    },
    "fuses-breakers-and-power-supplies-in-medical-equipment": {
        "description": "A practical introduction to fuses, circuit breakers, power supplies, and the common power-path failures found in medical equipment.",
        "category": "Testing & Verification",
        "badge": "Core Concept",
        "cardNote": "Power protection and supply basics",
        "plannedTitles": ["Fuses, Breakers, and Power Supplies"],
    },
    "voltage-current-resistance-and-continuity-in-plain-english": {
        "description": "A plain-English introduction to voltage, current, resistance, and continuity for medical-equipment troubleshooting.",
        "category": "Testing & Verification",
        "badge": "Core Concept",
        "cardNote": "Essential electrical concepts",
    },
    "sensors-and-transducers-basics": {
        "description": "A practical introduction to how medical devices convert pressure, flow, temperature, light, force, and other physical conditions into usable signals.",
        "category": "Testing & Verification",
        "badge": "Core Concept",
        "cardNote": "Sensor signals and measurement basics",
    },
    "relays-and-contact-closures-in-plain-english": {
        "description": "A practical introduction to relays, dry contacts, normally open and normally closed circuits, and their use in alarms, nurse call, and equipment control.",
        "category": "Testing & Verification",
        "badge": "Core Concept",
        "cardNote": "Relay and contact-closure basics",
    },
    "preserving-device-logs-after-a-serious-event": {
        "description": "A practical guide to protecting device logs, alarm histories, configurations, timestamps, and other electronic evidence after a serious clinical event.",
        "category": "Safety & Risk",
        "badge": "Incident Response",
        "cardNote": "Electronic evidence preservation",
    },
    "what-to-do-when-a-medical-device-is-involved-in-an-incident": {
        "description": "A practical guide for biomeds when medical equipment may have been involved in patient harm, injury, or another serious clinical event.",
        "category": "Safety & Risk",
        "badge": "Incident Response",
        "cardNote": "Device incident handling basics",
    },
    "how-to-avoid-confirmation-bias-while-troubleshooting": {
        "description": "A practical guide to challenging first impressions, separating evidence from assumptions, and avoiding premature conclusions during medical-equipment troubleshooting.",
        "category": "Troubleshooting",
        "badge": "Core Skill",
        "cardNote": "Evidence-based troubleshooting decisions",
    },
    "when-to-trust-the-device-s-internal-self-test": {
        "description": "A practical guide to understanding what medical-device self-tests prove, what they can miss, and when independent verification is still required.",
        "category": "Testing & Verification",
        "badge": "Core Concept",
        "cardNote": "Self-test limits and verification basics",
    },
    "why-changing-one-thing-at-a-time-matters": {
        "description": "A practical guide to controlling variables, preserving diagnostic evidence, and learning what actually fixed a medical-equipment problem.",
        "category": "Troubleshooting",
        "badge": "Core Skill",
        "cardNote": "Controlled troubleshooting and isolation",
    },
    "ground-neutral-and-hot-in-medical-equipment": {
        "description": "A practical explanation of hot, neutral, and protective ground conductors in AC-powered medical equipment and why their roles must remain distinct.",
        "category": "Testing & Verification",
        "badge": "Core Concept",
        "cardNote": "AC conductors and protective grounding",
    },
    "error-codes-what-they-tell-you-and-what-they-don-t": {
        "description": "A practical guide to interpreting medical-device error codes as diagnostic clues without mistaking the detected condition for the root cause.",
        "category": "Troubleshooting",
        "badge": "Core Skill",
        "cardNote": "Error-code interpretation and diagnosis",
    },
    "what-unable-to-duplicate-should-actually-mean": {
        "description": "A practical guide to investigating, testing, and documenting intermittent medical-equipment complaints that cannot be reproduced on the bench.",
        "category": "Troubleshooting",
        "badge": "Core Skill",
        "cardNote": "Intermittent-fault testing and documentation",
    },
    "medical-equipment-cables-and-connectors-inspection-and-isolation": {
        "description": "A practical guide to inspecting and isolating cable, connector, strain-relief, and pin failures before replacing expensive medical-device components.",
        "category": "Troubleshooting",
        "badge": "Core Skill",
        "cardNote": "Cable and connector fault isolation",
        "plannedTitles": ["Connectors, Pins, and Strain Relief"],
    },
    "how-to-troubleshoot-medical-device-accessories": {
        "description": "A practical guide to determining whether a medical-equipment problem follows a sensor, cable, module, probe, hose, battery, or other accessory.",
        "category": "Troubleshooting",
        "badge": "Core Skill",
        "cardNote": "Accessory and host-device fault isolation",
    },
    "how-to-isolate-device-vs-accessory-vs-infrastructure-problems": {
        "description": "A practical guide to determining whether a medical-equipment failure belongs to the device, an attached accessory, or the hospital infrastructure around it.",
        "category": "Troubleshooting",
        "badge": "Core Skill",
        "cardNote": "Device, accessory, and infrastructure isolation",
    },
    "medical-equipment-power-troubleshooting-outlet-to-internal-supply": {
        "description": "A practical guide to tracing no-power, charging, shutdown, and AC-input problems from the outlet through the internal medical-device power system.",
        "category": "Testing & Verification",
        "badge": "Core Skill",
        "cardNote": "End-to-end power-path troubleshooting",
        "plannedTitles": ["How to Troubleshoot a Device That Will Not Power On"],
    },
    "medical-device-alarm-troubleshooting-fundamentals": {
        "description": "A practical guide to separating alarm conditions, measurement errors, alarm-logic problems, and failed audible, visual, or remote notifications.",
        "category": "Testing & Verification",
        "badge": "Core Skill",
        "cardNote": "Alarm detection and notification testing",
        "plannedTitles": ["Alarm troubleshooting basics"],
    },
    "environmental-causes-of-medical-equipment-failures": {
        "description": "A practical guide to recognizing how heat, moisture, power, movement, cleaning, gas supply, and clinical conditions contribute to medical-equipment failures.",
        "category": "Troubleshooting",
        "badge": "Core Concept",
        "cardNote": "Environmental and location-based failure patterns",
    },
    "software-firmware-and-configuration-problems-in-medical-equipment": {
        "description": "A practical guide to recognizing software, firmware, version, and configuration problems that can make healthy medical-device hardware appear defective.",
        "category": "Troubleshooting",
        "badge": "Core Concept",
        "cardNote": "Software layers and configuration isolation",
        "plannedTitles": ["Software, Firmware, and Configuration: What's the Difference?"],
    },
    "how-to-read-and-use-medical-device-event-logs": {
        "description": "A practical guide to turning medical-device alarms, errors, resets, timestamps, and event history into useful troubleshooting evidence.",
        "category": "Troubleshooting",
        "badge": "Core Skill",
        "cardNote": "Event-log timelines and fault correlation",
        "plannedTitles": ["Medical Device Logs: What to Look For"],
    },
    "how-to-verify-a-repair-before-returning-equipment-to-service": {
        "description": "A practical guide to proving the original medical-equipment problem is fixed, completing required verification, and documenting return-to-service evidence.",
        "category": "Testing & Verification",
        "badge": "Core Skill",
        "cardNote": "Post-repair and return-to-service verification",
        "plannedTitles": ["How to Prove a Repair Before Return to Service"],
    },
    "how-to-troubleshoot-communication-failures": {
        "description": "A practical guide to finding where communication stops between a medical device, accessory, physical link, network, server, application, or connected system.",
        "category": "Integration",
        "badge": "Core Skill",
        "cardNote": "End-to-end communication path isolation",
    },
    "how-to-troubleshoot-charging-problems": {
        "description": "A practical guide to isolating charging failures among the battery, contacts, adapter, dock, power supply, software, and medical-device power-management circuitry.",
        "category": "Testing & Verification",
        "badge": "Core Skill",
        "cardNote": "Battery and charging-path fault isolation",
    },
    "the-troubleshooting-process-observe-isolate-test-verify": {
        "description": "A practical four-step framework for observing symptoms, isolating the failure, testing suspected causes, and verifying medical-equipment repairs.",
        "category": "Troubleshooting",
        "badge": "Start Here",
        "cardNote": "Observe, isolate, test, and verify",
    },
    "the-difference-between-a-symptom-cause-and-root-cause": {
        "description": "A practical guide to separating observed medical-equipment symptoms, direct causes, contributing factors, and evidence-supported root causes.",
        "category": "Troubleshooting",
        "badge": "Core Concept",
        "cardNote": "Symptom, cause, and root-cause distinctions",
    },
    "how-experienced-biomeds-think-through-a-new-problem": {
        "description": "A practical guide to approaching unfamiliar medical equipment by recognizing patterns, narrowing systems, choosing useful tests, and escalating with evidence.",
        "category": "Troubleshooting",
        "badge": "Start Here",
        "cardNote": "A practical mindset for unfamiliar problems",
    },
    "how-to-read-a-troubleshooting-flowchart": {
        "description": "A practical guide to following troubleshooting trees, evaluating decision points, respecting test conditions, and understanding what each branch proves.",
        "category": "Troubleshooting",
        "badge": "Core Skill",
        "cardNote": "Flowchart decisions and test logic",
    },
    "ac-vs-dc-power-basics": {
        "description": "A practical introduction to AC and DC power, conversion, polarity, voltage rails, adapters, batteries, and common medical-equipment power paths.",
        "category": "Testing & Verification",
        "badge": "Core Concept",
        "cardNote": "AC, DC, conversion, and polarity basics",
    },
    "analog-vs-digital-signals": {
        "description": "A practical introduction to analog and digital signals, conversion, noise, sampling, logic, and signal-path troubleshooting in medical equipment.",
        "category": "Testing & Verification",
        "badge": "Core Concept",
        "cardNote": "Signal types, conversion, and fault patterns",
    },
    "medical-device-batteries-runtime-capacity-and-state-of-health": {
        "description": "A practical guide to battery state of charge, capacity, state of health, internal resistance, load behavior, smart-battery data, and runtime testing.",
        "category": "Testing & Verification",
        "badge": "Core Skill",
        "cardNote": "Battery health and runtime evaluation",
    },
    "how-to-read-device-specifications": {
        "description": "A practical guide to interpreting medical-device accuracy, tolerance, range, resolution, units, test conditions, and pass/fail specifications.",
        "category": "Testing & Verification",
        "badge": "Core Skill",
        "cardNote": "Specifications, conditions, and test limits",
    },
    "tolerance-vs-accuracy": {
        "description": "A practical guide to distinguishing measurement accuracy from allowable tolerance and calculating defensible pass/fail limits for medical equipment.",
        "category": "Testing & Verification",
        "badge": "Core Concept",
        "cardNote": "Accuracy, tolerance, and pass/fail math",
    },
    "how-to-compare-your-test-result-to-manufacturer-specification": {
        "description": "A practical workflow for matching test conditions, calculating acceptable ranges, comparing analyzer results, and making defensible pass/fail decisions.",
        "category": "Testing & Verification",
        "badge": "Core Skill",
        "cardNote": "From measured result to pass/fail decision",
    },
    "pass-fail-limits-and-why-the-test-point-matters": {
        "description": "A practical guide to test-point-specific limits, multi-point testing, range-dependent errors, operating conditions, and defensible pass/fail decisions.",
        "category": "Testing & Verification",
        "badge": "Core Skill",
        "cardNote": "Test points, limits, and range behavior",
    },
    "how-nibp-works-in-a-patient-monitor": {
        "description": "A practical explanation of how cuffs, pumps, valves, pressure sensors, oscillations, and software work together during an NIBP measurement.",
        "category": "How It Works",
        "badge": "Patient Monitoring",
        "cardNote": "The NIBP pneumatic and measurement path",
    },
    "how-spo2-measurement-works": {
        "description": "A practical explanation of how pulse oximetry uses red and infrared light, pulsatile absorption, photodetection, and signal processing to estimate SpO2.",
        "category": "How It Works",
        "badge": "Patient Monitoring",
        "cardNote": "The optical SpO2 measurement path",
    },
    "how-ecg-acquisition-works": {
        "description": "A practical explanation of how electrodes, lead wires, differential inputs, amplification, filtering, conversion, and software produce an ECG waveform.",
        "category": "How It Works",
        "badge": "Patient Monitoring",
        "cardNote": "The ECG signal-acquisition path",
    },
    "how-sidestream-co2-monitoring-works": {
        "description": "A practical explanation of how sampling lines, water traps, pumps, infrared measurement, zeroing, and software produce EtCO2 values and capnograms.",
        "category": "How It Works",
        "badge": "Gas Monitoring",
        "cardNote": "The sidestream capnography sampling path",
    },
    "how-ventilator-flow-sensors-work": {
        "description": "A practical explanation of how ventilators measure gas movement and how flow-sensor problems affect tidal volume, alarms, triggering, leaks, and calibration.",
        "category": "How It Works",
        "badge": "Ventilation",
        "cardNote": "The ventilator flow-measurement path",
    },
    "how-ventilator-pressure-sensors-work": {
        "description": "A practical explanation of how ventilators measure airway pressure and how pressure-sensor problems affect alarms, PEEP, triggering, and delivered ventilation.",
        "category": "How It Works",
        "badge": "Ventilation",
        "cardNote": "The ventilator pressure-measurement path",
    },
    "how-medical-equipment-measures-pressure": {
        "description": "A practical explanation of how pressure sensors turn force from gas or fluid into electrical signals that medical equipment can display, control, and alarm on.",
        "category": "How It Works",
        "badge": "Measurement",
        "cardNote": "The pressure-to-signal measurement path",
    },
    "how-medical-equipment-measures-flow": {
        "description": "A practical explanation of how medical devices detect moving gas or liquid and turn that movement into values used for display, control, and alarms.",
        "category": "How It Works",
        "badge": "Measurement",
        "cardNote": "The flow-to-signal measurement path",
    },
    "how-invasive-blood-pressure-monitoring-works": {
        "description": "A practical explanation of how a fluid-filled pressure line and transducer turn arterial pressure into an electrical waveform on a patient monitor.",
        "category": "How It Works",
        "badge": "Patient Monitoring",
        "cardNote": "The fluid-filled invasive pressure path",
    },
    "how-oxygen-sensors-work-in-ventilators-and-anesthesia-machines": {
        "description": "A practical explanation of how ventilators and anesthesia machines measure oxygen concentration and why sensor age, calibration, gas flow, and sample location matter.",
        "category": "How It Works",
        "badge": "Gas Monitoring",
        "cardNote": "The oxygen measurement and calibration path",
    },
    "how-an-anesthesia-machine-breathing-system-works": {
        "description": "A practical explanation of how fresh gas, one-way valves, the breathing circuit, CO2 absorber, reservoir bag, and ventilator work together.",
        "category": "How It Works",
        "badge": "Anesthesia",
        "cardNote": "The anesthesia circle breathing-system path",
    },
    "how-anesthesia-waste-gas-scavenging-works": {
        "description": "A practical explanation of how excess anesthetic gas leaves the breathing system without allowing suction or backpressure to disturb the patient circuit.",
        "category": "How It Works",
        "badge": "Anesthesia",
        "cardNote": "The waste-gas disposal and isolation path",
    },
    "how-a-ventilator-measures-tidal-volume": {
        "description": "A practical explanation of how ventilators turn flow over time into delivered and exhaled volume, including leaks, compliance, and measurement location.",
        "category": "How It Works",
        "badge": "Ventilation",
        "cardNote": "The flow-to-tidal-volume calculation path",
    },
    "how-peep-is-generated-and-controlled": {
        "description": "A practical explanation of how ventilators maintain positive pressure at end expiration and how valves, flow, sensors, leaks, and control loops affect PEEP.",
        "category": "How It Works",
        "badge": "Ventilation",
        "cardNote": "The end-expiratory pressure control loop",
    },
    "how-infusion-pump-occlusion-detection-works": {
        "description": "A practical explanation of how infusion pumps detect rising pressure or force and decide when to stop delivery and generate an occlusion alarm.",
        "category": "How It Works",
        "badge": "Infusion",
        "cardNote": "The infusion pressure and occlusion-alarm path",
    },
    "how-infusion-pumps-measure-or-control-flow": {
        "description": "A practical explanation of how infusion pumps turn motor movement into fluid delivery and why programmed rate can differ from measured output.",
        "category": "How It Works",
        "badge": "Infusion",
        "cardNote": "The motor-to-fluid-delivery control path",
    },
    "how-defibrillators-charge-and-deliver-energy": {
        "description": "A practical explanation of how defibrillators store high voltage, shape and deliver a shock, and verify that delivered energy matches the selected value.",
        "category": "How It Works",
        "badge": "Defibrillation",
        "cardNote": "The high-voltage charge and discharge path",
    },
    "how-medical-device-batteries-charge-and-communicate": {
        "description": "A practical explanation of how chargers, protection circuits, battery-management electronics, and smart-battery communication work together.",
        "category": "How It Works",
        "badge": "Power & Batteries",
        "cardNote": "The smart-battery charging and communication path",
    },
    "how-smart-batteries-communicate-with-medical-equipment": {
        "description": "A practical explanation of how smart batteries report charge, temperature, capacity, faults, and identification data to medical equipment.",
        "category": "How It Works",
        "badge": "Power & Batteries",
        "cardNote": "The smart-battery data and host-interface path",
    },
    "how-parameter-modules-communicate-with-host-monitors": {
        "description": "A practical explanation of how removable parameter modules receive power, identify themselves, exchange data, and appear on patient monitors.",
        "category": "How It Works",
        "badge": "Patient Monitoring",
        "cardNote": "The parameter-module power and data path",
    },
    "how-patient-monitors-communicate-with-central-stations": {
        "description": "A practical explanation of how bedside monitors send waveforms, numerics, alarms, and patient information to central stations across the network.",
        "category": "How It Works",
        "badge": "Connectivity",
        "cardNote": "The bedside-to-central monitoring path",
    },
    "how-ecg-lead-off-detection-works": {
        "description": "A practical explanation of how patient monitors detect disconnected electrodes and broken lead wires, and how to isolate an invalid ECG path.",
        "category": "How It Works",
        "badge": "Patient Monitoring",
        "cardNote": "The ECG electrode and lead-off detection path",
    },
    "how-mainstream-co2-monitoring-works": {
        "description": "A practical explanation of how mainstream capnography measures CO2 at the airway and how adapters, optics, moisture, alignment, and sensor recognition affect readings.",
        "category": "How It Works",
        "badge": "Gas Monitoring",
        "cardNote": "The mainstream capnography optical path",
    },
    "how-medical-gas-sampling-systems-work": {
        "description": "A practical explanation of how medical gas systems transport a sample through tubing, moisture protection, pumps, analyzers, and exhaust or return paths.",
        "category": "How It Works",
        "badge": "Gas Monitoring",
        "cardNote": "The respiratory-gas sampling and analysis path",
    },
    "how-an-anesthesia-machine-performs-a-leak-test": {
        "description": "A practical explanation of how anesthesia machines pressurize or evacuate defined system volumes, measure pressure behavior, and identify excessive leakage.",
        "category": "How It Works",
        "badge": "Anesthesia",
        "cardNote": "Anesthesia leak-test boundaries and isolation",
    },
    "how-to-become-a-biomedical-equipment-technician": {
        "description": "A practical, plain-English guide to entering the biomed profession, building useful technical knowledge, and developing a career working on medical equipment.",
        "category": "Career",
        "badge": "Career Guide",
        "cardNote": "Education, skills, and entry-level career paths",
    },
    "what-degree-do-you-need-to-become-a-biomed": {
        "description": "A practical guide to BMET degrees, electronics programs, military training, certificates, and other educational paths into the biomed profession.",
        "category": "Career",
        "badge": "Education Guide",
        "cardNote": "Degrees, training, and entry paths for future biomeds",
    },
    "what-entry-level-biomeds-should-learn-first": {
        "description": "A practical learning order for new biomeds covering troubleshooting, electronics, test equipment, documentation, networking, and safe repair verification.",
        "category": "Career",
        "badge": "Career Guide",
        "cardNote": "Core skills and priorities for entry-level biomeds",
    },
    "what-electronics-knowledge-does-a-biomed-actually-need": {
        "description": "A practical guide to the electronics concepts biomeds actually use when troubleshooting medical equipment, from voltage and resistance to sensors and signals.",
        "category": "Career",
        "badge": "Education Guide",
        "cardNote": "Practical electronics knowledge for biomed troubleshooting",
    },
}


def inline(value: str) -> str:
    value = html.escape(value.strip(), quote=False)
    value = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"(?<!\*)\*(.+?)\*(?!\*)", r"<em>\1</em>", value)
    return value


def split_article(body: str) -> tuple[str, str, list[tuple[str, list[str]]]]:
    lines = body.splitlines()
    subtitle = ""
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].startswith("## "):
        subtitle = lines.pop(0)[3:].strip()
    while lines and not lines[0].strip():
        lines.pop(0)
    intro = ""
    intro_lines = []
    while lines and not re.match(r"^#{1,2} ", lines[0]):
        if lines[0].strip():
            intro_lines.append(lines[0].strip())
        elif intro_lines:
            break
        lines.pop(0)
    intro = " ".join(intro_lines)
    sections: list[tuple[str, list[str]]] = []
    current_title = ""
    current_lines: list[str] = []
    for line in lines:
        match = re.match(r"^#{1,2} (.+)$", line)
        if match:
            if current_title:
                sections.append((current_title, current_lines))
            current_title, current_lines = match.group(1).strip(), []
        elif current_title:
            current_lines.append(line)
    if current_title:
        sections.append((current_title, current_lines))
    return subtitle, intro, sections


def render_lines(lines: list[str]) -> str:
    out: list[str] = []
    paragraph: list[str] = []
    list_kind = ""

    def flush_paragraph() -> None:
        if paragraph:
            out.append(f"    <p>{inline(' '.join(paragraph))}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_kind
        if list_kind:
            out.append(f"    </{list_kind}>")
            list_kind = ""

    for raw in lines + [""]:
        line = raw.strip()
        if line.startswith("### "):
            flush_paragraph(); close_list()
            out.append(f"    <h4>{inline(line[4:])}</h4>")
        elif re.match(r"^[-*]\s+", line):
            flush_paragraph()
            if list_kind != "ul":
                close_list(); list_kind = "ul"; out.append("    <ul>")
            out.append(f"      <li>{inline(re.sub(r'^[-*]\s+', '', line))}</li>")
        elif re.match(r"^\d+\.\s+", line):
            flush_paragraph()
            if list_kind != "ol":
                close_list(); list_kind = "ol"; out.append("    <ol>")
            out.append(f"      <li>{inline(re.sub(r'^\d+\.\s+', '', line))}</li>")
        elif line.startswith("> "):
            flush_paragraph(); close_list()
            out.append(f"    <blockquote><p>{inline(line[2:])}</p></blockquote>")
        elif not line:
            flush_paragraph(); close_list()
        else:
            close_list(); paragraph.append(line)
    return "\n".join(out)


def related_section(slug: str, titles: dict[str, str]) -> str:
    items = "\n".join(
        f'      <li><a href="{target}.html">{html.escape(titles[target])}</a></li>'
        for target in RELATED[slug]
    )
    return f'''  <section class="content-box">
    <h3>Related Biomed Basics</h3>
    <ul>
{items}
    </ul>
    <div class="hero-buttons" style="margin-top:20px; margin-bottom:0;">
      <a href="../biomed-basics.html" class="hero-button">Back to Biomed Basics</a>
    </div>
  </section>'''


def page_html(title: str, subtitle: str, description: str, hero_intro: str, sections: list[tuple[str, list[str]]], titles: dict[str, str]) -> str:
    slug = slugify(title)
    jump_targets = [(heading, slugify(heading)) for heading, _ in sections if heading not in {"Jump to a Section", "Important Note"}]
    rendered = []
    for heading, lines in sections:
        if heading == "Jump to a Section":
            labels = [re.sub(r"^[-*]\s+", "", line.strip()) for line in lines if re.match(r"^[-*]\s+", line.strip())]
            links = "\n".join(f'      <li><a href="#{slugify(label)}">{html.escape(label)}</a></li>' for label in labels)
            rendered.append(f'  <section class="content-box">\n    <h3>Jump to a Section</h3>\n    <ul>\n{links}\n    </ul>\n  </section>')
            continue
        rendered.append(f'  <section class="content-box" id="{slugify(heading)}">\n    <h3>{html.escape(heading)}</h3>\n{render_lines(lines)}\n  </section>')
    rendered.append(related_section(slug, titles))
    body = "\n\n".join(rendered)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{html.escape(title)} | Jake Troubleshoots</title>
  <meta name="description" content="{html.escape(description, quote=True)}">
  <link rel="stylesheet" href="../style.css">
  <link rel="icon" type="image/x-icon" href="../images/favicon.ico">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-1L34E3TJL6"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-1L34E3TJL6');</script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js?client=ca-pub-8569368568902704" crossorigin="anonymous"></script>
  <link rel="canonical" href="{SITE_URL}/biomed-basics/{slug}.html" />
  <script src="../social-links.js" defer></script>
</head>
<body class="biomed-article">
<header>
  <a href="../index.html" class="site-logo"><img src="../images/logo.png" alt="Jake Troubleshoots Logo" class="site-icon"><span class="logo-text">Jake Troubleshoots</span></a>
  <nav><a href="../index.html">Home</a><a href="../guides.html">Guides</a><a href="../search.html">Search</a><a href="../preventive-maintenance.html">PMs</a><a href="../vendors.html">Vendors</a><a href="../contact.html">About</a></nav>
</header>
<section class="hero">
  <h2>{html.escape(title)}</h2>
  <p>{html.escape(subtitle)}</p>
  <p style="max-width:760px; margin:10px auto 0; font-size:0.95em;">{html.escape(hero_intro)}</p>
  <div class="hero-buttons" style="margin-top:20px; display:flex; justify-content:center; gap:12px; flex-wrap:wrap;"><a href="../biomed-basics.html" class="hero-button">Back to Biomed Basics</a></div>
</section>
<main>
{body}
</main>
<footer>
  <p>Contact: <a href="mailto:contact@jaketroubleshoots.com" style="color:#8fff00;">contact@jaketroubleshoots.com</a></p>
  <p><a href="../privacy-policy.html">Privacy Policy</a> &nbsp;|&nbsp; <a href="../terms-of-use.html">Terms of Use</a></p>
  <p>Guides intended for trained personnel only.</p><p>© 2026 Jake Troubleshoots</p>
</footer>
</body>
</html>
'''


def title_map(root: Path, new_titles: list[str]) -> dict[str, str]:
    titles = {slugify(title): title for title in new_titles}
    for path in (root / "biomed-basics").glob("*.html"):
        source = path.read_text(encoding="utf-8")
        match = re.search(r"<h2\b[^>]*>(.*?)</h2>", source, re.I | re.S)
        titles[path.stem] = re.sub(r"<[^>]+>", "", match.group(1)).strip() if match else path.stem.replace("-", " ").title()
    return titles


def parse_batch(path: Path) -> list:
    source = path.read_text(encoding="utf-8")
    source_lines = source.splitlines()
    reviewed_start = next(
        (index for index, line in enumerate(source_lines) if slugify(line.strip()) in ARTICLE_CONFIG),
        None,
    )
    if reviewed_start is not None:
        source = "\n".join(source_lines[reviewed_start:])
    chunks = re.split(r"\n\s*---\s*\n(?=#\s+)", source)
    articles = []
    with tempfile.TemporaryDirectory() as directory:
        for index, chunk in enumerate(chunks, 1):
            temporary = Path(directory) / f"article-{index}.md"
            temporary.write_text(chunk.strip() + "\n", encoding="utf-8")
            articles.append(parse_input(temporary))
    return articles


def replace_related(source: str, replacement: str) -> str:
    pattern = re.compile(r'\s*<section class="content-box">\s*<h3>Related Biomed Basics</h3>.*?</section>', re.I | re.S)
    updated, count = pattern.subn("\n\n" + replacement, source, count=1)
    if count != 1:
        raise ValueError("expected exactly one Related Biomed Basics section")
    return updated


def biomed_group(category: str) -> str:
    normalized = category.casefold()
    if "how it works" in normalized:
        return "how-it-works"
    if any(word in normalized for word in ("network", "integration", "imaging", "dicom")):
        return "connected-systems"
    if any(word in normalized for word in ("career", "communication", "terminology")):
        return "career-communication"
    if any(word in normalized for word in ("testing", "electrical")):
        return "start-here"
    if any(word in normalized for word in ("troubleshoot", "safety", "risk")):
        return "troubleshooting-safety"
    return "everyday-skills"


def catalog_entry(title: str, slug: str, config: dict[str, str], existing: dict | None = None) -> dict:
    entry = {
        "title": title,
        "slug": slug,
        "url": f"biomed-basics/{slug}.html",
        "description": config["description"],
        "category": config["category"],
        "group": biomed_group(config["category"]),
        "badge": config["badge"],
        "cardNote": config["cardNote"],
        "lastRevision": (
            existing.get("lastRevision")
            if existing and existing.get("lastRevision")
            else datetime.date.today().isoformat()
        ),
    }
    for key in ("featured", "featuredOrder"):
        if existing and key in existing:
            entry[key] = existing[key]
    return entry


def remove_published_planned_topics(landing: str, published_titles: set[str]) -> str:
    section_pattern = re.compile(
        r'(<section class="content-box planned-topics-section">.*?<h3>Planned Topics</h3>.*?)(</section>\s*</div>\s*</section>)',
        re.S,
    )
    match = section_pattern.search(landing)
    if not match:
        raise SystemExit("Planned Topics section not found")
    normalized_titles = {slugify(title) for title in published_titles}
    cleaned_section = re.sub(
        r'\s*<li>(.*?)</li>',
        lambda item: "" if slugify(html.unescape(re.sub(r"<[^>]+>", "", item.group(1)))) in normalized_titles else item.group(0),
        match.group(1),
        flags=re.S,
    )
    remaining_count = len(re.findall(r'<li>.*?</li>', cleaned_section, re.S))
    cleaned_section = re.sub(
        r'(<div class="planned-topic-count"[^>]*>\s*<strong>)\d+(</strong>)',
        rf'\g<1>{remaining_count}\2',
        cleaned_section,
        count=1,
    )
    cleaned_section = re.sub(
        r'(aria-label=")\d+( planned articles")',
        rf'\g<1>{remaining_count}\2',
        cleaned_section,
        count=1,
    )
    return landing[:match.start()] + cleaned_section + match.group(2) + landing[match.end():]


def atomic_write(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temporary = tempfile.mkstemp(dir=path.parent, prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(data)
        os.replace(temporary, path)
    except Exception:
        Path(temporary).unlink(missing_ok=True)
        raise


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", type=Path, nargs="+")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--confirm-plan")
    args = parser.parse_args()
    articles = [article for input_path in args.inputs for article in parse_batch(input_path)]
    if len({article.slug for article in articles}) != len(articles):
        raise SystemExit("batch contains duplicate article slugs")
    configs = {}
    for article in articles:
        config = ARTICLE_CONFIG.get(article.slug)
        if not config:
            raise SystemExit(f"missing reviewed ARTICLE_CONFIG for {article.slug}")
        configs[article.slug] = config
    titles = title_map(ROOT, [article.title for article in articles])
    if set(titles) != set(RELATED):
        raise SystemExit(f"relationship map mismatch: missing={set(titles)-set(RELATED)}, extra={set(RELATED)-set(titles)}")
    outputs: dict[Path, str] = {}
    targets = {}
    for article in articles:
        subtitle, original_description, sections = split_article(article.body)
        target = ROOT / "biomed-basics" / f"{article.slug}.html"
        targets[article.slug] = target
        outputs[target] = page_html(article.title, subtitle, configs[article.slug]["description"], original_description, sections, titles)
    for slug in RELATED:
        path = ROOT / "biomed-basics" / f"{slug}.html"
        if slug in targets:
            continue
        outputs[path] = replace_related(path.read_text(encoding="utf-8"), related_section(slug, titles))
    catalog_path = ROOT / "data" / "biomed-basics.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    if not isinstance(catalog, list):
        raise SystemExit("data/biomed-basics.json must contain a list")
    catalog_by_slug = {item.get("slug"): item for item in catalog if isinstance(item, dict)}
    if len(catalog_by_slug) != len(catalog):
        raise SystemExit("data/biomed-basics.json contains an invalid or duplicate slug")
    for article in articles:
        catalog_by_slug[article.slug] = catalog_entry(
            article.title, article.slug, configs[article.slug], catalog_by_slug.get(article.slug)
        )
    catalog = sorted(catalog_by_slug.values(), key=lambda item: (item["group"], item["title"].casefold()))
    outputs[catalog_path] = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"

    landing = (ROOT / "biomed-basics.html").read_text(encoding="utf-8")
    published_titles = set(titles.values())
    for config in configs.values():
        published_titles.update(config.get("plannedTitles", []))
    landing = remove_published_planned_topics(landing, published_titles)
    outputs[ROOT / "biomed-basics.html"] = landing
    sitemap_path = ROOT / "sitemap.xml"
    sitemap = sitemap_path.read_text(encoding="utf-8")
    for article in articles:
        article_href = f"biomed-basics/{article.slug}.html"
        canonical = f"{SITE_URL}/{article_href}"
        if sitemap.count(canonical) == 0:
            next_entry = f"<url>\n<loc>{SITE_URL}/biomed-basics.html</loc>\n</url>"
            compact_entry = f"<url><loc>{SITE_URL}/biomed-basics.html</loc></url>"
            if next_entry in sitemap:
                addition = f"<url>\n<loc>{canonical}</loc>\n</url>\n"
                sitemap = sitemap.replace(next_entry, addition + next_entry, 1)
            elif compact_entry in sitemap:
                addition = f"<url><loc>{canonical}</loc></url>"
                sitemap = sitemap.replace(compact_entry, compact_entry + addition, 1)
            else:
                raise SystemExit("expected Biomed Basics sitemap insertion point not found")
        elif sitemap.count(canonical) != 1:
            raise SystemExit("new article canonical appears more than once in sitemap")
    outputs[sitemap_path] = sitemap
    digest_input = "".join(
        f"{path.relative_to(ROOT).as_posix()}\0{data}\0"
        for path, data in sorted(outputs.items(), key=lambda item: item[0].as_posix())
    )
    digest = hashlib.sha256(digest_input.encode("utf-8")).hexdigest()
    print("Biomed Basics publication plan")
    for path in outputs:
        print(f"  {'CREATE' if not path.exists() else 'UPDATE'} {path.relative_to(ROOT)}")
    print(f"Plan digest: {digest}")
    if not args.write:
        print("DRY RUN — NO FILES WRITTEN")
        return 0
    if args.confirm_plan != digest:
        raise SystemExit("--write requires --confirm-plan with the complete current dry-run digest")
    for path, data in outputs.items():
        atomic_write(path, data)
    print(f"WROTE {len(outputs)} FILES")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
