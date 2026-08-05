---
schemaVersion: 1
title: "Masimo Rad-97 Pulse Oximeter - Signal IQ Poor Or Pleth Waveform Missing"
issueTitle: "Signal IQ Poor Or Pleth Waveform Missing"
description: "Poor signal quality or absent pleth waveform caused by motion, placement, perfusion, sensor damage, cable problems, or display configuration."
assetType: "Pulse Oximeter"
manufacturer: "Masimo"
model: "Rad-97"
slug: "masimo-rad-97-signal-iq-poor-or-pleth-waveform-missing"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported poor Signal IQ and no visible pleth waveform during pulse oximetry monitoring."
  cause: "Clinical Engineering found a damaged patient cable that produced an unstable signal when flexed near the connector."
  resolution: "Replaced the patient cable with a compatible approved cable, confirmed stable Signal IQ and pleth waveform, verified alarms, and returned the monitor to service."
helpfulDetails:
  - "Signal IQ indication"
  - "Pleth waveform status"
  - "Numerical reading behavior"
  - "Sensor site and perfusion condition"
  - "Patient movement or vibration"
  - "Sensor and cable condition"
  - "Display profile or waveform setting"
  - "Known-good accessory results"
  - "Simulator results"
  - "Final alarm and functional test results"
---

## What This Guide Helps With

Poor signal quality or absent pleth waveform caused by motion, placement, perfusion, sensor damage, cable problems, or display configuration.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Monitoring

Do not continue using unreliable monitoring while a patient depends on it. Move the patient to another verified monitor or establish an appropriate alternate monitoring method before troubleshooting.

Expected outcome: Patient monitoring remains continuous during evaluation.

### 2. Confirm the Signal Problem

Observe whether Signal IQ is consistently poor, the pleth waveform is missing, or both conditions occur together.

Determine whether numerical values are present, unstable, delayed, or absent. Confirm whether the issue affects one patient, one sensor, or every setup.

Expected outcome: The reported condition is reproduced and clearly defined.

### 3. Check the Sensor Site and Perfusion

Inspect the site for cold skin, low perfusion, edema, excessive pressure, nail coverings, poor contact, or placement on an extremity affected by a blood pressure cuff.

Use a clinically appropriate alternate site when authorized.

Expected outcome: Signal IQ improves and a stable pleth waveform appears. If it remains stable, troubleshooting can stop.

### 4. Correct Sensor Placement

Verify that the sensor is properly aligned, fully seated, and secure without being overly tight.

Ensure the optical components face each other correctly and are not obstructed by contamination, adhesive folds, or damaged material.

Expected outcome: A consistent waveform and signal quality indication are restored. If so, troubleshooting can stop.

### 5. Minimize Motion and Cable Strain

Stabilize the extremity and route the patient cable to prevent pulling, swinging, or repeated movement at the sensor.

Check for tremor, shivering, transport vibration, or nearby equipment contacting the cable.

Expected outcome: Signal quality becomes stable when motion and cable strain are reduced.

### 6. Check Display and Waveform Configuration

Verify that the pleth waveform is enabled and visible in the active display layout or profile.

Do not change clinical alarm limits or protected configuration settings without authorization. Compare the display with another Rad-97 using the same approved profile when available.

Expected outcome: The waveform is visible when enabled and configured correctly. If this resolves the issue, troubleshooting can stop.

### 7. Inspect All External Accessories

Inspect the sensor, patient cable, adapter, and monitor connection for damage, contamination, bent contacts, loose fit, or worn strain relief.

Reconnect all accessible connections securely.

Expected outcome: The signal remains stable without moving or holding the cable.

### 8. Test With Known-Good Accessories

Substitute a compatible known-good sensor and patient cable. Test the suspect accessories on another verified compatible device when appropriate.

Expected outcome: The problem follows a failed accessory or remains with the Rad-97. Replace the defective external accessory if identified.

### 9. Test Under Controlled Conditions

Remove the device from patient care and test it with an approved simulator or suitable controlled test subject.

Observe Signal IQ, pleth waveform, pulse rate, saturation response, and stability.

Expected outcome: The device produces a stable waveform and normal signal indication under controlled conditions.

### 10. Complete Functional Verification or Escalate

Verify waveform display, sensor detection, alarm response, and stable operation after correction.

If poor Signal IQ or a missing waveform continues with known-good accessories and controlled testing, remove the unit from service.

Expected outcome: The device either passes final verification or is routed for bench evaluation.

## If the Problem Persists

External causes involving patient site, perfusion, motion, sensor alignment, accessory damage, and display configuration have been ruled out.

The remaining cause may involve the sensor input connector, signal-processing system, display software, profile configuration, or another internal service-level condition. Remove the Rad-97 from service, label it Out of Service, and send it for qualified repair or bench evaluation using current manufacturer documentation and approved test equipment.

Do not perform unauthorized service-menu changes or internal board-level repair. Complete functional, waveform, and alarm verification before return to service.

## Clinical Use Tip

A displayed saturation value without a reliable pleth waveform should be interpreted cautiously until signal quality and the complete monitoring setup are verified.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain patient monitoring, verify signal quality from the patient outward, rule out placement and accessory problems before internal failure, and document the confirmed correction and final test results.

That is successful troubleshooting.
