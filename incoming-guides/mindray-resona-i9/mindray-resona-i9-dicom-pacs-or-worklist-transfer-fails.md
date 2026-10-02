---
schemaVersion: 1
title: "Mindray Resona I9 Ultrasound System - DICOM, PACS, or Worklist Transfer Fails"
issueTitle: "DICOM, PACS, or Worklist Transfer Fails"
description: "Use when modality worklist, DICOM image transfer, PACS delivery, or communication with configured clinical destinations does not work."
assetType: "Ultrasound System"
manufacturer: "Mindray"
model: "Resona I9"
slug: "mindray-resona-i9-dicom-pacs-or-worklist-transfer-fails"
dateAdded: "2026-10-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported completed Resona I9 studies were not transferring to PACS."
  cause: "Clinical Engineering found the external network cable was loose at the ultrasound system and network communication was interrupted."
  resolution: "Clinical Engineering secured the network connection, transmitted a test study successfully, confirmed receipt with the PACS workflow, and returned the system to service."
helpfulDetails:
  - "Failed DICOM function"
  - "Destination affected"
  - "Exact message displayed"
  - "Time of failure"
  - "Network cable condition"
  - "Link indication"
  - "Whether other devices are affected"
  - "Whether one or all studies fail"
  - "Test transfer result"
  - "PACS or worklist receipt confirmation"
  - "IT or imaging-informatics ticket number"
  - "Final device status"
---
## What This Guide Helps With

Use when modality worklist, DICOM image transfer, PACS delivery, or communication with configured clinical destinations does not work.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification and Study Integrity
Do not bypass patient-identification safeguards to keep scanning. If worklist is unavailable, follow the facility-approved downtime workflow and verify patient information carefully before acquisition.

**Expected outcome:** Patient images remain associated with the correct patient and examination despite the communication problem.

### 2. Identify the Failed Function
Determine whether the problem involves worklist retrieval, sending completed images, communication with one destination, communication with all destinations, or confirmation of receipt. Record any displayed message and approximate time of failure.

**Expected outcome:** The communication failure is narrowed to a specific workflow and destination.

### 3. Verify Physical Network Connection
Inspect the Ethernet cable and accessible network connection for looseness or damage. Confirm normal link indication where applicable.

**Expected outcome:** The physical network connection is intact. If reseating an externally loose connection restores communication, continue with transfer verification.

### 4. Determine Whether the Network Problem Is Broader
Check whether other clinical devices in the same area can reach the relevant PACS, worklist, or network resources. Contact IT or imaging informatics when multiple devices are affected.

**Expected outcome:** The issue is identified as device-specific or a wider network/service outage.

### 5. Verify the Correct Destination Is Selected
Using normal operator-accessible functions, confirm that the intended configured DICOM or PACS destination is being used. Do not change AE titles, IP addresses, ports, or other protected network parameters without authorization and verified configuration information.

**Expected outcome:** The system is attempting to communicate with the intended configured destination.

### 6. Verify Patient and Study Workflow
Confirm the examination has been completed or placed in the appropriate state for the expected transfer and that the correct patient record is selected. Determine whether only one study is affected or all studies fail.

**Expected outcome:** A workflow-state problem is ruled out.

### 7. Retry a Controlled Test Transfer
Using an approved test or appropriate nonpatient workflow, retry communication to the configured destination. Observe whether the system reports successful transmission.

**Expected outcome:** The transfer completes successfully. If the receiving system also confirms receipt, troubleshooting can stop after final verification.

### 8. Check Receipt at the Destination
Coordinate with PACS, imaging informatics, or IT personnel to determine whether the images reached the destination but were delayed, rejected, misrouted, or not received.

**Expected outcome:** The communication path is localized to the modality, network, interface, or receiving system.

### 9. Perform a Controlled Restart if Appropriate
If the network path and destination services appear available but the Resona I9 remains unable to communicate, perform a normal system restart when clinical workflow permits.

**Expected outcome:** Network services initialize normally and communication resumes.

### 10. Perform Final End-to-End Verification
Verify worklist retrieval if applicable, correct patient selection, successful image transmission, and confirmed receipt at the intended destination.

**Expected outcome:** The complete communication path functions correctly. If successful, troubleshooting can stop.

## If the Problem Persists

Physical network connections, destination selection, study workflow, receiving-system availability, and controlled restart have been evaluated. A persistent failure may involve modality configuration, network addressing, DICOM services, interface infrastructure, PACS/worklist systems, firewall or routing changes, or ultrasound system software.

Remove the system from service only when the communication problem prevents safe clinical workflow or reliable study management and no approved downtime procedure is available. Otherwise, clearly communicate the limitation while coordinating escalation.

Use appropriate Mindray documentation and coordinate with imaging informatics or hospital IT. Protected network or DICOM configuration should be changed only by authorized qualified personnel using verified settings.

Before normal service is restored, perform an end-to-end test confirming both transmission and receipt.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A successful “send” indication on the ultrasound system is not enough when troubleshooting PACS issues; confirm the study reached the intended receiving system.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Preserve patient identification first, verify the physical network and complete communication path before changing configuration, involve IT or imaging informatics when appropriate, confirm actual receipt at the destination, and document the resolution clearly.

That is successful troubleshooting.
