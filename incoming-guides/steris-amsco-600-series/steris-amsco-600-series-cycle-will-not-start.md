---
schemaVersion: 1
title: "STERIS AMSCO 600 Series Sterilizer - Cycle Will Not Start"
issueTitle: "Cycle Will Not Start"
description: "Use this guide when the sterilizer powers on but a selected cycle will not begin due to door, utility, control, or readiness conditions."
assetType: "Sterilizer"
manufacturer: "STERIS"
model: "AMSCO 600 Series"
slug: "steris-amsco-600-series-cycle-will-not-start"
dateAdded: "2026-08-17"
taxonomyMode: "reuse"
ccr:
  complaint: "Sterile Processing reported that the AMSCO 600 Series powered on and allowed cycle selection but would not start."
  cause: "Clinical Engineering found packaging material preventing the chamber door from fully closing and achieving the recognized closed condition."
  resolution: "Removed the obstruction, verified proper door closure, started an approved test cycle, and confirmed normal cycle initiation before returning the sterilizer to service."
helpfulDetails:
  - "Cycle selected when the failure occurred."
  - "Exact displayed message or alarm."
  - "Door closed/locked indication."
  - "Whether one or all cycles were affected."
  - "Facility utility status."
  - "Recent power or utility interruption."
  - "Visible leaks or abnormal sounds."
  - "Results before and after correction."
  - "Final functional test performed."
  - "Final device status."
---

## What This Guide Helps With
Use this guide when the sterilizer powers on but a selected cycle will not begin due to door, utility, control, or readiness conditions.

## Step-by-Step Troubleshooting

### 1. Protect Patient Safety and Sterile Processing Continuity
Do not rely on a sterilizer that cannot reliably initiate a cycle. Keep questionable loads from being released as sterile. If processing is needed, move the workload to another verified sterilizer according to facility procedure.

Identify whether an instrument load is already inside the chamber and maintain appropriate load traceability.

**Expected outcome:** Sterile processing continuity is maintained without depending on the affected sterilizer. If another verified unit is available, troubleshooting may proceed without delaying required processing.

### 2. Confirm the Exact Reported Condition
Have staff describe what occurs when attempting to start the cycle. Determine whether:
- The cycle can be selected.
- The Start control responds.
- A message, alarm, or readiness indication appears.
- The door appears closed and locked.
- The problem affects one cycle or all cycles.
- The problem began after loading, a utility interruption, cleaning, or another event.

Reproduce the condition without altering service-level settings.

**Expected outcome:** The failure is clearly identified as a no-start condition rather than an incomplete cycle, door fault, or control-display problem. If normal operation is reproduced and repeated cycle initiation is successful, troubleshooting can stop after functional verification.

### 3. Verify Main Power and Normal Startup
Confirm the sterilizer is energized and the display, indicators, and controls have completed normal startup. Check for an obvious facility power interruption or upstream electrical issue.

Do not open electrical enclosures solely to investigate a cycle-start complaint unless required later under authorized service procedures.

**Expected outcome:** The sterilizer remains powered with a stable user interface and no obvious loss of facility power. If power is unstable, correct the external supply issue before continuing.

### 4. Inspect the Door and Door Area
Verify the door is fully closed and there is no tray, rack, packaging material, debris, or other obstruction preventing complete closure.

Observe whether the sterilizer recognizes the expected closed or locked condition. Do not bypass or defeat door interlocks.

**Expected outcome:** The door closes normally and the sterilizer recognizes the required door condition. If removing an external obstruction restores proper recognition and the cycle starts normally, troubleshooting can stop after verification.

### 5. Verify Cycle Selection and Readiness
Confirm an appropriate cycle can be selected using normal operator controls. Check the displayed status for any indication that the sterilizer is not ready, is waiting for a condition, or requires acknowledgment of an existing message.

Do not change validated cycle parameters simply to force the unit to start.

**Expected outcome:** A valid cycle is selected and the sterilizer indicates that it is ready to begin. If an incorrectly selected or incomplete control sequence was the cause and normal cycle initiation is restored, troubleshooting can stop.

### 6. Check Accessible Utility Conditions
Verify that facility utilities required for normal operation are available at the sterilizer. Depending on installation, this may include steam, water, compressed air, electrical power, or drainage support.

Look for obvious closed external isolation valves, facility outages, or utility work affecting the sterilizer.

**Expected outcome:** Required utilities appear available and no external interruption is identified. If an external utility condition is corrected and the cycle starts normally, troubleshooting can stop after verification.

### 7. Inspect External Connections and Surrounding Conditions
Check accessible external utility connections and the area around the sterilizer for:
- Visible leakage.
- Damaged hoses or piping.
- Disconnected accessible cables.
- Water accumulation.
- Unusual heat, odor, or noise.
- Recent construction or utility work.

Do not disassemble internal valve, control, or steam components during this step.

**Expected outcome:** No obvious external condition is preventing operation. Any unsafe leak, electrical concern, burning odor, or significant physical damage requires removal from service.

### 8. Power-Cycle Only When Operationally Appropriate
If permitted by facility procedure and no load is being actively processed, perform a normal shutdown and restart using approved controls.

Do not remove power during an active sterilization process solely as a troubleshooting shortcut.

**Expected outcome:** The sterilizer completes startup normally and accepts a cycle-start command. If normal operation returns and remains repeatable, perform final verification and stop troubleshooting.

### 9. Perform Final Functional Verification
Using an appropriate unloaded or facility-approved test process, verify that the sterilizer accepts cycle selection, recognizes the door condition, starts normally, and transitions into the expected initial cycle phase.

Follow facility and manufacturer requirements before returning the unit to production.

**Expected outcome:** The cycle begins consistently without unexpected messages or abnormal behavior. If successful, troubleshooting is complete.

### 10. Escalate an Unresolved No-Start Condition
If power, door condition, cycle selection, accessible utilities, external connections, and normal startup have been verified but the sterilizer still will not begin a cycle, stop external troubleshooting.

Potential service-level categories include door-interlock sensing, control input, utility-control, safety-interlock, or internal control-system problems.

**Expected outcome:** An unresolved sterilizer is removed from service rather than repeatedly attempted in clinical production.

## If the Problem Persists
Common external causes have been ruled out. The sterilizer should be **removed from service**, **labeled Out of Service**, and sent for appropriate repair or bench/on-site service evaluation.

Further evaluation should use current STERIS service documentation and approved test equipment. Internal controls, interlocks, valves, sensors, or configuration should be repaired or adjusted only by qualified personnel.

After corrective work, complete required operational and sterilization-performance testing before return to service. Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip
Do not release a load as sterile from a sterilizer that failed to initiate or complete the intended validated cycle.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Begin with patient safety, confirm the actual no-start condition, verify simple external causes before assuming internal failure, escalate appropriately when unresolved, and document what was found and verified.

That is successful troubleshooting.
