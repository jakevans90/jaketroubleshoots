---
schemaVersion: 1
title: "Samsung Healthcare GM85 Fit Mobile X-Ray System - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "Addresses studies that cannot save, process, reconstruct, or export because of storage, workflow, network, software, or study-state problems."
assetType: "Mobile X-Ray System"
manufacturer: "Samsung Healthcare"
model: "GM85 Fit"
slug: "samsung-healthcare-gm85-fit-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-09-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported that images acquired on the GM85 Fit remained on the system and would not export to PACS."
  cause: "Clinical Engineering found the external network connection disconnected while local study storage remained functional."
  resolution: "Clinical Engineering restored network connectivity, successfully transferred the pending study to PACS, and verified a complete test save-and-export workflow."
helpfulDetails:
  - "Exact workflow step that failed"
  - "Whether images were stored locally"
  - "Displayed message"
  - "Number of affected studies"
  - "Local storage or queue status"
  - "Network connection status"
  - "PACS destination status"
  - "Whether other studies transferred"
  - "Restart result"
  - "End-to-end test result"
  - "Final device status"
---
## What This Guide Helps With

Addresses studies that cannot save, process, reconstruct, or export because of storage, workflow, network, software, or study-state problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data and Avoid Repeat Exposure
Do not repeat a patient exposure simply because a completed image will not save or export.

Preserve the current study and locally stored images whenever possible. Use another verified system for additional imaging if necessary.

Expected outcome: Existing patient data is protected and unnecessary radiation exposure is avoided.

### 2. Confirm Which Workflow Step Fails
Determine whether the image is acquired but will not save locally, processing does not complete, the study remains pending, reconstruction fails, or export to PACS or external media fails.

Record any displayed message exactly.

Expected outcome: The failure is isolated to a specific part of the workflow.

### 3. Verify the Study Is Complete and Valid
Using normal operator-accessible functions, confirm the study has required patient identification and is not still in an incomplete acquisition state.

Do not alter clinical demographics solely to bypass a save problem.

Expected outcome: The study is in a valid state for normal saving or export.

### 4. Check Local System Responsiveness
Confirm the console remains responsive and other studies or normal functions can be viewed.

If the workstation is frozen or unstable, address the workstation condition before assuming a storage-specific problem.

Expected outcome: The local workstation is operating normally or the issue is recognized as a broader system fault.

### 5. Check Storage or Queue Status
Review normal system indicators for storage warnings, pending studies, transfer queues, or failed exports.

Do not delete clinical studies or clear queues simply to free space unless authorized procedures specifically direct it and patient data has been protected.

Expected outcome: Any visible storage or queue condition is identified without risking patient data.

### 6. Determine Whether Saving and Export Are Separate
Confirm whether the study exists locally but cannot export, or whether it never saves locally.

A study that saves locally but will not transmit points toward communication or destination issues rather than image acquisition.

Expected outcome: The problem is narrowed to local storage, processing, or downstream transfer.

### 7. Verify Destination Connectivity
If export is the only failure, check physical network connectivity, the selected destination, and whether other studies can transfer.

Coordinate with PACS or IT if the destination appears unavailable.

Expected outcome: The export path is either restored or ruled out as the source of the problem.

### 8. Perform a Controlled Restart Only After Protecting Data
If the application remains unstable and locally acquired patient data is protected according to facility procedure, perform a normal supported restart when appropriate.

Avoid hard shutdowns when unsaved patient data may still be recoverable.

Expected outcome: The system returns to stable operation without loss of required patient information.

### 9. Verify With a Nonpatient Test Workflow
After correction, use an approved test or nonpatient workflow to confirm acquisition, processing, local saving, and export functions.

Expected outcome: A complete test workflow saves and processes correctly, and export succeeds when required. If so, troubleshooting can stop.

## If the Problem Persists

If study state, workstation responsiveness, visible storage status, transfer queues, physical network connectivity, and destination availability have been checked, common external causes have been ruled out.

Possible remaining categories include local storage failure, database or application faults, reconstruction software, filesystem issues, workstation hardware, DICOM services, or service-level configuration.

The system should be:

- Removed from service when reliable storage of patient images cannot be assured.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate Samsung Healthcare documentation and approved diagnostic methods.
- Repaired or configured only by qualified personnel.

Preserve recoverable patient data and coordinate with PACS or IT as appropriate. Verify the complete acquire-save-process-export workflow before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Never repeat an exposure solely because an image failed to export; first determine whether the original image is safely stored locally.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Study-storage troubleshooting should protect existing patient data, distinguish local storage from downstream transfer problems, verify external communication causes before assuming software or hardware failure, and prove the complete workflow before clinical release.

That is successful troubleshooting.
