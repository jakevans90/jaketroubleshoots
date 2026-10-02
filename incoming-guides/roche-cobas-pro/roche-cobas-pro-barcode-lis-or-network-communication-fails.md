---
schemaVersion: 1
title: "Roche cobas pro Clinical Chemistry Analyzer - Barcode, LIS, or Network Communication Fails"
issueTitle: "Barcode, LIS, or Network Communication Fails"
description: "Troubleshoots barcode, LIS, and network failures caused by label quality, cables, ports, connectivity, interface status, configuration, or upstream systems."
assetType: "Clinical Chemistry Analyzer"
manufacturer: "Roche"
model: "cobas pro"
slug: "roche-cobas-pro-barcode-lis-or-network-communication-fails"
dateAdded: "2026-10-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported the cobas pro stopped receiving LIS orders while the analyzer otherwise remained operational."
  cause: "Clinical Engineering found the analyzer network cable partially disconnected at the external network jack."
  resolution: "Reseated the network connection, verified link restoration, and confirmed with laboratory staff that test orders and results transmitted correctly through the LIS interface."
helpfulDetails:
  - "Exact barcode or interface message"
  - "Orders, results, or both affected"
  - "Whether other analyzers are affected"
  - "Barcode label condition"
  - "Network cable condition"
  - "Link/activity indication"
  - "Network jack or port used"
  - "Recent IT or switch changes"
  - "Middleware/LIS status"
  - "Communication path tested"
  - "Test order/result outcome"
  - "Final interface status"
---
## What This Guide Helps With

Troubleshoots barcode, LIS, and network failures caused by label quality, cables, ports, connectivity, interface status, configuration, or upstream systems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification and Establish Downtime Workflow

Do not bypass positive patient identification or manually alter orders merely to work around an unresolved communication problem.

Follow laboratory downtime procedures when:
- Orders are not received
- Patient identifiers cannot be verified
- Results cannot transmit
- Barcode identification is unreliable

**Expected outcome:** Patient identification and result reporting remain controlled while communication is unavailable.

### 2. Determine Which Communication Function Failed

Separate the problem into:
- Barcode read failure
- LIS order-download failure
- Result-upload failure
- Analyzer network connectivity loss
- Bidirectional interface failure
- One workstation or multiple systems affected

Record the exact message and time of failure.

**Expected outcome:** The failure domain is narrowed before configuration changes are considered.

### 3. Inspect the Barcode and Sample Label

For barcode-specific failures, check:
- Label is present
- Print is clear
- Barcode is not wrinkled or damaged
- Label is not covered with condensation
- Placement does not interfere with tube seating
- The same barcode can be read through an approved alternate workflow if available

**Expected outcome:** A readable, correctly positioned barcode is presented. If relabeling according to laboratory procedure restores identification, troubleshooting can stop after verification.

### 4. Inspect External Network and Interface Connections

Check accessible:
- Ethernet cables
- Network jacks
- External interface connections
- Connected middleware or interface devices
- Link/activity indicators where normally visible

Reseat loose accessible connections and look for cable damage.

**Expected outcome:** Physical network connections are secure and expected link indications are present.

### 5. Check Scope of the Network Problem

Determine whether:
- Only the cobas pro is affected
- Other laboratory analyzers have also lost LIS connectivity
- The associated workstation has network access
- A recent switch, VLAN, firewall, interface-engine, or server change occurred

Coordinate with hospital IT or laboratory middleware support when infrastructure is involved.

**Expected outcome:** The problem is separated into analyzer-local or infrastructure-wide categories.

### 6. Verify Normal Interface Status Without Unauthorized Changes

Review normal user-accessible communication status displays.

Document:
- Connected/disconnected state
- Queued transactions
- Failed orders or results
- Interface messages visible to authorized users

Do not change IP addresses, host definitions, ports, interface mappings, or other validated configuration unless authorized and documented.

**Expected outcome:** Communication status is known without introducing configuration drift.

### 7. Test the Communication Path

Using approved procedures, verify the complete path as appropriate:
- Barcode to analyzer
- Analyzer to middleware
- Middleware to LIS
- LIS order back to analyzer
- Analyzer result transmission

Coordinate testing with LIS/IT personnel so duplicate or test records are handled correctly.

**Expected outcome:** The point where communication stops is identified.

### 8. Verify Recovery

After correcting an external cable, network, label, or upstream problem:
- Confirm orders populate correctly
- Confirm sample identifiers match
- Confirm an approved test result reaches the intended destination
- Check any queued data according to laboratory procedure

**Expected outcome:** Bidirectional communication functions normally and specimen/result identity is preserved. Troubleshooting is complete.

### 9. Escalate Persistent Communication Failure

If physical connections and upstream systems are verified but communication remains unavailable, escalate to the appropriate Roche, LIS, middleware, or hospital-network support team.

Avoid trial-and-error configuration changes on a production analyzer.

**Expected outcome:** The communication fault is handed off with enough evidence to identify the responsible support domain.

## If the Problem Persists

Common label, cable, connection, and basic network causes have been ruled out. Remaining causes may involve interface configuration, middleware, LIS services, network segmentation, ports, firewall rules, software, or analyzer communication hardware.

The affected communication pathway should be:
- Removed from normal clinical use when patient/order identity cannot be assured
- Labeled or documented Out of Service as appropriate
- Evaluated using Roche-approved documentation and approved network diagnostic methods
- Reconfigured or repaired only by qualified and authorized personnel

Verify end-to-end order and result transmission before normal operation resumes.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A network connection is not fully verified until the complete patient-order-result pathway works correctly at the intended LIS destination.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Communication troubleshooting must protect patient identity first. Check the label and physical network path before configuration, verify the complete LIS workflow after correction, and involve the appropriate infrastructure team when the fault extends beyond the analyzer.

That is successful troubleshooting.
