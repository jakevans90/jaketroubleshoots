---
schemaVersion: 1
title: "Siemens Healthineers Biograph Vision PET / CT System - Detector or Acquisition Hardware Is Not Ready"
issueTitle: "Detector or Acquisition Hardware Is Not Ready"
description: "Use this guide when PET or CT acquisition hardware remains unavailable, not ready, or fails initialization because of startup, connection, environmental, or subsystem-readiness conditions."
assetType: "PET / CT System"
manufacturer: "Siemens Healthineers"
model: "Biograph Vision"
slug: "siemens-healthineers-biograph-vision-detector-or-acquisition-hardware-is-not-ready"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Biograph Vision remained unavailable for scanning because the acquisition subsystem would not reach ready status."
  cause: "Clinical Engineering found an accessible external communication cable loose following nearby equipment service."
  resolution: "Clinical Engineering secured the connection, restarted the system normally, verified stable acquisition readiness, and completed functional verification before return to service."
helpfulDetails:
  - "PET, CT, or both affected"
  - "Exact readiness message"
  - "Whether failure occurred during startup or scanning"
  - "Recent outage or service activity"
  - "External cable condition"
  - "Room cooling status"
  - "Result of controlled restart"
  - "Whether readiness was stable or intermittent"
  - "Quality-check result"
  - "Final system status"
---
## What This Guide Helps With

Use this guide when PET or CT acquisition hardware remains unavailable, not ready, or fails initialization because of startup, connection, environmental, or subsystem-readiness conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Clinical Acquisition Attempts

Do not continue attempting patient scans when required detector or acquisition hardware is not ready.

Move the patient to a safe condition and arrange alternate imaging when clinically necessary.

**Expected outcome:** No patient examination depends on unreliable acquisition hardware.

If acquisition readiness cannot be established, the system remains out of clinical use.

### 2. Confirm the Exact Not-Ready Condition

Identify:

- Whether PET, CT, or both acquisition paths are affected.
- The exact displayed status or message.
- Whether the problem occurred at startup or during a study.
- Whether the subsystem was ever ready after startup.
- Whether a recent restart, outage, calibration, or service event preceded the issue.

**Expected outcome:** The affected acquisition subsystem and sequence of events are documented.

If the subsystem transitions normally to ready and remains stable during verification, proceed to final functional testing.

### 3. Verify Complete System Startup

Confirm that the Biograph Vision has completed its normal startup sequence and that no other major system subsystem remains offline.

A detector or acquisition-not-ready indication may be secondary to incomplete system initialization.

**Expected outcome:** The scanner, workstation, and required supporting subsystems have completed normal startup.

If waiting for a legitimate startup sequence to complete resolves the condition and the system remains stable, verify operation and stop.

### 4. Inspect Accessible External Connections

Check accessible external cables and connectors related to operator consoles, acquisition peripherals, or externally connected system components.

Look for:

- Loose connectors.
- Accidentally disconnected cables.
- Damaged cabling.
- Recent room or service activity that may have disturbed a connection.

Do not open detector electronics, gantry covers, or internal equipment cabinets.

**Expected outcome:** Accessible external acquisition-related connections are secure and undamaged.

If restoring an obvious external connection returns the subsystem to ready, complete final verification and stop.

### 5. Check Environmental Conditions

Confirm that the equipment room and scanner environment do not show obvious signs of:

- Excessive temperature.
- Ventilation obstruction.
- Cooling interruption.
- Water intrusion.
- Facility HVAC failure.
- Recent room utility problems.

Detector and acquisition systems may remain inhibited if environmental conditions are not acceptable.

**Expected outcome:** No external environmental condition is preventing acquisition readiness.

If environmental restoration returns the hardware to a stable ready state, verify operation and stop.

### 6. Review System Status Without Changing Service Configuration

Use normal operator-accessible status information to identify whether another subsystem or prerequisite is preventing readiness.

Do not:

- Enter restricted service menus.
- Clear faults by altering calibration data.
- Modify detector configuration.
- Bypass initialization checks.

**Expected outcome:** Any operator-visible prerequisite or related fault is identified without altering protected settings.

If correcting a normal operating-state issue restores acquisition readiness, verify the system and stop.

### 7. Perform One Controlled Restart if Appropriate

If no hazard exists and the system can be shut down normally, perform one approved controlled restart.

Avoid repeated power cycling if the same acquisition hardware remains unavailable.

**Expected outcome:** All required detector and acquisition subsystems initialize and report ready after startup.

If readiness is restored and remains stable, proceed to final verification and stop.

### 8. Verify Consistent Ready State

Allow the system to remain in its normal ready condition and confirm that the affected subsystem does not immediately drop offline or return to not-ready status.

**Expected outcome:** The acquisition subsystem remains stable and ready without recurring faults.

If readiness is intermittent, remove the system from service and escalate even if it temporarily recovers.

### 9. Perform Final Functional Verification

Before release, confirm:

- PET and CT subsystem readiness as applicable.
- No unresolved acquisition faults.
- Required acquisition controls respond.
- Appropriate approved test or quality check completes when required.
- No new image-quality or communication concern is introduced.

**Expected outcome:** Acquisition hardware is stable, ready, and passes required verification.

If all checks pass, troubleshooting is complete.

### 10. Escalate Persistent Acquisition Hardware Faults

If detector or acquisition hardware remains unavailable after startup, environmental, connection, and normal system-state checks, stop external troubleshooting.

**Expected outcome:** The system is removed from clinical service and referred for qualified technical evaluation.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve internal detector electronics, acquisition controllers, timing or synchronization systems, internal communication, internal power distribution, cooling, calibration data, or another service-level condition.

The device should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or qualified system evaluation.
- Evaluated using appropriate Siemens Healthineers documentation and approved test equipment.
- Repaired, calibrated, or configured only by qualified personnel.

Do not open detector assemblies or attempt board-level diagnosis.

Return to clinical use only after acquisition readiness, required quality checks, and appropriate functional verification have passed.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A detector that briefly returns to ready but repeatedly drops offline should not be considered reliable enough for patient imaging.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient, confirm complete startup and simple external causes first, avoid assuming an internal detector failure prematurely, and escalate any acquisition subsystem that cannot demonstrate stable readiness.

That is successful troubleshooting.
