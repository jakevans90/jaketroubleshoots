---
schemaVersion: 1
title: "Stryker CrossFlow Fluid Management System - Unexpected Shutdown, Freeze, or Restart"
issueTitle: "Unexpected Shutdown, Freeze, or Restart"
description: "Troubleshoots intermittent CrossFlow shutdowns, freezes, resets, or restarts caused by power, connections, accessories, environment, or service-level faults."
assetType: "Fluid Management System"
manufacturer: "Stryker"
model: "CrossFlow"
slug: "stryker-crossflow-unexpected-shutdown-freeze-or-restart"
dateAdded: "2026-09-21"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported the CrossFlow unexpectedly shut off when the console was repositioned during room setup."
  cause: "Clinical Engineering found the external power cord was damaged near the strain relief and lost continuity when moved."
  resolution: "The damaged cord was replaced with an approved serviceable cord, and repeated movement and functional testing showed stable operation with no further shutdown."
helpfulDetails:
  - "Exact failure behavior"
  - "Activity occurring before failure"
  - "Displayed message or alarm"
  - "AC outlet result"
  - "Power cord condition"
  - "Whether movement affects operation"
  - "Accessories connected"
  - "Ventilation and environmental condition"
  - "Results of extended functional testing"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots intermittent CrossFlow shutdowns, freezes, resets, or restarts caused by power, connections, accessories, environment, or service-level faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Immediately

An unexpected shutdown, freeze, or restart makes the system unreliable until evaluated. If this occurs during a procedure, transition to a verified alternate fluid-management method or system.

Do not wait for a second failure while the patient remains dependent on the console.

**Expected outcome:** Patient care continues without reliance on the affected CrossFlow.

### 2. Capture the Exact Failure Behavior

Ask staff to describe precisely what happened:

- Complete power loss
- Display froze but output changed or stopped
- Automatic restart
- Manual restart required
- Alarm before shutdown
- Failure during a particular function
- Failure after equipment movement

Record displayed messages and the approximate sequence of events.

**Expected outcome:** The event is categorized rather than treated generically.

### 3. Inspect for Safety Hazards

Check for:

- Liquid intrusion
- Excessive heat
- Burning odor
- Damaged power components
- Unusual sound
- Visible impact damage
- Blocked ventilation

If any hazardous condition is present, do not energize the unit again.

**Expected outcome:** The system is safe for controlled testing or is immediately removed from service.

### 4. Verify the AC Power Path

Inspect the power cord, inlet, wall outlet, and any approved external power distribution equipment. Test the outlet and substitute a known-good power cord when appropriate.

Look specifically for loose connections that could momentarily interrupt power.

**Expected outcome:** The CrossFlow has stable AC input. If an unstable external connection is found and corrected, continue with repeated functional verification.

### 5. Evaluate Movement-Related Intermittency

Determine whether the failure occurred while the console, cart, cord, or external accessories were moved. Inspect external cables and connectors for intermittent seating or mechanical stress.

**Expected outcome:** Normal equipment movement does not interrupt power or operation. If a damaged connection is identified, correct it before further testing.

### 6. Disconnect Nonessential External Components

Power down the system and remove nonessential external accessories or interfaces. Restart in the simplest appropriate configuration.

**Expected outcome:** Stable operation without optional external components may identify an accessory or interface contributing to the failure.

### 7. Check Ventilation and Environment

Confirm vents are unobstructed and the unit is not positioned against material that restricts cooling. Evaluate whether the failure occurred after extended operation or in an unusually warm or contaminated environment.

**Expected outcome:** The system operates under suitable environmental conditions without signs of overheating.

### 8. Perform a Controlled Operational Test

Run the CrossFlow through an appropriate nonpatient functional setup while observing power, display, controls, alarms, and fluid-management behavior.

Do not intentionally induce unsafe operating conditions.

**Expected outcome:** The system remains stable throughout testing. Any repeat freeze, restart, or unexplained shutdown confirms the device is unreliable.

### 9. Repeat Verification After Any External Correction

If a loose cord, accessory, or environmental issue was corrected, repeat startup and functional testing sufficiently to confirm the failure does not recur.

**Expected outcome:** Operation remains stable and repeatable. Troubleshooting can stop only after reliability has been demonstrated.

### 10. Escalate an Unexplained Intermittent Failure

If the system freezes, shuts down, or restarts again despite verified external power and setup, stop troubleshooting.

**Expected outcome:** The CrossFlow is removed from service for qualified evaluation even if it subsequently appears to work normally.

## If the Problem Persists

External power, connections, accessories, and environmental conditions have been ruled out. Remaining categories may include internal power regulation, software, thermal management, internal communication, controls, or other electronics.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Stryker documentation and approved test equipment
- Repaired or configured only by qualified personnel

Intermittent failures require appropriate testing before return to service; a single successful restart is not sufficient proof of reliability. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Capture the sequence immediately after an intermittent event; what the display, alarms, accessories, and power indicators were doing just before failure can be critical.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Intermittent shutdowns deserve the same attention as complete failures. Verify power, external connections, accessories, and environment first, but remove the system from service whenever reliable operation cannot be demonstrated.

That is successful troubleshooting.
