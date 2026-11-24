---
schemaVersion: 1
title: "Fujifilm Sonosite Sonosite LX Ultrasound System - DICOM Worklist, Storage, or Wireless Connection Fails"
issueTitle: "DICOM Worklist, Storage, or Wireless Connection Fails"
description: "Troubleshoots missing worklists, failed image storage, or wireless communication caused by connectivity, configuration, destination, or infrastructure problems."
assetType: "Ultrasound System"
manufacturer: "Fujifilm Sonosite"
model: "Sonosite LX"
slug: "fujifilm-sonosite-sonosite-lx-dicom-worklist-storage-or-wireless-connection-fails"
dateAdded: "2026-11-24"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Sonosite LX could acquire images but could not retrieve the DICOM worklist or send studies wirelessly."
  cause: "Clinical Engineering verified normal local operation and found that the system could not maintain connectivity in the reported wireless coverage area."
  resolution: "The network issue was escalated to the appropriate infrastructure team, connectivity was restored, and worklist retrieval and test image storage were verified."
helpfulDetails:
  - "Function affected: worklist, storage, or wireless"
  - "Exact displayed message"
  - "Network connection indication"
  - "Location where failure occurred"
  - "Known-good area comparison"
  - "Destination selected"
  - "Connectivity-test results"
  - "PACS receipt confirmation"
  - "Infrastructure escalation"
  - "Final communication status"
---

## What This Guide Helps With

Troubleshoots missing worklists, failed image storage, or wireless communication caused by connectivity, configuration, destination, or infrastructure problems.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow
If network communication is required for immediate patient care, establish the facility-approved alternate imaging and documentation workflow before troubleshooting.

Expected outcome: Imaging and patient identification can continue safely without relying on failed connectivity.

### 2. Define the Communication Failure
Determine whether the problem affects worklist retrieval, image storage, wireless connectivity, or all network functions. Record any exact displayed message without interpreting or changing configuration prematurely.

Expected outcome: The failure is narrowed to a specific communication function.

### 3. Verify Basic System Operation
Confirm that the Sonosite LX otherwise operates normally and can acquire images locally.

Expected outcome: Local ultrasound operation is normal, separating the communication problem from a broader system failure.

### 4. Check Network Connection Status
Verify the expected network connection is active using normal user-accessible indicators. For wireless operation, verify the intended network is selected and that connectivity is not obviously lost because of location or signal availability.

Expected outcome: The system shows an active network connection.

### 5. Check the Environment and Location
Move the system, when practical, to a location known to have reliable approved wireless coverage. Compare with another functioning device on the same clinical network when available.

Expected outcome: Communication works in a known-good coverage area or the issue is confirmed to persist independent of location.

### 6. Verify Accessible DICOM Destination Settings
Review normal authorized configuration information such as the selected worklist or storage destination. Compare against documented facility settings or another correctly configured Sonosite LX.

Do not change IP addresses, security settings, certificates, or protected network configuration without authorization.

Expected outcome: The intended destination and accessible configuration match known-good facility values.

### 7. Test the Communication Path
Perform an approved DICOM or network connectivity test available through normal system functions. If local network connectivity is present but the destination cannot be reached, coordinate with PACS or network support.

Expected outcome: The system successfully communicates with the intended service or evidence identifies an infrastructure/destination failure.

### 8. Test a Controlled Image Transfer
Use a nonclinical or appropriately authorized test study and confirm that transmission completes and is received at the intended destination.

Expected outcome: Image storage completes successfully. If worklist retrieval and transfer both function normally, troubleshooting can stop.

### 9. Perform Final Workflow Verification
Verify the complete required path: connectivity, worklist if used, image acquisition, storage/send, and receipt by the intended clinical system.

Expected outcome: The full communication workflow is confirmed operational.

## If the Problem Persists

Basic system operation, physical or wireless connectivity, location, and accessible configuration have been checked. Remaining causes may involve DICOM configuration, authentication, certificates, network infrastructure, firewall rules, wireless services, PACS availability, software, or internal network hardware.

Remove the system from network-dependent clinical service if required connectivity cannot be assured. Label it **Out of Service** when appropriate and coordinate bench evaluation or infrastructure support. Use Fujifilm Sonosite documentation, approved test equipment, and authorized network personnel for further evaluation.

After correction, verify the complete communication path before return to normal workflow. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A successful local image acquisition does not prove successful documentation—verify that the study reaches the intended destination.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Communication troubleshooting should separate the ultrasound system from the network and destination. Verify each part of the path, avoid unauthorized configuration changes, and document exactly where communication succeeds or fails.

That is successful troubleshooting.
