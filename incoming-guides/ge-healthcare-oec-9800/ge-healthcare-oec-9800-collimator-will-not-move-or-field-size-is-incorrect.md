---
schemaVersion: 1
title: "GE Healthcare OEC 9800 C-Arm - Collimator Will Not Move or Field Size Is Incorrect"
issueTitle: "Collimator Will Not Move or Field Size Is Incorrect"
description: "Troubleshoots collimator movement or field-size problems caused by controls, positioning, obstruction, connections, configuration, or service-level collimator faults."
assetType: "C-Arm"
manufacturer: "GE Healthcare"
model: "OEC 9800"
slug: "ge-healthcare-oec-9800-collimator-will-not-move-or-field-size-is-incorrect"
dateAdded: "2026-09-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the OEC 9800 collimator would not reduce the fluoroscopy field during setup."
  cause: "Clinical Engineering found a positioning drape caught against the external collimator control area and interfering with operation."
  resolution: "Removed the obstruction and verified repeatable collimator movement and appropriate field-size changes using an approved imaging test."
helpfulDetails:
  - "No movement versus partial movement"
  - "Direction affected"
  - "Field-size indication"
  - "Actual observed field"
  - "C-arm position during failure"
  - "External obstruction or damage"
  - "Control response"
  - "Unusual noise or binding"
  - "Repeatability after correction"
  - "Imaging verification result"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots collimator movement or field-size problems caused by controls, positioning, obstruction, connections, configuration, or service-level collimator faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Uncontrolled Imaging

If the collimator cannot be positioned as intended, do not continue patient imaging when the resulting field could expose unnecessary anatomy or interfere with the procedure.

Move the procedure to another verified system when necessary.

Expected outcome: Imaging does not continue with uncontrolled or unreliable collimation.

### 2. Confirm the Reported Collimator Behavior

Determine whether the collimator does not move at all, moves only in one direction, moves intermittently, stops before reaching the desired field, or produces a field different from the indicated field size.

Reproduce the complaint without a patient using approved test conditions.

Expected outcome: The exact failure mode is confirmed.

### 3. Verify Normal System Readiness

Confirm that the OEC 9800 has completed startup normally and is not displaying a condition that inhibits imaging or mechanical operation.

If the system has another active fault, address or document that condition before continuing.

Expected outcome: The system is otherwise ready for normal imaging operation.

### 4. Check Operator Controls

Operate the normal collimator controls and verify that buttons, switches, or corresponding controls respond consistently. Check for a stuck, damaged, contaminated, or physically obstructed control.

Do not access unauthorized service controls.

Expected outcome: Controls operate normally or an external control problem is identified.

### 5. Inspect the Collimator Area Externally

Visually inspect the external collimator housing and surrounding area for impact damage, foreign material, accessories, drapes, cables, or other items that could interfere with movement.

Do not open the collimator assembly.

Expected outcome: No external obstruction or visible damage is present.

### 6. Reposition the C-Arm and Retest

Move the C-arm to a neutral, stable position and retry collimation. Confirm that cables, coverings, or accessories are not placing tension on the imaging head or interfering with controls.

Expected outcome: If collimator function returns in a neutral position, an external positioning or interference issue has been identified and troubleshooting can stop after verification.

### 7. Compare Indicated Field With Actual Field

Using an approved radiographic or fluoroscopic test method and appropriate test material, compare the displayed or selected field with the visible irradiated field.

Do not attempt calibration adjustments unless authorized and equipped to perform the manufacturer procedure.

Expected outcome: Collimation is confirmed as either accurate or clearly mismatched.

### 8. Check for Intermittent Operation

Cycle the collimator several times under controlled conditions. Observe for delayed response, sticking, unusual noise, incomplete travel, or operation that changes with system position.

Expected outcome: Collimator operation remains repeatable or the intermittent condition is reproduced.

### 9. Perform Final Imaging Verification

After correcting an external cause, perform an approved imaging test and verify that collimation changes smoothly, the field responds correctly, and the selected field is appropriate for imaging.

Expected outcome: Field-size control is reliable and the complaint cannot be reproduced. Troubleshooting can stop.

### 10. Remove From Service if Collimation Remains Unreliable

If the controls work but the collimator does not respond correctly, binds, moves unpredictably, or produces an incorrect field, remove the system from service.

Expected outcome: An imaging system with unreliable beam limitation is not used clinically.

## If the Problem Persists

External controls, positioning, obstructions, and basic operation have been ruled out. Remaining causes may involve the collimator drive mechanism, position sensing, control electronics, calibration, communication, or another service-level condition.

The OEC 9800 should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate GE Healthcare service documentation and approved imaging test equipment.
- Repaired or calibrated only by qualified personnel.

Return-to-service testing should verify reliable collimator movement and appropriate field alignment before clinical use.

Knowing when to stop rather than forcing or mechanically manipulating the collimator is proper troubleshooting.

## Clinical Use Tip

Do not compensate for a malfunctioning collimator by accepting an unnecessarily large radiation field during patient imaging.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- No movement versus partial movement
- Direction affected
- Field-size indication
- Actual observed field
- C-arm position during failure
- External obstruction or damage
- Control response
- Unusual noise or binding
- Repeatability after correction
- Imaging verification result
- Final device status

## Final Thought

Treat collimation as a radiation-safety function. Rule out controls, positioning, and external obstruction first, verify field performance before returning the unit to service, and escalate any persistent mismatch or mechanical problem.

That is successful troubleshooting.
