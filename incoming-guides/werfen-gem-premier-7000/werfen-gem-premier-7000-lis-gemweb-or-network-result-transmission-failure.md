---
schemaVersion: 1
title: "Werfen GEM Premier 7000 Blood Gas Analyzer - LIS, GEMweb, or Network Result Transmission Failure"
issueTitle: "LIS, GEMweb, or Network Result Transmission Failure"
description: "Result-transmission failures involving network connectivity, cabling, ports, configuration, LIS interfaces, GEMweb connectivity, or downstream infrastructure."
assetType: "Blood Gas Analyzer"
manufacturer: "Werfen"
model: "GEM Premier 7000"
slug: "werfen-gem-premier-7000-lis-gemweb-or-network-result-transmission-failure"
dateAdded: "2026-08-20"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that completed GEM Premier 7000 results were visible locally but were not appearing in the LIS."
  cause: "Clinical Engineering found the analyzer's Ethernet cable had a damaged connector and the network link was intermittent."
  resolution: "Replaced the external network cable, confirmed stable connectivity and successful end-to-end result transmission to the LIS, and returned the analyzer to normal use."
helpfulDetails:
  - "Destination affected: LIS, GEMweb, or both"
  - "Whether results remained available locally"
  - "Whether results were queued"
  - "Ethernet cable condition"
  - "Network link indication"
  - "Network jack or port tested"
  - "Known-good cable results"
  - "Whether other analyzers were affected"
  - "IT or middleware findings"
  - "End-to-end transmission verification"
  - "Final analyzer status"
---

## What This Guide Helps With

Result-transmission failures involving network connectivity, cabling, ports, configuration, LIS interfaces, GEMweb connectivity, or downstream infrastructure.

## Step-by-Step Troubleshooting

### 1. Protect Result Communication and Clinical Workflow

Do not assume a result has reached the electronic medical record, LIS, GEMweb, or receiving system simply because testing completed locally.

Establish an approved alternate method for communicating and documenting results while the interface is unavailable.

**Expected outcome:** Clinically important results continue to reach caregivers through a verified alternate workflow.

### 2. Confirm the Scope of the Failure

Determine whether results fail to transmit entirely, remain queued, transmit with delay, fail only to LIS, fail only to GEMweb, or whether the analyzer itself appears offline.

Check whether the issue affects one analyzer or multiple devices.

**Expected outcome:** The failure is isolated to a specific analyzer, destination, or broader network/interface pathway.

### 3. Verify Local Analyzer Operation

Confirm the GEM Premier 7000 completes testing normally and patient results are available locally.

A communication failure should be distinguished from an analyzer measurement failure.

**Expected outcome:** The analyzer itself is functioning normally aside from result transmission.

If the analyzer is also experiencing measurement or startup problems, address those separately before network troubleshooting.

### 4. Inspect the Network Cable and Connections

Check the external Ethernet cable for damage, loose connectors, excessive strain, or disconnection. Reseat accessible connections and verify the correct network jack is being used.

Substitute a known-good network cable when appropriate.

**Expected outcome:** The analyzer has a secure physical network connection.

If a known-good cable restores communication and results transmit successfully, verify the complete path and troubleshooting can stop.

### 5. Check Network Port Status

Observe available external link or connection indicators on the analyzer and network port if present.

Compare with a known-working connection where practical.

**Expected outcome:** Physical network connectivity is present at both ends.

If moving to an approved known-good port restores communication, coordinate correction of the original infrastructure issue and verify transmission.

### 6. Verify Approved Network Configuration

Confirm the analyzer's network configuration matches documented facility settings. Check relevant address, gateway, and other approved parameters only through authorized configuration access.

Do not assign arbitrary network settings or change network identity without coordination with IT or middleware support.

**Expected outcome:** The analyzer is configured according to the approved network design.

If an authorized configuration correction restores connectivity, verify result transmission end to end.

### 7. Check GEMweb, LIS, or Middleware Availability

Determine whether other analyzers can communicate with the same destination. Coordinate with laboratory IT, hospital IT, or middleware support to determine whether GEMweb, LIS, interface engine, or related network services are unavailable.

**Expected outcome:** A system-wide infrastructure problem is either identified or ruled out.

If downstream service restoration resumes normal transmission, confirm previously affected results are handled according to facility policy and troubleshooting can stop.

### 8. Verify Complete Result Transmission

Send or process an approved test transaction as appropriate and confirm the result appears at every required destination, not merely that the network shows connected.

Verify correct patient and result association.

**Expected outcome:** The analyzer transmits successfully and the expected result is received accurately by the intended system.

If achieved, troubleshooting is complete.

### 9. Escalate Persistent Communication Failure

If cabling, port status, analyzer configuration, and destination availability appear correct but transmission remains unsuccessful, stop external troubleshooting.

Escalate jointly to Werfen support, laboratory IT, middleware support, or hospital network teams as appropriate.

**Expected outcome:** The unresolved interface problem is transferred to the team with access to logs, servers, interface configuration, and approved diagnostic tools.

## If the Problem Persists

External cabling, physical network connection, basic analyzer configuration, and receiving-system availability have been checked. Remaining causes may involve interface configuration, network services, firewall or routing behavior, middleware, GEMweb, LIS connectivity, server-side problems, software, or internal analyzer communications.

If reliable result communication cannot be maintained and no approved alternate workflow is available, the analyzer should be:

- Removed from service
- Labeled Out of Service
- Sent for appropriate technical evaluation
- Evaluated using Werfen and facility network/interface documentation
- Configured or repaired only by qualified personnel

Verify the entire result path before return to normal clinical use.

Knowing when to escalate beyond the analyzer to IT or interface support is proper troubleshooting.

## Clinical Use Tip

Always confirm that a result actually reached the intended receiving system; a connected network icon alone does not prove successful result transmission.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->
## Final Thought

Protect clinical communication first, then work outward from the analyzer through cabling, ports, configuration, network infrastructure, middleware, and receiving systems. Verify the complete result path before declaring the problem resolved and document all teams involved.

That is successful troubleshooting.
