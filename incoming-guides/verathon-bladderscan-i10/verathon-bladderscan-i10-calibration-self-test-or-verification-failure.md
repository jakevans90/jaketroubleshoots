---
schemaVersion: 1
title: "Verathon BladderScan i10 Bladder Scanner - Calibration, Self-Test, or Verification Failure"
issueTitle: "Calibration, Self-Test, or Verification Failure"
description: "Addresses failed performance checks caused by setup, probe condition, test accessory, positioning, power, environment, procedure, or service-level faults."
assetType: "Bladder Scanner"
manufacturer: "Verathon"
model: "BladderScan i10"
slug: "verathon-bladderscan-i10-calibration-self-test-or-verification-failure"
dateAdded: "2026-08-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the BladderScan i10 failed its scheduled performance verification."
  cause: "Clinical Engineering found that the approved verification target was contaminated with dried gel and was not positioned correctly."
  resolution: "Clinical Engineering cleaned and repositioned the test accessory, repeated the approved verification successfully, and completed final functional testing."
helpfulDetails:
  - "Exact failed test or message"
  - "Test stage"
  - "Procedure and document used"
  - "Test accessory identification"
  - "Test equipment calibration status"
  - "Probe condition"
  - "Battery or AC operation"
  - "Environmental conditions"
  - "Known-good comparison result"
  - "Repeat test results"
  - "Final return-to-service status"
---

## What This Guide Helps With

Addresses failed performance checks caused by setup, probe condition, test accessory, positioning, power, environment, procedure, or service-level faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Unverified Measurements

Do not use the scanner for patient-care decisions after a failed calibration, self-test, or performance verification. Provide another verified scanner.

Clearly identify the device to prevent clinical reuse until the failure is resolved and documented.

**Expected outcome:** Patient care continues with equipment of verified performance.

### 2. Confirm the Type of Failure

Determine whether the failure occurred during:

- Startup self-test
- Routine functional verification
- Calibration procedure
- Approved phantom or verifier test
- Post-repair testing
- A software-generated maintenance prompt

Record the exact message, stage, and observed result. Do not invent acceptance limits or repeat procedures without knowing which test failed.

**Expected outcome:** The specific failed process and test stage are identified.

### 3. Review the Approved Procedure and Equipment

Confirm that the correct Verathon documentation, approved verifier or phantom, compatible probe, required accessories, and current facility procedure are being used.

Check that the test equipment is within its required calibration or verification status.

**Expected outcome:** The correct test method and valid test equipment are confirmed.

### 4. Verify Stable Power

Confirm adequate battery charge or connect approved external power. Ensure the device does not dim, restart, or shut down during the test.

Do not perform a performance test under unstable power conditions.

**Expected outcome:** The device remains powered and stable throughout the verification process.

### 5. Inspect the Probe

Inspect the probe surface, housing, cable, strain relief, and connector for cracks, wear, dried gel, contamination, impact damage, or loose connection.

Clean and prepare the probe using the approved method. Reseat the connector if applicable.

**Expected outcome:** The probe is clean, intact, and securely connected. If correction allows the test to pass, continue with repeat verification.

### 6. Inspect the Verification Accessory

Examine the approved phantom, target, stand, or verification accessory for contamination, damage, incorrect assembly, trapped air, missing components, or expired status when applicable.

Do not substitute improvised containers or materials.

**Expected outcome:** The verification accessory is suitable, correctly assembled, and ready for use.

### 7. Check Positioning and Test Setup

Position the probe and verification accessory exactly as required by the approved procedure. Stabilize both components and avoid movement during acquisition.

Confirm that the correct device mode and test selection are active.

**Expected outcome:** The test setup is repeatable and free of positioning error.

### 8. Check Environmental Conditions

Perform the test in a stable indoor environment away from vibration, direct heat, condensation, and strong electromagnetic interference.

Allow the device and test accessory to reach the same room environment after transport or storage.

**Expected outcome:** Environmental conditions do not interfere with the test.

### 9. Repeat the Test Once Using Corrected Setup

After correcting any external setup issue, repeat the complete test from the beginning. Do not repeatedly retest a failing device in an attempt to obtain a passing result.

**Expected outcome:** The device passes the approved check consistently. A single inconsistent pass is not sufficient for return to service.

### 10. Compare With a Known-Good Component

When permitted, compare the device using a known-good compatible probe, approved verifier, or another verified scanner with the same test accessory.

This comparison should isolate the scanner, probe, or verification accessory without altering internal calibration data.

**Expected outcome:** The failing component or test setup is narrowed to the scanner, probe, or accessory.

### 11. Verify Calibration and Configuration Status

Confirm that the device’s calibration or maintenance status matches the approved service record. Do not change calibration coefficients, enter restricted service menus, or clear maintenance conditions without authorization.

**Expected outcome:** No unauthorized or undocumented configuration change is made. Any service-level calibration requirement is escalated appropriately.

### 12. Complete Return-to-Service Verification

A device that passes must complete the full required verification, not only the previously failed portion. Confirm startup, probe recognition, scan completion, result display, data storage, and applicable safety checks.

**Expected outcome:** All required tests pass consistently and are documented before the device returns to service.

## If the Problem Persists

External causes involving the procedure, power, probe, verification accessory, positioning, environmental conditions, and approved configuration have been ruled out.

The remaining cause may involve probe performance, ultrasound acquisition hardware, system software, internal calibration data, or another service-level condition. Do not adjust internal calibration or replace boards without approved documentation, training, and test equipment.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Verathon documentation and approved test equipment
- Repaired, calibrated, or configured only by qualified personnel

After service, complete the manufacturer-supported calibration or verification process, functional testing, and all required return-to-service documentation.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A scanner that cannot pass its required verification must not be used to support bladder-volume decisions.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

A failed verification is a patient-safety condition, not a result to work around. Confirm the procedure, test equipment, setup, probe, power, and environment before assuming internal failure. Escalate unresolved performance problems and document the complete CCR and final test results.

That is successful troubleshooting.

