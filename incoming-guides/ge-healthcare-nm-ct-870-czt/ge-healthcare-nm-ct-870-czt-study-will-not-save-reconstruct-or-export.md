---
schemaVersion: 1
title: "GE Healthcare NM/CT 870 CZT PET / CT System - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "A completed study cannot save, reconstruct, or export because of workflow, storage, data, software, destination, or communication conditions."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "NM/CT 870 CZT"
slug: "ge-healthcare-nm-ct-870-czt-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-09-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported completed NM/CT 870 CZT studies would reconstruct locally but would not export to PACS."
  cause: "Clinical Engineering found the workstation had lost its external network connection while local reconstruction remained functional."
  resolution: "Clinical Engineering restored the network connection, verified successful export and receipt of the study in PACS, and returned the system to normal clinical workflow."
helpfulDetails:
  - "Save, reconstruction, or export stage affected"
  - "Exact displayed message"
  - "One study or multiple studies affected"
  - "Whether acquired data remain available"
  - "Patient and study information condition"
  - "Workstation responsiveness"
  - "Storage or queue status"
  - "Network and destination availability"
  - "Successful test after correction"
  - "Confirmation of destination receipt"
---
## What This Guide Helps With

A completed study cannot save, reconstruct, or export because of workflow, storage, data, software, destination, or communication conditions.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data Before Making Changes

Do not delete studies, clear storage, repeat acquisition, or restart the system until the status of unsaved or unreconstructed patient data is understood.

If the patient is still on the system, avoid additional exposure solely to recreate data that may still be recoverable.

**Expected outcome:** Existing clinical data are protected while the failure is evaluated.

### 2. Identify the Exact Failed Stage

Determine whether the study cannot be saved locally, cannot reconstruct, cannot open after reconstruction, or cannot export to a destination.

Record the exact message and whether the failure affects one study or multiple studies.

**Expected outcome:** The problem is localized to storage, reconstruction, or export rather than treated as one generic data failure.

### 3. Confirm the Study Is Complete

Verify through normal operator-visible information that the acquisition completed and that required study data are present.

Do not assume an export failure when the acquisition itself did not finish correctly.

**Expected outcome:** The underlying acquired data needed for the next workflow stage appear available.

### 4. Review Patient and Study Information

Check for obvious missing, duplicate, invalid, or mismatched patient and study data that may interfere with saving or downstream processing.

Coordinate corrections through approved clinical workflow rather than arbitrarily editing records.

**Expected outcome:** Patient and examination data are internally consistent for normal processing.

### 5. Check Workstation Responsiveness

Confirm the workstation is responsive and that the application is not frozen or reporting broader communication problems.

If the workstation is unstable, protect the study data before attempting an approved restart.

**Expected outcome:** The workstation is functioning normally enough to process the study.

### 6. Determine Whether Other Studies Are Affected

Using appropriate existing or test data, determine whether the failure is unique to one examination or occurs with multiple studies.

A single-study problem may involve data integrity or workflow, while a system-wide problem suggests storage, reconstruction, software, or communication issues.

**Expected outcome:** The scope of the failure is established.

### 7. Check Export Destination Availability

For export failures, verify the intended PACS, archive, removable-media workflow, or other approved destination is available.

Inspect network connectivity and coordinate with IS or PACS staff for known outages.

**Expected outcome:** The destination path is available, or a downstream outage is identified.

### 8. Review Operator-Visible Storage Status

Check available normal system indicators for storage or queue conditions.

Do not manually delete clinical data, alter storage partitions, or manipulate system files unless following an authorized data-management procedure.

**Expected outcome:** No obvious operator-visible storage condition explains the failure, or an approved storage-management action is identified.

### 9. Perform a Controlled Workflow Verification

After correcting an external condition, verify the affected function with an appropriate study or test dataset.

Confirm local save, reconstruction, and export as relevant, including receipt at the destination.

**Expected outcome:** The complete affected workflow succeeds. If it does and data integrity is confirmed, troubleshooting can stop.

### 10. Escalate Persistent Data-Processing Failure

If study data, destination availability, external network connections, and workstation operation appear normal but saving or reconstruction still fails, stop external troubleshooting.

Do not alter databases, reconstruction services, file systems, operating-system settings, or protected application configuration without authorized service support.

**Expected outcome:** The study and system are preserved for qualified recovery or repair rather than risking further data loss.

## If the Problem Persists

Common external causes involving patient data, study completion, workstation state, network connectivity, destination availability, and operator-visible storage conditions have been ruled out. Remaining categories may include internal storage, database services, reconstruction software, system communications, application services, or protected configuration.

The device should be:

- Removed from service when reliable data preservation or processing cannot be assured.
- Labeled Out of Service.
- Sent for repair or controlled system evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved diagnostic tools.
- Repaired, recovered, or configured only by qualified personnel.

Verify study saving, reconstruction, export, data integrity, and applicable quality functions before return to clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Preserve existing acquired data before restarting or performing any action that could jeopardize an unreconstructed or unsent patient study.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect patient data before restarting or deleting anything, determine exactly where the workflow fails, verify external storage and communication causes first, escalate safely when processing remains unreliable, and clearly document the final data status.

That is successful troubleshooting.
