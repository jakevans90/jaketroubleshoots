---
schemaVersion: 1
title: "Siemens Healthineers SOMATOM X.cite CT Scanner - Calibration or Quality-Control Test Fails"
issueTitle: "Calibration or Quality-Control Test Fails"
description: "Use this guide when an approved calibration or CT quality-control procedure cannot complete or produces an unacceptable result."
assetType: "CT Scanner"
manufacturer: "Siemens Healthineers"
model: "SOMATOM X.cite"
slug: "siemens-healthineers-somatom-xcite-calibration-or-quality-control-test-fails"
dateAdded: "2026-09-24"
taxonomyMode: "reuse"
ccr:
  complaint: "CT staff reported that a scheduled quality-control test on the SOMATOM X.cite failed."
  cause: "Clinical Engineering found the approved phantom was positioned incorrectly for the test."
  resolution: "The phantom was repositioned according to the approved setup, the test was repeated successfully, and scanner QC status was verified."
helpfulDetails:
  - "Exact test performed"
  - "Exact displayed result or message"
  - "Phantom used"
  - "Phantom condition and positioning"
  - "Test protocol selected"
  - "Scanner startup status"
  - "Environmental conditions"
  - "Previous QC comparison"
  - "Repeat-test result"
  - "Final scanner status"
---
## What This Guide Helps With

Use this guide when an approved calibration or CT quality-control procedure cannot complete or produces an unacceptable result.

## Step-by-Step Troubleshooting

### 1. Protect Patients From Use of Unverified Imaging Performance
If the failed test is required to establish acceptable scanner performance, suspend clinical scanning until the significance of the failure is understood.  
**Expected outcome:** Patients are not scanned on a system whose required performance verification has failed.

### 2. Confirm the Exact Test That Failed
Identify the calibration or quality-control test, when it failed, and the displayed result or message. Do not substitute a different test unless allowed by applicable procedures.  
**Expected outcome:** The specific failed verification activity is documented.

### 3. Inspect the Test Phantom and Setup
Verify that the correct approved phantom or test object is being used and that it is intact, properly positioned, centered, and free of obvious contamination or damage.  
**Expected outcome:** Test setup matches the intended procedure and obvious setup errors are eliminated.

### 4. Verify Table and Gantry Positioning
Confirm that the table and phantom positioning are appropriate for the required test and that no accessory or external object is interfering with the scan field.  
**Expected outcome:** Positioning does not account for the failed result.

### 5. Verify the Intended Protocol or QC Selection
Confirm the appropriate approved test workflow was selected. Do not alter service-level calibration values, reference data, or protected configuration parameters.  
**Expected outcome:** The correct test method is being used without unauthorized configuration changes.

### 6. Check Scanner Readiness and Environment
Confirm the scanner has completed startup and any normal preparation required before the test. Check for environmental issues, room temperature problems, power events, or other external conditions that may affect operation.  
**Expected outcome:** The scanner and environment are stable enough for valid testing.

### 7. Repeat the Test Once After Correcting External Setup Issues
If a clear external setup problem was identified and corrected, repeat the approved test according to facility or manufacturer procedure. Avoid repeated attempts intended only to obtain a passing result.  
**Expected outcome:** The test passes consistently. If so, document the original setup cause and stop troubleshooting.

### 8. Compare With Previous QC Information if Available
Review previous approved QC results to determine whether the failure represents a new change or an established trend.  
**Expected outcome:** The service evaluation includes meaningful comparison data without altering acceptance criteria.

### 9. Escalate a Repeated Failure
If the test fails again after correct setup and stable operating conditions are confirmed, discontinue external troubleshooting.  
**Expected outcome:** The scanner remains out of service until qualified personnel determine the cause and complete required verification.

## If the Problem Persists

Incorrect phantom setup, positioning, protocol selection, startup state, and obvious environmental factors have been ruled out. Remaining causes may involve calibration data, detector performance, X-ray generation, alignment, reconstruction, or other internal imaging subsystems.

The scanner should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or service evaluation
- Evaluated using Siemens Healthineers documentation and approved test equipment
- Calibrated, repaired, or configured only by qualified personnel

All required calibration, QC, image-quality, and functional testing should pass before return to clinical service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never adjust calibration values simply to make a failed quality-control test pass.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Treat failed calibration and QC results as performance concerns, verify setup and external conditions first, avoid unauthorized adjustments, and escalate any repeatable failure until the scanner is properly verified.

That is successful troubleshooting.
