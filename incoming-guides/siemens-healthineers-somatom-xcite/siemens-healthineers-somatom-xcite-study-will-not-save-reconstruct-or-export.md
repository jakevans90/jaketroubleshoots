---
schemaVersion: 1
title: "Siemens Healthineers SOMATOM X.cite CT Scanner - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "Use this guide when acquired CT data will not save, reconstruct, appear normally, or export to an intended destination."
assetType: "CT Scanner"
manufacturer: "Siemens Healthineers"
model: "SOMATOM X.cite"
slug: "siemens-healthineers-somatom-xcite-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-09-24"
taxonomyMode: "reuse"
ccr:
  complaint: "CT staff reported that a SOMATOM X.cite study completed acquisition but would not export to PACS."
  cause: "Clinical Engineering found that the local scanner study was intact but the configured PACS destination was temporarily unavailable."
  resolution: "PACS availability was restored by the appropriate support team, the existing study transferred successfully, and end-to-end image availability was verified without repeating the patient scan."
helpfulDetails:
  - "Exact save, reconstruction, or export message"
  - "Whether acquisition completed"
  - "Whether local images were available"
  - "Patient and study status"
  - "Processing or transfer queue status"
  - "Workstation responsiveness"
  - "Destination affected"
  - "Network status"
  - "PACS or IT findings"
  - "Whether existing data was preserved"
  - "Final reconstruction and transfer result"
---
## What This Guide Helps With

Use this guide when acquired CT data will not save, reconstruct, appear normally, or export to an intended destination.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data and Avoid Unnecessary Repeat Scanning
Do not repeat a patient scan solely because images are not immediately available. Preserve the existing study and raw data whenever possible and determine whether reconstruction or transfer can be restored first.  
**Expected outcome:** Existing patient data is protected and unnecessary repeat radiation exposure is avoided.

### 2. Confirm Which Stage Has Failed
Determine whether acquisition completed and whether the failure involves saving, reconstruction, local image display, export, or transfer to another system. Record the exact displayed message.  
**Expected outcome:** The failure is isolated to a specific stage of the image-processing workflow.

### 3. Confirm the Study and Patient Information
Verify that the correct patient and examination are selected and that normal required study information is present. Avoid creating duplicate studies unless directed by the approved clinical workflow.  
**Expected outcome:** The affected data is correctly identified and protected from accidental duplication.

### 4. Check Local Workstation Responsiveness
Confirm that the operator workstation remains responsive and that other normal functions operate. If the workstation is frozen or unstable, address that condition before attempting repeated save or reconstruction operations.  
**Expected outcome:** The problem is separated from a general workstation failure.

### 5. Review Processing or Transfer Status
Check the normal interface for pending, processing, failed, or queued reconstruction and export tasks. Do not delete queued patient data as a troubleshooting shortcut.  
**Expected outcome:** The location and status of the affected study are understood.

### 6. Verify Destination Availability for Export Problems
If local reconstruction succeeds but export fails, verify accessible network connectivity and confirm with PACS or IT staff that the intended destination is available.  
**Expected outcome:** A downstream destination or network problem is identified or ruled out.

### 7. Check for Broader Workflow Impact
Determine whether all studies are affected or only one study, reconstruction, or destination. Compare with a known-good recent workflow without exposing another patient.  
**Expected outcome:** The issue is isolated to a single dataset or recognized as a system-wide processing problem.

### 8. Perform an Approved Restart Only After Data Is Protected
If qualified personnel confirm that existing study data will not be jeopardized, perform the normal approved restart sequence and recheck the pending operation.  
**Expected outcome:** Normal saving, reconstruction, or export resumes without loss of patient data.

### 9. Verify the Complete Image Workflow
Confirm that an approved test dataset can be reconstructed, saved, displayed, and transferred to its intended destination as applicable.  
**Expected outcome:** The complete image-processing chain functions normally and troubleshooting can stop.

### 10. Escalate Unresolved Data-Processing Problems
If studies remain inaccessible, reconstruction repeatedly fails, storage appears unreliable, or data integrity is uncertain, discontinue clinical use until qualified service personnel evaluate the system.  
**Expected outcome:** Patient data is protected and the scanner is not returned to use with an unresolved processing or storage problem.

## If the Problem Persists

Patient selection, workstation status, processing queues, local connectivity, and receiving-system availability have been checked. Remaining causes may involve reconstruction services, storage systems, scanner software, database functions, internal networking, or other service-level components.

The scanner should be:

- Removed from service when the failure prevents reliable image processing or preservation
- Labeled Out of Service
- Sent for repair or service evaluation
- Evaluated using Siemens Healthineers documentation and approved diagnostic tools
- Repaired or configured only by qualified personnel

Protect existing patient data whenever possible. Before return to service, confirm that test data can be acquired, reconstructed, saved, displayed, and exported through the required clinical workflow. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not repeat a CT examination until staff have confirmed that the original acquisition cannot be safely recovered or reconstructed through the approved workflow.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect existing patient data and avoid unnecessary repeat exposure, isolate where the processing chain failed, verify external destinations before assuming scanner failure, and escalate unresolved data-integrity concerns appropriately.

That is successful troubleshooting.
