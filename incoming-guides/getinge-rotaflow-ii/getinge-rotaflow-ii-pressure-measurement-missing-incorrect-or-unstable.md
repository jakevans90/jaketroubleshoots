---
schemaVersion: 1
title: "Getinge ROTAFLOW II Extracorporeal Membrane Oxygenation (ECMO) System - Pressure Measurement Missing, Incorrect, or Unstable"
issueTitle: "Pressure Measurement Missing, Incorrect, or Unstable"
description: "Troubleshoots absent, implausible, drifting, or unstable ECMO pressure measurements involving transducers, cables, tubing, zeroing, connections, and setup."
assetType: "Extracorporeal Membrane Oxygenation (ECMO) System"
manufacturer: "Getinge"
model: "ROTAFLOW II"
slug: "getinge-rotaflow-ii-pressure-measurement-missing-incorrect-or-unstable"
dateAdded: "2026-09-16"
taxonomyMode: "reuse"
ccr:
  complaint: "ECMO staff reported one ROTAFLOW II pressure channel displayed an unstable value during setup."
  cause: "Clinical Engineering found the external pressure transducer cable connection partially disengaged at the monitor interface."
  resolution: "Reseated the connection, verified stable zero and controlled pressure response with approved test equipment, completed alarm and functional checks, and returned the system to service."
helpfulDetails:
  - "Affected pressure channel"
  - "Exact displayed value or alarm"
  - "Whether zeroing succeeded"
  - "Transducer and cable condition"
  - "Pressure tubing condition"
  - "Connector condition"
  - "Known-good accessory substitution"
  - "Controlled test result"
  - "Whether other channels were normal"
  - "Final alarm and functional verification"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots absent, implausible, drifting, or unstable ECMO pressure measurements involving transducers, cables, tubing, zeroing, connections, and setup.

## Step-by-Step Troubleshooting
### 1. Protect the Patient and Do Not Rely on Questionable Pressure Data
Inform the clinical ECMO team whenever circuit pressure information is missing or unreliable. Use approved alternate monitoring and clinical assessment as required.

Do not change patient-connected circuit connections solely to troubleshoot the monitor.

**Expected outcome:** Patient management continues without dependence on unreliable pressure values.

### 2. Confirm the Exact Pressure Problem
Identify:
- Which pressure channel is affected
- Whether the value is blank, fixed, drifting, or unstable
- Whether the channel can be zeroed
- Whether the problem occurs continuously or intermittently
- Any displayed alarm or message
- Whether other pressure channels are normal

**Expected outcome:** The affected channel and failure pattern are clearly documented.

### 3. Inspect the Pressure Transducer and Cable
Verify the appropriate pressure measurement accessory is connected correctly. Inspect accessible components for:
- Loose connectors
- Damaged cable
- Cracked transducer housing
- Fluid contamination
- Bent contacts
- Strain or pinching

**Expected outcome:** The transducer and cable are secure and externally intact.

### 4. Inspect External Pressure Tubing and Connections
Clinical personnel should inspect patient-connected pressure lines for appropriate setup. On a bench setup, verify:
- Tubing is connected to the intended channel
- Connections are secure
- No obvious kink or obstruction is present
- No unintended open connection or leak is present
- Tubing is not pulling on the transducer

**Expected outcome:** The pressure pathway is correctly connected and mechanically intact.

### 5. Verify Transducer Position and Zeroing Conditions
Confirm the pressure transducer is positioned and zeroed according to the applicable clinical and manufacturer procedure.

Clinical personnel must establish the appropriate reference condition on a patient-connected circuit.

Do not compensate for an incorrect reading by applying undocumented offsets.

**Expected outcome:** Zeroing completes appropriately and the baseline is stable.

### 6. Check for Environmental or Mechanical Interference
Look for:
- Wet connectors
- Excessive cable movement
- Pump or equipment vibration transmitted to the transducer
- Pressure tubing contacting moving components
- Transducer hanging under tension

**Expected outcome:** The measurement setup remains mechanically stable.

### 7. Substitute a Known-Good Compatible Transducer or Cable
When appropriate, use a known-good compatible pressure transducer or cable on an approved non-patient test setup.

Do not exchange patient-connected circuit components without clinical coordination.

**Expected outcome:** If the problem follows the transducer or cable, remove that accessory from service. If it remains on the same channel, further system evaluation is required.

### 8. Compare Channel Behavior Under Controlled Test Conditions
Using approved test equipment, apply appropriate controlled pressure input when authorized by the manufacturer procedure and observe whether the measurement responds smoothly and consistently.

Do not perform unauthorized calibration.

**Expected outcome:** The displayed pressure responds consistently to controlled input and remains stable.

### 9. Perform Final Functional Verification
Verify:
- Correct channel identification
- Stable zero
- Appropriate response to test input
- Secure transducer connections
- No unexplained drift or dropout
- Related alarms and indications function as required

**Expected outcome:** Pressure monitoring is reliable and repeatable. Troubleshooting can stop.

### 10. Escalate Persistent Pressure Measurement Failure
If known-good accessories, proper zeroing, secure connections, and controlled testing do not restore reliable pressure measurement, remove the system from service.

**Expected outcome:** Internal pressure-channel, communication, or processing problems are referred for qualified service evaluation.

## If the Problem Persists
External transducer, tubing, connection, zeroing, positioning, and accessory causes have been ruled out. Remaining possibilities include an internal measurement channel, interface electronics, configuration, or communication failure.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate Getinge documentation and approved test equipment
- Repaired or configured only by qualified personnel

After service, complete appropriate pressure-channel, alarm, system, and return-to-service verification before clinical use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
A plausible-looking ECMO pressure value can still be wrong; investigate any measurement that conflicts with circuit behavior, other monitoring, or the clinical picture.

## Work Order Documentation (CCR Method)
<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)
<!-- Helpful details come from front matter. -->

## Final Thought
Protect the patient from unreliable monitoring, verify transducers, tubing, connections, and zeroing before assuming internal failure, and require stable verified measurements before return to service.

That is successful troubleshooting.
