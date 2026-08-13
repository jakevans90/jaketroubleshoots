---
schemaVersion: 1
title: "GE Healthcare Carestation 750 Anesthesia Machine - High Airway Pressure or PEEP High Alarm"
issueTitle: "High Airway Pressure or PEEP High Alarm"
description: "High pressure or high PEEP alarms occur because of circuit obstruction, water, filters, valves, settings, patient factors, or breathing-system problems."
assetType: "Anesthesia Machine"
manufacturer: "GE Healthcare"
model: "Carestation 750"
slug: "ge-healthcare-carestation-750-high-airway-pressure-or-peep-high-alarm"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Anesthesia staff reported repeated high airway pressure alarms from the Carestation 750 during pre-use testing."
  cause: "Clinical Engineering found a kinked breathing hose creating an external obstruction."
  resolution: "The breathing circuit was replaced, airway pressure returned to normal during test-lung ventilation, alarms were verified, and checkout passed."
helpfulDetails:
  - "Exact alarm wording"
  - "Ventilation mode"
  - "Set PEEP"
  - "Observed airway pressure"
  - "Circuit condition"
  - "Filters and accessories installed"
  - "Presence of water or obstruction"
  - "Known-good circuit results"
  - "Expiratory pressure behavior"
  - "Test-lung results"
  - "Final checkout status"
  - "Final device disposition"
---

## What This Guide Helps With
High pressure or high PEEP alarms occur because of circuit obstruction, water, filters, valves, settings, patient factors, or breathing-system problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Address Ventilation Immediately
If a high airway pressure or PEEP high alarm occurs during patient care, clinical staff must assess the patient and airway first.

Do not troubleshoot the anesthesia machine while the patient depends on unreliable ventilation. Provide alternate ventilation if needed.

**Expected outcome:** Patient ventilation is stabilized before equipment troubleshooting begins.

### 2. Confirm the Alarm Under Controlled Conditions
After removing the machine from patient use, connect an appropriate test lung and attempt to reproduce the condition.

Record:

- Ventilation mode
- Pressure behavior
- Set PEEP
- Relevant pressure limits
- Whether the alarm is continuous or intermittent

**Expected outcome:** The equipment-related condition is either reproduced or separated from patient-specific factors.

### 3. Inspect the Patient Circuit for Obstruction
Check the entire external breathing circuit for:

- Kinks
- Pinched tubing
- Occluded connectors
- Blocked filters
- Water accumulation
- Incorrect hose routing
- Obstructed patient wye

**Expected outcome:** The circuit is open and unobstructed. If removing an obstruction restores normal pressure, troubleshooting can stop after verification.

### 4. Inspect Filters and Accessories
Remove or replace questionable filters, adapters, humidification components, sampling adapters, or other added accessories using compatible known-good components.

Do not omit clinically required accessories when returning the machine to service.

**Expected outcome:** No external accessory creates excessive resistance. If pressure normalizes after replacement, the external cause is confirmed.

### 5. Verify Ventilator Settings
Review the configured:

- Ventilation mode
- PEEP
- Pressure limits
- Tidal volume or pressure target
- Rate and timing parameters when relevant

Do not change clinically prescribed settings on an active patient as an equipment troubleshooting method.

**Expected outcome:** The test settings are appropriate and do not inherently explain the alarm. Incorrect test settings can be corrected and reassessed.

### 6. Check the Breathing-System Assembly
Verify externally removable breathing-system components are properly seated and assembled.

Inspect accessible expiratory-path components for obvious contamination, improper installation, or obstruction without deep disassembly.

**Expected outcome:** The breathing system is correctly assembled with no visible restriction.

### 7. Compare With a Known-Good Circuit and Test Lung
Replace the external breathing circuit and test lung with known-good compatible components.

**Expected outcome:** If the alarm disappears, the original circuit or accessory was responsible. If high pressure or PEEP persists, continue troubleshooting.

### 8. Observe Expiratory Pressure Return
During controlled ventilation, observe whether airway pressure returns appropriately during expiration.

Persistent elevated expiratory pressure with a known-good external setup may indicate a breathing-system, valve, sensor, or control problem requiring escalation.

**Expected outcome:** Pressure returns appropriately during expiration. If not, remove the machine from service.

### 9. Complete Final Functional Verification
After correcting an external cause, verify:

- Stable ventilation
- Appropriate airway-pressure behavior
- PEEP response
- Alarm operation
- Leak integrity
- Required checkout

**Expected outcome:** The original alarm does not recur under controlled testing and the machine passes checkout. Troubleshooting can stop.

### 10. Escalate Persistent High Pressure or High PEEP
If the alarm persists with known-good circuits, accessories, and appropriate settings, stop external troubleshooting.

**Expected outcome:** The Carestation 750 is removed from service for qualified service evaluation.

## If the Problem Persists
Common external causes have been ruled out. Remaining categories may include expiratory-path restriction, internal valve function, pressure measurement, ventilator control, breathing-system interfaces, or other service-level faults.

The Carestation 750 should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired or configured only by qualified personnel

After repair, airway pressure, PEEP, ventilation, alarms, and breathing-system performance must be verified before return to service.

Knowing when persistent elevated pressure requires escalation protects the patient and the equipment.

## Clinical Use Tip
During an actual high-pressure alarm, patient, airway, and circuit causes must be evaluated clinically before the machine itself is assumed to be defective.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
High airway pressure should be approached from the patient and external circuit inward. Confirm obstruction, accessories, settings, and breathing-system assembly before considering an internal fault, then verify stable ventilation and alarm behavior before return to service.

That is successful troubleshooting.
