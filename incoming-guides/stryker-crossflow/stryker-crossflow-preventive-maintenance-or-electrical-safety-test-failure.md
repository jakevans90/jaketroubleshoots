---
schemaVersion: 1
title: "Stryker CrossFlow Fluid Management System - Preventive Maintenance or Electrical Safety Test Failure"
issueTitle: "Preventive Maintenance or Electrical Safety Test Failure"
description: "Troubleshoots CrossFlow PM or electrical-safety failures by verifying setup, external components, test equipment, configuration, and repeatability before service escalation."
assetType: "Fluid Management System"
manufacturer: "Stryker"
model: "CrossFlow"
slug: "stryker-crossflow-preventive-maintenance-or-electrical-safety-test-failure"
dateAdded: "2026-09-21"
taxonomyMode: "reuse"
ccr:
  complaint: "The Stryker CrossFlow failed an electrical-safety check during scheduled preventive maintenance."
  cause: "Clinical Engineering isolated the failure to a damaged detachable AC power cord while the console itself passed testing with a verified approved cord."
  resolution: "The defective power cord was replaced, the electrical-safety test was repeated successfully, and the CrossFlow completed the remaining functional PM checks before return to service."
helpfulDetails:
  - "Exact PM or safety test failed"
  - "Actual measured result"
  - "Applicable acceptance requirement"
  - "Test-equipment identification"
  - "Test-equipment calibration status"
  - "Analyzer configuration"
  - "Power cord inspection result"
  - "Known-good cord substitution"
  - "Repeat measurement result"
  - "Functional-test results"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots CrossFlow PM or electrical-safety failures by verifying setup, external components, test equipment, configuration, and repeatability before service escalation.

## Step-by-Step Troubleshooting

### 1. Keep the Device Out of Clinical Service

A CrossFlow that has failed a required PM or electrical-safety test should not be returned to clinical use until the failure has been understood, corrected when appropriate, and successfully retested.

**Expected outcome:** The device remains controlled by Clinical Engineering until testing is complete.

### 2. Identify the Exact Failed Test

Document which inspection, functional test, performance test, or electrical-safety measurement failed.

Record the actual result and applicable acceptance requirement from approved documentation rather than simply writing "PM failed."

**Expected outcome:** The specific failed requirement is clearly identified and reproducible.

### 3. Verify the Test Procedure and Equipment

Confirm the correct approved procedure is being used and that test equipment:

- Is appropriate for the measurement
- Is within its required calibration status
- Is configured correctly
- Has intact leads and accessories
- Is connected properly

**Expected outcome:** The failure is confirmed using a valid test method and reliable test equipment.

### 4. Perform the Visual Inspection

Inspect the CrossFlow for:

- Damaged enclosure
- Loose hardware
- Damaged power cord
- Damaged plug
- Compromised strain relief
- Contamination or fluid intrusion
- Damaged connectors
- Blocked ventilation
- Missing or damaged external components

**Expected outcome:** No visible condition compromises safe operation. Any safety-related physical defect must be corrected before further return-to-service testing.

### 5. Verify the Power Cord and External Power Path

For electrical-safety concerns, inspect and test the detachable power cord separately when appropriate. Confirm the console is connected in the test configuration required by the approved procedure.

Substitute a known-good approved cord if the original cord is suspect.

**Expected outcome:** A cord-related failure is isolated from a console-related failure. If a defective cord was the cause, replace it and repeat the complete applicable test.

### 6. Confirm the Test Configuration

Verify accessories, applied parts if applicable, external interfaces, and operating state match the approved PM or electrical-safety procedure.

Incorrect test configurations can produce misleading results.

**Expected outcome:** The CrossFlow is tested in the correct configuration.

### 7. Repeat the Failed Measurement

After verifying procedure, analyzer setup, leads, power cord, and configuration, repeat the specific failed test.

Do not average away a failed result or alter acceptance criteria.

**Expected outcome:** The measurement either passes consistently or confirms a reproducible equipment failure.

### 8. Continue the Complete PM if the Failure Is Corrected

If an external test-setup issue or replaceable external component caused the failure, restart or continue the applicable PM process as required rather than assuming the rest of the device is acceptable.

**Expected outcome:** All required PM and safety checks are completed successfully.

### 9. Perform Complete Functional Verification

Verify startup, display and controls, alarms, applicable fluid-management functions, accessories, and any required performance measurements using approved documentation and calibrated test equipment.

**Expected outcome:** The entire required inspection and test process passes. The unit can be returned to service according to local policy.

### 10. Escalate a Confirmed Device Failure

If the failure remains after test setup, equipment, power cord, and external configuration have been verified, stop external troubleshooting.

Do not open the console or attempt board-level repair solely to clear a PM failure.

**Expected outcome:** The device remains out of service and is sent for qualified repair or bench evaluation.

## If the Problem Persists

The test method, analyzer, external power components, and test configuration have been verified. A persistent failure may involve protective grounding, insulation, internal power components, performance calibration, fluid-management hardware, sensing, alarms, or another service-level condition depending on the failed test.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Stryker documentation and approved test equipment
- Repaired, calibrated, or configured only by qualified personnel

After repair, repeat all required affected tests and any complete return-to-service testing required by the approved procedure. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not convert a failed PM result into a pass by changing the test method or acceptance criterion; resolve the reason for the failure first.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

A failed PM or safety test requires verification, not assumptions. Confirm the test setup and external components first, preserve valid acceptance criteria, escalate confirmed device failures, and document the complete path from failure to final disposition.

That is successful troubleshooting.
