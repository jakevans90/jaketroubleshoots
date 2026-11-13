---
schemaVersion: 1
title: "LivaNova S5 Heart-Lung Machine - Cardioplegia Delivery Ratio or Volume Is Inaccurate Although the Module Is Online"
issueTitle: "Cardioplegia Delivery Ratio or Volume Is Inaccurate Although the Module Is Online"
description: "Troubleshoots inaccurate cardioplegia ratio or delivered volume caused by setup, tubing, occlusion, pump, sensor, configuration, or accessory-related conditions."
assetType: "Heart-Lung Machine"
manufacturer: "LivaNova"
model: "S5"
slug: "livanova-s5-cardioplegia-delivery-ratio-or-volume-is-inaccurate-although-the-module-is-online"
dateAdded: "2026-10-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Perfusion reported that the S5 cardioplegia module remained online but the delivered mixture volume did not agree with the programmed ratio and expected output."
  cause: "Clinical Engineering found the cardioplegia tubing incorrectly seated in one pump channel, producing inconsistent delivery during controlled testing."
  resolution: "The tubing was reinstalled correctly and controlled delivery testing confirmed consistent ratio and volume performance before the system was returned to service."
helpfulDetails:
  - "Programmed cardioplegia ratio"
  - "Programmed and measured volume"
  - "Which pump channels were involved"
  - "Disposable or tubing set used"
  - "Tubing installation condition"
  - "Pump direction observed"
  - "Channel assignments"
  - "Any restrictions, clamps, or kinks found"
  - "Known-good substitutions performed"
  - "Independent measurement method used"
  - "Results before and after correction"
  - "Final functional verification results"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots inaccurate cardioplegia ratio or delivered volume caused by setup, tubing, occlusion, pump, sensor, configuration, or accessory-related conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Cardioplegia Capability

Do not troubleshoot an unreliable cardioplegia delivery function while a patient depends on it. Ensure the perfusion team has an alternate verified method for cardioplegia delivery before Clinical Engineering begins troubleshooting.

If the inaccurate ratio or volume was observed during a case, preserve the reported settings and observations when possible without delaying patient care.

**Expected outcome:** Patient care is transferred to a safe, verified cardioplegia delivery method and the affected system is available for controlled evaluation.

### 2. Confirm the Exact Reported Condition

Obtain the reported programmed ratio, intended volume, displayed delivered volume, and any independent measurement used to determine that delivery was inaccurate.

Determine whether the problem affects:

- Ratio calculation
- Total delivered volume
- One solution channel only
- Both cardioplegia components
- Displayed information versus actual measured delivery
- A specific disposable setup or repeated setups

Do not assume the module itself is defective solely because the displayed and expected values differ.

**Expected outcome:** The discrepancy is clearly defined and reproducible enough to guide testing.

### 3. Inspect the Cardioplegia Circuit and Disposable Setup

With the system out of clinical use, inspect the external cardioplegia tubing and associated disposables for:

- Incorrect tubing installation
- Reversed or crossed tubing paths
- Kinks or compression
- Loose connections
- Air in the fluid path
- Improperly seated tubing in the pump mechanism
- Damaged or stretched tubing
- Clamps or stopcocks restricting flow
- Incorrect disposable selection for the intended setup

Correct any obvious external setup problem and repeat the controlled test.

**Expected outcome:** Tubing and disposables are correctly installed, unrestricted, and appropriate for the configured delivery system. If delivery becomes accurate, troubleshooting can stop after final verification.

### 4. Verify Pump Direction and Channel Assignment

Confirm that each pump involved in cardioplegia delivery is operating in the intended direction and corresponds to the correct solution path.

Verify that the physical tubing paths match the displayed or configured pump assignments. A correct electronic ratio cannot produce the intended mixture if the tubing is connected to the wrong pump or solution source.

**Expected outcome:** Each pump moves the intended solution in the correct direction and channel assignments match the physical circuit.

### 5. Check External Pump Loading and Mechanical Engagement

Inspect the pump head and externally accessible loading area for:

- Tubing not fully seated
- Inconsistent tubing compression
- Foreign material
- Visible wear or damage
- Pump-head obstruction
- Improperly secured pump components

Do not disassemble the pump mechanism beyond normal approved access.

**Expected outcome:** The pump mechanism operates smoothly with the tubing correctly loaded and no visible external cause of inaccurate delivery.

### 6. Verify Cardioplegia Controls and Configuration

Review the cardioplegia-related settings available through normal authorized operation. Confirm that the intended ratio, delivery mode, pump selections, and applicable configuration match the clinical setup being tested.

Check for unintended changes made between cases or after servicing.

Do not enter restricted service menus or alter protected calibration values without approved service documentation.

**Expected outcome:** The displayed settings and normal configuration agree with the intended cardioplegia delivery setup.

### 7. Perform a Controlled Volume Comparison

Using an approved bench setup and appropriate measurement equipment, run a controlled delivery test without a patient connected.

Compare the commanded delivery with the independently measured output. If separate pumps contribute to the mixture, evaluate their outputs individually when this can be done using approved procedures.

Use fresh, correctly installed tubing if the disposable circuit is suspect.

**Expected outcome:** Independently measured delivery agrees with the commanded ratio and volume. If it does, the system may proceed to final verification.

### 8. Substitute Known-Good External Components

If the discrepancy remains, substitute known-good compatible external components where practical, such as:

- Tubing set
- Fluid container or source
- External accessory associated with the cardioplegia setup
- Another verified pump position or compatible module arrangement, if permitted by approved procedures

Change one variable at a time so the cause remains identifiable.

**Expected outcome:** A faulty disposable or external component is identified, or the problem remains associated with the equipment.

### 9. Perform Final Functional Verification

After correcting the cause, repeat a controlled cardioplegia delivery test across the functions involved in the complaint.

Verify:

- Pump operation
- Correct flow direction
- Ratio selection
- Delivered volume indication
- Independent measured output
- Relevant alarms and indicators
- No leaks, restrictions, or abnormal mechanical behavior

Document the test equipment and results according to facility practice.

**Expected outcome:** Cardioplegia delivery operates consistently and agrees with the intended setup. If verification passes, troubleshooting is complete.

### 10. Stop and Escalate if Accuracy Cannot Be Verified

If delivery remains inaccurate, inconsistent, or cannot be independently verified, do not return the cardioplegia function to clinical service.

**Expected outcome:** The affected equipment is removed from service rather than being used with uncertain cardioplegia delivery accuracy.

## If the Problem Persists

Common external causes such as tubing installation, disposable condition, pump loading, channel assignment, controls, and normal configuration have been ruled out.

Possible remaining categories include pump-drive performance, sensing, calibration, control electronics, communication between system components, or other service-level conditions.

The affected equipment should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or controlled bench evaluation
- Evaluated using appropriate LivaNova service documentation and approved test equipment
- Repaired, calibrated, or configured only by qualified personnel
- Subjected to complete functional and applicable performance verification before return to service

Knowing when to stop external troubleshooting and escalate an unresolved delivery-accuracy problem is proper troubleshooting.

## Clinical Use Tip

Never rely on a cardioplegia volume or ratio indication that has not been verified when the perfusion team reports a delivery discrepancy.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- rendered from front matter -->

## Final Thought

Patient safety depends on treating inaccurate cardioplegia delivery as a potentially serious performance problem. Verify the complete external setup and independently confirm output before assuming an internal failure. Escalate unresolved accuracy problems and document the complaint, cause, corrective action, and verification clearly.

That is successful troubleshooting.
