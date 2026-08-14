---
schemaVersion: 1
title: "Philips IntelliVue MX750 Patient Monitor - PIC iX Central Station or Network Communication Failure"
issueTitle: "PIC iX Central Station or Network Communication Failure"
description: "Troubleshoots loss of central monitoring or network communication caused by connections, network path, assignment, configuration, or infrastructure issues."
assetType: "Patient Monitor"
manufacturer: "Philips"
model: "IntelliVue MX750"
slug: "philips-intellivue-mx750-pic-ix-central-station-or-network-communication-failure"
dateAdded: "2026-08-14"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the IntelliVue MX750 was monitoring locally but was absent from the PIC iX central station."
  cause: "Clinical Engineering found the bedside network cable had an intermittent connector and failed comparison testing."
  resolution: "Clinical Engineering replaced the cable and verified patient data, waveform updates, and alarm communication at the assigned central station."
helpfulDetails:
  - "Whether local monitoring remained normal"
  - "Exact connectivity message"
  - "Central station or room affected"
  - "Whether one or multiple monitors were affected"
  - "Network cable condition"
  - "Wall port or docking connection tested"
  - "Known-good cable result"
  - "Comparison with another monitor or port"
  - "Patient assignment observed"
  - "End-to-end alarm verification"
  - "Final connectivity status"
---

## What This Guide Helps With
Troubleshoots loss of central monitoring or network communication caused by connections, network path, assignment, configuration, or infrastructure issues.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Alarm Surveillance
If the MX750 is not communicating with the Philips central monitoring environment, notify clinical staff and provide an alternate verified method of alarm surveillance before troubleshooting.

**Expected outcome:** The patient remains locally monitored and clinically significant alarms are observed despite the communication interruption.

### 2. Confirm the Scope of the Communication Failure
Determine whether only one MX750 is affected, multiple monitors in the same room or unit are affected, the device is missing from the central station, or data is present but incomplete. Record displayed network or connectivity messages exactly.

**Expected outcome:** The failure is categorized as device-specific, room-specific, unit-wide, or infrastructure-related.

### 3. Verify Local Monitor Operation
Confirm that the MX750 itself is operating normally and acquiring patient parameters locally. A network problem should be separated from a local measurement failure.

**Expected outcome:** Local monitoring remains functional. If local monitoring is also abnormal, troubleshoot the monitor or measurement issue separately.

### 4. Inspect Physical Network Connections
For wired configurations, inspect the approved network cable, wall jack, docking connection, intermediate external hardware, and accessible connectors for looseness or damage. Reseat connections as appropriate.

**Expected outcome:** Physical connections are secure and indicators, where available, show normal network activity. If communication returns, proceed to verification.

### 5. Substitute a Known-Good Network Cable or Approved Connection
Use a known-good approved network cable or another verified equivalent connection when practical.

**Expected outcome:** The monitor reconnects using the known-good path. If the failure follows the original cable, replace that cable.

### 6. Compare With Another Device or Network Port
Determine whether another verified monitor communicates correctly from the same location or whether the affected MX750 communicates when connected through another approved network point.

**Expected outcome:** Testing separates a monitor-side issue from a room jack, switch path, VLAN, or broader network issue.

### 7. Verify Patient Assignment and Approved Configuration
Confirm that the device is assigned to the expected location or central monitoring context and that no recent authorized configuration, room move, or equipment exchange occurred. Do not change protected network or service settings without authorization.

**Expected outcome:** The monitor's approved assignment and configuration match the intended clinical location.

### 8. Coordinate With Network or Clinical Systems Support
If multiple devices are affected or testing points to the network infrastructure, provide the appropriate support team with the affected rooms, ports, devices, time of failure, and comparison results.

**Expected outcome:** Infrastructure-related problems are escalated with enough information to identify the affected network segment or central monitoring service.

### 9. Verify End-to-End Communication
After correction, confirm that the patient appears at the appropriate PIC iX central station, parameters update correctly, alarms are transmitted as intended, and patient/device association is correct.

**Expected outcome:** Local and central monitoring agree and alarm communication is restored. If so, troubleshooting is complete.

### 10. Escalate Persistent Device-Specific Communication Failure
If known-good cabling, ports, assignments, and infrastructure have been verified but the MX750 still does not communicate, stop external troubleshooting.

**Expected outcome:** The monitor is removed from network-dependent clinical service and referred for qualified evaluation.

## If the Problem Persists
Common external connectivity and infrastructure causes have been ruled out. The remaining issue may involve device network hardware, docking communications, configuration, software, authentication, central system integration, or another service-level problem.

The affected equipment should be:
- Removed from service when central connectivity is required for safe use
- Labeled Out of Service when appropriate
- Sent for repair or bench evaluation if device-specific
- Evaluated using appropriate Philips and facility network documentation
- Configured or repaired only by authorized qualified personnel

Following repair or configuration correction, verify the entire path from bedside parameters through the central station, including alarm communication and correct patient association. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
A bedside monitor displaying normally does not confirm that central-station alarms are being received; verify the complete communication path.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Maintain local alarm surveillance, establish whether the failure is device-specific or infrastructure-wide, verify the physical network path before changing configuration, and document end-to-end central communication after correction.

That is successful troubleshooting.
