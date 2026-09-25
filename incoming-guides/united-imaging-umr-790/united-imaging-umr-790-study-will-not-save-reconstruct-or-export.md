---
schemaVersion: 1
title: "United Imaging uMR 790 MRI System - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "Troubleshoots failed study saving, reconstruction, or export caused by workflow, storage, workstation, network, study-specific, or communication problems."
assetType: "MRI System"
manufacturer: "United Imaging"
model: "uMR 790"
slug: "united-imaging-umr-790-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-09-25"
taxonomyMode: "reuse"
ccr:
  complaint: "MRI staff reported that a uMR 790 study reconstructed normally but would not export to PACS."
  cause: "Clinical Engineering found the workstation's external network connection was loose, interrupting communication with the configured destination."
  resolution: "The connection was secured, the affected study exported successfully, receipt at PACS was confirmed, and the complete workflow was verified."
helpfulDetails:
  - "Exact save, reconstruction, or export message"
  - "Study or series affected"
  - "Whether data exists locally"
  - "Workstation responsiveness"
  - "Whether other studies are affected"
  - "Storage-related warnings"
  - "Network connection status"
  - "PACS or destination availability"
  - "Controlled test result"
  - "Final data and device status"
---
## What This Guide Helps With

Troubleshoots failed study saving, reconstruction, or export caused by workflow, storage, workstation, network, study-specific, or communication problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data Before Making Changes
Do not delete studies, clear storage, restart unnecessarily, or recreate patient records until the status of acquired data is understood.

If the patient is still present, confirm whether additional imaging is clinically necessary before removing them from the department.

**Expected outcome:** Existing patient data is preserved and unnecessary repeat imaging is avoided.

### 2. Identify Which Part of the Workflow Failed
Determine whether the study:
- Acquired but will not save
- Saved but will not reconstruct
- Reconstructed but will not export
- Affects one series only
- Affects one study only
- Affects every new study

Record the exact displayed message.

**Expected outcome:** The failed stage of the imaging workflow is identified.

### 3. Confirm Workstation Responsiveness
Verify the workstation remains responsive and the MRI application is functioning normally.

Check for:
- Frozen application
- Delayed response
- Communication loss
- Unexpected restart
- Other abnormal behavior

**Expected outcome:** The workstation is stable enough to evaluate the study. If an approved normal restart is required, protect data first.

### 4. Verify the Study Exists Locally
Using normal clinical functions, confirm whether acquired images or series are present in local study storage.

Do not delete partial or failed data during troubleshooting.

**Expected outcome:** The available local data is identified and preserved.

### 5. Determine Whether the Problem Is Study-Specific
Check whether:
- Other existing studies open normally
- Another completed test study can save or reconstruct
- The failure applies to one sequence only
- All current workflow operations are affected

Use nonpatient testing when practical.

**Expected outcome:** The issue is narrowed to one study or a broader system condition.

### 6. Check Export and Network Availability
If saving and reconstruction work but export fails, inspect the external network connection and determine whether PACS or the selected destination is available.

Coordinate with IT or PACS support when appropriate.

**Expected outcome:** The export pathway is confirmed available. If network restoration allows successful export, verify destination receipt and stop.

### 7. Check Normal Destination and Export Selection
Confirm that the intended destination and normal export workflow are selected.

Do not modify protected DICOM or network configuration without authorization.

**Expected outcome:** The correct destination is being used. If correcting workflow selection resolves export, verify receipt and stop.

### 8. Check for Obvious Storage or System Warnings
Review normal user-visible system messages for indications related to local study storage or processing availability.

Do not manually purge storage or modify file systems without approved procedures and appropriate data safeguards.

**Expected outcome:** No unresolved user-visible storage condition remains. A service-level storage issue is escalated rather than altered experimentally.

### 9. Perform a Controlled Workflow Verification
After correcting an identified external cause, perform an approved nonpatient test and confirm:
- Acquisition completes
- Study saves
- Reconstruction completes
- Images open normally
- Export succeeds when required
- Destination receipt is verified

**Expected outcome:** The complete workflow operates successfully. Troubleshooting can stop.

### 10. Escalate Persistent Save, Reconstruction, or Export Failure
If workstation operation, local data presence, network connectivity, destination availability, and normal workflow have been checked but processing still fails, stop troubleshooting.

**Expected outcome:** The system is removed from clinical use as appropriate and escalated without risking patient data.

## If the Problem Persists

Common external and workflow causes have been ruled out. Remaining categories may include storage hardware, reconstruction services, application software, databases, internal communication, system configuration, or other service-level computing functions.

The device should be:
- Removed from service when reliable study retention or processing cannot be assured
- Labeled **Out of Service**
- Sent for repair or service evaluation
- Evaluated using United Imaging documentation and approved diagnostic tools
- Repaired or configured only by qualified personnel

Preserve affected studies and logs according to local procedures before service actions that could alter stored data.

Knowing when to stop external troubleshooting is proper troubleshooting. Return the system to clinical service only after the full acquisition-to-save-to-reconstruction-to-export workflow has been verified.

## Clinical Use Tip

Before releasing a patient after an unusual save or reconstruction failure, confirm that the clinically required images are actually stored and usable so avoidable repeat imaging is not needed.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Study-processing failures require protecting patient data before troubleshooting anything else. Identify exactly where the workflow stops, verify workstation and network conditions before assuming internal failure, and confirm the complete imaging-data path after correction.

That is successful troubleshooting.
