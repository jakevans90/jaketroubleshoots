---
schemaVersion: 1
title: "Stryker CrossFlow Fluid Management System - System Will Not Power On or Complete Startup"
issueTitle: "System Will Not Power On or Complete Startup"
description: "Troubleshoots a CrossFlow console that is completely unpowered, fails startup, or does not reach a normal ready state."
assetType: "Fluid Management System"
manufacturer: "Stryker"
model: "CrossFlow"
slug: "stryker-crossflow-system-will-not-power-on-or-complete-startup"
dateAdded: "2026-09-21"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported the Stryker CrossFlow console would not power on when preparing the room for a procedure."
  cause: "Clinical Engineering found the detachable power cord was not fully seated at the console power inlet."
  resolution: "The power cord was reseated, the console completed startup normally, and functional operation was verified before return to service."
helpfulDetails:
  - "Exact startup behavior"
  - "Any displayed message or alarm"
  - "AC outlet tested"
  - "Power cord condition"
  - "Power indicators observed"
  - "Accessories connected during failure"
  - "Evidence of liquid intrusion or damage"
  - "Results with nonessential accessories disconnected"
  - "Results of repeated startup testing"
  - "Final functional test result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots a CrossFlow console that is completely unpowered, fails startup, or does not reach a normal ready state.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Fluid Management

Do not troubleshoot an unreliable CrossFlow system while a patient depends on it. If the failure occurs during a procedure, notify the clinical team and transition to an approved alternate fluid-management method or verified replacement system.

Inspect for smoke, unusual odor, liquid intrusion, overheating, or visible damage before touching or energizing the console.

**Expected outcome:** Patient care is maintained independently of the affected system, and the console is safe for external evaluation. If hazardous damage is present, remove it from service immediately and stop troubleshooting.

### 2. Confirm the Exact Startup Failure

Ask staff what occurred when the problem appeared. Determine whether the console:

- Shows no signs of power
- Powers on briefly and shuts down
- Stops during its startup sequence
- Displays a startup message or alarm
- Started normally earlier in the case
- Was recently moved, cleaned, disconnected, or connected to different accessories

Attempt startup only when the system is disconnected from patient use.

**Expected outcome:** The failure is reproduced or clearly characterized. If the system starts normally and repeated startup testing is successful, proceed to final functional verification.

### 3. Verify AC Power

Inspect the power cord, plug, inlet, and strain relief for damage or looseness. Confirm the cord is fully seated at the console and wall outlet.

Test the outlet using an approved method or connect the CrossFlow to a known-good appropriate power source.

Avoid relying solely on the fact that another device was previously connected to the outlet.

**Expected outcome:** The console receives reliable AC power. If restoring the power connection corrects the problem and startup completes normally, troubleshooting can stop after functional verification.

### 4. Inspect External Power Components

If a detachable power cord is used, substitute a known-good compatible cord when appropriate. Check any approved power distribution equipment used in the room for a tripped switch, disconnected plug, or other obvious problem.

Do not bypass protective grounding or safety devices.

**Expected outcome:** External power components are verified serviceable. If replacing a damaged or defective external cord restores operation, document the correction and continue to final testing.

### 5. Disconnect Nonessential External Accessories

With the console powered down, disconnect external accessories or interfaces that are not required for a basic startup evaluation. Inspect connectors for contamination, fluid, bent contacts, damaged housings, or incomplete engagement.

Restart the console in the minimum appropriate configuration.

**Expected outcome:** The console completes startup without an external connection interfering. If startup succeeds, reconnect accessories individually to identify the external cause.

### 6. Verify Controls and Startup Conditions

Inspect the power control and accessible user controls for physical damage, sticking, or evidence of fluid contamination. Confirm required external components are properly installed when their presence is necessary for normal operation.

Do not enter unauthorized service modes or alter protected configuration settings.

**Expected outcome:** Controls operate normally and the system reaches its normal ready condition. If it does, troubleshooting may stop after final verification.

### 7. Evaluate for Environmental Causes

Confirm ventilation openings are unobstructed and the unit has not been exposed to excessive moisture, cleaning solution, unusual heat, or other adverse conditions.

If liquid intrusion is suspected, do not repeatedly energize the unit.

**Expected outcome:** No environmental condition is preventing safe startup. Suspected liquid intrusion or overheating requires removal from service.

### 8. Repeat Startup Under Controlled Conditions

After correcting any external issue, power-cycle the console using normal controls and observe the complete startup sequence. Repeat if appropriate to ensure the condition is not intermittent.

**Expected outcome:** The CrossFlow starts consistently without unexpected alarms, resets, or interruptions. A consistent successful startup indicates the immediate problem is resolved.

### 9. Perform Final Functional Verification

Connect the appropriate approved accessories or test setup and verify basic controls, display operation, alarm functionality, and fluid-management operation without patient connection.

Use manufacturer documentation and approved test equipment for any required performance testing.

**Expected outcome:** The system operates normally and passes applicable return-to-service checks. If verification passes, troubleshooting is complete.

### 10. Escalate an Unresolved Startup Failure

If verified AC power, external components, accessories, controls, and environmental conditions are satisfactory but the system still does not start correctly, stop external troubleshooting.

**Expected outcome:** The unresolved console is removed from clinical availability and routed for qualified service evaluation.

## If the Problem Persists

Common external causes have been ruled out. The remaining fault may involve an internal power subsystem, startup electronics, protected configuration, internal communication, or another service-level condition.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Stryker documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not continue repeated power cycling when the system cannot reliably complete startup. Return to service only after the identified problem has been corrected and appropriate functional and safety testing has passed.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Have a verified alternate fluid-management system available before removing an unreliable console from an active procedural setup.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient first, verify power and external conditions before assuming an internal failure, and escalate when reliable startup cannot be demonstrated. Clear CCR documentation should show exactly what was reported, found, corrected, and verified.

That is successful troubleshooting.
