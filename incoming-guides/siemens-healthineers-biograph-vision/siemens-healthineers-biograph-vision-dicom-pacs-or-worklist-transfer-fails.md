---
schemaVersion: 1
title: "Siemens Healthineers Biograph Vision PET / CT System - DICOM, PACS, or Worklist Transfer Fails"
issueTitle: "DICOM, PACS, or Worklist Transfer Fails"
description: "Use this guide when worklist retrieval, DICOM transfer, or PACS communication fails because of network, destination, interface, or accessible configuration conditions."
assetType: "PET / CT System"
manufacturer: "Siemens Healthineers"
model: "Biograph Vision"
slug: "siemens-healthineers-biograph-vision-dicom-pacs-or-worklist-transfer-fails"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that completed Biograph Vision studies would not transfer to PACS."
  cause: "Clinical Engineering found the workstation's accessible network cable loose at the wall connection."
  resolution: "Clinical Engineering secured the network connection, successfully transferred a representative study, confirmed PACS receipt, and returned the communication workflow to service."
helpfulDetails:
  - "Worklist, PACS, or other DICOM function affected"
  - "Destination affected"
  - "Exact error message"
  - "Local study availability"
  - "Network link status"
  - "Cable and wall-port condition"
  - "Whether other modalities were affected"
  - "Recent network maintenance"
  - "Transfer retry result"
  - "Confirmation of destination receipt"
---
## What This Guide Helps With

Use this guide when worklist retrieval, DICOM transfer, or PACS communication fails because of network, destination, interface, or accessible configuration conditions.

## Step-by-Step Troubleshooting

### 1. Preserve the Study and Maintain Clinical Workflow

Do not delete, recreate, or repeatedly manipulate patient studies solely to troubleshoot a communication problem.

Confirm that completed image data remains available locally and arrange an alternate approved workflow for urgent studies when necessary.

**Expected outcome:** Patient data is protected and clinical continuity is maintained.

### 2. Identify Which Communication Function Failed

Determine whether the issue affects:

- Modality worklist.
- Image transmission to PACS.
- One destination only.
- All DICOM destinations.
- Query/retrieve functions.
- Completed studies or only new studies.

Record any exact transfer or communication message.

**Expected outcome:** The failed communication path is clearly identified.

### 3. Confirm Local System Operation

Verify that the Biograph Vision workstation is otherwise operating normally and that studies can be accessed locally.

A local workstation or acquisition failure should be resolved before treating the issue as a network problem.

**Expected outcome:** Local scanner operation and study access are normal.

### 4. Inspect Accessible Network Connections

Check the scanner or workstation's accessible network cabling for:

- Loose connectors.
- Damaged patch cables.
- Disconnected wall ports.
- Recently moved equipment.
- Abnormal link indicators where normally visible.

Do not move the system to another port or network segment without authorization.

**Expected outcome:** Physical network connectivity appears intact.

If correcting an obvious external connection restores transfers, verify all required communication paths and stop.

### 5. Determine the Scope of the Network Problem

Check whether:

- Other imaging modalities can reach PACS.
- Other systems can retrieve worklists.
- The affected destination is generally available.
- The issue began after planned network or server maintenance.

Coordinate with IT, PACS, or interface support when the problem is broader than the scanner.

**Expected outcome:** The failure is localized to the Biograph Vision, a specific destination, or shared infrastructure.

### 6. Verify Normal Operator-Accessible Destination Selection

Confirm that staff are using the intended configured destination and workflow.

Do not alter IP addresses, ports, AE Titles, routing, or protected network parameters unless specifically authorized and supported by approved documentation.

**Expected outcome:** The intended existing communication destination is selected.

If an incorrect normal destination selection caused the failure, correct the selection, verify transfer, and stop.

### 7. Retry One Representative Transfer

Once physical connectivity and destination availability are verified, retry one representative non-duplicative study transfer or approved test transaction.

Avoid repeatedly sending large batches before confirming that the communication path is functioning.

**Expected outcome:** The study transfers and is acknowledged by the intended destination.

If the transfer succeeds, verify receipt and stop.

### 8. Verify the Complete Communication Path

Confirm both sides of the workflow when possible:

- Worklist entries arrive at the scanner.
- Images leave the scanner.
- PACS receives the images.
- The correct patient and study information is preserved.

A local “sent” indication alone should not be treated as proof of end-to-end success when confirmation is available.

**Expected outcome:** The intended end-to-end DICOM workflow functions correctly.

### 9. Perform Final Functional Verification

Verify all communication functions relevant to the reported problem, such as:

- Worklist retrieval.
- Study transfer.
- Destination receipt.
- Appropriate status display.
- No unintended duplicate or misrouted study.

**Expected outcome:** The required DICOM communication path operates normally.

If all checks pass, troubleshooting is complete.

### 10. Escalate Persistent Communication Failure

If physical connectivity, destination availability, and normal workflow selection are correct but communication still fails, escalate to appropriate PACS, network, interface, or Siemens Healthineers support.

**Expected outcome:** The unresolved communication issue is routed to the team responsible for the remaining infrastructure or service-level fault.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve network infrastructure, routing, DICOM services, PACS availability, interface engines, protected scanner network configuration, workstation software, or server-side conditions.

The device should be:

- Removed from affected clinical workflow when required communication cannot be reliably completed.
- Labeled **Out of Service** if the communication failure makes normal clinical use unsafe or impractical.
- Evaluated using appropriate Siemens Healthineers and institutional network documentation.
- Configured or repaired only by qualified personnel.
- Retested through the complete communication path before return to normal workflow.

Do not make undocumented network changes in an attempt to restore connectivity.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Confirm that urgent completed studies actually arrive at the receiving PACS; a scanner-side transfer attempt does not guarantee end-to-end delivery.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect patient data, verify the physical network and end-to-end workflow before changing configuration, involve infrastructure teams when appropriate, and document exactly where communication failed and how it was verified afterward.

That is successful troubleshooting.
