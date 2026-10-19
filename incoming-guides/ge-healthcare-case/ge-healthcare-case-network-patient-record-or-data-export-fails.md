---
schemaVersion: 1
title: "GE Healthcare CASE Stress Test System - Network, Patient Record, or Data Export Fails"
issueTitle: "Network, Patient Record, or Data Export Fails"
description: "CASE cannot access expected patient information, communicate with connected systems, or transfer completed study data through its configured workflow."
assetType: "Stress Test System"
manufacturer: "GE Healthcare"
model: "CASE"
slug: "ge-healthcare-case-network-patient-record-or-data-export-fails"
dateAdded: "2026-10-19"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the CASE workstation could not send completed stress-study data to the configured destination."
  cause: "Clinical Engineering found the workstation had no network link because the Ethernet cable was partially disconnected."
  resolution: "Reseated the network cable and verified successful transfer of an approved test record to the configured destination."
helpfulDetails:
  - "Exact failed workflow"
  - "Exact displayed message"
  - "One patient versus all patients affected"
  - "Ethernet cable and link status"
  - "Network jack tested"
  - "Known-good cable result"
  - "Documented network configuration checked"
  - "Destination or server availability"
  - "Test-record transfer result"
  - "Final device status"
---

## What This Guide Helps With
CASE cannot access expected patient information, communicate with connected systems, or transfer completed study data through its configured workflow.

## Step-by-Step Troubleshooting
### 1. Protect Patient Data and Clinical Workflow
Determine whether the communication failure affects only convenience or prevents safe identification, review, or storage of the current patient's study. Do not create duplicate or incorrectly identified patient records to work around the problem.

**Expected outcome:** Patient data integrity is protected and staff have an appropriate clinical workflow while troubleshooting occurs.

### 2. Define the Exact Communication Failure
Determine whether the problem involves patient lookup, worklist, inbound demographics, network connectivity, study storage, report transfer, printing, export, or another configured interface. Record the exact displayed message when available.

**Expected outcome:** The failing workflow and direction of data transfer are clearly identified.

### 3. Determine Whether One Patient or All Patients Are Affected
Test with an appropriate nonpatient or approved test workflow when possible. Determine whether the issue is record-specific, destination-specific, or system-wide.

**Expected outcome:** The scope of the failure is established without risking patient-data integrity.

### 4. Check Physical Network Connection
Inspect the Ethernet cable and accessible network connection for damage or looseness. Confirm link indicators are present when applicable. Test with a known-good approved cable or active jack when permitted.

Do not move the system to an arbitrary network port without confirming the correct network assignment.

**Expected outcome:** A stable physical network link is established.

### 5. Verify the Network Jack or Infrastructure
Determine whether other equipment on the same approved network segment is functioning. Coordinate with IT when the wall jack, switch port, VLAN, or broader infrastructure is suspected.

**Expected outcome:** The problem is separated between the CASE system and facility network infrastructure.

### 6. Review Approved Network Configuration
Verify user- or CE-accessible network information against the documented configuration. Do not change IP addressing, VLAN assignment, firewall settings, interface destinations, or other protected parameters without authorization.

**Expected outcome:** CASE is using the intended documented network configuration.

### 7. Verify Destination Availability
Confirm the expected receiving system, server, archive, or interface is available through the appropriate support team. Determine whether other devices are experiencing the same outage.

**Expected outcome:** The receiving infrastructure is confirmed available or the issue is identified as an external system outage.

### 8. Test Data Transfer Using an Approved Test Record
Once connectivity is restored, perform an approved test transaction or export. Confirm that information arrives at the intended destination and remains associated with the correct test identity.

**Expected outcome:** The transfer completes successfully end to end. If it does, troubleshooting can stop after documenting verification.

### 9. Verify Complete Clinical Workflow
Confirm patient information can be accessed as intended, a representative record can be saved, and required study data or reports reach the configured destination.

**Expected outcome:** The complete network and patient-record workflow operates normally and the system is ready for clinical use.

## If the Problem Persists
Physical cabling, network link, documented configuration, destination availability, and basic transfer testing have been evaluated. The remaining issue may involve network infrastructure, interface engines, server services, application configuration, database connectivity, security settings, or CASE software.

If the failure prevents safe patient identification, reliable study storage, or required clinical communication, remove the system from service and label it **Out of Service** until an approved workflow is restored. Coordinate with IT, Clinical Engineering integration support, and GE Healthcare service as appropriate.

Do not make undocumented network changes simply to restore connectivity. Verify the complete data path before return to service.

## Clinical Use Tip
After restoring connectivity, confirm the test record reached the correct patient and destination rather than assuming a successful network connection guarantees a successful clinical transfer.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Network troubleshooting should follow the complete data path from physical connection through infrastructure to the final clinical destination. Preserve patient identity and data integrity, avoid unauthorized configuration changes, and document successful end-to-end verification.

That is successful troubleshooting.
