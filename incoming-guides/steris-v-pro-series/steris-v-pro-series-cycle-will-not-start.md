---
schemaVersion: 1
title: "STERIS V-PRO Series Sterilizer - CYCLE WILL NOT START"
issueTitle: "CYCLE WILL NOT START"
description: "Troubleshooting a cycle that will not initiate due to door, load, sterilant, control, power, selection, or external readiness conditions."
assetType: "Sterilizer"
manufacturer: "STERIS"
model: "V-PRO Series"
slug: "steris-v-pro-series-cycle-will-not-start"
dateAdded: "2026-07-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Sterile Processing reported that the V-PRO sterilizer remained in ready status but would not begin the selected cycle."
  cause: "Clinical Engineering found that the chamber door was not fully closing because a tray corner was contacting the door opening."
  resolution: "The tray was repositioned, door recognition was verified, and the sterilizer successfully completed an approved verification cycle with a complete cycle record."
helpfulDetails:
  - "Exact displayed message or status"
  - "Selected cycle type"
  - "Whether Start was unavailable or ineffective"
  - "Door recognition status"
  - "Load type and arrangement"
  - "Sterilant status"
  - "Required ID or tracking entries"
  - "Recent abort or power interruption"
  - "Active alarms or maintenance prompts"
  - "Verification cycle result"
  - "Final service status"
---

## What This Guide Helps With

Troubleshooting a cycle that will not initiate due to door, load, sterilant, control, power, selection, or external readiness conditions.

## Step-by-Step Troubleshooting

### 1. Ensure Patient Safety and Continuity of Sterile Processing

Do not release instruments from an incomplete or unverified sterilization cycle.

Notify Sterile Processing leadership that the sterilizer is unavailable.

Redirect urgent loads to another verified sterilizer compatible with the devices being processed.

Keep the affected load segregated and identified as not processed.

Do not repeatedly attempt cycles if the sterilizer displays abnormal alarms, odors, leakage, overheating, or visible damage.

**Expected outcome:** Instrument processing continues through an approved alternate method, and no unsterilized load is mistaken for a completed load.

### 2. Confirm the Exact Reported Condition

Determine what happens when the operator attempts to start the cycle.

Record all displayed messages or status indicators.

Determine whether the Start control is unavailable, selectable but ineffective, or followed by an immediate abort.

Confirm whether the problem affects every cycle selection or only one cycle type.

Ask whether the condition began after a load change, sterilant replacement, power interruption, cleaning, software restart, or door problem.

**Expected outcome:** The failure is clearly defined and reproducible without assuming an internal fault.

### 3. Verify the Sterilizer Is Powered and Ready

Inspect the external power condition.

Confirm the sterilizer display and normal status indicators are active.

Verify the facility disconnect, approved receptacle, or branch circuit has not been switched off or tripped.

Inspect the accessible power cord, plug, and strain relief when the installation uses a cord connection.

Confirm the sterilizer has completed startup and is not still initializing, recovering, or displaying a service-required condition.

Do not reset breakers repeatedly.

**Expected outcome:** The sterilizer has stable power and reaches its normal ready state. If restoring an external power source returns the unit to ready and a test cycle begins normally, troubleshooting can stop after verification.

### 4. Verify Door Closure and Interlock Readiness

Inspect the chamber door and surrounding area.

Confirm the door is fully closed and no tray, pouch, instrument, packaging, or debris obstructs the opening.

Inspect the door seal area for visible contamination, folds, damage, or foreign material without removing protected components.

Confirm the display recognizes the door as closed.

Do not force the door, latch, or locking mechanism.

**Expected outcome:** The door closes normally and the control indicates a valid closed or ready condition. If proper closure restores cycle initiation, troubleshooting can stop after a successful verification cycle.

### 5. Check the Load and Loading Arrangement

Verify that the load is appropriate and positioned correctly.

Confirm only compatible, clean, dry devices and approved packaging are present.

Make sure trays and containers are fully inside the chamber and do not contact the door.

Confirm the chamber is not overloaded and items are arranged to permit circulation.

