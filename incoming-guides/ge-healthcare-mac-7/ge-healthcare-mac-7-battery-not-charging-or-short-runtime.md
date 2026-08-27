---
schemaVersion: 1
title: "GE Healthcare MAC 7 Electrocardiograph (EKG) Machine - Battery Not Charging or Short Runtime"
issueTitle: "Battery Not Charging or Short Runtime"
description: "Troubleshooting charging failure or reduced battery runtime caused by AC power, connection, charging conditions, battery seating, battery condition, or excessive load."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "GE Healthcare"
model: "MAC 7"
slug: "ge-healthcare-mac-7-battery-not-charging-or-short-runtime"
dateAdded: "2026-08-27"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the MAC 7 battery discharged quickly and would not maintain sufficient runtime away from AC power."
  cause: "Clinical Engineering found the installed battery had poor runtime while a known-good compatible battery charged and operated normally."
  resolution: "Replaced the failed battery and verified normal charging, battery recognition, and stable operation on AC and battery power."
helpfulDetails:
  - "AC or battery operation when failure occurred."
  - "Outlet tested."
  - "Power cord condition."
  - "Charging indication."
  - "Battery physical condition."
  - "Battery recognition status."
  - "Known-good battery test."
  - "Runtime evaluation result."
  - "Shutdown behavior."
  - "Final device status."
---

## What This Guide Helps With

Troubleshooting charging failure or reduced battery runtime caused by AC power, connection, charging conditions, battery seating, battery condition, or excessive load.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Determine Whether Battery Operation Is Required

If the MAC 7 cannot reliably remain powered for the required clinical workflow, provide another verified ECG machine or operate from an approved AC source when clinically appropriate.

Do not use a unit for transport or mobile testing when its battery reliability is uncertain.

**Expected outcome:** Patient testing continues without dependence on an unreliable battery.

### 2. Verify AC Power

Confirm the power cord is fully connected to both the MAC 7 and the AC receptacle. Inspect the cord and plug for damage.

Test the receptacle with an appropriate outlet tester or move the unit to a verified functional outlet if permitted.

**Expected outcome:** Reliable AC power is present and the unit indicates that external power is available. If charging resumes normally, continue to battery verification.

### 3. Inspect the Power Cord and External Connection

Look for cuts, crushed insulation, loose plug blades, damaged connectors, bent contacts, or evidence of overheating.

Use a known-good approved power cord if substitution is appropriate.

**Expected outcome:** The AC connection remains stable when the cord is normally positioned. A defective power cord is replaced and removed from service.

### 4. Confirm Charging Indication

With the system connected to verified AC power, observe the normal accessible battery or charging status indications.

Allow sufficient time to determine whether the displayed charge state is increasing rather than relying on a brief connection.

**Expected outcome:** The battery status indicates normal charging progress. If charging proceeds normally and runtime later verifies acceptable, troubleshooting can stop.

### 5. Inspect and Reseat the Battery When Externally Accessible

If the battery is intended to be user- or service-accessible without disassembly, power down appropriately and inspect it for swelling, leakage, deformation, contamination, or damaged contacts.

Do not use a physically damaged battery. Reseat an undamaged battery according to approved handling practices.

**Expected outcome:** The battery is properly installed and recognized. A damaged battery is removed from use and handled according to facility policy.

### 6. Compare With a Known-Good Battery

If an approved compatible known-good battery is available, substitute it and evaluate charging behavior.

Do not open or attempt cell-level battery repair.

**Expected outcome:** Normal charging and runtime with the known-good battery identify the original battery as the likely cause. Replace the failed battery according to approved procedures.

### 7. Evaluate Runtime Under Controlled Conditions

After achieving an appropriate charge, operate the MAC 7 under normal bench conditions and observe whether the battery depletes abnormally quickly.

Use manufacturer-approved evaluation criteria where a formal runtime requirement is needed; do not invent an acceptance threshold.

**Expected outcome:** Battery operation remains stable for the required manufacturer or facility acceptance criteria. If it does, proceed to final verification.

### 8. Check for Unexpected Power Load or Repeated Cycling

Confirm the complaint was not caused by repeated printing, prolonged battery-only storage, failure to leave the device connected to AC when appropriate, or another workflow condition affecting available runtime.

Do not dismiss a repeatable short-runtime problem as user behavior.

**Expected outcome:** The observed battery behavior is consistent with normal operation, or a correctable usage/storage condition is identified.

### 9. Perform Final Functional Verification

Verify normal AC operation, charging indication, battery recognition, transition to battery operation, and continued basic device function.

**Expected outcome:** The unit remains powered reliably and charging behavior is normal. Return to service only after required testing is satisfactory.

### 10. Escalate Persistent Charging Failure

If the device will not charge a known-good battery from verified AC power, or unexpectedly shuts down despite normal external conditions, stop external troubleshooting.

**Expected outcome:** The MAC 7 is removed from service for evaluation of the charging or power-management system.

## If the Problem Persists

Common external power, power-cord, outlet, seating, and battery causes have been ruled out. Remaining possibilities include charging circuitry, power-management hardware, battery communication, internal connection, or other service-level faults.

The device should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Repaired only by qualified personnel.

Complete required power, charging, battery, and functional checks before returning the MAC 7 to service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A MAC 7 with questionable battery endurance should not be sent for mobile ECG work where loss of power could delay a required tracing.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Verify the AC source, power cord, charging status, battery installation, and battery condition before assuming an internal charging failure. Battery reliability directly affects continuity of ECG testing, so unresolved power problems require appropriate escalation.

That is successful troubleshooting.
