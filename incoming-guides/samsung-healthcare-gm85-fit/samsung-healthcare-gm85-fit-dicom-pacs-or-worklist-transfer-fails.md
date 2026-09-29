---
schemaVersion: 1
title: "Samsung Healthcare GM85 Fit Mobile X-Ray System - DICOM, PACS, or Worklist Transfer Fails"
issueTitle: "DICOM, PACS, or Worklist Transfer Fails"
description: "Addresses failed worklist retrieval or image transfer caused by network connection, destination availability, configuration, selection, or infrastructure problems."
assetType: "Mobile X-Ray System"
manufacturer: "Samsung Healthcare"
model: "GM85 Fit"
slug: "samsung-healthcare-gm85-fit-dicom-pacs-or-worklist-transfer-fails"
dateAdded: "2026-09-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported that the GM85 Fit acquired images normally but could not send studies to PACS."
  cause: "Clinical Engineering found the Ethernet cable disconnected from the assigned network connection."
  resolution: "Clinical Engineering restored the network connection, resent the queued study, and verified successful receipt at the PACS destination."
helpfulDetails:
  - "Whether worklist, PACS transfer, or both failed"
  - "Exact communication message"
  - "Wired or wireless connection"
  - "Network link indication"
  - "Wall port or connection used"
  - "Whether other devices were affected"
  - "Destination selected"
  - "Number of queued studies"
  - "IT or PACS findings"
  - "End-to-end transfer result"
---
## What This Guide Helps With

Addresses failed worklist retrieval or image transfer caused by network connection, destination availability, configuration, selection, or infrastructure problems.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow and Patient Identification
Do not allow a network problem to result in incorrect patient selection or study association.

Use the facility-approved downtime workflow when worklist or PACS connectivity is unavailable.

Expected outcome: Patient identification and imaging continuity are maintained safely despite the communication failure.

### 2. Confirm Which Function Is Failing
Determine whether the problem affects modality worklist, image transfer to PACS, DICOM storage confirmation, query functions, or all network communication.

Record any displayed message and whether previously acquired images remain stored locally.

Expected outcome: The failed service is clearly identified.

### 3. Check Physical Network Connection
Inspect the Ethernet cable, connector, and wall connection if the system is using wired networking. If wireless networking is used, verify that the system indicates an expected connection without changing protected configuration.

Expected outcome: The basic network connection is physically present and stable. If restoring a disconnected cable resolves communication, verify transfer and stop troubleshooting.

### 4. Compare With Other Network Functions
Determine whether the GM85 Fit can communicate with any configured network destination or whether all network functions are unavailable.

Where practical, compare with another device in the same clinical area to determine whether an infrastructure outage may be present.

Expected outcome: The failure is narrowed to the mobile X-ray system, a specific destination, or the broader hospital network.

### 5. Verify the Intended Destination
Using normal operator-accessible information, confirm staff are attempting to send to the expected PACS or retrieve from the intended worklist source.

Do not edit AE titles, IP addresses, ports, or other protected DICOM parameters without authorization.

Expected outcome: The correct destination is selected.

### 6. Check for Pending or Unsent Studies
Review the normal study or transfer status interface for queued, failed, or pending exams.

Do not delete unsent patient studies as a troubleshooting shortcut.

Expected outcome: Stored studies remain identifiable and available for transfer once communication is restored.

### 7. Coordinate Infrastructure Verification
If physical connectivity appears normal but communication remains unavailable, coordinate with hospital IT, PACS, or network support to verify destination availability, network path, VLAN access, and related infrastructure.

Provide the device identification and observed symptoms without independently changing enterprise network settings.

Expected outcome: Infrastructure is either confirmed functional or a network-side issue is identified.

### 8. Retry the Transfer or Worklist Query
Once connectivity is restored or an external issue is corrected, retry the failed communication using normal system functions.

Expected outcome: Worklist data is retrieved or images transfer successfully with expected acknowledgment.

### 9. Verify End-to-End Clinical Communication
Confirm not only that the system reports a successful send, but that the intended study appears correctly at the receiving PACS or other destination when verification is available.

Expected outcome: The complete communication path is functional. Troubleshooting can stop.

## If the Problem Persists

If physical connectivity, destination selection, local transfer status, and infrastructure availability have been verified, common external causes have been ruled out.

Possible remaining categories include DICOM configuration, system network interface, workstation software, storage services, security policies, or enterprise network configuration.

The system should be:

- Removed from service when required communication cannot be supported safely by an approved downtime workflow.
- Labeled Out of Service when appropriate.
- Sent for repair or bench evaluation if a device-side failure is suspected.
- Evaluated using appropriate Samsung Healthcare documentation and approved network diagnostic methods.
- Configured only by qualified and authorized personnel.

Preserve unsent patient studies and coordinate with PACS or IT before making configuration changes. Verify end-to-end transfer before clinical release.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A successful local image does not confirm successful documentation; verify the study reaches the intended PACS destination when communication has been repaired.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

DICOM troubleshooting should preserve patient identification and study data, verify the physical and infrastructure path before changing configuration, and confirm successful receipt at the destination before closing the work order.

That is successful troubleshooting.
