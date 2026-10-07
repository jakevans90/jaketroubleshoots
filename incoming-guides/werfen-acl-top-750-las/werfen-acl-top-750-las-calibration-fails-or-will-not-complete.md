---
schemaVersion: 1
title: "Werfen ACL TOP 750 LAS Coagulation Analyzer - Calibration Fails or Will Not Complete"
issueTitle: "Calibration Fails or Will Not Complete"
description: "Troubleshoots calibration failures caused by calibration material, reagent status, sample handling, setup, fluidics, environmental conditions, or analyzer readiness."
assetType: "Coagulation Analyzer"
manufacturer: "Werfen"
model: "ACL TOP 750 LAS"
slug: "werfen-acl-top-750-las-calibration-fails-or-will-not-complete"
dateAdded: "2026-10-07"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that calibration for an ACL TOP 750 LAS assay repeatedly failed to complete."
  cause: "Clinical Engineering found visible bubbles in the calibration material that interfered with consistent aspiration."
  resolution: "Laboratory staff prepared fresh calibration material, Clinical Engineering verified normal aspiration and successful calibration, and required QC passed before patient testing resumed."
helpfulDetails:
  - "Assay affected"
  - "Exact calibration message"
  - "Calibration material and lot"
  - "Reagent status"
  - "Material condition"
  - "Sample volume"
  - "Visible bubbles or contamination"
  - "Associated aspiration or fluidics alarms"
  - "Repeat calibration result"
  - "QC result after calibration"
  - "Final assay status"
---
## What This Guide Helps With

Troubleshoots calibration failures caused by calibration material, reagent status, sample handling, setup, fluidics, environmental conditions, or analyzer readiness.

## Step-by-Step Troubleshooting

### 1. Protect Patient Testing and Confirm the Calibration Failure

Do not release patient results from an assay requiring a valid calibration when calibration is failed, incomplete, or otherwise unacceptable.

Identify:
- Which assay is affected
- Whether failure occurs consistently
- Whether other assays calibrate normally
- Exact analyzer message
- Whether calibration previously passed with the same setup

**Expected outcome:** The affected calibration and scope of the problem are clearly identified.

### 2. Verify Calibration Material

Confirm the correct calibration material is being used for the assay and that it is suitable for use according to laboratory procedures.

Inspect for:
- Incorrect material
- Container damage
- Contamination
- Preparation or handling concerns
- Storage concerns
- Expiration or status problems

Do not use material that appears compromised.

**Expected outcome:** Appropriate calibration material is available and prepared according to validated laboratory procedures.

### 3. Verify Reagent Status

Confirm the associated reagent:
- Is recognized by the analyzer
- Is correctly positioned
- Has no unresolved reagent warning
- Is appropriate for the calibration being attempted

If reagent recognition or inventory is abnormal, correct that problem before repeating calibration.

**Expected outcome:** Required reagent status is acceptable before calibration is attempted again.

### 4. Inspect the Calibration Sample and Loading Setup

Check the calibration container for:
- Adequate volume
- Correct placement
- External contamination
- Bubbles or foam visible in the sample
- Improper seating
- Identification problems

Do not repeatedly rerun obviously compromised material.

**Expected outcome:** Calibration material is properly loaded and available for aspiration.

### 5. Check for Broader Analyzer Problems

Determine whether the analyzer also has:
- Aspiration errors
- Probe errors
- Wash or waste faults
- Fluidics alarms
- Sample-detection problems
- Temperature or readiness warnings

A calibration failure may be secondary to a broader analyzer condition.

**Expected outcome:** No unresolved analyzer fault is present that would invalidate calibration.

### 6. Review Calibration Setup

Verify the assay and calibration selection in the normal user interface.

Confirm that staff have not selected the wrong assay, material, lot, or calibration sequence.

Do not alter validated assay parameters or restricted configuration values as a troubleshooting shortcut.

**Expected outcome:** The intended assay and calibration setup are selected correctly.

### 7. Repeat Calibration Using Verified Materials

After correcting any external issue, repeat the calibration according to the laboratory's approved workflow.

Observe whether:
- Material is aspirated normally
- Calibration completes
- Results are accepted by the analyzer
- The same failure repeats

**Expected outcome:** Calibration completes successfully and is accepted. If it does, continue with required QC and troubleshooting can stop after verification.

### 8. Confirm Quality Control Before Returning the Assay to Use

Following a successful calibration, run required QC according to laboratory procedure.

Do not assume a completed calibration alone is sufficient for patient testing.

**Expected outcome:** Required QC is acceptable and the assay is released according to laboratory policy. Troubleshooting can stop.

## If the Problem Persists

If calibration material, reagent status, loading, assay selection, and obvious analyzer conditions have been verified but calibration still fails, common external causes have been ruled out.

The remaining cause may involve pipetting accuracy, optical or mechanical measurement systems, temperature regulation, fluidics, analyzer calibration functions, assay configuration, or another service-level condition.

The affected assay or analyzer should be:
- Removed from patient use
- Labeled Out of Service as appropriate
- Sent for repair or bench evaluation if required
- Evaluated using current Werfen documentation and approved test equipment
- Repaired, calibrated, or configured only by qualified personnel

Do not adjust assay parameters or internal calibration mechanisms without authorized procedures.

Return the assay to service only after successful calibration and required QC.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A completed calibration is not the final release step; verify required QC before resuming patient testing.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect patient results by verifying materials, reagent status, sample handling, and analyzer readiness before assuming an internal calibration failure, then escalate when valid calibration cannot be established.

That is successful troubleshooting.
