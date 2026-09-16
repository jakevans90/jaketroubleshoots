---
schemaVersion: 1
title: "Getinge ROTAFLOW II Extracorporeal Membrane Oxygenation (ECMO) System - Flow Sensor Not Detected, Will Not Zero, or Reading Is Incorrect"
issueTitle: "Flow Sensor Not Detected, Will Not Zero, or Reading Is Incorrect"
description: "Troubleshoots missing, inaccurate, unstable, or non-zeroing flow measurements caused by sensor connection, placement, tubing, contamination, positioning, or setup."
assetType: "Extracorporeal Membrane Oxygenation (ECMO) System"
manufacturer: "Getinge"
model: "ROTAFLOW II"
slug: "getinge-rotaflow-ii-flow-sensor-not-detected-will-not-zero-or-reading-is-incorrect"
dateAdded: "2026-09-16"
taxonomyMode: "reuse"
ccr:
  complaint: "ECMO staff reported the ROTAFLOW II flow sensor was detected but displayed an unstable flow value during setup."
  cause: "Clinical Engineering found the flow sensor incompletely seated around the tubing at the measurement location."
  resolution: "Repositioned and fully seated the flow sensor, verified stable measurement response on the approved test setup, completed functional checks, and returned the system to service."
helpfulDetails:
  - "Exact alarm or displayed message"
  - "Whether sensor was detected"
  - "Zeroing result"
  - "Sensor and cable condition"
  - "Sensor orientation and placement"
  - "Tubing condition at measurement point"
  - "Known-good sensor result"
  - "Flow behavior versus pump-speed changes"
  - "Reading stability after correction"
  - "Final functional test results"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots missing, inaccurate, unstable, or non-zeroing flow measurements caused by sensor connection, placement, tubing, contamination, positioning, or setup.

## Step-by-Step Troubleshooting
### 1. Protect the Patient and Confirm Flow Independently
Do not rely on a questionable flow value for patient management. Notify the ECMO clinical team and maintain support using approved alternate clinical information and backup equipment as required.

Do not manipulate a patient-connected ECMO circuit solely to troubleshoot a sensor.

**Expected outcome:** Patient management does not depend on an unreliable displayed flow measurement.

### 2. Confirm the Exact Flow-Sensor Problem
Determine whether the sensor:
- Is not detected
- Will not zero
- Displays no flow
- Displays an implausible value
- Fluctuates unexpectedly
- Changes with cable movement or sensor repositioning
- Produces an alarm or message

Document the displayed value and operating conditions.

**Expected outcome:** The problem is specifically identified before components are moved or exchanged.

### 3. Inspect the Sensor and Cable Connection
Verify the flow sensor is securely connected and inspect accessible cable and connector surfaces for:
- Loose engagement
- Bent contacts
- Cuts or pinching
- Fluid contamination
- Strain at cable entry points

Do not continue using a damaged sensing cable.

**Expected outcome:** The connection is secure and the sensor is detected. If reseating the connection corrects the condition, proceed to verification.

### 4. Verify Sensor Placement
Confirm the flow sensor is installed on the appropriate circuit location and positioned according to the approved ROTAFLOW II setup.

Check for:
- Incorrect orientation
- Incomplete closure or seating around the tubing
- Sensor positioned over an unsuitable tubing section
- Tubing pulled or twisted through the sensor
- Mechanical stress on the sensor

**Expected outcome:** The sensor is correctly positioned and securely coupled to the tubing.

### 5. Inspect the Tubing at the Measurement Site
Without disrupting patient support, or using a bench circuit when necessary, inspect the tubing where the sensor is applied for:
- Kinking
- Flattening
- Distortion
- Contamination between sensor and tubing
- Incorrect tubing placement
- Excessive tension

**Expected outcome:** The measurement site is appropriate and mechanically undistorted.

### 6. Verify Zeroing Conditions
If zeroing is required by the applicable operating procedure, ensure the system is placed in the proper safe condition before attempting the zero procedure.

Clinical personnel must manage any circuit condition required to create zero-flow conditions on patient-connected equipment.

Do not improvise clamps or alter ECMO flow solely for a technical test.

**Expected outcome:** The sensor zeros successfully when the correct clinical and manufacturer-defined conditions are present.

### 7. Test With a Known-Good Compatible Sensor
When available, test the console or flow-measurement channel using a known-good compatible sensor and suitable non-patient setup.

Avoid exchanging sensors on an active ECMO circuit unless directed by the clinical team and applicable procedure.

**Expected outcome:** Normal readings with a known-good sensor isolate the problem to the original sensor, cable, or its positioning.

### 8. Compare the Reading With the Test Setup
On a controlled bench setup, compare displayed flow behavior with expected changes in pump operation. Look for:
- Appropriate directional response
- Smooth changes with pump speed
- Stable values at a steady operating condition
- Absence of unexplained jumps or dropouts

Do not invent calibration adjustments or enter restricted service functions.

**Expected outcome:** Flow measurement responds logically and remains stable.

### 9. Perform Final Functional Verification
After correction, verify:
- Sensor is consistently detected
- Zeroing completes when applicable
- Flow display is stable
- Measurement responds appropriately to controlled test changes
- No related alarms remain
- Cable and sensor positioning remain secure

**Expected outcome:** Flow monitoring is reliable and repeatable. Troubleshooting can stop after required return-to-service testing.

### 10. Escalate Persistent Flow Measurement Problems
If a known-good sensor, proper positioning, correct zeroing conditions, and secure connections do not restore reliable measurements, stop troubleshooting.

**Expected outcome:** The system is removed from service for flow-measurement channel or internal electronics evaluation.

## If the Problem Persists
External sensor connection, placement, tubing condition, zeroing conditions, and known-good substitution have been ruled out. Remaining possibilities include a failed sensor channel, internal communication problem, configuration issue, or other service-level fault.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate Getinge documentation and approved test equipment
- Repaired or configured only by qualified personnel

Following repair, complete manufacturer-appropriate flow monitoring and system functional verification before clinical release.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
Treat an implausible ECMO flow display as unreliable until verified; never make circuit or patient-management decisions from a questionable single measurement.

## Work Order Documentation (CCR Method)
<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)
<!-- Helpful details come from front matter. -->

## Final Thought
Maintain safe patient support, verify sensor connection and placement before assuming a measurement-system failure, confirm readings under controlled conditions, and escalate unresolved inaccuracies.

That is successful troubleshooting.
