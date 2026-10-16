---
schemaVersion: 1
title: "Canon Aplio i900 CV Echocardiography System - Self-Test or Calibration Will Not Complete"
issueTitle: "Self-Test or Calibration Will Not Complete"
description: "Troubleshooting incomplete self-test or calibration caused by startup state, connected accessories, setup conditions, external interference, configuration, or service-level problems."
assetType: "Echocardiography System"
manufacturer: "Canon"
model: "Aplio i900 CV"
slug: "canon-aplio-i900-cv-self-test-or-calibration-will-not-complete"
dateAdded: "2026-10-16"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Aplio i900 CV would not complete an expected system verification after a probe was connected."
  cause: "Clinical Engineering found contamination on the accessible probe connector that prevented a reliable connection."
  resolution: "Clinical Engineering cleaned and reconnected the probe using the approved method, repeated the verification successfully, confirmed basic imaging operation, and returned the system to service."
helpfulDetails:
  - "Exact self-test or calibration process"
  - "Exact displayed message"
  - "Point at which the process stopped"
  - "AC power status"
  - "Probe or accessory involved"
  - "Connector condition"
  - "Known-good substitution results"
  - "Result after restart"
  - "Final test result"
  - "Final device status"
---

## What This Guide Helps With
Troubleshooting incomplete self-test or calibration caused by startup state, connected accessories, setup conditions, external interference, configuration, or service-level problems.

## Step-by-Step Troubleshooting
### 1. Protect the Patient and Remove the System From Clinical Dependence
Do not use the Aplio i900 CV for patient imaging when a required self-test or calibration has failed and system performance cannot be verified. Move the examination to another verified system.
**Expected outcome:** Patient care continues without relying on unverified equipment.

### 2. Confirm Which Test Is Failing
Identify whether the problem occurs during startup self-test, a user-accessible calibration, or another approved verification process. Record the exact displayed message, stage, and circumstances of the failure. Do not enter restricted service menus.
**Expected outcome:** The failed process and repeatable symptom are clearly identified.

### 3. Verify Normal Startup and Stable Power
Confirm the system starts normally and is connected to a verified AC source. An unstable power source or incomplete startup can prevent tests from completing reliably.
**Expected outcome:** Stable power and normal system readiness are confirmed.

### 4. Check Required External Accessories and Connections
Verify that any accessory, probe, cable, or approved test item required for the particular procedure is present, compatible, correctly connected, and undamaged. Remove unrelated accessories if appropriate.
**Expected outcome:** The test has the correct external setup and no obvious connection problem.

### 5. Inspect for Contamination or Physical Damage
Check relevant accessible connectors, probe surfaces, cables, accessories, and external interfaces for gel, liquid, debris, bent areas, damage, or poor seating. Correct only external issues within Clinical Engineering scope.
**Expected outcome:** External components required for testing are clean, intact, and properly connected.

### 6. Verify Applicable Settings and Test Conditions
Confirm that the system is in the proper normal operating state for the approved self-test or calibration being performed. Verify relevant user-accessible settings against approved documentation. Do not change protected configuration simply to make a test pass.
**Expected outcome:** The test is being performed under the correct supported conditions.

### 7. Use a Known-Good Compatible Accessory When Appropriate
If the failing test depends on a probe or external accessory, substitute a known-good compatible item when available. Repeat only the approved test.
**Expected outcome:** A successful test with the known-good accessory isolates the original accessory as the likely cause.

### 8. Perform a Controlled Restart and Repeat Once
If no external cause is found, perform a normal shutdown and restart. Repeat the test under the same correct conditions. Avoid repeated test cycling when the same failure consistently returns.
**Expected outcome:** The self-test or calibration completes normally. If it does, proceed to functional verification.

### 9. Verify Normal Imaging Function
After a successful test, verify basic imaging operation and any functions related to the failed process. Complete return-to-service testing required by policy.
**Expected outcome:** The test passes and the system performs normally. Troubleshooting can stop.

### 10. Escalate a Repeatable Test Failure
If the same self-test or calibration failure remains after external setup, accessory, power, and restart checks, stop troubleshooting at the external level. Do not bypass the failure or alter unauthorized calibration data.
**Expected outcome:** An unresolved calibration, software, hardware, or internal communication issue is referred for qualified service.

## If the Problem Persists
Common external setup, accessory, power, connection, and operating-condition causes have been ruled out. The remaining issue may involve internal calibration data, software, imaging hardware, sensors, internal communication, or another manufacturer service-level condition.

Remove the system from service, label it Out of Service, and send it for repair or bench evaluation. Evaluate it using appropriate Canon documentation and approved test equipment. Calibration adjustments, service configuration, or internal repairs should be performed only by qualified personnel.

Successful completion of the applicable test and subsequent functional verification are required before return to service. Knowing when not to bypass a failed verification is proper troubleshooting.

## Clinical Use Tip
A required self-test or calibration failure should be treated as an unresolved performance issue until the system passes the appropriate verification.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Protect the patient from unverified equipment, confirm setup and external dependencies first, never bypass a failed test merely to restore availability, verify proper operation after correction, escalate persistent failures, and document the final test result.

That is successful troubleshooting.
