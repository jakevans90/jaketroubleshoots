---
schemaVersion: 1
title: "Stryker Neptune Surgical Fluid Management System - Docking, Waste Transfer, or Drain Cycle Will Not Start"
issueTitle: "Docking, Waste Transfer, or Drain Cycle Will Not Start"
description: "Use when the Neptune will not initiate docking-related waste transfer or drainage despite the rover being positioned for the expected process."
assetType: "Surgical Fluid Management System"
manufacturer: "Stryker"
model: "Neptune"
slug: "stryker-neptune-docking-waste-transfer-or-drain-cycle-will-not-start"
dateAdded: "2026-08-31"
taxonomyMode: "reuse"
ccr:
  complaint: "EVS staff reported that the Neptune would dock but the waste-transfer cycle would not become available."
  cause: "Clinical Engineering found debris at the external docking interface preventing complete rover engagement."
  resolution: "Removed the obstruction using appropriate precautions, re-docked the rover, verified a complete normal transfer cycle without leakage, and returned the equipment to service."
helpfulDetails:
  - "Exact docking or transfer message"
  - "Whether docking was recognized"
  - "Rover position at the station"
  - "External interface condition"
  - "Dock utility indicators"
  - "Whether another rover or dock was tested"
  - "Presence of leakage or unusual noise"
  - "Whether the cycle started or partially completed"
  - "Results after re-docking"
  - "Final rover and dock status"
---
## What This Guide Helps With

Use when the Neptune will not initiate docking-related waste transfer or drainage despite the rover being positioned for the expected process.

## Step-by-Step Troubleshooting

### 1. Protect Personnel From Waste Exposure

Treat the waste system and docking connection as contaminated. Use required PPE and infection-control precautions.

Do not manually open, bypass, disconnect, or manipulate a pressurized or actively transferring waste path.

**Expected outcome:** Personnel are protected and the rover is stable before troubleshooting begins.

### 2. Confirm the Exact Failure

Determine whether the rover fails to recognize docking, recognizes docking but will not begin transfer, starts and immediately stops, or cannot begin the drain cycle.

Record any displayed message, indicator, or unusual sound.

**Expected outcome:** The specific point in the docking or waste-transfer process is identified.

### 3. Verify Rover Positioning at the Dock

Confirm the Neptune is correctly aligned and fully positioned at the intended docking station.

Look for obstructions, floor debris, misalignment, or anything preventing complete mechanical engagement.

**Expected outcome:** The rover is correctly positioned and physically able to engage the dock. If proper alignment restores the cycle, verify completion and stop.

### 4. Inspect the Dock and Rover Interfaces

Inspect accessible docking surfaces and connections for:

- Visible debris
- Fluid contamination
- Physical damage
- Foreign material
- Bent or obstructed external features
- Incomplete engagement

Do not probe internal valves or defeat interlocks.

**Expected outcome:** The docking interfaces are clean, intact, and able to mate normally.

### 5. Verify Required External Utilities

Confirm that the docking station has the external services needed for normal operation and that no obvious facility condition is preventing use.

Check accessible power or utility indicators when provided.

Do not alter facility plumbing or electrical infrastructure outside Clinical Engineering scope.

**Expected outcome:** Required docking-station utilities appear available. If a facility-side problem is identified, refer it to the appropriate department.

### 6. Check Rover Status and Readiness

Verify the Neptune is powered, responsive, and not displaying another condition that inhibits waste transfer, such as an unresolved disposable, waste-path, or system-readiness issue.

Use normal accessible controls only.

**Expected outcome:** The rover indicates normal readiness for the docking process.

### 7. Re-Dock the Rover

Move the Neptune away from the station, inspect the path, and dock it again using normal operating positioning.

Observe whether the dock is recognized and whether the transfer process becomes available.

**Expected outcome:** The system recognizes proper docking and permits the expected cycle. If the cycle starts and completes normally, troubleshooting can stop after verification.

### 8. Compare With Another Compatible Dock When Available

If the facility has another approved compatible docking station, test the rover there when practical.

Alternatively, if another known-good rover uses the suspect docking station normally, that comparison can help isolate the issue.

**Expected outcome:** A comparison distinguishes a rover-specific condition from a docking-station or infrastructure issue.

### 9. Observe the Cycle Without Opening the Waste Path

Start the appropriate normal transfer or drain process and observe external indicators, sounds, and system status.

Stop if leakage, abnormal noise, odor, or unsafe operation occurs.

**Expected outcome:** The docking or drain cycle starts and completes without leakage or interruption. Troubleshooting can stop when the full process is successful.

### 10. Escalate an Unresolved Docking or Transfer Failure

If correct positioning, interfaces, readiness, and available facility utilities have been verified but the cycle still cannot begin or complete, stop troubleshooting.

**Expected outcome:** The affected rover or docking station is removed from use and referred for qualified service evaluation.

## If the Problem Persists

Common external causes such as poor alignment, dirty docking surfaces, incomplete engagement, rover readiness, and obvious utility problems have been ruled out.

The remaining issue may involve docking detection, internal valves or pumps, transfer controls, facility plumbing, infrastructure, internal sensors, or another service-level condition.

The affected equipment should be:

- Removed from service.
- Labeled **Out of Service** when appropriate.
- Sent for repair or bench evaluation, or the docking station isolated for service.
- Evaluated using appropriate Stryker documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Any waste-path repair requires appropriate contamination precautions and complete functional verification before return to service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Treat docking and waste-transfer connections as contaminated even when the rover appears empty, and never defeat an interlock to force a transfer cycle.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter; optional explanatory prose may follow. -->



## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Waste-transfer troubleshooting requires contamination control as well as logical isolation of positioning, docking interfaces, utilities, and readiness conditions. Do not bypass interlocks or open the waste path unnecessarily; escalate unresolved failures and document the completed transfer verification.

That is successful troubleshooting.
