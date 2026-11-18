---
schemaVersion: 1
title: "GE Healthcare AMX Navigate Mobile X-Ray System - Dose Indicator, Exposure Index, or Generator Output Is Out of Tolerance"
issueTitle: "Dose Indicator, Exposure Index, or Generator Output Is Out of Tolerance"
description: "Measured generator output, dose-related indication, or exposure index appears inconsistent, abnormal, or outside approved performance criteria."
assetType: "Mobile X-Ray System"
manufacturer: "GE Healthcare"
model: "AMX Navigate"
slug: "ge-healthcare-amx-navigate-dose-indicator-exposure-index-or-generator-output-is-out-of-tolerance"
dateAdded: "2026-11-18"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported unexpectedly high exposure-index values during routine imaging with the AMX Navigate."
  cause: "Clinical Engineering found the generator output was repeatable during approved testing and identified an incorrect examination-processing selection being used during the affected studies."
  resolution: "Restored the approved examination selection, verified normal exposure-index behavior with controlled test imaging, and confirmed generator performance remained within applicable acceptance criteria."
helpfulDetails:
  - "Parameter reported abnormal"
  - "Technique used"
  - "Detector identification"
  - "Examination or processing selection"
  - "Test equipment used"
  - "Calibration status of test equipment"
  - "Test geometry"
  - "Repeated measurement results"
  - "Collimation and accessory setup"
  - "Detector calibration status"
  - "Final QC result"
  - "Final device status"
---

## What This Guide Helps With

Measured generator output, dose-related indication, or exposure index appears inconsistent, abnormal, or outside approved performance criteria.

## Step-by-Step Troubleshooting

### 1. Remove Questionable Radiation Output From Patient Use
If generator output or dose performance is suspected to be outside acceptable limits, do not continue clinical exposures merely to investigate the complaint.

Expected outcome: Patient imaging does not continue using potentially inaccurate radiation output.

### 2. Define the Reported Problem
Determine whether the concern involves:
- Measured generator output
- Exposure reproducibility
- Dose-related indication
- Exposure index
- Unexpectedly high or low image receptor response
- A single technique
- Multiple techniques

Expected outcome: The exact parameter and conditions associated with the complaint are identified.

### 3. Confirm the Detector and Image-Processing Context
If the concern is exposure index rather than measured generator output, verify the detector used, examination selection, processing protocol, collimation, and positioning are appropriate.

Expected outcome: A workflow or detector-selection issue is not being mistaken for a generator problem.

### 4. Verify the Test Setup
For quantitative output testing, confirm:
- Approved test equipment is being used
- Test equipment is within applicable calibration status
- Geometry is repeatable
- The detector or meter is positioned correctly
- The same setup is used for comparison measurements

Expected outcome: The measurement setup itself is reliable.

### 5. Repeat the Measurement
Repeat the approved quality-control test under the same controlled conditions.

Expected outcome: The abnormal result is either reproduced or identified as a one-time test/setup issue.

### 6. Inspect External Conditions
Check for factors that could alter results, including:
- Unexpected filtration or objects in the beam
- Incorrect detector placement
- Collimation changes
- Wrong examination selection
- Incorrect accessory or grid use
- Inconsistent test geometry

Expected outcome: External setup variables are ruled out.

### 7. Compare Multiple Approved Test Points
If required by the applicable QC procedure, compare results at additional approved operating points rather than concluding failure from a single measurement.

Expected outcome: The problem is confirmed as isolated or systematic.

### 8. Compare With Image Receptor Performance
Where appropriate, confirm detector calibration and image quality are acceptable. An abnormal exposure index may reflect detector or processing issues even when measured generator output is acceptable.

Expected outcome: Generator performance is separated from detector and processing behavior.

### 9. Do Not Adjust Calibration Without Approved Procedure
Do not alter generator calibration, dose configuration, or protected service parameters based solely on a suspected discrepancy.

Expected outcome: No unauthorized adjustment masks the actual cause.

### 10. Perform Final Approved QC Verification
If an external or configuration-related cause is corrected, repeat the appropriate approved quality-control test.

Expected outcome: Results meet the applicable manufacturer, regulatory, and facility acceptance criteria. Troubleshooting can stop.

### 11. Escalate Confirmed Out-of-Tolerance Performance
If output remains outside approved criteria, remove the unit from clinical service and escalate for qualified generator/service evaluation.

Expected outcome: A system with unverified radiation output is not returned to patient use.

## If the Problem Persists

Common test-setup, detector, processing, positioning, and external causes have been ruled out. Remaining possibilities may involve generator calibration, tube output, high-voltage generation, detector response, image processing, system configuration, or another service-level imaging function.

The system should be:
- Removed from service
- Labeled Out of Service
- Evaluated using approved GE Healthcare service documentation
- Tested with calibrated radiation measurement equipment
- Repaired or calibrated only by qualified personnel

Return-to-service testing must verify all applicable performance and radiation-safety criteria before clinical use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

An exposure index is not by itself a direct generator-output measurement; evaluate detector, technique, collimation, and processing before drawing conclusions.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Dose and output concerns require measured verification, not assumptions. Confirm the test setup, detector, processing, and acquisition conditions before considering generator calibration, and remove the system from service whenever radiation output cannot be verified.

That is successful troubleshooting.
