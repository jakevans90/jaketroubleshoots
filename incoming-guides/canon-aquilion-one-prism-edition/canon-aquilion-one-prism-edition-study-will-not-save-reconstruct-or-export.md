---
schemaVersion: 1
title: "Canon Aquilion ONE / PRISM Edition CT Scanner - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "Addresses failed study saving, reconstruction, or export caused by workstation state, storage, workflow, network communication, or software-related conditions."
assetType: "CT Scanner"
manufacturer: "Canon"
model: "Aquilion ONE / PRISM Edition"
slug: "canon-aquilion-one-prism-edition-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-09-24"
taxonomyMode: "reuse"
ccr:
  complaint: "CT staff reported completed studies would reconstruct normally but could not be exported to PACS."
  cause: "Clinical Engineering found local image processing was normal but the approved network connection to the workstation was disconnected."
  resolution: "Restored the network connection, exported an approved test study, confirmed receipt in PACS, and verified the normal study workflow."
helpfulDetails:
  - "Exact save, reconstruction, or export message."
  - "Patient/study status when failure occurred."
  - "Whether images exist locally."
  - "Whether reconstruction completed."
  - "Workstation responsiveness."
  - "Storage or processing warnings."
  - "Network connection status."
  - "Whether other studies are affected."
  - "Destination receipt verification."
  - "Final scanner status."
---
## What This Guide Helps With

Addresses failed study saving, reconstruction, or export caused by workstation state, storage, workflow, network communication, or software-related conditions.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data and Avoid Unnecessary Repeat Scans
Do not repeat a patient scan solely because images are not immediately saving, reconstructing, or exporting.

Preserve any available raw data, images, and study identifiers while troubleshooting.

**Expected outcome:** Existing diagnostic data is protected and unnecessary repeat radiation is avoided.

### 2. Confirm Which Function Is Failing
Determine whether the study fails to save locally, reconstruct, display, export to PACS, or complete more than one of these steps.

Record any displayed message exactly.

**Expected outcome:** The failed portion of the imaging workflow is clearly identified.

### 3. Confirm Workstation Responsiveness
Verify that the operator workstation is responsive and that the CT application is not frozen or partially unresponsive.

**Expected outcome:** A general workstation problem is identified or ruled out.

### 4. Verify Study and Patient Selection
Confirm that the expected patient and study are open and that staff are attempting to save or export the intended examination.

Avoid deleting, merging, or modifying patient records during troubleshooting unless required by approved policy.

**Expected outcome:** The problem is not caused by selecting the wrong study or incomplete workflow.

### 5. Check Local System Status and Storage Indications
Review normal user-accessible indicators for warnings related to storage, study processing, reconstruction queues, or unavailable resources.

Do not manually delete system files or alter storage partitions.

**Expected outcome:** Any visible storage or processing condition is identified without modifying protected system data.

### 6. Check Network Connectivity for Export Problems
If local saving and reconstruction work but export fails, inspect accessible network connections and verify whether PACS or other destinations are available.

**Expected outcome:** Local processing and network-transfer problems are separated.

### 7. Determine Whether the Problem Is Study-Specific
Check whether another approved test or previously completed study can be accessed or exported without altering patient data.

Do not use unrelated patient records unnecessarily.

**Expected outcome:** The issue is narrowed to one study or confirmed to affect general system processing.

### 8. Perform an Approved Controlled Restart if Appropriate
If no active reconstruction or data-preservation concern prevents it, and approved procedures allow, perform a controlled workstation or system restart.

Do not restart if doing so could jeopardize unsaved or unrecoverable patient data without first escalating.

**Expected outcome:** Processing resumes without data loss and the affected functions return.

### 9. Verify Complete Study Workflow
Using an appropriate approved test case, confirm that images can be acquired or accessed, reconstructed, saved, and exported to the intended destination.

Confirm receipt at the destination when export is part of the complaint.

**Expected outcome:** The complete study workflow operates normally.

If achieved, troubleshooting is complete.

### 10. Escalate Persistent Save, Reconstruction, or Export Failure
If data remains inaccessible, processing repeatedly fails, or study integrity is uncertain, remove the system from clinical use as appropriate and escalate to qualified Canon service and imaging informatics personnel.

Do not manipulate databases, reconstruction software, storage arrays, or operating-system files without authorization.

**Expected outcome:** Patient data is preserved and higher-level troubleshooting proceeds without creating additional data risk.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may include workstation storage, database services, reconstruction software, processing resources, internal communications, DICOM services, network infrastructure, or service-level configuration.

The CT scanner should be:

- Removed from service when reliable study processing cannot be assured.
- Labeled Out of Service when appropriate.
- Sent for repair or qualified service evaluation.
- Evaluated using appropriate Canon, PACS, and IT documentation and approved diagnostic tools.
- Repaired or configured only by qualified personnel.

Verify acquisition, reconstruction, local saving, export, and destination receipt before returning the scanner to normal clinical operation.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Preserve existing patient data before restarting or escalating; inability to export does not automatically mean the images need to be reacquired.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect existing patient data, isolate local processing from network-transfer problems, avoid unnecessary repeat scans, and escalate unresolved study-handling failures with complete documentation.

That is successful troubleshooting.
