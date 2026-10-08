---
schemaVersion: 1
title: "Cepheid GeneXpert Infinity Molecular Diagnostic System - Barcode, LIS, or Network Communication Fails"
issueTitle: "Barcode, LIS, or Network Communication Fails"
description: "Troubleshoot barcode identification, LIS connectivity, network communication, interface, cabling, workstation, and configuration problems from the device outward."
assetType: "Molecular Diagnostic System"
manufacturer: "Cepheid"
model: "GeneXpert Infinity"
slug: "cepheid-genexpert-infinity-barcode-lis-or-network-communication-fails"
dateAdded: "2026-10-08"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that GeneXpert Infinity results were no longer transmitting to the LIS."
  cause: "Clinical Engineering found the external network cable partially disconnected at the analyzer workstation connection."
  resolution: "Clinical Engineering reseated the network connection and coordinated an end-to-end test confirming order communication and successful result transmission to the LIS."
helpfulDetails:
  - "Exact communication error"
  - "Barcode versus LIS versus network symptom"
  - "Scope of affected specimens"
  - "Cable and link status"
  - "Workstation status"
  - "Approved network settings observed"
  - "Recent switch, VLAN, firewall, or interface changes"
  - "LIS/interface status"
  - "Other affected laboratory systems"
  - "End-to-end test result"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoot barcode identification, LIS connectivity, network communication, interface, cabling, workstation, and configuration problems from the device outward.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification and Result Workflow
Determine whether patient testing can continue safely without the affected barcode or LIS connection. Do not allow manual workarounds that could create specimen-to-patient or result-to-patient mismatches unless they are part of an approved laboratory downtime procedure.

**Expected outcome:** Patient identification and result routing remain controlled while troubleshooting proceeds.

### 2. Define Which Communication Path Failed
Determine whether the problem affects barcode scanning, order download, specimen matching, LIS connectivity, result transmission, or all network communication.

Record the exact message and whether the problem affects all specimens or only selected ones.

**Expected outcome:** The fault is narrowed to barcode, local workstation, network, interface, or LIS workflow.

### 3. Check the Barcode and Label
For barcode-related failures, inspect the specimen label for damage, wrinkles, poor placement, contamination, or obstruction. Compare with another correctly labeled sample or approved test barcode when laboratory policy permits.

**Expected outcome:** A readable, properly positioned barcode scans successfully. If it does, troubleshooting can stop after verifying normal workflow.

### 4. Inspect External Network Connections
Check accessible Ethernet cables and connectors at the analyzer/workstation and approved network connection point. Look for loose connectors, damaged latches, pinched cables, or disconnected patching.

Do not move the analyzer to an arbitrary network port.

**Expected outcome:** All required physical network connections are secure and undamaged.

### 5. Check Network Link Status
Observe available link indicators on accessible network interfaces or approved infrastructure. Determine whether the device appears physically connected to the network.

**Expected outcome:** A network link is present. Absence of link after cable verification supports infrastructure or interface escalation.

### 6. Verify Workstation and Application Status
Confirm the GeneXpert Infinity workstation and required user-accessible applications are running normally and have not frozen or lost communication with the analyzer.

**Expected outcome:** The local workstation is operational and not the source of the communication failure.

### 7. Determine the Scope of the Network Problem
Ask whether other laboratory devices have lost LIS or network connectivity. Check whether the issue began after switch work, VLAN changes, network maintenance, interface-engine changes, or a facility outage.

**Expected outcome:** The issue is identified as device-specific or infrastructure-wide.

### 8. Verify Approved Network Configuration
Review documented device network settings when authorized and compare them with the established configuration. Do not change IP address, subnet, gateway, DNS, interface destinations, or security settings without proper coordination.

**Expected outcome:** Device configuration matches the approved network design or a discrepancy is identified for coordinated correction.

### 9. Verify LIS or Interface Availability
Coordinate with laboratory IT or interface support to determine whether the LIS/interface endpoint is available and receiving communication from other devices.

**Expected outcome:** The downstream system is either confirmed operational or identified as the source of the outage.

### 10. Test the Complete Communication Path
After correcting an external connection or infrastructure problem, have laboratory staff perform an approved end-to-end test, including the relevant barcode, order, and result-routing functions.

**Expected outcome:** The entire communication path works correctly. If verified, troubleshooting can stop.

### 11. Escalate Persistent Communication Failure
If barcode quality, cabling, network link, workstation operation, approved configuration, and downstream availability are verified but communication still fails, stop external troubleshooting.

**Expected outcome:** The device is not returned to unrestricted clinical use with an unreliable patient-data pathway.

## If the Problem Persists

Common external barcode, cable, network, workstation, interface, and infrastructure causes have been ruled out. The remaining problem may involve device software, the network interface, application configuration, middleware, security policy, or another service-level condition.

The affected GeneXpert Infinity should be:

- Removed from the affected connected workflow
- Labeled **Out of Service** if safe testing cannot continue
- Sent for repair or qualified service evaluation when device-related
- Evaluated using current manufacturer documentation and approved test equipment
- Reconfigured only by qualified and authorized personnel

Perform an end-to-end order and result-routing verification before returning connected clinical functionality to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A test result is not safely complete until the correct result reaches the correct patient record through the validated communication path.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Communication troubleshooting should move logically from labels and cables through the workstation, network, interface, and LIS. Protect patient identification, avoid unauthorized configuration changes, and verify the complete data path before closure.

That is successful troubleshooting.
