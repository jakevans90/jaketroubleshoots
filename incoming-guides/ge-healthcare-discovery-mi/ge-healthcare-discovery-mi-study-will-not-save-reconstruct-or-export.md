---
schemaVersion: 1
title: "GE Healthcare Discovery MI PET / CT System - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "Troubleshoots study saving, reconstruction, and export failures caused by workflow, storage, connectivity, destination availability, software state, or study-specific conditions."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "Discovery MI"
slug: "ge-healthcare-discovery-mi-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Imaging staff reported that a completed Discovery MI study reconstructed locally but would not export to PACS."
  cause: "Clinical Engineering found that network connectivity from the operator workstation had been interrupted by a loose external network connection."
  resolution: "Clinical Engineering restored the network connection, verified successful export and PACS receipt of the preserved study, confirmed normal subsequent data transfer, and returned the scanner to service."
helpfulDetails:
  - "Save, reconstruction, or export function affected"
  - "PET, CT, or fused data involved"
  - "Exact message"
  - "Study available locally"
  - "Other studies affected"
  - "Workstation responsiveness"
  - "Storage warning status"
  - "Network connection status"
  - "PACS or destination status"
  - "Restart result"
  - "Final save/reconstruction/export verification"
---
## What This Guide Helps With
Troubleshoots study saving, reconstruction, and export failures caused by workflow, storage, connectivity, destination availability, software state, or study-specific conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Existing Data

Do not repeat a PET or CT acquisition because a completed study will not save, reconstruct, or export until the existing data have been located and preserved.

Avoid deleting temporary, queued, or incomplete study data while troubleshooting.

**Expected outcome:** Existing patient data are preserved and unnecessary repeat imaging is avoided.

### 2. Identify Which Data Function Fails

Determine whether the study:

- Will not save locally
- Saves but will not reconstruct
- Reconstructs but will not export
- Exports to one destination but not another
- Fails only for one study
- Fails for all new studies

Record exact messages and whether the failure occurred during PET, CT, or fused-image processing.

**Expected outcome:** The problem is isolated to storage, reconstruction, export, or a specific study.

### 3. Confirm Workstation Responsiveness

Verify that the operator workstation is functioning normally and that other routine software functions respond.

Check for:

- Frozen controls
- Delayed response
- Missing study list
- Communication warnings
- Unexpected restart
- General software instability

**Expected outcome:** The workstation is responsive or the issue is recognized as a broader workstation problem.

### 4. Verify the Study Exists Locally

Using normal operator-accessible functions, determine whether the acquisition data and available reconstructed series remain on the system.

Do not remove or overwrite the study.

**Expected outcome:** The location and current state of the patient data are known.

### 5. Check for Study-Specific Workflow Problems

Review the affected examination for obvious issues such as:

- Incomplete acquisition
- Pending reconstruction step
- Incorrectly selected series
- Incomplete patient or study information
- Workflow step not completed

Do not alter patient identifiers merely to make the study process.

**Expected outcome:** The study workflow is complete and no obvious operator-level condition is preventing processing.

### 6. Compare With Another Existing Study

When appropriate, test processing using an existing noncritical study or approved test dataset rather than acquiring additional patient data.

Determine whether:

- Other studies reconstruct normally
- Other studies save normally
- Other studies export normally

**Expected outcome:** The failure is identified as study-specific or system-wide.

### 7. Verify Export Destination and Network Availability

If export is the only failed function, verify:

- Accessible network connection
- Destination availability
- PACS status
- Export queue status
- Whether another configured destination is affected

Coordinate with PACS or IT personnel when necessary.

**Expected outcome:** The export path is available or an external destination/network problem is identified.

### 8. Check Accessible Storage Status Indicators

Use normal operator-accessible system information to look for warnings indicating storage or data-management problems.

Do not manually delete system files or alter operating-system storage outside approved procedures.

**Expected outcome:** No accessible warning indicates that local storage or study management requires service-level intervention.

### 9. Perform an Approved Restart if Safe

After confirming that patient data are preserved and no active processing would be lost, perform an approved normal workstation or system restart if appropriate.

Avoid forced shutdowns unless required for safety.

**Expected outcome:** Normal study-processing services restart and the affected save, reconstruction, or export function becomes available.

### 10. Verify the Complete Data Workflow

Confirm as appropriate that:

- Test or preserved study data can be accessed
- Reconstruction completes
- Images display correctly
- Study data save normally
- Export completes
- Destination receipt is confirmed when applicable
- No unresolved data-handling error remains

**Expected outcome:** The complete study-processing workflow functions normally.

If all applicable verification passes, troubleshooting can stop and the scanner may be returned to service.

## If the Problem Persists

If study workflow, local data availability, workstation responsiveness, external network connectivity, destination availability, and approved restart procedures have been checked but saving, reconstruction, or export still fails, the cause may involve local storage, database services, reconstruction software, workstation hardware, internal communication, corrupted study data, network configuration, or another service-level condition.

The system should be:

- Removed from service when data integrity or reliable clinical operation cannot be assured
- Labeled Out of Service
- Sent for repair or formal system evaluation
- Evaluated using appropriate GE Healthcare documentation and approved diagnostic tools
- Repaired or configured only by qualified personnel

Preserve affected patient data whenever possible and coordinate with imaging informatics or IT before any action that could delete or overwrite studies.

After repair, verify acquisition, storage, reconstruction, retrieval, and export before return to clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Before repeating any PET or CT acquisition, confirm whether the original raw or reconstructed data still exist and can be recovered or processed.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient and preserve acquired data before troubleshooting study-processing problems. Separate storage, reconstruction, and export failures, verify external workflow and network causes first, and escalate when data integrity or reliable processing cannot be assured.

That is successful troubleshooting.
