---
schemaVersion: 1
title: "Getinge Cardiosave Hybrid / Rescue Intra-Aortic Balloon Pump - Auto Timing Fails or Inflation and Deflation Markers Are Incorrect"
issueTitle: "Auto Timing Fails or Inflation and Deflation Markers Are Incorrect"
description: "Troubleshoots incorrect balloon timing associated with poor ECG or pressure signals, trigger selection, connections, interference, or configuration problems."
assetType: "Intra-Aortic Balloon Pump"
manufacturer: "Getinge"
model: "Cardiosave Hybrid / Rescue"
slug: "getinge-cardiosave-hybrid-rescue-auto-timing-fails-or-inflation-and-deflation-markers-are-incorrect"
dateAdded: "2026-09-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that automatic timing was unstable and the inflation marker moved inconsistently."
  cause: "Clinical Engineering found intermittent artifact from a damaged external ECG patient cable."
  resolution: "Clinical Engineering replaced the cable with an approved known-good cable, verified stable triggering and timing with simulation, completed functional testing, and returned the unit to service."
helpfulDetails:
  - "Selected trigger source"
  - "ECG waveform quality"
  - "Arterial pressure waveform quality"
  - "Inflation and deflation marker behavior"
  - "External cable condition"
  - "Known-good substitutions"
  - "Nearby interference sources"
  - "Results with simulator"
  - "Whether timing remained stable after correction"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots incorrect balloon timing associated with poor ECG or pressure signals, trigger selection, connections, interference, or configuration problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Ineffective Counterpulsation

Incorrect inflation or deflation timing can reduce support or adversely affect hemodynamics. If timing is unreliable during active therapy, notify the clinical team and establish safe alternate support when needed.

Do not experiment with timing settings on a patient for equipment troubleshooting.

**Expected outcome:** The patient is protected from continued unreliable counterpulsation.

### 2. Confirm the Timing Complaint

Observe whether automatic timing fails to establish, timing markers move unpredictably, or inflation and deflation consistently appear misplaced relative to the displayed waveform.

Record the selected trigger source and whether the issue is continuous or rhythm-dependent.

**Expected outcome:** The timing problem is clearly characterized without unnecessary configuration changes.

### 3. Evaluate ECG Signal Quality

If ECG is being used for triggering, inspect the displayed ECG for noise, dropouts, baseline disturbance, or inconsistent complex detection.

Check external ECG leads, electrodes, cables, and connectors.

**Expected outcome:** A clean and stable ECG signal is available. If correcting a lead or cable problem restores proper timing, verify stability and stop troubleshooting.

### 4. Evaluate Arterial Pressure Signal Quality

Inspect the arterial pressure waveform for damping, artifact, noise, or signal loss. Check external pressure cables, transducer connections, tubing, and accessible interfaces.

**Expected outcome:** The pressure waveform is stable and physiologically plausible. If correcting the pressure signal restores automatic timing, troubleshooting can stop.

### 5. Verify the Intended Trigger Source

Confirm that the Cardiosave is using the trigger source intended by the clinical team and that the selected source is actually present and usable.

Do not alter clinical configuration merely to clear a symptom without understanding why the original trigger failed.

**Expected outcome:** The trigger source and available signal agree. Correcting an unintended trigger selection may resolve the issue.

### 6. Look for External Electrical Interference

Check whether electrosurgical equipment, damaged cables, poorly placed leads, disconnected electrodes, power accessories, or other nearby equipment correlate with the timing disturbance.

Reposition or substitute accessible external components when clinically appropriate.

**Expected outcome:** Trigger signals remain stable without excessive interference. If removing an external interference source restores correct timing, troubleshooting can stop.

### 7. Inspect All Relevant Signal Connections

Verify that ECG and pressure cables are securely seated and free of bent contacts, contamination, damaged insulation, or strain.

**Expected outcome:** All signal connections remain secure during gentle movement. An intermittent external cable should be replaced with an approved known-good cable.

### 8. Test Timing With an Approved Simulator

Once the Cardiosave is off-patient, connect appropriate approved simulation equipment and provide stable known input signals. Observe whether automatic timing and inflation/deflation markers respond consistently.

**Expected outcome:** Correct timing with stable simulated signals indicates that external patient-side signals or clinical conditions likely contributed. Incorrect timing under controlled input requires escalation.

### 9. Complete Final Functional Verification

After any corrective action, verify trigger acquisition, timing stability, pumping response, alarms, display operation, and required return-to-service checks.

**Expected outcome:** Timing remains stable through controlled testing. Troubleshooting can stop.

### 10. Escalate Persistent Timing Errors

If timing remains incorrect with known-good simulated signals and external cables, do not pursue unauthorized software, internal board, or calibration adjustments.

**Expected outcome:** The device is removed from service and referred for qualified evaluation.

## If the Problem Persists

External ECG, pressure, trigger-source, connection, and interference causes have been ruled out. Remaining possibilities include internal signal-processing, timing-control, software, or configuration problems requiring service-level diagnosis.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate Getinge documentation and approved test equipment
- Repaired or configured only by qualified personnel

Following service, verify triggering, timing, alarms, pumping operation, and applicable electrical safety requirements before return to use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A timing complaint should prompt verification of both ECG and arterial pressure signal quality before assuming the IABP itself has failed.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Selected trigger source
- ECG waveform quality
- Arterial pressure waveform quality
- Inflation and deflation marker behavior
- External cable condition
- Known-good substitutions
- Nearby interference sources
- Results with simulator
- Whether timing remained stable after correction
- Final device status

## Final Thought

Correct timing depends on reliable input signals as well as proper pump operation. Protect the patient, verify ECG and pressure quality, connections, trigger selection, and interference first, then escalate any timing problem that persists under controlled simulation.

That is successful troubleshooting.
