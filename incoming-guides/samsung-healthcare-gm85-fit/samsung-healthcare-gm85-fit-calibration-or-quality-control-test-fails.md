---
schemaVersion: 1
title: "Samsung Healthcare GM85 Fit Mobile X-Ray System - Calibration or Quality-Control Test Fails"
issueTitle: "Calibration or Quality-Control Test Fails"
description: "Addresses failed calibration or QC caused by setup, detector condition, positioning, environment, power, test equipment, or persistent system faults."
assetType: "Mobile X-Ray System"
manufacturer: "Samsung Healthcare"
model: "GM85 Fit"
slug: "samsung-healthcare-gm85-fit-calibration-or-quality-control-test-fails"
dateAdded: "2026-09-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported that the GM85 Fit detector quality-control test would not complete successfully."
  cause: "Clinical Engineering found the detector was positioned incorrectly for the approved QC setup."
  resolution: "Clinical Engineering corrected the detector and test-object positioning, repeated the approved QC procedure successfully, and documented the passing result."
helpfulDetails:
  - "Exact test that failed"
  - "Failure message"
  - "Detector used"
  - "Test-object or phantom used"
  - "Setup and positioning observed"
  - "Test equipment identification"
  - "Environmental conditions"
  - "Previous QC status"
  - "Result after correction"
  - "Final device status"
---
## What This Guide Helps With

Addresses failed calibration or QC caused by setup, detector condition, positioning, environment, power, test equipment, or persistent system faults.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Use
If the failed QC test affects confidence in image quality, detector performance, or radiation output, do not return the system to patient use until the failure is understood and resolved.

Provide another verified mobile X-ray unit when needed.

Expected outcome: A system with unresolved performance concerns is not used clinically.

### 2. Confirm Which Test Failed
Identify the exact calibration or QC procedure, the stage where it failed, the displayed message, and whether the test previously passed.

Do not substitute a different test for the failed requirement.

Expected outcome: The specific failure is documented and reproducible.

### 3. Verify Test Setup
Confirm the approved test object, detector, positioning, orientation, distance, and other setup elements are correct according to the applicable procedure.

Do not invent or approximate test geometry.

Expected outcome: The calibration or QC procedure is being performed with the correct setup. If setup error caused the failure, repeat the approved test and stop when it passes.

### 4. Inspect Detector and Imaging Surfaces
Check the detector and test object for contamination, damage, improper covers, or foreign material that could affect the measurement.

Expected outcome: Imaging surfaces and test objects are clean and intact.

### 5. Confirm System Readiness and Power
Verify the GM85 Fit has completed startup, the intended detector is ready, battery state is adequate, and no other system warning is active.

Expected outcome: The system is stable and ready before the test begins.

### 6. Check Environmental Conditions
Look for unusual temperature conditions, vibration, direct interference from nearby equipment, unstable flooring, or other obvious environmental changes that could affect testing.

Expected outcome: Testing is performed under appropriate and stable environmental conditions.

### 7. Verify Test Equipment
If external meters, phantoms, fixtures, or accessories are used, confirm they are the correct equipment and their calibration or verification status is current according to facility policy.

Expected outcome: The measurement equipment itself is not the source of the failure.

### 8. Repeat the Approved Test Once Conditions Are Correct
After correcting any external setup problem, repeat the applicable manufacturer or facility-approved test.

Do not repeatedly recalibrate the system in an attempt to force a passing result.

Expected outcome: The system passes the required test. If the failure repeats under correct conditions, stop external troubleshooting and escalate.

### 9. Document Return-to-Service Evidence
Record the test performed and passing result according to department policy before releasing the unit.

Expected outcome: Objective evidence supports return to clinical use.

## If the Problem Persists

If setup, detector condition, system readiness, environment, and test equipment have been verified and the QC or calibration still fails, common external causes have been ruled out.

Possible remaining categories include detector calibration, generator performance, image-processing calibration, internal sensors, acquisition electronics, software, or service-level adjustment requirements.

The system should be:

- Removed from service when the failed test affects safe or reliable imaging.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate Samsung Healthcare documentation and calibrated test equipment.
- Repaired, adjusted, or configured only by qualified personnel.

Required QC, calibration, radiation-performance, and functional testing must pass before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Never treat a failed quality-control test as a nuisance alarm; determine whether it affects confidence in patient imaging before returning the system to use.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

A failed QC test should be approached methodically by verifying setup and test conditions before assuming equipment failure, while preserving objective evidence and escalating any persistent performance concern.

That is successful troubleshooting.
