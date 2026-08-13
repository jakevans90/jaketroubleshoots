---
schemaVersion: 1
title: "GE Healthcare B105 / B125 / B155 Series Patient Monitor - Network or Central Station Communication Failure"
issueTitle: "Network or Central Station Communication Failure"
description: "Troubleshoots loss of central monitoring, network disconnection, cabling, infrastructure, configuration, location-specific faults, and communication-path problems."
assetType: "Patient Monitor"
manufacturer: "GE Healthcare"
model: "B105 / B125 / B155 Series"
slug: "ge-healthcare-b105-b125-b155-series-network-or-central-station-communication-failure"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that the B125 monitor was operating normally at bedside but was no longer visible at the central station."
  cause: "Clinical Engineering found the external network cable had a damaged locking tab and the connection was intermittently opening."
  resolution: "Replaced the network cable, verified stable bedside connectivity, confirmed correct waveforms and alarm communication at the central station, and returned the monitor to service."
helpfulDetails:
  - "Bedside monitor local status"
  - "Exact network indication"
  - "Central-station symptom"
  - "Wired or wireless connection"
  - "Network cable condition"
  - "Wall port or connection tested"
  - "Known-good cable result"
  - "Whether nearby monitors were affected"
  - "Approved configuration observed"
  - "Central-station recognition"
  - "Alarm communication test"
  - "Results before and after correction"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots loss of central monitoring, network disconnection, cabling, infrastructure, configuration, location-specific faults, and communication-path problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Alarm Surveillance
If the bedside monitor is not communicating with the central station or required networked alarm destination, ensure staff understand that central surveillance may be unavailable.

Provide an alternate verified monitoring and alarm-observation method as required by clinical workflow.

Do not assume bedside monitoring alone provides equivalent central alarm coverage.

**Expected outcome:** Patient monitoring and alarm surveillance remain clinically appropriate while communication is unavailable.

### 2. Confirm the Exact Communication Failure
Determine whether:
- The monitor is absent from the central station
- Waveforms or numerics are missing centrally
- Communication is intermittent
- The monitor indicates loss of network connectivity
- Only one bedside monitor is affected
- Multiple monitors or an entire area are affected
- The problem started after a move, network change, or equipment replacement

**Expected outcome:** The scope and direction of the communication failure are understood.

### 3. Verify Bedside Monitor Operation
Confirm the monitor itself is powered and locally displaying the expected patient parameters and alarms.

A local monitoring failure should be addressed before network troubleshooting.

**Expected outcome:** The bedside monitor is functioning normally apart from network or central-station communication.

### 4. Inspect External Network Connections
For wired connections, inspect accessible network cables, wall connections, couplers, and monitor-side connections for:
- Loose connectors
- Broken latches
- Damaged cable jackets
- Bent or contaminated ports
- Unapproved adapters

Reseat external cables.

For wireless configurations, confirm that the expected wireless communication state is present without making unauthorized network changes.

**Expected outcome:** The physical communication path is securely connected and free of obvious damage.

If reseating or replacing a damaged external cable restores communication, proceed to end-to-end verification.

### 5. Use a Known-Good Cable or Port Comparison
When authorized, substitute a known-good compatible network cable.

If infrastructure policy permits, compare operation at a verified working network connection in the same approved clinical environment.

Do not move network devices between ports arbitrarily or alter switch configurations.

**Expected outcome:** The fault is separated between the monitor/cable and the network connection.

If the monitor communicates normally through a known-good external path, escalate the original port or infrastructure issue to the appropriate network team.

### 6. Determine Whether the Problem Is Device-Specific or Area-Wide
Check whether nearby networked monitors are communicating normally.

A failure affecting multiple monitors suggests infrastructure, central-station, network-service, or system-level causes rather than simultaneous bedside monitor failures.

**Expected outcome:** The scope of the outage is identified.

If multiple devices are affected, follow the facility escalation process for monitoring-network or central-station outages.

### 7. Verify Approved Network Configuration
Review only configuration fields that Clinical Engineering is authorized to inspect.

Confirm that expected network identity, location, bed assignment, central-station association, or other required configuration has not obviously been changed.

Do not guess configuration values or copy settings from another monitor without verifying they are correct for that device and location.

**Expected outcome:** The monitor has the approved configuration required for its network role.

If an authorized configuration correction restores communication, proceed to end-to-end verification.

### 8. Check Central Station Recognition
At the receiving system, determine whether the bedside device:
- Appears but is disconnected
- Is assigned incorrectly
- Is visible without data
- Is entirely absent
- Reconnects intermittently

Coordinate with the appropriate clinical systems, IT, or network support team when central-station or infrastructure access is outside Clinical Engineering scope.

**Expected outcome:** The communication failure is localized to the bedside device, network path, or receiving system.

### 9. Perform an End-to-End Communication Test
After any correction, verify the complete path from bedside monitor to required receiving station.

Confirm:
- Monitor is connected
- Correct bed/device appears centrally
- Expected waveforms and numerics arrive
- Disconnect/reconnect status clears appropriately
- Alarm communication functions according to the facility's approved verification process

**Expected outcome:** The intended bedside-to-central communication path is fully restored.

If all required central monitoring functions are verified, troubleshooting can stop.

### 10. Escalate an Unresolved Communication Failure
If cabling, approved configuration, and local device operation are normal but communication remains unavailable, stop external troubleshooting and escalate appropriately.

Do not perform unauthorized switch, server, VLAN, network-security, or protected central-station configuration changes.

**Expected outcome:** The unresolved issue is assigned to the appropriate Clinical Engineering, clinical systems, IT, network, or manufacturer support resource.

## If the Problem Persists

External connections, device operation, basic approved configuration, and local comparisons have been checked. Remaining causes may involve monitor network hardware, central-station configuration, network infrastructure, switch or port configuration, server services, security controls, or other system-level communication functions.

The affected monitor should be:

- Removed from network-dependent clinical use if required alarm or monitoring communication cannot be assured
- Labeled Out of Service when the monitor itself is suspected
- Sent for repair or bench evaluation when appropriate
- Evaluated using appropriate GE Healthcare documentation and approved network test methods
- Configured or repaired only by qualified personnel

Infrastructure issues should be escalated to the responsible support team while clinical staff maintain an alternate surveillance plan.

Return the device to network-dependent service only after the complete communication and alarm path is verified.

Knowing when a failure belongs to infrastructure rather than the bedside monitor is proper troubleshooting.

## Clinical Use Tip

After restoring connectivity, verify the correct patient or bed appears at the intended central station; a network link alone does not prove the monitoring path is correct.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**




## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain a safe alarm-surveillance plan, verify the physical and logical communication path before assuming a monitor failure, separate device-specific problems from infrastructure outages, and confirm end-to-end central monitoring before return to service.

That is successful troubleshooting.
