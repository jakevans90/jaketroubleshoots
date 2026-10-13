---
schemaVersion: 1
title: "Getinge Flow-c Anesthesia Machine - Airway Pressure Is High, Low, or Inaccurate"
issueTitle: "Airway Pressure Is High, Low, or Inaccurate"
description: "Troubleshoots abnormal airway pressure caused by circuit obstruction, leaks, accessories, settings, sensing connections, patient-interface components, or measurement problems."
assetType: "Anesthesia Machine"
manufacturer: "Getinge"
model: "Flow-c"
slug: "getinge-flow-c-airway-pressure-is-high-low-or-inaccurate"
dateAdded: "2026-10-13"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported unexpectedly high airway-pressure readings from the Getinge Flow-c during setup."
  cause: "Clinical Engineering found a breathing-circuit filter visibly obstructed and increasing circuit resistance."
  resolution: "Clinical Engineering replaced the affected filter, verified airway pressure using approved test equipment, and confirmed normal ventilation and alarm performance."
helpfulDetails:
  - "Exact pressure alarm or message"
  - "Ventilation mode and settings"
  - "High, low, or inaccurate pressure behavior"
  - "Circuit and filter condition"
  - "Presence of kinks, blockage, or fluid"
  - "Sampling or sensing connection condition"
  - "Known-good substitutions"
  - "Independent pressure-test result"
  - "Alarm response"
  - "Final functional-test result"
  - "Final device status"
---
## What This Guide Helps With
Troubleshoots abnormal airway pressure caused by circuit obstruction, leaks, accessories, settings, sensing connections, patient-interface components, or measurement problems.

## Step-by-Step Troubleshooting
### 1. Protect the Patient and Maintain Ventilation
If airway pressure is unexpectedly high, low, or unreliable during patient care, immediately follow clinical procedures and move ventilation to a verified alternative when equipment malfunction is suspected. Do not troubleshoot the machine while the patient depends on it.

**Expected outcome:** Patient ventilation is safely maintained while the anesthesia machine is evaluated separately.

### 2. Confirm the Pressure Complaint
Determine whether pressure is actually abnormal, only the displayed value appears incorrect, or an alarm is being generated unexpectedly. Record ventilation mode, pressure-related settings, waveform behavior, and the exact alarm or message.

**Expected outcome:** The complaint is differentiated between true pressure abnormality and possible measurement error.

### 3. Inspect the Patient Circuit for Obstruction
Check breathing hoses, connectors, filters, adapters, and patient-interface components for kinks, crushing, fluid accumulation, blocked filters, improper assembly, or other restrictions.

**Expected outcome:** The breathing path is open and unobstructed. Removing an identified restriction restores expected pressure behavior.

### 4. Inspect for Leaks and Disconnections
Check the complete external breathing circuit for loose connections, damaged tubing, open ports, poorly seated components, or leaking accessories that could produce unexpectedly low pressure.

**Expected outcome:** The circuit is sealed and correctly assembled.

### 5. Verify Pressure-Related Settings and Controls
Confirm the selected ventilation mode and user-adjustable pressure, volume, and alarm settings match the intended clinical or test setup. Do not alter restricted configuration settings to force the machine to pass.

**Expected outcome:** The pressure behavior is evaluated using appropriate intended settings.

### 6. Check Sampling and Measurement Connections
Inspect accessible sensing, sampling, and monitoring connections associated with the breathing circuit. Confirm that tubing and adapters are correctly connected, undamaged, and not obstructed by fluid or contamination.

**Expected outcome:** External sensing pathways are connected and patent.

### 7. Compare With Approved Test Equipment
With the machine removed from patient use, connect appropriate anesthesia-system test equipment and compare airway-pressure behavior during controlled ventilation. Use a known-good circuit or appropriate removable accessory if needed to isolate the external breathing system.

**Expected outcome:** Measured pressure agrees with expected test behavior, or a repeatable machine-related discrepancy is identified.

### 8. Perform Final Functional Verification
After correcting the external cause, verify pressure generation, measurement, waveforms, relevant alarms, ventilation, and required pre-use checks.

**Expected outcome:** Airway pressure is stable and accurately represented under controlled testing.

## If the Problem Persists
If circuit obstruction, leaks, accessories, settings, external sensing connections, and test setup have been ruled out, the issue may involve internal pressure sensing, pneumatic regulation, valves, calibration, or another service-level problem.

Remove the Getinge Flow-c from service, label it **Out of Service**, and send it for bench evaluation. Use manufacturer documentation and approved pressure/flow test equipment for further evaluation. Internal pneumatic adjustments or calibration should be performed only by qualified personnel.

The machine must pass applicable pressure, ventilation, alarm, and functional tests before return to clinical use. Escalating rather than guessing at an internal cause is proper troubleshooting.

## Clinical Use Tip
Unexpected airway pressure can represent either a true ventilation hazard or a sensing problem; both require immediate verification away from the patient.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought
Airway-pressure complaints require immediate attention to patient safety, followed by systematic checks for obstruction, leaks, settings, and sensing connections. Verify performance independently before assuming internal failure and escalate any unresolved pressure abnormality.

That is successful troubleshooting.
