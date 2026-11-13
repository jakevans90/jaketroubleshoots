---
schemaVersion: 1
title: "Olympus EVIS EXERA III Endoscopic / OR Camera System - DICOM, Recording, or Image Export Fails"
issueTitle: "DICOM, Recording, or Image Export Fails"
description: "Troubleshoots failed image recording, DICOM transfer, or export caused by storage, media, network, connections, destination availability, or configuration."
assetType: "Endoscopic / OR Camera System"
manufacturer: "Olympus"
model: "EVIS EXERA III"
slug: "olympus-evis-exera-iii-dicom-recording-or-image-export-fails"
dateAdded: "2026-10-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that images were saved on the EVIS EXERA III but were not appearing at the configured DICOM destination."
  cause: "Clinical Engineering found the external network cable at the system cart was partially disconnected while local image storage remained functional."
  resolution: "Reseated the network connection, verified successful test-image transfer to the configured destination, and returned the system to service."
helpfulDetails:
  - "Whether capture, storage, recording, DICOM, or export failed"
  - "Whether images were stored locally"
  - "Destination affected"
  - "Network or data-cable condition"
  - "Recorder status"
  - "Storage or removable-media status"
  - "Patient/study information observed"
  - "Whether all destinations or only one were affected"
  - "IT/PACS/network testing performed"
  - "Results before and after correction"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots failed image recording, DICOM transfer, or export caused by storage, media, network, connections, destination availability, or configuration.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow and Preserve Required Images
If image documentation is required during an active procedure and the normal recording or export path has failed, notify clinical staff immediately and use an approved alternate documentation method when available.

Do not repeatedly restart or reconfigure the system while a patient depends on it.

**Expected outcome:** Clinical documentation can continue through an approved alternate workflow while the affected system is evaluated.

### 2. Confirm the Exact Failure
Determine whether the issue involves:
- Image capture not occurring
- Images being captured but not saved
- Recording unavailable
- DICOM transfer failure
- Network destination unavailable
- USB or removable-media export failure
- Images saved locally but not reaching the intended destination

Confirm whether all studies are affected or only one patient, destination, or export method.

**Expected outcome:** The failure is isolated to capture, local storage, export, or network transfer.

### 3. Verify Normal System Operation and Local Capture
Confirm the EVIS EXERA III and any connected recording or image-management equipment are powered and operating normally.

Attempt a controlled image capture without a patient connected, when appropriate.

Determine whether the image appears in local review or storage.

**Expected outcome:** Local capture either succeeds, isolating the problem to export/communication, or fails, indicating a more local recording issue.

### 4. Inspect External Recording and Data Connections
Inspect network cables, USB connections, recorder connections, external storage interfaces, and other accessible data cables.

Look for:
- Loose connectors
- Damaged cables
- Incorrect ports
- Unseated adapters
- Bent connector hardware
- Recently disconnected peripherals

**Expected outcome:** All required external data connections are secure and undamaged. If reconnecting a cable restores transfer or recording, verify repeated operation and stop troubleshooting.

### 5. Verify Destination or Recorder Availability
If images are sent to a network destination, confirm the receiving system or approved destination is available.

If an external recorder is used, verify it is powered, ready, and not displaying an external fault.

If the issue is limited to one destination, compare with another approved destination when available.

**Expected outcome:** The receiving device or destination is operational and available to the imaging system.

### 6. Check Local Storage and Export Media
Verify that local storage or approved removable media is available and not obviously full, write-protected, damaged, or improperly connected.

Use only supported media and approved export methods.

Do not erase clinical data without authorization.

**Expected outcome:** Storage and export media are available and capable of accepting data. If replacing a faulty external medium restores export, verify the files and stop troubleshooting.

### 7. Confirm Patient and Study Information
If DICOM transfer is affected, verify that required patient and study information has been entered or received correctly.

Check for obvious incomplete, mismatched, or invalid entries that could interfere with the facility's workflow.

Do not alter patient identifiers merely to force a transfer.

**Expected outcome:** Required patient and study information is present and consistent with the intended destination workflow.

### 8. Verify Accessible Network and Destination Configuration
Review user-accessible network status and destination selections without altering protected service configuration.

Confirm:
- The intended destination is selected
- Network connection is shown as available, if the system provides that information
- No recent destination change is evident
- The correct recording/export path is selected

Compare with a known-good system configuration when appropriate.

**Expected outcome:** Accessible destination and network selections are appropriate. If correcting an approved selection restores transfer, document the change and stop troubleshooting.

### 9. Test the Network Path With Appropriate Support
If local recording works but DICOM transfer fails, coordinate with the appropriate IT, PACS, integration, or networking team.

Verify external infrastructure such as:
- Network port availability
- Connected switch path
- Destination reachability
- DICOM service availability
- Recent network or server changes

Do not alter network addressing or protected DICOM configuration without authorization.

**Expected outcome:** The external communication path is confirmed available, or an infrastructure issue is identified and routed to the appropriate support team.

### 10. Perform a Controlled End-to-End Verification
After correction, perform a test using approved non-patient or test data when permitted.

Verify:
- Image capture completes
- Image or video is stored locally when expected
- Recording operates correctly
- Exported files can be opened
- DICOM images reach the intended destination
- Patient and study data remain associated correctly

**Expected outcome:** The complete recording or export workflow functions successfully. Troubleshooting can stop after end-to-end verification.

## If the Problem Persists

If DICOM, recording, or export continues to fail after local capture, storage, cables, media, destination availability, accessible configuration, and external network infrastructure have been checked, common external causes have been ruled out.

The remaining cause may involve internal storage, software, network-interface hardware, configuration, database handling, recorder integration, or another service-level condition.

The affected equipment should be:
- Removed from service when the failed function is required for clinical operation
- Labeled **Out of Service** when appropriate
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Coordinate with IT, PACS, cybersecurity, or the appropriate integration team when the failure involves hospital infrastructure rather than the device itself.

Return the system to clinical service only after the required image-management workflow has been successfully verified.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Verify the entire documentation path from image capture through the final clinical destination; a locally saved image does not confirm successful DICOM transfer.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- rendered from front matter -->

## Final Thought

Separate local image capture from storage, export, and network transfer so the failure can be isolated logically. Verify cables, storage, destinations, and infrastructure before assuming an internal system fault, then escalate appropriately and document the complete resolution.

That is successful troubleshooting.
