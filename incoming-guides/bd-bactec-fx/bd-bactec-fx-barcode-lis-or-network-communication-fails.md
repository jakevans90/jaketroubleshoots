---
schemaVersion: 1
title: "BD BACTEC FX Blood Culture System - Barcode, LIS, or Network Communication Fails"
issueTitle: "Barcode, LIS, or Network Communication Fails"
description: "Troubleshoots barcode-reading, LIS, and network failures caused by labels, scanners, cables, workstation status, network connectivity, or external configuration."
assetType: "Blood Culture System"
manufacturer: "BD"
model: "BACTEC FX"
slug: "bd-bactec-fx-barcode-lis-or-network-communication-fails"
dateAdded: "2026-10-09"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory reported the BACTEC FX was operating locally but no longer transmitted results to the LIS."
  cause: "Clinical Engineering found the workstation network cable partially disconnected, leaving the analyzer application functional but the LIS path unavailable."
  resolution: "The network connection was secured, end-to-end test communication was completed successfully, and laboratory staff confirmed result transmission to the LIS."
helpfulDetails:
  - "Exact communication symptom"
  - "Barcode versus LIS versus network issue"
  - "Whether all or selected specimens were affected"
  - "Barcode label condition"
  - "Scanner status and cable condition"
  - "Workstation status"
  - "Network link status"
  - "Other systems affected"
  - "IT or LIS ticket number if applicable"
  - "Network changes reported"
  - "End-to-end test result"
  - "Final communication status"
---
## What This Guide Helps With

Troubleshoots barcode-reading, LIS, and network failures caused by labels, scanners, cables, workstation status, network connectivity, or external configuration.

## Step-by-Step Troubleshooting

### 1. Protect Specimen Identification and Result Workflow

Do not allow communication troubleshooting to compromise positive patient identification or result traceability. Coordinate with laboratory staff regarding their approved downtime process for accessioning, specimen entry, and result handling.

Do not manually create or transmit patient information outside approved workflow.

**Expected outcome:** Specimen identification and result reporting remain controlled while communications are unavailable.

### 2. Identify Which Communication Path Failed

Determine whether the failure involves barcode reading, analyzer-to-workstation communication, LIS connectivity, result transmission, order download, or general network access.

Confirm whether the problem affects all specimens or only specific labels or transactions.

**Expected outcome:** The failure is isolated to a specific communication stage.

### 3. Check the Barcode and Label

For barcode issues, inspect the label for smearing, wrinkling, damage, poor placement, excessive curvature, overlapping labels, or contamination.

Compare with a known-good barcode when appropriate.

**Expected outcome:** The barcode is readable and appropriately positioned. If the issue follows one damaged label, resolve it through the laboratory's approved identification process and stop equipment troubleshooting.

### 4. Inspect the Barcode Reader

Check the reader's external cable, connector, and accessible scanning window. Verify the reader has power or normal status indicators when applicable.

Clean the scanning surface using an approved method.

**Expected outcome:** The reader is connected, clean, and responsive. If barcode scanning returns consistently, proceed to final verification.

### 5. Verify Workstation Operation

Confirm the connected workstation or computer is powered, responsive, and not frozen. Verify the BACTEC application or permitted interface is open and functioning normally.

Do not change operating-system, network, or application settings without authorization.

**Expected outcome:** The workstation is responsive and able to communicate with the analyzer. If restarting an approved workstation application resolves the issue, verify the full communication path.

### 6. Inspect External Network Connections

Check accessible network cables at the analyzer, workstation, wall jack, switch-connected equipment under Clinical Engineering responsibility, or approved interface device.

Look for disconnected cables, damaged connectors, or absent link indicators when visible.

**Expected outcome:** Physical network connectivity appears intact. If reseating an external network connection restores communication, perform end-to-end verification.

### 7. Determine the Scope of the Network Problem

Ask whether other laboratory systems on the same network or LIS are affected. When permitted, coordinate with IT or laboratory information systems staff to determine whether there is a broader network, interface-engine, or LIS outage.

**Expected outcome:** The issue is isolated to the BACTEC FX path or identified as an infrastructure problem. If the outage is upstream, escalate to the responsible support team.

### 8. Verify Approved Network Configuration

Check only authorized, visible network information such as connection state or documented endpoint assignment. Compare with known documentation if available.

Do not alter IP addressing, ports, firewall rules, interface mappings, or protected communication configuration without proper authorization.

**Expected outcome:** The device's approved external network configuration appears unchanged. Any unexplained configuration discrepancy is escalated rather than modified experimentally.

### 9. Test End-to-End Communication

After correcting an external issue, perform an approved test using laboratory or IT procedures to confirm barcode reading, order receipt, and/or result transmission through the complete required path.

**Expected outcome:** The appropriate information reaches the intended destination accurately. If communication remains incomplete, stop and escalate.

## If the Problem Persists

Barcode condition, reader connection, workstation status, external network cabling, and broad infrastructure availability have been checked. The remaining issue may involve an internal communication interface, application service, LIS interface engine, network configuration, server, firewall, or other service-level dependency.

The affected communication function should be:

- Removed from routine use when data integrity cannot be assured.
- Labeled **Out of Service** as appropriate.
- Evaluated jointly with Clinical Engineering, laboratory IT/LIS support, network support, or BD service as applicable.
- Tested using current documentation and approved tools.
- Reconfigured only by authorized personnel.

Before return to service, verify the complete communication path rather than only confirming that a network link light is present.

Knowing when a problem crosses from equipment troubleshooting into enterprise infrastructure support is part of proper troubleshooting.

## Clinical Use Tip

Verify the final patient result reaches the intended LIS destination before ending downtime procedures.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Communication troubleshooting must protect patient identity and data integrity. Isolate the failure from barcode to analyzer, workstation, network, and LIS, verify the complete path after correction, and escalate infrastructure or configuration problems to the appropriate support team.

That is successful troubleshooting.
