---
schemaVersion: 1
title: "Varian TrueBeam Radiation Therapy System - DICOM, PACS, or Worklist Transfer Fails"
issueTitle: "DICOM, PACS, or Worklist Transfer Fails"
description: "The TrueBeam cannot receive expected worklist information or send imaging and related DICOM data to configured clinical systems."
assetType: "Radiation Therapy System"
manufacturer: "Varian"
model: "TrueBeam"
slug: "varian-truebeam-dicom-pacs-or-worklist-transfer-fails"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that TrueBeam images were not transferring to the configured clinical destination."
  cause: "Clinical Engineering found the external network cable at the workstation disconnected from the active network port."
  resolution: "Clinical Engineering restored the network connection and verified successful end-to-end DICOM transfer to the intended destination."
helpfulDetails:
  - "Worklist, DICOM, or PACS function affected"
  - "Sending and receiving system"
  - "One patient versus all studies affected"
  - "Exact communication message"
  - "Network link status"
  - "Cable and port checked"
  - "Broader network outage status"
  - "Destination-system status"
  - "Test transfer result"
  - "Confirmation at receiving system"
  - "Final interface status"
---
## What This Guide Helps With

The TrueBeam cannot receive expected worklist information or send imaging and related DICOM data to configured clinical systems.

## Step-by-Step Troubleshooting

### 1. Protect the Clinical Workflow
Do not proceed using incomplete, mismatched, or unverified patient data. Confirm patient identity and coordinate an alternate approved workflow with Radiation Oncology when data transfer is unavailable.

**Expected outcome:** No treatment proceeds using incorrect or unverified electronic patient information.

### 2. Identify the Failed Data Path
Determine whether the problem affects worklist retrieval, DICOM image transfer, PACS communication, or another configured destination. Record the affected destination and any displayed message.

**Expected outcome:** The direction and type of failed communication are known.

### 3. Confirm the Scope of the Problem
Determine whether one patient, one workstation, one destination, or all network transfers are affected. Check whether other connected clinical systems are experiencing similar problems.

**Expected outcome:** The problem is narrowed to local, destination-specific, or broader infrastructure communication.

### 4. Check Physical Network Connectivity
Inspect accessible Ethernet and network connections for loose connectors, physical damage, or recent relocation. Confirm expected link indicators where visible.

**Expected outcome:** The TrueBeam network connection is physically intact.

### 5. Verify Basic Network Availability
Using approved Clinical Engineering or IT methods, confirm that the relevant network path is available. Do not change addresses, VLANs, hostnames, or other network configuration without authorization.

**Expected outcome:** Basic connectivity is either confirmed or an infrastructure problem is identified for escalation.

### 6. Verify the Destination System
Confirm with PACS, oncology information system, or IT support that the intended destination is online and not experiencing an outage, maintenance event, or service interruption.

**Expected outcome:** The receiving or sending system is confirmed available.

### 7. Check User-Accessible Destination Selection
Verify that the correct configured destination or worklist source is selected. Compare against previously documented working configuration without changing restricted settings.

**Expected outcome:** The intended configured endpoint is being used.

### 8. Perform a Controlled Transfer Test
Use an approved test workflow to send or retrieve appropriate non-patient or authorized test data.

**Expected outcome:** Communication succeeds across the full path. If transfer is confirmed at the destination, troubleshooting can stop.

### 9. Escalate Persistent Communication Failure
If network connectivity is present but DICOM, PACS, or worklist transfer remains unavailable, stop changing configuration and coordinate escalation with qualified service and IT/PACS support.

**Expected outcome:** The communication failure is escalated without introducing unauthorized configuration changes.

## If the Problem Persists

External cabling, basic network availability, destination availability, and user-accessible destination selection have been ruled out. Remaining causes may involve network routing, VLAN configuration, firewall rules, DICOM configuration, application services, server availability, or TrueBeam communication software.

The device or affected interface should be:

- Removed from the affected clinical workflow when safe data exchange cannot be guaranteed
- Labeled Out of Service when the communication failure prevents safe system use
- Sent for appropriate service, PACS, oncology-IT, or network evaluation
- Evaluated using approved documentation and diagnostic tools
- Reconfigured only by authorized qualified personnel

Return to service requires successful end-to-end communication verification using the intended clinical destination.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Always verify receipt at the intended destination; a local “sent” indication alone does not prove that the complete DICOM path worked.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Communication failures should be isolated from the physical network outward. Verify cabling, infrastructure, destination availability, and the complete end-to-end transfer before changing configuration, and escalate appropriately when the failure moves beyond external troubleshooting.

That is successful troubleshooting.
