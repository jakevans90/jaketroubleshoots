---
schemaVersion: 1
title: "Medtronic Capnostream 35 Capnography Monitor - No CO2 Waveform Despite Connected FilterLine"
issueTitle: "No CO2 Waveform Despite Connected FilterLine"
description: "Troubleshoots a missing CO2 waveform caused by patient connection, FilterLine placement, blockage, loose connections, settings, or sampling-path problems."
assetType: "Capnography Monitor"
manufacturer: "Medtronic"
model: "Capnostream 35"
slug: "medtronic-capnostream-35-no-co2-waveform-despite-connected-filterline"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Capnostream 35 displayed no CO2 waveform despite the FilterLine appearing connected."
  cause: "Clinical Engineering found that the FilterLine was kinked beneath the equipment mounting bracket and was not allowing adequate sample flow."
  resolution: "The obstructed FilterLine was replaced and correctly routed, and stable waveform, EtCO2 response, and alarm operation were verified."
helpfulDetails:
  - "Exact display message"
  - "Whether EtCO2 numeric data was also absent"
  - "FilterLine type and condition"
  - "Patient-side connection method"
  - "Presence of kinks, moisture, or secretions"
  - "FilterLine connector condition"
  - "Known-good accessory results"
  - "CO2 display configuration"
  - "Sampling response during functional testing"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots a missing CO2 waveform caused by patient connection, FilterLine placement, blockage, loose connections, settings, or sampling-path problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Monitoring

Do not troubleshoot unreliable respiratory monitoring while a patient depends on it. Move the patient to another verified capnography monitor or provide an approved alternate method of respiratory monitoring before removing or manipulating the FilterLine.

Inspect the monitor and sampling accessories for contamination, liquid intrusion, physical damage, overheating, or unusual odor. Remove the device from service immediately if any unsafe condition is present.

**Expected outcome:** The patient remains continuously monitored, and the Capnostream 35 can be evaluated without interrupting required surveillance.

### 2. Confirm the Exact Reported Condition

Determine whether the display shows no waveform, no EtCO2 value, a flat waveform, intermittent sampling, or a message indicating that the FilterLine is disconnected or blocked.

Ask whether the problem occurs with one patient, one FilterLine type, one room, or every attempted setup.

**Expected outcome:** The failure is clearly defined and can be reproduced under controlled conditions.

### 3. Verify Basic Monitor Operation

Confirm that the monitor powers on normally, completes startup, displays other parameters, and responds to controls. Verify that the CO2 parameter is enabled and visible in the active screen layout.

Restart the monitor using the normal power control when clinically safe. Do not repeatedly power-cycle a device that freezes, overheats, or fails startup.

**Expected outcome:** The monitor starts normally and the CO2 channel is available for testing. If the waveform returns and remains stable, troubleshooting can stop after final verification.

### 4. Inspect the FilterLine and Patient Connection

Verify that the correct compatible FilterLine is being used and that all patient-side connections are secure. Inspect the cannula, airway adapter, tubing, and connector for kinks, compression, stretching, cracks, contamination, or incorrect positioning.

Confirm that oxygen tubing, bedding, equipment rails, or patient movement are not pinching the sampling line.

**Expected outcome:** The complete external sampling path is correctly positioned, open, dry, and securely connected. If the waveform appears and remains stable, troubleshooting can stop.

### 5. Reseat the FilterLine Connection

Disconnect the FilterLine from the monitor and inspect the connector and monitor receptacle externally for debris, moisture, bent surfaces, or visible damage. Do not insert tools or fluids into the port.

Reconnect the FilterLine firmly and verify that it seats fully without excessive force.

**Expected outcome:** The monitor recognizes the connected FilterLine and begins displaying a CO2 waveform. If recognition and waveform display remain reliable, troubleshooting can stop.

### 6. Substitute a New Known-Good FilterLine

Replace the existing FilterLine with a new, compatible, known-good accessory. Use a clean test source or approved functional test method rather than exhaled breath from staff.

If the replacement works, inspect the original accessory for blockage, moisture, contamination, or physical damage and discard it according to facility policy.

**Expected outcome:** A normal waveform appears with the known-good FilterLine. This confirms an accessory-related cause, and troubleshooting can stop after documenting the replacement.

### 7. Check for Sampling-Path Blockage or Moisture

Inspect the entire disposable sampling path for condensation, secretions, medication residue, or other material that could block gas flow. Do not flush, blow through, or attempt to clean a single-use FilterLine.

Replace contaminated or blocked accessories rather than trying to restore them.

**Expected outcome:** The sampling path is dry and unobstructed, and the waveform returns with a replacement accessory. If stable, troubleshooting can stop.

### 8. Verify Display and Parameter Configuration

Confirm that the CO2 waveform is assigned to the current display view and has not been hidden by a screen-layout change. Verify that the monitor is not in a mode or configuration that suppresses the waveform display.

Do not enter restricted service menus or change network-wide clinical defaults without authorization.

**Expected outcome:** The active configuration displays the CO2 waveform and numeric value normally. If corrected, troubleshooting can stop after confirming settings remain appropriate.

### 9. Perform a Controlled Functional Test

Using an approved capnography analyzer, simulator, or manufacturer-supported test setup, verify that the monitor draws a sample and displays a recognizable waveform and corresponding numeric value.

Observe the system long enough to identify intermittent loss caused by connector movement or weak sampling.

**Expected outcome:** The monitor consistently displays the expected waveform during the controlled test. If it does, complete return-to-service testing and stop troubleshooting.

### 10. Remove From Service When the Waveform Remains Absent

If no waveform is produced with a known-good FilterLine and approved test source, remove the Capnostream 35 from service. Label it **Out of Service** and send it for bench evaluation.

Do not open the sampling system, replace internal pump components, or perform board-level troubleshooting unless authorized and supported by manufacturer documentation.

**Expected outcome:** An unreliable monitor is prevented from returning to clinical use and is escalated appropriately.

## If the Problem Persists

The common external causes have been ruled out. The remaining possibilities include an internal sampling-pump problem, blocked internal pneumatic pathway, damaged FilterLine receptacle, sensor failure, software malfunction, or configuration issue requiring service-level access.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Following repair, complete functional verification of FilterLine recognition, sample flow, waveform display, EtCO2 response, alarms, controls, battery operation, and electrical safety when applicable before returning the monitor to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Confirm the complete path from the patient airway to the displayed waveform before relying on the EtCO2 value for clinical decisions.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient first, verify the entire external sampling path, and use a known-good FilterLine before suspecting an internal failure. Escalate persistent sampling faults and document the confirmed complaint, cause, corrective action, and final verification clearly.

That is successful troubleshooting.
