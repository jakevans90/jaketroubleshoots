---
schemaVersion: 1
title: "Abbott Alinity hq Hematology Analyzer - Result Is Delayed, Missing, or Inconsistent"
issueTitle: "Result Is Delayed, Missing, or Inconsistent"
description: "Addresses delayed, absent, or inconsistent results caused by sample problems, analyzer status, QC, communication, workflow, identification, or analytical instability."
assetType: "Hematology Analyzer"
manufacturer: "Abbott"
model: "Alinity hq"
slug: "abbott-alinity-hq-result-is-delayed-missing-or-inconsistent"
dateAdded: "2026-10-06"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that results from the Abbott Alinity hq were completing on the analyzer but were intermittently missing from the LIS."
  cause: "Clinical Engineering found an unstable external network connection causing intermittent result transmission."
  resolution: "Clinical Engineering corrected the network connection and verified multiple approved test transmissions reached the intended downstream system while analyzer QC remained acceptable."
helpfulDetails:
  - "Sample identifier"
  - "Whether result was delayed, missing, or inconsistent"
  - "Whether result existed locally"
  - "Processing status"
  - "Sample and barcode condition"
  - "Reagent and fluidics status"
  - "QC and calibration status"
  - "Analyzer communication status"
  - "LIS or middleware status"
  - "Other systems affected"
  - "Recent changes"
  - "Repeat or comparison results"
  - "End-to-end verification result"
  - "Final analyzer status"
---
## What This Guide Helps With

Addresses delayed, absent, or inconsistent results caused by sample problems, analyzer status, QC, communication, workflow, identification, or analytical instability.

## Step-by-Step Troubleshooting

### 1. Protect Patient Results
Do not release or reconstruct questionable results outside approved laboratory procedures. If a result is missing, delayed, or inconsistent, ensure the specimen and patient identification remain controlled.

Use an alternate validated analyzer when clinically necessary.

**Expected outcome:** Patient care continues without relying on an unverified result.

### 2. Define the Result Problem Precisely
Determine whether the result is delayed, never generated, generated but not displayed, present on the analyzer but missing downstream, or analytically inconsistent with repeat testing or clinical expectations.

Record the sample identifier and timeline.

**Expected outcome:** The issue is categorized as processing, analytical, display, or communication related.

### 3. Verify Sample Identification
Confirm the correct specimen, barcode, rack position, and patient/order association were used.

Inspect for duplicate, unreadable, damaged, or incorrectly placed labels.

**Expected outcome:** The result is associated with the intended specimen and order. If an identification problem caused the apparent missing result, correct it only through approved laboratory procedures.

### 4. Check Analyzer Processing Status
Determine whether the sample is waiting, actively processing, held, rejected, repeated, or stopped because of another analyzer condition.

Review visible messages affecting the sample.

**Expected outcome:** The sample's current processing state is understood. If a simple workflow hold is safely resolved and the result completes normally, troubleshooting can stop after verification.

### 5. Check for Sample Quality Problems
Inspect the sample for clots, bubbles, inadequate volume, poor mixing, damaged tube, or other visible conditions that could delay or invalidate processing.

**Expected outcome:** No obvious specimen condition explains the result problem, or the issue is correctly identified as sample-related.

### 6. Verify Reagent, Fluidics, and Waste Status
Confirm the analyzer has the required reagents and fluids and is not operating under a wash, aspiration, waste, or fluidics fault.

**Expected outcome:** The analyzer is mechanically and fluidically ready for reliable sample processing.

### 7. Review QC and Calibration Status
Check whether current required laboratory QC and calibration status support reliable result generation.

Do not treat a communication fix as sufficient if analytical quality is also in question.

**Expected outcome:** Analytical readiness is verified. If QC is unacceptable, stop patient testing and troubleshoot the quality issue separately.

### 8. Determine Whether the Result Exists Locally
If the result is missing downstream, determine whether it is present and complete on the analyzer.

If present locally but absent from the LIS, focus troubleshooting on communication rather than repeating the test unnecessarily.

**Expected outcome:** Analytical generation is separated from result-transmission failure.

### 9. Check LIS and Network Communication
Review analyzer communication status and determine whether other results are transmitting normally. Coordinate with IT or the laboratory interface team when multiple results or systems are affected.

**Expected outcome:** The downstream result path is functioning or an infrastructure fault is identified for escalation.

### 10. Evaluate Inconsistent Results Carefully
For inconsistent values, determine whether the discrepancy follows one specimen, one sample preparation, one parameter, or multiple unrelated samples.

Use laboratory-approved repeat testing, alternate analyzer comparison, or control material as appropriate. Clinical Engineering should not interpret patient results clinically.

**Expected outcome:** A specimen-specific issue is distinguished from analyzer instability.

### 11. Review Recent Changes
Check for recent reagent replacement, calibration, maintenance, software or network changes, analyzer restart, relocation, or power events.

**Expected outcome:** Any relevant change is identified and evaluated before deeper troubleshooting.

### 12. Perform Final End-to-End Verification
Use approved laboratory material or a suitable test workflow to confirm normal sample processing, result generation, consistency, display, and downstream transmission.

**Expected outcome:** Results are generated consistently and arrive at the intended destination without abnormal delay. The issue is resolved and troubleshooting can stop.

## If the Problem Persists

Sample identification, specimen condition, processing state, reagents, fluidics, QC, calibration, and communication have been ruled out. The remaining cause may involve an internal analytical subsystem, data-processing fault, software condition, sensor, sample transport mechanism, interface configuration, middleware, or other service-level issue.

The analyzer should be:

- Removed from service when result integrity cannot be assured
- Labeled Out of Service
- Sent for repair or bench/service evaluation
- Evaluated using appropriate Abbott documentation and approved test equipment
- Repaired or configured only by qualified personnel

After service, complete required analytical verification, QC, and end-to-end result-transmission testing before patient testing resumes.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

When a result is missing, first determine whether it was never generated or was generated but failed to reach the LIS; those are different troubleshooting paths.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

A delayed or inconsistent result can originate from the specimen, analyzer, analytical process, or communication path. Trace each stage logically, protect result integrity, and verify the entire process before returning the analyzer to normal use.

That is successful troubleshooting.
