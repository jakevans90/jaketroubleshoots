---
schemaVersion: 1
title: "Medtronic 5392 External Pacemaker - Pacing Output Is Low, Intermittent, or Outside Tolerance"
issueTitle: "Pacing Output Is Low, Intermittent, or Outside Tolerance"
description: "Low or unstable pacing output caused by batteries, patient cables, connections, controls, test setup, or a possible device-level output problem."
assetType: "External Pacemaker"
manufacturer: "Medtronic"
model: "5392"
slug: "medtronic-5392-pacing-output-is-low-intermittent-or-outside-tolerance"
dateAdded: "2026-11-12"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported intermittent ventricular pacing output from the Medtronic 5392."
  cause: "Clinical Engineering confirmed unstable ventricular output on a pacing analyzer after verifying known-good batteries and patient cable connections."
  resolution: "The pacemaker was removed from service and referred for qualified bench repair because output remained unstable after external causes were eliminated."
helpfulDetails:
  - "Atrial or ventricular channel"
  - "Reported output setting"
  - "Measured output result"
  - "Battery condition"
  - "Patient cable condition"
  - "Known-good cable result"
  - "Analyzer and test setup used"
  - "Whether intermittency followed cable movement"
  - "Control behavior"
  - "Final device status"
---

## What This Guide Helps With

Low or unstable pacing output caused by batteries, patient cables, connections, controls, test setup, or a possible device-level output problem.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Transfer Pacing Support

Do not troubleshoot questionable pacing output while a patient depends on the Medtronic 5392. Transfer the patient to another verified pacing source before testing.

**Expected outcome:** Patient pacing continues safely without dependence on an unreliable output channel.

### 2. Confirm the Reported Output Problem

Determine whether the issue involves atrial output, ventricular output, or both. Record whether the problem is low amplitude, intermittent pulses, failure under movement, or failure of measured output to meet the applicable manufacturer requirement.

**Expected outcome:** The affected channel and failure condition are reproducible and documented.

### 3. Verify Battery Condition

Inspect battery installation and repeat testing with known-good approved batteries when appropriate. Low or unstable supply power must be excluded before assuming an output-stage fault.

**Expected outcome:** The pacemaker has a reliable power source for output testing.

### 4. Inspect Patient Cables and Connections

Inspect the affected channel cable, connector, strain relief, and receptacle. Reseat connections and check for contamination or mechanical damage.

**Expected outcome:** The output path is securely connected with no obvious external defect.

### 5. Substitute a Known-Good Cable

Repeat the output test using an approved known-good patient cable.

**Expected outcome:** Output becomes stable if the original cable was defective. If output is restored and remains within the applicable verification requirement, replace the cable and troubleshooting can stop after final testing.

### 6. Verify Output Controls

Confirm that the selected output control is functioning normally and has not been inadvertently set differently from the expected test condition. Check for mechanical looseness, binding, or intermittent response.

Do not alter protected calibration settings.

**Expected outcome:** The displayed setting responds consistently to control adjustment.

### 7. Verify the Test Setup

Inspect pacing analyzer leads, test cables, adapters, loading connections, and analyzer configuration. Compare with a known-good setup when available.

**Expected outcome:** The measurement system is confirmed not to be causing the apparent output error.

### 8. Measure Pacing Output

Using approved pacing test equipment and the applicable manufacturer procedure, measure the affected channel at appropriate settings.

Do not invent or substitute tolerances; use the current approved service documentation.

**Expected outcome:** Measured pacing output agrees with the applicable specification and remains stable.

### 9. Check for Intermittency

While maintaining the controlled bench setup, gently observe cable and connector stability without stressing the device. Repeat measurements to identify intermittent changes.

**Expected outcome:** Output remains stable during repeated testing. If stable and within tolerance, troubleshooting can stop after complete functional verification.

### 10. Escalate Out-of-Tolerance Output

If output remains low, intermittent, or outside the applicable requirement with known-good batteries, cables, and test equipment, remove the pacemaker from service.

**Expected outcome:** A possible internal output or control problem is referred for qualified repair.

## If the Problem Persists

External power, cables, connections, settings, and measurement setup have been ruled out. The remaining fault may involve internal output generation, channel control, connector interfaces, or calibration requiring service-level evaluation.

Remove the device from service, label it **Out of Service**, and send it for bench evaluation using approved Medtronic documentation and calibrated test equipment. Internal repairs or calibration adjustments must be performed only by qualified personnel. Complete output, sensing, alarm, and safety verification is required before return to service.

## Clinical Use Tip

A pacemaker with intermittent or questionable output must not remain available for emergency clinical use until its performance has been verified.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient, confirm the measurement path, rule out batteries and cables first, and escalate any persistent out-of-tolerance pacing output rather than assuming a specific internal failure.

That is successful troubleshooting.
