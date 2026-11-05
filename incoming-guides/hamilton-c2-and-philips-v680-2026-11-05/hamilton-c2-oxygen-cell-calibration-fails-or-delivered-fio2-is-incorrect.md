---
schemaVersion: 1
title: "Hamilton C2 Ventilator - Oxygen Cell Calibration Fails or Delivered FiO2 Is Incorrect"
issueTitle: "Oxygen Cell Calibration Fails or Delivered FiO2 Is Incorrect"
description: "Troubleshoots oxygen calibration or FiO2 discrepancies caused by oxygen supply problems, sensor condition, leaks, connections, setup, or external measurement differences."
assetType: "Ventilator"
manufacturer: "Hamilton"
model: "C2"
slug: "hamilton-c2-oxygen-cell-calibration-fails-or-delivered-fio2-is-incorrect"
dateAdded: "2026-11-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the Hamilton C2 would not complete oxygen calibration."
  cause: "Clinical Engineering found the oxygen sensor connection not fully seated."
  resolution: "Reseated the sensor connection, completed oxygen calibration successfully, verified delivered oxygen with approved test equipment, and passed operational checks."
helpfulDetails:
  - "Exact oxygen message"
  - "Oxygen source used"
  - "Hose and fitting condition"
  - "Oxygen sensor condition"
  - "Calibration result"
  - "External analyzer used"
  - "Measured versus displayed oxygen"
  - "Circuit leak findings"
  - "Known-good substitution result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots oxygen calibration or FiO2 discrepancies caused by oxygen supply problems, sensor condition, leaks, connections, setup, or external measurement differences.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Oxygenation

Do not troubleshoot questionable oxygen delivery while a patient depends on the ventilator. Transfer the patient to another verified ventilator or approved ventilation source.

**Expected outcome:** Reliable ventilation and oxygen delivery are maintained independently of the affected C2.

### 2. Confirm the Oxygen Problem

Determine whether the issue is a failed oxygen calibration, displayed oxygen concentration that appears incorrect, discrepancy with an external analyzer, or an oxygen-related alarm.

Record the exact condition and when it occurs.

**Expected outcome:** The oxygen-related symptom is clearly identified and reproducible.

### 3. Verify the Oxygen Supply

Inspect the oxygen hose, wall connection, source connection, and fittings. Confirm that the intended oxygen source is available and connected securely.

Check for damaged hoses, loose fittings, crossed gas connections, or obvious supply interruption.

**Expected outcome:** A reliable oxygen source is correctly connected to the ventilator.

If correcting the supply restores normal oxygen operation, complete verification and stop troubleshooting.

### 4. Inspect the Breathing Circuit

Check the circuit for leaks, disconnected components, improperly installed accessories, or other conditions that could affect delivered or measured oxygen concentration.

**Expected outcome:** The breathing circuit is intact and appropriately assembled.

If correcting a circuit issue eliminates the FiO2 discrepancy, complete final verification.

### 5. Inspect the Oxygen Sensor or Cell

Inspect the externally serviceable oxygen cell or sensor interface for proper installation, secure connection, contamination, damage, or age-related deterioration if applicable.

Do not alter internal oxygen circuitry or calibration values outside authorized procedures.

**Expected outcome:** The oxygen sensing component is properly installed and physically intact.

### 6. Perform the Approved Oxygen Calibration

With the ventilator off the patient, perform the normal manufacturer-provided oxygen calibration procedure available to trained personnel.

Do not bypass failed calibration or enter unauthorized service settings.

**Expected outcome:** Oxygen calibration completes successfully.

If calibration succeeds and measured oxygen agrees during functional testing, troubleshooting can stop.

### 7. Compare With an Approved External Oxygen Analyzer

Using approved test equipment and a controlled bench setup, compare ventilator oxygen indication and delivered gas concentration.

Ensure the analyzer itself is properly prepared and suitable for the test.

**Expected outcome:** The ventilator and independent measurement are reasonably consistent according to applicable manufacturer/service criteria.

If the discrepancy disappears after correcting the external analyzer setup or ventilator connection, document the result and stop.

### 8. Substitute a Known-Good External Sensor When Applicable

If permitted and appropriate for the C2 configuration, install a known-good compatible oxygen sensing component and repeat calibration.

**Expected outcome:** The fault either follows the sensor or remains with the ventilator.

If replacing a defective sensor restores successful calibration and verification, complete required return-to-service checks.

### 9. Perform Final Functional Verification

Run the appropriate preoperational checks and verify oxygen delivery with an approved analyzer across an appropriate test setup. Confirm oxygen-related alarms and indicators function normally.

**Expected outcome:** Oxygen calibration passes and delivered oxygen is verified within applicable service criteria.

If successful, the ventilator may be returned to service.

## If the Problem Persists

If oxygen calibration continues to fail or delivered oxygen remains incorrect after supply, circuit, sensor installation, and external measurement factors have been ruled out, possible categories include internal oxygen regulation, mixing, sensing, pneumatic, or calibration problems.

The ventilator should be:

- Removed from service
- Labeled **Out of Service**
- Sent for qualified bench evaluation
- Tested using Hamilton documentation and approved gas-analysis equipment
- Repaired or calibrated only by qualified personnel
- Fully verified before return to clinical use

Do not compensate for inaccurate oxygen delivery by adjusting clinical settings around the fault.

## Clinical Use Tip

When oxygen accuracy is questionable, verify the patient is receiving reliable oxygen from another device before beginning any calibration or testing.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Reliable oxygen delivery is a patient-safety requirement. Confirm the gas source, circuit, sensor, and independent measurement before assuming an internal oxygen-control failure, and escalate any unresolved accuracy problem.

That is successful troubleshooting.
