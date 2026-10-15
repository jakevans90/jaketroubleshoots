---
schemaVersion: 1
title: "GE Healthcare CardioLab Electrophysiology Recording System - DICOM, PACS, or Worklist Transfer Fails"
issueTitle: "DICOM, PACS, or Worklist Transfer Fails"
description: "CardioLab cannot receive worklist data or transfer supported study information because of network, destination, patient-data, configuration, or infrastructure problems."
assetType: "Electrophysiology Recording System"
manufacturer: "GE Healthcare"
model: "CardioLab"
slug: "ge-healthcare-cardiolab-dicom-pacs-or-worklist-transfer-fails"
dateAdded: "2026-10-15"
taxonomyMode: "reuse"
ccr:
  complaint: "EP staff reported that CardioLab could not retrieve the scheduled patient from the worklist."
  cause: "Clinical Engineering found the workstation Ethernet cable disconnected from the wall network connection."
  resolution: "The cable was reconnected, network communication was restored, the correct worklist entry was received, and CardioLab was returned to service."
helpfulDetails:
  - "Worklist, send, or receive function affected"
  - "Exact destination involved"
  - "Exact displayed message"
  - "Patient or study context"
  - "Ethernet and link status"
  - "Whether other systems were affected"
  - "Destinations tested"
  - "Infrastructure ticket or outage information"
  - "Transfer results before correction"
  - "Receiving-system confirmation"
  - "Final communication status"
---

## What This Guide Helps With

CardioLab cannot receive worklist data or transfer supported study information because of network, destination, patient-data, configuration, or infrastructure problems.

## Step-by-Step Troubleshooting

### 1. Protect the Clinical Workflow

Confirm clinicians have a safe approved method to continue the procedure if worklist or data transfer is unavailable.

Do not create duplicate or incorrect patient records simply to bypass a connectivity problem.

**Expected outcome:** Patient identification and procedural continuity are maintained while communication is investigated.

### 2. Confirm the Exact Transfer Failure

Determine whether CardioLab cannot receive a worklist, cannot send supported data, sends to one destination but not another, or appears to transfer while data never arrives.

Record any visible message and the affected destination.

**Expected outcome:** The failed communication direction and endpoint are clearly identified.

### 3. Verify Patient and Study Information

Confirm the correct patient, identifier, study, and procedure context are selected before transfer.

Look for obvious incomplete or mismatched information that could cause downstream rejection, but do not alter patient information without clinical authorization.

**Expected outcome:** The intended record is correctly identified and ready for transfer.

If correcting an authorized demographic or workflow error resolves transfer, verify receipt and stop troubleshooting.

### 4. Inspect the Physical Network Connection

Check the CardioLab workstation Ethernet cable, wall jack, dock, or other approved network connection for looseness or damage.

Observe link indicators where available.

**Expected outcome:** The workstation has a stable physical network connection.

If restoring the physical connection resolves communication, confirm successful transfer and stop troubleshooting.

### 5. Check Scope of the Network Problem

Determine whether other CardioLab functions, nearby systems, or other clinical devices are experiencing network or worklist problems.

Contact IT, PACS, integration, or interface support if the outage appears broader than the workstation.

**Expected outcome:** The failure is localized to CardioLab or identified as an infrastructure issue.

If infrastructure service is restored and CardioLab resumes normal transfers, verify and stop troubleshooting.

### 6. Verify Configured Destination Without Unauthorized Changes

Review permitted user-visible destination or connection information and confirm the intended destination is selected.

Do not change IP addresses, AE titles, ports, VLANs, DNS, firewall rules, or protected DICOM configuration unless authorized and working from approved documentation.

**Expected outcome:** CardioLab is attempting communication with the intended configured endpoint.

### 7. Compare Another Transfer or Destination When Appropriate

If the workflow permits, test another approved patient-independent connection, worklist request, or destination to determine whether the problem follows CardioLab or one remote endpoint.

Protect PHI and follow institutional data-handling requirements.

**Expected outcome:** The failure is isolated to the workstation, a specific destination, or the wider infrastructure.

If one remote destination is proven unavailable while CardioLab communicates normally elsewhere, escalate to the responsible destination owner rather than altering CardioLab unnecessarily.

### 8. Verify End-to-End Transfer

After correcting any external issue, confirm that CardioLab sends or receives the required information and that the destination actually receives the expected record.

Do not consider a local “sent” indication sufficient when downstream receipt is part of the complaint.

**Expected outcome:** The complete transfer path functions successfully.

If the correct study or worklist information is confirmed at the receiving endpoint, troubleshooting is complete.

### 9. Escalate Unresolved Connectivity

If physical networking is intact and the correct destination is selected but DICOM, PACS, or worklist communication still fails, escalate to the appropriate GE Healthcare, IT, PACS, or integration support team.

Avoid unauthorized configuration changes that may create additional connectivity problems.

**Expected outcome:** The unresolved interface problem is routed to the team responsible for the affected layer.

## If the Problem Persists

Common physical-network, patient-data, workflow, and destination-selection causes have been ruled out. Remaining possibilities may involve managed network configuration, interface engines, PACS or worklist services, CardioLab software, destination configuration, authentication, or other service-level infrastructure.

The CardioLab system should be:

- Removed from service if the connectivity failure prevents safe required clinical operation.
- Labeled Out of Service when appropriate.
- Sent for repair or bench evaluation if a local equipment fault is suspected.
- Evaluated using appropriate GE Healthcare and institutional network documentation.
- Repaired or configured only by qualified personnel.

Complete end-to-end communication verification before return to normal use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Confirm the complete information path, not just the CardioLab workstation; a successful local send does not prove the intended downstream system received the record.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Treat CardioLab data-transfer failures as an end-to-end communication problem. Verify patient context, physical networking, scope of the outage, and destination behavior before changing configuration, then document both the correction and confirmed downstream result.

That is successful troubleshooting.
