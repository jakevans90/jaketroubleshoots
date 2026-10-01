---
schemaVersion: 1
title: "Elekta Versa HD Radiation Therapy System - System Will Not Power On or Complete Startup"
issueTitle: "System Will Not Power On or Complete Startup"
description: "Versa HD does not power on, remains partially initialized, or cannot complete startup because of external power, interlock, peripheral, or communication conditions."
assetType: "Radiation Therapy System"
manufacturer: "Elekta"
model: "Versa HD"
slug: "elekta-versa-hd-system-will-not-power-on-or-complete-startup"
dateAdded: "2026-10-01"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that the Elekta Versa HD powered partially but would not complete startup or enter a treatment-ready state."
  cause: "Clinical Engineering found an external workstation connection was loose, preventing the affected system component from initializing correctly."
  resolution: "Clinical Engineering secured the connection, completed an approved restart, verified normal system initialization, and confirmed required functions before return to service."
helpfulDetails:
  - "Exact point at which startup stopped"
  - "Displayed messages or indicators"
  - "Components that did and did not power on"
  - "Recent power outage or electrical work"
  - "Emergency-stop status"
  - "Facility power condition"
  - "External cable condition"
  - "Network or infrastructure status"
  - "Results before and after restart"
  - "Final return-to-service status"
---
## What This Guide Helps With

Versa HD does not power on, remains partially initialized, or cannot complete startup because of external power, interlock, peripheral, or communication conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Clinical Use

Do not continue treatment or troubleshoot the system while a patient depends on it. If a patient is positioned for treatment, follow departmental procedures to safely remove the patient from the treatment position and maintain continuity of care.

Check for smoke, unusual odor, excessive heat, fluid intrusion, visible damage, or other immediate hazards.

**Expected outcome:** The patient is safe, the equipment is not being used clinically, and no immediate electrical or mechanical hazard is present. If a hazard exists, remove the system from service and stop troubleshooting.

### 2. Confirm the Exact Startup Failure

Determine whether the system is completely without power or whether only part of the Versa HD environment has failed to start. Note which consoles, displays, workstations, gantry indicators, treatment controls, or peripheral devices are powered.

Record any displayed messages or abnormal startup behavior exactly as observed.

**Expected outcome:** The failure is narrowed to total loss of power, partial startup, or a specific subsystem that is not becoming ready.

### 3. Verify Facility Power

Verify that applicable room power, disconnects, breakers, emergency power arrangements, and accessible power connections appear normal. Check whether other equipment supplied from the same electrical area is operating normally.

Do not reset facility electrical protection repeatedly if it trips again.

**Expected outcome:** Required facility power is available and stable. If an upstream electrical problem is identified, correct or escalate that condition before troubleshooting the Versa HD further.

### 4. Check Accessible Power and Emergency Controls

Inspect accessible power switches, emergency-off controls, and system enable controls for their normal operating state. Verify that an emergency-stop or room emergency control has not been activated.

Do not bypass or defeat any safety circuit.

**Expected outcome:** Accessible power and emergency controls are in their intended operating state. If restoring a legitimately activated external control permits normal startup, verify full system operation before stopping troubleshooting.

### 5. Inspect External Connections and Peripherals

Inspect accessible workstation power cords, network connections, peripheral cables, monitors, keyboards, control interfaces, and other external connections for looseness or obvious damage.

Reseat only connections intended for routine external service access and only when the system is safely powered down where required.

**Expected outcome:** External connections are secure and undamaged. A loose external connection that restores normal startup identifies a correctable external cause.

### 6. Verify Room and Infrastructure Conditions

Check for recent utility interruptions, electrical work, network outages, HVAC problems, equipment relocation, or other room infrastructure events that could affect startup.

Verify that room temperature and ventilation appear normal and that equipment ventilation openings are unobstructed.

**Expected outcome:** No unresolved environmental or infrastructure condition is preventing initialization.

### 7. Perform an Approved Restart if Appropriate

If no hazard is present and site procedures permit, perform a normal system shutdown and restart using the approved operating sequence. Do not repeatedly cycle power in an attempt to clear a persistent fault.

Observe which component fails to initialize.

**Expected outcome:** The Versa HD completes its normal startup sequence. If it does, continue with required functional and safety verification before clinical use.

### 8. Verify System Readiness

After successful startup, confirm that operator workstations, treatment controls, positioning systems, imaging components, communication paths, and safety indicators reach their normal ready state.

Do not return the system to clinical service based solely on the fact that it powers on.

**Expected outcome:** All required system functions initialize normally and no unresolved fault remains. Troubleshooting can stop after required return-to-service verification is completed.

### 9. Escalate an Unresolved Startup Failure

If the system remains unable to complete startup after external power, controls, connections, infrastructure, and approved restart checks are completed, stop troubleshooting.

**Expected outcome:** The system is removed from clinical service and referred for qualified service evaluation rather than subjected to deeper unauthorized troubleshooting.

## If the Problem Persists

Common external causes have been ruled out. The remaining problem may involve internal power distribution, safety circuitry, system controllers, inter-system communications, startup configuration, or another service-level condition.

The Versa HD should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or qualified service evaluation.
- Evaluated using appropriate Elekta documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Do not perform internal board-level repair, defeat interlocks, or make undocumented configuration changes. Following repair, complete applicable functional, safety, imaging, and treatment-system verification before return to clinical service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Do not attempt to recover a startup problem while a patient remains positioned for treatment; establish a safe clinical plan before technical troubleshooting begins.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient first, determine whether the failure is global or limited to one subsystem, verify external power and connections before assuming internal failure, and escalate persistent startup faults with complete CCR documentation.

That is successful troubleshooting.
