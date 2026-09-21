---
schemaVersion: 1
title: "Stryker CrossFlow Fluid Management System - Self-Test or Calibration Will Not Complete"
issueTitle: "Self-Test or Calibration Will Not Complete"
description: "Troubleshoots CrossFlow self-test, setup verification, or calibration functions that fail, stop, repeat, or will not complete normally."
assetType: "Fluid Management System"
manufacturer: "Stryker"
model: "CrossFlow"
slug: "stryker-crossflow-self-test-or-calibration-will-not-complete"
dateAdded: "2026-09-21"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported the CrossFlow setup verification would repeatedly stop before completion."
  cause: "Clinical Engineering found a required external tubing component was kinked during the verification setup."
  resolution: "The tubing was repositioned, the verification completed successfully, and normal fluid-management operation was confirmed before return to service."
helpfulDetails:
  - "Exact test or calibration attempted"
  - "Displayed message"
  - "Point where the process fails"
  - "Accessories and consumables installed"
  - "Tubing condition and positioning"
  - "Known-good substitutions"
  - "Connection inspection results"
  - "Restart result"
  - "Final test result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots CrossFlow self-test, setup verification, or calibration functions that fail, stop, repeat, or will not complete normally.

## Step-by-Step Troubleshooting

### 1. Remove the System From Patient Use

Do not attempt to clear a failed self-test or calibration while a patient depends on the system. A system that cannot complete a required verification should not be considered ready for clinical use.

**Expected outcome:** Testing occurs in a controlled nonpatient environment.

### 2. Confirm Which Test Is Failing

Determine the exact test, calibration, startup verification, or setup procedure involved. Record any displayed text exactly as shown.

Determine whether the failure occurs:

- Immediately
- At the same point each time
- Only with a particular accessory
- After changing a disposable component
- After transport or cleaning
- During routine maintenance

**Expected outcome:** The failing process and stage are clearly identified.

### 3. Verify Required Setup Conditions

Using applicable manufacturer documentation, verify all externally required components are installed correctly for the test being performed.

Check tubing, accessories, fluid sources, connections, and other required setup items only as applicable to that procedure.

**Expected outcome:** The test setup matches the required external configuration. If correcting setup allows successful completion, the issue is resolved.

### 4. Inspect Accessories and Consumables

Inspect all components involved in the test for damage, incorrect installation, kinks, occlusion, contamination, improper positioning, or obvious incompatibility.

**Expected outcome:** Accessories and consumables are appropriate, intact, and correctly installed.

### 5. Verify the System Is in the Correct Operating State

Confirm startup has completed normally and the system is in the proper mode for the requested test. Verify no unrelated active alarm or incomplete setup condition is blocking the process.

**Expected outcome:** The console is ready to perform the applicable test.

### 6. Repeat the Test With a Known-Good Setup

When appropriate, substitute verified compatible accessories or consumables and repeat the test using the documented procedure.

Do not bypass a failed self-test or force a calibration value.

**Expected outcome:** If the test passes with known-good components, the original external component or setup was responsible.

### 7. Evaluate Connections and Positioning

Inspect accessible connection points, sensors, tubing placement, and component positioning involved in the test. Reseat components when appropriate.

**Expected outcome:** All required external interfaces are secure and correctly positioned. The test completes normally if poor connection or positioning was the cause.

### 8. Perform a Normal Restart

If the external setup is correct and no hazardous condition exists, shut the CrossFlow down normally, restart it, rebuild the test setup, and repeat the documented process.

**Expected outcome:** The test completes successfully and remains repeatable. A one-time recovery should still be followed by complete verification.

### 9. Verify the Result Before Return to Service

After a successful test or calibration, verify normal fluid-management operation, controls, displays, alarms, and associated functions using approved test methods.

**Expected outcome:** Required tests pass and normal function is confirmed. Troubleshooting can stop.

### 10. Escalate Repeated Test Failure

If correct setup, known-good accessories, positioning, connections, and normal restart do not resolve the failure, stop troubleshooting.

**Expected outcome:** The device is removed from service and evaluated by qualified personnel rather than having the test bypassed.

## If the Problem Persists

Common external setup and accessory causes have been ruled out. Remaining categories may include sensors, internal measurement systems, protected calibration data, software, internal communication, or other service-level faults.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Stryker documentation and approved test equipment
- Repaired, calibrated, or configured only by qualified personnel

Do not return a device to clinical service when a required self-test or calibration cannot be completed successfully. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A completed setup screen is not a substitute for a required self-test or calibration; verify the actual required check has passed before clinical use.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

A failed self-test or calibration should be treated as meaningful until proven otherwise. Verify setup and external components carefully, never bypass required checks, and escalate persistent failures with complete documentation.

That is successful troubleshooting.
