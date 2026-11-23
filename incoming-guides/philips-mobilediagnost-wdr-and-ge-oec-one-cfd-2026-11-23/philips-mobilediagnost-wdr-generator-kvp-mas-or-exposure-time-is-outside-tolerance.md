---
schemaVersion: 1
title: "Philips MobileDiagnost wDR Mobile X-Ray System - Generator kVp, mAs, or Exposure Time Is Outside Tolerance"
issueTitle: "Generator kVp, mAs, or Exposure Time Is Outside Tolerance"
description: "Troubleshoots suspected radiographic output inaccuracy using controlled setup, settings verification, and approved measurement before escalating a generator-performance problem."
assetType: "Mobile X-Ray System"
manufacturer: "Philips"
model: "MobileDiagnost wDR"
slug: "philips-mobilediagnost-wdr-generator-kvp-mas-or-exposure-time-is-outside-tolerance"
dateAdded: "2026-11-23"
taxonomyMode: "reuse"
ccr:
  complaint: "Preventive-maintenance testing indicated that the MobileDiagnost wDR exposure-time measurement did not meet the applicable acceptance requirement."
  cause: "Clinical Engineering repeated testing with verified setup and confirmed the exposure timing remained outside the approved requirement."
  resolution: "Clinical Engineering removed the unit from service and referred it for qualified generator evaluation and calibration before return-to-service testing."
helpfulDetails:
  - "Reported parameter"
  - "Selected technique"
  - "Test equipment used"
  - "Test-equipment calibration status"
  - "Measurement geometry"
  - "Repeated results"
  - "Applicable acceptance source"
  - "Historical comparison"
  - "Whether the deviation was setting-specific"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots suspected radiographic output inaccuracy using controlled setup, settings verification, and approved measurement before escalating a generator-performance problem.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Remove Questionable Output From Clinical Use
Do not continue patient imaging with a system suspected of producing inaccurate kVp, mAs, or exposure timing.

Use another verified X-ray system until performance is confirmed.

Expected outcome: Patients are not exposed using equipment with unverified generator accuracy.

### 2. Confirm the Reported Output Concern
Determine whether the issue was identified through:
- Quality-control testing
- Preventive maintenance
- Image-quality complaints
- Exposure inconsistency
- A service measurement

Record the technique settings and test conditions involved.

Expected outcome: The reported output problem is tied to a reproducible test condition.

### 3. Verify the Test Equipment and Setup
Confirm that the radiation analyzer or other approved measurement device:
- Is appropriate for the test
- Is within its required calibration status
- Is positioned correctly
- Is configured correctly
- Is not affected by poor geometry

Expected outcome: The measurement setup is valid before the generator is judged to be out of tolerance.

### 4. Verify Technique Selection
Confirm that the programmed kVp, mAs, mA, and exposure-time selections used in the test are the intended settings.

Do not alter service calibration values.

Expected outcome: The system is being tested against the actual selected technique.

### 5. Check Power and System Condition
Confirm that the MobileDiagnost wDR is in its proper operating state for generator testing and has adequate power.

Follow applicable Philips procedures regarding AC or battery condition during performance testing.

Expected outcome: Generator measurements are not being influenced by an inappropriate power condition or incomplete startup.

### 6. Repeat the Measurement
Repeat the questionable measurement under the same controlled conditions.

Avoid making a repair decision from a single unexplained reading.

Expected outcome: The result is either reproducible or identified as an isolated test anomaly.

### 7. Check Multiple Appropriate Test Points
Using approved Clinical Engineering procedures, evaluate additional relevant technique selections to determine whether the deviation:
- Occurs at one setting
- Occurs over a range
- Affects only timing
- Affects kVp or output more broadly

Do not invent tolerance limits; use applicable manufacturer, regulatory, or facility criteria.

Expected outcome: The scope of the performance problem is objectively defined.

### 8. Compare With Historical or Approved Reference Data
Review prior PM or acceptance-test results if available.

Do not use historical values to override current applicable acceptance requirements.

Expected outcome: A trend or sudden change may support escalation and help identify when performance changed.

### 9. Perform Final Verification if Measurements Are Acceptable
If repeated testing demonstrates that generator performance meets the applicable requirement, document the actual test results and confirm normal operation.

Expected outcome: Generator output is objectively verified. Troubleshooting can stop when applicable criteria are met.

### 10. Escalate Confirmed Generator Inaccuracy
If kVp, mAs, exposure time, or related generator performance does not meet applicable requirements, remove the system from service.

Do not perform unauthorized calibration adjustments.

Expected outcome: A confirmed radiation-output problem is referred for qualified service and calibration.

## If the Problem Persists

Common external and measurement causes such as test setup, analyzer configuration, technique selection, operating condition, and isolated measurement error have been ruled out.

The remaining problem may involve generator regulation, timing control, calibration, power electronics, measurement feedback, or other service-level functions.

The device should be:
- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Philips documentation and approved radiation test equipment
- Calibrated or repaired only by qualified personnel

After service, repeat all required generator-performance and return-to-service tests using applicable criteria.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never adjust generator calibration simply to make one measurement agree; first verify the analyzer, geometry, selected technique, and repeatability.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Generator accuracy must be proven by controlled measurement, not assumed from image appearance alone. Verify test equipment, geometry, technique, and repeatability before declaring a failure, then remove the system from service when performance does not meet applicable requirements.

That is successful troubleshooting.
