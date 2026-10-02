---
schemaVersion: 1
title: "Roche cobas pro Clinical Chemistry Analyzer - Reagent Is Not Recognized or Inventory Is Incorrect"
issueTitle: "Reagent Is Not Recognized or Inventory Is Incorrect"
description: "Troubleshoots unrecognized reagents and incorrect inventory caused by loading, identification, container condition, positioning, workflow status, or communication errors."
assetType: "Clinical Chemistry Analyzer"
manufacturer: "Roche"
model: "cobas pro"
slug: "roche-cobas-pro-reagent-is-not-recognized-or-inventory-is-incorrect"
dateAdded: "2026-10-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported a newly loaded reagent was physically present but remained unavailable in the cobas pro inventory."
  cause: "Clinical Engineering found the reagent container was not fully seated in its loading position."
  resolution: "Reseated the container, verified correct analyzer recognition and inventory update, and had laboratory staff complete required assay verification before reuse."
helpfulDetails:
  - "Reagent or assay affected"
  - "Exact displayed status"
  - "Whether one or multiple reagents were affected"
  - "Container condition"
  - "Identification surface condition"
  - "Loading position"
  - "Known-good reagent comparison"
  - "Inventory status before and after correction"
  - "Recent analyzer restart or service"
  - "Calibration or QC required afterward"
  - "Final analyzer status"
---
## What This Guide Helps With

Troubleshoots unrecognized reagents and incorrect inventory caused by loading, identification, container condition, positioning, workflow status, or communication errors.

## Step-by-Step Troubleshooting

### 1. Protect Patient Testing and Confirm the Reagent Problem

Do not report patient results from an assay when required reagent identity, availability, or inventory status is uncertain.

Determine whether:
- One reagent is affected
- One assay is affected
- Multiple reagents are affected
- Inventory quantity is wrong
- The reagent is physically present but shown as unavailable
- Recognition failed after replacement or loading

Record the exact analyzer message and reagent status.

**Expected outcome:** The specific reagent-recognition or inventory discrepancy is defined and affected testing is withheld.

### 2. Verify the Correct Reagent Was Loaded

Confirm with laboratory staff that the reagent:
- Is intended for the required assay
- Is appropriate for the analyzer workflow
- Has not been accidentally exchanged with another container
- Was loaded in the expected position and orientation

Clinical Engineering should not make reagent-selection decisions that belong to laboratory procedure.

**Expected outcome:** The correct reagent is confirmed to be loaded in the appropriate location.

### 3. Inspect the Reagent Container

Check the affected reagent container externally for:
- Damage
- Leakage
- Deformation
- Contamination
- Improper seating
- Obstruction around identification features

Do not manipulate sealed reagent components beyond approved handling.

**Expected outcome:** The container is intact and seated normally. If reseating an otherwise valid container restores recognition, troubleshooting can stop after verification.

### 4. Check Reagent Identification Surfaces

Inspect accessible barcode, RFID, label, or other identification areas used by the laboratory workflow for:
- Damage
- Contamination
- Moisture
- Obstruction
- Poor positioning

Do not alter reagent identification information.

**Expected outcome:** The reagent's identification features are unobstructed and intact.

### 5. Compare With a Known-Good Reagent

When laboratory policy permits, have authorized laboratory staff load a verified compatible reagent or reagent pack.

Determine whether:
- The replacement is recognized normally
- The problem follows the original reagent
- Multiple valid reagents fail in the same location

**Expected outcome:** The problem is isolated to the original reagent/container or to the analyzer's recognition path.

### 6. Verify Inventory Updates After Normal Loading

Allow the analyzer to complete its normal reagent loading and inventory process.

Observe whether:
- The reagent appears in inventory
- The correct status is displayed
- The quantity or availability updates
- Duplicate or stale entries remain

Avoid unauthorized inventory edits or service-level configuration changes.

**Expected outcome:** Analyzer inventory matches the physically loaded reagent status.

### 7. Check for Widespread Recognition Problems

Determine whether other reagent positions are recognized normally.

If many reagents become unrecognized simultaneously, consider:
- Recent analyzer restart
- Communication fault
- Module not initialized
- Identification subsystem issue
- Recent service or configuration event

**Expected outcome:** The scope is established as isolated or system-wide.

### 8. Perform Final Verification

After correction:
- Confirm reagent recognition
- Confirm appropriate inventory status
- Confirm affected assay becomes available when all laboratory conditions are met
- Have laboratory staff perform required calibration or QC before releasing patient results when appropriate

**Expected outcome:** Reagent recognition and inventory are correct and laboratory verification is satisfactory. Troubleshooting is complete.

### 9. Escalate if Recognition Remains Unreliable

If known-good reagents are not reliably recognized after loading, seating, identification surfaces, and normal inventory processing are checked, stop external troubleshooting.

**Expected outcome:** The analyzer is prevented from producing results dependent on uncertain reagent identification and the issue is escalated.

## If the Problem Persists

External reagent handling and identification causes have been ruled out. The remaining problem may involve internal reagent sensing, identification readers, module communication, inventory database synchronization, software, or service-level configuration.

The affected analyzer or module should be:
- Removed from service when reagent identity cannot be assured
- Labeled Out of Service as appropriate
- Sent for repair or appropriate service evaluation
- Evaluated using Roche-approved documentation and approved test equipment
- Repaired or configured only by qualified personnel

Required calibration, QC, and laboratory verification must be completed before patient testing resumes.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Correct physical reagent placement is not enough; patient testing should resume only when the analyzer also identifies and tracks that reagent correctly.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Treat reagent identity as a patient-safety issue. Verify the physical container, recognition path, and displayed inventory before assuming an internal analyzer failure, and require appropriate laboratory verification after correction.

That is successful troubleshooting.
