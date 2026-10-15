---
schemaVersion: 1
title: "GE Healthcare CardioLab Electrophysiology Recording System - Calibration or Quality-Control Test Fails"
issueTitle: "Calibration or Quality-Control Test Fails"
description: "CardioLab calibration or functional quality verification fails because of setup, test equipment, cables, accessories, configuration, or acquisition-system problems."
assetType: "Electrophysiology Recording System"
manufacturer: "GE Healthcare"
model: "CardioLab"
slug: "ge-healthcare-cardiolab-calibration-or-quality-control-test-fails"
dateAdded: "2026-10-15"
taxonomyMode: "reuse"
ccr:
  complaint: "CardioLab failed a scheduled signal-acquisition verification during Clinical Engineering testing."
  cause: "Clinical Engineering found a damaged external simulator lead causing an unstable test input."
  resolution: "The test lead was replaced, the verification was repeated successfully with approved equipment, and CardioLab passed final functional testing."
helpfulDetails:
  - "Exact test performed"
  - "Exact failure indication"
  - "Test-equipment identification"
  - "Test-equipment calibration status"
  - "External cable and adapter condition"
  - "Channels tested"
  - "Known-good substitution results"
  - "Relevant settings observed"
  - "Repeat-test results"
  - "Final verification results"
  - "Final device status"
---

## What This Guide Helps With

CardioLab calibration or functional quality verification fails because of setup, test equipment, cables, accessories, configuration, or acquisition-system problems.

## Step-by-Step Troubleshooting

### 1. Remove the System From Clinical Dependence

Do not perform calibration or quality-control troubleshooting while CardioLab is required for active patient monitoring or recording.

If the failed test could affect measurement or waveform reliability, keep the system out of clinical service until the result is understood.

**Expected outcome:** Calibration troubleshooting proceeds without compromising patient monitoring.

### 2. Confirm Which Test Failed

Identify the exact calibration, verification, or quality-control activity that failed and record the displayed result or message.

Confirm whether the test is a CardioLab function, an approved Clinical Engineering verification, or a test belonging to connected equipment.

**Expected outcome:** The failed test and responsible subsystem are clearly identified.

If the wrong procedure or test selection caused the failure, repeat the correct approved test and stop troubleshooting if it passes.

### 3. Verify Test Equipment and Setup

Confirm the test device or simulator is appropriate for the required verification, is within its required calibration status, and is connected according to approved procedures.

Inspect test leads, adapters, and connectors for damage or looseness.

**Expected outcome:** The test setup itself is valid and reliable.

If correcting the test setup produces a passing result, document the correction and stop troubleshooting.

### 4. Inspect External Signal Connections

Check CardioLab patient-interface cables, acquisition connections, adapters, and external modules used during the test.

Look for loose, damaged, contaminated, or incorrect accessories.

**Expected outcome:** The complete external test signal path is correctly connected.

If an external connection or accessory causes the failure and correcting it produces a valid pass, complete verification and stop troubleshooting.

### 5. Confirm Required Settings and Channel Selection

Verify the appropriate externally accessible channel, signal source, scale, gain, or other relevant settings for the approved test.

Do not change protected configuration or calibration constants without proper authorization.

**Expected outcome:** CardioLab is configured appropriately for the verification being performed.

If an accidental user-facing setting caused the failed test, correct it and repeat the full verification.

### 6. Repeat the Test Under Controlled Conditions

Repeat the approved test after checking setup and connections. Do not repeatedly rerun a failing test without changing or isolating a cause.

Observe whether the failure is consistent, intermittent, or channel-specific.

**Expected outcome:** The test passes consistently or produces a repeatable failure that can be isolated.

If the complete verification passes, troubleshooting is complete.

### 7. Compare Channels or External Accessories

Where appropriate, compare the affected channel with another known-good CardioLab input or substitute a known-good approved cable or adapter.

Change one factor at a time.

**Expected outcome:** The failure is isolated to an external accessory, a particular input path, or the broader acquisition system.

If an external item is confirmed defective, remove it from service and repeat the required verification.

### 8. Verify Overall Acquisition Function

Use an approved simulator or test source to confirm that CardioLab receives, displays, and records expected signals after corrective action.

A single passing calibration result should not substitute for functional testing when the original complaint involved clinical signal reliability.

**Expected outcome:** Required signal paths function normally and the applicable quality test passes.

If all required tests pass, the system may proceed toward return to service.

### 9. Escalate Repeated Test Failure

If calibration or quality verification continues to fail with a valid test setup and known-good external accessories, stop external troubleshooting.

Do not change internal calibration values, protected service parameters, or board-level hardware without authorized procedures.

**Expected outcome:** The unresolved measurement or acquisition problem is escalated rather than masked by unauthorized adjustment.

## If the Problem Persists

Test equipment, setup, accessories, external signal paths, and basic configuration have been ruled out. Remaining possibilities may include acquisition electronics, internal signal processing, software, protected configuration, or another service-level condition.

The CardioLab system should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate GE Healthcare documentation and calibrated approved test equipment.
- Repaired, calibrated, or configured only by qualified personnel.

Repeat the applicable full verification after repair before return to service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A failed measurement or signal-quality verification is a return-to-service issue, not merely a test inconvenience; do not release CardioLab until required checks pass.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Treat a failed CardioLab calibration or quality test as a systematic verification problem. Confirm the test method and external signal path first, avoid unauthorized adjustment, and require a complete passing verification before return to service.

That is successful troubleshooting.
