---
schemaVersion: 1
title: "Siemens Healthineers Biograph Vision PET / CT System - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "Use this guide when acquired data cannot be saved, reconstructed, or exported because of workflow, storage, communication, software-state, or external destination problems."
assetType: "PET / CT System"
manufacturer: "Siemens Healthineers"
model: "Biograph Vision"
slug: "siemens-healthineers-biograph-vision-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that completed Biograph Vision studies remained on the scanner and would not export to PACS."
  cause: "Clinical Engineering found an accessible workstation network connection partially disconnected."
  resolution: "Clinical Engineering secured the connection, successfully exported the retained study, confirmed PACS receipt, verified normal subsequent transfer, and returned the system to service."
helpfulDetails:
  - "Save, reconstruction, or export stage affected"
  - "PET, CT, or combined study affected"
  - "Exact displayed message"
  - "Whether raw or reconstructed data remained locally"
  - "Processing queue status"
  - "Storage warnings"
  - "Workstation responsiveness"
  - "Network status"
  - "Destination availability"
  - "Final end-to-end verification result"
---
## What This Guide Helps With

Use this guide when acquired data cannot be saved, reconstructed, or exported because of workflow, storage, communication, software-state, or external destination problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data Before Making Changes

Do not delete studies, temporary files, raw data, or acquisition records in an attempt to create space or clear an error unless specifically directed by approved service documentation.

Preserve all available patient data and arrange an alternate workflow for urgent clinical interpretation when necessary.

**Expected outcome:** Existing patient data remains protected while the failure is investigated.

### 2. Identify Which Stage Is Failing

Determine whether the study:

- Cannot be saved locally.
- Saves but will not reconstruct.
- Reconstructs but will not export.
- Fails only for PET data.
- Fails only for CT data.
- Fails only for one destination.
- Remains queued or pending.

Record the exact displayed message and study status.

**Expected outcome:** The failure is localized to saving, reconstruction, or export.

### 3. Confirm the Study Is Present Locally

Verify through normal operator-accessible functions whether the acquired study or source data is still visible on the system.

Do not assume data is lost merely because it did not reach PACS.

**Expected outcome:** The presence or absence of local study data is clearly established.

If the study exists locally and only export is failing, focus subsequent checks on communication rather than reacquisition.

### 4. Check Workstation Responsiveness

Verify that the workstation is responsive and that the application is not frozen or stalled.

Check:

- Mouse and keyboard response.
- Normal application navigation.
- System-status indications.
- Whether other studies can be opened normally.

**Expected outcome:** The workstation is either functioning normally or identified as part of the problem.

If restoring a loose external input or workstation connection corrects the problem, verify the study workflow and stop.

### 5. Review Normal Queue and Workflow Status

Use normal operator-accessible screens to determine whether reconstruction or export jobs are:

- Pending.
- Paused.
- Waiting for another process.
- Directed to an unavailable destination.
- Failing consistently.

Do not alter protected processing, storage, or service configuration.

**Expected outcome:** The workflow state is understood without changing restricted settings.

### 6. Check External Network Connectivity for Export Problems

If saving and reconstruction are successful but export fails, inspect accessible network connections and determine whether the intended PACS or destination is available.

Check whether other modalities are also affected.

**Expected outcome:** Export failure is distinguished between local scanner behavior and external network or destination availability.

If a simple accessible network connection problem is corrected and export succeeds, confirm destination receipt and stop.

### 7. Check for Obvious Storage Warnings

Review normal operator-accessible indications for storage or resource warnings.

Do not manually delete patient studies or system files as a troubleshooting shortcut.

If storage management is required, follow approved institutional and manufacturer procedures.

**Expected outcome:** Any operator-visible storage concern is identified without risking patient data.

### 8. Perform One Controlled Restart if Appropriate

If no processing task is actively preserving data and an approved normal restart can be performed safely, complete one controlled restart.

Do not force power off while data is actively saving or processing unless specifically directed by an approved procedure.

**Expected outcome:** The workstation and processing services restart normally and queued functions resume or can be retried appropriately.

If the workflow returns to normal and retained study data processes successfully, proceed to final verification.

### 9. Verify the Complete Study Workflow

Using an approved existing or test study as appropriate, verify:

- Data saves locally.
- Required reconstruction completes.
- Images are viewable.
- Export completes.
- Receiving destination confirms receipt when applicable.

**Expected outcome:** The complete save-reconstruct-export path functions normally.

If all required functions pass, troubleshooting is complete.

### 10. Escalate Persistent Data-Processing Failure

If studies still cannot save, reconstruct, or export after workflow status, workstation operation, external networking, and approved restart conditions are verified, stop external troubleshooting.

**Expected outcome:** The system is protected from further data risk and escalated for qualified service.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve workstation storage, reconstruction services, application software, data integrity, processing hardware, internal database functions, protected configuration, or network/infrastructure services.

The device should be:

- Removed from affected clinical use.
- Labeled **Out of Service** when reliable study handling cannot be assured.
- Sent for repair or qualified system evaluation.
- Evaluated using appropriate Siemens Healthineers documentation and approved diagnostic tools.
- Repaired or configured only by qualified personnel.

Do not delete data, rebuild databases, modify system storage, or reinstall software without the appropriate approved procedure and authorization.

Before return to service, verify the complete acquisition-to-save-to-reconstruction-to-export workflow.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Before repeating a patient scan because images are “missing,” confirm whether the acquired data still exists locally and whether the problem is only reconstruction or export.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Preserve patient data first, distinguish saving, reconstruction, and export failures before troubleshooting, verify external network and workflow conditions before assuming internal failure, and require end-to-end confirmation before return to service.

That is successful troubleshooting.
