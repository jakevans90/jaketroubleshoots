---
schemaVersion: 1
title: "Mindray TE X Ultrasound System - Measurement, Annotation, or Exam Preset Will Not Save"
issueTitle: "Measurement, Annotation, or Exam Preset Will Not Save"
description: "Troubleshoots saving failures involving measurements, annotations, or presets caused by workflow state, permissions, storage availability, configuration, or software response."
assetType: "Ultrasound System"
manufacturer: "Mindray"
model: "TE X"
slug: "mindray-te-x-measurement-annotation-or-exam-preset-will-not-save"
dateAdded: "2026-11-24"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that newly entered exam annotations on the TE X disappeared after leaving the examination screen."
  cause: "Clinical Engineering found the user was attempting to save annotations before completing the required examination workflow."
  resolution: "Clinical Engineering verified the correct workflow with an approved test examination and confirmed that annotations saved and remained available after reopening the test record."
helpfulDetails:
  - "Item that would not save"
  - "Exact displayed message"
  - "User/login type"
  - "Examination state"
  - "Storage status"
  - "Whether other save functions worked"
  - "Test-exam result"
  - "Restart result"
  - "Persistence after reopening"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots saving failures involving measurements, annotations, or presets caused by workflow state, permissions, storage availability, configuration, or software response.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data
Do not experiment with patient records or delete clinical examinations while troubleshooting. If required measurements or annotations cannot be preserved, use an approved alternate documentation workflow.

Expected outcome: Patient information remains protected and required clinical documentation continues.

### 2. Confirm What Will Not Save
Determine whether the problem affects a measurement, annotation, customized preset, entire examination, or all saved settings. Note whether a message appears.

Expected outcome: The failed function is precisely identified rather than treated as a general system fault.

### 3. Verify the Examination or Workflow State
Using normal controls, confirm the system is in the appropriate examination or setup state for the requested save action and that required fields or workflow steps have been completed.

Expected outcome: The save function becomes available when the workflow is complete.

### 4. Confirm User Permissions
Determine whether the logged-in user is permitted to modify or save the requested item. Compare with an appropriately authorized account when institutional policy permits.

Expected outcome: Authorized users can perform the intended save action. Permission problems are escalated rather than bypassed.

### 5. Check Available Storage Status
Using normal user-accessible system information, confirm the TE X is not reporting unavailable or full storage. Do not delete patient records solely to create space without following institutional data-retention policy.

Expected outcome: Adequate storage is available and no storage warning prevents saving.

### 6. Test a Nonclinical Entry
Use an approved test examination or nonpatient workflow to create a simple measurement, annotation, or preset change and attempt to save it.

Expected outcome: The test item saves and remains available after navigating away and returning.

### 7. Perform a Normal Restart
If the interface appears unresponsive or changes fail to persist despite proper workflow and permissions, perform a normal restart when clinically appropriate.

Expected outcome: Normal saving function returns and remains stable after restart.

### 8. Recheck Configuration Without Unauthorized Changes
Confirm the expected user profile, preset library, and storage destination are selected through normal controls. Do not alter protected service configuration or perform software recovery.

Expected outcome: The intended save destination and user environment are selected correctly.

### 9. Perform Final Functional Verification
Save an approved test measurement, annotation, or preset; exit the relevant screen; return to it; and confirm the saved item remains available as expected.

Expected outcome: The saved information persists correctly. If it does not, keep the affected functionality out of clinical use and escalate.

## If the Problem Persists

Workflow state, permissions, storage availability, user-accessible configuration, and normal restart have been checked. Remaining causes may include software, database/storage services, profile configuration, internal storage, or another service-level condition.

Remove the TE X from service if the inability to save information compromises required clinical documentation or examination integrity. Label it **Out of Service** when appropriate and obtain repair or configuration support using approved Mindray documentation.

Do not delete clinical data, reset databases, reinstall software, or alter restricted configuration without proper authorization and data-protection procedures. Verify saving and retrieval before return to service.

## Clinical Use Tip

A measurement visible on the screen is not safely documented until the required information has actually been saved in the intended examination record.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect patient data, distinguish workflow and permission problems from actual storage failures, verify persistence with a controlled test, and escalate before making service-level changes.

That is successful troubleshooting.
