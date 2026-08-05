---
schemaVersion: 1
title: "Masimo Rad-97 Pulse Oximeter - Wi-Fi Or Network Communication Failure"
issueTitle: "Wi-Fi Or Network Communication Failure"
description: "Loss of wireless or network communication caused by signal coverage, incorrect profiles, access restrictions, infrastructure, time settings, or interface configuration."
assetType: "Pulse Oximeter"
manufacturer: "Masimo"
model: "Rad-97"
slug: "masimo-rad-97-wi-fi-or-network-communication-failure"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Rad-97 monitored locally but no data appeared at the receiving station."
  cause: "Clinical Engineering found the monitor connected to an incorrect approved wireless profile after being moved from another department."
  resolution: "Applied the authorized department profile, confirmed stable Wi-Fi connection and current data at the receiving station, verified local alarms, and returned the device to service."
helpfulDetails:
  - "Network icon or displayed message"
  - "Local monitoring status"
  - "Rooms or coverage areas tested"
  - "Approved network profile"
  - "Date and time status"
  - "Wired cable or port tested"
  - "Known-good monitor comparison"
  - "Receiving system and destination"
  - "Device identity or patient association"
  - "End-to-end communication results"
---

## What This Guide Helps With

Loss of wireless or network communication caused by signal coverage, incorrect profiles, access restrictions, infrastructure, time settings, or interface configuration.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Clarify Monitoring Dependence

Confirm whether the Rad-97 is being used for local monitoring only or whether clinicians depend on central alarm or data communication.

If remote alarm visibility is required and communication is unavailable, provide another verified monitoring path before troubleshooting.

Expected outcome: The patient has a confirmed local and remote monitoring method as required.

### 2. Confirm the Exact Communication Failure

Determine whether the device cannot connect to Wi-Fi, connects without transmitting data, drops connection intermittently, or communicates in some rooms but not others.

Record visible network icons, messages, and the affected destination system.

Expected outcome: The communication problem is accurately defined.

### 3. Verify Local Monitoring Operation

Confirm that the Rad-97 continues to measure, display, and alarm locally.

A network problem must not be confused with a complete monitor malfunction.

Expected outcome: Local monitoring is either verified or the device is removed from service for a broader failure.

### 4. Check Location and Wireless Coverage

Move the device within the approved clinical area and compare network status with another known-good Rad-97 or approved wireless device.

Check whether the issue occurs near known coverage gaps, elevators, shielded rooms, or recently changed infrastructure.

Expected outcome: Communication returns in an area with verified coverage, indicating an infrastructure or location-related problem.

### 5. Verify the Correct Network Profile

Confirm that the active network, clinical profile, and destination configuration match an approved Rad-97 in the same department.

Do not enter credentials, change security settings, or modify protected network configuration without authorization.

Expected outcome: The device is using the approved network configuration.

### 6. Check Date and Time

Verify that the device date, time, and time zone are reasonable and aligned with facility systems.

Incorrect time may interfere with secure communication, data association, or event display.

Expected outcome: Time settings are correct or synchronized through the approved method.

### 7. Restart the Device and Recheck Connection

With monitoring transferred to another device, perform a normal restart.

Observe whether the Rad-97 reconnects automatically and resumes data communication.

Expected outcome: The network connection restores and remains stable. If communication is verified end to end, troubleshooting can stop.

### 8. Inspect External Network Connections

For any wired interface, inspect the cable, connector, wall port, adapter, or docking interface for damage, looseness, or incorrect connection.

Test with a known-good approved cable and verified active port when available.

Expected outcome: The device communicates through the verified connection.

### 9. Verify the Complete Data Path

Confirm that the receiving system identifies the correct device and patient context, receives current values, and displays alarms or data as intended.

Coordinate with clinical systems, networking, or interface teams when the Rad-97 is connected but data does not reach the destination.

Expected outcome: Current data is visible at the intended receiving system.

### 10. Isolate Device Versus Infrastructure Failure

Test another known-good Rad-97 in the same location and the affected Rad-97 in a known-good location.

Expected outcome: The comparison identifies whether the problem follows the monitor or remains with the room, network, or interface.

### 11. Perform Final Communication Verification

Confirm local monitoring, network status, correct device identity, current data transmission, alarm path where applicable, and stable communication after movement or restart.

Expected outcome: The complete communication path operates reliably.

### 12. Escalate an Unresolved Communication Failure

If the problem follows the Rad-97 after approved profile, time, coverage, cable, and port checks, remove it from the affected workflow.

Expected outcome: The unit is labeled Out of Service for network use and routed for qualified evaluation.

## If the Problem Persists

Common external causes including wireless coverage, incorrect location, network profile, date and time, cable condition, port status, and receiving-system availability have been ruled out.

The remaining cause may involve network hardware, certificates, device configuration, interface mapping, wireless infrastructure, or enterprise systems. Remove the device from service when network communication is required, label it Out of Service, and coordinate bench evaluation with Clinical Engineering, networking, cybersecurity, or clinical systems personnel.

Use manufacturer documentation and approved diagnostic methods. Only authorized personnel should change network or security configuration. Verify the entire monitoring and alarm path before return to service.

## Clinical Use Tip

A working local display does not confirm that alarms or data are reaching the central station; always verify the receiving endpoint.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Preserve patient monitoring, verify the full communication path from the device to the receiving system, rule out location and infrastructure causes first, and escalate configuration changes appropriately.

That is successful troubleshooting.
