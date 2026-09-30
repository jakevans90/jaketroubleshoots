---
schemaVersion: 1
title: "Canon Ultimax-i Fluoroscopy / Interventional System - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "Troubleshoots study-processing failures caused by workflow state, storage, workstation responsiveness, patient information, destination availability, or communication problems."
assetType: "Fluoroscopy / Interventional System"
manufacturer: "Canon"
model: "Ultimax-i"
slug: "canon-ultimax-i-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that studies acquired on the Canon Ultimax-i would save locally but would not export to PACS."
  cause: "Clinical Engineering found the workstation's external network connection loose, preventing communication with the destination."
  resolution: "Clinical Engineering secured the network connection and verified successful export and PACS receipt of a nonclinical test study."
helpfulDetails:
  - "Save, reconstruct, or export function affected"
  - "Exact displayed message"
  - "One study or all studies affected"
  - "Workstation responsiveness"
  - "Local storage warning"
  - "Patient/study workflow status"
  - "Network connection condition"
  - "Destination availability"
  - "Test study result"
  - "Confirmation of final receipt"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots study-processing failures caused by workflow state, storage, workstation responsiveness, patient information, destination availability, or communication problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data and Clinical Continuity
Do not delete, overwrite, or repeatedly manipulate a study that may contain the only copy of clinically important images. Confirm that necessary imaging data is preserved locally when possible and follow departmental downtime procedures.

**Expected outcome:** Existing patient data is protected before troubleshooting begins.

### 2. Confirm Which Operation Is Failing
Determine whether the study cannot be saved locally, reconstruction does not complete, export fails, or the system reports that the study is incomplete. Record any displayed message and whether the issue affects one study or every study.

**Expected outcome:** The exact workflow stage and scope of the failure are identified.

### 3. Verify Workstation Responsiveness
Confirm that the workstation is responding normally and that the problem is not part of a larger freeze or communication failure. Check whether other studies can be opened or normal user functions can be completed.

**Expected outcome:** The workstation is either confirmed stable or identified as part of the problem.

### 4. Review Study Information and Workflow
Verify that required patient and examination information is present and that the study has been completed through the normal clinical workflow. Compare the affected study with a known normal workflow without changing protected clinical data unnecessarily.

**Expected outcome:** No obvious incomplete workflow or missing information is preventing processing. If completing the proper workflow resolves the problem, verify and stop.

### 5. Check Local Storage or System Messages
Review normal user-accessible indicators for storage or processing warnings. Do not delete clinical studies or clear storage solely to create space without following approved data-retention procedures.

**Expected outcome:** No obvious user-accessible storage condition is preventing save or reconstruction.

### 6. Check Export Destination Availability
If local saving succeeds but export fails, verify the intended destination is available and that network connectivity is intact. Check whether another study can be transferred through the same route.

**Expected outcome:** The problem is narrowed to local processing or external export communication.

### 7. Use an Approved Restart When Appropriate
If the workstation is stable enough to protect existing data and normal procedures permit, complete a controlled application or system restart. Avoid forced shutdown during active saving, reconstruction, or export.

**Expected outcome:** Processing services restart normally without loss of stored data.

### 8. Verify With a Nonclinical Test Study
Using an approved test workflow, confirm that a new study can be saved, processed or reconstructed as applicable, and exported to the intended destination. Confirm destination receipt when export is tested.

**Expected outcome:** Study processing and export complete successfully end to end. If successful, troubleshooting can stop.

## If the Problem Persists

Persistent save, reconstruction, or export failures after workflow, workstation state, local storage indications, destination availability, and network connectivity have been checked may involve software, database functions, storage hardware, reconstruction services, configuration, DICOM services, or another service-level problem.

Preserve affected clinical data. Remove the system from service if reliable study storage or image availability cannot be assured, label it **Out of Service**, and arrange Canon and/or IT/PACS evaluation as appropriate.

Do not delete patient data, rebuild databases, modify protected configuration, or perform unsupported software repair. After service, verify local save, processing, reconstruction, export, destination receipt, and required clinical workflow before return to use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Before restarting a system with a study-processing problem, confirm that clinically important images have been preserved and are not actively being written or transferred.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Study-processing failures require protection of patient data first, followed by logical separation of workflow, workstation, storage, processing, and network causes. Verify external causes before assuming internal failure, escalate when data integrity is uncertain, and clearly document the final result.

That is successful troubleshooting.
