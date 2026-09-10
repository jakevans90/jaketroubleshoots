---
schemaVersion: 1
title: "Philips Lumify Ultrasound System - Exam Will Not Save, Export, or Upload"
issueTitle: "Exam Will Not Save, Export, or Upload"
description: "Troubleshoot Lumify exam storage and transfer failures involving patient data, device storage, export destination, connectivity, permissions, and workflow configuration."
assetType: "Ultrasound System"
manufacturer: "Philips"
model: "Lumify"
slug: "philips-lumify-exam-will-not-save-export-or-upload"
dateAdded: "2026-09-10"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that completed Lumify exams would not save and the application displayed a storage-related warning."
  cause: "Clinical Engineering found that the mobile device had insufficient available storage for new examinations."
  resolution: "Clinical Engineering cleared approved nonclinical storage according to policy and verified successful saving and retrieval of a test examination before return to service."
helpfulDetails:
  - "Whether save, export, or upload failed"
  - "Exact displayed message"
  - "Whether all exams were affected"
  - "Available device storage"
  - "Required patient fields present"
  - "Export destination tested"
  - "Network connection status"
  - "Local save result"
  - "Remote transfer result"
  - "Final destination verification"
  - "Final equipment status"
---

## What This Guide Helps With
Troubleshoot Lumify exam storage and transfer failures involving patient data, device storage, export destination, connectivity, permissions, and workflow configuration.

## Step-by-Step Troubleshooting
### 1. Protect Patient Data and Maintain Clinical Workflow
Do not repeatedly manipulate or delete an affected patient exam without confirming institutional data-handling requirements. If ongoing imaging is needed, use another verified system when necessary.

Preserve any available images and patient information until the failure is understood.

Expected outcome: Patient care continues and potentially recoverable examination data is protected.

### 2. Confirm Which Function Is Failing
Determine whether the exam cannot be saved locally, cannot be exported, or saves successfully but will not upload.

Capture any displayed message and determine whether the problem affects all exams or one specific study.

Expected outcome: The failure is separated into local storage, export, or network-upload behavior.

### 3. Verify the Exam Contains Required Information
Review normal patient and examination fields for obviously missing information required by the facility's workflow.

Do not invent patient identifiers or alter clinical information simply to complete an upload.

Expected outcome: The exam contains the necessary information for the intended storage or transfer workflow.

### 4. Check Available Mobile Device Storage
Using normal mobile-device controls, check for low-storage conditions.

Do not delete clinical examinations or other protected information without following approved retention and data-management procedures.

Expected outcome: Adequate storage is available. If approved storage cleanup restores saving, verify by creating and saving a nonpatient test exam.

### 5. Restart the Application and Mobile Device
If the application appears stuck during save or export, close Lumify normally and reopen it. If necessary, restart the mobile device.

Confirm that required data remains intact before continuing.

Expected outcome: Lumify resumes normal save and export behavior. If successful, proceed to final verification.

### 6. Verify the Export Destination
For exports to an approved destination, confirm the expected storage location, connection, or receiving application is available and accessible.

Inspect any physical connection used in the workflow.

Expected outcome: The export destination is present and reachable. If restoring the destination resolves the failure, troubleshooting can stop after verification.

### 7. Verify Network Connectivity for Uploads
If the exam saves locally but will not upload, confirm that the mobile device is connected to the expected network and has normal network access required for the workflow.

Do not alter enterprise security settings or certificates without authorization.

Expected outcome: Required network connectivity is available. If reconnecting to the approved network restores upload operation, verify successful transfer and troubleshooting can stop.

### 8. Compare Local Save Versus Remote Transfer
Create an approved nonpatient test exam and determine whether it saves locally. Then test the normal export or upload process.

Expected outcome: The comparison shows whether the fault is local to Lumify storage or downstream in the transfer path.

### 9. Verify Successful Completion
After correction, save a test exam and complete the intended export or upload. Confirm that the receiving destination contains the expected study when applicable.

Expected outcome: The full workflow completes successfully from acquisition through final destination. Troubleshooting can stop.

### 10. Escalate Persistent Data-Handling Failure
If exams still cannot save, export, or upload after storage, destination, network, and workflow checks, stop external troubleshooting.

Expected outcome: The affected system is removed from clinical use when reliable exam retention cannot be assured and the issue is escalated.

## If the Problem Persists
Common external causes have been ruled out. Remaining possibilities include application data corruption, local storage problems, permissions issues, destination configuration faults, enterprise infrastructure problems, or other service-level software conditions.

Remove the device from service when patient studies cannot be reliably retained. Label it Out of Service and send it for bench or software evaluation. Use appropriate Philips documentation, organizational IT procedures, and approved test methods. Software repair or configuration changes should be completed only by qualified personnel.

Return to service only after local saving and the required export or upload workflow are successfully verified end to end.

## Clinical Use Tip
Confirm that an exam actually reached its required destination before deleting or clearing any local copy according to approved workflow.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought
Treat image retention as part of the clinical workflow. Preserve patient data, isolate local storage from downstream transfer problems, verify the complete path, and escalate when reliable exam handling cannot be assured.

That is successful troubleshooting.
