---
schemaVersion: 1
title: "GE Healthcare Carestation 750 Anesthesia Machine - O2 Sensor Calibration or FiO2 Measurement Error"
issueTitle: "O2 Sensor Calibration or FiO2 Measurement Error"
description: "Oxygen calibration fails or FiO2 appears incorrect because of gas supply, sampling, circuit, sensor, calibration, or configuration problems."
assetType: "Anesthesia Machine"
manufacturer: "GE Healthcare"
model: "Carestation 750"
slug: "ge-healthcare-carestation-750-o2-sensor-calibration-or-fio2-measurement-error"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that the Carestation 750 displayed unstable FiO2 values and would not complete oxygen calibration."
  cause: "Clinical Engineering found a partially obstructed gas-sampling line containing moisture."
  resolution: "The sampling line was replaced, oxygen calibration completed successfully, FiO2 was verified with an approved analyzer, and checkout passed."
helpfulDetails:
  - "Exact O2-related message"
  - "Selected oxygen concentration"
  - "Displayed FiO2"
  - "Pipeline and cylinder status"
  - "Sampling-line condition"
  - "Water-trap condition"
  - "Sensor condition"
  - "Calibration result"
  - "Independent analyzer comparison"
  - "Response to concentration changes"
  - "Final checkout status"
  - "Final device disposition"
---

## What This Guide Helps With
Oxygen calibration fails or FiO2 appears incorrect because of gas supply, sampling, circuit, sensor, calibration, or configuration problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Unreliable Oxygen Measurement
Do not troubleshoot questionable oxygen measurement or delivery while a patient depends on the affected machine.

If FiO2 cannot be trusted during clinical use, transition to appropriate verified equipment and remove the Carestation 750 from service.

**Expected outcome:** The patient is protected from unreliable oxygen monitoring or delivery.

### 2. Confirm Whether the Problem Is Calibration, Measurement, or Delivery
Document whether the issue involves:

- Calibration failure
- FiO2 reading inconsistent with the selected concentration
- Slow or unstable oxygen readings
- No oxygen measurement
- Associated gas-supply or monitoring messages

Use a controlled test setup rather than a patient.

**Expected outcome:** The problem is clearly categorized. If the reading proves normal under controlled testing, document the test conditions and continue only if the reported condition remains reproducible.

### 3. Verify the Oxygen Supply
Confirm the oxygen pipeline hose is securely connected and inspect it for damage or kinking.

If appropriate for the machine's configuration, verify backup cylinder availability and connection.

**Expected outcome:** An adequate external oxygen source is available with no obvious connection problem. Correcting an external supply issue that restores normal readings resolves the problem.

### 4. Inspect the Breathing Circuit and Sampling Path
Check the breathing circuit, gas-sampling tubing, airway adapter, water trap, filters, and other external sampling accessories.

Look for:

- Disconnections
- Occlusions
- Moisture
- Cracks
- Loose connections
- Incorrect assembly

**Expected outcome:** The sampling and breathing paths are intact. If correcting a sampling issue restores stable FiO2 measurement, troubleshooting can stop.

### 5. Verify Fresh-Gas and Ventilation Settings
Confirm selected gas mixture and fresh-gas settings are appropriate for the test being performed.

Allow adequate stabilization when changing gas concentration before judging the measurement response.

**Expected outcome:** The measured oxygen response is consistent with the test configuration. If an incorrect setting explains the discrepancy, correct it and verify operation.

### 6. Perform the Approved O2 Calibration
Perform only the normal approved calibration procedure provided for the Carestation 750.

Do not enter unauthorized service menus or alter internal calibration constants.

**Expected outcome:** Calibration completes successfully. If subsequent FiO2 verification is correct, troubleshooting can stop.

### 7. Inspect Accessible Oxygen-Sensing Components
If the sensor or associated external component is intended to be accessible, inspect for contamination, incorrect seating, visible damage, or expired/consumed condition when applicable.

Use only compatible approved replacement components.

**Expected outcome:** The oxygen-sensing component is properly installed and serviceable. If replacement of an appropriate consumable sensor restores calibration, the issue is resolved after final verification.

### 8. Compare Against an Independent Oxygen Analyzer
Using an approved calibrated oxygen analyzer, compare the Carestation 750 reading with a controlled delivered oxygen concentration.

Do not adjust the machine solely to force agreement without following manufacturer procedures.

**Expected outcome:** The displayed FiO2 and independent analyzer show clinically consistent behavior under the test conditions. If they do, proceed to final checkout.

### 9. Complete Final Checkout
After correction, verify:

- O2 calibration
- Stable FiO2 measurement
- Response to changes in oxygen concentration
- Relevant alarms
- Gas delivery
- Required system checkout

**Expected outcome:** Oxygen monitoring and delivery behave normally and checkout passes. Troubleshooting can stop.

### 10. Escalate an Unresolved O2 Measurement Problem
If oxygen measurement remains inaccurate, unstable, or uncalibratable after supplies, sampling, external components, and approved calibration have been checked, stop troubleshooting.

**Expected outcome:** The machine is removed from service for qualified technical evaluation.

## If the Problem Persists
Common external causes have been ruled out. Remaining possibilities include internal oxygen-sensing circuitry, pneumatic sampling paths, internal gas-control issues, signal processing, calibration data, or other service-level conditions.

The Carestation 750 should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired or configured only by qualified personnel

After repair, verify oxygen delivery and measurement with approved independent test equipment and complete all required checkout procedures.

Knowing when unreliable FiO2 measurement requires removal from service is proper troubleshooting.

## Clinical Use Tip
Anesthesia equipment with questionable oxygen measurement should not be relied on until both oxygen delivery and displayed FiO2 have been independently verified.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Separate oxygen delivery problems from oxygen measurement problems and verify external gas supplies and sampling paths before assuming an internal defect. Calibration and independent verification should both succeed before the machine returns to service.

That is successful troubleshooting.
