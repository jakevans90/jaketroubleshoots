---
schemaVersion: 1
title: "GE Healthcare Discovery MI PET / CT System - Cooling, Fan, or Overtemperature Fault Occurs"
issueTitle: "Cooling, Fan, or Overtemperature Fault Occurs"
description: "Troubleshoots cooling, airflow, fan, and temperature faults caused by blocked ventilation, room conditions, facility cooling, contamination, or service-level cooling problems."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "Discovery MI"
slug: "ge-healthcare-discovery-mi-cooling-fan-or-overtemperature-fault-occurs"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Imaging staff reported that the Discovery MI displayed an overtemperature warning and became unavailable for scanning."
  cause: "Clinical Engineering found equipment stored against an external ventilation opening and restricting airflow."
  resolution: "Clinical Engineering cleared the ventilation area, allowed the system to return to normal operating condition, verified that the warning did not recur during functional testing, and returned the scanner to service."
helpfulDetails:
  - "Exact temperature or cooling message"
  - "Room condition"
  - "HVAC status"
  - "Ventilation obstruction"
  - "Fan sound"
  - "Unusual heat or odor"
  - "Recent power or HVAC event"
  - "Whether the fault recurred"
  - "Functional test result"
  - "Final system status"
---
## What This Guide Helps With
Troubleshoots cooling, airflow, fan, and temperature faults caused by blocked ventilation, room conditions, facility cooling, contamination, or service-level cooling problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Respond to Overtemperature Safely

If the scanner reports an overtemperature condition, produces unusual heat, smells hot, or has abnormal fan noise, stop clinical operation and safely remove the patient when appropriate.

If smoke, burning odor, visible electrical damage, or excessive heat is present, isolate the equipment according to emergency procedures and do not continue troubleshooting under power.

**Expected outcome:** The patient is safe and no overheating equipment remains in clinical use.

### 2. Confirm the Exact Cooling Condition

Determine whether the complaint involves:

- Overtemperature message
- Fan fault
- Excessive fan noise
- Reduced airflow
- Unexpected shutdown associated with heat
- Room-temperature concern
- Intermittent temperature warning

Record when the fault appears and whether it clears after the system is idle.

**Expected outcome:** The cooling-related symptom is clearly identified.

### 3. Check Room Temperature and HVAC Operation

Assess the imaging room and nearby equipment area for obvious environmental problems.

Check for:

- Unusually warm room
- Failed HVAC
- Blocked room vents
- Recent HVAC maintenance
- Facility alarms
- Doors being held open to warmer spaces

Coordinate with Facilities when room cooling is abnormal.

**Expected outcome:** The room environment is appropriate or an external HVAC problem is identified.

If restoring room cooling resolves the scanner condition and required verification passes, troubleshooting can stop.

### 4. Inspect Accessible Scanner Ventilation

Inspect externally accessible air inlets, outlets, and surrounding clearance.

Look for:

- Obstructed ventilation openings
- Stored materials against equipment
- Dust accumulation
- Linens or covers restricting airflow
- Portable equipment blocking vents

Do not remove internal covers solely to inspect fans.

**Expected outcome:** External ventilation paths are unobstructed.

### 5. Listen for Abnormal Fan Operation

From outside the equipment, note whether cooling fans sound:

- Normal
- Abnormally loud
- Intermittent
- Grinding or rattling
- Completely absent where airflow is normally expected

Do not reach into vents or moving equipment.

**Expected outcome:** No obvious abnormal mechanical fan condition is present.

If grinding, binding, or other abnormal mechanical noise is identified, stop and escalate.

### 6. Check for Recent Environmental or Power Events

Determine whether the fault followed:

- Power interruption
- System restart
- HVAC outage
- Room construction
- Equipment relocation
- Cleaning activity
- Blocked airflow caused by temporary equipment

**Expected outcome:** Any external event contributing to the cooling problem is identified or ruled out.

### 7. Allow Approved Cool-Down if Appropriate

If the manufacturer-approved workflow permits and no hazardous condition exists, allow the system to remain idle or shut down normally while the environmental issue is corrected.

Do not repeatedly restart an overheating system.

**Expected outcome:** The system returns to a normal temperature state without recurring warning after the external cause is corrected.

### 8. Verify Normal Operation

After correcting an external cooling condition, confirm:

- No temperature warning remains
- Cooling noise is normal
- Airflow is unobstructed
- Startup completes
- Required acquisition subsystems reach ready state
- No unexpected shutdown occurs during approved functional testing

**Expected outcome:** The system remains thermally stable during verification.

If applicable return-to-service testing passes, troubleshooting can stop and the scanner may be returned to service.

## If the Problem Persists

If room conditions, ventilation, external obstruction, recent power or HVAC events, and approved cool-down procedures have been addressed but a cooling or overtemperature fault persists, the cause may involve an internal fan, cooling circuit, temperature sensor, power supply, heat exchanger, detector cooling requirement, or another service-level condition.

The system should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or formal system evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired only by qualified personnel

Do not bypass thermal protection or operate the scanner repeatedly to determine how long it runs before overheating.

After service, verify stable operating temperature and all affected scanner functions before return to clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

An overtemperature warning should never be treated as a nuisance alarm; unreliable thermal control can affect scanner availability and image acquisition reliability.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Cooling problems should begin with patient safety and the environment. Verify room HVAC, external airflow, ventilation clearance, and obvious fan behavior before assuming an internal cooling failure. Do not bypass thermal protections, and escalate recurring faults appropriately.

That is successful troubleshooting.
