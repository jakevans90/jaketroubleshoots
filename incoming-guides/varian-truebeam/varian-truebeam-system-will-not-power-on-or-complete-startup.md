---
schemaVersion: 1
title: "Varian TrueBeam Radiation Therapy System - System Will Not Power On or Complete Startup"
issueTitle: "System Will Not Power On or Complete Startup"
description: "TrueBeam does not power up, remains unavailable during startup, or stops before reaching a clinically ready state."
assetType: "Radiation Therapy System"
manufacturer: "Varian"
model: "TrueBeam"
slug: "varian-truebeam-system-will-not-power-on-or-complete-startup"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that the Varian TrueBeam powered on but did not complete startup or reach the ready condition."
  cause: "Clinical Engineering found an external workstation connection partially disconnected following a room equipment move."
  resolution: "Clinical Engineering secured the connection, restarted the system using the approved startup process, and verified normal startup and system readiness before return to clinical staff."
helpfulDetails:
  - "Exact startup message or condition"
  - "Point where startup stopped"
  - "Facility power status"
  - "Recent outage or power event"
  - "Status of accessible emergency stops and room interlocks"
  - "Workstation and display status"
  - "External cable and network condition"
  - "Results before and after restart"
  - "Final system status"
  - "Required return-to-service verification completed"
---
## What This Guide Helps With

TrueBeam does not power up, remains unavailable during startup, or stops before reaching a clinically ready state.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Treatment Continuity
Do not attempt troubleshooting while a patient depends on the system for treatment or positioning. Safely discontinue the treatment workflow, remove the patient when appropriate, and coordinate an alternate treatment plan with Radiation Oncology staff.

**Expected outcome:** No patient remains dependent on an unreliable or incompletely initialized system.

### 2. Confirm the Exact Startup Failure
Determine whether the entire system is unpowered or whether only a console, workstation, display, imaging subsystem, accessory, or other component failed to initialize. Record any visible messages and the last normal startup stage observed.

**Expected outcome:** The affected portion of the system and the point at which startup stops are clearly identified.

### 3. Verify Facility and System Power
Check accessible power indicators, approved disconnects or breakers that Clinical Engineering is authorized to inspect, workstation power, monitors, and supporting equipment. Look for evidence of a facility outage or recent power interruption.

Do not repeatedly reset breakers or bypass protective devices.

**Expected outcome:** Required external power sources are available and no accessible protective device is obviously tripped or abnormal. If normal power restoration resolves startup, troubleshooting can stop after verification.

### 4. Inspect External Connections and Peripheral Equipment
Inspect accessible power cords, network connections, workstation cables, monitors, input devices, and externally connected accessories for loose connectors, damage, or incomplete seating.

**Expected outcome:** External connections are secure and no damaged cable or accessory is preventing normal startup.

### 5. Check Safety and Room Conditions
Verify that accessible emergency-stop devices, room interlocks, doors, and other externally observable safety conditions are in their normal operating state. Do not bypass or defeat an interlock.

**Expected outcome:** No external safety condition is intentionally preventing system readiness.

### 6. Allow the Approved Startup Sequence to Complete
If power and external conditions are normal, perform only the normal operator-accessible restart or startup process permitted by facility policy and manufacturer documentation. Avoid repeated power cycling.

**Expected outcome:** The system completes startup and reaches its normal ready condition. If it does, proceed to functional verification and stop troubleshooting.

### 7. Verify Supporting Workstations and Communications
Confirm that associated workstations, displays, and network-dependent components have started normally and communicate as expected. Compare with another known operational system or infrastructure endpoint when appropriate.

**Expected outcome:** Required supporting components are online and communicating normally.

### 8. Perform Final Functional Verification
Before clinical use, verify that the system reaches the expected ready state, controls respond normally, required safety functions are available, and any facility-required pre-use or daily verification is successfully completed by the appropriate qualified personnel.

**Expected outcome:** The TrueBeam is fully operational and passes required return-to-service checks.

### 9. Stop and Escalate if Startup Remains Incomplete
If the system repeatedly fails startup, reports a persistent fault, loses power again, or cannot establish a safe ready state, discontinue further external troubleshooting.

**Expected outcome:** An unreliable system remains unavailable for patient treatment pending qualified service evaluation.

## If the Problem Persists

Common external power, connection, room-condition, and workstation causes have been ruled out. The remaining problem may involve internal power distribution, control electronics, safety interlocks, system communications, software initialization, or another service-level subsystem.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or appropriate on-site service evaluation
- Evaluated using current manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not return the system to treatment use until the underlying fault is corrected and all required functional, safety, imaging, and treatment-system verification has been completed by the appropriate qualified personnel.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A TrueBeam that has not completed startup normally should never be used for patient treatment simply because selected subsystems appear functional.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient first, verify external power and safety conditions before assuming an internal failure, and escalate when the system cannot achieve a dependable ready state. Clear CCR documentation should show exactly what was reported, found, corrected, and verified.

That is successful troubleshooting.
