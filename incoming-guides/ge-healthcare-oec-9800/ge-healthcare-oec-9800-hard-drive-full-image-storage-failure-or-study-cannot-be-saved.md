---
schemaVersion: 1
title: "GE Healthcare OEC 9800 C-Arm - Hard Drive Full, Image Storage Failure, or Study Cannot Be Saved"
issueTitle: "Hard Drive Full, Image Storage Failure, or Study Cannot Be Saved"
description: "Troubleshoots study-storage problems caused by workflow, available storage, study completion, data handling, external transfer, or service-level disk and software faults."
assetType: "C-Arm"
manufacturer: "GE Healthcare"
model: "OEC 9800"
slug: "ge-healthcare-oec-9800-hard-drive-full-image-storage-failure-or-study-cannot-be-saved"
dateAdded: "2026-09-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the OEC 9800 would acquire images but new studies could not be saved."
  cause: "Clinical Engineering found that normal image transfer to the facility archive had stopped, resulting in local storage becoming unavailable for additional studies."
  resolution: "Restored the external connection, confirmed queued studies transferred, and verified that a controlled test study could be saved and recalled normally."
helpfulDetails:
  - "Exact storage message"
  - "New versus existing study behavior"
  - "Ability to recall prior images"
  - "Reported storage status"
  - "PACS or archive transfer status"
  - "Network connection status"
  - "Restart result"
  - "Test-study save result"
  - "Test-study recall result"
  - "Data-preservation actions"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots study-storage problems caused by workflow, available storage, study completion, data handling, external transfer, or service-level disk and software faults.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data and Clinical Continuity

If images cannot be saved reliably, notify clinical staff before additional imaging is performed. Follow facility policy for image retention and determine whether another verified system is required.

Do not delete patient studies simply to create space unless authorized by policy.

Expected outcome: Required patient images are not knowingly placed at risk of loss.

### 2. Confirm the Storage Complaint

Determine whether new images cannot be stored, an entire study cannot be saved, prior images cannot be recalled, storage is reported as full, or the system freezes during save operations.

Document any exact message displayed.

Expected outcome: The storage failure is clearly characterized.

### 3. Verify Normal Study Workflow

Confirm that staff are starting, acquiring, completing, and closing studies using the normal workflow.

Check whether the issue occurs with every study or only a specific patient record.

Expected outcome: User workflow is ruled out as the cause.

### 4. Check Available Storage Through Normal Functions

Use only normal operator-accessible system information to determine whether local image storage is reported as full or near capacity.

Do not access the operating system or hidden maintenance functions.

Expected outcome: Storage status is confirmed without unauthorized system changes.

### 5. Confirm Completed Studies Are Being Managed Normally

Determine whether stored studies are expected to be archived, transferred, printed, or otherwise managed before local deletion.

If facility workflow includes routine transfer, verify whether that process has stopped.

Expected outcome: A backlog caused by interrupted study management is identified or ruled out.

### 6. Verify External Transfer Path When Relevant

If images normally move to PACS, network storage, or another destination, inspect accessible network connections and confirm whether recent studies are transferring successfully.

Do not change network configuration without authorization.

Expected outcome: External transfer is functioning or an external communication problem is identified.

### 7. Restart the System Normally

If permitted and no unsaved patient data will be lost, perform a normal shutdown and restart.

Do not power-cycle repeatedly when data corruption is suspected.

Expected outcome: Temporary storage or application problems clear and normal study saving resumes.

### 8. Perform a Controlled Test Study

Using an approved non-patient workflow, create a test study, acquire an image, save or complete the study, and attempt to recall it.

Expected outcome: The test study stores and recalls successfully. If so, troubleshooting can stop after confirming clinical workflow.

### 9. Protect Existing Data if Storage Failure Continues

If studies cannot be stored or recalled consistently, stop additional clinical use that depends on local image retention. Do not format, initialize, delete, or repair storage media without approved service procedures and data-protection safeguards.

Expected outcome: Existing data is preserved for qualified evaluation.

### 10. Escalate Persistent Storage Failure

Remove the system from service when reliable image storage is required and cannot be verified.

Expected outcome: A system with unresolved image-retention risk is not returned to clinical use.

## If the Problem Persists

Workflow, accessible storage status, external transfer, and basic restart have been ruled out. Remaining possibilities may involve the hard drive, file system, database, application software, image-management service, network configuration, or another service-level storage issue.

The OEC 9800 should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved diagnostic tools.
- Repaired or configured only by qualified personnel.
- Handled according to facility requirements for protected health information and retained clinical images.

Return to service only after successful image acquisition, storage, retrieval, and any required export functions are verified.

Knowing when to protect data and stop instead of deleting or reformatting is proper troubleshooting.

## Clinical Use Tip

Do not assume images are safely retained until a saved study can be recalled or confirmed at the intended archive destination.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Exact storage message
- New versus existing study behavior
- Ability to recall prior images
- Reported storage status
- PACS or archive transfer status
- Network connection status
- Restart result
- Test-study save result
- Test-study recall result
- Data-preservation actions
- Final device status

## Final Thought

Image-storage failures are both equipment and patient-data issues. Verify workflow and external transfer before assuming disk failure, preserve existing data, confirm successful save and recall, and escalate service-level storage faults appropriately.

That is successful troubleshooting.
