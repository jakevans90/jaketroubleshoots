---
schemaVersion: 1
title: "Getinge Cardiosave Hybrid / Rescue Intra-Aortic Balloon Pump - Fiber-Optic Pressure Sensor Will Not Zero or Calibrate"
issueTitle: "Fiber-Optic Pressure Sensor Will Not Zero or Calibrate"
description: "Troubleshoots fiber-optic pressure zeroing or calibration problems caused by connections, setup, handling, contamination, configuration, or external sensor issues."
assetType: "Intra-Aortic Balloon Pump"
manufacturer: "Getinge"
model: "Cardiosave Hybrid / Rescue"
slug: "getinge-cardiosave-hybrid-rescue-fiber-optic-pressure-sensor-will-not-zero-or-calibrate"
dateAdded: "2026-09-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Cardiosave fiber-optic pressure sensor would not complete zeroing."
  cause: "Clinical Engineering found the external fiber-optic connector was incompletely seated."
  resolution: "Clinical Engineering reseated the connector, verified successful zeroing and stable pressure response with approved testing, and returned the unit to service after required checks."
helpfulDetails:
  - "Exact zeroing or calibration behavior"
  - "Whether the sensor was detected"
  - "Fiber-optic connection condition"
  - "Evidence of contamination or moisture"
  - "Cable or interface damage"
  - "Configuration observed"
  - "Known-good sensor or test setup used"
  - "Drift after zeroing"
  - "Final functional verification"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots fiber-optic pressure zeroing or calibration problems caused by connections, setup, handling, contamination, configuration, or external sensor issues.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Reliable Pressure Monitoring

Do not rely on an unverified fiber-optic pressure value for patient management. Ensure another clinically appropriate pressure-monitoring method is available while the issue is evaluated.

Do not disconnect or manipulate an invasive patient catheter solely for technical troubleshooting while the patient depends on it.

**Expected outcome:** Reliable pressure monitoring and patient support remain available.

### 2. Confirm the Exact Zeroing or Calibration Failure

Determine whether the sensor is not detected, will not zero, zeroing repeatedly fails, the value immediately drifts, or calibration cannot be completed.

Record the actual displayed message or behavior if available.

**Expected outcome:** The failure is clearly identified rather than treated as a generic pressure problem.

### 3. Inspect the Fiber-Optic Connection

Check the accessible sensor connection for incomplete seating, contamination, moisture, bent or damaged components, or excessive strain.

Handle optical connections carefully and avoid touching sensitive surfaces unnecessarily.

**Expected outcome:** The fiber-optic connection is properly seated, clean, dry, and physically intact. If proper reconnection restores operation, verify stability and stop troubleshooting.

### 4. Inspect the External Sensor Cable or Catheter Interface

Examine accessible portions for sharp bends, crushing, tension, visible damage, or routing that may stress the connection.

Do not manipulate the invasive portion of the catheter.

**Expected outcome:** No external damage or mechanical stress is present.

### 5. Verify the Correct Pressure Input and Configuration

Confirm that the intended fiber-optic pressure input is selected and that the connected configuration matches the approved Cardiosave setup.

Do not enter unauthorized service menus or alter protected configuration parameters.

**Expected outcome:** The system is configured to use the connected sensor correctly.

### 6. Verify Appropriate Zeroing Conditions

Coordinate with clinical staff to ensure the sensor is being zeroed under the appropriate clinical conditions and according to approved practice. Clinical Engineering should verify equipment behavior rather than independently changing the patient's invasive setup.

**Expected outcome:** External setup conditions are appropriate for zeroing. If correcting the setup permits successful zeroing, verify the reading and stop troubleshooting.

### 7. Compare With a Known-Good Approved Sensor or Test Interface

When the device is off-patient and an approved test method is available, use a known-good sensor, simulator, or manufacturer-supported test accessory to distinguish a disposable/sensor problem from a Cardiosave input problem.

**Expected outcome:** Successful operation with a known-good test setup isolates the problem to the original external sensor or interface.

### 8. Evaluate for Drift or Intermittency

After successful zeroing, observe whether the value remains stable during controlled testing and whether gentle movement of external connections causes loss of signal.

**Expected outcome:** The pressure input remains stable. Recurring drift or connection-dependent failure indicates the system should not return to service until resolved.

### 9. Perform Final Functional Verification

Verify the pressure input, zeroing function, displayed waveform or value, alarms, trigger behavior when applicable, and required return-to-service checks.

**Expected outcome:** Fiber-optic pressure measurement remains stable throughout testing. Troubleshooting can stop.

### 10. Escalate Persistent Zero or Calibration Failure

If the Cardiosave fails with an approved known-good test setup, do not attempt internal optical alignment, board-level repair, or unauthorized calibration.

**Expected outcome:** The device is removed from service and escalated for qualified evaluation.

## If the Problem Persists

Common external connection, sensor, handling, setup, and configuration causes have been ruled out. Remaining possibilities include an internal optical interface, pressure-processing, configuration, or related service-level problem.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate Getinge documentation and approved test equipment
- Repaired or calibrated only by qualified personnel

Complete applicable pressure, trigger, alarm, operational, and electrical safety testing before return to clinical use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never accept a questionable fiber-optic pressure reading simply because a numeric value is displayed; use a verified alternate pressure source until the measurement path is confirmed.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Exact zeroing or calibration behavior
- Whether the sensor was detected
- Fiber-optic connection condition
- Evidence of contamination or moisture
- Cable or interface damage
- Configuration observed
- Known-good sensor or test setup used
- Drift after zeroing
- Final functional verification
- Final device status

## Final Thought

Fiber-optic pressure problems should be approached from the connection and setup outward. Maintain independent pressure monitoring, verify the sensor path before assuming internal failure, and escalate persistent zeroing or calibration problems for qualified service.

That is successful troubleshooting.
