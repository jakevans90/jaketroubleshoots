---
schemaVersion: 1
title: "Abbott Alinity c Clinical Chemistry Analyzer - Sample/Reagent Pipettor Collision, Clot, or Aspiration Error"
issueTitle: "Sample/Reagent Pipettor Collision, Clot, or Aspiration Error"
description: "Troubleshoot pipettor collisions, clot detection, and aspiration failures caused by sample tubes, reagent cartridges, obstructions, or external handling conditions."
assetType: "Clinical Chemistry Analyzer"
manufacturer: "Abbott"
model: "Alinity c"
slug: "abbott-alinity-c-sample-reagent-pipettor-collision-clot-or-aspiration-error"
dateAdded: "2026-11-25"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported repeated sample pipettor collision errors when processing a specific specimen rack."
  cause: "Clinical Engineering found a sample tube improperly seated in its carrier, allowing it to protrude into the pipettor travel path."
  resolution: "The tube was correctly seated by laboratory personnel, the approved recovery sequence completed successfully, and subsequent functional checks and QC passed without additional errors."
helpfulDetails:
  - "Exact error message and timestamp"
  - "Sample or reagent pipettor affected"
  - "Specimen rack and position"
  - "Tube type and condition"
  - "Cartridge and carrier inspection findings"
  - "Visible pipettor condition"
  - "Consumable status"
  - "Results of recovery or initialization"
  - "QC results and final device status"
---

## What This Guide Helps With

Troubleshoot pipettor collisions, clot detection, and aspiration failures caused by sample tubes, reagent cartridges, obstructions, or external handling conditions.

## Step-by-Step Troubleshooting

### 1. Protect Patient Testing and Stop Unsafe Operation
- Notify laboratory personnel that the affected analyzer may not reliably process specimens.
- Stop affected testing using the approved laboratory workflow.
- Arrange testing on another validated analyzer when necessary.
- Do not attempt to reposition a pipettor while the instrument is operating.
- Treat all specimens and exposed fluid-path components as potentially biohazardous.
- If a collision has occurred, do not repeatedly restart movement without identifying the obstruction.

Expected outcome: Specimen processing is safely stopped or redirected, and the pipettor is not exposed to additional damage.

### 2. Confirm the Exact Pipettor Error
- Review the Alinity c event history and active error messages.
- Identify whether the failure involves the sample pipettor, reagent pipettor, or another liquid-handling operation.
- Determine whether the reported condition is a mechanical collision, clot detection, insufficient aspiration, or liquid-level detection problem.
- Record the affected specimen, reagent, rack position, and time when available.
- Determine whether the failure occurs consistently at the same position or intermittently across multiple tests.

Expected outcome: The affected pipetting operation and failure pattern are identified.

### 3. Inspect Sample Tubes and Carrier Positioning
- Verify that the tube or sample container is approved for the configured assay and sampling arrangement.
- Check for tilted tubes, improperly seated containers, incorrect caps, damaged carriers, or physical obstructions.
- Confirm the sample is positioned correctly in its assigned carrier.
- Have laboratory personnel assess specimen volume, clots, fibrin, bubbles, and other sample-quality concerns.
- Do not manually disturb the specimen or override sample acceptance requirements.

Expected outcome: The specimen is correctly positioned and suitable for the intended aspiration operation. If correcting a positioning problem restores verified operation, troubleshooting can stop.

### 4. Inspect Reagent Cartridges and Accessible Loading Areas
- Confirm that reagent cartridges are fully seated and correctly positioned.
- Look for protruding packaging, damaged cartridge housings, displaced containers, or visible spills.
- Verify that the expected reagent is available in the instrument inventory.
- Check for any obstruction in the accessible pipettor travel area without entering guarded moving mechanisms.
- If a cartridge has tipped or leaked inside the reagent area, stop and follow the manufacturer-approved spill and service process.

Expected outcome: No cartridge or accessible obstruction interferes with the pipettor path.

### 5. Check Pipettor Condition Without Manual Adjustment
- With the instrument in the manufacturer-approved safe state, visually inspect accessible probe surfaces.
- Look for visible bending, residue, dried material, or signs of physical contact.
- Do not bend, straighten, manually align, or force the pipettor.
- Do not attempt internal tubing, motor, or alignment repairs.
- If probe damage is visible, remove the affected module from service.

Expected outcome: No visible pipettor damage is present, or suspected damage is identified for qualified service evaluation.

### 6. Verify Consumables and Operating Conditions
- Check applicable wash solution, cleaning solution, water supply, and waste status.
- Review whether the analyzer reports liquid-handling pressure, aspiration, or wash-related faults.
- Confirm appropriate reagent availability and that no required consumable is depleted.
- Review whether a recent reagent or consumable change immediately preceded the error.

Expected outcome: External liquid-handling supplies and consumables are available, correctly installed, and free of reported faults.

### 7. Perform an Approved Functional Check
- Once external problems are corrected, allow the analyzer to complete the applicable manufacturer-approved recovery or initialization process.
- Observe the affected pipetting operation through normal guarded operation.
- Have laboratory personnel perform the appropriate system checks, calibration, and QC as required.
- Verify that no collision, clot, or aspiration errors recur.

Expected outcome: The pipettor completes its operating sequence without errors and the laboratory accepts the verification results. Troubleshooting can stop.

### 8. Escalate Repeated Failures
- If errors recur with correctly positioned specimens and verified consumables, stop testing on the affected module.
- Preserve the event history and affected-position information.
- Contact Abbott technical support or authorized service personnel.

Expected outcome: The unresolved fault is documented and transferred for manufacturer-level evaluation without additional mechanical damage.

## If the Problem Persists

Once sample positioning, reagent seating, consumables, and visible obstructions have been ruled out, the problem may involve pipettor positioning, liquid-level sensing, aspiration components, motion control, or another internal liquid-handling mechanism.

The affected analyzer or module should be:

- Removed from service and labeled **Out of Service**.
- Sent for repair or bench evaluation by qualified personnel.
- Evaluated using current Abbott service documentation and approved diagnostic equipment.
- Repaired, adjusted, or calibrated only by authorized personnel.
- Returned to service only after required functional testing, applicable calibration, and acceptable laboratory QC.

Knowing when to stop external troubleshooting is part of proper Clinical Engineering practice.

## Clinical Use Tip

A pipettor collision can affect subsequent specimens. Coordinate with laboratory leadership to determine whether previously processed samples require review or repeat testing.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Pipettor troubleshooting begins with patient testing continuity and careful inspection of specimens, consumables, and positioning. Confirm external causes before suspecting internal mechanisms, stop when damage is possible, escalate appropriately, and document both the correction and final verification.

That is successful troubleshooting.
