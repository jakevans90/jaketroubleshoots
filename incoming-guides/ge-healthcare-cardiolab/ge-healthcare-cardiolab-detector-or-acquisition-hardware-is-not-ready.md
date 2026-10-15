---
schemaVersion: 1
title: "GE Healthcare CardioLab Electrophysiology Recording System - Detector or Acquisition Hardware Is Not Ready"
issueTitle: "Detector or Acquisition Hardware Is Not Ready"
description: "CardioLab acquisition hardware is unavailable or not ready because of startup, cable, accessory, interface, communication, or associated-system problems."
assetType: "Electrophysiology Recording System"
manufacturer: "GE Healthcare"
model: "CardioLab"
slug: "ge-healthcare-cardiolab-detector-or-acquisition-hardware-is-not-ready"
dateAdded: "2026-10-15"
taxonomyMode: "reuse"
ccr:
  complaint: "EP staff reported that CardioLab displayed the acquisition system as unavailable and no signals could be acquired."
  cause: "Clinical Engineering found an external communication cable between the workstation and acquisition hardware loose at the connector."
  resolution: "The cable was secured, acquisition hardware returned to ready status, test signals were verified, and the system was returned to service."
helpfulDetails:
  - "Exact readiness message"
  - "Channels or functions affected"
  - "Acquisition component power indicators"
  - "Patient-interface cable condition"
  - "Modules or accessories connected"
  - "Known-good substitution results"
  - "Communication link indicators"
  - "Whether the issue followed equipment movement"
  - "Test-signal results"
  - "Results after restart"
  - "Final acquisition status"
---

## What This Guide Helps With

CardioLab acquisition hardware is unavailable or not ready because of startup, cable, accessory, interface, communication, or associated-system problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Monitoring

Do not troubleshoot unreliable acquisition hardware while the patient depends on CardioLab for essential electrophysiology monitoring or recording. Ensure an appropriate alternate monitoring or recording method is available before disconnecting equipment.

Confirm whether the complaint concerns CardioLab signal-acquisition hardware or an imaging detector belonging to another integrated system.

**Expected outcome:** Patient monitoring remains supported and the affected acquisition subsystem is identified correctly.

### 2. Confirm the Reported Ready-State Problem

Determine which acquisition functions are unavailable, whether all channels are affected, whether the problem appeared at startup or during a case, and whether a specific module or connected accessory is implicated.

Record any displayed message exactly.

**Expected outcome:** The failure is narrowed to the complete acquisition system, a particular interface, or an associated device.

If the system is actually ready and the issue was a workflow misunderstanding, verify operation and stop troubleshooting.

### 3. Check Power to Acquisition Components

Verify externally accessible acquisition hardware, interface modules, displays, and associated equipment are powered and showing expected status indicators.

Inspect external power cords and approved power distribution connections.

**Expected outcome:** All required acquisition components have stable power and complete their normal startup.

If restoring external power makes the acquisition system ready, verify operation and stop troubleshooting.

### 4. Inspect Acquisition and Patient-Interface Connections

Inspect accessible acquisition cables, patient-interface leads, amplifier connections, breakout cables, and external modules for loose connectors, bent or damaged housings, strain, contamination, or obvious physical damage.

Disconnect equipment from the patient before manipulating patient-connected signal cables when required for safety.

**Expected outcome:** All required acquisition interfaces are securely connected and physically intact.

If correcting a loose connection restores the ready state, confirm signal acquisition and stop troubleshooting.

### 5. Verify Required Accessories Are Present and Recognized

Confirm that required external modules, patient-interface components, leads, and accessories for the intended CardioLab workflow are connected and appropriate for use.

Where approved, compare the suspect accessory with a known-good compatible item.

**Expected outcome:** Required accessories are recognized and the system reaches its normal acquisition-ready condition.

If a known-good external accessory resolves the problem, remove the defective accessory from service and stop troubleshooting after verification.

### 6. Check Communication Between Workstation and Acquisition Hardware

Inspect Ethernet or other external communication connections used between CardioLab components. Check available link indicators and confirm the workstation has not lost connection to the acquisition subsystem.

Do not alter network addresses or restricted configuration without authorization.

**Expected outcome:** CardioLab workstation and acquisition hardware communicate normally.

If restoring an external communication connection returns the hardware to ready status, verify stable operation and stop troubleshooting.

### 7. Restart the Affected System When Clinically Safe

With the system removed from patient dependence, perform an approved orderly restart if the acquisition hardware remains unavailable.

Observe whether all required components initialize in the correct sequence and become recognized.

**Expected outcome:** Acquisition hardware completes initialization and remains ready without repeated disconnects.

If normal readiness returns and remains stable through testing, proceed to final verification.

### 8. Perform Functional Signal Verification

Using an approved simulator, test source, or manufacturer-supported functional method when applicable, verify that CardioLab detects the acquisition hardware and receives expected signals.

Do not rely only on a ready indicator when the original complaint involved missing acquisition capability.

**Expected outcome:** Acquisition hardware is recognized and produces stable, appropriate test data.

If functional testing passes without recurrence, troubleshooting is complete.

### 9. Escalate an Unresolved Acquisition Failure

If acquisition hardware remains unavailable after external power, cabling, accessories, and communication are ruled out, remove the affected CardioLab equipment from service.

Avoid internal amplifier, computer, interface-board, or other board-level repair unless specifically authorized and trained.

**Expected outcome:** The unresolved acquisition problem is safely escalated for qualified service.

## If the Problem Persists

External power, connection, accessory, and communication causes have been ruled out. Remaining possibilities may include acquisition electronics, workstation software, interface hardware, system configuration, or another internal service-level condition.

The CardioLab system should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Complete functional acquisition and applicable safety testing before return to service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Maintain an alternate patient-monitoring method before disconnecting CardioLab acquisition hardware or patient-interface components.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect active monitoring first, then check power, external interfaces, accessories, and communication before suspecting acquisition electronics. Verify actual signal acquisition after correction and escalate unresolved hardware problems with complete documentation.

That is successful troubleshooting.
