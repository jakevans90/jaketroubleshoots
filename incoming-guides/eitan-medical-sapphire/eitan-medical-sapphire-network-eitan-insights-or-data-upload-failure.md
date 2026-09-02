---
schemaVersion: 1
title: "Eitan Medical Sapphire Infusion Pump - Network, Eitan Insights, or Data Upload Failure"
issueTitle: "Network, Eitan Insights, or Data Upload Failure"
description: "Troubleshoots network or data-transfer failures caused by connectivity, registration, configuration, infrastructure, server availability, or device communication problems."
assetType: "Infusion Pump"
manufacturer: "Eitan Medical"
model: "Sapphire"
slug: "eitan-medical-sapphire-network-eitan-insights-or-data-upload-failure"
dateAdded: "2026-09-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported a Sapphire pump was not appearing in Eitan Insights and recent data was not uploading."
  cause: "Clinical Engineering found the pump was being used in an area with no functioning connection to the intended network."
  resolution: "Moved the pump to a verified network location, confirmed communication and data synchronization, and verified normal pump operation."
helpfulDetails:
  - "Exact communication symptom"
  - "Whether one or multiple pumps were affected"
  - "Device location"
  - "Network availability"
  - "External connection condition"
  - "Device registration or assignment"
  - "Result in another known-good location"
  - "Platform visibility"
  - "Upload or synchronization result"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots network or data-transfer failures caused by connectivity, registration, configuration, infrastructure, server availability, or device communication problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Separate Therapy From Connectivity
Do not interrupt active patient therapy solely to troubleshoot nonessential data connectivity.

If network communication is required for a critical clinical workflow and the pump cannot meet that requirement, follow facility contingency procedures.

**Expected outcome:** Patient therapy continues safely while the communication problem is evaluated.

### 2. Confirm the Exact Communication Failure
Determine whether the issue involves:

- Pump not connecting to the network
- Device not appearing in Eitan Insights
- Data not uploading
- Intermittent connectivity
- Delayed synchronization
- Only one pump affected
- Multiple pumps or locations affected

**Expected outcome:** The scope and failure pattern are defined.

### 3. Verify Basic Pump Operation
Confirm the pump powers on normally and otherwise performs its intended infusion functions.

A communication problem should be separated from a broader device startup or power failure.

**Expected outcome:** The device is otherwise operational. If basic device failure is also present, address that before network troubleshooting.

### 4. Inspect External Communication Hardware
If the installation uses cables, docks, adapters, access points, or related external equipment, inspect them for obvious disconnection or damage.

Reseat accessible external connections where appropriate.

**Expected outcome:** External communication hardware is securely connected. If restoring a loose connection resolves communication, troubleshooting can stop.

### 5. Verify Network Availability
Determine whether the expected network is functioning in the device's location.

Check whether other compatible devices in the same area are communicating normally.

**Expected outcome:** A local or system-wide infrastructure problem is identified or ruled out. If several devices are affected, escalate the network or platform issue rather than replacing individual pumps.

### 6. Confirm Device Assignment or Registration
Verify through authorized support workflows that the pump is correctly assigned, registered, or associated with the intended environment.

Do not alter protected network or security settings without authorization.

**Expected outcome:** The pump is correctly represented in the approved management platform.

### 7. Compare in Another Known-Good Location
When practical, test the pump in a location where similar devices are known to communicate normally.

This helps distinguish a device-specific problem from local wireless or network coverage issues.

**Expected outcome:** If communication works in the known-good area, the original location or infrastructure is the likely cause.

### 8. Verify Data Transfer Through the Approved Platform
Using authorized workflows, confirm whether the pump's expected status or data becomes visible after connectivity is restored.

Do not manually manipulate database records to force synchronization.

**Expected outcome:** The pump communicates and expected data becomes available. If so, troubleshooting can stop.

### 9. Perform Final Functional Verification
Verify the pump's normal operation after communication is restored and confirm that the network or platform connection remains stable.

If applicable, document successful upload or synchronization.

**Expected outcome:** Both infusion function and expected communication are reliable. If all required checks pass, troubleshooting can stop.

### 10. Escalate Persistent Communication Failure
If one pump remains unable to communicate while other comparable pumps function normally on the same infrastructure, stop external troubleshooting.

Do not open the pump, alter unauthorized network settings, or bypass security controls.

**Expected outcome:** The issue is escalated appropriately to qualified Clinical Engineering, IT, cybersecurity, platform support, or manufacturer service personnel.

## If the Problem Persists

External connections, network availability, location, assignment, and basic platform access have been ruled out. Remaining causes may involve device communication hardware, software, security configuration, wireless infrastructure, server-side services, or account/platform settings.

The device should be:

- Removed from service when connectivity is required for safe intended use
- Labeled Out of Service when appropriate
- Sent for bench evaluation if a device-specific fault is suspected
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Configured or repaired only by qualified personnel

Complete communication and functional verification before return to service when connectivity is part of the intended deployment.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

When checking network failures, confirm the complete communication path rather than assuming the pump is defective because data is missing from the remote platform.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter; optional explanatory prose may follow. -->



## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Connectivity troubleshooting should distinguish the pump from the infrastructure around it. Verify location, network availability, assignment, and external communication paths before assuming a device communication failure.

That is successful troubleshooting.
