---
schemaVersion: 1
title: "GE Healthcare Discovery MI PET / CT System - System Will Not Power On or Complete Startup"
issueTitle: "System Will Not Power On or Complete Startup"
description: "Troubleshoots loss of power, incomplete startup, startup hangs, and external power, interlock, peripheral, or environmental conditions preventing normal readiness."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "Discovery MI"
slug: "ge-healthcare-discovery-mi-system-will-not-power-on-or-complete-startup"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Imaging staff reported that the GE Discovery MI would not complete startup and remained unavailable for patient scanning."
  cause: "Clinical Engineering found an accessible system power connection not fully seated after recent equipment activity in the room."
  resolution: "Clinical Engineering secured the connection, restarted the system normally, verified complete startup and subsystem readiness, and confirmed the scanner passed applicable return-to-service checks."
helpfulDetails:
  - "Exact point where startup stopped"
  - "Messages displayed"
  - "Components with or without power"
  - "Recent outage or electrical work"
  - "Emergency-control status"
  - "Facility power status"
  - "Room temperature or cooling condition"
  - "External cable condition"
  - "Results of controlled restart"
  - "Final PET / CT readiness status"
---
## What This Guide Helps With
Troubleshoots loss of power, incomplete startup, startup hangs, and external power, interlock, peripheral, or environmental conditions preventing normal readiness.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Continuity of Care

Do not troubleshoot an unreliable PET / CT system while a patient depends on it. Stop the examination, safely remove the patient from the system when appropriate, and redirect clinical care according to department procedures.

Check for smoke, unusual odor, overheating, liquid intrusion, visible electrical damage, or abnormal sounds. If any are present, disconnect or isolate power only when safe and remove the system from service.

**Expected outcome:** The patient is safe, the system is not being used clinically, and no immediate electrical or mechanical hazard is present.

If a hazardous condition is identified, troubleshooting is complete. Keep the system out of service and escalate for repair.

### 2. Confirm the Exact Startup Failure

Ask staff what occurred before the failure and determine whether the entire system is unpowered or whether specific components are failing to initialize.

Observe:

- Operator workstation status
- Gantry indicators or displays
- Table status
- PET / CT subsystem readiness
- Any visible messages
- Whether startup stops consistently at the same point

Record the exact message or observed behavior rather than relying on a general report that the scanner "will not start."

**Expected outcome:** The affected portion of the startup sequence is clearly identified.

### 3. Verify Facility Power

Confirm that the scanner area has normal facility power and that no known outage, transfer event, electrical work, or emergency-power event occurred.

Check accessible facility disconnects, emergency-off controls, and power distribution indicators only within Clinical Engineering responsibilities. Do not reset breakers or facility electrical protection repeatedly.

If power availability is uncertain, involve Facilities or qualified electrical personnel.

**Expected outcome:** Required facility power is available and there is no unresolved building electrical condition.

If facility power restoration returns the system to normal operation and startup completes successfully, troubleshooting can stop after functional verification.

### 4. Check Accessible Power Connections and Emergency Controls

Inspect accessible external power connections and controls for:

- Loose or disconnected cables
- Damaged plugs or receptacles
- Activated emergency-stop or emergency-off controls
- Evidence that a safety control was recently used
- Physical damage around power interfaces

Reset an emergency control only after determining why it was activated and confirming that doing so is safe.

**Expected outcome:** External power connections are secure and no safety control is unintentionally preventing startup.

If correcting an external power or emergency-control condition allows normal startup, proceed to final verification.

### 5. Verify Room and Support Infrastructure

Check whether room-support systems required for scanner operation appear normal, including environmental cooling and any facility services monitored by the department.

Look for:

- Excessive room temperature
- Cooling alarms
- Water leaks
- Facility maintenance activity
- Network or infrastructure outages occurring at the same time

Do not bypass environmental or safety protections.

**Expected outcome:** The operating environment and required support infrastructure are available.

### 6. Inspect External Peripheral Connections

Check accessible connections between major external components such as the operator console, displays, approved peripherals, network interfaces, and system communication cables.

Look for disconnected, partially seated, damaged, or recently disturbed connections. Do not disconnect high-voltage, internal gantry, or restricted service connections.

**Expected outcome:** Accessible system and peripheral connections are secure and undamaged.

### 7. Perform an Approved Controlled Restart

If no hazardous condition exists and local policy permits, perform a normal system shutdown and restart using approved operator-accessible controls or established manufacturer procedures.

Do not repeatedly cycle power if the system consistently fails at the same stage.

**Expected outcome:** The Discovery MI completes startup, initializes required subsystems, and reaches its normal ready state.

If startup completes normally and remains stable, troubleshooting can stop after final verification.

### 8. Verify System Readiness Before Clinical Use

Confirm that:

- Operator controls respond normally
- Gantry and table indicate normal readiness
- PET / CT acquisition components report ready
- No unresolved warning or fault remains
- Required network functions are available
- Any required system checks can be completed normally

Perform applicable return-to-service testing according to department and manufacturer requirements.

**Expected outcome:** The scanner completes startup and is safe and functional for intended clinical operation.

If all required checks pass, the device may be returned to service.

## If the Problem Persists

If the Discovery MI still will not power on or complete startup after external power, emergency controls, connections, environment, and approved restart procedures are verified, common external causes have been ruled out.

The remaining cause may involve internal power distribution, startup sequencing, subsystem communication, computer hardware, safety interlocks, cooling infrastructure, or another service-level condition.

The system should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or formal system evaluation
- Evaluated using appropriate GE Healthcare service documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not repeatedly cycle power, bypass interlocks, or enter restricted service functions in an attempt to force startup.

After corrective service, complete all required functional, safety, and manufacturer-defined return-to-service checks before releasing the scanner.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Ensure the patient is safely removed from the scanner and an alternate imaging plan is established before troubleshooting an unreliable startup condition.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Start with patient safety, confirm what actually failed, and rule out power, emergency controls, connections, environment, and other external causes before suspecting internal hardware. Verify normal operation before return to service and document the complaint, cause, and resolution clearly.

That is successful troubleshooting.
