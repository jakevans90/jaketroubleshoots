---
schemaVersion: 1
title: "Newport e360 Ventilator - Internal Oxygen Sensor Will Not Calibrate or FiO2 Display Drifts"
issueTitle: "Internal Oxygen Sensor Will Not Calibrate or FiO2 Display Drifts"
description: "Addresses oxygen-sensor calibration failure or drifting FiO2 indication caused by gas supplies, sensor condition, circuit setup, calibration conditions, or measurement faults."
assetType: "Ventilator"
manufacturer: "Newport"
model: "e360"
slug: "newport-e360-internal-oxygen-sensor-will-not-calibrate-or-fio2-display-drifts"
dateAdded: "2026-11-06"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the Newport e360 FiO2 display drifted despite a stable oxygen setting."
  cause: "Clinical Engineering found the replaceable oxygen sensor would not maintain calibration while independent oxygen delivery remained stable."
  resolution: "The oxygen sensor was replaced, calibration completed successfully, and displayed FiO2 was verified against an external oxygen analyzer."
helpfulDetails:
  - "Set FiO2"
  - "Displayed FiO2"
  - "Independent analyzer reading"
  - "Calibration result"
  - "Air and oxygen supply condition"
  - "Sensor condition"
  - "Known-good sensor substitution"
  - "Drift observed over time"
  - "Oxygen alarm behavior"
  - "Final device status"
---

## What This Guide Helps With

Addresses oxygen-sensor calibration failure or drifting FiO2 indication caused by gas supplies, sensor condition, circuit setup, calibration conditions, or measurement faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Independently Verify Oxygen
Do not rely on a questionable FiO2 display for patient management. Move the patient to a verified ventilator if oxygen measurement or delivery cannot be trusted.

Use an approved external oxygen analyzer to distinguish a display problem from an actual gas-delivery problem.

**Expected outcome:** The patient is protected and actual delivered oxygen concentration is independently known.

### 2. Compare Displayed and Measured FiO2
Allow the system and external analyzer to stabilize under controlled bench conditions.

Compare the ventilator display with the independent measurement.

**Expected outcome:** The independent analyzer establishes whether the problem is actual oxygen delivery or oxygen-sensor indication.

### 3. Verify Air and Oxygen Supplies
Check both gas supplies and associated hoses for secure connections and proper availability.

**Expected outcome:** Stable gas supplies are confirmed. If an external supply problem explains the unstable reading and correcting it restores normal operation, troubleshooting can stop after verification.

### 4. Inspect the Breathing Circuit
Check for major leaks, unusual adapters, incorrect setup, or other external conditions that could affect the gas mixture being sampled.

**Expected outcome:** The circuit is correctly configured and stable.

### 5. Inspect the Oxygen Sensor Externally
Where the sensor is externally accessible under approved service procedures, inspect its seating, connector, age or condition information if available, and evidence of contamination or damage.

Do not disassemble the sensor.

**Expected outcome:** The sensor is properly installed and physically acceptable.

### 6. Perform Approved Oxygen-Sensor Calibration
Using the required gas conditions and manufacturer-approved procedure, attempt calibration.

Do not alter hidden calibration constants or bypass a failed calibration.

**Expected outcome:** Calibration completes successfully and subsequent readings stabilize. If so, continue to verification.

### 7. Substitute a Known-Good Sensor When Permitted
If the sensor is a qualified replaceable service item, install a compatible known-good or approved replacement sensor.

**Expected outcome:** Calibration succeeds and displayed FiO2 agrees with independent measurement. If so, the original sensor was the cause and troubleshooting can stop after final testing.

### 8. Check for Drift Over Time
Operate the ventilator on a test lung and monitor displayed and independently measured FiO2 over a controlled observation period.

**Expected outcome:** The displayed oxygen concentration remains stable and tracks independent measurement appropriately.

### 9. Verify Multiple Oxygen Settings
Where permitted, compare displayed and measured oxygen concentration at more than one commanded FiO2.

**Expected outcome:** The ventilator indicates oxygen concentration consistently across the tested range according to approved acceptance criteria.

### 10. Escalate Persistent Calibration or Drift
If a verified gas supply, correct setup, approved calibration, and known-good sensor do not resolve the problem, remove the ventilator from service.

**Expected outcome:** An unresolved oxygen-monitoring fault is escalated for service evaluation.

## If the Problem Persists

External gas sources, circuit setup, calibration conditions, and the replaceable oxygen sensor have been evaluated. Remaining causes may involve internal oxygen-sensor signal processing, wiring, gas delivery, calibration electronics, or other service-level faults.

Remove the ventilator from service, label it **Out of Service**, and send it for bench evaluation using manufacturer documentation and an approved oxygen analyzer. Service-level calibration or internal repair should be performed only by qualified personnel.

Return the ventilator to service only when displayed and independently measured oxygen concentrations agree within applicable manufacturer criteria and oxygen-related alarms function correctly.

## Clinical Use Tip

When the displayed FiO2 is questionable, use independent oxygen analysis to determine whether the problem is measurement, delivery, or both.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Separate oxygen-delivery problems from oxygen-measurement problems using independent verification. Check external supplies and sensor condition first, escalate unresolved calibration failures, and document measured results clearly.

That is successful troubleshooting.
