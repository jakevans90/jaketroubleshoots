---
schemaVersion: 1
title: "Elekta Versa HD Radiation Therapy System - Exposure or Scan Will Not Start or Is Aborted"
issueTitle: "Exposure or Scan Will Not Start or Is Aborted"
description: "Imaging exposure or scan will not begin or terminates unexpectedly because of interlocks, readiness, positioning, workflow, control, or communication conditions."
assetType: "Radiation Therapy System"
manufacturer: "Elekta"
model: "Versa HD"
slug: "elekta-versa-hd-exposure-or-scan-will-not-start-or-is-aborted"
dateAdded: "2026-10-01"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that imaging acquisitions on the Elekta Versa HD would begin but repeatedly abort before completion."
  cause: "Clinical Engineering found that the imaging detector was not fully in its required operating position."
  resolution: "Clinical Engineering corrected the detector positioning condition, completed a nonclinical acquisition successfully, and verified normal imaging operation before return to service."
helpfulDetails:
  - "Whether acquisition never started or aborted"
  - "Exact displayed message"
  - "Detector readiness"
  - "Gantry and table position"
  - "Room safety indications"
  - "Workflow selected"
  - "External connection condition"
  - "Whether failure was repeatable"
  - "Nonclinical test results"
  - "Final system status"
---
## What This Guide Helps With

Imaging exposure or scan will not begin or terminates unexpectedly because of interlocks, readiness, positioning, workflow, control, or communication conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Repeated Attempts

Do not repeatedly attempt imaging or treatment-related exposures while the cause of an abort is unknown.

Maintain patient safety and follow departmental procedures if a patient must be removed from the treatment position.

**Expected outcome:** No unnecessary exposure or unsafe treatment delay occurs during troubleshooting.

### 2. Confirm the Exact Failure

Determine whether the exposure never begins, starts and immediately aborts, or stops partway through acquisition.

Record the exact on-screen message and the workflow step at which the failure occurs.

**Expected outcome:** The failure is reproducible and clearly associated with a specific stage of acquisition.

### 3. Verify System Readiness

Confirm that required treatment and imaging subsystems show their normal ready status before initiation.

Check whether detectors, positioning components, workstations, and acquisition hardware are fully initialized.

**Expected outcome:** All required components are ready before the exposure command is issued.

### 4. Check Safety and Room Conditions

Verify that accessible emergency controls, door-related status indications, and other external safety conditions appear normal.

Do not bypass any treatment-room or equipment safety interlock.

**Expected outcome:** No external safety condition is intentionally preventing the exposure or scan.

### 5. Verify Positioning and Equipment Deployment

Confirm that the gantry, table, detector, and other required equipment are positioned appropriately for the intended imaging workflow and that no obstruction exists.

**Expected outcome:** The physical setup permits the requested acquisition.

### 6. Verify Controls and Selected Workflow

Confirm that the correct patient, study, imaging workflow, and acquisition selection are active and that no obvious incomplete workflow step is preventing initiation.

Do not change clinical parameters merely to force an exposure to occur.

**Expected outcome:** The intended workflow is correctly selected and logically ready to proceed.

### 7. Inspect External Acquisition Connections

Check accessible connections between imaging hardware, workstations, controls, and network interfaces.

Look for loose cables, damaged connectors, or peripherals that have lost power.

**Expected outcome:** External acquisition and control connections are intact.

### 8. Repeat Using an Approved Nonclinical Test

After correcting any external issue, use an approved quality-control or service verification method rather than a patient exposure to determine whether acquisition now starts and completes normally.

**Expected outcome:** The exposure or scan initiates and completes without aborting.

### 9. Verify Complete Imaging Operation

Confirm that the image is acquired, transferred to the appropriate workstation, displayed correctly, and retained as expected.

**Expected outcome:** The complete acquisition path functions normally. Troubleshooting can stop after applicable verification requirements are met.

### 10. Escalate Persistent Exposure Failure

If exposures remain inhibited or continue to abort after external readiness, controls, positioning, workflow, and communication checks, stop troubleshooting.

**Expected outcome:** The system is removed from affected clinical use pending qualified service evaluation.

## If the Problem Persists

External causes have been ruled out. The remaining problem may involve safety interlocks, acquisition controls, imaging hardware, internal communications, timing or synchronization, system configuration, or other service-level conditions.

The Versa HD should be:

- Removed from service when treatment or imaging reliability cannot be assured.
- Labeled Out of Service.
- Sent for qualified repair or service evaluation.
- Evaluated using appropriate Elekta documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Following service, required imaging, safety, and treatment-system verification must be completed before clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Do not use repeated patient exposures as a troubleshooting method; confirm correction using approved nonclinical verification whenever possible.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Confirm safety, readiness, positioning, workflow, and external communication before assuming an internal exposure-system fault. Avoid repeated clinical attempts and escalate persistent aborts appropriately.

That is successful troubleshooting.
