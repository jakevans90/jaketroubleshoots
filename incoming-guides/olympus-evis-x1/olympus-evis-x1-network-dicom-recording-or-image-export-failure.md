---
schemaVersion: 1
title: "Olympus EVIS X1 Endoscopic / OR Camera System - Network, DICOM, Recording, or Image Export Failure"
issueTitle: "Network, DICOM, Recording, or Image Export Failure"
description: "Troubleshoots missing network, DICOM, recording, or export functions caused by cabling, storage media, destinations, configuration, or infrastructure availability."
assetType: "Endoscopic / OR Camera System"
manufacturer: "Olympus"
model: "EVIS X1"
slug: "olympus-evis-x1-network-dicom-recording-or-image-export-failure"
dateAdded: "2026-09-11"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported EVIS X1 images could be captured locally but would not transfer to the configured destination."
  cause: "Clinical Engineering found the network cable at the processor had a damaged retaining tab and was intermittently losing physical link."
  resolution: "Replaced the network cable and verified image capture, transfer, and receipt at the intended destination."
helpfulDetails:
  - "Exact network or DICOM message."
  - "Local capture result."
  - "Recording function status."
  - "Network link indicator."
  - "Cable and wall-port tested."
  - "Approved destination selected."
  - "Known-good port or cable result."
  - "Removable media condition."
  - "Whether other devices reached the same destination."
  - "Confirmation of destination receipt."
  - "Final device status."
---

## What This Guide Helps With

Troubleshoots missing network, DICOM, recording, or export functions caused by cabling, storage media, destinations, configuration, or infrastructure availability.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Clinical Workflow

Determine whether the failure affects only documentation or whether it also affects active visualization.

Do not interrupt a procedure solely to troubleshoot nonessential export functions if clinical visualization remains reliable. If required images cannot be preserved, notify the clinical team and follow the facility's alternate documentation workflow.

**Expected outcome:** Patient care and required documentation continue through an approved alternate method while troubleshooting proceeds.

### 2. Identify the Failed Function

Determine whether the problem involves:

- Network connectivity.
- DICOM communication.
- Worklist retrieval.
- Recording.
- Still-image capture.
- USB or external media export.
- Transfer to PACS or another destination.

Record the exact error or status message.

**Expected outcome:** The problem is localized to a specific workflow instead of being treated as a general connectivity failure.

### 3. Confirm Local Image Capture or Recording

If possible, determine whether the system can create an image or recording locally before testing network transfer.

**Expected outcome:** Successful local capture separates acquisition problems from network/export problems.

### 4. Inspect Physical Network Connections

Check the Ethernet cable, wall jack, patch connection, and accessible network interface for loose connections or physical damage.

Where appropriate, substitute a known-good network cable.

**Expected outcome:** The physical connection is secure and a known-good cable does not change the problem, or the failed cable is identified and replaced.

### 5. Check Network Link Status

Verify the system and connected network equipment show expected physical link status where indicators are available.

Do not change network addresses or infrastructure configuration without authorization.

**Expected outcome:** A physical network link is present. If link is absent, isolate the cable, port, or infrastructure path before changing device configuration.

### 6. Verify Destination and Workflow Configuration

Compare user-accessible network, DICOM, export, or recording selections to the facility's known working configuration.

Confirm the correct destination, server, recording device, or export media is selected.

Do not alter undocumented network or DICOM parameters merely to test possibilities.

**Expected outcome:** The device is pointed to the intended destination using the approved configuration.

### 7. Test the Infrastructure Independently

If available, determine whether other systems on the same network segment can reach the same PACS, DICOM destination, or recording infrastructure.

Coordinate with IT or PACS support when the problem extends beyond the device.

**Expected outcome:** The failure is isolated to the EVIS X1 or identified as a broader network/server problem.

### 8. Check External Recording or Storage Media

For local recording or export failure, inspect removable media or external recording devices for:

- Proper connection.
- Recognition.
- Available capacity.
- Physical damage.
- Compatibility.
- Write protection where applicable.

Use only approved media.

**Expected outcome:** The recording or storage destination is available and writable, or the external media is identified as the cause.

### 9. Compare With a Known-Good Port or Destination

When authorized, test the device using a known-good approved network port, cable, recording device, or destination.

**Expected outcome:** The problem follows the device or remains with the infrastructure path, allowing proper escalation.

### 10. Perform Final Workflow Verification

Verify the complete required workflow:

- Image acquisition.
- Recording or capture.
- Patient or study association where applicable.
- Transfer or export.
- Receipt at the intended destination.

Do not consider a successful send alone sufficient if destination receipt is required.

**Expected outcome:** The complete image or recording path works end to end. If confirmed, troubleshooting can stop.

### 11. Escalate Unresolved Connectivity or Export Problems

If physical connections, media, local recording, settings, and infrastructure checks do not identify the cause, stop changing configuration and escalate appropriately.

**Expected outcome:** The issue is referred to Olympus service, IT, PACS, networking, or application support according to the isolated failure domain.

## If the Problem Persists

Common external cable, network-port, destination, media, recording accessory, and user-accessible configuration causes have been ruled out. Remaining possibilities may involve network infrastructure, server availability, DICOM configuration, software, security controls, internal network hardware, or another service-level condition.

The affected equipment should be handled according to clinical impact. If required clinical documentation cannot be safely completed, it should be:

- Removed from service or restricted from the affected workflow.
- Labeled appropriately.
- Sent for repair or bench evaluation when device-related.
- Evaluated using appropriate Olympus documentation and approved test equipment.
- Configured only by qualified personnel with appropriate network or DICOM authorization.

Verify the full communication path before return to unrestricted clinical use.

## Clinical Use Tip

A transfer is not fully verified until the intended receiving system confirms the correct study or image arrived under the correct patient context.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Separate acquisition, recording, network, and destination problems logically, verify the entire communication path before assuming internal failure, and involve IT or application support when the evidence points beyond the device.

That is successful troubleshooting.
