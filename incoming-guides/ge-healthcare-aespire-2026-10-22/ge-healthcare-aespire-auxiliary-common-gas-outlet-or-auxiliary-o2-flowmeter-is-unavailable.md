---
schemaVersion: 1
title: "GE Healthcare Aespire Anesthesia Machine - Auxiliary Common Gas Outlet or Auxiliary O2 Flowmeter Is Unavailable"
issueTitle: "Auxiliary Common Gas Outlet or Auxiliary O2 Flowmeter Is Unavailable"
description: "Troubleshoots unavailable auxiliary gas output caused by supply, control position, connection, accessory, flowmeter, outlet, or external configuration problems."
assetType: "Anesthesia Machine"
manufacturer: "GE Healthcare"
model: "Aespire"
slug: "ge-healthcare-aespire-auxiliary-common-gas-outlet-or-auxiliary-o2-flowmeter-is-unavailable"
dateAdded: "2026-10-22"
taxonomyMode: "reuse"
ccr:
  complaint: "Anesthesia staff reported that no oxygen was available from the Aespire auxiliary oxygen flowmeter during room setup."
  cause: "Clinical Engineering found the attached oxygen tubing kinked tightly behind the equipment cart, preventing downstream flow."
  resolution: "Replaced and rerouted the tubing, verified normal auxiliary oxygen flow and shutoff, and completed functional testing successfully."
helpfulDetails:
  - "Auxiliary common gas outlet or O2 flowmeter involved"
  - "Type of gas supply in use"
  - "Pipeline or cylinder status"
  - "External control position"
  - "Outlet and connector condition"
  - "Flowmeter movement"
  - "Accessory or tubing condition"
  - "Known-good accessory substitution"
  - "Presence of downstream restriction"
  - "Audible leakage"
  - "Functional-test result"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots unavailable auxiliary gas output caused by supply, control position, connection, accessory, flowmeter, outlet, or external configuration problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Provide an Alternate Gas Source

If an auxiliary gas outlet or auxiliary oxygen flowmeter is needed for current patient care and is unavailable, use another verified gas-delivery source before troubleshooting.

Do not interrupt anesthesia delivery or another essential oxygen source to test the auxiliary function.

**Expected outcome:** Patient oxygenation and anesthesia support remain unaffected while the auxiliary function is evaluated.

### 2. Confirm Which Auxiliary Function Is Unavailable

Determine whether the complaint involves:

- Auxiliary common gas outlet
- Auxiliary oxygen flowmeter
- No gas output
- Low or intermittent output
- A control that will not activate
- An outlet that cannot accept the expected accessory
- Gas flow that is available from the main system but not the auxiliary pathway

**Expected outcome:** The exact unavailable function is identified and can be evaluated independently.

### 3. Verify the Machine Gas Supply

Confirm that the appropriate pipeline or cylinder gas supply is connected and available.

Inspect:

- Hose connections
- Wall connections
- Cylinder connection when applicable
- External gas-supply indicators
- Kinked or damaged hoses

**Expected outcome:** The required source gas is available to the anesthesia machine. If restoring the supply restores the auxiliary function, troubleshooting can stop after verification.

### 4. Verify External Control Position

Confirm that the applicable auxiliary outlet or flowmeter control is in the correct user-selectable position for the desired function.

Check for:

- Incorrect switch position
- Flow control set fully closed
- Control accidentally left in another operating mode
- Physical obstruction preventing movement

Do not alter protected configuration settings.

**Expected outcome:** The external controls are correctly positioned and move normally.

### 5. Inspect the Auxiliary Outlet and Connector

Inspect the external outlet for:

- Debris
- Foreign material
- Physical damage
- Bent or damaged mating accessories
- Loose connection
- Incorrect accessory
- Incomplete insertion or engagement

Do not insert tools into a gas outlet.

**Expected outcome:** The outlet is clean, undamaged externally, and used with the correct compatible connection. If correcting the connection restores output, troubleshooting can stop after functional verification.

### 6. Inspect the Auxiliary O2 Flowmeter

If the auxiliary oxygen flowmeter is involved, inspect the external flowmeter assembly for:

- Visible physical damage
- A control that binds
- A float or indicator that does not move as expected
- Cracks
- Evidence of impact
- Contamination

Do not disassemble or attempt internal flowmeter repair.

**Expected outcome:** The flowmeter control operates freely and the external assembly shows no obvious damage.

### 7. Substitute a Known-Good External Accessory

If a hose, adapter, oxygen tubing set, or other external accessory is attached, replace it with a compatible known-good item.

A downstream obstruction can make an available gas outlet appear nonfunctional.

**Expected outcome:** Gas output returns with the known-good accessory, identifying the original accessory as the cause.

### 8. Check for Downstream Restriction

Inspect attached tubing and accessories for:

- Kinks
- Closed clamps
- Blockage
- Damaged connectors
- Incorrect assembly

Disconnect downstream accessories under safe non-patient test conditions when appropriate to determine whether the restriction is external to the machine.

**Expected outcome:** The auxiliary outlet provides expected gas delivery when external restrictions are removed.

### 9. Compare With a Known-Good Machine When Needed

If operation remains unclear, compare the externally accessible control behavior and outlet setup with another verified Aespire or equivalent configuration.

Do not use comparison as a substitute for manufacturer functional testing.

**Expected outcome:** The comparison confirms whether the observed behavior is abnormal or caused by setup.

### 10. Perform Final Functional Verification

After correcting any external cause, verify the auxiliary gas function using the appropriate manufacturer-approved method and test equipment when required.

Verify:

- Gas is available only when intentionally selected
- Flow starts and stops normally
- Connections remain secure
- No audible or visible leakage is present
- The primary anesthesia system remains unaffected

**Expected outcome:** The auxiliary outlet or flowmeter functions reliably and safely. If so, troubleshooting is complete.

### 11. Remove From Service if the Auxiliary Function Remains Unreliable

If the auxiliary outlet or oxygen flowmeter is required for the machine's intended clinical use and cannot be verified, remove the machine from service.

If facility policy permits use without the unavailable auxiliary feature, the machine should only remain available after the limitation has been formally evaluated and managed by the responsible clinical and technical teams.

**Expected outcome:** An unresolved auxiliary gas-delivery problem is not ignored or returned to use without appropriate disposition.

## If the Problem Persists

External gas supply, user controls, connections, accessories, downstream restrictions, and visible outlet or flowmeter condition have been ruled out.

The remaining condition may involve an internal gas pathway, valve, regulator, flow-control component, outlet mechanism, configuration issue, or other service-level fault.

The device should be:

- Removed from service when the function is required for intended use
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Complete required gas-delivery, leak, functional, and anesthesia-machine return-to-service testing before clinical use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never depend on an unverified auxiliary gas outlet for patient oxygen delivery; establish a known-good alternate source before investigating the machine.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

An unavailable auxiliary gas function should be isolated methodically from the source to the outlet. Verify supply, controls, connectors, accessories, and downstream restrictions before suspecting an internal gas-path problem, then document the final verification or appropriate escalation.

That is successful troubleshooting.
