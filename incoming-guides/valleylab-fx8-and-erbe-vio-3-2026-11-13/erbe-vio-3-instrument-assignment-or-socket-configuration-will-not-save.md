---
schemaVersion: 1
title: "ERBE VIO 3 Electrosurgical Unit (ESU) - Instrument Assignment or Socket Configuration Will Not Save"
issueTitle: "Instrument Assignment or Socket Configuration Will Not Save"
description: "Troubleshoots assignments or socket settings that revert, fail to store, or load unexpectedly because of program selection, permissions, workflow, or configuration faults."
assetType: "Electrosurgical Unit (ESU)"
manufacturer: "ERBE"
model: "VIO 3"
slug: "erbe-vio-3-instrument-assignment-or-socket-configuration-will-not-save"
dateAdded: "2026-11-13"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that the VIO 3 repeatedly loaded the wrong footswitch-to-socket assignment when their procedure program was selected."
  cause: "Clinical Engineering found that staff had been editing a different subprogram than the one routinely loaded for the procedure."
  resolution: "Corrected the approved assignment in the intended program and verified that it remained stored after restart and activated the proper socket during testing."
helpfulDetails:
  - "Program and subprogram"
  - "Setting or assignment affected"
  - "Intended socket"
  - "Connected instrument"
  - "Footswitch assignment"
  - "Whether the value survives restart"
  - "Other programs tested"
  - "Actual versus displayed activation"
  - "Changes made"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots assignments or socket settings that revert, fail to store, or load unexpectedly because of program selection, permissions, workflow, or configuration faults.

## Step-by-Step Troubleshooting

### 1. Prevent Use With an Unverified Configuration
If the generator does not retain the intended instrument or socket assignment, do not use it clinically until the active configuration has been confirmed. An unexpected assignment can result in the wrong output being activated.

**Expected outcome:** Patient use is prevented until configuration behavior is predictable.

### 2. Define What Will Not Save
Identify the exact program, subprogram, socket, instrument, activation assignment, or setting that reverts. Record the value before saving, the action used to save it, and what appears after changing programs or restarting.

**Expected outcome:** The failure is reproducible and limited to a defined configuration item.

### 3. Verify the Correct Program Is Being Edited
Confirm that staff are modifying the intended program or subprogram rather than a temporary setup or another saved configuration.

**Expected outcome:** The correct configuration context is being used. If the apparent loss was caused by reopening a different program, no device repair is required.

### 4. Verify the Connected Instrument and Socket
Confirm the compatible instrument is connected to the intended socket and is recognized normally. The VIO 3 associates instrument detection and socket functionality with the connected interface. [register.erbe-med.com](https://register.erbe-med.com/productfinder/Marketingmaterialien/80116-939_ERBE_US_VIO_3__D165797.pdf?utm_source=chatgpt.com)

**Expected outcome:** Recognition is stable and configuration is not being altered because the expected instrument is absent or connected elsewhere.

### 5. Check for Conflicting Activation Assignments
Review normal user-accessible footswitch or instrument activation assignments. Make sure the intended socket is not being confused with another active socket or program.

**Expected outcome:** The displayed assignment corresponds to the intended instrument and activation method.

### 6. Repeat the Save Workflow Deliberately
Using the authorized workflow, make one controlled change, save it as intended, leave the configuration screen, and then reopen it.

Do not modify multiple settings simultaneously.

**Expected outcome:** The single change remains stored. If so, repeat as needed to confirm that the reported issue was workflow-related rather than a device fault.

### 7. Perform a Normal Restart
With the generator removed from patient use, shut it down normally, restart it, and reload the same approved configuration.

**Expected outcome:** The saved assignment remains unchanged after restart. If it reverts, document exactly which field or program is affected.

### 8. Compare With Another Approved Program
Without altering protected configuration, determine whether other existing programs retain their settings normally.

**Expected outcome:** The issue is isolated to one program/configuration or shown to affect stored settings broadly.

### 9. Verify Functional Behavior, Not Just the Display
Using appropriate test equipment, confirm that the socket and activation controls actually correspond to the displayed assignment after the configuration is reloaded.

**Expected outcome:** Displayed and actual activation assignments agree. Troubleshooting can stop if the approved configuration is retained and verified.

### 10. Escalate Persistent Configuration Loss
If configuration repeatedly reverts, cannot be stored, changes without user action, or displayed assignments do not match actual activation, remove the VIO 3 from service.

**Expected outcome:** A generator with unreliable stored configuration is not returned to clinical use.

## If the Problem Persists

User workflow, program selection, connected accessories, and normal assignment checks have been ruled out. Remaining possibilities include protected configuration, software, storage, configuration database integrity, internal communications, or another service-level condition.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using current ERBE documentation and approved tools
- Reconfigured, updated, or repaired only by qualified personnel

Do not enter unauthorized service menus or overwrite configuration merely to eliminate the symptom. After service, verify retained settings through shutdown/restart and confirm actual socket activation before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

After any configuration correction, verify the actual activated socket with test equipment rather than relying only on what is shown on screen.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Configuration complaints should be reproduced methodically before assuming software or memory failure. Confirm the exact program and assignment, verify what the generator actually activates, and escalate unexplained configuration changes.

That is successful troubleshooting.
