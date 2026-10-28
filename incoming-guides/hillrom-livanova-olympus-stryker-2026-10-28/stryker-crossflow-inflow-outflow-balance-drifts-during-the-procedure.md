---
schemaVersion: 1
title: "Stryker CrossFlow Fluid Management System - Inflow/Outflow Balance Drifts During the Procedure"
issueTitle: "Inflow/Outflow Balance Drifts During the Procedure"
description: "Troubleshoots unstable fluid balance caused by tubing restrictions, suction changes, cassette problems, settings, leaks, or integrated resection activity."
assetType: "Fluid Management System"
manufacturer: "Stryker"
model: "CrossFlow"
slug: "stryker-crossflow-inflow-outflow-balance-drifts-during-the-procedure"
dateAdded: "2026-10-28"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that fluid balance became unstable whenever the shaver was activated during arthroscopy."
  cause: "Clinical Engineering found the shaver outflow tubing was partially kinked where it exited the cassette area."
  resolution: "Corrected the tubing routing, repeated shaver activation testing, verified stable pressure and outflow response, and returned the CrossFlow to service."
helpfulDetails:
  - "Procedure mode"
  - "Active surgeon profile"
  - "Pressure, flow, and suction configuration observed"
  - "Whether drift occurs with shaver or RF activation"
  - "Inflow tubing condition"
  - "Outflow line routing"
  - "Cassette condition and seating"
  - "External suction setup"
  - "Integration-cable condition"
  - "Known-good substitutions"
  - "Leakage findings"
  - "Results before and after correction"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots unstable fluid balance caused by tubing restrictions, suction changes, cassette problems, settings, leaks, or integrated resection activity.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Safe Fluid Management

A system that cannot reliably manage inflow and outflow should not remain the sole fluid-management device during an active procedure.

If excessive distention, loss of visualization, unexpected fluid consumption, or unstable pressure is occurring, immediately notify the clinical team. Transition to an approved alternative or replacement system as clinically appropriate before technical troubleshooting.

**Expected outcome:** Fluid management remains under reliable clinical control while the CrossFlow is evaluated.

### 2. Confirm What “Balance Drift” Means

Determine whether staff are reporting:

- Increasing fluid accumulation or distention
- Excessive suction
- Falling pressure during shaver or RF activation
- Increasing pressure when suction stops
- Unexpectedly high fluid consumption
- Different behavior between inflow-only and inflow/outflow operation
- Drift beginning only when a resection device is activated

