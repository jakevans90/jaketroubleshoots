---
schemaVersion: 1
title: "GE Healthcare Discovery MI PET / CT System - Gantry, Table, or Positioning Motion Is Unavailable"
issueTitle: "Gantry, Table, or Positioning Motion Is Unavailable"
description: "Troubleshoots unavailable or interrupted gantry and patient-table motion caused by safety controls, obstructions, positioning conditions, connections, or system readiness."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "Discovery MI"
slug: "ge-healthcare-discovery-mi-gantry-table-or-positioning-motion-is-unavailable"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "PET / CT staff reported that the Discovery MI patient table would not advance into the gantry."
  cause: "Clinical Engineering found an accessory cable routed into the table travel path and preventing normal positioning."
  resolution: "Clinical Engineering rerouted the cable, verified unobstructed table movement and normal positioning response, and completed applicable return-to-service checks."
helpfulDetails:
  - "Motion function affected"
  - "Direction affected"
  - "Control station used"
  - "Emergency-stop status"
  - "Obstruction found"
  - "Patient or accessory setup"
  - "Visible messages"
  - "Unusual noise or resistance"
  - "Results from alternate normal controls"
  - "Final movement verification"
---
## What This Guide Helps With
Troubleshoots unavailable or interrupted gantry and patient-table motion caused by safety controls, obstructions, positioning conditions, connections, or system readiness.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Unintended Movement

Do not troubleshoot unreliable motion while a patient depends on the scanner for positioning or support.

If a patient is on the table, maintain patient safety and prevent unintended movement. Follow departmental procedures for safely removing or transferring the patient if normal positioning cannot be assured.

Stop immediately if there is binding, collision risk, unusual mechanical noise, uncontrolled movement, or visible damage.

**Expected outcome:** The patient is safe and no further motion is attempted under unsafe conditions.

If mechanical damage or unsafe movement is present, remove the scanner from service and escalate.

### 2. Confirm Which Motion Is Affected

Determine exactly what will not move:

- Patient table
- Table elevation
- Longitudinal positioning
- Gantry-related positioning function
- A specific direction only
- All positioning controls

Determine whether the problem occurs from one control location or all available normal controls.

**Expected outcome:** The failed motion and the conditions under which it occurs are clearly identified.

### 3. Inspect for Physical Obstruction

Inspect the accessible travel path around the gantry and table.

Check for:

- Patient belongings
- Linens
- Cables
- Injector tubing
- Monitoring leads
- Positioning aids
- Accessories
- Objects under or beside the table
- Contact between equipment and the gantry

Do not force motion against resistance.

**Expected outcome:** The movement path is clear and no external object is preventing safe travel.

If clearing an obstruction restores normal movement, verify operation through the required range and stop troubleshooting.

### 4. Check Emergency Stops and Safety Controls

Inspect accessible emergency-stop and motion-inhibit controls.

Determine whether a control was activated intentionally. Reset it only after confirming that the reason for activation has been resolved and movement can occur safely.

**Expected outcome:** No emergency or safety control is unintentionally disabling positioning motion.

### 5. Verify System Readiness

Confirm that the Discovery MI has completed startup and is not displaying a condition that prevents motion.

Check whether:

- System initialization is complete
- The scanner is in an appropriate operating state
- An active examination or sequence is restricting movement
- A door, accessory, or other safety condition is preventing positioning
- A visible fault remains active

Do not bypass a safety interlock.

**Expected outcome:** The scanner is in a normal state that permits commanded movement.

### 6. Check Patient Load and Positioning Conditions

Confirm that the table and patient setup are appropriate for normal operation.

Look for:

- Equipment hanging from the tabletop
- Accessories interfering with travel
- Patient position causing contact
- Cables pulled tight during motion
- Items extending into the travel path

Do not attempt to overcome a mechanical restriction by repeatedly commanding motion.

**Expected outcome:** The patient setup and accessories do not interfere with safe table or gantry travel.

### 7. Compare Available Motion Controls

With no patient at risk, test the affected motion using normal approved controls from available operator locations where appropriate.

Observe whether:

- One control station fails while another works
- One direction is affected
- Motion begins and stops
- No response occurs
- A message appears when movement is commanded

**Expected outcome:** Normal controls produce smooth, predictable movement without abnormal noise, hesitation, or fault indication.

If motion operates normally after an external control or positioning issue is corrected, proceed to final verification.

### 8. Perform Final Functional Verification

Exercise the affected motion sufficiently to verify:

- Smooth operation
- Normal stopping
- Repeatable response
- No obstruction
- No unusual sound
- No unexpected drift or movement
- Normal system readiness afterward

Complete applicable return-to-service testing.

**Expected outcome:** Gantry and table positioning respond normally and safely.

If the motion system performs normally and all required checks pass, troubleshooting can stop and the scanner may be returned to service.

## If the Problem Persists

If external obstruction, patient setup, emergency controls, normal system state, and accessible controls have been verified but motion remains unavailable, the cause may involve a motion-control subsystem, position sensing, drive system, safety interlock, communication path, or another service-level condition.

The system should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench/system evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not force movement, defeat interlocks, or access internal motion assemblies without authorized service procedures.

After repair, verify all affected positioning functions and required safety features before return to clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Keep the patient and all lines, cables, accessories, and nearby equipment clear of the table and gantry travel path before testing any positioning movement.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient first and check the physical travel path, safety controls, positioning setup, and normal operating state before suspecting an internal motion failure. Stop if movement is unsafe, verify the correction completely, and document what was found.

That is successful troubleshooting.
