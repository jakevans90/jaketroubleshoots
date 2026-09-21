---
schemaVersion: 1
title: "Stryker CrossFlow Fluid Management System - Battery Will Not Charge or Runtime Is Short"
issueTitle: "Battery Will Not Charge or Runtime Is Short"
description: "Troubleshoots reported battery, backup-power, charging, or short-runtime concerns when the CrossFlow configuration includes applicable battery-supported operation."
assetType: "Fluid Management System"
manufacturer: "Stryker"
model: "CrossFlow"
slug: "stryker-crossflow-battery-will-not-charge-or-runtime-is-short"
dateAdded: "2026-09-21"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported the CrossFlow displayed an abnormal power condition and did not appear to charge while connected in the procedure room."
  cause: "Clinical Engineering found the AC power cord was loose at the rear console inlet, causing intermittent loss of AC input."
  resolution: "The cord connection was corrected, stable AC operation and normal power indications were verified, and the system passed functional testing."
helpfulDetails:
  - "Whether battery-supported operation applies to the configuration"
  - "Reported charging or runtime symptom"
  - "AC versus backup-power behavior"
  - "Power and charging indicators"
  - "Outlet test result"
  - "Power cord condition"
  - "Intermittent behavior during movement"
  - "Charging observation"
  - "Applicable runtime test result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots reported battery, backup-power, charging, or short-runtime concerns when the CrossFlow configuration includes applicable battery-supported operation.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Before Evaluating Backup Power

Do not test questionable battery or backup-power operation while the CrossFlow is supporting a procedure. Move clinical use to a verified system or maintain the console on its approved reliable power source.

**Expected outcome:** Patient care does not depend on an uncertain power source. If reliable power cannot be maintained, remove the system from service.

### 2. Confirm the CrossFlow Configuration and Reported Condition

Verify whether the specific system configuration actually includes battery-supported operation applicable to the complaint. Do not assume a battery feature is present based solely on the reported problem description.

Determine whether staff observed:

- Failure to charge
- A battery or power indication that did not change
- Unexpected shutdown after AC was removed
- Shorter-than-expected backup operation
- A power-related alarm or message

**Expected outcome:** The reported condition is confirmed as applicable to the installed configuration. If no battery-supported feature is present, redirect troubleshooting toward the actual external power source or associated equipment.

### 3. Verify Reliable AC Input

Inspect the power cord and power inlet, and verify the wall outlet or approved source. A charging complaint may simply be caused by absent or intermittent AC input.

**Expected outcome:** Reliable AC power is reaching the console. If charging indications return after restoring AC power, continue observation until normal operation is verified.

### 4. Inspect External Power Connections

Check the power cord, plug, strain relief, and console inlet for looseness, damage, contamination, or evidence of heating. Substitute an appropriate known-good cord if the cord is suspect.

**Expected outcome:** External power connections are intact and stable. If correcting the connection restores normal charging behavior, the external cause has been identified.

### 5. Observe Available Power and Charging Indicators

With the console on an approved AC source, observe available power, charging, or battery status indications. Record any message rather than relying on staff recollection.

Do not use hidden service menus to force charging or modify battery-management parameters.

**Expected outcome:** The console recognizes the appropriate power state and indicates normal charging or power operation. An abnormal indication that persists with verified AC input requires further evaluation.

### 6. Allow Appropriate Charging Opportunity

If the battery-supported configuration has been deeply discharged or stored without power, allow it to charge in accordance with applicable manufacturer instructions before evaluating runtime.

Do not invent or assume a charging duration.

**Expected outcome:** Battery status improves as expected under manufacturer-defined charging conditions. If it does not, continue troubleshooting.

### 7. Check for Intermittent Power Loss

Gently inspect accessible external connections without stressing them. Determine whether movement of the cord, cart, or console causes power indications to change.

Do not continue using a connection that is loose, arcing, overheated, or visibly damaged.

**Expected outcome:** AC input remains stable during normal handling. Any intermittent external connection is corrected before further evaluation.

### 8. Perform a Controlled Runtime Check if Applicable

Only if manufacturer documentation supports battery operation, perform an appropriate controlled runtime evaluation away from patient use and using approved procedures.

Do not infer battery health from an arbitrary runtime requirement.

**Expected outcome:** Backup operation meets the applicable manufacturer-defined criteria. If it does, the reported problem is resolved.

### 9. Verify Normal Operation After Correction

Restore the normal configuration and verify startup, display, controls, alarms, and power-source transitions applicable to the system.

**Expected outcome:** The CrossFlow operates reliably under its intended power configuration without unexpected shutdown. Troubleshooting can stop when verification passes.

### 10. Escalate Persistent Charging or Runtime Problems

If AC power, external connections, configuration, and applicable charging conditions are correct but charging or runtime remains abnormal, stop external troubleshooting.

**Expected outcome:** The system is removed from service when reliable power availability cannot be assured and is sent for qualified evaluation.

## If the Problem Persists

External AC supply, cords, connections, and applicable charging conditions have been ruled out. Remaining possibilities may include the battery assembly if equipped, charging circuitry, internal power management, protected configuration, or another service-level fault.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Stryker documentation and approved test equipment
- Repaired or configured only by qualified personnel

Any battery-supported function must meet applicable manufacturer requirements before return to clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not depend on backup runtime that has not been verified; maintain an approved alternate power or fluid-management plan during procedures.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Battery complaints should first be separated from AC-input and configuration problems. Verify external power before assuming an internal battery or charging failure, and document the verified cause and final safety status clearly.

That is successful troubleshooting.
