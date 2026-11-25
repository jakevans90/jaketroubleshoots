---
schemaVersion: 1
title: "Sysmex XN-2000 Hematology Analyzer - Rerun/Reflex Rule Executes but the Sample Does Not Route Correctly"
issueTitle: "Rerun/Reflex Rule Executes but the Sample Does Not Route Correctly"
description: "A rerun or reflex condition is generated, but the rack or sample does not follow the expected automated routing workflow."
assetType: "Hematology Analyzer"
manufacturer: "Sysmex"
model: "XN-2000"
slug: "sysmex-xn-2000-rerun-reflex-rule-executes-but-the-sample-does-not-route-correctly"
dateAdded: "2026-11-25"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that rerun rules were being generated on the Sysmex XN-2000, but affected samples were not routing to the expected analyzer module."
  cause: "Clinical Engineering found the intended analyzer module was not in a ready state and could not accept rerouted samples."
  resolution: "The external readiness condition was corrected, and a test sample successfully completed the expected rerun routing sequence."
helpfulDetails:
  - "Sample ID"
  - "Rack position"
  - "Rule or reflex condition observed"
  - "Intended destination"
  - "Actual destination"
  - "Analyzer module readiness"
  - "Rack transport condition"
  - "Middleware or communication status"
  - "Known-good test result"
  - "Final routing verification"
---

## What This Guide Helps With

A rerun or reflex condition is generated, but the rack or sample does not follow the expected automated routing workflow.

## Step-by-Step Troubleshooting

### 1. Protect Sample Identity and Result Integrity
Do not manually move or reassign patient specimens in a way that could separate the tube from its correct sample identification or requested test pathway.

Use the laboratory's approved backup workflow for any specimen requiring immediate rerun or reflex testing.

Expected outcome: Patient specimens remain correctly identified and required testing continues safely.

### 2. Confirm the Rule Actually Triggered
Review the analyzer or middleware display and confirm that the rerun or reflex condition was generated for the expected specimen.

Distinguish between a rule that failed to trigger and a rule that triggered but did not result in physical routing.

Expected outcome: The problem is confirmed as a routing issue rather than a rule-execution issue.

### 3. Verify Sample and Rack Identification
Confirm the barcode was read correctly and that the displayed sample ID matches the physical tube and rack position.

An identification mismatch can make a routing problem appear to be a rule problem.

Expected outcome: The sample identity, rack position, and displayed record match.

If correcting a barcode or rack identification issue restores proper routing, verify another sample and stop.

### 4. Inspect the Rack Transport Path
Check accessible transport areas for obstructions, mispositioned racks, damaged racks, or debris that could prevent the sample from being redirected.

Expected outcome: The rack path is clear and transport hardware can move the rack normally.

If clearing an accessible obstruction restores rerun routing, verify operation and stop.

### 5. Confirm Destination Availability
Verify the analyzer module or measurement pathway required by the rerun or reflex action is online, ready, and not blocked by another visible fault.

Do not alter protected routing configuration to bypass an unresolved module condition.

Expected outcome: The intended destination is available to receive the sample.

If restoring the destination to normal readiness resolves routing, verify and stop.

### 6. Check for Queue or Workflow Holds
Review the system for visible rack holds, pending operator actions, unresolved sample exceptions, or other conditions preventing automatic continuation.

Expected outcome: No unresolved workflow condition is holding the sample.

If resolving an appropriate operator-level hold allows the sample to route normally, verify the complete rerun path and stop.

### 7. Compare With a Known-Good Test Scenario
Using approved nonpatient material and an established workflow where permitted, determine whether rerun routing works for another sample or rack.

Do not intentionally create unsupported patient-testing conditions.

Expected outcome: The system successfully routes a known-good rerun scenario.

If only one rack or barcode is affected, address that external cause and stop after verification.

### 8. Verify External Communication Dependencies
If routing depends on middleware or another external system, verify external communication status, network connections, and whether the instruction is reaching the XN-2000.

Avoid unauthorized changes to rules or middleware configuration.

Expected outcome: Required routing instructions are communicated successfully.

If restoring an external communication connection restores routing, verify the full path and stop.

### 9. Perform Final Functional Verification
Confirm a test sample can trigger the appropriate approved rerun/reflex workflow and physically reach the intended destination without manual intervention beyond the normal workflow.

Expected outcome: Rule execution and physical sample routing agree.

If successful, return the system to routine use.

### 10. Escalate Persistent Routing Mismatch
If rules execute correctly but samples repeatedly route incorrectly after identification, transport, destination readiness, and communication causes are ruled out, stop external troubleshooting.

Expected outcome: A persistent automation or configuration fault is prevented from affecting patient workflow.

## If the Problem Persists

Remaining causes may include middleware configuration, routing logic, internal sampler control, system integration, or other service-level configuration problems.

The device should be:

- Removed from automated use when sample identity or routing reliability cannot be assured
- Labeled Out of Service as appropriate
- Sent for repair or technical evaluation
- Evaluated using appropriate Sysmex and middleware documentation
- Configured or repaired only by qualified personnel

Return-to-service testing should verify both rule execution and the complete physical routing path.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Whenever automated rerun routing is unreliable, preserve tube identity and use an approved manual backup workflow rather than improvising rack movement.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Automated routing problems require verification of identity, transport, destination readiness, and communication before configuration is blamed. Protect specimen traceability, test the full workflow, and escalate persistent routing mismatches.

That is successful troubleshooting.
