---
schemaVersion: 1
title: "Mindray Resona I9 Ultrasound System - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "Use when acquired images or studies cannot be stored, processed, reviewed, exported, or transferred through the expected workflow."
assetType: "Ultrasound System"
manufacturer: "Mindray"
model: "Resona I9"
slug: "mindray-resona-i9-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-10-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported Resona I9 studies could be acquired but would not export through the expected workflow."
  cause: "Clinical Engineering found the external network connection was not fully seated, preventing communication with the configured destination."
  resolution: "Clinical Engineering secured the network connection, completed a controlled test study, verified successful save and export, confirmed destination receipt, and returned the system to service."
helpfulDetails:
  - "Exact function that failed"
  - "Exact displayed message"
  - "Patient or test study workflow involved"
  - "Whether local saving works"
  - "Whether review works"
  - "Export destination"
  - "Network connection status"
  - "Removable media used, if applicable"
  - "Whether one or all studies are affected"
  - "Results after restart"
  - "Destination receipt confirmation"
  - "Final device status"
---
## What This Guide Helps With

Use when acquired images or studies cannot be stored, processed, reviewed, exported, or transferred through the expected workflow.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data and Continuity of Care
Do not continue acquiring clinically important images if there is no reliable way to preserve the examination. Avoid deleting studies, clearing storage, or repeating patient imaging solely to troubleshoot a storage problem.

**Expected outcome:** Existing patient data is protected and additional data loss is avoided.

### 2. Identify the Exact Failed Function
Determine whether the problem occurs when saving newly acquired images, processing or reconstructing stored data, reviewing a study, exporting to removable media, or sending to a configured network destination. Record any displayed message.

**Expected outcome:** The failure is localized to storage, processing, external export, or network transfer.

### 3. Verify the Correct Patient and Study Are Active
Confirm that the intended patient and examination are selected and that the workflow is in the appropriate state for saving or exporting. Do not bypass patient-identification requirements.

**Expected outcome:** The failure is not caused by an incorrect or incomplete study workflow.

### 4. Confirm Basic System Responsiveness
Verify the workstation controls respond normally and live imaging remains functional. A broader workstation freeze should be treated as a system stability problem rather than only a save/export failure.

**Expected outcome:** The system is responsive enough for controlled testing.

### 5. Check the Intended Export Destination
For network export, verify the physical network connection and configured destination availability. For approved removable media, confirm the media is supported by the facility workflow, properly connected, and not visibly damaged.

**Expected outcome:** The selected export destination is accessible and correctly connected.

### 6. Test Another Approved Destination or Media When Appropriate
If the issue appears limited to removable media, test known-good approved media. If it appears limited to one configured network destination, determine whether other approved destinations function without changing protected configuration.

**Expected outcome:** The failure is isolated to a specific external destination or shown to be system-wide.

### 7. Check for Storage-Related Warnings
Review normal user-accessible system information for warnings indicating storage or study-management limitations. Do not delete patient studies or clear internal storage unless following an approved data-management procedure.

**Expected outcome:** Any storage-related condition is identified without risking patient data.

### 8. Perform a Controlled Restart if Appropriate
After ensuring active data has been handled according to facility procedure, perform a normal restart if the problem appears software-related and no patient is dependent on the system.

**Expected outcome:** Study management and export functions initialize normally after restart.

### 9. Repeat the Workflow With a Controlled Test
Using an approved test study or nonpatient workflow, acquire and save an image, review it, and test the reported export or processing function.

**Expected outcome:** The complete workflow succeeds without error.

### 10. Confirm Destination Receipt and Data Integrity
When exporting to PACS or another network destination, confirm the study is actually received and associated correctly. When using approved removable media, confirm the exported data can be accessed through the intended workflow.

**Expected outcome:** The study is saved and available at its intended destination. If successful, troubleshooting can stop.

## If the Problem Persists

Patient/study workflow, system responsiveness, external destinations, removable media, network connectivity, and controlled restart have been evaluated. A persistent failure may involve local storage, database or study-management software, processing software, internal computing hardware, DICOM configuration, or network infrastructure.

Remove the system from service if reliable patient-data storage cannot be assured. Label it **Out of Service** and arrange repair or bench evaluation using appropriate Mindray documentation and approved test equipment. Coordinate with PACS, imaging informatics, or IT when the failure involves network destinations or enterprise systems.

Do not erase studies, reinitialize storage, or perform software recovery without authorized procedures and appropriate protection of patient data.

Return the system to service only after an end-to-end test confirms reliable acquisition, saving, review, and the required export workflow.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Before releasing a patient after a storage or export problem, confirm that the clinically required images have actually been preserved according to the facility workflow.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect patient data first, separate local storage problems from export and network problems, verify external causes before assuming internal failure, confirm the entire workflow after correction, escalate unresolved faults, and document the outcome clearly.

That is successful troubleshooting.
