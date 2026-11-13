---
schemaVersion: 1
title: "Hamilton C2 Ventilator - CO2 or SpO2 Monitoring Module Is Not Detected"
issueTitle: "CO2 or SpO2 Monitoring Module Is Not Detected"
description: "Troubleshoots missing CO2 or SpO2 monitoring caused by disconnected modules, damaged sensors, contaminated connectors, incompatible accessories, configuration, or communication problems."
assetType: "Ventilator"
manufacturer: "Hamilton"
model: "C2"
slug: "hamilton-c2-co2-or-spo2-monitoring-module-is-not-detected"
dateAdded: "2026-11-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the Hamilton C2 did not recognize the connected SpO2 monitoring module."
  cause: "Clinical Engineering found the module connector not fully seated."
  resolution: "Reseated the module, verified SpO2 detection using an approved test setup, confirmed alarm operation, and returned the ventilator to service."
helpfulDetails:
  - "CO2 or SpO2 affected"
  - "Exact displayed message"
  - "Module detected or not detected"
  - "Sensor/cable condition"
  - "Connector condition"
  - "Compatible accessory confirmed"
  - "Known-good substitution result"
  - "Configuration observed"
  - "Alarm verification result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots missing CO2 or SpO2 monitoring caused by disconnected modules, damaged sensors, contaminated connectors, incompatible accessories, configuration, or communication problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Required Monitoring

If CO2 or SpO2 monitoring is clinically required and the C2 cannot provide it, use another verified monitoring method before troubleshooting.

Do not remove necessary monitoring from an actively supported patient.

**Expected outcome:** Required patient monitoring remains available independently.

### 2. Confirm What Is Not Detected

Determine whether the C2 does not recognize the monitoring module itself, recognizes the module but not the sensor, or displays the parameter without a valid measurement.

Record any displayed message.

**Expected outcome:** The missing component or communication stage is identified.

### 3. Inspect the Module Connection

Verify that the CO2 or SpO2 module is fully seated and connected to the intended interface.

Inspect accessible connectors for looseness, contamination, bent contacts, or damage.

**Expected outcome:** The module is properly connected and connectors are clean and intact.

If reseating restores detection, continue to final verification.

### 4. Inspect the Patient Sensor or Cable

Inspect the SpO2 sensor, CO2 sensor, adapter, sampling line, and associated cable as applicable.

Look for broken wires, cracked housings, contamination, moisture, occlusion, or improper assembly.

**Expected outcome:** The external sensor system is complete and undamaged.

### 5. Verify Compatible Accessories

Confirm that the installed module, cable, and sensor are approved and compatible with the C2 configuration.

Do not assume that physically similar accessories are interchangeable.

**Expected outcome:** All connected monitoring accessories are appropriate for the ventilator.

### 6. Substitute a Known-Good Sensor or Module

When available and permitted, substitute a known-good compatible sensor, cable, or module one component at a time.

**Expected outcome:** The failure follows an external component or remains with the ventilator interface.

If a known-good component restores operation, replace the defective accessory and proceed to final verification.

### 7. Check Accessible Monitoring Configuration

Verify that the intended monitoring function is enabled through normal authorized configuration and that no obvious configuration change explains its absence.

Do not enter restricted service menus or alter protected settings without authorization.

**Expected outcome:** Monitoring is appropriately configured for the installed hardware.

### 8. Verify Measurement Function

With an appropriate simulator, approved test method, or controlled test setup, verify that the module produces a stable measurement and associated alarms function.

**Expected outcome:** The C2 recognizes the module and displays reliable monitoring data.

If successful, troubleshooting can stop.

## If the Problem Persists

If known-good modules, sensors, cables, and authorized configuration have been verified but monitoring is still not detected, possible categories include interface electronics, communication hardware, software/configuration, or internal power to the module connection.

The ventilator should be:

- Removed from service if the failed monitoring function is required for intended use
- Labeled **Out of Service** when appropriate
- Sent for bench evaluation
- Evaluated using Hamilton service documentation and approved simulators/test equipment
- Repaired or configured only by qualified personnel
- Fully verified before clinical use

## Clinical Use Tip

A ventilator can continue ventilating while an integrated monitor fails, so always ensure the patient has an independent verified monitoring pathway during troubleshooting.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain required monitoring first, then isolate the module, sensor, cable, connection, and configuration before suspecting an internal interface failure. Escalate any unresolved monitoring problem that affects safe intended use.

That is successful troubleshooting.
