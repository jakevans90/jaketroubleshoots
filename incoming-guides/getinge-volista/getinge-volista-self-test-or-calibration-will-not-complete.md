---
schemaVersion: 1
title: "Getinge Volista Surgical Light - Self-Test or Calibration Will Not Complete"
issueTitle: "Self-Test or Calibration Will Not Complete"
description: "Troubleshoots an applicable Volista test or calibration process that cannot complete because of setup, positioning, connection, environment, or service-level conditions."
assetType: "Surgical Light"
manufacturer: "Getinge"
model: "Volista"
slug: "getinge-volista-self-test-or-calibration-will-not-complete"
dateAdded: "2026-09-17"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical Engineering reported that an applicable Volista verification procedure repeatedly stopped before completion."
  cause: "Inspection found an accessory required by the procedure was not fully connected."
  resolution: "Clinical Engineering corrected the connection, repeated the approved procedure successfully, verified normal light operation, and returned the system to service."
helpfulDetails:
  - "Exact procedure attempted"
  - "Exact displayed message or indication"
  - "Point where the test stopped"
  - "Power and startup condition"
  - "Required component positioning"
  - "Accessory and connection condition"
  - "Environmental conditions"
  - "Test equipment used"
  - "Test equipment calibration status"
  - "Final verification result"
---

## What This Guide Helps With
Troubleshoots an applicable Volista test or calibration process that cannot complete because of setup, positioning, connection, environment, or service-level conditions.

## Step-by-Step Troubleshooting
### 1. Protect the Patient and Remove the Light From Clinical Dependence
Do not perform technical testing or calibration while a procedure depends on the affected light. Provide verified alternate illumination and place the system in an appropriate service condition.

**Expected outcome:** Testing can proceed without compromising patient care.

### 2. Verify That the Requested Procedure Applies
Determine exactly which self-test, verification, or calibration procedure is being attempted. Confirm from current Getinge documentation that the procedure is applicable to the installed Volista configuration and that Clinical Engineering is authorized to perform it.

**Expected outcome:** The correct procedure and required authorization are established. Do not invent or substitute a calibration process.

### 3. Record the Point of Failure
Repeat the applicable test only under safe conditions and record where it stops, what indicators are shown, and whether the failure is repeatable. Preserve any exact displayed message without paraphrasing it into an assumed diagnosis.

**Expected outcome:** The failure is consistently characterized.

### 4. Verify Normal Power and Startup
Confirm that the system powers normally and completes ordinary startup before attempting a service test or calibration. Resolve unstable power or startup conditions first.

**Expected outcome:** The Volista is stable in normal operation. If the test subsequently completes, perform the required functional verification and stop.

### 5. Verify Required Setup and Positioning
Confirm that light heads, controls, accessories, and other applicable components are positioned and configured as specified by the approved procedure. Remove unintended obstructions and ensure required components are connected.

**Expected outcome:** Test conditions match applicable documentation.

### 6. Inspect External Connections and Components
Inspect accessible cables, connectors, sensors, controls, and accessories involved in the procedure for looseness, contamination, physical damage, or incorrect installation.

**Expected outcome:** External components required for testing are properly installed and serviceable.

### 7. Check the Test Environment
Confirm that room conditions, obstructions, reflective surfaces, external light sources, or other environmental factors are not interfering with a test that depends on optical measurement or positioning. Follow the applicable manufacturer's setup requirements.

**Expected outcome:** The environment is suitable for the documented procedure.

### 8. Verify Approved Test Equipment
If the procedure requires measurement equipment, confirm that the correct approved test equipment is being used and that its own calibration status is current.

**Expected outcome:** Measurement uncertainty from incorrect or unverified test equipment is ruled out.

### 9. Repeat the Approved Procedure
Repeat the test exactly as defined in current manufacturer documentation. Do not alter hidden parameters or bypass failed portions simply to obtain a passing result.

**Expected outcome:** The procedure completes successfully and required results meet applicable manufacturer criteria. If so, troubleshooting can stop after final functional verification.

### 10. Escalate a Repeatable Test Failure
If setup, power, external connections, environment, and test equipment are correct but the procedure still fails, stop. Do not attempt internal adjustments without the appropriate service documentation, training, and authorization.

**Expected outcome:** A repeatable failure is appropriately escalated rather than bypassed.

## If the Problem Persists
External setup, positioning, power, environmental, accessory, and test-equipment causes have been ruled out. Remaining possibilities may involve configuration, internal sensing, control electronics, software, or another service-level condition.

Remove the device from service if the failed test affects safe or required operation, label it **Out of Service**, and arrange qualified evaluation using current Getinge service documentation and approved test equipment. Calibration, configuration, or repair should be performed only by qualified personnel.

Return to service only after the applicable test passes and normal lighting functions are verified. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
Never treat an incomplete required verification or calibration as acceptable simply because the light appears to illuminate normally.

## Work Order Documentation (CCR Method)
<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)
<!-- Helpful details come from front matter. -->

## Final Thought
Use only applicable approved procedures, establish correct setup before suspecting an internal fault, never bypass a failed required test, and document the final verified condition clearly.

That is successful troubleshooting.
