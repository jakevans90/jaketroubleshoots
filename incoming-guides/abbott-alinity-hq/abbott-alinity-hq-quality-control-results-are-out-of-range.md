---
schemaVersion: 1
title: "Abbott Alinity hq Hematology Analyzer - Quality-Control Results Are Out of Range"
issueTitle: "Quality-Control Results Are Out of Range"
description: "Addresses out-of-range QC caused by control material, preparation, reagents, aspiration, calibration status, environmental conditions, or analytical instability."
assetType: "Hematology Analyzer"
manufacturer: "Abbott"
model: "Alinity hq"
slug: "abbott-alinity-hq-quality-control-results-are-out-of-range"
dateAdded: "2026-10-06"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that Abbott Alinity hq QC results were repeatedly outside the laboratory's acceptable range."
  cause: "Clinical Engineering found the QC material contained visible bubbles and confirmed a properly prepared replacement control produced stable results."
  resolution: "Clinical Engineering removed the compromised control preparation from use, verified repeat QC was acceptable, and documented the analyzer's return to normal laboratory workflow."
helpfulDetails:
  - "QC level affected"
  - "Parameters affected"
  - "Direction or pattern of failure"
  - "QC lot and preparation condition"
  - "Reagent status"
  - "Recent reagent or calibration changes"
  - "Aspiration messages"
  - "Known-good QC comparison"
  - "Environmental changes"
  - "QC results before and after correction"
  - "Final analyzer status"
---
## What This Guide Helps With

Addresses out-of-range QC caused by control material, preparation, reagents, aspiration, calibration status, environmental conditions, or analytical instability.

## Step-by-Step Troubleshooting

### 1. Stop Affected Patient Testing
Do not release patient results for affected tests while quality-control results are unacceptable. Follow laboratory policy for result review, alternate testing, and any required patient-result assessment.

Identify which QC level, parameter, and direction of failure are involved.

**Expected outcome:** Potentially unreliable patient results are contained and the QC problem is clearly defined.

### 2. Confirm the QC Failure Pattern
Determine whether the problem affects one control level, one parameter, multiple parameters, or all QC material.

Review whether the shift occurred suddenly or has been trending.

**Expected outcome:** The scope and pattern of the QC failure are established.

### 3. Verify Control Material
Confirm the correct QC material is being used and that storage, handling, mixing, preparation, and laboratory-defined use conditions are appropriate.

Inspect the material for contamination, leakage, or insufficient volume.

**Expected outcome:** QC material is suitable for testing. If questionable material is replaced and QC becomes acceptable, troubleshooting can stop after required confirmation.

### 4. Verify QC Identification and Assigned Information
Confirm the control is correctly identified by the analyzer and that the laboratory is using the intended QC lot and associated configuration.

Do not alter target data or acceptable ranges merely to make a failed result pass.

**Expected outcome:** The correct QC material and associated laboratory configuration are confirmed.

### 5. Check Reagent and Consumable Status
Review reagent recognition, inventory, recent reagent changes, empty or low consumables, wash status, and waste conditions.

Inspect accessible reagent connections for obvious leakage, looseness, or installation problems.

**Expected outcome:** Reagents and consumables are properly installed and available. If correcting an external reagent issue restores acceptable QC, troubleshooting can stop after confirmation.

### 6. Check Aspiration and Sample Presentation
Verify the QC container is properly loaded and has adequate accessible volume. Look for bubbles, foam, tube damage, or repeated aspiration-related messages.

**Expected outcome:** QC material can be aspirated consistently. If correcting presentation or replacing a compromised sample resolves QC, verify with an additional acceptable run and stop.

### 7. Review Calibration Status
Determine whether a recent calibration, failed calibration, reagent change, prolonged shutdown, or maintenance event preceded the QC shift.

Follow laboratory policy for any required calibration action.

**Expected outcome:** Calibration status is appropriate and no unresolved calibration problem remains.

### 8. Compare With Fresh or Known-Good QC Material
Use another properly prepared control sample when permitted. Compare results to determine whether the failure follows the QC material or remains with the analyzer.

**Expected outcome:** A material-related issue is separated from analyzer-related instability. If fresh QC produces acceptable results consistently, remove the suspect material from use.

### 9. Review Environmental and Operational Conditions
Check for recent relocation, room-condition changes, vibration, power events, fluid spills, prolonged idle time, or other environmental changes.

**Expected outcome:** No external environmental condition remains likely to affect measurement performance.

### 10. Perform Final QC Verification
Repeat the laboratory-required QC process after correcting any identified external cause.

**Expected outcome:** Required QC results are acceptable and stable. The issue is resolved and troubleshooting can stop.

## If the Problem Persists

QC material, configuration, reagents, accessible fluidics, aspiration, calibration status, and environmental factors have been ruled out. The remaining cause may involve an internal analytical system, fluidics, optical or measurement subsystem, sensor, calibration state, or service-level configuration problem.

The analyzer should be:

- Removed from service for affected testing
- Labeled Out of Service
- Sent for repair or bench/service evaluation
- Evaluated using appropriate Abbott documentation and approved test equipment
- Repaired, calibrated, or configured only by qualified personnel

Following repair, required calibration and QC must be successfully completed before patient testing resumes.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

An analyzer that produces out-of-range QC should be treated as analytically unreliable even when it appears mechanically normal.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

QC failure requires protection of result integrity first. Separate control-material, reagent, aspiration, calibration, and environmental causes before escalating to an internal analytical problem, and document the complete verification path.

That is successful troubleshooting.
