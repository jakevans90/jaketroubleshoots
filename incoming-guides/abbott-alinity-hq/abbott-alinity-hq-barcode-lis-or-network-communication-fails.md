---
schemaVersion: 1
title: "Abbott Alinity hq Hematology Analyzer - Barcode, LIS, or Network Communication Fails"
issueTitle: "Barcode, LIS, or Network Communication Fails"
description: "Addresses barcode, LIS, and network failures caused by label quality, cabling, connectivity, interface status, configuration, or external infrastructure problems."
assetType: "Hematology Analyzer"
manufacturer: "Abbott"
model: "Alinity hq"
slug: "abbott-alinity-hq-barcode-lis-or-network-communication-fails"
dateAdded: "2026-10-06"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that the Abbott Alinity hq completed testing but results were not transmitting to the LIS."
  cause: "Clinical Engineering found the analyzer's external network cable partially disconnected at the approved connection point."
  resolution: "Clinical Engineering secured the network connection and verified a test result transmitted successfully through the laboratory interface to the intended downstream system."
helpfulDetails:
  - "Whether barcode, orders, results, or all communication failed"
  - "One sample or all samples affected"
  - "Barcode condition"
  - "Network-cable condition"
  - "Link indicator status"
  - "Analyzer interface status"
  - "Other laboratory devices affected"
  - "LIS or middleware availability"
  - "Recent network or interface changes"
  - "Ports or rooms affected"
  - "End-to-end test result"
  - "Final interface status"
---
## What This Guide Helps With

Addresses barcode, LIS, and network failures caused by label quality, cabling, connectivity, interface status, configuration, or external infrastructure problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification and Result Routing
Do not manually associate specimens or transmit results outside approved laboratory downtime procedures when identification or interface communication is unreliable.

Confirm whether the issue affects barcode reading, worklist receipt, order matching, result transmission, or all network communication.

**Expected outcome:** Patient identification and result integrity are protected, and the affected communication layer is identified.

### 2. Determine the Scope
Check whether one sample barcode fails or all barcodes fail. Determine whether one analyzer is affected or other laboratory systems are also experiencing LIS or network problems.

**Expected outcome:** The problem is identified as sample-specific, analyzer-specific, or infrastructure-wide.

### 3. Inspect the Barcode
For sample-specific failures, inspect the barcode for wrinkles, smearing, low contrast, damage, excessive curvature, poor placement, or obstruction by another label.

Use a known-good properly labeled sample or approved test barcode for comparison.

**Expected outcome:** A valid barcode is read successfully. If only the original label fails, correct the specimen-identification issue and stop.

### 4. Inspect External Network Connections
Verify accessible network or interface cables are fully seated and not damaged. Check link indicators where normally visible without disturbing infrastructure.

Do not move cables between network ports unless the approved port assignment is known.

**Expected outcome:** Physical communication connections are secure. If reseating an approved loose connection restores communication, verify end-to-end transmission and stop.

### 5. Check Analyzer Communication Status
Review the normal analyzer interface or connectivity status available to Clinical Engineering and laboratory staff.

Determine whether the analyzer reports disconnected, offline, paused, or another visible communication state.

**Expected outcome:** The analyzer is configured to participate in normal communication. If communication was simply paused and approved restoration resolves the issue, verify and stop.

### 6. Verify the Upstream and Downstream Path
Determine whether the LIS, middleware, interface engine, switch, or other connected systems are available. Coordinate with laboratory IT or hospital IT when appropriate.

Avoid changing IP addressing, ports, interface configuration, or routing without an approved change process.

**Expected outcome:** External infrastructure availability is confirmed, or the issue is appropriately transferred to the responsible team.

### 7. Compare With Other Connected Devices
Check whether another laboratory analyzer on the same workflow can receive orders and send results.

A broader outage suggests network, LIS, middleware, or interface infrastructure rather than an isolated Alinity hq failure.

**Expected outcome:** The fault domain is narrowed to the analyzer or shared infrastructure.

### 8. Review Recent Changes
Ask whether the issue began after switch work, network maintenance, LIS changes, middleware updates, analyzer relocation, cable work, or configuration changes.

Document the timing and involved teams.

**Expected outcome:** A recent external change is identified or ruled out.

### 9. Perform an Approved Communication Restart
If appropriate and coordinated with the laboratory, restart the normal communication session or perform an approved analyzer restart.

Do not repeatedly reboot to compensate for unresolved infrastructure problems.

**Expected outcome:** Communication reconnects and remains stable. If it does, proceed to end-to-end verification.

### 10. Verify the Complete Communication Path
Using an approved test workflow, confirm sample identification, order receipt where applicable, analysis association, result transmission, and receipt at the intended downstream system.

**Expected outcome:** Barcode and LIS/network communication function correctly end to end. The issue is resolved and troubleshooting can stop.

## If the Problem Persists

Barcode condition, external cables, analyzer communication state, known infrastructure availability, and recent external changes have been ruled out. The remaining cause may involve analyzer network hardware, interface software, middleware configuration, LIS configuration, network services, port assignment, or other service-level communication issues.

The analyzer should be:

- Removed from normal interfaced use if patient identification or result routing cannot be assured
- Labeled Out of Service when appropriate
- Sent for repair or service evaluation if the fault is analyzer-specific
- Evaluated using appropriate Abbott documentation and approved network/service tools
- Configured only by qualified and authorized personnel

After correction, verify the complete communication path before returning the analyzer to normal interfaced patient testing.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never confirm communication repair only at the analyzer screen; verify that the correct result reaches the correct downstream patient record or approved test destination.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Communication troubleshooting should move from specimen identification to physical connection to analyzer status and then shared infrastructure. Protect patient-result association throughout, and verify the entire path before declaring the issue resolved.

That is successful troubleshooting.
