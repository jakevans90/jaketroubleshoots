---
schemaVersion: 1
title: "Fujifilm Sonosite PX Ultrasound System - Freeze, Store, or Image Capture Function Not Working"
issueTitle: "Freeze, Store, or Image Capture Function Not Working"
description: "Troubleshoots failed freeze, store, or image capture caused by controls, workflow state, storage availability, configuration, or software responsiveness."
assetType: "Ultrasound System"
manufacturer: "Fujifilm Sonosite"
model: "PX"
slug: "fujifilm-sonosite-px-freeze-store-or-image-capture-function-not-working"
dateAdded: "2026-08-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that images on the SonoSite PX would freeze but would not save during an examination."
  cause: "Clinical Engineering found local storage was unavailable to the active workflow until the system was restarted, while the capture controls remained responsive."
  resolution: "Performed a controlled restart, verified repeated freeze, store, and image retrieval using a test workflow, and returned the system to service."
helpfulDetails:
  - "Function that failed"
  - "Whether the control responded"
  - "Patient/exam workflow state"
  - "Storage messages"
  - "External media connected"
  - "Whether saved images were retrievable"
  - "Result after restart"
  - "Local capture versus PACS behavior"
  - "Number of successful test captures"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots failed freeze, store, or image capture caused by controls, workflow state, storage availability, configuration, or software responsiveness.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Documentation

If image capture is required for the active examination and the PX cannot reliably freeze or store images, provide an alternate verified imaging or documentation method according to clinical workflow.

Do not allow missing image documentation to go unnoticed.

**Expected outcome:** Patient care and required image documentation can continue without depending on an unreliable capture function.

### 2. Confirm Which Function Fails

Determine whether the problem involves:

- Freeze
- Unfreeze
- Still-image capture
- Cine or clip capture
- Store function
- Only certain exams
- Only certain patients
- Capture works but saved images cannot be found

**Expected outcome:** The exact failed function is reproduced and separated from export or PACS transmission problems.

### 3. Verify the Relevant Control Responds

Test the touchscreen, control panel, or assigned physical control used for the function.

Confirm other user inputs respond normally.

**Expected outcome:** The command itself is being accepted. If the associated control is unresponsive, troubleshoot the control interface rather than the storage function.

### 4. Confirm the System Is in an Appropriate Imaging State

Verify live imaging is active when attempting freeze or capture and that no open dialog, incomplete workflow, or screen state is preventing the expected command.

**Expected outcome:** The function works in the correct operating state or a genuine capture problem remains.

### 5. Verify Patient and Exam Workflow

Confirm the current study or patient workflow is properly established as required by normal operation.

Avoid changing protected system configuration.

**Expected outcome:** The image can be associated with the active examination and storage behavior is normal.

### 6. Check Available Local Storage Indicators

Review user-accessible system information for indications that storage is full, unavailable, or otherwise preventing additional image capture.

Do not delete patient data unless authorized and compliant with facility policy.

**Expected outcome:** Adequate storage is available or an identified storage-capacity problem is handled through approved data-management procedures.

### 7. Remove Nonessential External Media

If USB or other external storage is attached, safely remove nonessential media and retest local freeze/store operation.

This separates local image capture from external export failures.

**Expected outcome:** Local image capture functions independently of attached external media.

### 8. Perform a Controlled Restart

If controls function but freeze/store behavior remains abnormal, perform a normal system restart when no active patient examination depends on the unit.

**Expected outcome:** Normal freeze and capture functionality returns and remains stable.

### 9. Test a New Nonclinical Study or Approved Test Workflow

Using an appropriate test workflow:

- Generate a test image
- Freeze the image
- Store or capture it
- Confirm the saved image appears where expected
- Return to live imaging

Avoid creating inappropriate patient records.

**Expected outcome:** Freeze, capture, storage, and retrieval work as expected.

### 10. Verify Downstream Functions Separately

If local capture works but the image does not reach PACS or external storage, do not continue treating the problem as an image-capture failure.

Troubleshoot DICOM/PACS or USB export separately.

**Expected outcome:** The failure is correctly isolated to local capture, export, or network transmission.

### 11. Perform Final Functional Verification

Confirm:

- Freeze and unfreeze
- Still-image storage
- Any required clip/cine capture
- Saved-image retrieval
- Normal return to live imaging
- Stable operation through repeated cycles

**Expected outcome:** Required image capture functions are reliable. Troubleshooting can stop when the system performs the workflow normally.

## If the Problem Persists

If controls, workflow state, local storage availability, external media, and controlled restart have been ruled out, the remaining cause may involve local storage, application software, internal communication, configuration, or another service-level fault.

The system should be:

- Removed from service when image documentation is required and cannot be reliably performed
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Fujifilm SonoSite documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not modify internal storage, software, or protected configuration without authorized procedures.

After repair, verify complete freeze, store, retrieval, and associated workflow functions before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Confirm that images are actually stored and retrievable before assuming a successful button press has preserved required clinical documentation.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Separate control problems, workflow state, local storage, and downstream transfer before assuming internal failure. Reliable image capture and retrieval must be verified before returning the system to clinical use.

That is successful troubleshooting.
