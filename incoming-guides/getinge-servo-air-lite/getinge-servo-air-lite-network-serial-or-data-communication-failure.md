---
schemaVersion: 1
title: "Getinge Servo-air Lite Ventilator - Network, Serial, or Data Communication Failure"
issueTitle: "Network, Serial, or Data Communication Failure"
description: "Addresses communication loss caused by cables, external interfaces, infrastructure, ports, accessible configuration, or downstream monitoring and integration systems."
assetType: "Ventilator"
manufacturer: "Getinge"
model: "Servo-air Lite"
slug: "getinge-servo-air-lite-network-serial-or-data-communication-failure"
dateAdded: "2026-08-10"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Servo-air Lite was ventilating normally but no data was appearing at the connected clinical information system."
  cause: "Clinical Engineering found the external Ethernet cable had a damaged connector and would not maintain network link."
  resolution: "Clinical Engineering replaced the cable, verified stable network link and data at the receiving system, confirmed normal ventilator operation, and returned the device to service."
helpfulDetails:
  - "Communication type"
  - "Receiving system"
  - "Local device operation"
  - "Cable and connector condition"
  - "Link indicators"
  - "Known-good cable or port result"
  - "Configuration observed"
  - "Other equipment affected"
  - "End-to-end result"
  - "Final device status"
---

Asset Type: Ventilator
Manufacturer: Getinge
Model: Servo-air Lite

## What This Guide Helps With

Addresses communication loss caused by cables, external interfaces, infrastructure, ports, accessible configuration, or downstream monitoring and integration systems.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Monitoring and Documentation
If ventilator data is expected at a central monitoring system, EMR, or integration platform, confirm that staff have another method to monitor and document the patient while communication is unavailable.
Expected outcome: Patient care continues safely without relying on missing remote data.
### 2. Define the Failed Communication Path
Determine whether the problem involves Ethernet, serial data, device integration, central monitoring, export, middleware, or intermittent communication.
Confirm whether local Servo-air Lite ventilation and alarms remain normal.
Expected outcome: The failed portion of the communication workflow is identified.
### 3. Inspect Communication Cables and Connectors
Check Ethernet, serial, adapter, and interface cables for secure seating, visible damage, bent connectors, and strain.
Reseat accessible connections.
Expected outcome: Connections are secure. If communication returns and remains stable, proceed to end-to-end verification.
### 4. Observe Link and Status Indicators
Check applicable port, network, interface-adapter, or downstream connection indicators.
Compare with a nearby functioning setup when useful.
Expected outcome: Physical link status is consistent with proper connectivity.
### 5. Substitute Known-Good External Hardware
Replace the external communication cable with a known-good equivalent or connect to a verified infrastructure port when authorized.
Expected outcome: Restored communication identifies a cable or port problem.
### 6. Verify Approved Accessible Configuration
Review normal accessible network or serial configuration and compare it with the approved configuration for the location or a known-good device.
Do not alter protected network parameters or service settings without authorization.
Expected outcome: Configuration matches the intended communication environment.
### 7. Check External Infrastructure
Confirm whether the bedside integration hardware, network switch, serial converter, device adapter, interface engine, server, or receiving application is functioning for other equipment.
Expected outcome: The problem is isolated to the ventilator or the surrounding infrastructure.
### 8. Verify End-to-End Data Reception
After correction, verify that expected Servo-air Lite data appears at the actual destination system.
Do not consider link lights alone sufficient.
Expected outcome: Data is transmitted and received consistently. Troubleshooting can stop after successful end-to-end verification.
### 9. Verify Normal Ventilator Function
Complete appropriate functional and pre-use testing to confirm that communication troubleshooting did not alter ventilator operation.
Expected outcome: Local ventilation and alarms remain fully functional.
### 10. Escalate Unresolved Communication Failure
If cables, ports, infrastructure, and approved configuration are verified but communication remains unavailable, escalate to qualified Clinical Engineering, IT, integration, or manufacturer support personnel.
Expected outcome: The affected communication workflow remains out of service until the full path is restored and verified.

## If the Problem Persists

Common external cable, port, interface, and infrastructure causes have been ruled out. The remaining issue may involve internal communication hardware, protected configuration, software, integration equipment, middleware, or network infrastructure.
If the communication function is required for the device's intended clinical use, remove the Servo-air Lite from service or restrict use according to facility policy, label it appropriately, and send it for qualified evaluation.
Use appropriate Getinge documentation and authorized integration procedures. Verify end-to-end data transmission and normal ventilator operation before return to service.
Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Always verify the complete communication path at the receiving station or clinical system rather than assuming a connected cable means data is being delivered.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Troubleshoot communication as a complete path, starting with cables and infrastructure before assuming an internal device problem, and verify data where clinicians actually receive it.
That is successful troubleshooting.
