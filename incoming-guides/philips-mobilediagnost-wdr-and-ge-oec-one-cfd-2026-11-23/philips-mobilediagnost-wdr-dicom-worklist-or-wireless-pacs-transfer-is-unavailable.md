---
schemaVersion: 1
title: "Philips MobileDiagnost wDR Mobile X-Ray System - DICOM Worklist or Wireless PACS Transfer Is Unavailable"
issueTitle: "DICOM Worklist or Wireless PACS Transfer Is Unavailable"
description: "Troubleshoots wireless connectivity, worklist retrieval, PACS transfer, destination, network, and workflow issues before assuming an internal imaging-system failure."
assetType: "Mobile X-Ray System"
manufacturer: "Philips"
model: "MobileDiagnost wDR"
slug: "philips-mobilediagnost-wdr-dicom-worklist-or-wireless-pacs-transfer-is-unavailable"
dateAdded: "2026-11-23"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported that the MobileDiagnost wDR could acquire images but could not retrieve the DICOM worklist or send studies over wireless."
  cause: "Clinical Engineering confirmed normal local imaging and found the problem was limited to a hospital wireless coverage area where other devices were also disconnected."
  resolution: "Clinical Engineering coordinated with network support, verified restored wireless connectivity, then confirmed worklist retrieval and successful PACS image transfer."
helpfulDetails:
  - "Worklist status"
  - "Wireless connection indication"
  - "Location of failure"
  - "Whether other systems were affected"
  - "Queue status"
  - "Destination affected"
  - "Local image-acquisition status"
  - "Results after restart"
  - "Network or PACS support involvement"
  - "Final end-to-end transfer result"
---

## What This Guide Helps With

Troubleshoots wireless connectivity, worklist retrieval, PACS transfer, destination, network, and workflow issues before assuming an internal imaging-system failure.

## Step-by-Step Troubleshooting

### 1. Protect Continuity of Imaging and Patient Identification
Do not allow a network problem to create incorrect patient identification or lost images.

Follow approved downtime procedures when worklist or PACS connectivity is unavailable, and verify patient information carefully.

Expected outcome: Imaging workflow continues safely without misidentification or loss of clinically required images.

### 2. Confirm the Exact Communication Failure
Determine whether:
- Worklist does not populate
- Wireless connection is unavailable
- Images remain queued
- One PACS destination fails
- All destinations fail
- Transfer succeeds only in certain locations

Record the exact visible status or message.

Expected outcome: The communication failure is narrowed to worklist, wireless connectivity, image transmission, or destination availability.

### 3. Verify Local System Operation
Confirm that the MobileDiagnost wDR boots normally, examinations can be opened, images can be acquired, and local functions operate normally.

Expected outcome: Imaging functions work locally. If local operation is also impaired, address the broader system problem before focusing on DICOM.

### 4. Check Wireless Status and Location
Verify through normal system indicators that wireless communication is enabled and connected as expected.

Move the unit, when practical, to a known area with established clinical wireless coverage and reassess.

Expected outcome: The mobile system connects normally in a known-good area. Location-specific failure suggests wireless infrastructure or coverage rather than a system-wide DICOM problem.

### 5. Check Whether the Problem Affects Other Devices
Determine whether other imaging devices in the same area are also unable to retrieve worklists or send images.

Coordinate with Radiology IT or network support when appropriate.

Expected outcome: A shared failure indicates likely infrastructure, PACS, worklist-server, or network service involvement.

### 6. Verify Normal DICOM Destination Selection
Confirm that the expected worklist source or image destination is selected through approved normal workflow.

Do not change IP addresses, AE titles, ports, routing, or service-level DICOM configuration without authorization.

Expected outcome: The correct configured destination is being used. If an incorrect normal destination selection caused the problem, correct it and verify communication.

### 7. Review the Image Queue
Check whether images are:
- Pending
- Failed
- Retrying
- Already transmitted

Retry transmission only through approved normal controls.

Expected outcome: Queued studies transmit successfully when connectivity returns. If all queued studies clear normally, verify the workflow and stop troubleshooting.

### 8. Restart Communication Through Normal Operation
When appropriate, perform a normal system restart and reassess wireless connection, worklist retrieval, and image transmission.

Do not perform unauthorized network resets or service configuration changes.

Expected outcome: Normal communication services restart and DICOM functions recover. If stable, proceed to final verification.

### 9. Perform End-to-End Verification
Verify:
- Wireless connection is established
- A worklist can be retrieved
- Correct patient information appears
- A test or approved clinical image can be sent
- The destination receives the image
- No study remains unexpectedly queued

Expected outcome: The complete communication path functions successfully. Troubleshooting can stop.

### 10. Escalate Persistent Communication Failures
If communication remains unavailable after external checks, coordinate with Radiology IT, PACS, network support, or Philips service as appropriate.

Expected outcome: Device, network, and server responsibilities are clearly separated and the fault is escalated to the correct support group.

## If the Problem Persists

Common external causes such as location, wireless availability, destination selection, local queue status, and shared infrastructure outages have been ruled out.

The remaining problem may involve system network hardware, wireless hardware, stored configuration, DICOM services, hospital networking, worklist services, PACS, routing, or cybersecurity controls.

The device should be:
- Removed from service when reliable patient identification or image delivery cannot be maintained
- Labeled Out of Service when appropriate
- Sent for repair or bench evaluation if the failure is device-specific
- Evaluated using appropriate Philips documentation and approved network test methods
- Repaired or configured only by qualified personnel

Verify the complete worklist and image-transfer path before return to normal service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A locally acquired image is not enough; confirm that the correct patient, study, and receiving destination are preserved through the entire communication path.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect patient identification and image availability first. Separate local imaging operation from wireless, worklist, PACS, and infrastructure functions before changing anything. Escalate network or server problems to the appropriate team and document the full communication-path verification.

That is successful troubleshooting.
