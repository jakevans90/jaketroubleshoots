---
schemaVersion: 1
title: "Drager Savina 300 Ventilator - Flow Sensor Not Recognized, Contaminated, or Will Not Calibrate"
issueTitle: "Flow Sensor Not Recognized, Contaminated, or Will Not Calibrate"
description: "Troubleshoots flow-sensor detection and calibration problems caused by installation, contamination, moisture, damage, incompatible components, or service-level sensing faults."
assetType: "Ventilator"
manufacturer: "Drager"
model: "Savina 300"
slug: "drager-savina-300-flow-sensor-not-recognized-contaminated-or-will-not-calibrate"
dateAdded: "2026-09-08"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the Savina 300 would not recognize the installed flow sensor and calibration would not complete."
  cause: "Clinical Engineering found visible moisture contamination on the flow sensor."
  resolution: "The contaminated sensor was removed and replaced with a known-good compatible sensor, which calibrated successfully and passed test-lung functional verification."
helpfulDetails:
  - "Exact displayed message"
  - "Sensor recognized or not recognized"
  - "Moisture or contamination observed"
  - "Sensor installation condition"
  - "Known-good sensor result"
  - "Circuit condition"
  - "Calibration result"
  - "Flow and volume verification results"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots flow-sensor detection and calibration problems caused by installation, contamination, moisture, damage, incompatible components, or service-level sensing faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Before Handling the Flow Sensor
Do not remove, clean, reseat, or replace a flow sensor while a patient depends on the affected ventilator unless the clinical situation and manufacturer procedure specifically support it. Move the patient to another verified ventilator when necessary.

**Expected outcome:** Patient ventilation remains uninterrupted and the ventilator can be safely evaluated off-patient.

### 2. Confirm the Exact Flow-Sensor Complaint
Determine whether the sensor:
- Is not recognized
- Is intermittently detected
- Produces implausible flow or volume values
- Will not complete calibration
- Has visible contamination or moisture

Record any displayed message exactly.

**Expected outcome:** The failure is clearly identified and reproducible.

### 3. Inspect Sensor Installation
Verify the flow sensor is the correct compatible type, oriented correctly, fully inserted, and seated as intended.

Inspect associated accessible connectors or holders for looseness or damage.

**Expected outcome:** The sensor is installed correctly. If reseating the sensor restores recognition and calibration, proceed to final verification and stop further troubleshooting.

### 4. Inspect for Moisture or Contamination
Remove the sensor only according to approved handling procedures and inspect for:
- Condensation
- Secretion contamination
- Cleaning residue
- Debris
- Physical damage

Do not introduce tools or cleaning agents that are not approved for the component.

**Expected outcome:** The sensor is clean, dry, and undamaged. If contamination caused the problem, clean or replace it according to approved procedure and retest.

### 5. Inspect the Sensor Interface
Inspect the accessible sensor receptacle or installation area for moisture, debris, bent contacts, damaged guides, or anything preventing complete seating.

Do not probe internal electrical contacts.

**Expected outcome:** The interface is clean and mechanically intact. Damage to the ventilator interface requires service evaluation.

### 6. Substitute a Known-Good Flow Sensor
Install a known-good compatible flow sensor when available and repeat recognition and calibration checks.

This is one of the most useful ways to distinguish a sensor problem from a ventilator-side problem.

**Expected outcome:** The known-good sensor is recognized and calibrates normally. If so, remove the original sensor from service and stop troubleshooting after functional verification.

### 7. Verify Circuit and Exhalation Components
Confirm the breathing circuit and exhalation components are installed correctly and do not create abnormal flow conditions that could interfere with calibration.

**Expected outcome:** The breathing system is properly assembled and free of obvious obstruction or leakage.

### 8. Repeat Calibration Under Correct Conditions
Perform the applicable flow-sensor calibration according to current Drager instructions with the required test setup.

Do not alter service calibration coefficients or enter unauthorized menus.

**Expected outcome:** Calibration completes successfully. If so, proceed to performance verification.

### 9. Verify Flow and Volume Performance
Connect an appropriate test lung and ventilator analyzer when required. Confirm displayed and delivered respiratory values are stable and reasonable for the selected test conditions.

**Expected outcome:** Flow and volume measurements behave consistently and the ventilator operates without flow-sensor faults. Troubleshooting can stop.

### 10. Escalate Persistent Recognition or Calibration Failure
If multiple known-good compatible sensors fail to be recognized or calibrated after correct installation, suspect a ventilator-side problem.

**Expected outcome:** The ventilator is removed from clinical use for service-level evaluation.

## If the Problem Persists

External installation, contamination, circuit, and sensor causes have been ruled out. Remaining causes may involve the sensor interface, signal processing, wiring, internal electronics, software, or another service-level measurement fault.

The ventilator should be:
- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Drager documentation and approved test equipment
- Repaired or calibrated only by qualified personnel

Following repair, complete applicable flow, volume, leak, alarm, and ventilator performance verification before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Condensation reaching a flow sensor can create intermittent measurements even when the sensor appears functional at first inspection.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Flow measurement problems should be isolated from the sensor outward before assuming a ventilator failure. Protect the patient, verify installation and cleanliness, substitute known-good components, escalate persistent faults, and document the final verified condition.

That is successful troubleshooting.
