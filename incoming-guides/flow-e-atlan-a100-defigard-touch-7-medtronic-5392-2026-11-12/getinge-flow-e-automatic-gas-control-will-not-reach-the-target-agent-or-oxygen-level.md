---
schemaVersion: 1
title: "Getinge Flow-e Anesthesia Machine - Automatic Gas Control Will Not Reach the Target Agent or Oxygen Level"
issueTitle: "Automatic Gas Control Will Not Reach the Target Agent or Oxygen Level"
description: "Automatic gas control does not achieve the selected oxygen or anesthetic-agent target because of supply, sampling, circuit, module, configuration, or delivery problems."
assetType: "Anesthesia Machine"
manufacturer: "Getinge"
model: "Flow-e"
slug: "getinge-flow-e-automatic-gas-control-will-not-reach-the-target-agent-or-oxygen-level"
dateAdded: "2026-11-12"
taxonomyMode: "reuse"
ccr:
  complaint: "Anesthesia staff reported that the Flow-e automatic gas control would not reach the selected oxygen and anesthetic-agent targets during checkout."
  cause: "Clinical Engineering found the gas-analyzer sampling line partially obstructed, causing unstable feedback to the automatic gas-control system."
  resolution: "Replaced the affected sampling component, repeated checkout and gas-control verification, and confirmed stable oxygen and agent control before returning the machine to service."
helpfulDetails:
  - "Whether oxygen, agent, or both failed to reach target"
  - "Selected automatic gas-control mode"
  - "Gas supplies connected"
  - "Breathing-system and cassette condition"
  - "Agent module installed and recognized"
  - "Sampling line and water-trap condition"
  - "Known-good substitutions performed"
  - "Independent gas-analyzer comparison"
  - "Checkout results"
  - "Final device status"
---

## What This Guide Helps With

Automatic gas control does not achieve the selected oxygen or anesthetic-agent target because of supply, sampling, circuit, module, configuration, or delivery problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Anesthesia Delivery
Do not troubleshoot unreliable gas delivery while a patient depends on the Flow-e. Transfer ventilation and anesthetic delivery to a verified alternative method or anesthesia machine as directed by the clinical team before technical troubleshooting.

Confirm whether the complaint involved failure to reach the oxygen target, agent target, or both.

**Expected outcome:** Patient care is maintained independently, and the exact automatic gas-control complaint is identified. If operation is normal on subsequent controlled testing, troubleshooting may stop after final verification.

### 2. Verify Gas Supplies and Basic Machine Status
Confirm required pipeline hoses or approved gas sources are securely connected and that the machine does not indicate a gas-supply problem. Inspect hoses and connectors for obvious damage, kinks, loose fittings, or incorrect connections.

Verify the machine completes normal startup sufficiently to permit checkout testing.

**Expected outcome:** Required gas supplies are available, connections are secure, and no obvious external supply problem prevents gas delivery. Correct an external supply issue and retest; if targets are then achieved, troubleshooting can stop after verification.

### 3. Confirm the Reported Targets and Control Mode
Verify the selected oxygen concentration, anesthetic-agent target, fresh-gas settings, and automatic gas-control mode associated with the complaint. Confirm the issue was not caused by an unintended setting or a change between manual and automatic control modes.

Do not alter restricted clinical defaults or unauthorized configuration settings.

**Expected outcome:** Requested targets and operating mode are appropriate for the test condition. If correcting an unintended setting restores normal operation, troubleshooting can stop after functional verification.

### 4. Inspect the Breathing System and Patient Cassette
Inspect the installed patient cassette, breathing hoses, reservoir components, filters, connectors, and accessible seals for improper seating, disconnection, obstruction, or visible damage.

A significant leak or incorrect cassette installation can prevent the machine from maintaining the gas composition expected by the control system.

**Expected outcome:** The breathing system is correctly assembled, unobstructed, and leak-free during approved checkout testing. If reseating or replacing an external component restores target control, troubleshooting can stop after checkout passes.

### 5. Inspect the Vaporizer or Agent-Delivery Module
Confirm the intended anesthetic-agent module is installed correctly, recognized by the machine, contains the appropriate agent, and shows no obvious external damage or improper seating.

If an approved known-good compatible module is available, substitute it according to facility practice.

**Expected outcome:** The correct agent-delivery module is recognized and available for delivery. If a known-good module restores automatic agent control, remove the suspect module from service and troubleshooting may stop after verification.

### 6. Check the Gas Analyzer Sampling Path
Inspect the sampling line, water trap, connectors, and accessible sample-gas pathway for kinks, liquid contamination, blockage, disconnection, or improper installation.

Automatic gas regulation depends on reliable measured gas values. A compromised sampling path can cause the control system to respond to inaccurate or unavailable feedback.

**Expected outcome:** The analyzer has an intact, dry, unobstructed sampling path and produces stable gas measurements. If correcting the sampling path restores target control, troubleshooting can stop after verification.

### 7. Compare Measured and Delivered Gas During Controlled Testing
With an appropriate anesthesia test setup and approved gas-analysis equipment, observe whether oxygen and agent measurements respond logically when delivery settings are changed.

Do not use a patient as the test load.

**Expected outcome:** Measured oxygen and agent values respond consistently to controlled changes and move toward the selected targets. If they do, repeat checkout and document the corrected external cause.

### 8. Evaluate Whether the Problem Is Delivery or Measurement Related
If displayed gas values appear inconsistent, compare the Flow-e measurements with an appropriate independent analyzer when available.

A machine that is delivering correctly but measuring incorrectly requires removal from service just as a machine that cannot control delivery does.

**Expected outcome:** Internal displayed values agree reasonably with independent verification according to applicable service procedures. Any unresolved discrepancy requires escalation.

### 9. Perform Final Functional Verification
Run the appropriate manufacturer-approved checkout and functional tests after any correction. Verify automatic gas control reaches and maintains appropriate commanded conditions within the applicable manufacturer verification criteria.

Also verify ventilation, alarms, gas monitoring, and normal transition between relevant operating states.

**Expected outcome:** Checkout passes and automatic gas control operates normally. The device may be returned to service only after all applicable functional verification is satisfactory.

### 10. Stop and Escalate if Automatic Control Remains Unreliable
If oxygen or agent targets cannot be reliably achieved after external supplies, settings, breathing components, agent module, and sampling components have been checked, stop external troubleshooting.

**Expected outcome:** The device remains removed from clinical use until qualified service personnel complete further evaluation.

## If the Problem Persists

Common external gas-supply, breathing-system, sampling, module-installation, and setting causes have been ruled out. Remaining possibilities include internal gas-control components, internal sensors, analyzer faults, calibration problems, software/configuration problems, or other service-level conditions.

The Flow-e should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate Getinge service documentation and approved anesthesia test equipment.
- Repaired, calibrated, or configured only by qualified personnel.

Do not perform internal board-level repair or unauthorized service-menu adjustments. Knowing when automatic gas delivery can no longer be safely verified is proper troubleshooting.

Return the machine to service only after required checkout, gas-delivery verification, monitoring verification, alarm testing, and applicable electrical-safety testing are completed successfully.

## Clinical Use Tip

If gas delivery is questionable, move anesthesia care to a verified alternative system before troubleshooting the Flow-e.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient first, verify external gas supplies and the complete delivery and sampling paths before assuming an internal failure, escalate when automatic control cannot be confidently verified, and document the complaint, cause, correction, and final testing clearly.

That is successful troubleshooting.
