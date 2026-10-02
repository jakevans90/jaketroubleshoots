---
schemaVersion: 1
title: "Mindray Resona I9 Ultrasound System - Calibration or Quality-Control Test Fails"
issueTitle: "Calibration or Quality-Control Test Fails"
description: "Use when an approved ultrasound quality-control check or calibration-related verification does not complete or produces an unacceptable result."
assetType: "Ultrasound System"
manufacturer: "Mindray"
model: "Resona I9"
slug: "mindray-resona-i9-calibration-or-quality-control-test-fails"
dateAdded: "2026-10-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical Engineering reported that a routine image-quality check on the Resona I9 did not meet the approved test criteria."
  cause: "Clinical Engineering found inadequate acoustic coupling between the test object and transducer during the original check."
  resolution: "Clinical Engineering corrected the test setup, repeated the approved QC procedure successfully, verified normal live imaging, and returned the system to service."
helpfulDetails:
  - "Exact QC test performed"
  - "Applicable acceptance criteria source"
  - "Probe used"
  - "Test object or phantom used"
  - "Original result"
  - "Coupling and positioning"
  - "Imaging settings observed"
  - "Known-good probe comparison"
  - "Repeat test result"
  - "Any displayed message"
  - "Final device status"
---
## What This Guide Helps With

Use when an approved ultrasound quality-control check or calibration-related verification does not complete or produces an unacceptable result.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Reliability
If a required quality-control test has failed and the result calls diagnostic performance into question, do not use the affected system or probe for patient examinations until the failure is evaluated according to facility policy.

**Expected outcome:** Questionable equipment is prevented from affecting patient diagnosis.

### 2. Identify the Exact Failed Test
Record the specific QC or calibration-related test, probe used, imaging mode, test object, displayed result, and whether the failure is repeatable. Do not substitute an invented acceptance criterion for the approved procedure.

**Expected outcome:** The exact failed verification and its approved acceptance criteria are known.

### 3. Verify the Test Setup
Confirm the correct test object, phantom, probe, coupling method, positioning, and approved procedure were used. Check that the test materials are in suitable condition and have been prepared as required by the applicable procedure.

**Expected outcome:** The test setup matches the approved QC method. If correcting the setup produces a passing result, troubleshooting can stop after repeat verification.

### 4. Inspect the Probe
Check the probe surface, housing, cable, strain relief, and connector for contamination or visible damage that could affect the test.

**Expected outcome:** The transducer is clean, undamaged, and correctly connected.

### 5. Verify Imaging Settings
Confirm the QC procedure is being performed with the required user-accessible imaging settings or approved preset. Do not adjust protected calibration values or service parameters merely to obtain a passing result.

**Expected outcome:** The test is performed using the correct approved configuration.

### 6. Repeat the Test Under Controlled Conditions
Repeat the failed QC check using the same approved method after correcting any external setup issue. Record both the original and repeat results.

**Expected outcome:** The test passes consistently. If it does, document the external cause and complete final verification.

### 7. Compare With a Known-Good Compatible Probe When Appropriate
If the procedure permits, repeat the relevant check using a known-good compatible probe to determine whether the failure follows the transducer.

**Expected outcome:** The failure is isolated to a specific probe or shown to affect the broader imaging system.

### 8. Check Environmental Conditions
Verify that room conditions, electrical interference, poor coupling, equipment placement, or other obvious environmental factors are not affecting the QC result.

**Expected outcome:** The failed test is not caused by an external environmental condition.

### 9. Perform Final Verification
Repeat the approved test enough to establish that the corrected condition is stable, and verify normal live imaging before return to service.

**Expected outcome:** The required QC result meets the applicable approved acceptance criteria and basic imaging is normal. If successful, troubleshooting can stop.

## If the Problem Persists

Test setup, probe condition, approved settings, repeat testing, and relevant external factors have been ruled out. Persistent QC or calibration failure may involve a transducer, acquisition path, calibration state, image-processing subsystem, software, or another service-level condition.

Remove the affected probe or system from service, label it **Out of Service**, and send it for repair or bench evaluation. Use current Mindray service documentation, the facility's approved QC procedure, appropriate ultrasound test equipment, and qualified service personnel.

Do not alter internal calibration values or restricted service parameters without authorized procedures. Return the equipment to service only after the required QC or calibration verification passes.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A failed QC result should not be cleared simply because the live image appears acceptable; resolve the reason for the failed verification before clinical use.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Treat QC failures as potential diagnostic-performance concerns, verify the test method and external setup before assuming internal failure, never bypass approved criteria, escalate persistent failures, and document the final verification.

That is successful troubleshooting.
