---
schemaVersion: 1
title: "Canon Aquilion ONE / PRISM Edition CT Scanner - DICOM, PACS, or Worklist Transfer Fails"
issueTitle: "DICOM, PACS, or Worklist Transfer Fails"
description: "Addresses failed DICOM, PACS, or worklist communication caused by network, destination, interface, workflow, or infrastructure problems."
assetType: "CT Scanner"
manufacturer: "Canon"
model: "Aquilion ONE / PRISM Edition"
slug: "canon-aquilion-one-prism-edition-dicom-pacs-or-worklist-transfer-fails"
dateAdded: "2026-09-24"
taxonomyMode: "reuse"
ccr:
  complaint: "CT staff reported completed studies would not transfer to PACS."
  cause: "Clinical Engineering found the CT workstation had lost physical network connectivity at the approved wall connection."
  resolution: "Restored the network connection, transmitted an approved test study, and confirmed the images were received and viewable in PACS."
helpfulDetails:
  - "Interface affected."
  - "Exact communication message."
  - "PACS or worklist destination."
  - "Network link status."
  - "Cable and wall-jack condition."
  - "Whether other modalities were affected."
  - "Recent switch, VLAN, firewall, or PACS work."
  - "Test-study results."
  - "Confirmation at receiving system."
  - "Final clinical workflow status."
---
## What This Guide Helps With

Addresses failed DICOM, PACS, or worklist communication caused by network, destination, interface, workflow, or infrastructure problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification and Image Availability
Do not bypass normal patient-identification or image-transfer processes in a way that risks misidentification or loss of diagnostic data.

Use approved downtime workflows when PACS or worklist services are unavailable.

**Expected outcome:** Patient identification and diagnostic image availability remain controlled.

### 2. Confirm Which Interface Is Failing
Determine whether the problem affects modality worklist, image transmission to PACS, query/retrieve, multiple destinations, or one specific destination.

Record any displayed communication message exactly.

**Expected outcome:** The failed communication path is identified.

### 3. Verify Local CT Operation
Confirm the CT scanner can operate locally and that the workstation is responsive.

**Expected outcome:** The issue is isolated to data communication rather than a general scanner failure.

### 4. Check Physical Network Connectivity
Inspect accessible network cables, wall jacks, patch connections, and link indicators where available.

Do not move the scanner to a different network port without confirming the approved network configuration.

**Expected outcome:** Physical network connectivity appears intact.

If restoring an approved external cable connection resolves communication, proceed to final verification.

### 5. Determine Whether the Problem Affects Other Systems
Check whether nearby modalities or clinical systems can reach the same PACS, RIS, or worklist infrastructure.

Coordinate with IT or imaging informatics when appropriate.

**Expected outcome:** The fault is narrowed to the CT scanner, one network segment, or enterprise infrastructure.

### 6. Verify Destination and Workflow Selection
Confirm staff are selecting the intended destination, worklist source, and patient workflow.

Do not change DICOM nodes, IP parameters, AE titles, ports, or restricted configuration unless authorized and verified against approved records.

**Expected outcome:** The failure is not caused by an incorrect normal workflow selection.

### 7. Review Recent Network or Configuration Changes
Determine whether the failure began after switch work, VLAN changes, firewall updates, PACS maintenance, server replacement, software updates, or scanner service.

**Expected outcome:** Relevant infrastructure changes are identified for escalation.

### 8. Use an Approved Test Study or Communication Test
When appropriate, use an approved non-patient or designated test record to verify worklist retrieval or image transmission.

Protect patient data and avoid creating unnecessary duplicate records.

**Expected outcome:** The affected communication path succeeds or fails reproducibly.

### 9. Confirm End-to-End Transfer
If communication is restored, confirm the study reaches the intended PACS or destination and is visible where expected.

For worklist problems, confirm expected patient/exam information populates correctly.

**Expected outcome:** The full communication path works, not merely the local send command.

If achieved, troubleshooting is complete.

### 10. Escalate Unresolved DICOM or Network Failure
If the problem persists, escalate to qualified Canon service, PACS, imaging informatics, or IT personnel as appropriate.

Do not make undocumented network or DICOM configuration changes.

**Expected outcome:** Persistent communication faults are handled through controlled infrastructure troubleshooting.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may include CT DICOM services, network configuration, VLAN routing, firewall rules, PACS/RIS availability, interface engines, server configuration, or service-level software issues.

The CT scanner should be:

- Removed from service only if the communication failure prevents safe clinical workflow and no approved downtime process exists.
- Labeled Out of Service when required.
- Evaluated using appropriate Canon, PACS, and network documentation.
- Tested with approved diagnostic tools.
- Configured only by qualified Clinical Engineering, imaging informatics, IT, or vendor personnel.

Verify the complete worklist and image-transfer path before closing the work order.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A successful local send does not prove success; confirm the study is actually available at the intended receiving system.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Trace DICOM problems end to end, verify physical connectivity before configuration, involve the correct infrastructure team, and document successful receipt rather than only successful transmission.

That is successful troubleshooting.
