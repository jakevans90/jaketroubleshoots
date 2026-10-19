---
schemaVersion: 1
title: "GE Healthcare CASE Stress Test System - Measurement Is Inaccurate or Will Not Calibrate"
issueTitle: "Measurement Is Inaccurate or Will Not Calibrate"
description: "Displayed or acquired measurements appear incorrect, inconsistent, or fail an applicable calibration or verification process."
assetType: "Stress Test System"
manufacturer: "GE Healthcare"
model: "CASE"
slug: "ge-healthcare-case-measurement-is-inaccurate-or-will-not-calibrate"
dateAdded: "2026-10-19"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that heart-rate values on the CASE system were intermittently inconsistent with the observed ECG signal."
  cause: "Clinical Engineering found poor ECG electrode contact producing unstable detection and incorrect derived heart-rate values."
  resolution: "Replaced the electrodes, verified stable ECG acquisition, and confirmed consistent heart-rate indication using an approved simulator."
helpfulDetails:
  - "Exact measurement affected"
  - "Reported and comparison values"
  - "Accessory condition"
  - "Patient connection condition"
  - "Settings observed"
  - "Reference instrument used"
  - "Known-good substitution results"
  - "Calibration or verification result"
  - "External interface status"
  - "Final device status"
---

## What This Guide Helps With
Displayed or acquired measurements appear incorrect, inconsistent, or fail an applicable calibration or verification process.

## Step-by-Step Troubleshooting
### 1. Protect the Patient From Unreliable Measurements
Do not continue a stress study when a measurement needed for clinical decision-making is known or suspected to be inaccurate. Stop the study as clinically appropriate and use verified alternate measurement equipment.

**Expected outcome:** Clinical decisions are not based on a questionable CASE measurement.

### 2. Identify the Exact Measurement
Determine what staff consider inaccurate: ECG-related values, heart rate, a connected blood-pressure measurement, exercise-device information, or another configured parameter. Record the observed value and the comparison source used by staff.

**Expected outcome:** The complaint is tied to one specific measurement path rather than a general assumption that the CASE system is inaccurate.

### 3. Verify Patient-Side Connections and Accessories
Inspect electrodes, patient cables, cuffs, sensors, or other applicable external accessories for correct placement, condition, and secure connection. Confirm the accessory is appropriate for the configured system.

**Expected outcome:** External measurement accessories are suitable and correctly applied. If correcting the accessory restores expected measurements, verify operation and stop troubleshooting.

### 4. Confirm Settings and Patient Information
Review accessible clinical settings relevant to the affected measurement. Confirm obvious patient-data or operating-mode errors have not created a misleading result.

Do not alter protected configuration or calibration values without authorized manufacturer procedures.

**Expected outcome:** User-accessible settings match the intended test setup.

### 5. Compare Against an Approved Reference
Use an appropriate simulator, reference device, or approved test instrument to compare the affected measurement. Test independently from the patient whenever possible.

**Expected outcome:** The CASE measurement agrees appropriately with the approved reference according to applicable manufacturer requirements. If it does, the equipment problem is not reproduced and troubleshooting can stop after documentation.

### 6. Test the Accessory Separately When Possible
If the measurement relies on a removable sensor, cable, cuff, or interface, replace it with a compatible known-good accessory and repeat the comparison.

**Expected outcome:** If the known-good accessory restores accurate measurements, remove the original accessory from service and complete final verification.

### 7. Check External Interface Communication
For measurements supplied by another configured device, inspect the external communication cable and verify the connected device itself is operating normally. Confirm the displayed measurement is being sourced from the intended device.

**Expected outcome:** The measurement source and CASE interface communicate consistently without data corruption or dropout.

### 8. Repeat Only Approved Calibration or Verification
If the affected measurement has an authorized calibration or verification procedure available to Clinical Engineering, perform it exactly according to current manufacturer documentation using approved equipment.

Do not guess calibration values or use undocumented service procedures.

**Expected outcome:** The measurement passes the approved process. If it does not, stop external troubleshooting and escalate.

### 9. Perform Final Functional Verification
Repeat the measurement comparison after correction and verify consistent performance across several observations or test points as required by the approved procedure.

**Expected outcome:** Measurements are repeatable and meet applicable manufacturer verification requirements. The issue is resolved and troubleshooting can stop.

## If the Problem Persists
External accessories, patient connections, accessible settings, reference comparisons, and external communication paths have been evaluated. Persistent inaccuracy may involve acquisition electronics, measurement processing, configuration, software, connected peripheral hardware, or calibration requiring authorized service.

Remove the system or affected measurement component from service, label it **Out of Service**, and perform bench evaluation using appropriate manufacturer documentation and approved test equipment. Calibration or internal repair must be completed only by qualified personnel.

Document the test equipment used and complete applicable return-to-service performance testing.

## Clinical Use Tip
Never use a questionable CASE-derived value to decide whether a patient should continue exercising; confirm critical measurements with a verified method.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Treat measurement accuracy as a patient-safety issue. Verify the measurement source, accessories, settings, and reference comparison before assuming internal failure, and escalate any device that cannot meet its approved performance requirements.

That is successful troubleshooting.
