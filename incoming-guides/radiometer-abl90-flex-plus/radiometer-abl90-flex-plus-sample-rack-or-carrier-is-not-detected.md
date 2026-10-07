---
schemaVersion: 1
title: "Radiometer ABL90 FLEX PLUS Blood Gas Analyzer - Sample, Rack, or Carrier Is Not Detected"
issueTitle: "Sample, Rack, or Carrier Is Not Detected"
description: "Troubleshoot failure to recognize a presented sample caused by sample positioning, container condition, contamination, obstruction, or analyzer readiness."
assetType: "Blood Gas Analyzer"
manufacturer: "Radiometer"
model: "ABL90 FLEX PLUS"
slug: "radiometer-abl90-flex-plus-sample-rack-or-carrier-is-not-detected"
dateAdded: "2026-10-07"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that the Radiometer ABL90 FLEX PLUS would not detect a presented patient sample."
  cause: "Clinical Engineering found dried residue at the accessible sample presentation area that interfered with normal sample positioning."
  resolution: "Clinical Engineering cleaned the accessible area using the approved procedure, verified consistent sample detection with an appropriate control, and returned the analyzer to service."
helpfulDetails:
  - "Exact behavior when the sample was presented"
  - "Sample container type"
  - "Whether the issue occurred with one or multiple samples"
  - "Presence of clotting, bubbles, leakage, or container damage"
  - "Condition of the accessible sample inlet"
  - "Known-good sample or control comparison"
  - "Analyzer ready-state indication"
  - "Any concurrent analyzer message"
  - "Cleaning or reseating performed"
  - "Final quality verification"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoot failure to recognize a presented sample caused by sample positioning, container condition, contamination, obstruction, or analyzer readiness.

## Step-by-Step Troubleshooting

### 1. Protect Patient Testing and Confirm the Failure

Do not repeatedly attempt patient testing on an analyzer that cannot reliably detect or accept samples. Route urgent testing to another verified analyzer when necessary.

Confirm what staff mean by “not detected.” Determine whether the analyzer does not recognize sample presentation, will not begin aspiration, rejects the sample, or behaves inconsistently with different samples.

**Expected outcome:** The exact detection failure is defined and patient testing is not delayed by repeated unsuccessful attempts.

### 2. Verify Analyzer Readiness

Confirm the analyzer has completed initialization, is in its normal ready state, and is not displaying another fault that would prevent sample processing.

A detection problem may be secondary to a fluidics, consumable, calibration, or system-readiness condition.

**Expected outcome:** The analyzer is otherwise ready to accept a sample. If correcting a readiness condition restores sample detection, verify normal operation and troubleshooting can stop.

### 3. Inspect the Sample Container

Inspect the syringe, capillary, or other approved sample container for damage, incorrect assembly, leakage, excessive air, contamination, clotting, or an unsuitable presentation condition.

Do not manipulate a potentially biohazardous sample beyond approved handling practices.

**Expected outcome:** The sample container is appropriate, intact, and suitable for testing. If replacing a defective sample container resolves detection, troubleshooting can stop after verification.

### 4. Verify Sample Positioning and Presentation

Confirm the sample is being presented correctly to the analyzer's accessible sample interface and is aligned without excessive force.

Inspect the accessible sample inlet area for dried blood, debris, obstruction, or visible damage. Clean only using approved external cleaning procedures.

**Expected outcome:** The sample is properly positioned and the accessible inlet area is clean and unobstructed. If detection returns, verify with an appropriate sample or control and troubleshooting can stop.

### 5. Compare With a Known-Good Sample Container

When clinically appropriate, test the analyzer using an approved known-good sample container or control material prepared according to facility practice.

This helps distinguish a sample-container problem from an analyzer detection problem.

**Expected outcome:** A known-good presentation is detected normally. If so, the original sample or container was the likely cause and analyzer troubleshooting can stop.

### 6. Check for Repeated Behavior Across Samples

Determine whether the failure occurs with one sample, one container type, or all properly prepared samples.

A problem limited to one sample points toward sample preparation or container condition. A problem affecting all samples increases concern for the analyzer's sampling interface or internal detection system.

**Expected outcome:** The scope of the failure is defined. Consistent failure across known-good samples warrants escalation.

### 7. Inspect Accessible Covers and Consumables

Verify that any user-accessible cover, consumable, or sampling-related component required for normal operation is fully seated and not damaged.

Do not disassemble the sampling mechanism or access internal sensors.

**Expected outcome:** All accessible components are correctly positioned. If correcting an external seating issue restores detection, perform final verification and troubleshooting can stop.

### 8. Perform Final Functional Verification

Verify the analyzer accepts and processes an appropriate control or approved test sample without repeated detection or aspiration problems. Complete required quality checks before clinical use.

**Expected outcome:** Sample presentation is detected consistently and processing begins normally. The analyzer may be returned to service.

## If the Problem Persists

External sample-container, positioning, contamination, consumable, and readiness causes have been ruled out. Persistent failure may involve the sample-detection mechanism, aspiration interface, sensor system, fluidics assembly, or service-level configuration.

The analyzer should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate Radiometer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Do not disassemble the sample inlet or attempt internal sensor adjustment without authorized procedures. Complete required functional and quality verification before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Avoid repeated aspiration attempts on a compromised patient sample; obtain or route an appropriate specimen according to laboratory policy when sample integrity is questionable.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Verify analyzer readiness, sample integrity, positioning, and the accessible sampling interface before assuming a detection-system failure. Use known-good comparisons, stop when the fault becomes internal, and document the complete result.

That is successful troubleshooting.
