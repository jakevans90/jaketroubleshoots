---
schemaVersion: 1
title: "GE Healthcare AMX Navigate Mobile X-Ray System - Worklist, DICOM Send, or Wireless Network Transfer Fails"
issueTitle: "Worklist, DICOM Send, or Wireless Network Transfer Fails"
description: "Worklist retrieval, image transfer, DICOM communication, or wireless connectivity fails while local imaging functions may remain available."
assetType: "Mobile X-Ray System"
manufacturer: "GE Healthcare"
model: "AMX Navigate"
slug: "ge-healthcare-amx-navigate-worklist-dicom-send-or-wireless-network-transfer-fails"
dateAdded: "2026-11-18"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported the AMX Navigate could acquire images but could not send studies to PACS from one clinical area."
  cause: "Clinical Engineering confirmed local imaging was normal and found the communication failure occurred only in that location, while transfers succeeded in a known-good wireless area."
  resolution: "Coordinated the location-specific wireless issue with IT and verified successful DICOM image transfer to PACS after network service was restored."
helpfulDetails:
  - "Exact network or DICOM message"
  - "Worklist versus image-send failure"
  - "Wireless status"
  - "Room or location"
  - "Time of failure"
  - "Destination affected"
  - "Whether other devices were affected"
  - "Transfer-queue condition"
  - "Known-good location result"
  - "IT/PACS findings"
  - "Successful receipt verification"
  - "Final device status"
---

## What This Guide Helps With

Worklist retrieval, image transfer, DICOM communication, or wireless connectivity fails while local imaging functions may remain available.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow
Determine whether imaging can safely continue using the facility's approved downtime or alternate workflow. Do not make unauthorized network changes to restore connectivity.

Expected outcome: Patient imaging and documentation continue safely while connectivity is evaluated.

### 2. Define the Exact Communication Failure
Determine whether the problem affects:
- Worklist retrieval
- DICOM image send
- Both send and receive functions
- Wireless connection
- One destination only
- All network destinations
- One room or location
- The entire hospital area

Record any displayed network or transfer message exactly.

Expected outcome: The affected portion of the communication path is identified.

### 3. Verify Local Imaging Operation
Confirm the AMX Navigate starts normally and can acquire and locally display an image using an approved test workflow.

Expected outcome: Local imaging operation is separated from the network-transfer problem.

### 4. Check Wireless Status
Verify the system indicates connection to the expected facility wireless environment. Compare operation in a known-good coverage area if practical.

Do not alter SSIDs, security settings, IP parameters, or protected network configuration without authorization.

Expected outcome: The system shows a normal network connection or the failure is confirmed to be location-related.

### 5. Compare With Other Devices
Determine whether other imaging devices in the same area are also experiencing worklist or DICOM problems.

Expected outcome: A broader outage suggests infrastructure rather than an isolated AMX Navigate problem.

### 6. Verify the Destination
Confirm the intended PACS, worklist, archive, or other configured destination is the one selected. If multiple approved destinations exist, compare behavior without changing protected configuration.

Expected outcome: The communication attempt is being sent to the intended destination.

### 7. Review Queue or Transfer Status
Check normal user-accessible transfer status for pending, failed, or retrying studies. Do not delete unsent patient data simply to clear a queue unless facility procedure specifically authorizes it.

Expected outcome: The system's transfer state is understood and patient data is preserved.

### 8. Test in a Known-Good Network Location
If the failure appears wireless and the unit can be moved safely, test network operation in a location where the AMX Navigate previously communicated normally.

Expected outcome: Location-dependent success points toward wireless coverage or infrastructure rather than the imaging system itself.

### 9. Coordinate With IT or PACS Support
Provide:
- Device identity
- Location
- Time of failure
- Affected service
- Destination
- Whether other systems are affected
- Relevant network status indications

Clinical Engineering should not make individual network configuration changes outside approved responsibility.

Expected outcome: Infrastructure and destination availability can be checked without altering the device unnecessarily.

### 10. Verify End-to-End Transfer
After corrective action, confirm:
- Worklist retrieval if applicable
- Successful test image transmission using approved workflow
- Receipt at the intended destination
- No remaining failed transfer condition

Expected outcome: The complete communication path works normally. Troubleshooting can stop.

### 11. Escalate Persistent Isolated Communication Failure
If the network and destination are verified good but this AMX Navigate remains unable to communicate, escalate for system-level evaluation.

Expected outcome: The device is not assumed repaired based only on a wireless indicator; actual DICOM functionality is verified.

## If the Problem Persists

Common external and infrastructure causes have been ruled out. Remaining possibilities may involve system network hardware, application configuration, software services, security/certificate configuration, DICOM configuration, or other service-level issues.

The system should be removed from clinical network-dependent use if reliable workflow cannot be maintained, labeled appropriately when necessary, and evaluated using approved GE Healthcare and facility network procedures.

Any repair or configuration change should be performed only by qualified personnel with appropriate IT/PACS coordination.

Return-to-service verification should confirm the full path from worklist or acquisition through successful receipt at the intended destination.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A wireless icon alone does not prove PACS connectivity; verify the complete worklist and image-transfer path.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Separate local imaging, wireless connectivity, hospital infrastructure, and DICOM destination problems before changing the device. End-to-end verification and clear coordination with IT or PACS support are essential.

That is successful troubleshooting.
