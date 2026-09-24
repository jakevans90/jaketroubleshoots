---
schemaVersion: 1
title: "Siemens Healthineers SOMATOM X.cite CT Scanner - DICOM, PACS, or Worklist Transfer Fails"
issueTitle: "DICOM, PACS, or Worklist Transfer Fails"
description: "Use this guide when worklists do not populate or CT studies cannot transfer reliably to PACS or another configured DICOM destination."
assetType: "CT Scanner"
manufacturer: "Siemens Healthineers"
model: "SOMATOM X.cite"
slug: "siemens-healthineers-somatom-xcite-dicom-pacs-or-worklist-transfer-fails"
dateAdded: "2026-09-24"
taxonomyMode: "reuse"
ccr:
  complaint: "CT staff reported that the SOMATOM X.cite could not retrieve the modality worklist."
  cause: "Clinical Engineering found the scanner's accessible network cable was disconnected at the workstation network connection."
  resolution: "The cable was reconnected, the worklist populated normally, and DICOM image transfer to the configured destination was verified."
helpfulDetails:
  - "Failed DICOM function"
  - "Exact displayed communication message"
  - "Worklist or PACS destination affected"
  - "Network link status"
  - "Cable condition"
  - "Whether other modalities were affected"
  - "Study queue status"
  - "IT/PACS findings"
  - "Results after retry or restart"
  - "Final worklist and transfer verification"
---
## What This Guide Helps With

Use this guide when worklists do not populate or CT studies cannot transfer reliably to PACS or another configured DICOM destination.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification and Image Availability
Do not create duplicate or incorrectly identified examinations while troubleshooting connectivity. Confirm an alternate workflow with clinical and imaging staff if electronic transfer is unavailable.  
**Expected outcome:** Patient identification remains accurate and clinically necessary images remain accessible through an approved contingency workflow.

### 2. Identify Which Communication Function Failed
Determine whether the issue affects modality worklist, image transfer, query/retrieve, one PACS destination, or all network communication. Record the exact displayed status or message.  
**Expected outcome:** The affected DICOM function and destination are identified.

### 3. Verify Local Scanner Network Connectivity
Inspect the accessible network cable and connection. Confirm normal network link indication where available and check for visible cable damage.  
**Expected outcome:** The scanner has an intact physical network connection.

### 4. Determine Whether the Problem Is Local or Department-Wide
Check whether other modalities or workstations can access the same worklist or PACS destination. Coordinate with IT, PACS, or imaging informatics staff as appropriate.  
**Expected outcome:** The failure is isolated to the SOMATOM X.cite or identified as a broader infrastructure problem.

### 5. Verify the Intended Destination and Workflow
Confirm the operator is using the expected configured worklist source or DICOM destination. Do not change AE titles, IP addresses, ports, or protected configuration values without authorization.  
**Expected outcome:** The correct existing destination is selected and no obvious workflow error is present.

### 6. Check Study and Queue Status
Review the normal operator interface for studies waiting, failed, or pending transfer. Confirm sufficient patient and study information is present for the intended workflow.  
**Expected outcome:** Failed transfers or worklist requests are clearly identified without altering protected system configuration.

### 7. Retry After Infrastructure Confirmation
If IT or PACS support confirms the destination is available and the local connection is intact, retry the normal worklist request or image transfer using the standard workflow.  
**Expected outcome:** Communication succeeds. If it does, verify the complete path and stop troubleshooting.

### 8. Perform an Approved Restart if Appropriate
If only the CT system remains affected and no active patient workflow depends on it, perform an approved normal restart and retest communication.  
**Expected outcome:** Worklist and/or DICOM transfer returns to normal operation.

### 9. Escalate Persistent Communication Failure
If the CT remains unable to communicate despite confirmed network availability and correct normal workflow, escalate jointly to Siemens Healthineers service and the appropriate IT/PACS team.  
**Expected outcome:** The scanner is not relied upon for normal electronic workflow until communication is restored and verified.

## If the Problem Persists

Physical connectivity, destination selection, general network availability, and normal workflow have been checked. Remaining causes may involve DICOM configuration, modality networking, PACS services, firewall or routing changes, integration configuration, scanner software, or another service-level issue.

The scanner should be:

- Removed from normal network-dependent workflow when appropriate
- Labeled Out of Service if the communication failure prevents safe or reliable clinical use
- Evaluated by qualified Clinical Engineering, IT/PACS, and Siemens Healthineers personnel as appropriate
- Evaluated using approved documentation and network diagnostic tools
- Configured only by authorized personnel

Before full return to service, confirm worklist retrieval, correct patient information, study transfer, and image availability at the intended receiving system. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Verify the entire communication path through the receiving PACS or worklist system, not just that the CT reports a transfer as initiated.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect patient identity and image availability, isolate physical connectivity and infrastructure issues before changing configuration, verify the receiving system, and document the complete communication path after correction.

That is successful troubleshooting.
