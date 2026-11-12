---
schemaVersion: 1
title: "Drager Atlan A100 Anesthesia Machine - Breathing-System Oxygen Sensor Fails Calibration or Reports Incorrect FiO2"
issueTitle: "Breathing-System Oxygen Sensor Fails Calibration or Reports Incorrect FiO2"
description: "Addresses oxygen-sensor calibration or FiO2 errors caused by gas source, sensor exposure, installation, leaks, contamination, or sensor deterioration."
assetType: "Anesthesia Machine"
manufacturer: "Drager"
model: "Atlan A100"
slug: "drager-atlan-a100-breathing-system-oxygen-sensor-fails-calibration-or-reports-incorrect-fio2"
dateAdded: "2026-11-12"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that the Drager Atlan A100 failed oxygen-sensor calibration and displayed an FiO2 lower than expected."
  cause: "Clinical Engineering found the oxygen sensor was not fully seated after the breathing system had been reassembled."
  resolution: "Clinical Engineering reseated the oxygen sensor, completed calibration successfully, verified FiO2 against an approved oxygen analyzer, completed the system test, and returned the machine to service."
helpfulDetails:
  - "Exact calibration message"
  - "Displayed FiO2"
  - "Independent analyzer reading"
  - "Pipeline or cylinder source"
  - "Sensor condition and seating"
  - "Breathing-system leak findings"
  - "Gas configuration during calibration"
  - "Replacement sensor used"
  - "Final calibration result"
  - "Final device status"
---

## What This Guide Helps With

Addresses oxygen-sensor calibration or FiO2 errors caused by gas source, sensor exposure, installation, leaks, contamination, or sensor deterioration.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Unverified Oxygen Measurement
Do not troubleshoot an unreliable oxygen measurement while a patient depends on the machine. Transfer care to another verified anesthesia system or use an appropriate independent oxygen-monitoring method during equipment exchange.

**Expected outcome:** Patient oxygen delivery and monitoring are maintained independently.

### 2. Confirm the Exact Oxygen Measurement Problem
Determine whether the oxygen sensor fails calibration, reads unexpectedly high or low, drifts, or disagrees with another analyzer.

Record gas source, selected settings, and displayed FiO2.

**Expected outcome:** The concern is clearly defined and reproducible in a controlled test setup.

### 3. Verify the Oxygen Supply
Confirm oxygen pipeline or cylinder supply is correctly connected and stable. Check hoses and connectors for damage, incorrect connection, or loose fittings.

If appropriate, compare operation using another verified oxygen source.

**Expected outcome:** A stable, correct oxygen source is supplied to the machine. If the problem follows the facility source, escalate the infrastructure issue rather than the machine.

### 4. Verify Test Conditions
Ensure the breathing system has been configured correctly for the normal oxygen-sensor calibration procedure and is not being exposed to an unintended gas mixture from residual anesthetic gas, alternate carrier gas, or an external accessory.

**Expected outcome:** Calibration is attempted under appropriate and stable gas conditions.

### 5. Inspect the Oxygen Sensor and Its Installation
Inspect accessible oxygen-sensor components and connections for correct seating, contamination, moisture, visible damage, or incomplete engagement.

Do not open or repair the sensor internally.

**Expected outcome:** The sensor is clean, correctly installed, and securely connected.

### 6. Check for Breathing-System Leaks
Inspect the circuit, breathing-system assembly, absorber, sampling connections, and accessible seals for leaks that could dilute or alter the measured gas.

**Expected outcome:** No significant external leak is present. If correcting a leak restores accurate oxygen measurement, proceed to verification.

### 7. Compare With an Independent Oxygen Analyzer
Use an approved and properly calibrated oxygen analyzer to compare actual delivered oxygen concentration with the Atlan A100 reading.

Ensure the independent analyzer and its sampling arrangement are functioning correctly.

**Expected outcome:** The independent measurement confirms whether the machine reading is accurate or incorrect.

### 8. Substitute a Known-Good Replaceable Sensor When Appropriate
If the oxygen-sensing element is an approved field-replaceable component and a known-good compatible replacement is available, substitute it following authorized procedures.

Repeat calibration.

**Expected outcome:** Successful calibration with the replacement isolates the original sensor as the cause.

### 9. Repeat System Test and Functional Verification
After correcting an external cause or replacing an approved external sensor, repeat oxygen calibration and the normal system test.

Verify delivered oxygen concentration across controlled test conditions using approved analysis equipment.

**Expected outcome:** Oxygen calibration passes and displayed FiO2 agrees with independent measurement. Troubleshooting can stop.

### 10. Escalate Persistent Oxygen Measurement Failure
If supply, leaks, calibration conditions, sensor installation, and independent measurement are verified but the problem remains, remove the machine from service.

**Expected outcome:** The unit is referred for qualified evaluation of the oxygen-sensing system or associated internal circuitry.

## If the Problem Persists

External gas supply, breathing-system leaks, sensor installation, calibration conditions, and independent analyzer accuracy have been ruled out. The remaining fault may involve the oxygen sensor, internal gas path, sensor interface, or signal-processing circuitry.

The device should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate Drager documentation and approved oxygen-analysis equipment.
- Repaired or calibrated only by qualified personnel.
- Fully tested for oxygen measurement, gas delivery, ventilation, alarms, and system-test performance before return to service.

An anesthesia machine with unverified FiO2 measurement should not be returned to patient use.

## Clinical Use Tip

When the displayed FiO2 is questionable, confirm oxygen delivery independently and move the patient to a verified system before troubleshooting.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Incorrect oxygen measurement is a direct patient-safety concern. Verify supply, calibration conditions, sensor installation, leaks, and independent measurement before assuming internal failure, and escalate whenever FiO2 cannot be reliably confirmed.

That is successful troubleshooting.
