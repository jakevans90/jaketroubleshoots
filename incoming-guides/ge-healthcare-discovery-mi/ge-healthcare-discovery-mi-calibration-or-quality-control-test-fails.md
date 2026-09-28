---
schemaVersion: 1
title: "GE Healthcare Discovery MI PET / CT System - Calibration or Quality-Control Test Fails"
issueTitle: "Calibration or Quality-Control Test Fails"
description: "Troubleshoots failed PET / CT calibration or QC caused by setup, phantom positioning, environment, incomplete readiness, accessories, or repeatable system conditions."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "Discovery MI"
slug: "ge-healthcare-discovery-mi-calibration-or-quality-control-test-fails"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "PET / CT staff reported that the Discovery MI quality-control test repeatedly failed before the start of scheduled patient imaging."
  cause: "Clinical Engineering found the required QC phantom positioned incorrectly for the selected test."
  resolution: "Clinical Engineering repositioned the phantom correctly, repeated the approved QC procedure, verified a successful result, and returned the scanner to service."
helpfulDetails:
  - "Exact QC or calibration test"
  - "PET or CT subsystem"
  - "Failure message or result"
  - "Phantom used"
  - "Phantom condition"
  - "Positioning observed"
  - "Environmental condition"
  - "Recent QC history"
  - "Result before correction"
  - "Result after correction"
  - "Final system status"
---
## What This Guide Helps With
Troubleshoots failed PET / CT calibration or QC caused by setup, phantom positioning, environment, incomplete readiness, accessories, or repeatable system conditions.

## Step-by-Step Troubleshooting

### 1. Stop Clinical Use When Required Quality Cannot Be Verified

If a required calibration or quality-control test fails and the test is necessary to establish safe or diagnostically reliable operation, do not continue patient imaging on the affected modality until the failure is resolved.

**Expected outcome:** Clinical imaging does not continue when required system performance has not been verified.

### 2. Identify the Exact Failed Test

Record:

- Test or calibration performed
- PET or CT subsystem involved
- Exact displayed result or message
- Whether the test failed to start or failed after acquisition
- Whether the problem occurred once or repeatedly

Do not substitute a different test merely to obtain a passing result.

**Expected outcome:** The specific failed QC or calibration process is clearly documented.

### 3. Verify Complete System Readiness

Confirm that the Discovery MI has fully completed startup and that no unresolved hardware, cooling, detector, communication, or motion fault is active.

**Expected outcome:** The scanner is in the normal state required for the approved test.

### 4. Verify the Test Object or Phantom

Inspect the designated phantom or test device for:

- Correct phantom selected
- Correct assembly
- Visible damage
- Contamination
- Incorrect orientation
- Incorrect positioning
- Objects or accessories interfering with the test

Use only the appropriate approved phantom or test device.

**Expected outcome:** The required test object is intact, correctly positioned, and suitable for the procedure.

### 5. Confirm Test Setup and Selected Procedure

Verify that the correct approved QC or calibration procedure was selected and that the operator-accessible setup matches the intended test.

Review positioning and setup against current department or manufacturer documentation.

Do not alter calibration constants or restricted service parameters.

**Expected outcome:** The correct test is being performed with the correct approved setup.

### 6. Check Environmental Conditions

Verify that no obvious environmental condition is affecting the test.

Check for:

- Abnormal room temperature
- Cooling alarms
- Recent power interruption
- Vibration or nearby activity
- Objects introduced into the scan area
- Facility work affecting the room

**Expected outcome:** The testing environment is stable and appropriate for valid QC results.

### 7. Repeat the Test Once After Correcting External Conditions

If an identifiable setup issue is corrected, repeat the approved QC or calibration procedure once under proper conditions.

Do not perform repeated calibrations simply to force a passing result.

**Expected outcome:** The test completes successfully and produces an acceptable result.

If the test passes after correcting a confirmed external cause, proceed to final verification.

### 8. Compare With Recent QC History

Review recent documented QC results where available.

Determine whether the current failure is:

- A single isolated setup issue
- A developing trend
- A sudden change
- Repeated across multiple tests

**Expected outcome:** The result is placed in context and a recurring system-performance problem is not overlooked.

### 9. Complete Required Verification

If the failed condition is corrected, repeat the appropriate approved verification required before clinical use.

Confirm no related image-quality, detector-readiness, or system fault remains.

**Expected outcome:** Required QC and calibration verification passes and the scanner is suitable for clinical operation.

If all applicable tests pass, troubleshooting can stop and the scanner may be returned to service.

## If the Problem Persists

If the correct phantom, positioning, test selection, system readiness, and environmental conditions have been verified but QC or calibration continues to fail, the cause may involve detector performance, calibration data, acquisition electronics, image reconstruction, alignment, environmental control, or another service-level condition.

The system should be:

- Removed from service as appropriate for the failed test
- Labeled Out of Service
- Sent for repair or formal system evaluation
- Evaluated using appropriate GE Healthcare documentation, phantoms, and approved test equipment
- Calibrated, repaired, or configured only by qualified personnel

Do not adjust internal calibration values solely to obtain a passing QC result.

After service, repeat all required affected calibration, QC, image-quality, and safety checks before return to clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A failed required QC test is evidence that system performance has not been verified; do not use a successful patient image as a substitute for proper QC.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

A failed QC or calibration test should be treated as a verification problem, not bypassed. Confirm the correct test object, setup, readiness, and environment first, then escalate persistent failures for qualified service and document the final result clearly.

That is successful troubleshooting.
