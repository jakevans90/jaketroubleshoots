---
schemaVersion: 1
title: "Newport e360 Ventilator - Air/Oxygen Blender Will Not Reach the Set FiO2"
issueTitle: "Air/Oxygen Blender Will Not Reach the Set FiO2"
description: "Addresses incorrect delivered oxygen concentration caused by gas supplies, hoses, source connections, circuit conditions, settings, or oxygen-measurement problems."
assetType: "Ventilator"
manufacturer: "Newport"
model: "e360"
slug: "newport-e360-air-oxygen-blender-will-not-reach-the-set-fio2"
dateAdded: "2026-11-06"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the Newport e360 would not achieve the selected oxygen concentration."
  cause: "Clinical Engineering found the oxygen hose was connected to an external source that was not providing a usable oxygen supply."
  resolution: "The ventilator was connected to a verified oxygen source, delivered FiO2 was confirmed with an oxygen analyzer, and ventilation and alarms passed functional testing."
helpfulDetails:
  - "Set FiO2"
  - "Displayed FiO2"
  - "Independently measured FiO2"
  - "Air and oxygen source tested"
  - "Gas-hose condition"
  - "Circuit condition"
  - "Oxygen-sensor calibration result"
  - "Gas-supply alarm behavior"
  - "Results before and after correction"
  - "Final device status"
---

## What This Guide Helps With

Addresses incorrect delivered oxygen concentration caused by gas supplies, hoses, source connections, circuit conditions, settings, or oxygen-measurement problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Verify Oxygenation Support
Do not continue using a ventilator that cannot reliably deliver the prescribed oxygen concentration. Transfer the patient to another verified ventilator or appropriate backup ventilation system.

Confirm the set FiO2, displayed FiO2, and independently measured oxygen concentration when approved test equipment is available.

**Expected outcome:** The patient is safely supported and the actual oxygen-delivery discrepancy is confirmed.

### 2. Verify the Set FiO2
Confirm that the oxygen concentration setting is appropriate and that no recent setting or mode change explains the reported condition.

Avoid changing clinical settings merely to make a fault disappear.

**Expected outcome:** The intended FiO2 setting is verified. If the issue resulted from an incorrect setting and proper operation is restored after correction, troubleshooting can stop after verification.

### 3. Inspect Air and Oxygen Supply Connections
Check both gas hoses from the ventilator to their sources. Confirm secure connections, correct gas source identification, absence of damaged fittings, and no obvious kinking or restriction.

**Expected outcome:** Both required gas supplies are correctly connected and physically intact. Correcting a disconnected or restricted supply that restores normal FiO2 resolves the issue.

### 4. Verify External Gas Sources
Confirm that the air and oxygen sources are available and functioning normally. When appropriate, compare operation on another verified source or approved gas outlet.

Do not assume an internal blender problem until external supplies have been ruled out.

**Expected outcome:** Stable external air and oxygen supplies are available. If moving to a verified supply restores normal FiO2 control, investigate the original infrastructure source rather than the ventilator.

### 5. Inspect the Patient Circuit
Inspect the breathing circuit for major leaks, incorrectly connected components, or unusual restrictions that could affect delivered gas measurements or ventilation.

**Expected outcome:** The circuit is properly assembled and intact. Any external circuit problem is corrected before further testing.

### 6. Compare Set and Measured Oxygen Concentration
Using approved oxygen-analysis equipment, compare delivered oxygen concentration with the ventilator setting under controlled bench conditions.

Allow the system to stabilize according to approved procedures before interpreting results.

**Expected outcome:** Delivered oxygen concentration corresponds appropriately with the selected setting. If verified output is correct, investigate the reported clinical circumstances or displayed measurement rather than assuming blender failure.

### 7. Test Across More Than One FiO2 Setting
With the ventilator off-patient and connected to appropriate test equipment, verify that oxygen concentration responds when the set value is changed through representative test points allowed by your procedure.

**Expected outcome:** Measured oxygen concentration changes predictably with commanded FiO2. If control is stable and accurate, the issue is resolved.

### 8. Check for Oxygen-Sensor Contribution
If independently measured oxygen concentration is correct but the ventilator display remains inaccurate, evaluate the oxygen-sensor calibration and condition using approved procedures.

**Expected outcome:** Independent measurement and ventilator indication agree after approved sensor verification or calibration. If not, continue escalation.

### 9. Perform Final Functional Verification
Verify ventilation, delivered oxygen concentration, applicable gas-supply alarms, and oxygen-monitoring response before return to service.

**Expected outcome:** FiO2 control is stable, independent measurement agrees with expected delivery, and alarms function normally.

### 10. Escalate if FiO2 Cannot Be Controlled
If stable known-good gas supplies and correct external setup do not restore oxygen control, remove the ventilator from service.

**Expected outcome:** An unresolved oxygen-delivery problem is escalated rather than accepted for clinical use.

## If the Problem Persists

External gas supplies, hoses, settings, circuit configuration, and oxygen measurement have been evaluated. Remaining causes may include internal gas-mixing control, pneumatic regulation, sensing, calibration, or other service-level faults.

Remove the device from service, label it **Out of Service**, and send it for bench evaluation. Use manufacturer documentation and approved gas-analysis equipment. Internal pneumatic repair and service-level adjustment should be performed only by qualified personnel.

Return the ventilator to service only after oxygen-delivery accuracy, ventilation, gas-supply alarms, and related functional checks pass.

## Clinical Use Tip

When FiO2 is questionable, independently verify delivered oxygen and move the patient to another verified ventilator before investigating the e360.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Verify gas sources, hoses, settings, circuit conditions, and independent oxygen measurement before assuming an internal blender failure. Protect the patient, confirm results objectively, escalate unresolved faults, and document the complete test path.

That is successful troubleshooting.
