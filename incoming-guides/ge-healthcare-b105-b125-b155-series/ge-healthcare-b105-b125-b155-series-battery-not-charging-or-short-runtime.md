---
schemaVersion: 1
title: "GE Healthcare B105 / B125 / B155 Series Patient Monitor - Battery Not Charging or Short Runtime"
issueTitle: "Battery Not Charging or Short Runtime"
description: "Troubleshoots poor charging, rapid discharge, battery recognition problems, AC-source issues, battery seating, and externally verifiable battery faults."
assetType: "Patient Monitor"
manufacturer: "GE Healthcare"
model: "B105 / B125 / B155 Series"
slug: "ge-healthcare-b105-b125-b155-series-battery-not-charging-or-short-runtime"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the B155 monitor battery discharged rapidly and would not maintain the monitor during transport."
  cause: "Clinical Engineering found the installed battery had poor runtime while a compatible known-good battery operated normally."
  resolution: "Replaced the failed battery, verified charging and stable battery operation off AC, tested alarms and monitoring functions, and returned the monitor to service."
helpfulDetails:
  - "Battery status or warning displayed"
  - "AC-power indication"
  - "Outlet and power cord tested"
  - "Battery physical condition"
  - "Battery recognition"
  - "Known-good battery comparison"
  - "Whether the problem followed the battery"
  - "Behavior after AC removal"
  - "Charging behavior"
  - "Unexpected heat or swelling"
  - "Results before and after correction"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots poor charging, rapid discharge, battery recognition problems, AC-source issues, battery seating, and externally verifiable battery faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Monitoring
If battery performance could interrupt active patient monitoring, place the patient on another verified monitor or maintain reliable AC power while arranging replacement equipment.

Do not test questionable battery runtime while a patient depends on the monitor.

**Expected outcome:** Patient monitoring remains continuous and independent of the suspect battery.

### 2. Confirm the Exact Battery Complaint
Determine whether the issue is:
- Battery not charging
- Battery not recognized
- Battery percentage or status not increasing
- Short runtime
- Immediate shutdown after AC removal
- Intermittent battery connection
- Battery-related warning or status indication

Determine whether the problem follows a particular battery or remains with the monitor.

**Expected outcome:** The battery symptom and operating condition are clearly defined.

### 3. Inspect the Battery and Battery Area
Inspect accessible battery surfaces and the battery compartment for:
- Swelling
- Cracks
- Leakage
- Contamination
- Damaged contacts
- Evidence of overheating
- Poor seating

Do not continue using or charging a battery that is swollen, leaking, damaged, or excessively hot.

**Expected outcome:** The battery and accessible connection area are physically safe for further evaluation.

If unsafe battery damage is present, remove the battery from service according to facility battery-handling procedures and troubleshooting can stop.

### 4. Verify AC Power
Confirm the monitor is connected to a known-good AC source and that normal AC-power indication is present.

Inspect and reseat the external power cord. Use a compatible known-good cord when appropriate.

**Expected outcome:** The monitor has reliable AC power available for charging.

If charging begins normally after restoring AC power or correcting an external cord issue, verify continued charging and troubleshooting can stop.

### 5. Verify Battery Seating and Recognition
If accessible under approved Clinical Engineering procedures, power down as appropriate and reseat the battery.

Restart the monitor and observe whether the battery is recognized.

Do not repeatedly force a battery into a damaged compartment or connector.

**Expected outcome:** The monitor consistently recognizes the installed battery.

If reseating restores reliable battery recognition and charging, perform final verification.

### 6. Allow a Controlled Charging Evaluation
With the monitor off-patient, leave it connected to verified AC power and observe whether the displayed battery status indicates charging or improves over time.

Do not declare a battery faulty solely because the charge level does not change immediately after connection.

**Expected outcome:** Battery status behaves consistently with charging while reliable AC power is present.

If the monitor does not indicate or demonstrate charging despite verified AC power, continue troubleshooting.

### 7. Compare With a Known-Good Battery
When a compatible known-good battery is available and substitution is permitted, install it and compare:
- Recognition
- Charging behavior
- Ability to remain powered after AC removal
- Runtime behavior under controlled testing

Use only approved compatible batteries.

**Expected outcome:** The known-good battery charges and operates normally.

If the known-good battery works normally while the original does not, replace the failed battery through the approved process and proceed to final verification.

### 8. Compare the Suspect Battery in Another Compatible Unit When Appropriate
If facility practice permits and another compatible verified monitor is available, determine whether the suspect battery exhibits the same behavior in that unit.

This can help distinguish a battery problem from a monitor charging problem.

**Expected outcome:** The failure either follows the battery or remains associated with the original monitor.

If the failure follows the battery, remove that battery from service.

### 9. Verify Runtime After Correction
After charging an acceptable battery, perform an off-patient battery operation test appropriate to facility procedures.

Confirm:
- Stable battery recognition
- Normal transition from AC to battery
- No unexpected shutdown
- No abnormal heat
- No erratic battery-status behavior

Do not return the monitor to service based only on a charging icon if the original complaint was short runtime.

**Expected outcome:** The monitor remains stable on battery for the verification period required by facility procedures.

If battery performance is acceptable, continue to final verification.

### 10. Perform Final Functional Verification
Reconnect AC power and verify expected power-source transition, battery indication, display, controls, monitoring functions, and alarm operation.

Complete any required electrical safety or return-to-service tests.

**Expected outcome:** The monitor charges and operates normally from its intended power sources without interruption.

If all checks pass, document and return the monitor to service.

### 11. Escalate an Unresolved Charging Problem
If multiple acceptable batteries are not charging or the monitor has unstable battery recognition despite verified AC power and proper seating, stop external troubleshooting.

Do not proceed into unauthorized internal charging-circuit or board-level repair.

**Expected outcome:** The unresolved monitor is removed from service and routed for qualified evaluation.

## If the Problem Persists

External AC supply, cord condition, battery seating, and battery condition have been checked. Remaining causes may involve the charging subsystem, battery-interface circuitry, internal power management, configuration, or another service-level problem.

The monitor should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired or configured only by qualified personnel

After repair, verify charging, battery recognition, power-source transition, runtime behavior, alarms, and other required return-to-service functions.

Knowing when to stop battery troubleshooting before an unreliable monitor returns to clinical use is proper troubleshooting.

## Clinical Use Tip

A monitor with uncertain battery runtime should not be relied on for patient transport, even when it operates normally while connected to AC power.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**




## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain patient monitoring while evaluating battery concerns, verify AC power and battery seating before condemning components, use controlled known-good comparisons, and escalate charging problems that remain with the monitor. Document the confirmed cause rather than assuming normal battery aging.

That is successful troubleshooting.
