---
schemaVersion: 1
title: "Roche cobas pro Clinical Chemistry Analyzer - Calibration Fails or Will Not Complete"
issueTitle: "Calibration Fails or Will Not Complete"
description: "Troubleshoots calibration failures caused by calibrator handling, reagent status, sample loading, consumables, fluidics, settings, or analyzer readiness."
assetType: "Clinical Chemistry Analyzer"
manufacturer: "Roche"
model: "cobas pro"
slug: "roche-cobas-pro-calibration-fails-or-will-not-complete"
dateAdded: "2026-10-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported calibration for an assay repeatedly stopped before completion on the cobas pro."
  cause: "Clinical Engineering found the calibrator tube was not fully seated in the sample carrier and was not being presented correctly for aspiration."
  resolution: "Corrected the tube seating, verified normal sample detection, and laboratory staff completed calibration and acceptable QC before returning the assay to service."
helpfulDetails:
  - "Assay affected"
  - "Exact calibration message"
  - "Whether calibration started or aborted"
  - "Reagent status"
  - "Calibrator preparation and placement"
  - "Rack or carrier condition"
  - "Wash and waste status"
  - "Other analyzer alarms"
  - "Whether other assays calibrate normally"
  - "Calibration result after correction"
  - "QC result after calibration"
  - "Final testing status"
---
## What This Guide Helps With

Troubleshoots calibration failures caused by calibrator handling, reagent status, sample loading, consumables, fluidics, settings, or analyzer readiness.

## Step-by-Step Troubleshooting

### 1. Protect Patient Testing and Confirm the Calibration Failure

Do not release patient results for an assay requiring successful calibration when calibration has failed or remains incomplete.

Confirm:
- Which assay is affected
- Whether calibration starts
- Whether it aborts or completes unsuccessfully
- Whether one or multiple assays are involved
- The exact displayed message

**Expected outcome:** The failed calibration and affected testing are clearly identified and held from clinical reporting as appropriate.

### 2. Verify Analyzer Readiness

Confirm the analyzer and required module are fully initialized and not showing unresolved faults involving:
- Reagents
- Samples
- Fluidics
- Waste
- Temperature
- Consumables
- Probe or aspiration functions

Do not proceed with calibration while another unresolved analyzer fault could invalidate the process.

**Expected outcome:** The analyzer is otherwise ready for the calibration attempt.

### 3. Verify the Reagent Status

With laboratory staff, confirm the appropriate reagent is:
- Present
- Recognized
- Available
- Correctly loaded
- Not displaying another unresolved status that prevents calibration

Do not make laboratory reagent-validity decisions outside established laboratory procedures.

**Expected outcome:** The required reagent is correctly loaded and available.

### 4. Verify Calibrator Preparation and Identification

Have authorized laboratory personnel confirm:
- Correct calibrator selection
- Proper preparation
- Correct labeling
- Appropriate handling
- Correct placement
- Required volume is available

Clinical Engineering should focus on analyzer function rather than independently validating laboratory chemistry preparation.

**Expected outcome:** No obvious calibrator handling or loading problem is present.

### 5. Inspect Sample and Carrier Loading

Check that the calibrator container and carrier are:
- Properly seated
- Correctly oriented
- Detectable by the analyzer
- Free of obvious physical obstruction

Use a known-good carrier if a rack or carrier issue is suspected.

**Expected outcome:** The calibrator is physically presented to the analyzer correctly.

### 6. Check Accessible Consumables and Fluid Conditions

Verify externally accessible:
- Wash supplies
- Water or system fluid status
- Waste status
- Disposable consumables
- Required containers

Address only conditions covered by normal technical or laboratory procedures.

**Expected outcome:** No external supply or waste condition is preventing successful calibration.

### 7. Repeat Calibration Only After a Correctable Cause Is Addressed

Do not repeatedly rerun calibration without identifying a reason for the prior failure.

After correcting a documented external issue, have laboratory personnel initiate the appropriate calibration again and observe the process.

**Expected outcome:** Calibration completes successfully. If it does, proceed to required QC and stop troubleshooting once laboratory acceptance is confirmed.

### 8. Determine Whether the Failure Is Assay-Specific or System-Wide

Compare the affected calibration with other assays or modules.

A single-assay failure may point toward:
- Reagent/calibrator issues
- Assay-specific conditions

Multiple unrelated calibration failures may indicate:
- Fluidics
- Pipetting
- Environmental
- Analyzer readiness
- Service-level problems

**Expected outcome:** The failure scope is clearly established before escalation.

### 9. Perform Final Verification

After successful calibration:
- Confirm calibration is accepted by the analyzer
- Confirm no calibration-related alarms remain
- Have laboratory personnel run required QC
- Do not return the assay to patient testing until laboratory acceptance criteria are met

**Expected outcome:** Calibration and subsequent required QC are accepted. Troubleshooting is complete.

### 10. Escalate Persistent Calibration Failure

If appropriate reagent, calibrator handling, sample loading, supplies, and analyzer readiness have been verified but calibration continues to fail, stop external troubleshooting.

**Expected outcome:** The affected assay or analyzer is withheld from patient testing and escalated for qualified evaluation.

## If the Problem Persists

Common external causes have been ruled out. Persistent calibration failure may involve pipetting performance, fluidics, measurement systems, environmental control, internal sensing, software, assay configuration, or another service-level condition.

The affected analyzer or assay should be:
- Removed from service as required to prevent invalid reporting
- Labeled Out of Service when appropriate
- Sent for repair or qualified service evaluation
- Evaluated using Roche-approved documentation and approved test equipment
- Repaired or configured only by qualified personnel

Successful calibration and required QC must be completed before return to patient testing.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A completed calibration is not by itself permission to resume patient testing; required laboratory QC must also be acceptable.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Calibration failures require disciplined separation of laboratory-material problems from analyzer problems. Verify external conditions first, require successful QC afterward, and escalate persistent failures rather than repeatedly rerunning an unexplained calibration.

That is successful troubleshooting.
