---
schemaVersion: 1
title: "GE Healthcare NM/CT 870 CZT PET / CT System - Calibration or Quality-Control Test Fails"
issueTitle: "Calibration or Quality-Control Test Fails"
description: "A calibration or QC check fails because of setup, phantom positioning, environmental conditions, readiness, contamination, or an underlying system-performance problem."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "NM/CT 870 CZT"
slug: "ge-healthcare-nm-ct-870-czt-calibration-or-quality-control-test-fails"
dateAdded: "2026-09-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Imaging staff reported the NM/CT 870 CZT daily quality-control check would not pass."
  cause: "Clinical Engineering found the approved phantom was incorrectly positioned for the test."
  resolution: "Clinical Engineering corrected the phantom position, repeated the approved QC procedure, verified a passing result, and returned the system to service."
helpfulDetails:
  - "Exact QC or calibration test"
  - "Exact displayed failure"
  - "Phantom or test object used"
  - "Phantom condition"
  - "Positioning and orientation"
  - "System readiness state"
  - "Environmental condition"
  - "Number of test attempts"
  - "Result after correction"
  - "Final clinical status"
---
## What This Guide Helps With

A calibration or QC check fails because of setup, phantom positioning, environmental conditions, readiness, contamination, or an underlying system-performance problem.

## Step-by-Step Troubleshooting

### 1. Protect Patients by Suspending Affected Clinical Use

If a required calibration or quality-control check fails, do not assume the system remains suitable for patient imaging. Follow departmental policy for removing the affected modality or system from clinical use until acceptable performance is demonstrated.

**Expected outcome:** Patient imaging does not continue on a system whose required performance verification has failed.

### 2. Record the Exact Failed Test

Identify the specific calibration or QC test, the displayed failure message, whether the test stopped or completed with unacceptable results, and whether the failure is new or recurring.

Do not invent or reinterpret manufacturer limits.

**Expected outcome:** The exact failed process and observed result are documented.

### 3. Verify System Readiness Before Retesting

Confirm the workstation, detectors, CT subsystem, gantry, table, and acquisition hardware are fully initialized and ready.

If another subsystem is not ready, resolve that external condition before repeating QC.

**Expected outcome:** The system is in the proper operating state for the test.

### 4. Inspect the Test Object or Phantom

Verify the correct approved phantom or test object is being used and inspect it for visible damage, contamination, missing components, incorrect assembly, or obvious deterioration.

**Expected outcome:** The test object is appropriate and physically suitable for the procedure.

### 5. Verify Phantom Positioning and Setup

Confirm the phantom is positioned and oriented according to the applicable approved procedure and that the table, detector, and gantry positions are appropriate.

Small setup errors can create repeatable QC failures without an internal hardware fault.

**Expected outcome:** The physical test setup matches the required procedure.

### 6. Verify the Correct Test Selection

Confirm the intended QC or calibration procedure is selected and that the correct normal operator-accessible settings are in use.

Do not alter protected service parameters simply to obtain a passing result.

**Expected outcome:** The system is running the correct test under the correct approved setup.

### 7. Inspect for Contamination or Obstruction

Check detector surfaces, table components, phantom surfaces, pads, cables, and the imaging path for contamination, debris, fluid, or unintended objects.

**Expected outcome:** No external material is compromising the QC measurement.

### 8. Check Environmental Conditions

Verify there has not been an HVAC issue, excessive room temperature, unusual vibration, construction activity, power disturbance, or other environmental event associated with the failed test.

**Expected outcome:** External environmental conditions are suitable for system verification.

### 9. Repeat the Test Only After a Correctable Cause Is Addressed

If an identifiable setup, positioning, connection, or environmental problem was corrected, repeat the approved QC or calibration test once under proper conditions.

Do not repeatedly rerun a failing test without changing the underlying condition.

**Expected outcome:** The test passes within the manufacturer's defined acceptance criteria. If it does, document the correction and troubleshooting can stop.

### 10. Escalate a Repeated QC or Calibration Failure

If the properly configured test fails again, remove the affected system or function from clinical service according to site policy and escalate.

Do not adjust internal detector calibration, CT calibration, alignment, service constants, or restricted configuration solely to force a passing result.

**Expected outcome:** A genuine performance problem receives qualified service evaluation before patient use resumes.

## If the Problem Persists

Common external causes involving readiness, phantom condition, positioning, test selection, contamination, and environment have been ruled out. Remaining categories may include detector performance, CT subsystem performance, calibration data, alignment, internal electronics, or service-level software/configuration.

The device should be:

- Removed from service as required by the failed QC condition.
- Labeled Out of Service.
- Sent for repair or controlled system evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved test equipment.
- Calibrated, repaired, or configured only by qualified personnel.

The applicable QC or calibration process must pass before return to clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A repeated QC failure is a performance finding, not an inconvenience to work around by repeatedly rerunning the test.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Treat failed QC as meaningful evidence, verify setup before assuming equipment failure, avoid altering service-level calibration merely to obtain a pass, and return the system to use only after required performance is demonstrated.

That is successful troubleshooting.
