---
schemaVersion: 1
title: "Siemens Healthineers SOMATOM X.cite CT Scanner - System Will Not Power On or Complete Startup"
issueTitle: "System Will Not Power On or Complete Startup"
description: "Use this guide when the CT system is unresponsive, does not power on normally, or stops during startup before becoming clinically ready."
assetType: "CT Scanner"
manufacturer: "Siemens Healthineers"
model: "SOMATOM X.cite"
slug: "siemens-healthineers-somatom-xcite-system-will-not-power-on-or-complete-startup"
dateAdded: "2026-09-24"
taxonomyMode: "reuse"
ccr:
  complaint: "CT staff reported that the SOMATOM X.cite would power partially but would not complete system startup."
  cause: "Clinical Engineering found an accessible operator workstation power connection loose following a recent room activity."
  resolution: "The connection was secured, the system completed normal startup, and basic scanner readiness and workstation functions were verified before return to service."
helpfulDetails:
  - "Whether the entire scanner or only certain components were unpowered"
  - "Exact startup message or displayed fault"
  - "Condition of emergency-stop or emergency-off controls"
  - "Facility power status"
  - "Workstation and display status"
  - "Recent power outage or room work"
  - "Network connection status"
  - "Unusual sound, heat, odor, or visible damage"
  - "Results after approved restart"
  - "Final system status"
---
## What This Guide Helps With

Use this guide when the CT system is unresponsive, does not power on normally, or stops during startup before becoming clinically ready.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Imaging Coverage
Do not troubleshoot the scanner while a patient depends on it for an active examination. Safely remove the patient from the table when appropriate and arrange an alternate CT scanner if imaging is urgent.  
**Expected outcome:** The patient is safe, no examination depends on the affected scanner, and troubleshooting can proceed without disrupting care.

### 2. Confirm the Exact Startup Condition
Determine whether the entire system is without power or whether specific components such as the operator workstation, gantry, table, displays, or accessories are powered while startup remains incomplete. Record any displayed message or abnormal indicator.  
**Expected outcome:** The failure is narrowed to a total-power condition, partial-power condition, or startup-sequence problem.

### 3. Verify Facility Power and External Disconnects
Check accessible facility power indicators, approved system disconnects, emergency-off controls, and room power conditions without opening electrical cabinets. Verify that an emergency-stop or emergency-off control has not been activated.  
**Expected outcome:** Normal external power is available and no accessible safety disconnect or emergency control is preventing startup. If restoring an appropriate external control returns the system to normal operation, continue to final verification and stop troubleshooting.

### 4. Inspect External Power and Communication Connections
Visually inspect accessible workstation power cords, monitor connections, network cables, and peripheral connections for looseness, damage, or accidental disconnection. Do not open gantry or power-distribution enclosures.  
**Expected outcome:** All accessible connections are secure and free of visible damage.

### 5. Check the Operator Workstation and Displays
Verify that the workstation, displays, and related operator components receive power. If a display is blank but the workstation appears active, verify display power, input selection, and external video connections.  
**Expected outcome:** The operator interface powers normally or the problem is isolated to an external workstation/display connection.

### 6. Perform an Approved Normal Restart
If the system is stable and no electrical smell, smoke, overheating, or abnormal sound is present, perform only the normal shutdown/startup sequence available to Clinical Engineering through approved operating controls. Do not repeatedly cycle system power.  
**Expected outcome:** The SOMATOM X.cite completes startup and reaches its normal ready state. If it does, proceed to final verification and stop troubleshooting.

### 7. Check Environmental and Infrastructure Conditions
Verify that the room has normal HVAC operation and that there is no evidence of recent facility power interruption, water intrusion, network outage, or environmental event affecting the scanner.  
**Expected outcome:** No external environmental or infrastructure condition explains the incomplete startup.

### 8. Perform Final Functional Verification
After normal startup, confirm the operator interface, gantry status, patient table, communications, and scanner readiness using approved nonpatient checks. Confirm no persistent warnings or abnormal indicators remain.  
**Expected outcome:** The system reaches normal operational status and basic functions respond as expected. Troubleshooting can stop and the unit may be returned to service according to facility procedure.

### 9. Escalate an Unresolved Startup Failure
If the system remains unpowered, repeatedly stops during startup, shows persistent system faults, or exhibits abnormal heat, odor, electrical noise, or other unsafe conditions, discontinue external troubleshooting.  
**Expected outcome:** The scanner remains out of clinical use and is referred for qualified service evaluation.

## If the Problem Persists

Common external causes such as facility power, accessible emergency controls, workstation connections, displays, and environmental conditions have been ruled out. The remaining cause may involve internal power distribution, system control hardware, startup software, gantry electronics, or other service-level functions.

The scanner should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench/service evaluation as appropriate
- Evaluated using current Siemens Healthineers service documentation and approved test equipment
- Repaired or configured only by qualified personnel

After corrective service, complete appropriate manufacturer-required checks, scanner functional verification, and applicable image-quality or safety testing before clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not leave a patient positioned on the scanner while investigating a system that cannot reliably complete startup.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient first, verify external power and accessible controls before assuming an internal failure, confirm normal operation after correction, escalate persistent startup problems appropriately, and document the complaint, cause, and resolution clearly.

That is successful troubleshooting.
