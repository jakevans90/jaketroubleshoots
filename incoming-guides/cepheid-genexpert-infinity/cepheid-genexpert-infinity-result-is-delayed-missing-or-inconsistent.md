---
schemaVersion: 1
title: "Cepheid GeneXpert Infinity Molecular Diagnostic System - Result Is Delayed, Missing, or Inconsistent"
issueTitle: "Result Is Delayed, Missing, or Inconsistent"
description: "Troubleshoot delayed, missing, or inconsistent results by separating assay completion, specimen, cartridge, module, software, communication, and result-routing causes."
assetType: "Molecular Diagnostic System"
manufacturer: "Cepheid"
model: "GeneXpert Infinity"
slug: "cepheid-genexpert-infinity-result-is-delayed-missing-or-inconsistent"
dateAdded: "2026-10-08"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that completed GeneXpert Infinity results were visible locally but missing from the LIS."
  cause: "Clinical Engineering found loss of network communication between the analyzer workstation and the laboratory network while local testing remained complete."
  resolution: "Clinical Engineering restored the external network connection and coordinated verification that a completed test result successfully transmitted through the interface to the LIS."
helpfulDetails:
  - "Specimen and assay involved"
  - "Exact error or status"
  - "Test start and completion times"
  - "Whether a result exists locally"
  - "Patient and order association"
  - "Cartridge condition"
  - "Affected module"
  - "Other recent test behavior"
  - "Workstation status"
  - "LIS/network status"
  - "End-to-end verification result"
  - "Final equipment status"
---
## What This Guide Helps With

Troubleshoot delayed, missing, or inconsistent results by separating assay completion, specimen, cartridge, module, software, communication, and result-routing causes.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Decision-Making
Notify laboratory personnel that the affected result pathway is under evaluation. Do not allow clinicians to rely on an incomplete, inconsistent, or unverified result.

Urgent specimens should be redirected according to laboratory downtime or alternate-testing procedures when necessary.

**Expected outcome:** Clinical decisions are not based on questionable or unavailable results.

### 2. Confirm What Happened to the Result
Determine whether the assay failed to complete, completed without displaying a result, displayed locally but did not reach the LIS, produced an unexpected result pattern, or was significantly delayed.

Record the specimen, assay, cartridge, module, timestamps, and exact messages involved.

**Expected outcome:** The problem is narrowed to test processing, result generation, local display, or downstream transmission.

### 3. Verify Patient and Specimen Identification
Confirm with laboratory staff that the correct specimen, patient identifier, barcode, test order, and assay were associated with the run.

Do not correct patient identification outside established laboratory procedures.

**Expected outcome:** The result is associated with the intended specimen and order.

### 4. Review the Test Status
Determine whether the test completed normally, stopped with an error, remained in progress, or was interrupted. Check for power, module, automation, or workstation events occurring during the run.

**Expected outcome:** The system state explains whether the issue occurred before or after result generation.

### 5. Inspect Cartridge and Sample Factors
With laboratory staff, review whether the cartridge was appropriate and intact and whether sample preparation met the validated workflow.

Look for a pattern involving a particular cartridge, lot, specimen type, or assay.

**Expected outcome:** Obvious sample or consumable causes are identified or ruled out.

### 6. Determine Whether the Problem Follows a Module
Review whether delays or inconsistent results repeatedly occur on one GeneXpert module while comparable testing on other available modules is normal.

**Expected outcome:** A module-specific pattern is identified or ruled out.

### 7. Check Workstation and Application Status
Confirm the workstation is responsive and the GeneXpert application is functioning normally. Look for frozen screens, incomplete synchronization, storage warnings, or communication messages visible to the user.

Do not delete data or alter databases during troubleshooting.

**Expected outcome:** The local system can display and manage completed testing normally.

### 8. Check LIS and Network Routing
If a result exists locally but is missing downstream, inspect network connections and coordinate with laboratory IT or interface support to verify LIS and interface availability.

**Expected outcome:** The missing result is localized to the analyzer or downstream communication path.

### 9. Compare With Other Recent Tests
Review whether other specimens processed before and after the affected test completed and transmitted normally. Avoid drawing conclusions from a single unusual patient result without laboratory review.

**Expected outcome:** The issue is identified as isolated or part of a repeatable system pattern.

### 10. Perform Approved Functional Verification
After correcting an external issue, have laboratory staff perform appropriate approved verification using suitable material and confirm both local completion and downstream result transmission when applicable.

**Expected outcome:** Results complete consistently, display properly, and reach the intended system. If verified, troubleshooting can stop.

### 11. Escalate Unresolved Result Problems
If identification, specimen handling, cartridge factors, module behavior, workstation status, network communication, and result routing are all verified but results remain delayed, missing, or inconsistent, stop external troubleshooting.

**Expected outcome:** An unreliable result pathway is removed from clinical use pending qualified evaluation.

## If the Problem Persists

Common external specimen, cartridge, workflow, workstation, communication, and infrastructure causes have been ruled out. Remaining causes may involve an analyzer module, processing subsystem, software, database, interface configuration, or another service-level condition.

The affected GeneXpert Infinity system or module should be:

- Removed from service for the affected workflow
- Labeled **Out of Service**
- Sent for repair or qualified service evaluation
- Evaluated using current manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Following repair, verify test completion, result consistency, and the entire result-routing pathway. Laboratory quality requirements must be satisfied before patient testing resumes.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

When a result is missing, always determine whether the test failed to generate a result or whether a valid result exists but failed to reach the LIS.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Separate result generation from result transmission before assuming analyzer failure. Protect clinical decision-making, verify each step of the testing and communication pathway, escalate unresolved faults, and document the confirmed cause and final verification.

That is successful troubleshooting.
