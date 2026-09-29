---
schemaVersion: 1
title: "GE Healthcare NM/CT 870 CZT PET / CT System - System Will Not Power On or Complete Startup"
issueTitle: "System Will Not Power On or Complete Startup"
description: "System remains off, stops during startup, or fails to reach a ready state because of power, connection, peripheral, or environmental conditions."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "NM/CT 870 CZT"
slug: "ge-healthcare-nm-ct-870-czt-system-will-not-power-on-or-complete-startup"
dateAdded: "2026-09-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported the GE Healthcare NM/CT 870 CZT would power partially but would not complete startup."
  cause: "Clinical Engineering found an external workstation power connection was loose, preventing the operator console from initializing with the system."
  resolution: "Clinical Engineering secured the connection, completed a controlled restart, verified normal system readiness and functional checks, and returned the unit to service."
helpfulDetails:
  - "Exact startup message or screen state"
  - "Whether the entire system or one subsystem was unpowered"
  - "Recent facility power interruption"
  - "Outlet or power source verification"
  - "External cable and connector condition"
  - "Emergency-stop status"
  - "Workstation and peripheral status"
  - "Environmental or HVAC condition"
  - "Results after controlled restart"
  - "Final system readiness state"
---
## What This Guide Helps With

System remains off, stops during startup, or fails to reach a ready state because of power, connection, peripheral, or environmental conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Continuity of Care

Do not troubleshoot the NM/CT 870 CZT while a patient depends on the system for an active procedure. Safely end or transfer the examination as clinically appropriate, remove the patient from the equipment, and prevent further use until system readiness is confirmed.

Inspect for smoke, unusual odor, abnormal heat, liquid intrusion, or visible electrical damage. If any are present, disconnect or isolate power only when safe and remove the system from service.

**Expected outcome:** The patient is safe, the system is available for controlled troubleshooting, and no immediate electrical or environmental hazard is present. If a hazard is identified, stop troubleshooting and escalate.

### 2. Confirm the Exact Startup Failure

Ask staff what occurred immediately before the problem, including whether there was a facility power interruption, shutdown, software restart, maintenance activity, or unusual message.

Determine whether the entire system is unpowered or whether only a workstation, gantry subsystem, display, acquisition component, or peripheral failed to initialize. Record any displayed message exactly.

**Expected outcome:** The failure is narrowed to total power loss, incomplete startup, or a specific subsystem. If normal startup now completes, verify readiness and troubleshooting can stop.

### 3. Verify Facility Power Availability

Check that the system's normal power source is available and that accessible power disconnects, approved system switches, and associated room power controls are in their normal operating positions.

Verify the applicable receptacles or supplied power sources using approved methods when accessible to Clinical Engineering. Do not reset facility breakers repeatedly or operate electrical distribution equipment outside your authorization.

**Expected outcome:** Required facility power is present and stable. If a facility power problem is identified, involve Facilities or Electrical Services and stop device-level troubleshooting until power is restored.

### 4. Inspect External Power Connections

Inspect accessible power cords, plugs, strain reliefs, connectors, power strips or approved distribution components, and workstation power connections for looseness, damage, overheating, or disconnection.

Reseat only user-accessible or service-authorized external connections with power safely controlled.

**Expected outcome:** All accessible power connections are secure and undamaged. If correcting an external connection restores startup, complete functional verification and troubleshooting can stop.

### 5. Check External System Components Required for Startup

Verify that operator consoles, monitors, keyboards, mice, network-connected system components, and other required external peripherals are powered and connected.

A powered gantry with an unavailable console, or a powered workstation with an unavailable acquisition subsystem, may appear to staff as a complete startup failure.

**Expected outcome:** Required external components power normally and communicate as expected. If the system reaches its normal ready state, troubleshooting can stop after verification.

### 6. Verify Emergency and Safety Controls Are Restored

Inspect accessible emergency-stop or safety controls and verify none remain activated from a previous event. Restore controls only according to approved operating or service procedures and only after confirming the area is safe.

Do not bypass safety circuits.

**Expected outcome:** No external emergency or safety control is preventing startup. If restoring a legitimately activated control allows normal startup, verify system operation and troubleshooting can stop.

### 7. Perform One Controlled Restart When Appropriate

If there is no evidence of electrical damage, overheating, fluid intrusion, or unstable facility power, perform a normal controlled shutdown and restart using the approved system process.

Do not repeatedly cycle power when startup repeatedly stops at the same point.

**Expected outcome:** The system completes startup and reaches its normal ready condition. If it does, verify major functions before return to service and stop troubleshooting.

### 8. Verify Environmental Conditions

Check for blocked ventilation, excessive room temperature, water leaks, recent HVAC problems, construction dust, or other environmental conditions that could prevent equipment initialization.

Correct external environmental issues before attempting continued operation.

**Expected outcome:** The equipment environment supports normal operation without obvious ventilation or facility concerns.

### 9. Perform Final Functional Verification

After startup is restored, confirm the operator workstation, acquisition system, detectors, gantry, table, communications, and status indicators reach their expected ready states.

Perform appropriate manufacturer-required operational or quality checks before clinical use.

**Expected outcome:** The complete system initializes normally and passes required functional verification. The issue is resolved and troubleshooting can stop.

### 10. Escalate an Unresolved Startup Failure

If verified facility power, external connections, peripherals, controls, and environment are normal but startup still fails, stop external troubleshooting.

Do not proceed into internal power distribution, control electronics, system boards, or restricted service procedures without appropriate authorization and documentation.

**Expected outcome:** An unresolved system-level fault is appropriately removed from clinical use and referred for qualified service.

## If the Problem Persists

Common external power, connection, peripheral, safety-control, and environmental causes have been ruled out. The remaining problem may involve internal power distribution, startup sequencing, subsystem communication, computer hardware, control electronics, or service-level configuration.

The device should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or controlled bench/system evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

After corrective service, complete required operational, safety, and quality-control testing before returning the system to clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not leave a patient positioned on the imaging table while investigating an incomplete system startup.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient first, confirm facility power and external causes before assuming an internal failure, verify the complete system after correction, escalate appropriately when startup remains abnormal, and document the event clearly using CCR.

That is successful troubleshooting.
