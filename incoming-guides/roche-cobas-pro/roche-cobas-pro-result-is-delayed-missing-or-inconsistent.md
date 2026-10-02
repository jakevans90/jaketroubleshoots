---
schemaVersion: 1
title: "Roche cobas pro Clinical Chemistry Analyzer - Result Is Delayed, Missing, or Inconsistent"
issueTitle: "Result Is Delayed, Missing, or Inconsistent"
description: "Troubleshoots delayed, missing, or inconsistent results caused by sample status, analyzer holds, QC, calibration, communication, workflow, or repeat-processing conditions."
assetType: "Clinical Chemistry Analyzer"
manufacturer: "Roche"
model: "cobas pro"
slug: "roche-cobas-pro-result-is-delayed-missing-or-inconsistent"
dateAdded: "2026-10-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported completed cobas pro results were visible on the analyzer but were not appearing in the LIS."
  cause: "Clinical Engineering found the analyzer's external network connection loose, interrupting result transmission while local analysis continued normally."
  resolution: "Secured the network connection, verified interface restoration, and confirmed an approved test result transmitted successfully to the LIS before normal reporting resumed."
helpfulDetails:
  - "Specimen and assay affected"
  - "Whether result is delayed, missing, or inconsistent"
  - "Analyzer sample status"
  - "Reagent status"
  - "Calibration status"
  - "QC status"
  - "Sample condition"
  - "Aspiration or fluidics alarms"
  - "Whether result exists locally"
  - "LIS/interface status"
  - "Network condition"
  - "Repeat-processing behavior"
  - "Result transmission after correction"
  - "Final analyzer status"
---
## What This Guide Helps With

Troubleshoots delayed, missing, or inconsistent results caused by sample status, analyzer holds, QC, calibration, communication, workflow, or repeat-processing conditions.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Define the Result Problem

Determine whether the result is:
- Still processing
- Held
- Missing from the analyzer
- Present on the analyzer but missing from the LIS
- Repeatedly inconsistent
- Associated with an analyzer error

Notify laboratory personnel of any potentially significant reporting delay and follow established critical-result or downtime procedures.

Do not release or reconstruct a result based on assumption.

**Expected outcome:** The missing or inconsistent result is traced to a specific specimen, assay, and workflow stage.

### 2. Verify Positive Specimen Identification

Confirm:
- Patient/sample identifier
- Tube barcode
- Rack position
- Requested assay
- Specimen currently loaded
- Whether the sample was rerun or moved

Resolve identification discrepancies before further troubleshooting.

**Expected outcome:** The specimen being investigated is unquestionably matched to the correct order and patient record.

### 3. Check Analyzer Sample Status

Review normal analyzer workflow information to determine whether the specimen is:
- Waiting
- In process
- Completed
- Held
- Rejected
- Requiring repeat testing
- Associated with an error

Record any message rather than repeatedly resubmitting the sample.

**Expected outcome:** The analyzer's current handling state is known.

### 4. Check Reagent, Calibration, and QC Status

Determine whether the assay is delayed or withheld because of:
- Reagent unavailable
- Reagent not recognized
- Calibration required or failed
- QC not acceptable
- Another analyzer readiness condition

Clinical Engineering should not override laboratory controls designed to prevent release of potentially invalid results.

**Expected outcome:** Any legitimate analytical hold is identified.

### 5. Inspect the Specimen and Sample Handling

Check with laboratory staff for:
- Insufficient volume
- Clot
- Fibrin
- Bubble or foam
- Damaged tube
- Incorrect placement
- Aspiration error

Review whether the analyzer logged a sampling-related fault.

**Expected outcome:** Sample-specific causes of delay or inconsistency are identified or ruled out.

### 6. Determine Whether the Result Exists Locally

If the result is missing from the LIS, verify whether it is visible and finalized at the analyzer.

This separates:
- Analytical failure
- Result-processing delay
- Interface transmission failure

Do not manually recreate or transmit a result unless authorized by laboratory procedure.

**Expected outcome:** The problem is localized to analysis, analyzer data handling, or downstream communication.

### 7. Check LIS and Network Communication

If the result is complete on the analyzer but absent downstream:
- Verify interface status
- Check accessible network connections
- Determine whether other results are transmitting
- Coordinate with LIS, middleware, or IT support
- Review queued or failed transmissions using authorized functions

**Expected outcome:** The communication pathway is confirmed or the point of failure is identified.

### 8. Evaluate Inconsistent Results Carefully

For inconsistent results, have laboratory staff determine whether repeat testing is clinically and procedurally appropriate.

Clinical Engineering should investigate associated:
- Aspiration errors
- Calibration status
- QC performance
- Reagent status
- Fluidics faults
- Analyzer alarms

Do not conclude that the first or second result is correct based solely on which appears more plausible.

**Expected outcome:** Analyzer-related conditions that could affect consistency are identified without independently interpreting clinical validity.

### 9. Verify Complete Recovery

After correcting the identified cause:
- Confirm the specimen processes normally
- Confirm the expected result is generated
- Confirm the result reaches the intended LIS destination when applicable
- Confirm required QC remains acceptable
- Have laboratory staff verify the result workflow before normal testing resumes

**Expected outcome:** Results are produced, associated, and transmitted consistently. Troubleshooting is complete.

### 10. Escalate Unresolved or Unreliable Results

Stop external troubleshooting if:
- Results remain inconsistent
- Samples repeatedly disappear from workflow
- Results cannot be reliably associated with specimens
- Analytical output remains unavailable despite normal external conditions
- Analyzer and LIS records disagree without a clear communication cause

**Expected outcome:** Potential result-integrity problems are prevented from affecting patient reporting and are escalated.

## If the Problem Persists

Common specimen, reagent, calibration, QC, workflow, and external communication causes have been ruled out. Remaining possibilities include internal analytical systems, pipetting, measurement hardware, software, data handling, database synchronization, middleware, or service-level configuration.

The affected analyzer or assay should be:
- Removed from service when result integrity cannot be assured
- Labeled Out of Service
- Sent for repair or qualified service evaluation
- Evaluated using Roche-approved documentation and approved test equipment
- Repaired or configured only by qualified personnel

Complete required calibration, QC, functional, and end-to-end result-transmission verification before return to patient testing.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Always determine whether a “missing result” is missing from the analyzer, merely held, or only missing from the LIS before troubleshooting the wrong system.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Result problems require tracing the complete path from specimen identification through analysis and final transmission. Verify each stage before assuming internal failure, protect result integrity throughout, and escalate unresolved discrepancies with clear documentation.

That is successful troubleshooting.
