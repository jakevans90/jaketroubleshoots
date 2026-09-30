---
schemaVersion: 1
title: "Varian TrueBeam Radiation Therapy System - Calibration or Quality-Control Test Fails"
issueTitle: "Calibration or Quality-Control Test Fails"
description: "A required calibration or quality-control check fails, will not complete, or produces a result that cannot be accepted."
assetType: "Radiation Therapy System"
manufacturer: "Varian"
model: "TrueBeam"
slug: "varian-truebeam-calibration-or-quality-control-test-fails"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that a scheduled TrueBeam imaging quality-control test would not pass."
  cause: "Clinical Engineering found the approved test phantom positioned incorrectly for the verification procedure."
  resolution: "Clinical Engineering corrected the phantom setup and the qualified team repeated the approved quality-control procedure with an acceptable result."
helpfulDetails:
  - "Exact test that failed"
  - "Stage of failure"
  - "Displayed message"
  - "Test equipment used"
  - "Phantom or fixture condition"
  - "Setup and positioning observed"
  - "Known-good substitution performed"
  - "Environmental or recent power events"
  - "Medical Physics involvement"
  - "Repeat-test result"
  - "Final system status"
---
## What This Guide Helps With

A required calibration or quality-control check fails, will not complete, or produces a result that cannot be accepted.

## Step-by-Step Troubleshooting

### 1. Protect Patients by Withholding Unverified Functions
Do not use an affected treatment, imaging, positioning, or safety function clinically when a required quality-control or calibration check has failed.

**Expected outcome:** Clinical use is suspended when required verification is not successfully completed.

### 2. Identify the Exact Failed Test
Record the name of the calibration or quality-control activity, the stage at which it failed, and any displayed message. Determine whether the failure is repeatable.

**Expected outcome:** The failed verification activity is clearly identified.

### 3. Verify the Test Setup
Confirm that the correct phantom, fixture, accessory, detector position, couch position, or other approved test equipment is being used and positioned correctly.

**Expected outcome:** The test setup matches the approved facility or manufacturer procedure.

### 4. Inspect Test Equipment and Accessories
Check applicable phantoms, fixtures, cables, and accessories for damage, contamination, incorrect assembly, or obvious positioning problems.

**Expected outcome:** Test equipment is intact, clean, and suitable for use.

### 5. Confirm System Readiness
Verify that the TrueBeam and required imaging, positioning, workstation, and supporting systems have completed initialization and report normal readiness.

**Expected outcome:** The system is in the correct operational state for the quality-control test.

### 6. Check Environmental Conditions
Determine whether room temperature changes, recent power interruptions, construction, equipment relocation, or other unusual environmental conditions could have affected the test.

Do not invent or apply environmental limits unless documented by the manufacturer or facility.

**Expected outcome:** No obvious environmental condition is invalidating the verification.

### 7. Repeat the Approved Test Once the Setup Is Corrected
If a clear setup or external issue is found, correct it and repeat the test exactly as required by approved procedures.

**Expected outcome:** The test completes successfully. If it passes and all requirements are met, troubleshooting can stop.

### 8. Compare With Known-Good Test Equipment When Appropriate
Where approved and available, substitute a known-good cable, phantom, accessory, or other external test component to determine whether the failure follows the test equipment.

**Expected outcome:** An external test-equipment problem is either identified or ruled out.

### 9. Stop After a Persistent Failure
Do not repeatedly adjust calibration or configuration values merely to obtain a passing result. Persistent failures require qualified evaluation.

**Expected outcome:** The affected system remains unavailable until the failed quality requirement is resolved.

## If the Problem Persists

Test setup, accessories, equipment condition, system readiness, and obvious environmental causes have been ruled out. Remaining causes may involve imaging calibration, geometry, detector response, positioning accuracy, treatment-delivery performance, software, or another internal service-level condition.

The device should be:

- Removed from service when the failed test affects required clinical safety or performance
- Labeled Out of Service
- Sent for repair or appropriate service evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Calibrated, repaired, or configured only by qualified personnel

Medical Physics involvement may be required depending on the failed test and the function affected. Return to service requires successful completion of all applicable verification before patient use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A failed quality-control result is itself meaningful information; do not adjust the system merely to make the result pass without understanding the cause.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Quality-control failures should never be cleared by assumption. Verify the setup, accessories, system state, and environment first, then escalate persistent failures to qualified service and Medical Physics as appropriate before clinical use resumes.

That is successful troubleshooting.
