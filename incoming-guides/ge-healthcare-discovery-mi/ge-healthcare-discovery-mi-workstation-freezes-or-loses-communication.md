---
schemaVersion: 1
title: "GE Healthcare Discovery MI PET / CT System - Workstation Freezes or Loses Communication"
issueTitle: "Workstation Freezes or Loses Communication"
description: "Troubleshoots frozen workstations and communication loss caused by power, cables, network connectivity, peripherals, software state, or subsystem availability."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "Discovery MI"
slug: "ge-healthcare-discovery-mi-workstation-freezes-or-loses-communication"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Imaging staff reported that the Discovery MI operator workstation lost communication with the scanner during setup for a study."
  cause: "Clinical Engineering found an accessible network connection at the workstation partially disconnected."
  resolution: "Clinical Engineering reseated the connection, performed an approved workstation restart, verified stable scanner communication and data access, and completed functional checks before return to service."
helpfulDetails:
  - "Exact displayed message"
  - "Workstation response"
  - "PET or CT communication affected"
  - "Study active at time of failure"
  - "External cable condition"
  - "Network link status"
  - "Other devices affected"
  - "IT or PACS outage status"
  - "Restart result"
  - "Final communication status"
---
## What This Guide Helps With
Troubleshoots frozen workstations and communication loss caused by power, cables, network connectivity, peripherals, software state, or subsystem availability.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve the Study

If the workstation freezes or loses communication during a patient examination, do not continue scanning until system status and data handling are understood.

Maintain patient safety and avoid unnecessary repeat acquisition. Do not force shutdowns that could jeopardize unsaved study data unless required for safety.

**Expected outcome:** The patient is safe and existing study data are protected as much as possible.

### 2. Define the Failure

Determine whether:

- The display is frozen
- Keyboard or mouse input is unresponsive
- The workstation is responsive but scanner communication is lost
- PET communication is affected
- CT communication is affected
- Network destinations are affected while local scanning remains available
- The problem followed a specific action

Record exact messages and visible status indicators.

**Expected outcome:** The issue is identified as a local workstation, scanner-communication, or broader network problem.

### 3. Check Workstation Power and Displays

Verify that accessible workstation and display power connections are secure.

Check:

- Power indicators
- Display status
- Power strips or approved UPS equipment where applicable
- Loose external power cords
- Whether the workstation itself is running despite a blank display

**Expected outcome:** Workstation and display power are stable.

### 4. Check External Data and Network Connections

Inspect accessible network and communication cables.

Look for:

- Loose connections
- Damaged connectors
- Disconnected cables
- Recently moved equipment
- Inactive link indicators where normally visible
- Known network maintenance or outage

Do not disconnect restricted internal system network connections without service guidance.

**Expected outcome:** Accessible communication and network connections are secure.

### 5. Check Connected Peripherals

Inspect approved external peripherals for abnormal behavior.

A malfunctioning removable peripheral can sometimes coincide with workstation responsiveness problems. Disconnect or substitute only equipment that is approved for user or Clinical Engineering handling and only when doing so will not affect active patient data.

**Expected outcome:** No obvious external peripheral is causing or contributing to the problem.

### 6. Determine the Scope of the Communication Failure

Check whether other systems on the same network or imaging area are experiencing similar communication problems.

When appropriate, coordinate with IT or imaging informatics to determine whether there is a broader:

- Network outage
- Switch issue
- VLAN issue
- Server outage
- PACS or worklist outage

**Expected outcome:** A facility-network problem is identified or ruled out before the scanner is blamed.

### 7. Perform an Approved Workstation Restart

After protecting study data and when no patient depends on the scanner, use an approved normal shutdown and restart process.

Do not repeatedly hard-power-cycle the workstation.

**Expected outcome:** The workstation restarts normally, reconnects to required system components, and remains responsive.

If normal function returns, proceed to final verification.

### 8. Verify Complete Communication and Workflow

Confirm:

- Workstation controls respond
- Scanner status is visible
- PET and CT components communicate normally
- Study data can be accessed
- Required network destinations are reachable through normal system workflow
- No unresolved communication warning remains

**Expected outcome:** The workstation and scanner communication path operate normally.

If communication remains stable and applicable functional checks pass, troubleshooting can stop and the system may be returned to service.

## If the Problem Persists

If workstation power, external cabling, peripherals, network availability, and an approved restart have been verified but freezing or communication loss persists, the cause may involve workstation hardware, operating software, internal system networking, storage, subsystem communication, database services, or another service-level condition.

The system should be:

- Removed from service if reliable operation cannot be assured
- Labeled Out of Service
- Sent for repair or formal system evaluation
- Evaluated using appropriate GE Healthcare documentation and approved diagnostic tools
- Repaired or configured only by qualified personnel

Coordinate with IT or imaging informatics when evidence points to shared infrastructure.

After repair, verify system communication, acquisition, data handling, and required network workflow before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Before restarting a frozen workstation, determine whether active or unsaved patient data could be lost and preserve the study whenever possible.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Workstation problems should be separated into local power, peripheral, scanner-communication, and network categories before internal failure is assumed. Preserve patient data, verify the complete communication path, and escalate persistent failures appropriately.

That is successful troubleshooting.
