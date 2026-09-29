---
schemaVersion: 1
title: "Siemens Healthineers Biograph Vision PET / CT System - Exposure or Scan Will Not Start or Is Aborted"
issueTitle: "Exposure or Scan Will Not Start or Is Aborted"
description: "Use this guide when an acquisition will not begin or unexpectedly stops because of readiness, positioning, protocol, safety, communication, or external system conditions."
assetType: "PET / CT System"
manufacturer: "Siemens Healthineers"
model: "Biograph Vision"
slug: "siemens-healthineers-biograph-vision-exposure-or-scan-will-not-start-or-is-aborted"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the selected Biograph Vision scan would not start after patient positioning was completed."
  cause: "Clinical Engineering found the table had not reached the required completed positioning state because an accessory was obstructing travel."
  resolution: "Clinical Engineering removed the obstruction, verified normal table positioning, completed an approved test acquisition without abort, and returned the system to service."
helpfulDetails:
  - "CT, PET, or combined acquisition affected"
  - "Exact message displayed"
  - "Point at which the scan stopped"
  - "Protocol or workflow involved"
  - "System readiness state"
  - "Table position"
  - "Obstructions or accessories present"
  - "Result of restart"
  - "Result of approved test acquisition"
  - "Final device status"
---
## What This Guide Helps With

Use this guide when an acquisition will not begin or unexpectedly stops because of readiness, positioning, protocol, safety, communication, or external system conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Repeated Scan Attempts

Do not repeatedly attempt exposure or PET acquisition when the cause of a failed or aborted scan is unknown.

Confirm the patient is safe, table movement is controlled, and any required alternate imaging or clinical workflow is arranged.

**Expected outcome:** The patient is protected from unnecessary repeat exposure or unreliable acquisition.

If the system demonstrates an unresolved safety or exposure-control concern, remove it from service.

### 2. Confirm Exactly When the Scan Fails

Determine whether the scan:

- Never becomes available to start.
- Accepts the start command but does nothing.
- Begins and immediately aborts.
- Stops during CT acquisition.
- Stops during PET acquisition.
- Fails only with one protocol or workflow.

Record the exact displayed message and sequence.

**Expected outcome:** The failure point and affected acquisition type are clearly identified.

### 3. Verify System and Acquisition Readiness

Confirm that the required PET and CT subsystems show normal ready status before beginning a study.

Check for:

- Pending initialization.
- Detector not-ready state.
- Gantry or table positioning fault.
- Active system warning.
- Cooling or environmental fault.

**Expected outcome:** All required systems indicate readiness for the selected examination.

If a legitimate readiness condition is corrected and scanning proceeds normally, complete verification and stop.

### 4. Check Patient Table and Positioning Conditions

Confirm that:

- The table is positioned appropriately.
- No obstruction is present.
- Positioning accessories are secure.
- Required motion has completed.
- No safety stop or positioning fault remains active.

Do not bypass positioning or safety interlocks to initiate a scan.

**Expected outcome:** Patient positioning is stable and does not inhibit acquisition.

If correcting positioning resolves the issue, verify scan operation and stop.

### 5. Verify Protocol and Study Selection

Check the normal operator-accessible examination setup for obvious issues such as:

- Incorrect study selection.
- Incomplete required examination information.
- A workflow step not completed.
- A protocol inconsistent with the intended acquisition path.
- A selected task waiting for an earlier step to finish.

Do not change service-level parameters or protected scan configuration.

**Expected outcome:** The intended study and protocol are correctly selected and ready to execute.

If correcting an obvious workflow or protocol-selection issue allows normal scanning, stop after verification.

### 6. Inspect External Controls and Connections

Inspect accessible scan controls, workstation connections, input devices, and external communication cables for obvious looseness or damage.

If an exposure or acquisition control appears physically damaged, do not continue clinical use.

**Expected outcome:** External controls required to initiate the scan are intact and responsive.

If an approved external connection correction restores normal scan initiation, verify the system and stop.

### 7. Evaluate Whether the Failure Is Protocol-Specific or System-Wide

Using an approved non-patient test workflow when appropriate, determine whether the issue occurs across normal acquisition functions or only within one specific configured workflow.

Do not create experimental patient protocols as a troubleshooting method.

**Expected outcome:** The problem is identified as either broad system failure or limited workflow/configuration behavior.

If the issue is traced to an approved configurable workflow and corrected by authorized personnel, complete verification before release.

### 8. Perform One Controlled Restart if Appropriate

If the system is otherwise safe and no patient depends on it, perform one normal controlled restart.

Do not use repeated restarts to mask an intermittent exposure or scan-abort condition.

**Expected outcome:** The system returns to ready status and a permitted test acquisition can be initiated and completed normally.

If the problem does not recur during required verification, troubleshooting may stop.

### 9. Perform Final Functional Verification

Before return to service, verify:

- Scan initiation.
- Stable acquisition.
- Appropriate table behavior.
- No unexpected abort.
- Image generation.
- Required alarms and system status.
- Any required quality or functional tests.

**Expected outcome:** A complete approved test workflow starts and finishes without interruption.

If all verification passes, troubleshooting is complete.

### 10. Escalate Persistent Scan-Start or Abort Problems

If scans continue to fail after readiness, positioning, protocol, external controls, and normal restart conditions have been verified, stop troubleshooting.

**Expected outcome:** The system is removed from clinical use and escalated for qualified service.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve exposure control, acquisition synchronization, internal communication, detector control, motion interlocks, internal system faults, protected configuration, or other service-level conditions.

The device should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or qualified system evaluation.
- Evaluated using appropriate Siemens Healthineers documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Do not bypass exposure interlocks, safety circuits, or acquisition checks.

Before clinical use resumes, complete appropriate functional and imaging verification, including any required radiation-safety or quality-control testing.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Avoid unnecessary repeat CT exposure while troubleshooting; resolve the cause of a failed acquisition before repeating patient imaging.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient from unnecessary repeat acquisition, verify readiness and positioning before suspecting internal exposure hardware, and require a complete successful test before returning the system to clinical service.

That is successful troubleshooting.
