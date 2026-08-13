---
schemaVersion: 1
title: "GE Healthcare Carestation 750 Anesthesia Machine - Electronic Flow Control Malfunction"
issueTitle: "Electronic Flow Control Malfunction"
description: "Fresh-gas flow does not respond correctly because of supply problems, settings, controls, configuration, or a service-level electronic flow-control fault."
assetType: "Anesthesia Machine"
manufacturer: "GE Healthcare"
model: "Carestation 750"
slug: "ge-healthcare-carestation-750-electronic-flow-control-malfunction"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Anesthesia staff reported that fresh-gas flow on the Carestation 750 would not increase when the selected flow setting was raised."
  cause: "Clinical Engineering found the external air pipeline hose was not fully connected."
  resolution: "The pipeline connection was secured, fresh-gas response was verified with approved test equipment, and the machine completed system checkout successfully."
helpfulDetails:
  - "Gas or gases affected"
  - "Selected flow values"
  - "Displayed flow behavior"
  - "Pipeline connection status"
  - "Backup gas status"
  - "Control-input behavior"
  - "Associated warnings"
  - "Independent flow-test results"
  - "Oxygen analyzer results"
  - "Checkout status"
  - "Final device disposition"
---

## What This Guide Helps With
Fresh-gas flow does not respond correctly because of supply problems, settings, controls, configuration, or a service-level electronic flow-control fault.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Gas Delivery
Do not troubleshoot unreliable fresh-gas control while a patient depends on the Carestation 750.

If gas delivery becomes unreliable during a case, maintain ventilation and anesthesia using appropriate verified alternatives and follow clinical escalation procedures.

**Expected outcome:** Patient care is maintained without relying on questionable electronic flow control.

### 2. Confirm the Exact Flow-Control Problem
Determine whether the reported problem involves:

- No flow
- Flow that does not change with the selected setting
- One gas unavailable
- Unstable flow
- Incorrect displayed gas mixture
- Flow-control input not responding

Record relevant displayed values and messages.

**Expected outcome:** The malfunction is clearly characterized and reproducible during controlled testing.

### 3. Verify External Gas Supplies
Confirm each required pipeline hose is properly connected and inspect for damage, severe kinking, or incorrect attachment.

If applicable, verify available backup gas sources.

**Expected outcome:** Required gas sources are externally available. If reconnecting or restoring a supply corrects flow control, troubleshooting can stop after final checkout.

### 4. Verify Flow and Gas-Mixture Settings
Review user-accessible fresh-gas settings and confirm the selected gases, total flow, and concentration are appropriate for the test.

Make only normal operational adjustments.

**Expected outcome:** The settings are valid and the displayed flow responds appropriately. If an incorrect selection caused the reported condition, correct it and verify operation.

### 5. Check Control Inputs
Verify the touchscreen or other operator controls used to change fresh-gas settings respond reliably.

Look for delayed response, unintended selections, or an unresponsive control.

**Expected outcome:** Inputs are accepted normally and the commanded values update as expected. If the control interface itself is unreliable, remove the machine from service.

### 6. Observe Gas-Flow Response
Using an appropriate controlled test configuration, change fresh-gas settings within normal operating ranges and observe whether displayed and independently measured flow changes correspond appropriately.

Do not attempt internal adjustment.

**Expected outcome:** Gas flow responds consistently to user commands. If normal response is restored after correcting an external supply or setting, troubleshooting can stop after verification.

### 7. Check for Concurrent Gas-Supply or System Errors
Review visible system status for any gas-supply, calibration, communication, or checkout problem that could explain flow-control behavior.

Address external gas or setup issues first.

**Expected outcome:** No unresolved external warning remains that could explain the malfunction.

### 8. Perform Required Checkout
Run the appropriate system checkout after any correction.

Verify gas delivery, oxygen concentration, ventilation, alarms, and fresh-gas response using approved test equipment.

**Expected outcome:** Electronic flow control responds predictably and checkout passes. Troubleshooting can stop.

### 9. Escalate Persistent Flow-Control Malfunction
If commanded gas flow remains absent, unstable, or inconsistent after external gas supplies, settings, and control inputs have been verified, stop troubleshooting.

**Expected outcome:** The Carestation 750 is removed from service for qualified technical evaluation.

## If the Problem Persists
Common external causes have been ruled out. Remaining categories may include internal electronic flow-control hardware, pneumatic regulation, valves, sensors, command interfaces, or configuration requiring service-level evaluation.

The Carestation 750 should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved gas-analysis and flow-test equipment
- Repaired or configured only by qualified personnel

After repair, verify the complete fresh-gas delivery range appropriate to manufacturer procedures, oxygen concentration, ventilation, alarms, and system checkout.

Stopping when fresh-gas delivery cannot be trusted is proper troubleshooting.

## Clinical Use Tip
Unexpected fresh-gas flow should be treated as a gas-delivery reliability issue, not merely a display problem, until verified with independent test equipment.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Electronic flow-control complaints should first be separated from gas-supply, setting, and input problems. Verify the external gas path and commanded response before assuming an internal failure, and do not return the machine to service until gas delivery is independently confirmed.

That is successful troubleshooting.
