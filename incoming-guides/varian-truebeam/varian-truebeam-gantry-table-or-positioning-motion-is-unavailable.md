---
schemaVersion: 1
title: "Varian TrueBeam Radiation Therapy System - Gantry, Table, or Positioning Motion Is Unavailable"
issueTitle: "Gantry, Table, or Positioning Motion Is Unavailable"
description: "Gantry, treatment couch, or positioning motion is unavailable, inhibited, interrupted, or does not respond to normal controls."
assetType: "Radiation Therapy System"
manufacturer: "Varian"
model: "TrueBeam"
slug: "varian-truebeam-gantry-table-or-positioning-motion-is-unavailable"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that the TrueBeam treatment couch would not move when positioning was commanded."
  cause: "Clinical Engineering found an external positioning accessory interfering with the couch movement path."
  resolution: "Clinical Engineering corrected the accessory placement and verified smooth couch movement and normal stopping before the system was returned for clinical verification."
helpfulDetails:
  - "Motion function or axis affected"
  - "Direction of failed movement"
  - "Displayed inhibit or fault message"
  - "Emergency-stop status"
  - "Room interlock status"
  - "Accessory and immobilization setup"
  - "Physical obstruction found"
  - "Control interface condition"
  - "Abnormal sound or movement"
  - "Results after correction"
  - "Final functional verification"
---
## What This Guide Helps With

Gantry, treatment couch, or positioning motion is unavailable, inhibited, interrupted, or does not respond to normal controls.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Unexpected Motion
Do not troubleshoot unreliable positioning motion while a patient depends on the system. Stop the treatment workflow and ensure the patient is safe from unintended gantry, couch, or accessory movement.

**Expected outcome:** The patient is no longer exposed to risk from unexpected or unavailable positioning motion.

### 2. Identify Which Motion Is Affected
Determine whether the issue involves gantry rotation, treatment couch motion, a specific direction or axis, or all positioning functions. Record any displayed inhibit or fault message.

**Expected outcome:** The exact affected motion and reported condition are identified.

### 3. Check for Physical Obstructions
Inspect the patient-support area, gantry clearance, immobilization equipment, accessories, cables, floor area, and surrounding equipment for anything that could obstruct movement.

Do not force the gantry or couch through resistance.

**Expected outcome:** The full intended motion path is clear of external obstruction.

### 4. Verify Patient-Support and Accessory Positioning
Check that externally mounted accessories, immobilization devices, indexing components, and patient-support attachments are correctly positioned and not interfering with the expected movement path.

**Expected outcome:** Accessories are correctly installed and no external component is restricting motion.

### 5. Check Emergency Stops and Safety Interlocks
Verify that accessible emergency-stop controls and room safety conditions are normal. Check for door or system conditions that may intentionally inhibit motion.

Never bypass an interlock or defeat a safety circuit.

**Expected outcome:** No external safety condition is preventing authorized positioning movement.

### 6. Verify Motion Controls
Confirm that the appropriate positioning controls are enabled and responsive. Inspect accessible pendant, console, or control interfaces for damage, stuck controls, or disconnected external cables where applicable.

**Expected outcome:** Controls are connected, undamaged, and produce the expected response.

### 7. Check System State and Positioning Workflow
Confirm the system is in an appropriate operational state for the requested movement and that no active workflow, safety condition, or incomplete system initialization is preventing motion.

**Expected outcome:** The system is in a state that permits the requested positioning function.

### 8. Compare Available Motion Functions
With no patient dependent on the system, verify whether other permitted positioning axes respond normally. Do not continue testing any motion that behaves unpredictably, makes abnormal noise, or moves inconsistently.

**Expected outcome:** Either normal motion is restored or the failure is narrowed to a specific movement function.

### 9. Perform Final Functional Verification
If the issue is corrected, verify the affected movement through its clinically required operating range under controlled conditions. Confirm smooth response, proper stopping, and expected control behavior.

**Expected outcome:** Positioning motion operates consistently and safely. If so, troubleshooting can stop.

### 10. Stop and Escalate Unsafe or Persistent Motion Problems
Remove the system from service if motion remains unavailable, intermittent, unexpectedly continues, produces unusual sound, or cannot be verified as safe.

**Expected outcome:** A system with unreliable mechanical motion is prevented from clinical use.

## If the Problem Persists

External obstruction, accessory placement, controls, emergency-stop conditions, and basic operating-state causes have been ruled out. The remaining problem may involve internal motion control, drive systems, position feedback, interlocks, control electronics, or system-level configuration.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or appropriate on-site bench/service evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Return to service requires verification of affected positioning functions and any required safety checks before patient treatment resumes.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never attempt to overcome a positioning inhibit by repeatedly commanding motion when the cause of the inhibit is unknown.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Positioning problems require a patient-safety-first approach. Check obstructions, accessories, controls, and safety conditions before assuming an internal drive failure, and remove the system from service whenever motion cannot be verified as predictable and safe.

That is successful troubleshooting.
