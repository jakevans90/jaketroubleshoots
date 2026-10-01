---
schemaVersion: 1
title: "Elekta Versa HD Radiation Therapy System - DICOM, PACS, or Worklist Transfer Fails"
issueTitle: "DICOM, PACS, or Worklist Transfer Fails"
description: "Patient, image, or worklist data does not transfer correctly because of network connectivity, destination availability, identifiers, interface configuration, or infrastructure problems."
assetType: "Radiation Therapy System"
manufacturer: "Elekta"
model: "Versa HD"
slug: "elekta-versa-hd-dicom-pacs-or-worklist-transfer-fails"
dateAdded: "2026-10-01"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that Versa HD imaging studies would not transfer to the configured destination."
  cause: "Clinical Engineering found the external network cable at the affected workstation was disconnected."
  resolution: "Clinical Engineering restored the network connection, repeated the transfer, and verified successful receipt of the correct study at the destination system."
helpfulDetails:
  - "Transfer type affected"
  - "Source and destination systems"
  - "Exact error message"
  - "Network link status"
  - "Cable condition"
  - "Whether other destinations work"
  - "Whether other devices can reach the destination"
  - "Patient or study information checked"
  - "IT or PACS findings"
  - "Transfer verification after correction"
  - "Final system status"
---
## What This Guide Helps With

Patient, image, or worklist data does not transfer correctly because of network connectivity, destination availability, identifiers, interface configuration, or infrastructure problems.

## Step-by-Step Troubleshooting

### 1. Protect the Clinical Workflow

Do not proceed with treatment using uncertain patient identification, incomplete transferred data, or an unverified workaround.

Follow departmental procedures for any downtime workflow.

**Expected outcome:** Patient identification and treatment data integrity remain protected during troubleshooting.

### 2. Define the Failed Transaction

Determine whether the failure involves DICOM image transfer, PACS communication, modality worklist retrieval, patient data exchange, or another network transaction.

Record the source, intended destination, and exact failure behavior.

**Expected outcome:** The specific data path being tested is clearly identified.

### 3. Verify Local Network Connectivity

Check the Versa HD workstation or applicable interface for normal network connection and visible link indications.

Inspect accessible network cables and patch connections for damage or disconnection.

**Expected outcome:** The local network connection is physically intact.

### 4. Determine Whether Other Network Functions Work

Check whether the affected workstation can communicate with other normally available systems or whether multiple network functions are unavailable.

**Expected outcome:** The problem is localized to one destination or identified as a broader network outage.

### 5. Verify Destination Availability

Determine whether PACS, worklist, oncology information, or other destination systems are operational and accessible to other clinical devices.

Coordinate with IT or the responsible application team when necessary.

**Expected outcome:** The receiving system is confirmed available or an external infrastructure outage is identified.

### 6. Verify Patient and Study Information

Check that the intended patient, study, and workflow information is selected correctly and that the failure is not caused by an obvious mismatch or incomplete entry.

Do not modify clinical identifiers simply to force a transfer.

**Expected outcome:** The transaction is being attempted with the intended patient and study information.

### 7. Review Visible Communication Configuration

Verify only authorized, visible configuration information such as intended destination selection or normal user-accessible network targets.

Do not alter protected network, DICOM, or service configuration without authorization.

**Expected outcome:** The expected destination is selected and no obvious user-level configuration error is present.

### 8. Retry a Controlled Transfer

After correcting any external connectivity or destination issue, retry an appropriate nonclinical or authorized transaction.

**Expected outcome:** The data transfers successfully to the intended system.

### 9. Confirm End-to-End Receipt

Verify at the receiving system that the correct data arrived completely and is associated with the intended patient or test record.

**Expected outcome:** End-to-end communication is confirmed. Troubleshooting can stop once transfer and data integrity are verified.

### 10. Escalate Persistent Interface Failure

If the transfer still fails after physical network, destination availability, patient information, and approved configuration checks, stop troubleshooting.

**Expected outcome:** The issue is escalated to the appropriate Elekta, IT, PACS, oncology information system, or network support resource.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may include DICOM configuration, interface services, server routing, network policy, application services, certificates, database functions, or other service-level communication problems.

The Versa HD should be:

- Removed from affected clinical workflow if safe data transfer cannot be assured.
- Labeled Out of Service when the communication failure prevents safe treatment.
- Evaluated using appropriate Elekta and institutional IT documentation.
- Configured or repaired only by qualified personnel.
- Verified end to end before return to normal clinical workflow.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Confirm data at the receiving endpoint, not just a successful send indication at the Versa HD workstation.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Trace communication failures from the physical connection through the network and receiving application before changing configuration. Protect patient-data integrity, confirm end-to-end receipt, and escalate when infrastructure or service-level support is required.

That is successful troubleshooting.
