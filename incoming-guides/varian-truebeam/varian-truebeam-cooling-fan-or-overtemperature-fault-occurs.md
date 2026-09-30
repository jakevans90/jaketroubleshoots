---
schemaVersion: 1
title: "Varian TrueBeam Radiation Therapy System - Cooling, Fan, or Overtemperature Fault Occurs"
issueTitle: "Cooling, Fan, or Overtemperature Fault Occurs"
description: "The TrueBeam reports a cooling, fan, temperature, or thermal condition that interrupts operation or prevents system readiness."
assetType: "Radiation Therapy System"
manufacturer: "Varian"
model: "TrueBeam"
slug: "varian-truebeam-cooling-fan-or-overtemperature-fault-occurs"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that the TrueBeam displayed a thermal warning and became unavailable during operation."
  cause: "Clinical Engineering found an external ventilation opening obstructed by materials placed against the equipment."
  resolution: "Clinical Engineering cleared the ventilation area, allowed the system to return to normal temperature, and verified stable operation without recurrence during functional testing."
helpfulDetails:
  - "Exact thermal or fan message"
  - "Time and activity when fault occurred"
  - "Room temperature or HVAC condition"
  - "Ventilation obstruction"
  - "Fan sound or visible operation"
  - "Heat, odor, or smoke observed"
  - "Recent room work or equipment relocation"
  - "Restart result"
  - "Recurrence during testing"
  - "Final system status"
---
## What This Guide Helps With

The TrueBeam reports a cooling, fan, temperature, or thermal condition that interrupts operation or prevents system readiness.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Operation
Do not continue treatment or imaging when the system reports an unresolved thermal condition or shows signs of overheating. Safely stop the clinical workflow and remove the patient as appropriate.

**Expected outcome:** No patient depends on equipment that may be overheating or inadequately cooled.

### 2. Confirm the Reported Thermal Condition
Record the exact message, affected subsystem if identified, when the condition appeared, and whether the system shut down or inhibited operation.

**Expected outcome:** The thermal problem is accurately documented without assuming an internal component failure.

### 3. Inspect for Heat, Odor, or Abnormal Noise
From the exterior, check for unusual heat, burning odor, smoke, grinding, rattling, or abnormal fan noise.

If smoke, burning odor, or obvious electrical overheating is present, disconnect from service according to facility safety procedures and do not restart.

**Expected outcome:** Potentially hazardous overheating is identified immediately.

### 4. Check External Airflow
Inspect accessible ventilation openings and surrounding clearance for blocked vents, dust accumulation, stored materials, drapes, or equipment restricting airflow.

Do not open protected covers or access internal cooling assemblies.

**Expected outcome:** External ventilation paths are unobstructed.

### 5. Verify Room Environmental Conditions
Check whether the treatment room or equipment area is unusually warm or whether HVAC service is impaired. Coordinate with Facilities if environmental cooling appears abnormal.

**Expected outcome:** The room environment is suitable for equipment operation or an HVAC issue is identified.

### 6. Check Accessible Fans and Supporting Cooling Equipment
Observe only externally accessible fan operation and indicators. Do not insert objects into vents or bypass fan monitoring.

**Expected outcome:** Accessible cooling indications appear normal or a nonfunctioning external cooling element is identified.

### 7. Allow Appropriate Cooldown
If the event followed extended operation and no hazardous condition is present, allow the system to remain out of use for an appropriate period according to approved procedures before attempting a normal restart.

**Expected outcome:** The thermal condition clears and the system restarts normally, or the fault returns and requires escalation.

### 8. Verify Stable Operation
After correction of an external airflow or environmental issue, verify that the system remains stable during an approved functional test and does not redevelop the thermal condition.

**Expected outcome:** Normal cooling is maintained and no thermal alarm recurs. Troubleshooting can stop if required verification is successful.

### 9. Remove From Service for Persistent Thermal Faults
If the condition returns, fans behave abnormally, or unusual heat, noise, or odor remains, stop troubleshooting.

**Expected outcome:** A potentially overheating radiation-therapy system is kept out of clinical service.

## If the Problem Persists

External airflow, room conditions, visible ventilation issues, and accessible cooling indicators have been ruled out. Remaining causes may involve internal fans, cooling systems, thermal sensors, power electronics, heat exchangers, control electronics, or another internal service-level condition.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or appropriate service evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Return to service requires resolution of the thermal condition and successful verification of stable operation under the required functional workload.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not repeatedly clear or restart through an unexplained overtemperature condition; recurring heat faults can indicate a condition that worsens under clinical load.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Thermal faults require conservative troubleshooting because overheating can affect both reliability and safety. Rule out blocked airflow and environmental problems first, but stop and escalate whenever abnormal heat, fan behavior, or repeated thermal faults remain.

That is successful troubleshooting.
