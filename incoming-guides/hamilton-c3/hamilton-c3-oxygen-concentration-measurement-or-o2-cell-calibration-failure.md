---
schemaVersion: 1
title: "Hamilton C3 Ventilator - Oxygen Concentration Measurement or O2 Cell Calibration Failure"
issueTitle: "Oxygen Concentration Measurement or O2 Cell Calibration Failure"
description: "Helps isolate oxygen-supply, connection, sensor, calibration-condition, configuration, or environmental causes of inaccurate oxygen measurement or calibration failure."
assetType: "Ventilator"
manufacturer: "Hamilton"
model: "C3"
slug: "hamilton-c3-oxygen-concentration-measurement-or-o2-cell-calibration-failure"
dateAdded: "2026-08-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the ventilator would not complete oxygen sensor calibration."
  cause: "Clinical Engineering found the oxygen supply connection partially disconnected, producing an unstable supply condition."
  resolution: "Secured the oxygen connection, completed the authorized calibration, and verified oxygen delivery with calibrated test equipment."
helpfulDetails:
  - "Exact displayed message"
  - "Oxygen source used"
  - "Hose condition"
  - "Supply connection status"
  - "When calibration failed"
  - "Sensor condition"
  - "Independent analyzer results"
  - "Configuration observed"
  - "Results after calibration"
  - "Final device status"
---

## What This Guide Helps With

Helps isolate oxygen-supply, connection, sensor, calibration-condition, configuration, or environmental causes of inaccurate oxygen measurement or calibration failure.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Verify Oxygen Delivery
Do not troubleshoot questionable oxygen measurement while a patient depends on the ventilator. If oxygen delivery or monitoring cannot be trusted, provide ventilation and oxygen using another verified device or method according to clinical protocol.

**Expected outcome:** The patient has reliable oxygen delivery and monitoring independent of the suspect Hamilton C3.

### 2. Confirm the Reported Condition
Determine whether the problem involves an oxygen concentration reading, failed calibration, unstable measurement, unexpected value, or loss of oxygen measurement.

Record the exact displayed message and whether the issue occurs during startup, calibration, or ventilation.

**Expected outcome:** The specific oxygen-measurement problem is identified without assuming sensor failure.

### 3. Verify the Oxygen Supply
Inspect the oxygen supply connection and hose for:

- Secure connection
- Kinks
- Visible damage
- Incorrect source connection
- Closed or unavailable supply
- Signs of contamination

Where appropriate, verify the source using approved test equipment or a known-good supply connection.

**Expected outcome:** A stable, appropriate oxygen source is available to the ventilator.

If restoring the oxygen supply clears the measurement or calibration problem and verification passes, troubleshooting can stop.

### 4. Inspect External Oxygen-Related Components
Inspect accessible sensor-related connections and externally replaceable oxygen-sensing components where applicable. Look for contamination, loose connections, moisture, obvious deterioration, or installation problems.

Do not access internal sensor circuitry or pneumatic assemblies unless authorized by approved service procedures.

**Expected outcome:** Accessible oxygen-measurement components are properly installed and undamaged.

If reseating or replacing an approved external component corrects the issue, proceed to final verification.

### 5. Confirm Calibration Conditions
Ensure the ventilator is not being calibrated under an unsuitable external condition, such as unstable gas supply, disconnected hoses, or an incorrectly assembled breathing system.

Follow only authorized Hamilton procedures for oxygen-sensor calibration.

**Expected outcome:** Calibration is attempted under appropriate, stable conditions.

If calibration completes successfully and measured oxygen remains stable afterward, troubleshooting can stop after verification.

### 6. Compare With Independent Oxygen Measurement
Using approved calibrated test equipment, compare the ventilator's delivered oxygen concentration with an independent measurement during an appropriate bench test.

Do not rely solely on the ventilator's displayed value when evaluating the reported problem.

**Expected outcome:** Independent testing confirms that oxygen concentration is being delivered and measured consistently.

If the delivered concentration is correct and the original problem does not recur, the device may proceed to return-to-service testing.

### 7. Check Relevant Configuration
Verify that the ventilator configuration reflects the installed oxygen-measurement hardware and intended operating setup. Avoid unauthorized configuration changes or service menus.

**Expected outcome:** No obvious configuration discrepancy explains the measurement or calibration failure.

If an authorized configuration correction resolves the issue, verify oxygen measurement before returning the ventilator to service.

### 8. Perform Final Functional Verification
Complete an off-patient functional check using approved test equipment. Verify stable oxygen measurement, expected response to changes in commanded oxygen concentration, and appropriate alarm behavior.

**Expected outcome:** Oxygen concentration measurement is stable, credible, and consistent with independent testing.

If all required checks pass, return the device to service according to policy.

## If the Problem Persists

If oxygen supply, external connections, calibration conditions, sensor installation, and configuration have been ruled out, the problem may involve an oxygen sensor requiring service replacement, internal gas-delivery control, internal measurement circuitry, calibration data, or another service-level condition.

The ventilator should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Hamilton service documentation and approved test equipment
- Repaired, calibrated, or configured only by qualified personnel
- Subjected to appropriate oxygen-delivery and ventilator performance testing before return to service

Knowing when oxygen measurement can no longer be trusted and escalating the device is proper troubleshooting.

## Clinical Use Tip

Do not return a ventilator to patient care when commanded and independently measured oxygen concentration cannot be reconciled.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Oxygen-measurement problems require verified patient support, confirmation of the gas source, and objective testing before internal failure is assumed. Escalate when measurement reliability remains uncertain and document the complete result.

That is successful troubleshooting.
