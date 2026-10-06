---
schemaVersion: 1
title: "Siemens Healthineers Atellica IM 1600 Immunoassay Analyzer - Quality-Control Results Are Out of Range"
issueTitle: "Quality-Control Results Are Out of Range"
description: "Use this guide when QC results fall outside laboratory acceptance criteria, shift unexpectedly, or show a new pattern of inconsistent performance."
assetType: "Immunoassay Analyzer"
manufacturer: "Siemens Healthineers"
model: "Atellica IM 1600"
slug: "siemens-healthineers-atellica-im-1600-quality-control-results-are-out-of-range"
dateAdded: "2026-10-06"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that QC for one Atellica IM 1600 assay shifted outside the laboratory's acceptable range."
  cause: "Clinical Engineering found the affected control material had insufficient usable volume for consistent aspiration while analyzer and reagent status were otherwise normal."
  resolution: "Fresh control material was loaded, repeat QC met laboratory acceptance criteria, and the assay was returned to patient testing."
helpfulDetails:
  - "Assay and QC level affected"
  - "QC pattern or trend"
  - "Control material and lot"
  - "Reagent status and recent reagent change"
  - "Calibration status"
  - "Sample volume and tube condition"
  - "Aspiration or fluidic events"
  - "Other assays affected"
  - "Corrective action performed"
  - "Repeat QC result"
  - "Final analyzer status"
---
## What This Guide Helps With

Use this guide when QC results fall outside laboratory acceptance criteria, shift unexpectedly, or show a new pattern of inconsistent performance.

## Step-by-Step Troubleshooting

### 1. Stop Affected Patient Testing

Do not release patient results for an affected assay while required QC is unacceptable.

Identify:
- Which assay is involved
- Which control level is affected
- Whether failure is isolated or widespread
- Whether a sudden shift, trend, or random pattern is present
- Whether the analyzer recently underwent calibration, reagent change, maintenance, or restart

**Expected outcome:** Affected patient testing is controlled and the QC failure pattern is identified. If a correctable external cause is found and repeat QC is accepted, troubleshooting can stop.

### 2. Verify QC Material

Confirm the correct QC material was used for the intended assay.

Check with laboratory staff for:
- Correct lot or material
- Correct preparation
- Proper mixing if applicable
- Proper storage and handling
- Adequate volume
- No visible contamination
- No known compromise during use

Do not independently alter laboratory QC targets or acceptance rules.

**Expected outcome:** Suitable QC material is confirmed. If a fresh or correctly prepared control produces acceptable results, the issue is resolved.

### 3. Inspect QC Containers and Loading

Verify QC tubes or cups are:
- Correctly positioned
- Unobstructed
- Adequately filled
- Free of bubbles where visible
- Properly labeled
- Compatible with normal aspiration

**Expected outcome:** The analyzer can reliably aspirate the QC sample. If correcting the container or loading restores acceptable QC, troubleshooting can stop.

### 4. Verify Reagent Status

Check the affected assay's reagent for:
- Correct identity
- Correct onboard status
- Proper seating
- No visible leakage or damage
- No unresolved reagent recognition issue

Determine whether the QC shift began after a reagent change.

**Expected outcome:** Reagent status is normal and stable. If replacing or correctly loading an identified problematic reagent restores acceptable QC, the issue is resolved.

### 5. Verify Calibration Status

Check whether the affected assay has:
- Valid calibration status
- Recent failed calibration
- Calibration performed immediately before the QC change
- An unresolved requirement for calibration

Do not force or bypass calibration validity.

**Expected outcome:** Calibration status is appropriate for the assay. If recalibration is legitimately required and successful calibration followed by QC resolves the problem, troubleshooting can stop.

### 6. Check for Analyzer-Wide Patterns

Compare QC across multiple assays and levels.

Determine whether:
- Only one assay is affected
- One control level is affected across assays
- Multiple unrelated assays shifted together
- Other aspiration or fluidic faults are occurring

This distinction helps separate material or assay-specific causes from broader analyzer performance problems.

**Expected outcome:** The problem is categorized as isolated or analyzer-wide.

### 7. Check Sample Handling, Probe, and Fluidic Status

Review recent analyzer events for evidence of:
- Aspiration problems
- Probe obstruction
- Air or bubble conditions
- Wash faults
- Waste problems
- Fluidic interruptions

Do not perform invasive probe or internal fluidic repair.

**Expected outcome:** No unresolved handling or fluidic condition is affecting measurement reliability. If an approved external correction restores acceptable QC, the issue is resolved.

### 8. Repeat QC After a Specific Corrective Action

Do not repeatedly rerun QC without addressing a likely cause.

After correcting the identified issue, run QC again under normal laboratory procedures.

**Expected outcome:** QC returns within the laboratory's established acceptance criteria and remains stable. Troubleshooting can stop.

### 9. Escalate Persistent QC Failure

If acceptable control material, reagent status, calibration, aspiration, and basic analyzer operation have been verified but QC remains unacceptable, remove the affected assay or analyzer from patient testing.

**Expected outcome:** Continued unreliable testing is prevented and the problem is escalated for qualified technical or application support.

## If the Problem Persists

If QC material, preparation, loading, reagent status, calibration, and external analyzer conditions have been verified, common external causes have been ruled out.

Possible remaining categories include internal fluidics, measurement system performance, assay configuration, software, environmental influence, or another service-level problem.

The analyzer or affected assay should be:
- Removed from service
- Labeled Out of Service when appropriate
- Sent for repair or qualified technical evaluation
- Evaluated using Siemens Healthineers documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not return the affected assay to clinical use until required QC is accepted by the laboratory after corrective action.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

An analyzer that runs samples normally is not necessarily safe for reporting; unacceptable QC means the affected patient results cannot be trusted.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Out-of-range QC should be treated as a result-reliability problem. Confirm control material, loading, reagent, calibration, and analyzer operation before considering internal failure, and resume patient testing only after accepted QC verifies the correction.

That is successful troubleshooting.
