---
schemaVersion: 1
title: "GE Healthcare Discovery MI PET / CT System - DICOM, PACS, or Worklist Transfer Fails"
issueTitle: "DICOM, PACS, or Worklist Transfer Fails"
description: "Troubleshoots worklist and image-transfer failures caused by connectivity, destination availability, patient data, queue status, network infrastructure, or configuration."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "Discovery MI"
slug: "ge-healthcare-discovery-mi-dicom-pacs-or-worklist-transfer-fails"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "PET / CT staff reported that completed Discovery MI studies remained in the send queue and were not appearing in PACS."
  cause: "Clinical Engineering found that the scanner's accessible network connection had been disconnected during nearby equipment work."
  resolution: "Clinical Engineering restored the network connection, verified queued studies transmitted successfully to PACS, confirmed receipt with imaging staff, and returned the system to normal workflow."
helpfulDetails:
  - "Worklist or image transfer affected"
  - "One or all destinations affected"
  - "Exact message"
  - "Queue status"
  - "Local study availability"
  - "Network connection condition"
  - "Other modalities affected"
  - "PACS or server status"
  - "Patient information reviewed"
  - "Transfer test result"
  - "Final destination confirmation"
---
## What This Guide Helps With
Troubleshoots worklist and image-transfer failures caused by connectivity, destination availability, patient data, queue status, network infrastructure, or configuration.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Imaging Data

A DICOM or PACS failure may not require stopping acquisition immediately if local imaging remains reliable, but do not delete studies, recreate examinations unnecessarily, or repeat scans because images have not transferred.

Follow department downtime procedures when required.

**Expected outcome:** Patient imaging data are preserved and no unnecessary repeat exposure or acquisition occurs.

### 2. Identify Which Function Is Failing

Determine whether the issue involves:

- Modality worklist
- Sending images to PACS
- Sending to one destination only
- Sending to all destinations
- Receiving acknowledgments
- Query/retrieve functions
- A single study or all studies

Record any message or queue status.

**Expected outcome:** The affected DICOM workflow is clearly identified.

### 3. Confirm Local Scanner Operation

Verify that the Discovery MI can:

- Access the patient study locally
- Display acquired images
- Reconstruct images as expected
- Store the study locally
- Navigate the workstation normally

**Expected outcome:** Local acquisition and storage either function normally or reveal that the issue is broader than DICOM transfer.

### 4. Check External Network Connectivity

Inspect accessible network connections for:

- Loose cables
- Damaged connectors
- Disconnected network interfaces
- Recently moved equipment
- Loss of normal link indication

Check whether other networked imaging equipment is experiencing similar problems.

**Expected outcome:** Physical network connectivity is intact or an external network problem is identified.

### 5. Verify Destination Availability

Coordinate with PACS, IT, or imaging informatics staff to determine whether the destination service is available.

Check for known:

- PACS downtime
- Worklist server outage
- Interface-engine problems
- Network maintenance
- Storage-system outage

**Expected outcome:** The remote destination is confirmed available or the infrastructure outage is identified.

If the destination is unavailable, do not make unnecessary scanner configuration changes. Follow downtime procedures.

### 6. Verify Patient and Study Information

Review the affected examination for obvious demographic or workflow problems such as incomplete patient identification or an examination that was manually created differently from normal workflow.

Do not alter patient identifiers merely to force transmission.

**Expected outcome:** Patient and study information are complete and consistent with department workflow.

### 7. Review the Transfer Queue or Status

Use normal operator-accessible functions to determine whether images are:

- Pending
- Failed
- Repeatedly retrying
- Sent successfully
- Waiting on a specific destination

Avoid deleting queued studies unless the data have been safely preserved and department procedures specifically permit it.

**Expected outcome:** The transfer status identifies whether the scanner is attempting communication and where the process stops.

### 8. Compare With Another Study or Destination

When appropriate and without exposing a patient, determine whether:

- Another existing study transfers
- Another configured destination receives data
- Worklist fails while image send succeeds
- Only one destination is affected

**Expected outcome:** The issue is narrowed to the scanner, a particular DICOM service, or broader infrastructure.

### 9. Perform an Approved Restart if Appropriate

If local policy permits and patient data are protected, restart the affected workstation or communication function using approved procedures.

Do not alter DICOM network parameters without authorization and verified configuration information.

**Expected outcome:** Network services reconnect and the expected DICOM workflow resumes.

### 10. Verify End-to-End Transfer

Confirm the complete workflow:

- Worklist populates when applicable
- Correct patient can be selected
- Images transmit
- The destination receives the study
- Study identifiers are correct
- No unresolved queue failure remains

**Expected outcome:** The full DICOM, PACS, or worklist path operates normally.

If the complete path is verified, troubleshooting can stop.

## If the Problem Persists

If physical connections, local operation, destination availability, patient information, queue status, and approved restart procedures have been checked but DICOM communication still fails, the remaining cause may involve network infrastructure, server services, DICOM configuration, interface routing, workstation software, firewall or security controls, or another service-level condition.

The system should be:

- Removed from affected network workflow as appropriate
- Labeled Out of Service if safe clinical operation or data integrity cannot be assured
- Sent for repair or formal system evaluation when scanner-side failure is suspected
- Evaluated using appropriate GE Healthcare documentation and approved network tools
- Reconfigured only by qualified and authorized personnel

Coordinate with PACS, IT, and imaging informatics as needed.

After correction, verify the complete transfer path before restoring normal workflow.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Never repeat a PET or CT acquisition simply because images failed to reach PACS; verify that the original study is preserved and troubleshoot the communication path first.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Treat DICOM failures as an end-to-end communication problem. Preserve patient data, confirm local operation, verify physical network connectivity, remote services, study information, and queue status, and involve IT or PACS support when the fault is outside the scanner.

That is successful troubleshooting.
