---
schemaVersion: 1
title: "Fujifilm Sonosite PX Ultrasound System - Measurement Package or Calculation Function Error"
issueTitle: "Measurement Package or Calculation Function Error"
description: "Troubleshoots unavailable or incorrect measurement and calculation functions caused by exam selection, workflow, settings, inputs, configuration, or software state."
assetType: "Ultrasound System"
manufacturer: "Fujifilm Sonosite"
model: "PX"
slug: "fujifilm-sonosite-px-measurement-package-or-calculation-function-error"
dateAdded: "2026-08-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the expected calculation tools were unavailable during an examination on the SonoSite PX."
  cause: "Clinical Engineering found the system had been placed in a different exam preset that did not present the expected measurement package."
  resolution: "Restored the appropriate user-level exam selection, verified the required measurement workflow with a test study, and returned the system to service."
helpfulDetails:
  - "Measurement or calculation affected"
  - "Exam type or preset"
  - "Probe used"
  - "Imaging mode"
  - "Whether the tool was missing or produced an error"
  - "Patient/exam workflow state"
  - "Required input completion"
  - "Other measurements tested"
  - "Result after restart"
  - "Comparison with another system"
  - "Final functional result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots unavailable or incorrect measurement and calculation functions caused by exam selection, workflow, settings, inputs, configuration, or software state.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Decision-Making

Do not rely on measurements or calculations that appear inconsistent, unavailable, or incorrect.

If the result could influence diagnosis, treatment, medication, procedure decisions, or patient management, use another verified method or ultrasound system until the issue is resolved.

**Expected outcome:** Clinical decisions are not based on questionable measurement output.

### 2. Confirm the Exact Measurement Complaint

Record:

- Measurement or calculation being attempted
- Exam type or preset
- Transducer used
- Whether the tool is missing, disabled, or produces an unexpected result
- Whether the problem affects one calculation or the entire measurement package
- Whether the issue began after a configuration or software change

**Expected outcome:** The exact function and conditions producing the problem are identified.

### 3. Verify the Correct Exam Type and Preset

Confirm the system is using the intended clinical exam or preset for the measurement being performed.

Do not alter protected presets or clinical calculation definitions during troubleshooting unless authorized.

**Expected outcome:** The expected measurement package becomes available when the correct exam configuration is selected, or the problem persists under the correct setup.

### 4. Verify the Connected Transducer and Imaging Mode

Some measurement functions depend on the current probe and imaging mode.

Confirm the intended compatible probe is recognized and the required imaging mode is active.

**Expected outcome:** The appropriate measurement tools are available for the current probe and imaging context.

### 5. Confirm the Measurement Inputs Are Complete

Check whether the calculation requires multiple caliper placements, traces, patient data, or other user-entered values.

Review the workflow for incomplete entries without instructing clinicians on diagnostic interpretation.

**Expected outcome:** Required inputs are present and the system performs the calculation normally.

### 6. Check Basic Patient and Exam Data

Confirm the current study contains the basic information required for the intended workflow.

Incorrect or missing study information may prevent a calculation or cause an inappropriate package to appear.

**Expected outcome:** The calculation operates normally with a correctly established study.

### 7. Compare With Another Supported Measurement

Using an approved test workflow or phantom where appropriate, determine whether other basic measurement tools function.

**Expected outcome:** The problem is isolated to one measurement package or shown to affect measurement functionality more broadly.

### 8. Restart the System

When clinically appropriate, close the test workflow and perform a normal controlled restart.

Recreate the test under the same known conditions.

**Expected outcome:** Measurement functionality returns and remains stable, or the failure is reproducible after restart.

### 9. Compare With a Known-Good PX Configuration When Available

Where the facility has another appropriately configured SonoSite PX, compare visible exam selections and available measurement functions without copying or changing protected configuration.

**Expected outcome:** An obvious configuration difference is identified for authorized review, or the system appears normally configured and requires escalation.

### 10. Verify Measurement Operation With a Test Object

Use a suitable phantom or test object when applicable.

Perform a simple known measurement and confirm the system accepts caliper placement, displays the result, and completes the expected workflow.

Do not declare quantitative calibration accuracy without using an approved performance test.

**Expected outcome:** Basic measurement functionality operates consistently.

### 11. Perform Final Functional Verification

After correction:

- Select the appropriate exam
- Confirm the intended measurement package is present
- Perform the previously failing measurement
- Verify required calculations complete
- Repeat the workflow
- Confirm no unexpected error or function loss occurs

**Expected outcome:** The measurement package functions consistently. Troubleshooting can stop after applicable performance verification.

## If the Problem Persists

If exam selection, transducer, imaging mode, required inputs, patient workflow, and restart have been ruled out, the remaining issue may involve system configuration, software, application data, licensed functionality, or another service-level fault.

The system should be:

- Removed from service if the affected measurement is required for safe clinical use
- Labeled Out of Service as appropriate
- Sent for repair or bench evaluation
- Evaluated using appropriate Fujifilm SonoSite documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not modify protected calculation definitions, clinical presets, calibration values, or undocumented service settings.

Following corrective service, verify the affected measurement workflow and any applicable measurement-performance requirements before return to clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

When a calculated value appears questionable, verify the measurement workflow and system function before the result is used for a clinical decision.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Measurement errors require careful verification of exam context, inputs, probe, and configuration before internal or software failure is assumed. Questionable calculations should never be accepted without functional verification.

That is successful troubleshooting.
