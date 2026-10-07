---
schemaVersion: 1
title: "Werfen ACL TOP 750 LAS Coagulation Analyzer - Result Is Delayed, Missing, or Inconsistent"
issueTitle: "Result Is Delayed, Missing, or Inconsistent"
description: "Troubleshoots delayed, missing, or inconsistent results caused by sample quality, workflow status, reagent/QC conditions, processing errors, or communication problems."
assetType: "Coagulation Analyzer"
manufacturer: "Werfen"
model: "ACL TOP 750 LAS"
slug: "werfen-acl-top-750-las-result-is-delayed-missing-or-inconsistent"
dateAdded: "2026-10-07"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that completed ACL TOP 750 LAS results were visible on the analyzer but missing from the LIS."
  cause: "Clinical Engineering found an external network connection problem preventing result transmission while analyzer testing remained functional."
  resolution: "Clinical Engineering restored the network connection, verified the correct results transmitted to the LIS, and confirmed normal end-to-end operation before automated reporting resumed."
helpfulDetails:
  - "Patient or test identifier according to privacy policy"
  - "Assay affected"
  - "Analyzer result status"
  - "LIS result status"
  - "Sample condition"
  - "Reagent status"
  - "Calibration status"
  - "QC status"
  - "Aspiration or fluidics alarms"
  - "Network or interface status"
  - "Whether other assays or samples were affected"
  - "Verification results"
  - "Final analyzer and LIS status"
---
## What This Guide Helps With

Troubleshoots delayed, missing, or inconsistent results caused by sample quality, workflow status, reagent/QC conditions, processing errors, or communication problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Confirm the Result Problem

Do not release a result that is missing, unexpectedly delayed, internally inconsistent, or questionable.

Use another verified testing pathway for urgent specimens when necessary.

Identify whether:
- The analyzer never generated a result
- The analyzer generated a result but LIS did not receive it
- The result is delayed
- Replicate results are unexpectedly inconsistent
- Only one assay is affected
- Multiple assays are affected

**Expected outcome:** The problem is classified as analytical, workflow-related, or communication-related.

### 2. Verify the Correct Patient Sample and Order

Confirm:
- Correct specimen
- Correct patient/order association
- Correct assay requested
- Sample is in the expected rack or position
- Barcode or identification is correct

Do not troubleshoot analytical performance until specimen identity is confirmed.

**Expected outcome:** The correct specimen and test request are being evaluated.

### 3. Review the Analyzer's Test Status

Using normal user-accessible screens, determine whether the test is:
- Pending
- In progress
- Completed
- Flagged
- Repeated
- Held
- Missing because of an analyzer error

Record any displayed flag or message exactly.

**Expected outcome:** The point at which the result workflow stopped is identified.

### 4. Inspect the Sample

Check for externally visible specimen concerns such as:
- Clot or fibrin
- Bubbles
- Insufficient volume
- Damaged container
- Incorrect positioning
- Obvious handling concern

If specimen quality is questionable, follow laboratory policy rather than repeatedly retesting the same unsuitable specimen.

**Expected outcome:** The specimen is appropriate for testing or is identified as the likely cause.

### 5. Check Reagent, Calibration, and QC Status

Verify the affected assay has:
- Recognized reagent
- Acceptable reagent status
- Valid calibration as required
- Acceptable QC

Do not interpret inconsistent patient results independently of assay readiness.

**Expected outcome:** The assay is in an acceptable analytical state.

### 6. Check for Sample-Handling or Fluidics Errors

Review for:
- Aspiration errors
- Probe faults
- Volume errors
- Clot or bubble messages
- Wash faults
- Waste or fluidics alarms

These conditions may explain why a result was delayed, suppressed, or unreliable.

**Expected outcome:** No unresolved sample-handling fault explains the result problem.

### 7. Separate Analyzer Results from LIS Transmission

If the result appears on the analyzer but not in the LIS, treat the problem as a communication pathway issue rather than an analytical failure.

Verify:
- Analyzer result exists
- Patient/order association is correct
- Communication status is normal
- Other results are transmitting

**Expected outcome:** The fault is isolated to either result generation or result transmission.

### 8. Compare Using Appropriate Verification Material

When inconsistent analytical results are suspected, use appropriate QC, laboratory verification material, or another validated comparison process according to laboratory policy.

Do not repeatedly test a patient specimen solely to obtain a preferred value.

**Expected outcome:** Analyzer performance is shown to be stable or the inconsistency is reproduced and confirmed.

### 9. Check for Workflow or Infrastructure Delays

If results are delayed but the analyzer appears functional, investigate:
- LIS/interface delays
- Network interruptions
- Queued testing
- Analyzer workload
- Held samples
- Middleware or host-system availability

Coordinate with laboratory or IT personnel when appropriate.

**Expected outcome:** Any external workflow or infrastructure delay is identified.

### 10. Perform Final Functional Verification

After correcting the cause, verify:
- Test completes normally
- Result is generated
- Result is associated with the correct specimen
- Required QC remains acceptable
- Result transmits to the LIS when applicable
- No repeat unexplained inconsistency occurs

**Expected outcome:** The complete testing and reporting pathway functions reliably. Troubleshooting can stop.

## If the Problem Persists

If specimen identity and quality, reagent status, calibration, QC, sample handling, and communication pathways have been verified but results remain delayed, missing, or inconsistent, common external causes have been ruled out.

The remaining cause may involve analytical measurement systems, pipetting accuracy, fluidics, temperature control, software processing, data handling, interface configuration, or another internal or infrastructure-level condition.

The affected assay or analyzer should be:
- Removed from patient testing
- Labeled Out of Service as appropriate
- Sent for repair or bench evaluation
- Evaluated using current Werfen documentation and approved test equipment
- Repaired, calibrated, or configured only by qualified personnel

Any potentially affected patient results should be handled according to laboratory quality procedures.

Return the analyzer to service only after reliable analytical performance, required QC, and end-to-end result reporting have been verified.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

When a result is missing, determine whether it was never generated or simply never transmitted; the corrective path is very different.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect result integrity first, separate analytical problems from communication problems, verify external and specimen-related causes before assuming internal failure, and escalate when reliable testing cannot be demonstrated.

That is successful troubleshooting.
