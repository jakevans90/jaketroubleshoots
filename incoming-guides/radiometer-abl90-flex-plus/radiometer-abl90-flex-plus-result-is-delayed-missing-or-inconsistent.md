---
schemaVersion: 1
title: "Radiometer ABL90 FLEX PLUS Blood Gas Analyzer - Result Is Delayed, Missing, or Inconsistent"
issueTitle: "Result Is Delayed, Missing, or Inconsistent"
description: "Troubleshoot delayed, missing, or inconsistent results caused by specimen quality, analyzer readiness, QC, communication, workflow, or service-level analytical problems."
assetType: "Blood Gas Analyzer"
manufacturer: "Radiometer"
model: "ABL90 FLEX PLUS"
slug: "radiometer-abl90-flex-plus-result-is-delayed-missing-or-inconsistent"
dateAdded: "2026-10-07"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that results from the Radiometer ABL90 FLEX PLUS appeared on the analyzer but were intermittently missing from the LIS."
  cause: "Clinical Engineering found an unstable external network connection at the analyzer while local analytical performance and QC remained acceptable."
  resolution: "Clinical Engineering corrected the network connection, verified successful transmission of test results to the LIS, confirmed acceptable QC, and returned the analyzer to normal clinical workflow."
helpfulDetails:
  - "Whether the result appeared locally on the analyzer"
  - "Exact sample or result warning"
  - "Patient or specimen identification status"
  - "Specimen condition"
  - "Calibration status"
  - "QC results"
  - "Recent consumable changes"
  - "Whether one or multiple parameters were affected"
  - "Whether other analyzers had similar transmission issues"
  - "Network and LIS status"
  - "Comparison or verification results"
  - "End-to-end transmission result"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoot delayed, missing, or inconsistent results caused by specimen quality, analyzer readiness, QC, communication, workflow, or service-level analytical problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Confirm the Result Problem

Do not rely on a result that appears inconsistent with the specimen, clinical situation, QC status, or analyzer behavior. Follow laboratory policy for questionable results and route urgent testing to another verified analyzer.

Determine whether the result is delayed on the analyzer, missing from the LIS, absent entirely, or analytically inconsistent.

**Expected outcome:** The problem is categorized as processing, analytical, or communication-related and patient care is protected.

### 2. Verify the Analyzer's Local Result

Check whether the analyzer completed the test and produced a local result. Review any displayed sample warning, analyzer message, or status associated with the test.

Do not assume a missing LIS result means the analyzer failed to perform the measurement.

**Expected outcome:** It is known whether the analyzer generated the result locally. If the result exists locally but not downstream, focus on communication troubleshooting.

### 3. Verify Sample Identification

Confirm the sample was associated with the correct patient or specimen identification according to laboratory workflow.

Check for barcode-read failures, manual-entry errors, duplicate identifiers, or mismatched orders.

**Expected outcome:** The sample and result are correctly associated. Identification discrepancies are resolved according to laboratory policy before further use of the result.

### 4. Review Specimen Integrity

Inspect or review the specimen for potential clotting, air bubbles, insufficient volume, delay in testing, improper handling, or other collection concerns that could produce questionable results.

Clinical Engineering should coordinate with laboratory staff rather than make clinical judgments about result validity.

**Expected outcome:** Obvious specimen-related causes are either identified or reasonably ruled out.

### 5. Verify QC and Calibration Status

Confirm required QC is acceptable and the analyzer has a valid calibration state. Review whether the inconsistent result occurred near a calibration failure, consumable change, fluidics fault, or other analyzer event.

**Expected outcome:** The analyzer has acceptable calibration and QC performance. If QC is unacceptable, remove the analyzer from patient testing and address that condition first.

### 6. Repeat Using Appropriate Verification Material

When permitted by laboratory procedure, use appropriate control material or a suitable comparison process to determine whether the analyzer produces repeatable results.

Do not repeatedly consume a limited patient specimen solely for equipment troubleshooting.

**Expected outcome:** Verification material produces consistent acceptable performance. If so, investigate specimen or workflow factors before assuming analyzer failure.

### 7. Check Result Transmission

If the analyzer produced the correct local result, verify external network connections and determine whether the result reached the LIS, middleware, or downstream destination.

Coordinate with IT or LIS support if multiple devices or interfaces are affected.

**Expected outcome:** The result appears at the intended destination with the correct identification. If transmission is restored, the communication portion of the issue is resolved.

### 8. Look for a Repeatable Analyzer Pattern

Determine whether delays or inconsistencies occur with one specimen, one parameter, multiple parameters, or all testing.

Persistent problems across known-good controls or multiple specimens indicate a higher likelihood of an analyzer-level analytical or fluidics problem.

**Expected outcome:** The scope and repeatability of the problem are clearly documented for escalation if necessary.

### 9. Perform Final Functional Verification

Before return to unrestricted clinical use, verify analyzer readiness, acceptable calibration and QC, successful sample processing, correct result display, and correct transmission to the intended downstream system when applicable.

**Expected outcome:** Results are generated consistently, appear within the expected workflow, and transmit correctly. Troubleshooting can stop.

## If the Problem Persists

Specimen condition, identification, calibration, QC, external communication, and obvious workflow causes have been ruled out. Persistent delayed, missing, or inconsistent results may involve internal analytical systems, sensors, fluidics, software, data processing, network hardware, middleware, or other service-level conditions.

The analyzer should be:

- Removed from service when result reliability cannot be assured.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate Radiometer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Coordinate with laboratory leadership, LIS support, middleware support, or IT when the problem extends beyond the analyzer. Following repair, complete required calibration, QC, functional testing, and end-to-end result verification before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

When a blood gas result appears clinically inconsistent, laboratory staff should follow their verification procedure rather than assume either the analyzer or the patient value is correct.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Separate specimen, analytical, and communication causes before deciding that a result problem is an analyzer failure. Protect patient care, verify QC and calibration, confirm the complete result path, escalate unresolved reliability concerns, and document the evidence clearly.

That is successful troubleshooting.
