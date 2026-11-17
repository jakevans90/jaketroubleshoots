---
schemaVersion: 1
title: "Advanced Sterilization Products (ASP) AEROFLEX Endoscope Reprocessor (AER) - AEROFLEX Touchscreen or Operator Control Freezes During Cycle Setup"
issueTitle: "AEROFLEX Touchscreen or Operator Control Freezes During Cycle Setup"
description: "Touchscreen or control freezes caused by startup state, contamination, external peripherals, temporary software faults, power problems, or service-level control failures."
assetType: "Endoscope Reprocessor (AER)"
manufacturer: "Advanced Sterilization Products (ASP)"
model: "AEROFLEX"
slug: "advanced-sterilization-products-asp-aeroflex-aeroflex-touchscreen-or-operator-control-freezes-during-cycle-setup"
dateAdded: "2026-11-17"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported the AEROFLEX touchscreen repeatedly froze while entering scope information before cycle start."
  cause: "Clinical Engineering found a connected barcode scanner intermittently locking the setup interface when scanned."
  resolution: "Removed the faulty scanner from service, connected an approved known-good scanner, and verified repeated cycle setup with normal touchscreen response."
helpfulDetails:
  - "Whole-screen or partial-screen freeze"
  - "Specific setup step"
  - "Touch versus physical control behavior"
  - "Screen cleanliness"
  - "Peripheral devices connected"
  - "AC power condition"
  - "Restart result"
  - "Reproducibility"
  - "Final operational test"
  - "Final device status"
---

## What This Guide Helps With

Touchscreen or control freezes caused by startup state, contamination, external peripherals, temporary software faults, power problems, or service-level control failures.

## Step-by-Step Troubleshooting

### 1. Protect Processing Continuity
Do not begin a reprocessing cycle on a unit whose controls cannot reliably display or accept required setup information. Use another validated AER when necessary.

Expected outcome: Staff are not forced to operate an unreliable control interface during scope reprocessing.

### 2. Confirm the Exact Control Failure
Determine whether the entire display freezes, touch input stops responding, only one area is affected, the interface becomes slow, or an attached scanner or peripheral appears to trigger the problem.

Expected outcome: The problem is clearly characterized and can be reproduced if possible.

### 3. Inspect and Clean the Touch Surface
Check for moisture, cleaning residue, gloves or objects resting on the display, damaged screen covers, or contamination that could cause false touches.

Expected outcome: The touchscreen is clean, dry, and unobstructed. If normal control returns and remains stable, troubleshooting can stop after verification.

### 4. Check External Peripherals
Disconnect only approved nonessential external accessories such as a barcode scanner or printer connection when appropriate and observe whether the control interface responds normally.

Expected outcome: A faulty peripheral is identified if the freeze disappears when it is removed. Replace or troubleshoot that peripheral separately.

### 5. Verify Stable AC Power
Inspect the power cord and plug for visible damage and confirm the unit is connected to an appropriate functioning outlet. Do not continue using the AER with an intermittent power connection.

Expected outcome: The system receives stable external power.

### 6. Perform a Normal Controlled Restart
When no cycle is active and no scope depends on the unit, use the normal shutdown and restart process available to trained personnel. Do not remove power during active processing unless required for immediate safety.

Expected outcome: The AER completes startup normally and the controls respond consistently. If the freeze was transient and does not recur through verification, troubleshooting can stop.

### 7. Check Whether the Freeze Occurs at a Specific Setup Step
Repeat an approved setup workflow and note whether the control freezes during barcode entry, chemistry confirmation, scope selection, operator entry, or another consistent action.

Expected outcome: A reproducible trigger is identified for service documentation.

### 8. Verify Normal Operation After Correction
Confirm the touchscreen, operator inputs, barcode entry if used, and cycle setup remain responsive through an approved test.

Expected outcome: Controls remain stable without unexpected freezes or delayed responses.

### 9. Escalate Recurrent Control Freezes
If the control repeatedly becomes unresponsive despite clean controls, stable power, and normal external peripherals, stop troubleshooting.

Expected outcome: The AEROFLEX is removed from service for qualified software or control-system evaluation.

## If the Problem Persists

External causes involving screen contamination, peripherals, and power have been ruled out. Remaining causes may involve the touchscreen assembly, control electronics, software, memory, communication, or configuration.

Remove the AEROFLEX from service, label it Out of Service, and send it for repair or bench evaluation. Evaluate it using appropriate ASP documentation and approved test equipment. Do not enter unauthorized service menus or alter configuration in an attempt to clear the problem.

Return the device to service only after the operator interface remains reliable through required setup and functional testing.

## Clinical Use Tip

An AER with unreliable controls should not be used merely because a cycle can sometimes be started; setup errors can compromise processing traceability and configuration.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Control freezes should be isolated from simple screen, peripheral, and power issues before internal electronics are suspected. Recurrent interface instability warrants removal from service and qualified evaluation.

That is successful troubleshooting.
