---
schemaVersion: 1
title: "Smiths Medical Medfusion 3500 Infusion Pump - Wireless Network Connection or Server Communication Failure"
issueTitle: "Wireless Network Connection or Server Communication Failure"
description: "Troubleshoots wireless or server communication failures caused by signal, infrastructure, configuration, network availability, or device-side communication problems."
assetType: "Infusion Pump"
manufacturer: "Smiths Medical"
model: "Medfusion 3500"
slug: "smiths-medical-medfusion-3500-wireless-network-connection-or-server-communication-failure"
dateAdded: "2026-09-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that one Medfusion 3500 would not communicate with the pump server while other pumps remained connected."
  cause: "Clinical Engineering found the failure was location-specific and the same pump communicated normally in a verified wireless coverage area."
  resolution: "The wireless coverage issue was escalated to IT, pump communication was verified in a known-good location, and the device status was documented for appropriate clinical use."
helpfulDetails:
  - "Failed network-dependent function"
  - "Displayed network status"
  - "Physical location"
  - "Whether other pumps were affected"
  - "Known-good comparison result"
  - "Result after restart"
  - "Wireless infrastructure status"
  - "Server availability"
  - "End-to-end communication result"
  - "IT or vendor ticket reference"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots wireless or server communication failures caused by signal, infrastructure, configuration, network availability, or device-side communication problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Separate Networking From Infusion Safety
Do not interrupt an active infusion solely to troubleshoot network communication unless the communication failure creates a clinical safety concern. If the pump itself is otherwise unreliable, transfer therapy to another verified device before testing.

**Expected outcome:** Patient therapy continues safely while communication troubleshooting is performed appropriately.

### 2. Confirm the Exact Communication Failure
Determine what function is unavailable: wireless association, server connection, data transfer, configuration distribution, status reporting, or another network-dependent feature. Record any displayed network status or message.

**Expected outcome:** The failed communication stage is clearly identified.

### 3. Check Whether the Problem Is Device-Specific
Compare the affected pump with another known-good Medfusion 3500 in the same area. Determine whether other pumps or network-connected medical devices are experiencing similar communication problems.

**Expected outcome:** The problem is narrowed to one pump, one location, or broader infrastructure.

### 4. Check Physical Location and Signal Environment
Move the pump within the normal approved clinical coverage area if appropriate and determine whether communication changes by location. Consider known wireless dead zones, shielded rooms, recent construction, or environmental changes.

**Expected outcome:** Communication remains stable in a known-good coverage area or a location-dependent issue is identified.

### 5. Verify Normal Device Network Status
Review only the network information available through authorized normal or service-approved interfaces. Confirm that the pump is intended to participate in the facility's wireless environment and has not been assigned to the wrong clinical or network configuration.

**Expected outcome:** The pump's expected network assignment is confirmed.

### 6. Restart the Pump When Safe
With the pump removed from patient use, perform a normal restart and observe whether it reconnects automatically. Do not clear network configuration or reset protected settings without authorization.

**Expected outcome:** The pump starts normally and reconnects, or the communication failure remains reproducible.

### 7. Verify Infrastructure Availability
Coordinate with IT or the responsible network team to confirm that the applicable wireless network, authentication services, servers, interfaces, and required communication paths are available.

**Expected outcome:** Infrastructure required for communication is confirmed operational or an external outage is identified.

### 8. Compare Network Behavior With a Known-Good Pump
Place a known-good pump in the same location and compare its connectivity. If appropriate, move the affected pump to a location where the known-good pump communicates successfully.

**Expected outcome:** The comparison distinguishes infrastructure coverage from a pump-specific communication problem.

### 9. Verify End-to-End Communication
After correcting the identified cause, verify the complete intended communication path rather than relying only on a wireless icon or local connection indicator. Confirm the expected server-side or application-side result when applicable.

**Expected outcome:** The pump communicates successfully through the complete required system. If verified, troubleshooting can stop.

### 10. Escalate Persistent Device-Specific Failures
If infrastructure is operational and known-good pumps communicate normally while the affected unit does not, remove or restrict the pump from workflows requiring connectivity and escalate for qualified evaluation.

**Expected outcome:** A device with unresolved network functionality is not returned to a workflow that depends on that communication.

## If the Problem Persists

External coverage, infrastructure availability, device assignment, startup, and comparison testing have been completed. Remaining causes may involve wireless hardware, network configuration, certificates or credentials managed by authorized systems, device software, server configuration, or other service-level issues.

The device should be:

- Removed from service when communication is required for safe intended use
- Labeled Out of Service when appropriate
- Sent for repair or bench evaluation if device-specific
- Evaluated using appropriate manufacturer documentation and approved network tools
- Repaired or configured only by qualified personnel

After correction, verify the entire communication path and basic pump operation before return to service. Knowing when to involve IT, system administration, or manufacturer support is proper troubleshooting.

## Clinical Use Tip

A wireless connection indicator alone does not prove successful integration; verify the complete pump-to-server communication path when that connection supports clinical workflow.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Failed network-dependent function
- Displayed network status
- Physical location
- Whether other pumps were affected
- Known-good comparison result
- Result after restart
- Wireless infrastructure status
- Server availability
- End-to-end communication result
- IT or vendor ticket reference
- Final device status

## Final Thought

Separate pump operation from network infrastructure, compare against a known-good device, and verify the complete communication path. Escalate device-specific or infrastructure problems to the appropriate qualified team.

That is successful troubleshooting.
