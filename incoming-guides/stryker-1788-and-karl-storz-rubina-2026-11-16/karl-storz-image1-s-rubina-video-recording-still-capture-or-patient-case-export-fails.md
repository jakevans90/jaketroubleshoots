---
schemaVersion: 1
title: "Karl Storz IMAGE1 S Rubina Endoscopic / OR Camera System - Video Recording, Still Capture, or Patient-Case Export Fails"
issueTitle: "Video Recording, Still Capture, or Patient-Case Export Fails"
description: "Helps isolate capture or export problems caused by controls, storage, removable media, connections, case workflow, network path, or configuration issues."
assetType: "Endoscopic / OR Camera System"
manufacturer: "Karl Storz"
model: "IMAGE1 S Rubina"
slug: "karl-storz-image1-s-rubina-video-recording-still-capture-or-patient-case-export-fails"
dateAdded: "2026-11-16"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that still images appeared to capture but were not available on the approved export media."
  cause: "Clinical Engineering found the removable storage device was not being recognized by the system."
  resolution: "The approved storage media was replaced, test images were captured and exported successfully, and file retrieval was verified."
helpfulDetails:
  - "Function that failed"
  - "Whether live video remained normal"
  - "Capture control used"
  - "Case workflow status"
  - "Storage media recognition"
  - "Local save result"
  - "Network or external destination status"
  - "Test file retrieval result"
  - "Final export status"
  - "Final device status"
---

## What This Guide Helps With

Helps isolate capture or export problems caused by controls, storage, removable media, connections, case workflow, network path, or configuration issues.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Clinical Workflow

Do not allow troubleshooting of recording or export functions to interfere with active surgical visualization.

If images or recordings are clinically required, notify the team and establish an approved alternate documentation method.

**Expected outcome:** Patient care and required documentation can continue safely.

### 2. Confirm Which Function Is Failing

Determine whether still capture, video recording, local saving, patient-case association, removable-media export, or network export is affected.

Confirm whether the live image itself remains normal.

**Expected outcome:** The failure is narrowed to the specific recording or export stage.

If the function begins working normally and saved content is verified, troubleshooting can stop.

### 3. Verify Capture Controls

Test capture using the normal controller control and, if applicable, the assigned camera-head button.

Confirm that the expected control function has not been changed through normal user-accessible configuration.

**Expected outcome:** The capture command is accepted by the system.

If one control fails but another works, investigate the control path rather than storage.

### 4. Check Patient or Case Workflow

Verify that the case is properly initiated using the approved clinical workflow and that required patient or case information has been entered when applicable.

Do not create real patient records solely for testing.

**Expected outcome:** The recording session has the required valid case context.

If correcting the case workflow restores capture or export, perform final verification.

### 5. Check External Storage or Removable Media

If removable media is involved, confirm it is approved, properly inserted, recognized, and not visibly damaged.

Do not use unknown personal media on clinical equipment.

**Expected outcome:** Approved storage media is recognized and available for the intended function.

If replacing or reseating approved media restores export, verify saved content.

### 6. Check Network or External Destination When Applicable

If the failure involves network export, confirm the external network connection is physically connected and that other normal system communication indicators are present.

Do not modify network addresses, security settings, or institutional infrastructure without authorization.

**Expected outcome:** The physical communication path is available and no obvious external connection problem is present.

If the camera system saves locally but export fails, escalate the network, server, or integration path as appropriate.

### 7. Verify Saved Content

Perform a non-patient test using approved procedures. Confirm the system records or captures the test content and that the resulting file can be located or exported through the intended workflow.

**Expected outcome:** Captured content is successfully saved and retrievable.

If successful, troubleshooting can stop after confirming the clinical workflow.

### 8. Perform Final Functional Verification

Verify each required function: still capture, video recording, correct case association, and intended export destination.

**Expected outcome:** Required media functions complete successfully and saved content can be verified.

If these checks pass, the system may be returned to service.

## If the Problem Persists

Controls, case workflow, approved media, external connections, and intended export path have been checked.

Remove the affected recording or export function from service as appropriate and provide an approved alternate documentation workflow. If the system cannot meet required clinical documentation needs, label it **Out of Service** and send it for bench evaluation.

Persistent failures may involve internal storage, software, network integration, server communication, permissions, or configuration. Evaluate using appropriate Karl Storz documentation and approved tools.

Do not alter protected network or service settings without authorization. Verify successful storage and retrieval before return to service.

## Clinical Use Tip

A successful button press does not prove that a recording was saved; verify that the expected file actually exists at the intended destination.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Follow the media path from capture command through storage and final destination. Verify the actual saved result before declaring success, escalate infrastructure or internal problems appropriately, and document exactly what was tested.

That is successful troubleshooting.
