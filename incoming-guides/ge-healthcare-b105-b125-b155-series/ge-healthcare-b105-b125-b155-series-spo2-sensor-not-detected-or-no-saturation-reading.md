---
schemaVersion: 1
title: "GE Healthcare B105 / B125 / B155 Series Patient Monitor - SpO2 Sensor Not Detected or No Saturation Reading"
issueTitle: "SpO2 Sensor Not Detected or No Saturation Reading"
description: "Troubleshoots missing SpO2 readings, sensor detection problems, damaged cables, poor application, low signal conditions, and external connection faults."
assetType: "Patient Monitor"
manufacturer: "GE Healthcare"
model: "B105 / B125 / B155 Series"
slug: "ge-healthcare-b105-b125-b155-series-spo2-sensor-not-detected-or-no-saturation-reading"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that the B125 monitor intermittently displayed no SpO2 reading and lost sensor detection."
  cause: "Clinical Engineering found the SpO2 sensor cable was damaged near the strain relief and failed when flexed."
  resolution: "Replaced the defective compatible sensor, verified a stable SpO2 signal and saturation display, tested alarms, and returned the monitor to service."
helpfulDetails:
  - "Exact displayed SpO2 message"
  - "Sensor type and compatibility"
  - "Sensor and cable condition"
  - "Patient site involved"
  - "Whether motion affected the reading"
  - "Known-good sensor result"
  - "Known-good cable result"
  - "Simulator test result"
  - "Monitor connector condition"
  - "Alarm behavior"
  - "Results before and after correction"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots missing SpO2 readings, sensor detection problems, damaged cables, poor application, low signal conditions, and external connection faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Oxygenation Monitoring
If SpO2 monitoring is clinically required and the displayed saturation is absent or unreliable, provide another verified method of monitoring before troubleshooting.

Do not leave a patient dependent on an unreliable SpO2 channel.

**Expected outcome:** The patient's oxygenation is being monitored reliably while the affected device is evaluated.

### 2. Confirm the Exact SpO2 Complaint
Determine whether:
- The sensor is not detected
- No SpO2 value is displayed
- A waveform is present without a value
- The reading is intermittent
- The problem occurs only with a particular sensor
- The problem occurs only at a particular patient site

Record any displayed status or alarm message without assuming its cause.

**Expected outcome:** The specific SpO2 failure pattern is identified.

### 3. Inspect and Reseat the SpO2 Connections
Inspect the sensor, extension/interconnect cable if present, and monitor connection for:
- Loose connections
- Bent or recessed contacts
- Cable cuts
- Cracked housings
- Contamination
- Strain-relief damage

Disconnect and reconnect each accessible external connection securely.

**Expected outcome:** The SpO2 signal path is physically intact and fully connected.

If reseating a loose connection restores normal readings, proceed to final verification.

### 4. Verify Sensor Compatibility
Confirm that the attached sensor and any interface cable are approved and compatible with the monitor's installed SpO2 technology.

Do not assume that connectors which physically fit are electrically or technologically compatible.

**Expected outcome:** The connected SpO2 accessories are appropriate for the monitor.

If an incompatible accessory was installed, replace it with an approved compatible accessory and verify operation.

### 5. Check Sensor Application and Measurement Site
Coordinate with clinical staff to verify appropriate sensor placement and adequate contact with the patient.

Consider external factors such as:
- Excessive patient motion
- Poor sensor positioning
- Excessive ambient light
- Poor peripheral perfusion
- Obstruction at the measurement site

Clinical staff should select or reposition the patient measurement site as appropriate.

**Expected outcome:** The sensor has appropriate patient contact and a usable physiologic signal.

If proper application restores a stable waveform and saturation value, troubleshooting can stop after verification.

### 6. Substitute a Known-Good Sensor
Use a compatible known-good SpO2 sensor to determine whether the problem follows the original sensor.

If an intermediate cable is used, substitute that component separately when available.

Change one component at a time.

**Expected outcome:** A known-good sensor and cable are detected and produce normal monitoring.

If the failure follows the original sensor or cable, replace the defective accessory.

### 7. Compare With an Approved SpO2 Simulator When Available
For bench evaluation, connect approved test equipment appropriate for the installed SpO2 technology.

Verify the monitor can detect a valid signal and display expected monitoring information.

**Expected outcome:** The monitor responds normally to a controlled known-good SpO2 input.

If simulator testing passes, focus on patient-side sensors, cables, application, and physiologic/environmental conditions.

### 8. Inspect the Monitor SpO2 Input
Inspect the accessible input connection for debris, contamination, looseness, or physical damage.

Do not probe or repair the internal connector without approved service procedures.

**Expected outcome:** The monitor input appears clean, intact, and mechanically secure.

### 9. Perform Final Functional Verification
After correction, verify:
- Sensor detection
- Stable SpO2 waveform or signal indication
- Stable saturation display
- No unintended sensor-disconnect condition
- Appropriate alarm function using an approved test method
- Stable response during normal cable movement

**Expected outcome:** SpO2 monitoring and alarms function reliably.

If all checks pass, document and return the monitor to service.

### 10. Escalate an Unresolved SpO2 Failure
If multiple compatible known-good sensors and cables fail, or approved simulator testing indicates the monitor cannot acquire SpO2, stop external troubleshooting.

**Expected outcome:** The monitor is removed from service for qualified evaluation.

## If the Problem Persists

Accessory compatibility, connections, patient application, known-good sensors, and accessible monitor connections have been checked. Remaining causes may involve the SpO2 acquisition subsystem, input interface, installed parameter hardware, configuration, or another service-level condition.

The monitor should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired or configured only by qualified personnel

After repair, verify SpO2 acquisition, sensor detection, alarm operation, and required overall monitor functions before return to service.

Knowing when the problem no longer follows an external SpO2 accessory is proper troubleshooting.

## Clinical Use Tip

When comparing SpO2 accessories, verify technology compatibility first; a physically connectable sensor is not automatically compatible with the monitor.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**




## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain reliable oxygenation monitoring, verify compatibility and the complete external sensor path before suspecting the monitor, and use controlled substitutions to separate accessory failures from equipment faults. Escalate unresolved acquisition problems and document the verified findings.

That is successful troubleshooting.
