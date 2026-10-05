---
schemaVersion: 1
title: "Beckman Coulter DxC 700 AU Clinical Chemistry Analyzer - Result Is Delayed, Missing, or Inconsistent"
issueTitle: "Result Is Delayed, Missing, or Inconsistent"
description: "Use when expected chemistry results are late, absent, repeated unexpectedly, or inconsistent with other verified testing."
assetType: "Clinical Chemistry Analyzer"
manufacturer: "Beckman Coulter"
model: "DxC 700 AU"
slug: "beckman-coulter-dxc-700-au-result-is-delayed-missing-or-inconsistent"
dateAdded: "2026-10-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that completed DxC 700 AU results were visible on the analyzer but were delayed in the LIS."
  cause: "Clinical Engineering found an intermittent external network connection at the analyzer workstation."
  resolution: "The network connection was secured, test results were transmitted successfully, and normal analyzer-to-LIS result flow was verified."
helpfulDetails:
  - "Assay affected"
  - "Whether result exists on analyzer"
  - "Whether result reached LIS"
  - "Specimen identification status"
  - "Sample condition"
  - "Analyzer flags"
  - "Reagent and calibration status"
  - "QC status"
  - "Repeat or comparison result"
  - "Communication test result"
  - "Final analyzer and LIS status"
---
## What This Guide Helps With

Use when expected chemistry results are late, absent, repeated unexpectedly, or inconsistent with other verified testing.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Result Integrity
Do not release questionable results solely because the analyzer completed a run. Notify laboratory personnel to follow approved procedures for delayed or suspect results and redirect urgent testing if necessary.

**Expected outcome:** Clinical decisions are not based on unverified analyzer results.

### 2. Confirm the Exact Result Problem
Determine whether the result is missing from the analyzer, present on the analyzer but missing from the LIS, delayed in processing, flagged, duplicated, or inconsistent with repeat or comparison testing.

**Expected outcome:** The issue is categorized as analytical, processing, identification, or communication related.

### 3. Verify Specimen Identification
Confirm specimen identity, barcode readability, rack position, and order information. Check for specimen swaps, duplicate labels, or incorrect accession association.

**Expected outcome:** The result is confirmed to belong to the correct specimen and order.

### 4. Review Sample Condition
Inspect available specimen information for inadequate volume, clotting, bubbles, contamination, or another condition that could cause incomplete or abnormal processing.

**Expected outcome:** The sample is suitable for analysis or a specimen-related cause is identified.

### 5. Check Analyzer Status and Flags
Review the normal analyzer interface for flags, rerun status, aspiration messages, reagent issues, calibration status, or other conditions associated with the affected result.

**Expected outcome:** Any analyzer-generated condition affecting the result is identified and addressed appropriately.

### 6. Verify Reagent, Calibration, and QC Status
Confirm required reagents are recognized and appropriate, calibration is valid, and QC meets laboratory acceptance criteria for the affected assay.

**Expected outcome:** The analytical system is verified suitable for the assay before the result is trusted.

### 7. Separate Analytical From Communication Problems
If the result is correct and complete on the analyzer but absent or delayed in the LIS, troubleshoot the barcode/LIS/network path rather than the analytical subsystem.

**Expected outcome:** Communication problems are distinguished from true analytical result problems.

### 8. Compare With an Approved Repeat or Alternate Method When Appropriate
Follow laboratory policy for repeat testing or comparison using approved material or another validated analyzer. Do not repeatedly rerun specimens simply to obtain a preferred value.

**Expected outcome:** Comparison testing confirms whether the original discrepancy follows the specimen, assay, or analyzer.

### 9. Verify Result Flow and Consistency
After correction, confirm the analyzer produces expected results, required QC remains acceptable, and results reach the intended laboratory information workflow correctly.

**Expected outcome:** Results are complete, timely, traceable, and analytically acceptable. Troubleshooting can stop.

## If the Problem Persists

Specimen identification, sample condition, reagent status, calibration, QC, and external communication causes have been ruled out. The remaining issue may involve aspiration, measurement stability, processing software, data handling, internal timing, interface services, or another service-level analyzer condition.

Remove affected testing from service when result reliability cannot be assured. Label the analyzer Out of Service and arrange qualified evaluation using Beckman Coulter documentation and approved test equipment. Coordinate with LIS or network support when the analytical result is correct but data transfer remains unreliable.

Return the analyzer to service only after required QC, functional testing, and end-to-end result verification demonstrate dependable operation.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

When a result is missing, first determine whether it never existed on the analyzer or simply failed to reach the LIS; those are two different troubleshooting paths.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Delayed or inconsistent results require separating specimen, analytical, and communication causes methodically. Protect patient care, verify basic conditions before assuming internal failure, escalate unresolved reliability concerns, and document the entire result path clearly.

That is successful troubleshooting.
