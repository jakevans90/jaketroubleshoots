---
schemaVersion: 1
title: "ZOLL X Series Advanced Defibrillator - SpO2 Sensor Not Detected or No Saturation Reading"
issueTitle: "SpO2 Sensor Not Detected or No Saturation Reading"
description: "SpO2 sensor is not detected or saturation is absent because of sensor, cable, placement, perfusion, motion, connection, or configuration issues."
assetType: "Defibrillator"
manufacturer: "ZOLL"
model: "X Series Advanced"
slug: "zoll-x-series-advanced-spo2-sensor-not-detected-or-no-saturation-reading"
dateAdded: "2026-08-07"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported the X Series Advanced would not display an SpO2 value with the patient sensor attached."
  cause: "Clinical Engineering found the connected SpO2 sensor cable had intermittent damage and was not consistently recognized."
  resolution: "Replaced the defective cable and verified stable sensor recognition, pleth waveform, and SpO2 operation with approved test equipment."
helpfulDetails:
  - "Sensor detection status"
  - "Pleth waveform present or absent"
  - "Sensor type"
  - "Measurement site"
  - "Sensor and cable condition"
  - "Connector condition"
  - "Motion or low-perfusion conditions"
  - "Known-good sensor or cable result"
  - "Alarm behavior"
  - "Final device status"
---

## What This Guide Helps With

SpO2 sensor is not detected or saturation is absent because of sensor, cable, placement, perfusion, motion, connection, or configuration issues.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Oxygenation Monitoring
If continuous oxygen saturation monitoring is clinically required, provide another verified SpO2 monitor or appropriate alternate monitoring before troubleshooting.

Do not rely on a missing or clearly unreliable saturation value.

**Expected outcome:** Patient oxygenation monitoring continues safely.

### 2. Confirm the Exact SpO2 Condition
Determine whether the sensor is not detected, a value never appears, the reading drops in and out, the pleth waveform is missing, or the displayed value is clearly unreliable.

Note whether the problem occurs with one sensor or multiple sensors.

**Expected outcome:** The failure is clearly identified and can be reproduced when appropriate.

### 3. Inspect Sensor Placement
Check that the sensor is correctly positioned on an appropriate measurement site and is not excessively loose, tight, contaminated, or obstructed.

Consider nail coverings, strong ambient light, patient motion, or poor peripheral perfusion when clinically relevant.

**Expected outcome:** Proper sensor placement produces a stable signal. If the reading returns and remains reliable, proceed to final verification.

### 4. Inspect the Sensor and Cable
Inspect the SpO2 sensor, extension cable if present, and monitor connector for damage, contamination, bent contacts, strain damage, or incomplete insertion.

Reconnect each accessible connection securely.

**Expected outcome:** The sensor is securely connected and recognized. If correcting the connection restores the reading, troubleshooting can stop after verification.

### 5. Verify Compatible Accessories
Confirm the sensor and any intermediate cable are compatible with the installed SpO2 technology and intended for the device.

Do not assume that a physically fitting sensor is electrically or functionally compatible.

**Expected outcome:** A verified compatible sensor is connected. If the original accessory was incompatible, replace it and verify operation.

### 6. Reduce Motion and Perfusion-Related Interference
When clinically appropriate, test at a well-perfused site and minimize movement.

Compare signal quality and pleth behavior while the sensor is undisturbed.

**Expected outcome:** A stable pleth and saturation value appear under appropriate measurement conditions.

### 7. Substitute a Known-Good Sensor and Cable
Use known-good compatible SpO2 accessories when available.

If the monitor works normally with known-good accessories, remove the suspect sensor or cable from service.

**Expected outcome:** Normal SpO2 acquisition identifies the original accessory as the cause. Replace it and proceed to final verification.

### 8. Perform Final Functional Verification
Using approved test equipment where appropriate, verify sensor recognition, signal acquisition, displayed saturation, pleth waveform, and applicable alarm behavior.

**Expected outcome:** The SpO2 channel operates reliably with verified accessories. If all checks pass, troubleshooting is complete.

## If the Problem Persists

Common external causes involving sensor placement, compatibility, cabling, perfusion, and motion have been ruled out. The remaining cause may involve the SpO2 input module, connector assembly, configuration, signal processing, or another service-level fault.

The device should be:

- Removed from service if SpO2 monitoring is required and unreliable
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Complete applicable physiological-monitoring functional testing before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Confirm the entire sensor-to-monitor path before replacing the defibrillator; disposable sensors and extension cables are frequent external failure points.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**
## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain alternate oxygenation monitoring, evaluate placement and accessories before assuming an internal fault, verify the full signal path using known-good components, and remove the device from service when reliable SpO2 monitoring cannot be confirmed.

That is successful troubleshooting.
