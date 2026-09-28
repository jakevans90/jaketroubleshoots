---
schemaVersion: 1
title: "Siemens Healthineers Biograph Vision PET / CT System - Calibration or Quality-Control Test Fails"
issueTitle: "Calibration or Quality-Control Test Fails"
description: "Use this guide when an authorized PET or CT calibration or quality-control check will not complete or produces an unacceptable result."
assetType: "PET / CT System"
manufacturer: "Siemens Healthineers"
model: "Biograph Vision"
slug: "siemens-healthineers-biograph-vision-calibration-or-quality-control-test-fails"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Imaging staff reported that a routine Biograph Vision quality-control test repeatedly failed."
  cause: "Clinical Engineering found the approved QC test object incorrectly positioned on the patient table."
  resolution: "Clinical Engineering corrected the test-object placement, repeated the approved QC procedure successfully, documented the passing result, and returned the system to service."
helpfulDetails:
  - "Exact test name"
  - "PET or CT subsystem involved"
  - "Exact failure message"
  - "Test-object condition"
  - "Test-object position"
  - "System readiness state"
  - "Environmental conditions"
  - "Previous test result"
  - "Repeat-test result"
  - "Final system status"
---
## What This Guide Helps With

Use this guide when an authorized PET or CT calibration or quality-control check will not complete or produces an unacceptable result.

## Step-by-Step Troubleshooting

### 1. Prevent Clinical Use When Required QC Is Not Established

If the failed test is required to confirm safe or acceptable imaging performance, do not use the affected imaging function clinically until the failure is resolved.

**Expected outcome:** Patient studies are not performed using a subsystem whose required performance has not been verified.

### 2. Confirm the Exact Failed Test

Identify:

- The exact test or calibration attempted.
- Whether PET, CT, or combined-system performance is involved.
- The exact displayed result or message.
- Whether the test fails consistently.
- When the last successful test occurred.
- Whether service or environmental changes occurred since then.

Do not substitute a different test and assume it proves the failed requirement.

**Expected outcome:** The exact failed verification activity is documented.

### 3. Confirm Test Setup

Inspect the approved test setup for:

- Correct phantom or test object.
- Correct placement.
- Proper table position.
- Proper orientation.
- Absence of unintended objects in the scan field.
- Correct authorized test workflow selection.

Do not improvise substitute test objects unless specifically allowed by the approved procedure.

**Expected outcome:** Test setup matches the approved procedure.

If correcting setup allows the QC test to pass, document the correction and stop after verification.

### 4. Inspect Test Equipment and Accessories

Check approved QC accessories for:

- Damage.
- Contamination.
- Missing components.
- Improper assembly.
- Incorrect positioning.
- Expired or unsuitable supporting material when applicable.

**Expected outcome:** The external QC equipment is suitable for use.

If an approved known-good accessory allows the test to pass, remove the defective accessory from use and stop after completing verification.

### 5. Verify System Readiness

Confirm the scanner has completed normal startup and required imaging subsystems report ready before calibration or QC begins.

Do not attempt to calibrate through an unrelated system fault.

**Expected outcome:** The system is stable and ready for the required test.

If resolving a readiness problem allows the test to complete successfully, troubleshooting can stop after documentation.

### 6. Verify Environmental Conditions

Check for obvious environmental conditions that may invalidate or interrupt testing:

- Excessive room temperature.
- Cooling problems.
- Recent HVAC outage.
- Power interruption.
- Water intrusion.
- Unusual room changes.

**Expected outcome:** The test is being performed under normal facility conditions.

If correcting an environmental cause restores repeatable passing results, stop after verification.

### 7. Repeat the Test Once With Correct Setup

After external conditions and setup have been verified, repeat the failed test using the approved procedure.

Do not repeatedly rerun a failing calibration hoping for an intermittent pass.

**Expected outcome:** The test completes successfully and produces an acceptable result according to the applicable approved criteria.

If it passes repeatably and no related issue remains, troubleshooting is complete.

### 8. Compare With Prior Results When Available

Review prior QC or calibration records for sudden changes, repeated marginal behavior, or a clear change coinciding with service or environmental activity.

Do not alter limits or acceptance criteria to make a failing result pass.

**Expected outcome:** Current results are placed in appropriate historical context without changing acceptance requirements.

### 9. Perform Final Verification

If an external setup issue was corrected, verify:

- The required QC test passes.
- The result is repeatable when required.
- System status remains normal.
- No related image-quality concern remains.

**Expected outcome:** Required quality verification is successfully completed.

If all required checks pass, return-to-service requirements are satisfied.

### 10. Escalate Repeated QC or Calibration Failure

If the authorized test continues to fail with correct setup, suitable test equipment, normal environment, and stable system readiness, stop external troubleshooting.

**Expected outcome:** The affected system is withheld from clinical use and escalated for service evaluation.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve detector calibration, internal acquisition electronics, geometry, system timing, calibration files, internal environmental controls, or another service-level condition.

The device should be:

- Removed from affected clinical service.
- Labeled **Out of Service** when required.
- Sent for repair or qualified system evaluation.
- Evaluated using appropriate Siemens Healthineers documentation and approved test equipment.
- Calibrated, repaired, or configured only by qualified personnel.

Do not modify acceptance thresholds, service calibration values, or protected configuration to force a passing result.

Required calibration and QC must be completed successfully before return to clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A successful scan does not substitute for a required failed QC test; required system performance must be objectively verified before clinical use.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Verify test setup and external conditions before assuming system calibration failure, never alter acceptance criteria to create a passing result, and keep the scanner out of affected clinical use until required verification succeeds.

That is successful troubleshooting.
