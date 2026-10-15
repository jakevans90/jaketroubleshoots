---
schemaVersion: 1
title: "GE Healthcare CardioLab Electrophysiology Recording System - Exposure or Scan Will Not Start or Is Aborted"
issueTitle: "Exposure or Scan Will Not Start or Is Aborted"
description: "An associated EP-lab imaging exposure or scan cannot start or aborts because of readiness, interlock, communication, workflow, or external-system conditions."
assetType: "Electrophysiology Recording System"
manufacturer: "GE Healthcare"
model: "CardioLab"
slug: "ge-healthcare-cardiolab-exposure-or-scan-will-not-start-or-is-aborted"
dateAdded: "2026-10-15"
taxonomyMode: "reuse"
ccr:
  complaint: "EP staff reported that the imaging workflow repeatedly aborted while CardioLab was being used during room setup."
  cause: "Clinical Engineering found a loose external interface connection between the procedure systems."
  resolution: "The interface connection was secured, communication was verified, the procedural workflow completed normally during testing, and the systems were returned to service."
helpfulDetails:
  - "Whether the procedure never started or aborted"
  - "Exact displayed messages"
  - "Responsible imaging modality"
  - "Emergency-stop or interlock status"
  - "Footswitch or control condition"
  - "Interface cable condition"
  - "Network status"
  - "Patient or study workflow state"
  - "Whether recent room work occurred"
  - "Controlled test result"
  - "Final device status"
---

## What This Guide Helps With

An associated EP-lab imaging exposure or scan cannot start or aborts because of readiness, interlock, communication, workflow, or external-system conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Identify the Responsible System

Do not repeatedly attempt imaging or procedural actions while the cause of an abort is unknown. Notify the clinical team and maintain required patient monitoring.

CardioLab is an electrophysiology recording system; determine whether the reported exposure or scan function belongs to an integrated fluoroscopy, angiography, CT, or other imaging system.

**Expected outcome:** Patient safety is maintained and the system responsible for generating the exposure or scan is correctly identified.

If the problem belongs entirely to another modality, route troubleshooting to that equipment while verifying CardioLab remains operational.

### 2. Confirm the Exact Failure

Determine whether the exposure never begins, starts and immediately aborts, stops after a predictable interval, or only fails during a particular workflow.

Record any visible message from CardioLab and the associated imaging system.

**Expected outcome:** The failure pattern and affected equipment are clearly defined.

If the issue cannot be reproduced and all systems function normally, continue with controlled verification before closing the work order.

### 3. Check System Ready States

Verify CardioLab and the associated imaging system have completed startup and show their expected operational or ready states.

Check whether a required patient or procedure record must be active for the workflow being attempted.

**Expected outcome:** All systems required for the procedure are powered, initialized, and ready.

If restoring normal system readiness resolves the problem, perform functional verification and stop troubleshooting.

### 4. Check External Interlocks and Controls

Inspect accessible emergency stops, exposure switches, footswitches, hand controls, door or room conditions, and other external controls relevant to the associated imaging equipment.

Do not bypass radiation, motion, or equipment-safety interlocks.

**Expected outcome:** Required external controls are connected and no unresolved interlock prevents the procedure.

If correcting an approved external control condition restores operation, verify safely and stop troubleshooting.

### 5. Inspect External Interface and Communication Connections

Check external network and synchronization connections between CardioLab and associated procedural equipment where applicable.

Inspect for disconnected or damaged cables following room cleaning, equipment movement, service activity, or workstation relocation.

**Expected outcome:** Integrated systems maintain required external communication.

If restoring a loose interface connection resolves the aborted workflow, verify repeatability and stop troubleshooting.

### 6. Verify Procedure and Patient Context

Confirm the correct patient, study, procedure, and available workflow state are selected as applicable. Avoid making configuration changes solely to bypass an error.

If the associated imaging system requires its own study or examination setup, verify that setup through the responsible clinical or technical workflow.

**Expected outcome:** The intended procedure is correctly established across required systems.

If correcting an external workflow mismatch resolves the issue, verify operation and stop troubleshooting.

### 7. Check for Environmental or Infrastructure Conditions

Determine whether the problem coincides with network outages, room power disturbances, equipment overheating, recent software changes, or loss of communication with integrated systems.

**Expected outcome:** No external infrastructure condition is preventing or interrupting the procedure.

If infrastructure restoration resolves the issue, verify stable operation before return to service.

### 8. Perform Controlled Functional Verification

With the patient removed from dependence on the affected workflow, use an approved test procedure to verify that CardioLab and the responsible imaging system maintain communication and complete the expected procedural sequence.

Do not create unnecessary radiation exposure solely for troubleshooting.

**Expected outcome:** The associated procedure can be initiated and completed without an unexplained abort.

If verification passes, troubleshooting is complete.

### 9. Escalate Repeated or Unexplained Aborts

If the exposure or scan continues to fail after external interlocks, workflow, communication, and infrastructure causes have been checked, remove the affected system from clinical use as appropriate and escalate to the responsible service team.

Do not bypass safety systems or attempt internal generator, detector, acquisition, or CardioLab electronics repair.

**Expected outcome:** The unresolved procedural failure is safely isolated and escalated.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve the associated imaging modality, internal acquisition hardware, radiation-system interlocks, software, managed integration, timing interfaces, or another service-level condition.

The affected equipment should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation as appropriate.
- Evaluated using applicable manufacturer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Return the system to service only after applicable functional, safety, communication, and imaging verification. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not confuse CardioLab recording problems with failures originating in the integrated imaging system; isolate which system actually owns the failed function.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Identify the system that actually controls the failed exposure or scan before troubleshooting. Rule out readiness, interlocks, workflow, external communication, and infrastructure first, then escalate repeated unexplained aborts without bypassing safety functions.

That is successful troubleshooting.
