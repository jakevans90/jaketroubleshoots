---
schemaVersion: 1
title: "Carestream DRX-Rise Mobile X-Ray System - Generator Output, kVp, mA, or Exposure Time Is Out of Tolerance"
issueTitle: "Generator Output, kVp, mA, or Exposure Time Is Out of Tolerance"
description: "Troubleshoot suspected generator performance problems using setup verification, approved test equipment, repeatable measurements, power checks, and proper escalation."
assetType: "Mobile X-Ray System"
manufacturer: "Carestream"
model: "DRX-Rise"
slug: "carestream-drx-rise-generator-output-kvp-ma-or-exposure-time-is-out-of-tolerance"
dateAdded: "2026-11-18"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported inconsistent image exposure and requested generator output verification on the DRX-Rise."
  cause: "Clinical Engineering repeated testing with calibrated radiation test equipment and confirmed exposure output remained outside the applicable approved acceptance criteria."
  resolution: "Removed the unit from service and referred it for qualified generator calibration and repair before return-to-service testing."
helpfulDetails:
  - "Parameter reported out of tolerance"
  - "Technique settings tested"
  - "Test geometry"
  - "Test instrument used"
  - "Calibration status of analyzer"
  - "Power condition during testing"
  - "Repeat measurement results"
  - "Applicable acceptance criteria source"
  - "Whether image quality was affected"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoot suspected generator performance problems using setup verification, approved test equipment, repeatable measurements, power checks, and proper escalation.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Unverified Radiation Output
Remove the DRX-Rise from clinical imaging if generator output is suspected to be inaccurate or inconsistent. Do not test questionable output on patients.  
Expected outcome: No patient is exposed using an unverified generator.

### 2. Confirm the Reported Performance Concern
Determine whether the concern involves kVp accuracy, output consistency, exposure time, mA-related performance, unexpectedly light or dark images, or a failed quality-control measurement.  
Expected outcome: The specific generator-performance complaint is defined.

### 3. Verify the Test Setup
Confirm the measurement instrument, detector placement, geometry, technique selection, and test method are appropriate for the intended generator test.  
Expected outcome: The test setup is valid before concluding the generator is inaccurate.

### 4. Check the Measurement Equipment
Verify the radiation analyzer or other test instrument is within its required calibration status and configured correctly for the measurement.  
Expected outcome: Test equipment is suitable and trustworthy.

### 5. Verify System Power and Battery Condition
Confirm the mobile system has normal power availability and is being tested under the appropriate manufacturer-approved operating condition.  
Expected outcome: Low or abnormal system power is not influencing the test.

### 6. Repeat the Measurement
Repeat the same approved test conditions to determine whether the result is consistent or was caused by setup variation.  
Expected outcome: Measurements are repeatable and can be meaningfully compared with approved performance criteria.

### 7. Check Technique Entry and Acquisition Setup
Confirm the selected technique values are the intended values and that no protocol, examination, or operator entry error explains the discrepancy.  
Expected outcome: Commanded exposure settings match the planned test.

### 8. Compare With Approved Acceptance Criteria
Evaluate measured kVp, exposure time, output, or related parameters only against applicable Carestream, facility, regulatory, or approved quality-control criteria. Do not invent tolerances.  
Expected outcome: Generator performance is clearly categorized as acceptable or outside approved limits.

### 9. Perform Final Verification if Results Are Acceptable
If repeated measurements meet the appropriate criteria, document the setup and results and verify normal image acquisition before returning the system to service.  
Expected outcome: Generator performance is verified and troubleshooting can stop.

### 10. Escalate Out-of-Tolerance Generator Performance
If measurements remain outside approved limits, do not attempt unauthorized internal calibration or generator adjustment.  
Expected outcome: The system remains out of clinical service for qualified repair and calibration.

## If the Problem Persists

External setup, measurement equipment, technique entry, power conditions, and repeatability have been checked. Remaining causes may involve generator calibration, high-voltage components, timing circuitry, current regulation, internal power electronics, sensors, or service-level configuration.

Remove the DRX-Rise from service, label it **Out of Service**, and arrange repair or bench evaluation using appropriate Carestream documentation and approved radiation test equipment.

Any generator adjustment or calibration should be performed only by qualified personnel. After repair, repeat all required generator performance and image-quality checks before return to clinical use.

Knowing when measured performance requires escalation instead of internal adjustment is proper troubleshooting.

## Clinical Use Tip

Always verify a suspected generator problem with calibrated test equipment before assuming image appearance alone proves an output failure.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Treat suspected radiation-output problems conservatively, verify the test setup before blaming the generator, use only approved limits, and escalate confirmed performance failures for qualified service.

That is successful troubleshooting.
