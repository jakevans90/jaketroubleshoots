---
schemaVersion: 1
title: "LivaNova S5 Heart-Lung Machine - Level Sensor Alarm or Sensor Will Not Calibrate"
issueTitle: "Level Sensor Alarm or Sensor Will Not Calibrate"
description: "Troubleshoots level sensor alarms or calibration problems by checking sensor placement, reservoir interface, cleanliness, cabling, and configuration."
assetType: "Heart-Lung Machine"
manufacturer: "LivaNova"
model: "S5"
slug: "livanova-s5-level-sensor-alarm-or-sensor-will-not-calibrate"
dateAdded: "2026-09-15"
taxonomyMode: "reuse"
ccr:
  complaint: "Perfusion reported that the S5 level sensor would not complete calibration during setup."
  cause: "Clinical Engineering found the sensor mounted over a label on the reservoir rather than directly against the intended sensing surface."
  resolution: "Clinical Engineering repositioned the sensor on the correct reservoir surface and verified successful calibration and alarm operation."
helpfulDetails:
  - "Sensor/channel affected"
  - "Reservoir type"
  - "Sensor position"
  - "Surface condition"
  - "Exact alarm or calibration message"
  - "Sensor and cable condition"
  - "Known-good substitutions"
  - "Configuration observed"
  - "Calibration result"
  - "Alarm verification result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots level sensor alarms or calibration problems by checking sensor placement, reservoir interface, cleanliness, cabling, and configuration.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Reservoir Level

Do not troubleshoot an unreliable level sensor while a patient depends on it as the active reservoir-level safeguard. Maintain direct clinical monitoring and follow the perfusion contingency plan using verified backup protection.

Never disable a level alarm simply to continue a case.

**Expected outcome:** Reservoir level remains safely managed independently of the suspect sensor.

Once the sensor is isolated from active patient support, troubleshooting may continue.

### 2. Confirm the Exact Failure

Determine whether:

- The level alarm is active unexpectedly.
- The sensor is not recognized.
- Calibration will not complete.
- The alarm appears intermittently.
- The condition changes when the sensor is moved.
- The problem began after changing reservoirs or sensor position.

Record the displayed message if present.

**Expected outcome:** The failure is identified as placement, recognition, calibration, or intermittent sensing.

If the sensor subsequently calibrates normally and passes verification, troubleshooting can stop.

### 3. Verify Sensor Placement

Inspect the position of the level sensor on the compatible reservoir. Confirm it is:

- At the intended sensing location
- Fully seated
- Properly oriented
- Flat against the required surface
- Not positioned over labels, seams, or obstructions that interfere with sensing

**Expected outcome:** The level sensor is positioned correctly for the installed reservoir.

If repositioning restores normal calibration and alarm function, troubleshooting can stop after verification.

### 4. Inspect the Reservoir Interface

Check the sensing location for:

- Condensation
- Moisture
- Adhesive residue
- Surface contamination
- Damage
- Unexpected wall thickness or incompatible reservoir design

Use only approved compatible components.

**Expected outcome:** The reservoir surface at the sensing point is clean, dry, intact, and compatible.

If correcting an interface problem restores sensing, troubleshooting can stop.

### 5. Inspect the Sensor and Cable

Examine the external sensor and cable for:

- Cracks
- Loose housing
- Damaged strain relief
- Cuts
- Fluid intrusion
- Connector damage

Reseat the external connector if appropriate.

**Expected outcome:** The sensor and external cabling are secure and physically intact.

If reseating or replacing a damaged approved external component resolves the issue, troubleshooting can stop after testing.

### 6. Verify Normal Configuration

Confirm the intended level sensor is selected and enabled in the normal system configuration. Verify that the correct sensor/channel is being used for the connected reservoir.

Do not alter protected calibration parameters or alarm thresholds outside authorized procedures.

**Expected outcome:** The configured sensor matches the physical setup.

If an authorized configuration correction allows successful calibration, troubleshooting can stop.

### 7. Compare With a Known-Good Setup

When permitted, use a known-good compatible reservoir setup, sensor, or cable to isolate whether the failure follows the disposable interface or the sensor hardware.

**Expected outcome:** The cause is isolated to an external component, setup, or the sensor/system channel.

If an external component is identified as defective and replacement restores normal operation, troubleshooting can stop after verification.

### 8. Perform Approved Calibration and Alarm Verification

Follow the approved normal calibration process and then verify the alarm responds appropriately to the approved test condition.

Do not invent calibration methods or simulate reservoir conditions in an unapproved manner.

**Expected outcome:** Calibration completes normally and the level alarm pathway operates predictably.

If all checks pass, troubleshooting is complete.

### 9. Escalate Persistent Sensor Failure

If the sensor will not calibrate, alarms intermittently, or cannot reliably detect the approved test condition, remove the affected function from service.

Do not bypass the sensor or perform internal electronic adjustment without manufacturer-authorized procedures.

**Expected outcome:** An unreliable level-sensing safety feature is not returned to patient care.

## If the Problem Persists

Sensor placement, reservoir compatibility, surface condition, cabling, configuration, and known-good substitutions have been ruled out. Remaining causes may involve internal sensor electronics, communication circuitry, protected calibration, or module-level faults.

The affected equipment should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate LivaNova documentation and approved test equipment.
- Repaired, calibrated, or configured only by qualified personnel.

Verify sensor calibration, alarm operation, and related system response before return to service.

Knowing when to stop after external causes are eliminated is proper troubleshooting.

## Clinical Use Tip

A level sensor is an additional safety layer, not a replacement for continuous perfusionist observation of reservoir volume.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Maintain independent reservoir-level safety first, then verify sensor placement, reservoir compatibility, cleanliness, cabling, and configuration before suspecting internal sensor failure. Confirm calibration and alarm behavior before returning the system to use.

That is successful troubleshooting.
