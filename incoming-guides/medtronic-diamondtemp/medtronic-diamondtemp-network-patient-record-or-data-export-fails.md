---
schemaVersion: 1
title: "Medtronic DiamondTemp Cardiac Ablation Generator - Network, Patient Record, or Data Export Fails"
issueTitle: "Network, Patient Record, or Data Export Fails"
description: "Use this guide when supported network communication, patient information handling, recording, or data export does not complete as expected."
assetType: "Cardiac Ablation Generator"
manufacturer: "Medtronic"
model: "DiamondTemp"
slug: "medtronic-diamondtemp-network-patient-record-or-data-export-fails"
dateAdded: "2026-10-16"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that procedure data from the DiamondTemp system would not transfer to the intended network destination."
  cause: "Clinical Engineering found the external network cable was disconnected from the system connection."
  resolution: "Clinical Engineering restored the network connection and verified successful transfer and receipt of the test record through the approved workflow."
helpfulDetails:
  - "Exact transfer or export problem"
  - "Displayed message"
  - "Patient record selected"
  - "Intended destination"
  - "Cable and link status"
  - "Network port tested"
  - "Approved configuration observed"
  - "Known-good cable or port result"
  - "Transfer and receipt confirmation"
  - "Final device status"
---

## What This Guide Helps With

Use this guide when supported network communication, patient information handling, recording, or data export does not complete as expected.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification and Preserve Clinical Data
Do not proceed with an incorrect patient association or assume data has been saved or transferred successfully. Follow the clinical workflow for preserving procedure information and correcting patient identification issues.

**Expected outcome:** Patient information remains correctly associated and important procedure data is not knowingly lost or misfiled.

### 2. Confirm the Exact Failure
Determine whether the problem involves network connection, patient record selection, data storage, external export, or transfer to another supported system. Record any displayed message and the affected destination.

**Expected outcome:** The failure is isolated to a specific part of the data path.

### 3. Verify Local System Operation
Confirm the generator is otherwise operating normally and that the issue is not part of a broader freeze, restart, or startup failure.

**Expected outcome:** The data problem is separated from a general system malfunction.

### 4. Inspect External Data and Network Connections
Check accessible Ethernet, USB, approved removable media, or other supported external data connections involved in the workflow. Inspect for loose connections, cable damage, or incorrect port use.

**Expected outcome:** The physical connection is secure and undamaged. Correcting a loose cable should restore the link where applicable.

### 5. Check Link and Infrastructure Availability
Where applicable, verify normal link indication and confirm the connected network port or destination is operational through approved hospital IT or Clinical Engineering methods.

**Expected outcome:** The infrastructure needed for communication is available, or the issue is identified outside the generator.

### 6. Verify Patient and Destination Selection
Confirm the intended patient record and supported export destination are selected correctly before retransmission. Do not create duplicate records simply to test connectivity.

**Expected outcome:** The correct patient and destination are selected without creating documentation conflicts.

### 7. Verify User-Accessible Network Configuration
Compare accessible network settings against the approved configuration record. Do not change addresses, security settings, interface parameters, or protected configuration without authorization from the responsible support team.

**Expected outcome:** The generator matches its documented approved network configuration.

### 8. Test With a Known-Good External Path
When practical, compare the suspect network cable, port, destination, removable media, or supported external interface against a known-good equivalent.

**Expected outcome:** The fault is isolated to the generator, cable, network infrastructure, destination system, or export medium.

### 9. Retry the Supported Transfer
After correcting an external issue, retry the approved transfer or export and confirm receipt at the intended destination.

**Expected outcome:** The correct data arrives successfully and can be associated with the intended patient or procedure. The issue is resolved and troubleshooting can stop.

### 10. Escalate Persistent Communication or Export Failure
If physical connections and infrastructure are functional but the generator still cannot communicate or export, preserve available data and escalate.

**Expected outcome:** The device or integration path receives appropriate Clinical Engineering, IT, cybersecurity, or manufacturer evaluation.

## If the Problem Persists

External cables, ports, destination availability, and approved configuration checks have been completed. Remaining possibilities include network infrastructure, interface configuration, software, storage, security controls, internal communication hardware, or service-level integration problems.

If the failure affects required clinical documentation or safe workflow, remove the generator from service and label it **Out of Service** until evaluated. Coordinate with appropriate Clinical Engineering, IT, integration, or manufacturer support. Use approved documentation and avoid unauthorized network or software configuration changes.

Before return to service, verify correct patient association, data storage, transfer, and receipt at the intended destination. Knowing when the fault extends beyond the device is proper troubleshooting.

## Clinical Use Tip

Confirm the complete data path and patient association; a successful local save does not prove the receiving system obtained the correct record.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect patient information and procedural data first, verify the physical and infrastructure path before changing configuration, confirm receipt rather than assuming transfer succeeded, escalate integration faults appropriately, and document the verified data path.

That is successful troubleshooting.
