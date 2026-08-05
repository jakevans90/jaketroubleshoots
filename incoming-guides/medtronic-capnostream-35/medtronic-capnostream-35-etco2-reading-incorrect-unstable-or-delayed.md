---
schemaVersion: 1
title: "Medtronic Capnostream 35 Capnography Monitor - EtCO2 Reading Incorrect, Unstable, or Delayed"
issueTitle: "EtCO2 Reading Incorrect, Unstable, or Delayed"
description: "Addresses inaccurate, fluctuating, or slow EtCO2 values caused by sampling accessories, leaks, moisture, positioning, patient factors, settings, or weak flow."
assetType: "Capnography Monitor"
manufacturer: "Medtronic"
model: "Capnostream 35"
slug: "medtronic-capnostream-35-etco2-reading-incorrect-unstable-or-delayed"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the Capnostream 35 EtCO2 reading fluctuated widely and responded slowly to changes in ventilation."
  cause: "Clinical Engineering found moisture accumulation and partial blockage in the disposable FilterLine."
  resolution: "The FilterLine was replaced, and stable waveform, prompt EtCO2 response, and alarm performance were verified with an approved test source."
helpfulDetails:
  - "Reported EtCO2 values"
  - "Whether the reading was high, low, unstable, or delayed"
  - "Waveform appearance"
  - "Patient interface and oxygen delivery method"
  - "FilterLine condition"
  - "Presence of moisture or secretions"
  - "Known-good FilterLine comparison"
  - "Relevant settings observed"
  - "Analyzer or simulator results"
  - "Final device status"
---

## What This Guide Helps With

Addresses inaccurate, fluctuating, or slow EtCO2 values caused by sampling accessories, leaks, moisture, positioning, patient factors, settings, or weak flow.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Compare With Clinical Condition

Do not rely on a questionable EtCO2 value while a patient depends on accurate respiratory monitoring. Transfer monitoring to another verified device or use an approved alternate method.

Ask clinical staff whether the displayed value conflicts with the patient’s respiratory status, waveform, ventilator information, or another verified monitor.

**Expected outcome:** Patient monitoring remains reliable while the suspect monitor is evaluated.

### 2. Confirm the Exact Behavior

Determine whether the value is consistently high or low, changes abruptly, responds slowly to breathing changes, drops out intermittently, or disagrees only during movement or oxygen delivery.

Review the waveform for clipping, a sloped baseline, reduced amplitude, irregular sampling, or periods of flat display.

**Expected outcome:** The instability pattern is defined and correlated with waveform behavior.

### 3. Inspect Patient-Side Placement

Verify proper placement of the nasal or oral-nasal cannula, airway adapter, and associated tubing. Confirm that the sampling point is exposed to exhaled gas and has not shifted away from the airway.

Check whether high-flow oxygen, masks, loose airway connections, mouth breathing, or patient movement could dilute or interrupt the sampled gas.

**Expected outcome:** The sampling accessory is correctly positioned and consistently captures exhaled gas. If the value stabilizes, troubleshooting can stop.

### 4. Inspect for Kinks, Leaks, and Loose Connections

Trace the FilterLine from the patient to the monitor. Inspect for crushed tubing, partial disconnection, cracked fittings, loose airway adapters, damaged cannulas, or connections that move during patient repositioning.

Secure the tubing without creating tension or pressure points.

**Expected outcome:** The sampling path is airtight, unobstructed, and stable. If readings become accurate and responsive, troubleshooting can stop.

### 5. Check for Moisture and Contamination

Inspect the sampling line and airway adapter for condensation, secretions, nebulized medication residue, or other contamination. Replace the disposable sampling accessory when contamination is present.

Do not flush, dry with compressed air, or reuse a single-use sampling line.

**Expected outcome:** A clean, dry sampling path produces a stable waveform and timely EtCO2 response. If so, troubleshooting can stop.

### 6. Substitute a Known-Good FilterLine

Install a new, compatible, known-good FilterLine and repeat the observation. Compare the new accessory’s response with the original under the same controlled test condition.

**Expected outcome:** The value stabilizes with the replacement accessory, confirming the original FilterLine was restricted, leaking, or contaminated. Troubleshooting can stop after documentation.

### 7. Verify Monitor Settings and Display Scale

Confirm that the correct patient category, CO2 parameter configuration, waveform scale, averaging behavior, and alarm limits are selected according to facility policy and the intended clinical application.

Do not alter protected defaults or service-level calibration settings without authorization.

**Expected outcome:** Appropriate settings are active and the displayed value and waveform respond normally. If corrected, troubleshooting can stop.

### 8. Consider Environmental and Patient-Related Influences

Evaluate whether rapid breathing, shallow ventilation, noninvasive ventilation leaks, supplemental oxygen flow, airway suctioning, nebulizer treatments, or excessive movement are affecting the sample.

Compare performance during a stable period or with an approved test source.

**Expected outcome:** Clinically induced variability is distinguished from a monitor or accessory fault.

### 9. Compare Against an Approved Capnography Test Source

Use an approved analyzer or simulator to provide a controlled CO2 signal. Verify waveform shape, numeric stability, response time, and recovery after signal changes.

Do not make calibration adjustments unless specifically authorized by manufacturer service documentation.

**Expected outcome:** The monitor produces stable and appropriate readings from a controlled source. If it passes, document the clinical or accessory-related cause and stop troubleshooting.

### 10. Escalate Persistent Inaccuracy

If readings remain incorrect, unstable, or delayed with a known-good FilterLine and approved test source, remove the device from service and label it **Out of Service**.

Send it for bench evaluation of the sampling system, CO2 measurement channel, configuration, and software.

**Expected outcome:** A monitor with unreliable respiratory measurements is withheld from clinical use.

## If the Problem Persists

External sampling, positioning, accessory, setting, and environmental causes have been ruled out. Remaining categories include weak internal sample flow, pneumatic leakage, sensor degradation, signal-processing problems, damaged connectors, or service-level configuration errors.

The device should be removed from service, labeled Out of Service, and evaluated using approved test equipment and applicable manufacturer documentation. Internal repair or calibration should be performed only by qualified personnel.

After repair, verify waveform quality, numeric accuracy using approved equipment, response to changing values, alarm operation, data storage, controls, and overall functional safety before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Always interpret the EtCO2 number together with waveform quality and the patient’s clinical condition.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Begin with the patient connection, waveform, and sampling accessories before assuming measurement failure. Compare the monitor against a controlled source, escalate unresolved inaccuracy, and clearly document what was reported, found, corrected, and verified.

That is successful troubleshooting.
