---
schemaVersion: 1
title: "Verathon GlideScope Video Laryngoscope - Video Recording or Snapshot Capture Failure"
issueTitle: "Video Recording or Snapshot Capture Failure"
description: "Addresses failed recording or image capture caused by storage, media, controls, permissions, capacity, configuration, or software problems."
assetType: "Video Laryngoscope"
manufacturer: "Verathon"
model: "GlideScope"
slug: "verathon-glidescope-video-recording-or-snapshot-capture-failure"
dateAdded: "2026-08-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the GlideScope snapshot button responded but no image file appeared in storage."
  cause: "Clinical Engineering found that the approved removable storage media was full."
  resolution: "Clinical Engineering followed the authorized data-management process, installed available approved media, and verified successful snapshot capture and retrieval."
helpfulDetails:
  - "Recording or snapshot function affected"
  - "Exact displayed message"
  - "Live-video condition"
  - "Capture-control response"
  - "Storage location"
  - "Available capacity"
  - "Media type and condition"
  - "Known-good media result"
  - "File timestamp and retrieval path"
  - "Final device status"
---
## What This Guide Helps With

Addresses failed recording or image capture caused by storage, media, controls, permissions, capacity, configuration, or software problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Airway Priorities

Recording and snapshot functions are secondary to airway visualization. Do not interrupt airway management or manipulate a malfunctioning system while it is being used on a patient.

Continue clinical care with a stable live image or move to another verified device if primary visualization is affected.

**Expected outcome:** Patient safety and live airway visualization are maintained independently of recording functions.

### 2. Confirm the Exact Capture Failure

Determine whether recording will not start, stops unexpectedly, snapshots are not saved, files cannot be found, or capture controls do not respond. Record any displayed message exactly.

Reproduce the issue using nonpatient test content and the same storage configuration.

**Expected outcome:** The failure is identified as control, storage, file-retrieval, or software related.

### 3. Verify Live Video and Basic System Operation

Confirm the camera is recognized and a stable live image is present. Verify the monitor is not frozen and other user controls respond normally.

Recording troubleshooting should not proceed until basic video operation is stable.

**Expected outcome:** Live video and general system controls operate normally.

### 4. Confirm the Correct Capture Control

Use the normal user-accessible recording or snapshot control for the specific GlideScope configuration. Check whether the control is on the monitor, handle, touchscreen, or accessory.

Inspect the button or touchscreen area for damage, contamination, or obstruction.

**Expected outcome:** The correct capture control is used and responds normally.

### 5. Check Storage Presence and Capacity

Verify that the required approved storage location or removable media is present, correctly inserted, and recognized. Review available storage through normal user-accessible menus.

Do not delete patient data without authorization and an approved data-handling process.

**Expected outcome:** Sufficient recognized storage is available. If storage is full, authorized data management restores capture function.

### 6. Inspect Removable Media When Applicable

Confirm removable media is the approved type and is not physically damaged, write-protected, contaminated, or improperly seated. Do not use unknown media that could introduce malware or corrupt files.

**Expected outcome:** Approved media is fully inserted and available for writing.

### 7. Test With Known-Good Approved Media

When applicable, use known-good approved media with no protected patient information. Attempt a test snapshot and short recording.

**Expected outcome:** Successful capture with known-good media identifies the original media as defective, incompatible, full, or write-protected.

### 8. Verify Date, Time, and File Retrieval Location

Confirm the system date and time are reasonable and that staff are looking in the correct folder, patient record, or media location. An incorrectly dated file may appear missing.

Do not change network or protected configuration without authorization.

**Expected outcome:** Newly captured test files appear in the expected location with identifiable timestamps.

### 9. Restart the System Normally

After confirming no active clinical use or file-writing process, perform a normal shutdown and restart. Reattempt capture with a stable live image and approved storage.

Do not repeatedly power-cycle a unit that freezes or restarts during boot.

**Expected outcome:** Recording and snapshot functions return after a normal restart. If so, complete repeated verification before return to service.

### 10. Perform Final Functional Verification

Capture a test snapshot and recording, stop the recording normally, locate the saved files, and confirm they can be opened or exported through the approved workflow.

Ensure no test content is mistaken for a patient record.

**Expected outcome:** Capture, storage, retrieval, and playback or review work consistently. The system may return to service after all required checks pass.

## If the Problem Persists

The live image, controls, available capacity, approved media, file location, date and time, and normal restart have been evaluated. The remaining cause may involve internal storage, file-system corruption, software, permissions, configuration, or capture-control hardware.

Remove the device from service if recording is required for the clinical workflow or if the failure affects general reliability. Label it **Out of Service** and send it for qualified repair or bench evaluation using manufacturer documentation and approved service tools.

Protect stored patient information throughout evaluation. Return-to-service testing must verify capture, saving, retrieval, export as applicable, live video, and normal startup. Stopping before unauthorized data deletion or software changes is proper troubleshooting.

## Clinical Use Tip

Never allow a recording failure to delay airway care; confirm required documentation capability before the procedure when recording is clinically expected.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Keep airway visualization separate from documentation functions, verify controls and storage before assuming software failure, protect patient data, escalate unresolved capture problems, and document the complete test result.

That is successful troubleshooting.
