---
schemaVersion: 1
title: "Abbott Alinity hq Hematology Analyzer - Reagent Is Not Recognized or Inventory Is Incorrect"
issueTitle: "Reagent Is Not Recognized or Inventory Is Incorrect"
description: "Addresses unrecognized reagents or inaccurate inventory caused by installation, identification, container condition, consumable status, connections, or inventory synchronization issues."
assetType: "Hematology Analyzer"
manufacturer: "Abbott"
model: "Alinity hq"
slug: "abbott-alinity-hq-reagent-is-not-recognized-or-inventory-is-incorrect"
dateAdded: "2026-10-06"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that a newly installed reagent was not recognized by the Abbott Alinity hq."
  cause: "Clinical Engineering found the reagent container not fully seated in its assigned position."
  resolution: "Clinical Engineering reinstalled the reagent correctly, confirmed the analyzer recognized it and displayed the expected inventory state, and released the analyzer for laboratory quality verification."
helpfulDetails:
  - "Reagent or consumable affected"
  - "Exact displayed status"
  - "Whether replacement had just occurred"
  - "Container condition"
  - "Installation position"
  - "Accessible connection condition"
  - "Evidence of leakage"
  - "Known-good reagent substitution"
  - "Whether one or multiple reagents were affected"
  - "Inventory before and after correction"
  - "Final quality-verification result"
---
## What This Guide Helps With

Addresses unrecognized reagents or inaccurate inventory caused by installation, identification, container condition, consumable status, connections, or inventory synchronization issues.

## Step-by-Step Troubleshooting

### 1. Protect Result Integrity
Do not release patient results if reagent identification or available-volume status is unreliable. Follow the laboratory's alternate testing or downtime process until reagent status is verified.

Identify which reagent or consumable is affected and whether the problem began after replacement.

**Expected outcome:** Patient testing is protected and the affected reagent is identified.

### 2. Confirm the Reported Inventory Condition
Determine whether the analyzer shows the reagent as missing, unidentified, empty, expired, unavailable, incorrectly installed, or at an unexpected inventory level.

Record the exact displayed status before making changes.

**Expected outcome:** The failure is clearly documented. If the displayed inventory corrects after a normal screen refresh or approved workflow action and remains stable, troubleshooting can stop after verification.

### 3. Inspect the Reagent Container
Verify the correct reagent is installed for the validated analyzer workflow. Inspect the container for obvious damage, leakage, deformation, incorrect orientation, or contamination.

Confirm labeling and identification features are intact and readable.

**Expected outcome:** The correct, intact reagent container is installed. If replacing a visibly damaged container resolves recognition, verify inventory and stop.

### 4. Verify Reagent Seating and Position
Remove and reinstall the affected reagent only according to approved laboratory handling procedures. Make sure the container is fully seated in the intended position and any accessible connections are properly engaged.

Do not force a container into position.

**Expected outcome:** The reagent is properly seated and recognized. If inventory updates correctly, troubleshooting can stop after verifying normal readiness.

### 5. Inspect Accessible Reagent Connections
Check accessible tubing, caps, connectors, pickup interfaces, and surrounding surfaces associated with the affected reagent for looseness, kinks, leakage, dried residue, or improper installation.

Do not disconnect internal fluid lines.

**Expected outcome:** Accessible reagent connections are intact and correctly installed. If correcting an external connection restores recognition or inventory, verify and stop.

### 6. Check Reagent Identification Information
Confirm the installed container's identification information is intact and compatible with the laboratory's current inventory workflow.

If appropriate, compare with a known-good reagent container from approved stock.

**Expected outcome:** A known-good container is recognized normally. If the problem follows the original reagent container, remove that container from use and stop.

### 7. Allow Inventory to Update Normally
After correcting installation, allow the analyzer to complete its normal reagent recognition or inventory update process.

Avoid repeated removal and reinsertion that could complicate the inventory state.

**Expected outcome:** The analyzer displays a stable and plausible reagent status. If the status remains correct through normal operation, troubleshooting can stop.

### 8. Verify No Broader Consumable Problem Exists
Check whether multiple reagents or consumables are simultaneously showing incorrect states. A multi-item issue may suggest a broader reader, configuration, software, or communication condition rather than multiple bad containers.

**Expected outcome:** Either the issue remains isolated to one consumable or a broader pattern is identified for escalation.

### 9. Perform Final Functional Verification
Confirm the analyzer reaches the appropriate ready state and complete required laboratory quality checks before relying on the reagent for patient testing.

**Expected outcome:** Reagent identification and inventory are stable, and required quality verification is satisfactory. The issue is resolved and troubleshooting can stop.

## If the Problem Persists

Container installation, reagent condition, accessible connections, identification, and known-good substitution have been ruled out. The remaining cause may involve a reagent reader, level-detection system, fluidics interface, software inventory state, configuration, or other service-level condition.

The analyzer should be:

- Removed from service if reagent status cannot be trusted
- Labeled Out of Service
- Sent for repair or bench/service evaluation
- Evaluated using appropriate Abbott documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not manually override reagent status without an approved laboratory or manufacturer-supported process. Complete required quality verification before return to patient testing.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A reagent inventory problem is a result-integrity issue; do not continue patient testing merely because the analyzer can still aspirate samples.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Treat reagent recognition as a quality and result-integrity problem. Confirm installation, container condition, identification, and accessible connections before escalating to reader, fluidics, software, or configuration service.

That is successful troubleshooting.
