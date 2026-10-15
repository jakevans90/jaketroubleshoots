---
schemaVersion: 1
title: "GE Healthcare CardioLab Electrophysiology Recording System - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "CardioLab study data cannot be saved or exported because of storage, patient-record, network, destination, software, or external media problems."
assetType: "Electrophysiology Recording System"
manufacturer: "GE Healthcare"
model: "CardioLab"
slug: "ge-healthcare-cardiolab-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-10-15"
taxonomyMode: "reuse"
ccr:
  complaint: "EP staff reported that a completed CardioLab study would not export to the configured network destination."
  cause: "Clinical Engineering found the workstation network connection disconnected, preventing access to the export destination."
  resolution: "The network connection was restored, the study exported successfully and was confirmed at the destination, and CardioLab was returned to service."
helpfulDetails:
  - "Save, reopen, processing, or export function affected"
  - "Exact displayed message"
  - "Patient and study involved"
  - "Whether the study remained accessible locally"
  - "Export destination"
  - "External media condition"
  - "Network-link status"
  - "Destination-system availability"
  - "Whether another test study succeeded"
  - "Data-preservation actions taken"
  - "Confirmation at receiving destination"
  - "Final device status"
---

## What This Guide Helps With

CardioLab study data cannot be saved or exported because of storage, patient-record, network, destination, software, or external media problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Existing Study Data

Do not restart, power-cycle, delete records, or disconnect storage during an active study solely to troubleshoot a save or export problem.

If the procedure is ongoing, notify the clinical team and preserve all accessible data before attempting corrective action.

**Expected outcome:** Existing patient and study data are protected while the failure is investigated.

### 2. Confirm the Exact Data Failure

Determine whether CardioLab cannot save the active study, cannot reopen existing data, cannot perform a supported processing function, or cannot export to the intended destination.

Record the exact displayed message and when it occurs.

**Expected outcome:** The failed operation and affected study are clearly identified.

### 3. Verify the Patient and Study Context

Confirm that the intended patient and study are open and that required identifying information is present.

Do not create duplicate studies or alter patient identifiers unless clinically authorized.

**Expected outcome:** The correct study context is active and internally consistent.

If correcting an authorized workflow or patient-record issue permits the study to save normally, verify the saved record and stop troubleshooting.

### 4. Check for Obvious Storage or Media Conditions

Review user-visible storage or export status information where available. Confirm approved external media, network destinations, or removable storage are correctly connected when part of the supported workflow.

Do not delete clinical data simply to create space unless following an approved data-management process.

**Expected outcome:** The selected save or export destination is available and connected.

If restoring an external destination or approved media connection resolves the issue, confirm the exported data can be accessed and stop troubleshooting.

### 5. Inspect the Network Connection for Network-Based Exports

Check Ethernet connections and link indicators when the destination is remote.

Determine whether other network services on CardioLab are operating normally.

**Expected outcome:** CardioLab has a stable physical network connection to support the export workflow.

If reconnecting an external network cable restores successful export, verify destination receipt and stop troubleshooting.

### 6. Check the Destination System

Determine whether the archive, network share, server, PACS, or other approved destination is available.

If multiple CardioLab functions fail to reach the same destination, coordinate with IT, PACS, or integration support rather than repeatedly modifying the workstation.

**Expected outcome:** The intended destination is available and accepting transfers.

If the remote destination was unavailable and normal transfer resumes after restoration, verify receipt and stop troubleshooting.

### 7. Test Another Approved Study or Destination When Appropriate

Without risking patient data, determine whether the failure is specific to one study or affects all save/export attempts.

Where permitted, use a nonclinical test record or approved alternate destination to isolate the problem.

**Expected outcome:** The problem is localized to one study, one destination, or the CardioLab system itself.

If the issue is confined to an external destination, escalate to that system owner rather than altering CardioLab unnecessarily.

### 8. Avoid Data-Loss Actions During a Software Freeze

If the save or export failure occurs with a frozen workstation, preserve the on-screen state and follow institutional procedures before restarting.

If the event involved a serious clinical incident, preserve logs and study information according to local incident-response requirements.

**Expected outcome:** Diagnostic information and recoverable study data are preserved.

### 9. Verify the Complete Data Workflow

After correcting the issue, confirm that the study saves successfully, can be reopened when applicable, and reaches the intended export destination.

For supported processing or reconstruction functions, verify the resulting data are complete and usable rather than relying solely on a completion message.

**Expected outcome:** CardioLab saves and transfers the expected study information successfully.

If end-to-end verification passes, troubleshooting is complete.

### 10. Escalate Persistent Save or Export Failure

If CardioLab continues to fail after study context, storage destination, physical networking, and remote-system availability are ruled out, remove it from service if data reliability is required for clinical operation.

Do not reinstall software, manipulate databases, delete system files, or alter protected storage configuration without authorized service procedures.

**Expected outcome:** Persistent data-integrity or software problems are escalated without risking clinical records.

## If the Problem Persists

Common patient-record, external media, storage-destination, physical-network, and remote-system causes have been ruled out. Remaining possibilities may involve workstation storage, database services, CardioLab software, data corruption, system configuration, or managed infrastructure.

The CardioLab system should be:

- Removed from service if reliable study storage cannot be assured.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved diagnostic tools.
- Repaired, recovered, or configured only by qualified personnel.

Before return to service, verify creation, saving, reopening, and applicable export of a test study. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not power-cycle CardioLab during an unsaved active study unless patient safety requires it and the clinical team understands the potential data-loss risk.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect existing study data before taking corrective action. Verify the study context, destination, networking, and downstream system before assuming an internal storage or software failure, and escalate persistent data-integrity problems appropriately.

That is successful troubleshooting.