Remove visibly wet items, pooled moisture, or improperly prepared devices from the load.

Compare the arrangement with a recently successful load when available.

**Expected outcome:** The load is dry, compatible, unobstructed, and correctly positioned. If correcting the load allows the cycle to start and complete, troubleshooting can stop.

### 6. Verify Cycle Selection and Required Entries

Review operator-accessible selections without changing protected configuration.

Confirm an appropriate cycle has been selected for the load.

Verify required load identification, user identification, or tracking entries have been completed.

Confirm no prompt remains unanswered on the touchscreen.

Check whether the Start control becomes available after all required fields are completed.

Do not enter restricted service menus or change validated cycle parameters.

**Expected outcome:** All required selections and entries are accepted, and the sterilizer permits cycle initiation. If the cycle starts normally, troubleshooting can stop after completion is verified.

### 7. Inspect Sterilant Availability and Recognition

Check the externally accessible sterilant status.

Review the displayed sterilant level, cassette status, expiration warning, or replacement prompt.

Confirm the installed sterilant container or cassette is approved for the sterilizer and is correctly seated.

Inspect accessible packaging and the loading area for damage or leakage.

Do not handle leaking sterilant without following facility hazardous-material procedures.

Do not bypass sterilant recognition or reuse a rejected container.

**Expected outcome:** The sterilizer recognizes an acceptable sterilant supply and shows no unresolved sterilant prompt. If correcting the supply restores operation, troubleshooting can stop after a successful cycle.

### 8. Check for Active Alarms, Incomplete Recovery, or Maintenance Holds

Review the current status and recent cycle information.

Confirm no active alarm requires acknowledgment or correction.

Determine whether the sterilizer is completing aeration, chamber conditioning, pressure equalization, or post-abort recovery.

Check for a maintenance, service, or consumable condition that intentionally prevents operation.

Allow normal recovery processes to finish rather than interrupting power.

**Expected outcome:** The sterilizer reaches a stable ready condition without active holds. If the unit becomes ready and starts normally, troubleshooting can stop.

### 9. Perform a Controlled Restart When Safe

Use a restart only when no load is in process and facility procedures permit it.

Remove or secure any unprocessed load.

Use the normal shutdown method when the interface remains responsive.

Allow the sterilizer to shut down completely before restoring power.

Observe the full startup sequence and record any messages.

Do not repeatedly power-cycle a unit that freezes, restarts, or reports faults.

**Expected outcome:** The sterilizer completes startup, recognizes the door and sterilant supply, and returns to ready. If it then completes an approved test cycle normally, troubleshooting can stop.

### 10. Perform Final Functional Verification

Before returning the sterilizer to service:

Run the appropriate approved verification or test cycle according to facility and manufacturer procedures.

Confirm the cycle starts, progresses through all phases, completes without alarms, and produces the required electronic or printed record.

Verify the door remains secured during operation and unlocks only when appropriate.

Confirm the load record identifies the correct cycle result.

Do not use patient-care items from a failed or interrupted test.

**Expected outcome:** The sterilizer completes the required verification with correct controls, records, alarms, and door operation. Only then may it be returned to service.

## If the Problem Persists

If the cycle still will not start, common external causes involving power, door closure, loading, required entries, sterilant recognition, and active prompts have been ruled out.

The remaining cause may involve an internal interlock, door-position circuit, control system, vacuum or pressure subsystem, sterilant-delivery subsystem, protected configuration, or facility utility problem.

The sterilizer should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or formal bench or field evaluation.
- Evaluated using appropriate STERIS documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Do not bypass interlocks, defeat alarms, alter validated cycle parameters, or continue repeated start attempts. After repair, complete all required return-to-service testing and sterilization-process verification before clinical use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Keep the affected load physically segregated until a complete, documented sterilization cycle has been verified.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the load first, verify readiness conditions logically, and rule out power, door, loading, sterilant, and entry problems before suspecting an internal failure. Escalate unresolved faults and document the complaint, confirmed cause, correction, and final verification clearly.

That is successful troubleshooting.