CrossFlow can be used in inflow-only or inflow/outflow configurations, so confirm the actual setup before comparing behavior. [Stryker](https://www.stryker.com/us/en/sports-medicine/products/crossflow-integrated-arthroscopy-pump.html?utm_source=chatgpt.com)

**Expected outcome:** The drift is characterized by operating mode and by when it occurs.

If testing shows stable fluid management with no repeatable abnormality, proceed to final verification and document the unable-to-duplicate result.

### 3. Verify the Selected Procedure Settings

Confirm that the intended:

- Joint/procedure selection
- Pressure setting
- Flow setting
- Suction setting
- Surgeon profile
- Inflow/outflow mode

are actually active.

CrossFlow supports preset and customizable pressure, flow, suction, and surgeon-profile settings. [Stryker](https://www.stryker.com/us/en/sports-medicine/products/crossflow-integrated-arthroscopy-pump.html?utm_source=chatgpt.com)

Do not change clinical settings simply to make the system appear stable. Compare them with the intended approved setup.

**Expected outcome:** Active settings match the intended clinical configuration.

If an incorrect profile or setting caused the drift, correct it using authorized controls, verify stable operation, and stop troubleshooting.

### 4. Inspect the Inflow Path

Check:

- Fluid supply
- Spikes and connections
- Open clamps
- Kinked tubing
- Partially collapsed tubing
- Tubing trapped under equipment
- Cassette seating
- Leakage
- Fluid remaining in the source bags

An inflow restriction may cause apparent balance drift even when the console is operating normally.

**Expected outcome:** Inflow tubing is unrestricted and fluid reaches the pump normally.

If correcting an inflow restriction stabilizes operation, troubleshooting can stop after verification.

### 5. Inspect the Outflow Tubing and Connections

CrossFlow outflow tubing includes dedicated labeled paths for outflow, shaver, and RF suction. [Stryker](https://www.stryker.com/us/en/sports-medicine/products/crossflow-tubing.html?utm_source=chatgpt.com)

Verify that:

- Tubes are connected to the intended ports
- Labeled lines have not been crossed
- No line is kinked or compressed
- Connections are secure
- Suction tubing is not leaking
- Collection/waste components are correctly connected
- External suction conditions are appropriate

**Expected outcome:** The outflow paths are correctly connected and unrestricted.

If correcting tubing routing or a loose connection restores stable balance, the issue is resolved.

### 6. Inspect the Cassette Installation

Remove and inspect the cassette in a safe off-patient condition.

Check for:

- Incomplete seating
- Cassette deformation
- Fluid contamination
- Pressure-membrane damage
- Obstruction in the cassette bay
- Misalignment during installation

The inflow cassette's pressure-sensing membrane is part of how the system determines pressure. [Stryker](https://www.stryker.com/us/en/sports-medicine/products/crossflow-tubing.html?utm_source=chatgpt.com)

**Expected outcome:** The cassette is intact, properly installed, and consistently recognized.

If reseating or replacing the cassette restores stable pressure and fluid balance, troubleshooting can stop.

### 7. Determine Whether Drift Coincides With Shaver or RF Activation

CrossFlow can integrate fluid management with resection activity and adjust suction behavior based on the connected device. [Stryker](https://www.stryker.com/us/en/sports-medicine/products/crossflow-integrated-arthroscopy-pump.html?utm_source=chatgpt.com)

During controlled testing, determine whether instability appears:

- Only when the shaver starts
- Only when RF activates
- With either device
- Even when no resection device is active

If the problem is limited to integrated resection activity, inspect the integration and associated tubing before treating it as a primary pump problem.

**Expected outcome:** The relationship between balance drift and resection-device activation is clearly identified.

### 8. Verify CrossFlow-to-CrossFire 2 Integration When Used

When CrossFlow is integrated with a CrossFire 2 console, inspect the external communication connection and ensure both systems are operating normally.

Stryker specifies integration between CrossFlow and CrossFire 2 for coordinated fluid-management and resection behavior. [Stryker](https://www.stryker.com/us/en/sports-medicine/products/crossflow-integrated-arthroscopy-pump.html?utm_source=chatgpt.com)

Check:

- Communication cable security
- Connector damage
- Whether integration is recognized
- Whether the problem changes when a known-good approved cable is used

Do not access unauthorized configuration menus.

**Expected outcome:** CrossFlow and CrossFire 2 communicate consistently.

If restoring the external integration connection resolves the drift, perform final verification and stop troubleshooting.

### 9. Substitute Known-Good External Components

When appropriate and off-patient, compare operation using:

- Known-good compatible tubing
- Known-good cassette
- Known-good integration cable
- Known-good compatible resection setup

Change one variable at a time so the cause remains identifiable.

**Expected outcome:** The defective or incorrectly configured external component can be isolated.

If a known-good substitution restores stable operation, replace the failed external item and verify the complete system.

### 10. Check for Environmental or Mechanical Causes

Confirm:

- Tubing is not being compressed by equipment movement
- Waste tubing is not being lifted, kinked, or repositioned during use
- Fluid bags are not emptying unexpectedly
- The pump and connected equipment are stable on the cart or stand
- External suction sources are not being altered during the procedure

**Expected outcome:** No external environmental condition is creating intermittent flow changes.

### 11. Perform Controlled Functional Verification

Using approved test conditions and manufacturer documentation:

- Prime the system
- Establish stable inflow
- Verify pressure response
- Verify outflow operation
- Activate applicable integrated functions
- Observe whether pressure and flow remain stable through multiple cycles
- Inspect for leakage
- Confirm settings remain as selected

**Expected outcome:** Fluid management remains stable and repeatable through the required operating conditions.

If the device passes all required checks, it may be returned to service according to facility policy.

### 12. Escalate Persistent Balance Instability

If balance continues to drift with verified settings, correctly routed tubing, known-good disposables, and confirmed external integration, remove the unit from service.

Possible service-level categories include:

- Pressure-sensing fault
- Pump-control fault
- Suction-control problem
- Integration/communication fault
- Internal calibration or configuration issue

Do not perform internal adjustment or calibration without approved manufacturer procedures and test equipment.

**Expected outcome:** An unreliable system is withheld from clinical use and escalated appropriately.

## If the Problem Persists

Common external causes have been ruled out.

The CrossFlow should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate Stryker documentation and approved test equipment
- Repaired or configured only by qualified personnel

Return-to-service testing should verify stable inflow, outflow, pressure response, resection integration when applicable, controls, alarms, and leakage performance under representative operating conditions.

Stopping when the system cannot demonstrate repeatable fluid control is proper troubleshooting.

## Clinical Use Tip

Do not dismiss unexplained fluid-balance drift as a visualization problem; confirm both the fluid path and the integrated suction behavior before returning the system to use.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- rendered from front matter -->

## Final Thought

Begin with patient safety, then verify settings, tubing, cassette installation, suction paths, and external integration before suspecting an internal control problem. Confirm stable operation under representative conditions and document exactly what corrected the drift.

That is successful troubleshooting.
