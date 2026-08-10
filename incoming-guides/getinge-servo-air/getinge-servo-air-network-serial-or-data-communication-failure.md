---
schemaVersion: 1
title: "Getinge Servo-air Ventilator - Network, Serial, or Data Communication Failure"
issueTitle: "Network, Serial, or Data Communication Failure"
description: "Addresses lost device communication caused by cables, ports, network infrastructure, interface equipment, configuration, or downstream system availability."
assetType: "Ventilator"
manufacturer: "Getinge"
model: "Servo-air"
slug: "getinge-servo-air-network-serial-or-data-communication-failure"
dateAdded: "2026-08-10"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Servo-air was operating normally but no ventilator data appeared in the connected monitoring system."
  cause: "Clinical Engineering found a damaged external network cable between the ventilator connection and the bedside interface."
  resolution: "Clinical Engineering replaced the cable, verified data transmission at the receiving system, confirmed normal ventilator operation, and returned the device to service."
helpfulDetails:
  - "Communication type"
  - "Receiving system affected"
  - "Local ventilator operation"
  - "Cable and connector condition"
  - "Port or link indicators"
  - "Known-good cable or port result"
  - "Configuration observed"
  - "Other devices affected or unaffected"
  - "End-to-end test result"
  - "Final device status"
---

Asset Type: Ventilator  
Manufacturer: Getinge  
Model: Servo-air

## What This Guide Helps With

Addresses lost device communication caused by cables, ports, network infrastructure, interface equipment, configuration, or downstream system availability.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Monitoring and Workflow

If ventilator data is required at a central station, EMR, integration system, or remote monitoring location, confirm clinical staff have an alternate method to monitor and document the patient before troubleshooting.

Do not allow a communication failure to create an unnoticed loss of clinical surveillance.

Expected outcome: Patient care continues safely despite the communication outage.

### 2. Confirm the Communication Failure

Determine exactly what is failing:

- Network connection
- Serial communication
- Device integration
- Central monitoring
- Data export
- Interface engine reception
- One-way or intermittent data flow

Confirm whether local ventilator operation remains normal.

Expected outcome: The communication path and scope of failure are clearly identified.

### 3. Inspect External Communication Cables

Check Ethernet, serial, interface, adapter, and other relevant external cables for secure connection, damage, bent connectors, strain, or improper routing.

Reseat accessible connections.

Expected outcome: Physical connections are secure. If communication returns and remains stable, troubleshooting can stop after end-to-end verification.

### 4. Check Link and Status Indicators

Observe applicable port, adapter, network, or integration-device indicators.

Compare with a functioning nearby system when useful.

Expected outcome: Link indicators are consistent with a functioning connection. Missing link at both ends suggests a cable, port, or infrastructure issue.

### 5. Substitute a Known-Good Cable or Port

When permitted, replace the external cable with a known-good equivalent or connect to a verified infrastructure port.

Avoid changing network configuration simply to test connectivity.

Expected outcome: Communication is restored with the known-good cable or port, identifying the external failed element.

### 6. Verify Normal Accessible Communication Configuration

Review user-accessible network or communication configuration and compare it with the expected approved configuration or a known-good device.

Do not alter protected addresses, integration parameters, or service-level settings without authorization.

Expected outcome: Device communication settings match the intended environment.

### 7. Check the Downstream System

Confirm whether the receiving system, bedside interface, device adapter, switch, serial converter, integration server, or clinical application is functioning for other devices.

Expected outcome: The failure is isolated to either the Servo-air side or the external infrastructure.

### 8. Perform an End-to-End Test

After correcting any cable, port, or configuration issue, verify data at the actual intended destination rather than relying only on a local link indication.

Expected outcome: Expected ventilator data reaches the receiving system consistently. Troubleshooting can stop after successful end-to-end verification.

### 9. Confirm Ventilator Operation Is Unaffected

Run appropriate functional and pre-use checks to ensure communication troubleshooting did not affect normal ventilator configuration or operation.

Expected outcome: Ventilation and alarms remain fully functional.

### 10. Escalate Unresolved Communication Failure

If known-good cables, ports, infrastructure, and approved configuration have been verified but communication remains unavailable, escalate to the appropriate Clinical Engineering, IT, integration, or manufacturer support group.

Expected outcome: The device is removed from the affected communication workflow until the complete path is restored and verified.

## If the Problem Persists

Common cable, port, interface, and infrastructure causes have been ruled out. The remaining issue may involve internal communication hardware, protected device configuration, software, network infrastructure, serial interface hardware, middleware, or downstream clinical systems.

If communication is required for safe intended use, remove the ventilator from service or restrict its use according to facility policy, label it appropriately, and send it for qualified evaluation. Use applicable Getinge documentation and authorized network/integration procedures.

Verify the complete data path and normal ventilator operation before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Always verify data at the receiving system; a link light at the ventilator does not prove that clinically useful data is reaching its destination.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Communication troubleshooting should follow the entire path from the ventilator to the receiving system, verifying external connections and infrastructure before assuming an internal device failure.

That is successful troubleshooting.
