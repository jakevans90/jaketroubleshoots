---
schemaVersion: 1
title: "LivaNova S5 Heart-Lung Machine - Bubble Detector Alarm or Detector Test Failure"
issueTitle: "Bubble Detector Alarm or Detector Test Failure"
description: "Troubleshoots bubble detector alarms and failed detector checks by examining sensor placement, tubing compatibility, contamination, connections, and configuration."
assetType: "Heart-Lung Machine"
manufacturer: "LivaNova"
model: "S5"
slug: "livanova-s5-bubble-detector-alarm-or-detector-test-failure"
dateAdded: "2026-09-15"
taxonomyMode: "reuse"
ccr:
  complaint: "Perfusion reported repeated S5 bubble detector alarms during pre-case setup with no bubble visible in the test circuit."
  cause: "Clinical Engineering found the tubing was only partially seated in the detector sensing channel."
  resolution: "Clinical Engineering correctly seated the tubing and verified normal detector recognition and successful approved alarm testing."
helpfulDetails:
  - "Detector/channel affected"
  - "Exact alarm message"
  - "Tubing type and position"
  - "Sensor cleanliness"
  - "Cable condition"
  - "Whether alarm changes with cable movement"
  - "Known-good substitutions"
  - "Functional test result"
  - "Whether the problem followed the circuit or detector"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots bubble detector alarms and failed detector checks by examining sensor placement, tubing compatibility, contamination, connections, and configuration.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Treat the Alarm as Valid

Do not assume a bubble detector alarm is false during patient support. Follow the perfusion protocol immediately and ensure the circuit is safe before investigating the equipment.

Do not bypass or disable a bubble detector to continue clinical use.

**Expected outcome:** Patient protection is maintained and the alarm is managed clinically before technical troubleshooting begins.

Once the affected detector is no longer required for active patient support, troubleshooting may continue.

### 2. Confirm the Exact Detector Problem

Determine whether the issue is:

- A bubble alarm with no visible bubble
- Failure of a detector self-test or functional test
- Detector not recognized
- Intermittent alarm
- Alarm only when tubing is moved
- Alarm after changing tubing or circuit setup

Record any message exactly as displayed.

**Expected outcome:** The detector problem is clearly characterized and reproducible.

If the detector subsequently passes repeated approved testing with the correct setup, troubleshooting can stop.

### 3. Inspect Tubing Position in the Detector

Verify that the intended compatible tubing is fully and correctly seated in the detector. Check for:

- Partial insertion
- Tubing off-center
- Kinks
- Tubing deformation
- Unexpected gaps
- Incorrect tubing diameter or type

**Expected outcome:** The tubing is correctly positioned within the detector sensing area.

If proper tubing placement clears the alarm and the detector passes functional verification, troubleshooting can stop.

### 4. Inspect the Sensor Area

With the equipment out of clinical use, inspect accessible detector surfaces for:

- Moisture
- Blood or fluid residue
- Gel
- Dust
- Adhesive
- Cracks
- Damage that could interfere with sensing

Clean only using approved methods.

**Expected outcome:** The detector sensing surfaces are clean, dry, and physically intact.

If approved cleaning restores normal detector function, troubleshooting can stop after testing.

### 5. Check Detector Cable and Connection

Inspect the external detector cable and connectors for looseness, strain, contamination, or visible damage. Reseat approved connections if needed.

Observe whether gentle movement of the cable causes recognition or alarm status to change.

**Expected outcome:** The detector remains recognized and stable regardless of normal cable positioning.

If correcting a loose external connection resolves the condition and testing passes, troubleshooting can stop.

### 6. Verify Correct Detector Configuration

Confirm the detector is connected to the expected system channel and the normal operating configuration matches the installed setup.

Do not bypass the safety function or change protected thresholds.

**Expected outcome:** The detector is correctly configured and enabled for the intended circuit.

If an authorized configuration correction restores normal operation, troubleshooting can stop after verification.

### 7. Compare With Known-Good Components

When permitted, compare operation using known-good compatible tubing, detector hardware, or external cable one component at a time.

**Expected outcome:** The failure follows a replaceable external component or remains with the detector/system channel.

If a faulty external component is identified and replaced, troubleshooting can stop after successful detector testing.

### 8. Perform Approved Functional Verification

Use the appropriate approved detector test method and verify:

- Detector recognition
- Alarm activation when expected
- Alarm clearing when the test condition is removed
- Stable operation with tubing correctly seated
- Associated system response as applicable

Do not invent or substitute unapproved bubble test methods.

**Expected outcome:** The bubble detector and associated alarm pathway operate correctly during approved testing.

If all checks pass, troubleshooting is complete.

### 9. Escalate an Unresolved Detector Failure

If the detector fails testing, alarms intermittently without an identifiable external cause, or cannot be trusted, remove it from service.

Do not disable the detector or troubleshoot internal sensing electronics at board level.

**Expected outcome:** An unreliable air-detection safety function is not returned to clinical use.

## If the Problem Persists

Tubing placement, cleanliness, external connections, configuration, and compatible component substitution have been checked. Remaining causes may include sensor electronics, internal signal processing, communication faults, or protected calibration/service conditions.

The affected equipment should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate LivaNova documentation and approved test equipment.
- Repaired, calibrated, or configured only by qualified personnel.

Return-to-service testing must verify the complete bubble-detection and alarm pathway before clinical release.

Knowing when to stop rather than dismissing an unexplained safety alarm is proper troubleshooting.

## Clinical Use Tip

A bubble alarm should be treated as a real circuit hazard until the perfusionist has established that the patient and circuit are safe.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Treat bubble detection as a critical safety function. Work from tubing placement and cleanliness through connections and configuration, verify using approved testing, and escalate immediately if the detector cannot be proven reliable.

That is successful troubleshooting.
