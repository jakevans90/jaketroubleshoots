---
schemaVersion: 1
title: "Canon Alphenix Sky+ Angiography System - Network, Patient Record, or Data Export Fails"
issueTitle: "Network, Patient Record, or Data Export Fails"
description: "Troubleshoot network connectivity, patient information exchange, image or data transfer, and export failures caused by connections, destinations, configuration, or infrastructure."
assetType: "Angiography System"
manufacturer: "Canon"
model: "Alphenix Sky+"
slug: "canon-alphenix-sky-network-patient-record-or-data-export-fails"
dateAdded: "2026-10-14"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Canon Alphenix Sky+ could not send study data to the configured clinical destination."
  cause: "Clinical Engineering found the accessible network cable disconnected at the system connection and confirmed network link after reconnection."
  resolution: "Clinical Engineering reconnected the cable, verified network communication and successful test transfer to the intended destination, and returned the network function to service."
helpfulDetails:
  - "Communication function affected"
  - "Exact error or status message"
  - "Date and time of failure"
  - "Network link status"
  - "Cable and port tested"
  - "Destinations affected"
  - "Whether other network functions worked"
  - "Patient/worklist behavior"
  - "IT or integration findings"
  - "Successful end-to-end test result"
  - "Final system status"
---
## What This Guide Helps With
Troubleshoot network connectivity, patient information exchange, image or data transfer, and export failures caused by connections, destinations, configuration, or infrastructure.

## Step-by-Step Troubleshooting
### 1. Protect Patient Care and Data Integrity
If network or patient-record communication fails during a procedure, follow the facility's approved downtime workflow. Do not alter identifiers or repeatedly resend data without understanding the destination state.

**Expected outcome:** Patient care continues safely and duplicate or mismatched records are avoided.

### 2. Define the Communication Failure
Determine whether the issue affects network connectivity, patient worklist or record information, image transfer, data export, one destination, or all destinations. Record exact messages and timestamps.

**Expected outcome:** The communication failure is narrowed to a specific function and destination.

### 3. Verify Local Network Connection
Inspect accessible Ethernet or approved network connections for looseness, damage, or disconnection. Observe available link indicators without changing network configuration.

**Expected outcome:** The physical connection appears intact and network link is present where applicable.

### 4. Check the Scope of the Problem
Determine whether other network functions on the system work and whether other devices in the same area can reach the relevant clinical system.

**Expected outcome:** The problem is classified as device-specific, destination-specific, or potentially infrastructure-wide.

### 5. Verify Patient and Destination Selection
Confirm that the correct patient, study, destination, or export target has been selected using normal clinical controls. Do not modify protected network parameters merely to test connectivity.

**Expected outcome:** The transfer is being attempted with the intended patient context and destination.

### 6. Check External Export Media or Accessories
If the failure involves approved removable media or another export accessory, inspect the media and interface and test with a known-good approved alternative when appropriate.

**Expected outcome:** External export media or accessories are confirmed functional or identified as the cause.

### 7. Verify Accessible Network Configuration Without Changing It
Record visible network status and configuration information that Clinical Engineering is authorized to view. Compare it with documented site records when available. Do not make unapproved IP, VLAN, destination, or security changes.

**Expected outcome:** No obvious discrepancy exists, or a documented configuration problem is identified for correction through the appropriate process.

### 8. Coordinate With IT or Integration Support
If physical connectivity is intact but communication remains unavailable, provide IT or application support with the affected system, destination, timestamp, network status, and exact failure behavior.

**Expected outcome:** Infrastructure, server, interface, firewall, routing, or destination-system causes can be evaluated without unnecessary changes to the medical device.

### 9. Verify End-to-End Communication
After correction, perform an approved test that confirms data reaches the intended destination and is associated with the correct patient or test record.

**Expected outcome:** The complete communication path operates correctly. Troubleshooting can stop.

### 10. Escalate Recurrent or Unresolved Communication Failure
If communication remains unreliable or the system loses data connectivity repeatedly, remove the affected network-dependent function from service and escalate appropriately.

**Expected outcome:** Unreliable data exchange is not represented as functional.

## If the Problem Persists
External cabling, patient/destination selection, approved export media, and obvious local network conditions have been checked. Remaining causes may involve server availability, network infrastructure, routing, security policies, interface-engine configuration, application services, device configuration, or internal communication hardware.

Label the affected system or network function **Out of Service** as appropriate and arrange coordinated evaluation with qualified Clinical Engineering, IT, application, integration, and/or manufacturer support. Use approved documentation and test tools. Do not make unauthorized network or software configuration changes.

Return to normal clinical workflow only after end-to-end patient and data communication has been verified. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
Always verify that transferred data reaches the correct destination and patient record rather than assuming a successful send command completed the workflow.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought
Preserve patient and data integrity, separate device problems from infrastructure problems logically, avoid unauthorized network changes, and verify the full communication path before closing the work order.

That is successful troubleshooting.
