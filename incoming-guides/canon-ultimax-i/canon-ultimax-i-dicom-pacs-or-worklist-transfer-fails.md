---
schemaVersion: 1
title: "Canon Ultimax-i Fluoroscopy / Interventional System - DICOM, PACS, or Worklist Transfer Fails"
issueTitle: "DICOM, PACS, or Worklist Transfer Fails"
description: "Troubleshoots failed worklist retrieval or image transfer caused by network connectivity, destination availability, configuration, workflow, or infrastructure issues."
assetType: "Fluoroscopy / Interventional System"
manufacturer: "Canon"
model: "Ultimax-i"
slug: "canon-ultimax-i-dicom-pacs-or-worklist-transfer-fails"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that studies from the Canon Ultimax-i were not transferring to PACS."
  cause: "Clinical Engineering found the external network cable at the workstation not fully seated."
  resolution: "Clinical Engineering secured the connection and verified successful transfer and PACS receipt of a nonclinical test study."
helpfulDetails:
  - "Function affected: worklist, PACS, or both"
  - "Exact transfer message"
  - "One study or all studies affected"
  - "Network cable and link status"
  - "Other modalities affected"
  - "Recent network changes"
  - "Configuration observed"
  - "Destination availability"
  - "Test study result"
  - "Confirmation of receipt"
---
## What This Guide Helps With

Troubleshoots failed worklist retrieval or image transfer caused by network connectivity, destination availability, configuration, workflow, or infrastructure issues.

## Step-by-Step Troubleshooting

### 1. Maintain Clinical and Data Continuity
If network services fail during an active case, ensure images and study information are preserved locally when supported and follow departmental downtime procedures. Do not delete or repeatedly resend studies without understanding their status.

**Expected outcome:** Patient imaging data is protected while network troubleshooting is performed.

### 2. Confirm Which Function Is Failing
Determine whether the problem affects modality worklist retrieval, DICOM image transfer, PACS receipt, query/retrieve functions, or all network communication.

Record any displayed network or transfer message and whether the issue affects one study or every study.

**Expected outcome:** The specific failing communication path is identified.

### 3. Verify Local Network Connectivity
Check accessible network cables, connectors, and link indications where available. Look for loose, damaged, or recently moved connections.

Do not change network addresses or configuration simply to test connectivity.

**Expected outcome:** The physical network connection appears intact. If restoring an external connection resolves communication, verify transfers and stop.

### 4. Determine Whether the Issue Is Device-Specific
Check whether other imaging systems or workstations in the same area can access the affected PACS, worklist, or network service.

Coordinate with IT when appropriate.

**Expected outcome:** The problem is narrowed to the Ultimax-i or to a broader network/server outage.

### 5. Verify Normal Network Configuration
Review user-accessible or documented configuration information without changing values. Confirm that no recent approved network change, room move, server migration, or maintenance event could explain the failure.

Do not alter IP, destination, port, or DICOM parameters without authorization and known-good configuration information.

**Expected outcome:** The observed configuration is consistent with the expected environment or a discrepancy is identified for authorized correction.

### 6. Check Study and Workflow Information
For a single-study problem, verify that the study is complete enough for transfer and that required patient or examination information is present. Check whether the failure follows one specific record or all records.

**Expected outcome:** A workflow-specific issue is distinguished from a general network failure.

### 7. Test the Affected Communication Path
When appropriate, use an approved test study or nonclinical workflow to verify worklist retrieval or DICOM transfer. Confirm receipt at the intended destination rather than relying only on a local "sent" indication.

**Expected outcome:** The destination receives the expected data successfully. If confirmed, troubleshooting can stop.

### 8. Verify End-to-End Operation
Confirm the complete path from the Ultimax-i through the network to the intended worklist or PACS destination. Verify that new communication remains reliable.

**Expected outcome:** Worklist and/or image transfer functions normally end to end. If successful, troubleshooting can stop.

## If the Problem Persists

If physical connectivity, workflow, destination availability, and expected configuration have been checked, the remaining cause may involve network infrastructure, DICOM configuration, server services, workstation software, routing, security controls, or another service-level issue.

If local imaging remains safe but transfer is unavailable, follow hospital downtime and data-retention procedures. If the failure compromises clinical workflow or image availability, remove the system from service as appropriate and label it **Out of Service**.

Coordinate Canon service and hospital IT/PACS support as required. Configuration changes should be performed only by authorized qualified personnel.

Before return to normal workflow, verify the complete worklist and/or DICOM path and confirm image receipt at the destination.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A successful local image does not confirm PACS delivery; verify the receiving system before considering the communication problem resolved.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

DICOM problems require verification of the entire communication path rather than assuming the imaging system has failed. Start with physical connectivity and workflow, involve IT when infrastructure is implicated, confirm end-to-end receipt, and document the evidence clearly.

That is successful troubleshooting.
