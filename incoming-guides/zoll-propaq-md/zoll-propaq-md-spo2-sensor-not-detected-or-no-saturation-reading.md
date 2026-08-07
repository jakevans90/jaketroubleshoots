---
schemaVersion: 1
title: "ZOLL Propaq MD Defibrillator - SpO2 Sensor Not Detected or No Saturation Reading"
issueTitle: "SpO2 Sensor Not Detected or No Saturation Reading"
description: "SpO2 sensor is not recognized or no saturation value appears because of sensor, cable, connection, placement, signal quality, or configuration issues."
assetType: "Defibrillator"
manufacturer: "ZOLL"
model: "Propaq MD"
slug: "zoll-propaq-md-spo2-sensor-not-detected-or-no-saturation-reading"
dateAdded: "2026-08-07"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Propaq MD intermittently displayed no SpO2 value and did not consistently recognize the sensor."
  cause: "Clinical Engineering found an intermittent SpO2 patient cable that failed during gentle cable movement."
  resolution: "The defective cable was replaced and the unit passed simulated SpO2 testing with stable sensor recognition, waveform, and displayed values."
helpfulDetails:
  - "Sensor type and condition"
  - "Sensor recognition status"
  - "Pleth waveform present or absent"
  - "SpO2 value behavior"
  - "Patient cable condition"
  - "Known-good substitution results"
  - "Patient versus simulator result"
  - "Motion or perfusion concerns"
  - "Connector condition"
  - "Alarm behavior"
  - "Final device status"
---

## What This Guide Helps With

SpO2 sensor is not recognized or no saturation value appears because of sensor, cable, connection, placement, signal quality, or configuration issues.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Oxygenation Monitoring
If continuous oxygen saturation monitoring is clinically required, use another verified pulse oximeter while troubleshooting the affected Propaq MD SpO2 channel.

**Expected outcome:** Patient oxygenation continues to be monitored without reliance on the malfunctioning channel.

### 2. Confirm the Exact SpO2 Complaint
Determine whether the problem involves:

- Sensor not detected
- No displayed SpO2 value
- Intermittent reading
- Missing pleth waveform
- Reading only on certain patients
- Problem with one sensor
- Problem with all sensors

Use an appropriate SpO2 simulator when available.

**Expected outcome:** The symptom is clearly identified and reproducible.

### 3. Inspect the Sensor
Inspect the sensor for:

- Physical damage
- Contamination
- Damaged optical surfaces
- Frayed cable
- Bent contacts
- Improper sensor type
- Worn reusable components

Replace damaged or questionable disposable sensors.

**Expected outcome:** The sensor is intact and appropriate for the installed SpO2 technology.

### 4. Inspect the Intermediate Cable and Connections
If an intermediate patient cable is used, inspect its entire length and connectors.

Check for:

- Loose connections
- Broken locking features
- Bent pins
- Contamination
- Cable strain
- Intermittency during gentle movement

**Expected outcome:** The complete external SpO2 signal path is securely connected and undamaged.

### 5. Verify Sensor Placement and Signal Conditions
For a clinical complaint, check for:

- Poor sensor alignment
- Excessive motion
- Poor peripheral perfusion
- Strong ambient light
- Nail products or contamination when relevant
- Inappropriate measurement site

Avoid interpreting a patient-related no-read condition as equipment failure without controlled testing.

**Expected outcome:** The sensor has an appropriate measurement site and adequate conditions for signal acquisition.

### 6. Reseat All SpO2 Connections
Disconnect and reconnect the sensor, patient cable, and device connection as applicable.

Verify connectors are fully seated.

**Expected outcome:** The device recognizes the sensor and begins displaying a stable pleth waveform and saturation value. If so, complete verification and troubleshooting can stop.

### 7. Substitute Known-Good Compatible Accessories
Test with a known-good compatible sensor and, when used, a known-good intermediate cable.

Change one component at a time when practical.

**Expected outcome:** If known-good accessories restore readings, replace the defective external component and proceed to final verification.

### 8. Test With an SpO2 Simulator
Connect approved SpO2 test equipment compatible with the installed technology.

Observe:

- Sensor recognition
- Pleth waveform
- Saturation display
- Pulse rate
- Stability during testing

**Expected outcome:** The Propaq MD displays stable simulated values. If simulator performance is normal, investigate patient, sensor placement, or environmental causes rather than internal failure.

### 9. Perform Final Functional Verification
Confirm:

- Reliable sensor recognition
- Stable pleth waveform
- Stable SpO2 reading
- Appropriate pulse indication
- Alarm functionality appropriate to the test setup
- No interruption during normal cable movement

**Expected outcome:** SpO2 monitoring operates reliably and consistently. Troubleshooting can stop.

### 10. Escalate Persistent SpO2 Failure
If no reading or sensor detection persists with compatible known-good accessories and approved test equipment, remove the unit from service.

**Expected outcome:** A device-side interface, acquisition, configuration, or service-level problem receives qualified evaluation.

## If the Problem Persists

After sensor compatibility, sensor placement, external cables, connectors, known-good substitutions, perfusion considerations, and simulator testing have been ruled out, the remaining cause may involve the SpO2 acquisition interface, configuration, connector assembly, or another internal service-level condition.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Complete applicable SpO2, alarm, monitoring, defibrillator, and electrical safety verification before return to clinical service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

When SpO2 reliability is uncertain, confirm oxygenation with another verified monitoring method rather than relying on an intermittent value.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect continuous oxygenation monitoring, inspect the entire external sensor path before assuming internal failure, verify performance using compatible test equipment, escalate unresolved acquisition problems, and document both the correction and final verification.

That is successful troubleshooting.
