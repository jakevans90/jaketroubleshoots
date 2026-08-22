---
schemaVersion: 1
title: "Philips Zenition Series C-Arm - DICOM Send, PACS, or Worklist Failure"
issueTitle: "DICOM Send, PACS, or Worklist Failure"
description: "Addresses imaging-network workflow failures caused by network connectivity, destination availability, patient data, configuration, ports, or infrastructure issues."
assetType: "C-Arm"
manufacturer: "Philips"
model: "Zenition Series"
slug: "philips-zenition-series-dicom-send-pacs-or-worklist-failure"
dateAdded: "2026-08-22"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology staff reported that the Philips Zenition Series could acquire images but could not send completed studies to PACS."
  cause: "Clinical Engineering found the Ethernet cable disconnected from the approved network wall port after the system had been relocated."
  resolution: "The network cable was reconnected, a test study was transmitted successfully, and correct receipt at the intended PACS destination was verified."
helpfulDetails:
  - "Whether worklist, DICOM send, or both failed."
  - "Exact visible communication message."
  - "Whether one or all studies were affected."
  - "Local imaging functionality."
  - "Ethernet cable and port condition."
  - "Network link indication."
  - "Whether other modalities are affected."
  - "Destination or worklist selected."
  - "Patient and study information status."
  - "Teams contacted."
  - "Test transaction result."
  - "Final PACS or worklist verification."
---
## What This Guide Helps With

Addresses imaging-network workflow failures caused by network connectivity, destination availability, patient data, configuration, ports, or infrastructure issues.

## Step-by-Step Troubleshooting

### 1. Protect the Clinical Workflow and Preserve Images

A DICOM or worklist problem may not prevent image acquisition but can affect patient identification, image availability, and interpretation. Confirm that images required for patient care are retained locally and that staff have an approved alternate workflow for patient identification, image transfer, or interpretation.

**Expected outcome:** Patient care and image preservation continue while network troubleshooting is performed.

### 2. Define the Exact Communication Failure

Determine whether the problem affects modality worklist, DICOM image send, PACS receipt, all network functions, or only one destination. Record any visible message and identify whether the failure affects one study or every study.

**Expected outcome:** The problem is narrowed to a specific network workflow.

### 3. Verify Local System Operation

Confirm the Zenition Series has completed startup and can acquire and review images locally. Verify the problem is not an overall system or mobile viewing station failure.

**Expected outcome:** The C-arm functions locally and the complaint is isolated to network communication.

### 4. Inspect the Physical Network Connection

Inspect the accessible Ethernet cable, network jack, connector latch, cable path, and any approved external network hardware. Look for loose cables, damage, pinching, or an unplugged connection.

If the system uses the facility's intended network connection, verify that the correct port is being used.

**Expected outcome:** The physical network connection is secure and undamaged.

If reconnecting a loose cable restores network communication, proceed to final verification.

### 5. Check Network Link Indications

Where normal user-accessible indicators are available, observe whether the network interface shows a link. Compare the wall port or connection with a known-good approved network device when facility policy permits.

Do not alter network infrastructure without appropriate authorization.

**Expected outcome:** A physical network link is present or an infrastructure problem is identified.

### 6. Verify Patient and Study Information

For worklist or send failures involving a single study, verify that required patient and study fields are present and correctly selected according to clinical workflow. Check for obviously incomplete or mismatched identifiers.

Do not alter patient data solely to force transmission.

**Expected outcome:** Required study information is complete and associated with the intended patient.

### 7. Verify Destination and Service Availability

Determine whether PACS, worklist, or other destination services are available to other modalities in the same area. Contact the appropriate PACS, network, or clinical applications team when necessary.

**Expected outcome:** The failure is identified as local to the C-arm or broader to the hospital infrastructure.

If multiple modalities are affected, escalate to the appropriate infrastructure team rather than changing the C-arm.

### 8. Review User-Accessible Network/DICOM Configuration

Verify observable configuration such as the intended destination or worklist selection against documented site configuration or a known-good equivalent system.

Do not change IP addressing, application entities, ports, or restricted DICOM parameters without authorization and approved documentation.

**Expected outcome:** The user-accessible configuration matches the intended clinical workflow.

### 9. Retry a Controlled Test Transaction

After correcting an identified external cause, perform an approved test worklist query or DICOM send. Verify the destination receives the correct study and that no unintended duplicate or incorrect patient record is created.

**Expected outcome:** The test transaction completes successfully through the intended destination.

If successful, troubleshooting can stop after final workflow confirmation.

### 10. Perform Final End-to-End Verification

Confirm the full workflow appropriate to the complaint: worklist retrieval, correct patient selection, local image acquisition, DICOM transmission, PACS receipt, and correct study association.

**Expected outcome:** The complete imaging communication path works correctly from the Zenition system to the intended clinical destination.

### 11. Escalate Persistent DICOM or Network Failure

If cabling, network link, patient information, destination availability, and approved configuration have been checked and communication remains unavailable, stop external troubleshooting.

**Expected outcome:** The unresolved issue is routed to the correct Philips, PACS, networking, or clinical-applications support path.

## If the Problem Persists

Common external network and workflow causes have been ruled out. The remaining issue may involve network infrastructure, VLAN or routing configuration, DICOM configuration, PACS/worklist services, application software, the system network interface, or another service-level condition.

The device should be:

- Removed from network-dependent clinical workflow when safe image transfer or patient association cannot be assured.
- Labeled Out of Service if the failure prevents safe intended use.
- Sent for qualified evaluation when the fault is local to the device.
- Evaluated using approved Philips documentation and institutional network/PACS procedures.
- Configured or repaired only by authorized qualified personnel.

Coordinate with PACS, networking, cybersecurity, or clinical applications teams as appropriate. After correction, perform complete end-to-end verification before normal use.

Knowing when to stop local troubleshooting and involve infrastructure teams is proper troubleshooting.

## Clinical Use Tip

Verify that the correct patient and study reached the receiving PACS, not merely that the system reported a successful send.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

DICOM troubleshooting should follow the complete communication path from the modality to the clinical destination. Verify physical connectivity, patient data, destination availability, and approved configuration before assuming a device fault, and document infrastructure escalation clearly.

That is successful troubleshooting.

