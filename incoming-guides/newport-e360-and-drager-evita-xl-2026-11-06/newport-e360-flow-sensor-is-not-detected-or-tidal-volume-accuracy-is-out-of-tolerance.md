---
schemaVersion: 1
title: "Newport e360 Ventilator - Flow Sensor Is Not Detected or Tidal-Volume Accuracy Is Out of Tolerance"
issueTitle: "Flow Sensor Is Not Detected or Tidal-Volume Accuracy Is Out of Tolerance"
description: "Addresses missing flow sensing or inaccurate tidal-volume measurement caused by circuit leaks, sensor setup, contamination, connections, configuration, or calibration."
assetType: "Ventilator"
manufacturer: "Newport"
model: "e360"
slug: "newport-e360-flow-sensor-is-not-detected-or-tidal-volume-accuracy-is-out-of-tolerance"
dateAdded: "2026-11-06"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the Newport e360 displayed inconsistent tidal volumes during setup."
  cause: "Clinical Engineering found moisture in the externally connected flow-sensing component, causing unstable measurements."
  resolution: "The affected component was replaced with a verified compatible sensor, calibration passed, and tidal-volume accuracy was confirmed with a ventilator analyzer."
helpfulDetails:
  - "Sensor-detection message"
  - "Circuit condition"
  - "Flow-sensor condition"
  - "Moisture or contamination"
  - "Connector condition"
  - "Known-good substitution results"
  - "Calibration result"
  - "Ventilator analyzer measurements"
  - "Results before and after correction"
  - "Final device status"
---

## What This Guide Helps With

Addresses missing flow sensing or inaccurate tidal-volume measurement caused by circuit leaks, sensor setup, contamination, connections, configuration, or calibration.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Confirm the Symptom
Do not continue clinical use if tidal-volume monitoring or delivery cannot be trusted. Transfer the patient to another verified ventilator.

Determine whether the problem is sensor detection, displayed tidal volume, delivered tidal volume, or a failed verification test.

**Expected outcome:** The patient is protected and the reported measurement problem is clearly defined.

### 2. Inspect the Breathing Circuit
Check the circuit for loose connections, leaks, incorrectly installed components, water accumulation, damaged tubing, or open sampling ports.

**Expected outcome:** The breathing circuit is intact and correctly assembled. If correcting a circuit leak restores normal volume readings, the issue is resolved after verification.

### 3. Inspect the Flow-Sensing Components
Inspect externally accessible flow-sensing components and their connectors for contamination, moisture, physical damage, improper orientation, or incomplete seating.

Do not attempt internal sensor repair.

**Expected outcome:** The sensor and connections are clean, dry, properly installed, and undamaged.

### 4. Reseat Sensor Connections
Disconnect and reconnect approved removable sensor connections with the ventilator removed from clinical use. Check for bent contacts, damaged connectors, or poor engagement.

**Expected outcome:** The ventilator consistently recognizes the sensor. If reseating restores detection and subsequent verification passes, troubleshooting can stop.

### 5. Substitute a Known-Good Compatible Sensor or Circuit
When available, install a verified compatible sensor or circuit component.

**Expected outcome:** The known-good component is detected and produces stable measurements. If the fault follows the original accessory, replace it and proceed to final testing.

### 6. Verify Configuration and Circuit Type
Confirm that the ventilator is configured appropriately for the circuit and accessories installed. Do not enter unauthorized service menus or alter calibration constants.

**Expected outcome:** External setup and permitted configuration agree with the installed circuit.

### 7. Perform Approved Flow or Sensor Calibration
With the ventilator off-patient, complete any user-accessible or authorized calibration required for the installed flow-sensing setup.

**Expected outcome:** Calibration completes successfully. A repeated calibration failure with known-good external components requires escalation.

### 8. Measure Delivered Tidal Volume Independently
Connect an approved ventilator analyzer and test lung. Compare independently measured tidal volume with the ventilator's delivered and displayed values under controlled conditions.

**Expected outcome:** Delivered and monitored values meet the applicable manufacturer verification criteria. If they do, the issue is resolved.

### 9. Check Across Representative Test Conditions
Where permitted by the approved procedure, repeat volume verification using more than one controlled test setting to ensure the problem is not intermittent or condition-dependent.

**Expected outcome:** Volume measurement remains stable and acceptable throughout testing.

### 10. Escalate an Unresolved Accuracy Problem
If known-good circuits and sensors, proper setup, and approved calibration do not restore acceptable performance, stop troubleshooting.

**Expected outcome:** The ventilator is removed from service for further evaluation.

## If the Problem Persists

External leaks, sensor installation, connectors, contamination, circuit configuration, and known-good substitutions have been ruled out. Remaining causes may involve internal flow sensing, pressure sensing, pneumatic delivery, signal processing, calibration, or other service-level systems.

Remove the ventilator from service, label it **Out of Service**, and send it for manufacturer-directed bench evaluation using approved ventilator-analysis equipment. Do not perform board-level repair or unauthorized calibration.

Return the ventilator to service only after flow sensing, tidal-volume accuracy, ventilation performance, and applicable alarms have been verified.

## Clinical Use Tip

Do not rely on a ventilator for patient management when measured tidal volume is known to be unreliable, even if the ventilator appears to cycle normally.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Verify the circuit, flow-sensing components, connections, calibration, and independent delivered volume before assuming an internal fault. Remove inaccurate equipment from service and document objective test results.

That is successful troubleshooting.
