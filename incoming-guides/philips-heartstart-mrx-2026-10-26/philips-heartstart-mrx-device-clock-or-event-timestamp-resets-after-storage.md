---
schemaVersion: 1
title: "Philips HeartStart MRx Defibrillator - Device Clock or Event Timestamp Resets After Storage"
issueTitle: "Device Clock or Event Timestamp Resets After Storage"
description: "Troubleshoot incorrect or resetting clock and event timestamps caused by prolonged storage, power condition, configuration, or service-level timekeeping problems."
assetType: "Defibrillator"
manufacturer: "Philips"
model: "HeartStart MRx"
slug: "philips-heartstart-mrx-device-clock-or-event-timestamp-resets-after-storage"
dateAdded: "2026-10-26"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the HeartStart MRx displayed an incorrect date and time after being removed from extended storage."
  cause: "Clinical Engineering found the device clock had reset after storage, and the incorrect time recurred under normal storage conditions after the clock was corrected."
  resolution: "Removed the MRx from service and escalated it for qualified bench evaluation because reliable clock retention and event timestamps could not be verified."
helpfulDetails:
  - "Displayed date and time when received"
  - "Reliable reference time used"
  - "Whether the clock reset or drifted"
  - "Storage duration and conditions"
  - "AC power status during storage"
  - "Battery status and recognition"
  - "Whether batteries had been removed or depleted"
  - "Results after resetting the clock"
  - "Results after power cycling"
  - "Event timestamp comparison"
  - "External review-system timestamp"
  - "Whether the problem recurred"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoot incorrect or resetting clock and event timestamps caused by prolonged storage, power condition, configuration, or service-level timekeeping problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Event Documentation

Do not remove a clinically needed defibrillator from service solely to investigate the clock while a patient depends on it.

If timestamps are known to be inaccurate, notify appropriate clinical personnel so event documentation can account for the discrepancy and exchange the unit if accurate event timing is operationally required.

**Expected outcome:** Patient care continues with awareness of any timestamp limitation.

### 2. Confirm the Exact Clock or Timestamp Complaint

Determine whether:

- The displayed clock resets
- The date changes
- Time is incorrect after prolonged storage
- Event timestamps differ from the displayed time
- The problem occurs after every power cycle or only after extended storage
- The clock gradually drifts rather than resetting

Record the observed date and time before making adjustments.

**Expected outcome:** The pattern of the timekeeping failure is clearly established.

### 3. Compare With a Reliable Time Reference

Compare the MRx date and time against the hospital's approved time reference or another reliable synchronized system.

Check both the displayed clock and, when practical, a newly generated non-patient test event.

**Expected outcome:** The amount and type of time discrepancy are documented. If the device time is correct, investigate whether the original complaint involved another system in the documentation pathway.

### 4. Verify Basic Device and Battery Condition

Confirm the MRx powers normally from its intended power sources and that installed batteries are recognized and functioning normally.

Look for broader evidence of power instability, unexpected shutdowns, or abnormal startup behavior.

Do not assume a clock problem is caused by an internal timekeeping component until general power conditions are verified.

**Expected outcome:** The unit powers and operates normally. Broader power problems are addressed before continuing clock troubleshooting.

### 5. Review the Storage Conditions

Determine whether the unit had been:

- Stored for an extended period
- Stored without its normal power arrangement
- Left with depleted or removed batteries
- Stored outside its normal clinical environment
- Recently returned from repair or long-term storage

Storage history can help distinguish a one-time loss of time information from an ongoing clock-retention problem.

**Expected outcome:** The circumstances surrounding the reset are understood and documented.

### 6. Correct the Date and Time Through Approved Controls

Set the clock using the normal authorized configuration method available to Clinical Engineering.

Do not enter restricted service functions or change unrelated configuration items.

After setting the correct time, power-cycle the unit through a normal operating sequence.

**Expected outcome:** The correct date and time remain after a normal restart. If the problem does not recur and subsequent testing is successful, continue with storage-retention verification.

### 7. Verify Event Timestamps

Generate an appropriate non-patient test event according to organizational practice and compare its timestamp with the displayed clock and reliable time reference.

Confirm that the event record reflects the expected date and time.

**Expected outcome:** The displayed time and recorded event timestamp agree appropriately. If both remain correct, the immediate issue is resolved.

### 8. Evaluate Retention After a Controlled Storage Period

If practical within the department's workflow, leave the device in its normal storage configuration and later recheck the date and time.

Avoid deliberately creating abnormal power conditions that could compromise readiness or stored clinical data.

**Expected outcome:** The device retains the correct clock through normal storage. If it does, troubleshooting can stop after final verification.

### 9. Check for Repeated Reset Behavior

If the clock resets again, document exactly what occurred immediately beforehand, including:

- AC connection status
- Battery installation and condition
- Duration of storage
- Whether batteries were removed or depleted
- Time/date displayed before storage
- Time/date displayed afterward

Repeated resets under normal storage conditions indicate the problem should be escalated.

**Expected outcome:** Reproducible evidence distinguishes an isolated event from a persistent device problem.

### 10. Verify the Complete Data Workflow

If the MRx clock remains correct but exported events display incorrect times elsewhere, compare the timestamps at each point in the workflow.

Check the MRx event, removable media, review workstation, and receiving application as applicable.

Do not change network or enterprise time configuration without appropriate authorization.

**Expected outcome:** The incorrect timestamp is localized either to the MRx or to an external review/documentation system.

### 11. Perform Final Functional Verification

Confirm:

- Correct date and time are displayed
- Time persists through normal restart
- Time remains correct after normal storage conditions
- Test event timestamps are correct
- Other device functions operate normally

Complete required return-to-service testing.

**Expected outcome:** Timekeeping and event documentation remain stable. The unit may return to service when all required checks pass.

### 12. Escalate Recurrent Time Loss

If the date or time repeatedly resets under normal storage conditions after power, batteries, authorized settings, and external workflow factors have been ruled out, stop external troubleshooting.

**Expected outcome:** The device is removed from service as required and referred for qualified service evaluation.

## If the Problem Persists

Common external power, storage, configuration, and documentation-path causes have been ruled out. Remaining possibilities may involve internal timekeeping retention, power-support circuitry, software/configuration, or another service-level condition.

The device should be:

- Removed from service if reliable event timing cannot be assured
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Philips documentation and approved test equipment
- Repaired or configured only by qualified personnel

After correction, verify clock retention and event timestamps in addition to all required defibrillator return-to-service testing. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Accurate timestamps can be important during code review and clinical documentation; record any known clock discrepancy before altering the device time.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Accurate event timing matters, but troubleshooting should remain methodical: verify power, storage conditions, authorized settings, and the complete documentation path before assuming an internal fault. Persistent time loss warrants escalation and clear CCR documentation.

That is successful troubleshooting.
