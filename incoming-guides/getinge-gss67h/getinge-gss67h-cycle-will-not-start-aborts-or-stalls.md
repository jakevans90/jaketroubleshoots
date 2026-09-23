---
schemaVersion: 1
title: "Getinge GSS67H Sterilizer - Cycle Will Not Start, Aborts, or Stalls"
issueTitle: "Cycle Will Not Start, Aborts, or Stalls"
description: "Use this guide when a selected sterilization cycle will not begin, terminates unexpectedly, or stops progressing through its normal phases."
assetType: "Sterilizer"
manufacturer: "Getinge"
model: "GSS67H"
slug: "getinge-gss67h-cycle-will-not-start-aborts-or-stalls"
dateAdded: "2026-09-23"
taxonomyMode: "reuse"
ccr:
  complaint: "Sterile Processing reported the Getinge GSS67H repeatedly aborted shortly after cycle initiation."
  cause: "Clinical Engineering found the door was not fully closing because a loading rack was interfering with the door path."
  resolution: "Clinical Engineering repositioned the rack, verified normal door closure, completed an approved test cycle, and returned the sterilizer to service."
helpfulDetails:
  - "Selected cycle"
  - "Exact displayed message"
  - "Phase where the cycle stopped"
  - "Whether all cycles are affected"
  - "Door condition"
  - "Load configuration"
  - "Utility status"
  - "Cycle record findings"
  - "Results of test cycle"
  - "Final device status"
---
## What This Guide Helps With

Use this guide when a selected sterilization cycle will not begin, terminates unexpectedly, or stops progressing through its normal phases.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Load Integrity
Do not consider an interrupted or incomplete load sterile. Quarantine the affected load according to Sterile Processing policy and provide another validated sterilization pathway.

Do not repeatedly restart a failed cycle without determining why it stopped.

**Expected outcome:** Potentially nonsterile instruments are controlled and the sterilizer can be evaluated without disrupting patient care.

### 2. Confirm the Exact Cycle Failure
Identify the selected cycle, point at which the cycle stopped, displayed message, whether the issue affects every cycle, and whether the condition is reproducible.

Review the available cycle record without clearing useful information.

**Expected outcome:** The failure is narrowed to a specific startup, conditioning, exposure, exhaust, drying, or other observable point.

### 3. Verify Door Closure and Interlocks
Inspect the door area for load obstruction, packaging, rack interference, debris, or visible gasket problems. Confirm the door reaches its normal closed position.

Never bypass a door switch, lock, or interlock.

**Expected outcome:** The sterilizer recognizes a properly closed door. If correcting an external obstruction allows the cycle to start and complete normally, troubleshooting can stop after verification.

### 4. Verify Required Utilities
Confirm that applicable electrical power, steam, water, compressed air, drainage, and other facility services are available and stable.

Coordinate with Facilities if other equipment in the area shows similar utility symptoms.

**Expected outcome:** Required utilities remain available throughout the cycle. If an external utility interruption caused the abort and correction restores normal cycling, verify with an appropriate test cycle and stop troubleshooting.

### 5. Inspect the Load and Chamber
Verify the load is positioned correctly and is not preventing door operation, drainage, air removal, or normal chamber function. Look for obvious loose materials or debris.

Do not modify validated loading practices as a workaround.

**Expected outcome:** The chamber and load are free of obvious external conditions that could interfere with cycle progression.

### 6. Verify Cycle Selection and Controls
Confirm the intended cycle was selected and that no unusual operator-entered setting, delayed-start feature, or control condition is preventing initiation.

Do not change validated sterilization parameters to force a cycle to run.

**Expected outcome:** A normal approved cycle is selected with controls responding properly. If correcting a selection or control condition resolves the problem, complete verification and stop troubleshooting.

### 7. Observe a Controlled Test Cycle
When safe and permitted, run an unloaded or otherwise appropriate test cycle in accordance with facility practice and manufacturer documentation.

Observe the phase where the original failure occurred.

**Expected outcome:** The test cycle progresses normally through all required phases. If it completes successfully and required verification is acceptable, troubleshooting can stop.

### 8. Compare Cycle Records
Compare the failed and successful cycle records for obvious differences in phase progression, utility-related interruptions, or repeated messages.

Do not interpret incomplete cycle data as proof of a specific internal component failure.

**Expected outcome:** External or repeatable patterns are identified without unnecessary internal troubleshooting.

### 9. Escalate Repeated Cycle Failures
If the unit continues to abort or stall after door, load, controls, utilities, and basic operating conditions are verified, remove it from service.

**Expected outcome:** An unreliable sterilizer is prevented from processing clinical loads until qualified service evaluation is completed.

## If the Problem Persists

Common external causes have been ruled out. Remaining causes may involve internal control functions, valves, sensors, utility regulation, vacuum or steam systems, door interlocks, or service-level configuration.

The sterilizer should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or qualified service evaluation.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.
- Required to complete applicable functional and process verification before return to service.

Stopping after external causes are exhausted is appropriate Clinical Engineering troubleshooting.

## Clinical Use Tip

Treat every aborted or stalled sterilization cycle as an incomplete process until the load is handled according to Sterile Processing policy.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect the load first, reproduce the failure, and verify the door, loading, controls, and utilities before assuming an internal sterilizer fault. Confirm a complete acceptable cycle before return to service and document the event clearly.

That is successful troubleshooting.
