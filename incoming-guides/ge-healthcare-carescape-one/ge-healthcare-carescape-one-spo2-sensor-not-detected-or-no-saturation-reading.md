---
schemaVersion: 1
title: "GE Healthcare CARESCAPE ONE Patient Monitor - SpO2 Sensor Not Detected or No Saturation Reading"
issueTitle: "SpO2 Sensor Not Detected or No Saturation Reading"
description: "Troubleshoots absent SpO2 detection or saturation readings caused by sensor, cable, placement, perfusion, connection, compatibility, or environmental issues."
assetType: "Patient Monitor"
manufacturer: "GE Healthcare"
model: "CARESCAPE ONE"
slug: "ge-healthcare-carescape-one-spo2-sensor-not-detected-or-no-saturation-reading"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported the CARESCAPE ONE would not detect the SpO2 sensor and displayed no saturation value."
  cause: "Clinical Engineering found the SpO2 sensor cable was damaged near the connector and failed with movement."
  resolution: "The damaged sensor was replaced with a compatible known-good sensor, and stable pleth, saturation, pulse rate, and alarm operation were verified."
helpfulDetails:
  - "Whether the sensor was detected."
  - "Presence or absence of pleth waveform."
  - "Sensor type used."
  - "Sensor site and placement condition."
  - "Patient motion or low-perfusion concerns."
  - "Cable and connector condition."
  - "Known-good sensor results."
  - "Results on another compatible monitor."
  - "Simulator or test results."
  - "Final SpO2 and alarm status."
---
## What This Guide Helps With

Troubleshoots absent SpO2 detection or saturation readings caused by sensor, cable, placement, perfusion, connection, compatibility, or environmental issues.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Verify Oxygenation Another Way
If SpO2 is clinically required and unavailable, establish oxygenation monitoring using another verified device or approved method while troubleshooting.

Treat unexpected low or absent readings as potentially clinical until patient condition is independently assessed.

**Expected outcome:** Patient oxygenation is safely monitored while the equipment problem is evaluated.

### 2. Confirm the Exact SpO2 Complaint
Determine whether:
- The sensor is not detected.
- A waveform is absent.
- A waveform is present but no numeric saturation appears.
- The value is intermittent.
- The issue occurs with one sensor or all sensors.
- The problem began after sensor, cable, module, or patient change.

**Expected outcome:** The symptom is clearly identified.

### 3. Verify Sensor Placement and Patient Factors
Inspect sensor placement for:
- Correct application.
- Excessive movement.
- Poor alignment.
- Moisture.
- Tight or loose placement.
- Low peripheral perfusion.
- Nail products or other site conditions when relevant.

Reposition or select another clinically appropriate site if needed.

**Expected outcome:** The sensor has an appropriate measurement site. If a stable reading returns, verify alarm function and stop troubleshooting.

### 4. Inspect the SpO2 Sensor and Cable
Check the sensor, extension cable if present, and external connector for damage, contamination, fraying, cracked housings, bent contacts, or loose engagement.

Remove visibly damaged accessories from service.

**Expected outcome:** The external SpO2 signal path is intact. If reconnecting a loose cable restores measurement, stop after verification.

### 5. Reseat All External Connections
Disconnect and reconnect the SpO2 sensor and extension cable, if used, ensuring each connection is fully seated.

Inspect the monitor or parameter interface externally for debris or damage.

**Expected outcome:** The sensor is recognized and a pleth waveform and numeric reading are produced when appropriate.

### 6. Substitute a Known-Good Compatible Sensor
Use a known-good compatible SpO2 sensor and cable appropriate to the installed technology and configuration.

Avoid assuming all SpO2 sensors are interchangeable.

**Expected outcome:** If the known-good sensor works, remove the original accessory from service. If the known-good sensor also fails, continue troubleshooting.

### 7. Compare With a Known-Good Monitoring Path
If practical, test the suspect sensor on another compatible monitor or test the CARESCAPE ONE with known-good accessories and a suitable simulator or test source.

**Expected outcome:** The problem follows either the accessory or the monitor/parameter path.

### 8. Check Environmental and Motion Causes
Determine whether the no-read condition corresponds to patient motion, bright external light, transport vibration, or poor site perfusion.

Reduce external interference where clinically appropriate.

**Expected outcome:** A stable pleth waveform and saturation value are obtained under appropriate conditions. If so, troubleshooting can stop.

### 9. Verify SpO2 Function and Alarms
Using approved test equipment or an appropriate functional test method, verify:
- Sensor detection.
- Pleth waveform.
- Numeric SpO2 response.
- Pulse rate response.
- SpO2 alarm annunciation.

**Expected outcome:** SpO2 monitoring and associated alarms operate correctly and consistently.

### 10. Escalate an Unresolved SpO2 Failure
If the sensor remains unrecognized or no valid signal is obtained with known-good compatible accessories and appropriate test conditions, stop external troubleshooting.

**Expected outcome:** Unreliable SpO2 monitoring equipment is removed from clinical use.

## If the Problem Persists

Common external causes have been ruled out. The remaining issue may involve the SpO2 parameter hardware, parameter module, connector interface, internal communication, configuration, software, or another service-level fault.

The affected equipment should be:
- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

After repair, verify SpO2 detection, waveform, numerical response, alarms, and overall monitor functionality before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A missing SpO2 value can be caused by the patient, sensor site, or equipment; confirm oxygenation independently before assuming monitor failure.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->
## Final Thought

Trace SpO2 complaints from the patient site through the sensor and external connection before assuming internal failure. Known-good substitutions and functional testing provide a logical stopping point, and unreliable oxygen saturation monitoring must be escalated appropriately.

That is successful troubleshooting.
