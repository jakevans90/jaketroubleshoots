---
schemaVersion: 1
title: "Siemens Healthineers Biograph Vision PET / CT System - Gantry, Table, or Positioning Motion Is Unavailable"
issueTitle: "Gantry, Table, or Positioning Motion Is Unavailable"
description: "Use this guide when gantry, patient table, or positioning motion is unavailable, inhibited, intermittent, or stopped by external controls, obstructions, or safety conditions."
assetType: "PET / CT System"
manufacturer: "Siemens Healthineers"
model: "Biograph Vision"
slug: "siemens-healthineers-biograph-vision-gantry-table-or-positioning-motion-is-unavailable"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the patient table would not move when positioning controls were pressed."
  cause: "Clinical Engineering found a positioning-control cable partially disconnected at an accessible external connector."
  resolution: "Clinical Engineering reseated the connection, verified smooth table positioning and stopping response, and returned the system to service."
helpfulDetails:
  - "Specific motion affected"
  - "Direction of failed movement"
  - "Control location used"
  - "Exact displayed message"
  - "Safety-stop status"
  - "Obstruction found"
  - "External controller and cable condition"
  - "Whether alternate approved controls worked"
  - "Abnormal sound or binding"
  - "Final motion verification results"
---
## What This Guide Helps With

Use this guide when gantry, patient table, or positioning motion is unavailable, inhibited, intermittent, or stopped by external controls, obstructions, or safety conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Before Testing Motion

Do not troubleshoot unreliable patient-support or positioning motion while a patient depends on the equipment.

If a patient is on the table, maintain safe support, prevent unintended movement, and follow the appropriate clinical process for safely removing or transferring the patient before further troubleshooting.

**Expected outcome:** The patient is safe and no one is depending on uncertain table or gantry motion.

If motion presents a safety risk, remove the system from service immediately.

### 2. Confirm Which Motion Is Unavailable

Determine whether the problem affects:

- Table longitudinal travel.
- Table vertical movement.
- Gantry-related positioning functions.
- All motion or only one direction.
- Local controls, operator controls, or both.
- Motion only at a certain location.

Record any exact message or indicator.

**Expected outcome:** The affected motion and control location are clearly identified.

If the reported problem cannot be reproduced and all motions operate normally during repeated safe testing, proceed to final verification.

### 3. Check for Physical Obstructions

Inspect the table, gantry opening, floor area, accessories, cables, blankets, straps, and nearby equipment.

Look for anything that could mechanically interfere with travel, including:

- Patient positioning accessories.
- Loose cables.
- Equipment carts.
- Bedding hanging into moving areas.
- Objects beneath or alongside the table.
- Accessories installed incorrectly.

Do not force movement past resistance.

**Expected outcome:** The entire intended travel path is unobstructed.

If removing an obstruction restores normal motion, inspect for damage, verify the full required motion range, and stop troubleshooting.

### 4. Verify Safety Stops and Motion Interlocks

Inspect accessible emergency stops and safety controls. Determine whether a safety device was intentionally or accidentally activated.

Do not bypass, defeat, tape, or hold a safety interlock in an operating state.

**Expected outcome:** All accessible safety controls required for normal motion are in their correct operating condition.

If restoring an inadvertently activated control safely restores motion, verify operation and stop.

### 5. Inspect External Positioning Accessories and Connections

Check accessible positioning controls, hand controls, foot controls if applicable, and their external cables and connectors.

Look for:

- Loose connectors.
- Bent or damaged cables.
- Fluid contamination.
- Cracked controls.
- Pinched cords.
- A control trapped beneath equipment.

Use an approved known-good accessory only when the accessory is designed to be interchangeable and substitution is permitted.

**Expected outcome:** External positioning controls and cables are intact and correctly connected.

If a known-good approved control restores normal movement, replace or remove the defective accessory and stop after verification.

### 6. Check System Readiness and Control State

Verify that the system has completed startup and is in a state that permits positioning.

Check for:

- Active system faults.
- Incomplete initialization.
- Active scan or procedure states.
- Pending safety acknowledgments.
- Control modes that legitimately inhibit movement.

Do not enter restricted service modes or alter service-level configuration.

**Expected outcome:** The system is in a normal state that permits requested motion.

If correcting an obvious operating-state condition restores motion, verify operation and stop.

### 7. Compare Local and Console Motion Commands

When safe and permitted, test the affected movement from the available approved control locations.

A difference between control locations may help distinguish an external control issue from a broader motion problem.

**Expected outcome:** Motion responds consistently to valid commands from approved controls.

If one external control is defective while another operates normally, replace or service the affected external control and stop after verification.

### 8. Check for Evidence of Mechanical Distress

Without opening covers, listen and observe during a safe motion attempt for:

- Grinding.
- Binding.
- Jerking.
- Repeated start-stop motion.
- Unusual vibration.
- Visible misalignment.
- Unexpected table drift.

Do not continue testing if abnormal mechanical behavior occurs.

**Expected outcome:** Motion is smooth and does not show signs of mechanical distress.

If abnormal movement is present, remove the system from service and escalate.

### 9. Perform Final Functional Verification

After correcting any external cause, verify:

- Required table and positioning movements.
- Smooth travel.
- Proper stopping behavior.
- Control response.
- No unexpected alarms.
- No obstruction throughout tested travel.

Complete appropriate return-to-service checks.

**Expected outcome:** Positioning motion is predictable, smooth, responsive, and safe.

If all required checks pass, troubleshooting is complete.

### 10. Escalate Unresolved Motion Problems

If motion remains unavailable after obstructions, safety controls, external controls, system readiness, and positioning conditions are verified, stop external troubleshooting.

**Expected outcome:** The system is removed from clinical use and routed for qualified service.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve motion drives, internal position sensing, internal safety circuits, system control electronics, mechanical assemblies, or service-level configuration.

The device should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or qualified system evaluation.
- Evaluated using appropriate Siemens Healthineers documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Do not force movement, defeat interlocks, enter unauthorized service modes, or disassemble gantry or table drive assemblies.

Return the system to clinical use only after safe positioning operation and required system checks have been verified.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Never place staff or patients where unexpected table or gantry movement could cause entrapment or injury during motion testing.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient from unintended motion, eliminate obstructions and external control problems first, verify safe operation before assuming an internal drive failure, and escalate when motion cannot be proven reliable.

That is successful troubleshooting.
