---
schemaVersion: 1
title: "Canon Vantage Orian MRI System - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "Addresses studies that cannot be saved, reconstructed, or exported because of workflow, storage, software, communication, destination, or data-related conditions."
assetType: "MRI System"
manufacturer: "Canon"
model: "Vantage Orian"
slug: "canon-vantage-orian-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-09-25"
taxonomyMode: "reuse"
ccr:
  complaint: "MRI staff reported completed studies were reconstructing normally but would not export to PACS."
  cause: "Clinical Engineering found the workstation had lost its external network connection while local study storage remained functional."
  resolution: "Restored the network connection, resent the affected study, confirmed receipt in PACS, and verified normal subsequent export operation."
helpfulDetails:
  - "Save, reconstruct, or export function affected"
  - "One study versus all studies"
  - "Exact displayed message"
  - "Whether source data remained available"
  - "Local storage status"
  - "Transfer queue status"
  - "Workstation responsiveness"
  - "Network status"
  - "Destination availability"
  - "Final local and PACS study status"
---
## What This Guide Helps With
Addresses studies that cannot be saved, reconstructed, or exported because of workflow, storage, software, communication, destination, or data-related conditions.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data Before Taking Action
Do not restart or power-cycle the workstation until the status of unsaved or unreconstructed patient data has been considered. Preserve available study information whenever possible.

If clinical workflow cannot continue reliably, move future imaging to another verified system.

**Expected outcome:** Existing patient data is protected as much as possible and no new studies are placed at unnecessary risk.

### 2. Identify the Exact Failed Function
Determine whether the study failed to save locally, failed during reconstruction, cannot be opened, or cannot be exported to the intended destination.

Determine whether the problem affects all studies or only one examination.

**Expected outcome:** The problem is narrowed to local storage, reconstruction, or export.

### 3. Verify Workstation Responsiveness
Confirm the workstation is responsive and not frozen or displaying broader system errors.

**Expected outcome:** The issue is distinguished from a general workstation failure.

### 4. Confirm the Study Is Present
Using normal operator-visible functions, determine whether the acquired images or raw study information expected from the workflow are still visible locally.

Do not delete studies or temporary data as a troubleshooting shortcut.

**Expected outcome:** The availability of the affected study data is known.

### 5. Check for Obvious Storage or Queue Conditions
Review normal operator-visible storage or transfer status indicators for a full queue, pending job, or storage warning.

Do not manually delete patient studies unless authorized under the facility's data-retention and recovery procedures.

**Expected outcome:** Any visible storage or queue condition is identified without risking patient data.

### 6. Determine Whether the Failure Is Study-Specific
Check whether another previously completed or approved test study can be accessed or processed normally without creating unnecessary patient data.

**Expected outcome:** The problem is identified as isolated to one study or affecting the system generally.

### 7. Check Export Destination Availability
If local saving and reconstruction work but export fails, verify the intended PACS or other approved destination is available and that network connectivity appears normal.

**Expected outcome:** Export failure is separated from local reconstruction or storage failure.

### 8. Retry Only Through the Normal Approved Workflow
After correcting any obvious external condition, retry the save, reconstruction, or export action using the standard workflow.

Avoid repeated retries if the system continues returning the same failure.

**Expected outcome:** The process completes successfully without duplicating or corrupting workflow data.

### 9. Verify the Final Data Path
Confirm the study can be opened locally when applicable, reconstructed images are complete, and exported data is received at the intended destination.

**Expected outcome:** Study integrity and the complete clinical data path are verified.

If achieved, troubleshooting can stop.

### 10. Escalate Persistent Data or Reconstruction Failures
If studies repeatedly fail to save or reconstruct, data disappears, the workstation reports storage problems, or multiple studies are affected, stop clinical use and escalate.

Do not manipulate databases, operating-system files, reconstruction services, or internal storage outside approved service procedures.

**Expected outcome:** Patient data and system integrity are protected while qualified support investigates the failure.

## If the Problem Persists

Common workflow, queue, destination, workstation, and external network causes have been ruled out. The remaining problem may involve local storage, reconstruction software, database services, workstation resources, system configuration, network services, or other service-level functions.

The MRI system should be:

- Removed from service when reliable study preservation cannot be assured
- Labeled Out of Service
- Sent for qualified evaluation
- Evaluated using appropriate Canon documentation and approved diagnostic methods
- Repaired or configured only by qualified personnel

After repair, verify acquisition, saving, reconstruction, local retrieval, and export as applicable before return to clinical use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Before restarting a system with a study-processing failure, determine whether patient data is still pending so troubleshooting does not turn a recoverable workflow problem into data loss.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Study-processing failures require both technical troubleshooting and careful protection of patient data. Determine where the workflow breaks, preserve existing information, rule out simple workstation and network causes, escalate persistent storage or reconstruction failures, and document the verified final data path.

That is successful troubleshooting.
