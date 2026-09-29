---
schemaVersion: 1
title: "GE Healthcare NM/CT 870 CZT PET / CT System - DICOM, PACS, or Worklist Transfer Fails"
issueTitle: "DICOM, PACS, or Worklist Transfer Fails"
description: "Studies, DICOM transfers, PACS communication, or modality worklist fail because of network, destination, connection, data, or interface conditions."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "NM/CT 870 CZT"
slug: "ge-healthcare-nm-ct-870-czt-dicom-pacs-or-worklist-transfer-fails"
dateAdded: "2026-09-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported NM/CT 870 CZT studies would not transfer to PACS after acquisition."
  cause: "Clinical Engineering found the scanner's external network cable was loose and the workstation had no active network link."
  resolution: "Clinical Engineering secured the network connection, verified restored link status and successful DICOM transfer to PACS, and returned the system to normal workflow."
helpfulDetails:
  - "Worklist, PACS, or export function affected"
  - "Exact transfer message"
  - "One or all destinations affected"
  - "Network link status"
  - "Cable condition"
  - "Destination selected"
  - "Patient or study data issue"
  - "Known PACS or network outage"
  - "Test transfer result"
  - "Confirmed receipt at destination"
---
## What This Guide Helps With

Studies, DICOM transfers, PACS communication, or modality worklist fail because of network, destination, connection, data, or interface conditions.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow and Patient Identification

If worklist or transfer functions are unavailable, follow the facility-approved downtime workflow. Prevent duplicate patient records, incorrect patient selection, or undocumented images.

Do not alter network or DICOM configuration while an active clinical study depends on the system.

**Expected outcome:** Imaging can continue only through an approved workflow without creating patient-identification or data-integrity risk.

### 2. Define the Exact Communication Failure

Determine whether the problem affects modality worklist, DICOM send, PACS query, image transfer, all destinations, or one specific destination.

Record the exact message and identify whether the failure occurs before acquisition, after acquisition, or during export.

**Expected outcome:** The affected interface and direction of communication are clearly identified.

### 3. Verify Local System Network Connectivity

Inspect the accessible network cable and link indicators. Confirm the workstation shows normal network availability through approved methods.

Do not change network settings simply because communication fails.

**Expected outcome:** The local physical network connection is present. If reconnecting a loose cable restores communication, verify transfer and troubleshooting can stop.

### 4. Determine Whether Other Network Functions Work

Check whether the system can reach other configured clinical destinations or services using normal approved functions.

If all network functions fail, suspect a local connection or infrastructure issue. If only one destination fails, the problem may be destination-specific.

**Expected outcome:** The scope of the network issue is narrowed.

### 5. Verify the Correct Destination Is Selected

Confirm staff are sending to the intended normal DICOM destination or using the expected worklist source.

Review operator-visible destination names without modifying protected network or DICOM parameters.

**Expected outcome:** The intended destination is selected and the failure is not caused by sending to the wrong configured target.

### 6. Check Patient and Study Data

Review required patient and study information for obvious missing, malformed, duplicate, or mismatched data that could interfere with workflow.

Do not alter clinical records merely to force transfer.

**Expected outcome:** Study information is suitable for normal DICOM workflow or a data-entry problem is identified.

### 7. Verify Whether the Destination Is Available

Coordinate with PACS, network, imaging informatics, or IS staff to determine whether the PACS, RIS, worklist server, interface engine, or network service is experiencing an outage.

**Expected outcome:** A downstream infrastructure outage is either identified or ruled out.

### 8. Perform an Approved Test Transfer

Once any external issue is corrected, send an appropriate test or completed study through the normal approved workflow.

Confirm receipt at the intended destination rather than relying only on a local “sent” status.

**Expected outcome:** The study transfers successfully and is available at the destination. If confirmed, troubleshooting can stop.

### 9. Verify End-to-End Workflow

For worklist problems, confirm a valid order appears at the modality. For PACS problems, confirm images arrive and are associated correctly. For export problems, verify the full intended path.

**Expected outcome:** The complete communication workflow functions from source to destination.

### 10. Escalate Persistent Interface Failure

If physical connectivity, destination selection, study data, and infrastructure availability are normal but communication remains unsuccessful, escalate to qualified system, PACS, or network support.

Do not independently change IP addresses, subnet masks, gateways, DICOM AE configuration, ports, firewall rules, or VLAN assignments without authorization.

**Expected outcome:** Configuration or infrastructure-level problems are handled by personnel responsible for those systems.

## If the Problem Persists

Common external causes involving physical network connection, destination selection, patient data, and known infrastructure outages have been ruled out. Remaining categories may include DICOM configuration, interface services, network routing, firewall policy, PACS/RIS availability, application services, or system software.

The device should be:

- Removed from the affected network workflow or clinical use when safe data handling cannot be assured.
- Labeled Out of Service when the system cannot be used safely.
- Sent for repair or system/network evaluation as appropriate.
- Evaluated using appropriate GE Healthcare and facility network documentation.
- Configured or repaired only by qualified personnel.

Complete end-to-end communication verification before normal workflow resumes. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Verify the complete path to the receiving system; a successful local send command does not prove the study reached PACS correctly.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect patient-data integrity, isolate the failure to the correct part of the communication path, verify physical and workflow causes before changing configuration, and document successful end-to-end verification.

That is successful troubleshooting.
