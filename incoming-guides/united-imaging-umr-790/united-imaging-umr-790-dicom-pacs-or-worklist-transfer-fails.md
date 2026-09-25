---
schemaVersion: 1
title: "United Imaging uMR 790 MRI System - DICOM, PACS, or Worklist Transfer Fails"
issueTitle: "DICOM, PACS, or Worklist Transfer Fails"
description: "Troubleshoots failed worklist retrieval, DICOM transfer, and PACS communication caused by network connectivity, destination availability, workflow selection, or external infrastructure."
assetType: "MRI System"
manufacturer: "United Imaging"
model: "uMR 790"
slug: "united-imaging-umr-790-dicom-pacs-or-worklist-transfer-fails"
dateAdded: "2026-09-25"
taxonomyMode: "reuse"
ccr:
  complaint: "MRI staff reported that completed uMR 790 studies would not transfer to PACS."
  cause: "Clinical Engineering found the MRI workstation network cable had been disconnected during nearby equipment movement."
  resolution: "The network connection was restored, a completed study transferred successfully, and receipt at PACS was confirmed."
helpfulDetails:
  - "Function affected"
  - "Exact communication error"
  - "Worklist versus image-transfer status"
  - "Physical network connection"
  - "Whether other modalities are affected"
  - "Destination involved"
  - "Study-specific or system-wide behavior"
  - "PACS/IT findings"
  - "Successful transfer verification"
  - "Final workflow status"
---
## What This Guide Helps With

Troubleshoots failed worklist retrieval, DICOM transfer, and PACS communication caused by network connectivity, destination availability, workflow selection, or external infrastructure.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow and Prevent Data Loss
Do not delete, overwrite, or repeatedly recreate studies while troubleshooting communication problems.

Ensure completed imaging data remains safely stored locally until successful transfer is confirmed.

**Expected outcome:** Patient imaging data is preserved while communication is investigated.

### 2. Identify Which Network Function Has Failed
Determine whether the problem involves:
- Modality worklist
- PACS image transfer
- DICOM destination
- One destination or all destinations
- One study or all studies
- Intermittent communication

Record the exact displayed message when available.

**Expected outcome:** The failed communication path is clearly defined.

### 3. Verify Local MRI Network Connectivity
Check accessible network cables, link indicators if present, and workstation connectivity.

Confirm no cable has been disconnected or damaged during equipment movement or room work.

**Expected outcome:** The MRI workstation has an intact physical network connection. If restoring the external connection resolves communication, verify transfer and stop.

### 4. Determine Whether Other Systems Are Affected
Check with clinical staff or IT whether PACS, worklist, or network issues are occurring on other modalities.

A broad outage should be treated as an infrastructure problem rather than an MRI hardware failure.

**Expected outcome:** The problem is classified as local or enterprise-wide.

### 5. Verify the Correct Destination or Workflow Is Selected
Using normal operator functions, confirm the intended DICOM destination, worklist source, or send workflow is being used.

Do not modify protected network addresses, ports, or DICOM configuration without authorization.

**Expected outcome:** The correct configured destination is selected. If workflow selection was incorrect, complete a transfer test and stop.

### 6. Test Another Study or Normal Network Function
When permitted, determine whether the failure affects:
- A single study
- All studies
- Worklist only
- Image transfer only

This helps separate study-specific problems from communication-path problems.

**Expected outcome:** The failure scope is narrowed without risking patient data.

### 7. Coordinate With PACS or IT Support
Confirm whether the destination system is online and accepting connections.

Provide:
- Scanner identification
- Time of failure
- Destination affected
- Error wording
- Whether other modalities are affected

**Expected outcome:** PACS or IT confirms whether the infrastructure side is available and correctly routing traffic.

### 8. Retry Transfer After the External Cause Is Corrected
Once network or destination availability is restored, resend an appropriate study using the normal workflow.

Do not create duplicate patient records unnecessarily.

**Expected outcome:** The study transfers successfully and is visible at the intended destination. Troubleshooting can stop.

### 9. Verify Worklist Operation
If worklist was affected, confirm new patient orders can be retrieved and matched through the standard workflow.

**Expected outcome:** Worklist communication operates normally and patient demographic workflow is restored.

### 10. Escalate Persistent Local Communication Failure
If network infrastructure is confirmed available and external connections are intact but the uMR 790 still cannot communicate, escalate the system.

**Expected outcome:** The scanner remains under controlled use or out of service as appropriate until configuration or service evaluation is completed.

## If the Problem Persists

Common external network and workflow causes have been ruled out. Remaining categories may include local network configuration, DICOM configuration, workstation software, interface services, system firewall rules, storage services, or other service-level communication problems.

The device should be:
- Removed from service when dependable image transfer or patient-data workflow cannot be assured
- Labeled **Out of Service** when clinical use is not safe or appropriate
- Sent for repair or service evaluation
- Evaluated using United Imaging documentation and approved network diagnostic tools
- Configured or repaired only by qualified Clinical Engineering, IT, PACS, or vendor personnel

Do not change network or DICOM parameters without approved values and change control.

Knowing when to stop external troubleshooting is proper troubleshooting. Confirm the complete path from modality to destination before return to normal workflow.

## Clinical Use Tip

Never assume a successful “send” means the images arrived; verify the study at the receiving PACS or intended destination when troubleshooting transfer failures.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

DICOM troubleshooting requires checking the complete communication path rather than assuming the scanner itself has failed. Preserve patient data, verify physical connectivity and infrastructure first, and confirm receipt at the destination before closing the work order.

That is successful troubleshooting.
