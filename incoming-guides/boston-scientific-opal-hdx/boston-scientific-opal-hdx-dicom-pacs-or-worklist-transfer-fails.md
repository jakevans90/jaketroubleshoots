---
schemaVersion: 1
title: "Boston Scientific OPAL HDx Electrophysiology Mapping System - DICOM, PACS, or Worklist Transfer Fails"
issueTitle: "DICOM, PACS, or Worklist Transfer Fails"
description: "Troubleshoots supported networked study, worklist, or export functions by checking network connectivity, destination availability, patient data, configuration, and infrastructure."
assetType: "Electrophysiology Mapping System"
manufacturer: "Boston Scientific"
model: "OPAL HDx"
slug: "boston-scientific-opal-hdx-dicom-pacs-or-worklist-transfer-fails"
dateAdded: "2026-10-15"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the OPAL HDx could not transfer supported study information to the configured network destination."
  cause: "Clinical Engineering found the system's external network cable disconnected at the wall connection."
  resolution: "Clinical Engineering restored the network connection and verified successful end-to-end transfer and receipt at the configured destination."
helpfulDetails:
  - "Exact transfer or worklist function"
  - "Exact error message"
  - "Destination system"
  - "Network cable condition"
  - "Link indication"
  - "Whether other network functions work"
  - "Whether other devices are affected"
  - "Patient or study record involved"
  - "IT or integration team findings"
  - "Transfer and receipt verification"
---

## What This Guide Helps With

Troubleshoots supported networked study, worklist, or export functions by checking network connectivity, destination availability, patient data, configuration, and infrastructure.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Separate Clinical Operation From Data Transfer

Do not interrupt active mapping or patient monitoring solely to troubleshoot a noncritical network transfer unless the failure affects safe clinical operation.

Determine whether the study can continue safely while data-transfer troubleshooting is deferred.

**Expected outcome:** Patient care remains uninterrupted while the transfer problem is assessed.

### 2. Confirm Which Network Function Actually Failed

Determine whether the reported problem involves:

- Patient or procedure worklist
- Study transfer
- Archive or server communication
- Another supported network export
- A separate workstation or integration system

Confirm that the requested DICOM, PACS, or worklist function is actually configured and supported in the local OPAL HDx installation.

**Expected outcome:** The exact network service and destination are identified.

### 3. Record the Exact Failure

Capture:

- Exact message
- Time of failure
- Destination involved
- Whether all studies fail or only one
- Whether the problem affects all patients
- Whether transfer previously worked that day

**Expected outcome:** The problem can be correlated with device or infrastructure behavior.

### 4. Check Physical Network Connectivity

Inspect the accessible network cable and connection.

Check for:

- Loose cable
- Damaged latch or connector
- No link indication where visible
- Cable disconnected during equipment movement

Use a known-good approved network cable when appropriate.

**Expected outcome:** Physical network connectivity is intact. If replacing or reconnecting the cable restores transfer, troubleshooting can stop after verification.

### 5. Verify Other Network Functions

Determine whether other supported network functions from the system are working.

If every networked function has failed, suspect the local connection or infrastructure before assuming an application-specific problem.

**Expected outcome:** The fault is narrowed to the entire network path or one specific service.

### 6. Verify Patient and Study Information

Check that required patient or study fields used by the local workflow are populated correctly.

Do not alter clinical identifiers merely to force a transfer.

If only one study fails, compare it with a study that transfers normally.

**Expected outcome:** Required data is present and no obvious record-specific issue explains the failure.

### 7. Check Destination Availability

Coordinate with PACS, imaging informatics, clinical IT, or the appropriate system owner to determine whether the destination server or worklist service is available.

Check whether other devices are experiencing similar failures.

**Expected outcome:** A hospital infrastructure outage is either identified or ruled out.

### 8. Verify Approved Network Configuration

Review visible configuration information only if authorized.

Compare with documented local configuration rather than changing:

- Network addressing
- Destination entries
- Application endpoints
- Other integration settings

Do not make undocumented configuration changes.

**Expected outcome:** Existing configuration matches the approved site setup or discrepancies are escalated to the appropriate support team.

### 9. Retry the Transfer and Verify Receipt

After correcting an external connection or after infrastructure service is restored, retry the affected workflow.

Confirm not only that the system reports success but that the intended receiving system actually receives the expected information.

**Expected outcome:** Transfer completes end to end. Troubleshooting can stop.

### 10. Escalate Persistent Integration Failure

If local connectivity, patient data, destination availability, and approved configuration appear correct but the transfer still fails, escalate jointly to qualified system support and the appropriate IT or integration team.

**Expected outcome:** The unresolved network or application issue is routed to the correct service owner.

## If the Problem Persists

Common external cable, data-entry, destination, and infrastructure causes have been ruled out. The remaining problem may involve application configuration, network services, server-side interfaces, software, cybersecurity controls, or another integration-level issue.

The affected system should be:

- Removed from service if the failed function prevents safe clinical use
- Labeled Out of Service when appropriate
- Sent for repair or bench evaluation if device-side malfunction is suspected
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Verify the complete communication path and successful receipt at the destination before closing the work order.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A successful send indication is not enough—verify that the intended receiving system actually received the patient or study information.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Network transfer problems require end-to-end troubleshooting. Verify the physical connection, record data, destination, and infrastructure before changing configuration or assuming device failure. Escalate across system boundaries appropriately and document actual transfer verification.

That is successful troubleshooting.
