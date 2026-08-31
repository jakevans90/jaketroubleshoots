---
schemaVersion: 1
title: "Stryker Neptune Surgical Fluid Management System - Smoke Evacuation Has Low Flow or Will Not Start"
issueTitle: "Smoke Evacuation Has Low Flow or Will Not Start"
description: "Use when smoke evacuation is unavailable, weak, intermittent, or unable to provide expected capture despite the system otherwise appearing operational."
assetType: "Surgical Fluid Management System"
manufacturer: "Stryker"
model: "Neptune"
slug: "stryker-neptune-smoke-evacuation-has-low-flow-or-will-not-start"
dateAdded: "2026-08-31"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that Neptune smoke evacuation started but produced very low airflow."
  cause: "Clinical Engineering found the external smoke tubing sharply kinked near the equipment connection."
  resolution: "Repositioned the tubing to remove the restriction, verified stable smoke-evacuation flow and controls, and returned the unit to service."
helpfulDetails:
  - "Whether evacuation would not start or had low flow"
  - "Displayed messages or indicators"
  - "Smoke tubing condition"
  - "Capture accessory tested"
  - "Filter installation and status"
  - "Known-good tubing or accessory substitutions"
  - "Unusual blower noise"
  - "Other active Neptune conditions"
  - "Results before and after correction"
  - "Final device status"
---
## What This Guide Helps With

Use when smoke evacuation is unavailable, weak, intermittent, or unable to provide expected capture despite the system otherwise appearing operational.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Smoke-Control Measures

If smoke evacuation is required during an active procedure and the Neptune cannot provide reliable evacuation, use another verified smoke-evacuation method before troubleshooting.

Do not troubleshoot unreliable evacuation equipment while clinical staff depend on it.

**Expected outcome:** Surgical smoke continues to be managed safely through an alternate method while the Neptune is evaluated.

### 2. Confirm the Reported Condition

Determine whether smoke evacuation will not start at all, starts but has weak flow, stops intermittently, or works only in certain configurations.

Record any displayed message, indicator, unusual noise, or recent accessory change.

**Expected outcome:** The failure pattern is clearly defined. If an incorrect control selection is identified and normal smoke evacuation returns, troubleshooting can stop after verification.

### 3. Verify the Smoke-Evacuation Function Is Enabled

Check accessible operating controls and confirm the smoke-evacuation function is selected and commanded to operate as intended.

Do not enter unauthorized service menus or alter protected configuration.

**Expected outcome:** The smoke-evacuation function is enabled and responds to its normal control. If normal flow is restored, verify operation and stop.

### 4. Inspect External Tubing and Connections

Inspect smoke tubing from the Neptune to the clinical accessory for:

- Loose connections
- Kinks
- Crushing
- Occlusion
- Excessive bends
- Damaged tubing
- Incorrect connection point

Reconnect or replace damaged external tubing as appropriate.

**Expected outcome:** The smoke path is open, correctly connected, and unrestricted. If adequate flow returns, proceed to final functional verification.

### 5. Inspect the Smoke Capture Accessory

Check the externally connected smoke pencil, tubing adapter, wand, or other approved capture accessory for obstruction, contamination, or damage.

Replace a suspect disposable accessory rather than attempting invasive cleaning of a disposable smoke path.

**Expected outcome:** A clean, unobstructed compatible capture accessory is connected. Normal evacuation should be present if the accessory caused the restriction.

### 6. Verify Filter Installation and Status

Inspect the accessible smoke-evacuation filter installation. Confirm the filter is present, correctly seated, compatible with the Neptune, and not presenting an active filter-related condition.

Do not bypass filter-recognition or filtration features.

**Expected outcome:** The required filter is properly installed and accepted by the system. If smoke flow returns after correcting filter installation, troubleshooting can stop after verification.

### 7. Substitute Known-Good External Components

When available, test with known-good compatible smoke tubing and capture accessories.

Change one component at a time to isolate the cause.

**Expected outcome:** Smoke evacuation operates normally with known-good external components. The failed accessory can then be removed from use.

### 8. Check for Waste-System Conditions Affecting Operation

Observe whether the Neptune has another active condition involving waste capacity, disposable recognition, filter installation, or system readiness that prevents normal smoke evacuation.

Correct only externally accessible conditions within Clinical Engineering scope.

**Expected outcome:** The system indicates normal readiness without an external condition inhibiting smoke evacuation.

### 9. Perform Final Functional Verification

Operate the smoke-evacuation function using an appropriate nonclinical test setup. Confirm activation, stable airflow, normal controls, and absence of abnormal noise or odor.

**Expected outcome:** Smoke evacuation starts reliably and maintains adequate flow through the external test setup. Troubleshooting can stop when operation is stable.

### 10. Escalate Low or Absent Flow That Remains

If known-good tubing, accessories, filter installation, controls, and external conditions have been verified but smoke evacuation remains weak or unavailable, stop troubleshooting.

**Expected outcome:** The Neptune is removed from service for qualified evaluation of the internal smoke-evacuation system.

## If the Problem Persists

Common external causes such as blocked tubing, damaged accessories, poor connections, incorrect control selection, and filter installation problems have been ruled out.

The remaining problem may involve the internal evacuation blower, airflow sensing, internal filtration path, control system, power delivery, or another service-level condition.

The device should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate Stryker documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Complete applicable functional and safety testing before return to service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Provide another verified smoke-evacuation method before removing an unreliable Neptune from an active surgical procedure.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter; optional explanatory prose may follow. -->



## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain safe surgical smoke control while evaluating the Neptune, and rule out tubing, accessories, filters, controls, and other external restrictions before suspecting an internal evacuation problem. Escalate unreliable operation and document the final functional result.

That is successful troubleshooting.
