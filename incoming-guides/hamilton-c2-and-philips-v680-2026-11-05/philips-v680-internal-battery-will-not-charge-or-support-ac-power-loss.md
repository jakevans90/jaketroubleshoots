---
schemaVersion: 1
title: "Philips V680 Ventilator - Internal Battery Will Not Charge or Support AC Power Loss"
issueTitle: "Internal Battery Will Not Charge or Support AC Power Loss"
description: "Troubleshoots battery charging or backup-power failure caused by AC supply, connection, battery condition, charging state, or service-level power faults."
assetType: "Ventilator"
manufacturer: "Philips"
model: "V680"
slug: "philips-v680-internal-battery-will-not-charge-or-support-ac-power-loss"
dateAdded: "2026-11-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported the Philips V680 shut down when AC power was disconnected despite showing a battery installed."
  cause: "Clinical Engineering found the installed battery was not supporting operation, while a known-good approved battery completed the AC-loss test successfully."
  resolution: "The defective battery was replaced and the ventilator passed charging, power-transition, and functional verification."
helpfulDetails:
  - "Battery detected or not detected"
  - "Charge indicator behavior"
  - "AC outlet verified"
  - "Power-cord condition"
  - "Battery physical condition"
  - "Battery status before testing"
  - "AC-loss transition result"
  - "Known-good battery result"
  - "Any shutdown or reboot"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots battery charging or backup-power failure caused by AC supply, connection, battery condition, charging state, or service-level power faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Before Testing Battery Backup
Do not intentionally remove AC power from a ventilator supporting a patient to test battery operation. Transfer the patient to another verified ventilator before power-source testing.

**Expected outcome:** The patient is protected and the V680 can be tested without clinical risk.

### 2. Confirm the Battery Complaint
Determine whether the battery does not charge, is not detected, reports low capacity, fails immediately during AC loss, or provides unusually short backup operation.

Record whether the problem occurred after storage, transport, battery replacement, or prolonged disconnection from AC.

**Expected outcome:** The specific charging or backup-power symptom is documented.

### 3. Verify External AC Power
Inspect the power cord and equipment inlet and connect the ventilator to a verified hospital-grade outlet.

Confirm that the ventilator recognizes AC power normally.

**Expected outcome:** Stable AC power is available to the ventilator. If the original outlet or cord caused the charging problem, correct it and reassess battery operation.

### 4. Allow Normal Charging Under Approved Conditions
Leave the ventilator connected to verified AC power for the appropriate approved charging period before judging battery performance. Do not invent or assume a charge duration.

Observe the device's normal battery and charging indicators.

**Expected outcome:** The ventilator indicates that the battery is recognized and charging. If charging behavior returns to normal, continue with controlled verification.

### 5. Inspect Accessible Battery-Related Areas
Inspect externally accessible battery compartments, covers, connectors, and retaining hardware for damage, looseness, contamination, swelling, or evidence of overheating.

Do not open or repair a battery pack.

**Expected outcome:** The battery and accessible mounting area show no physical abnormality. Swollen, leaking, overheated, or damaged batteries require immediate removal from service according to facility battery-safety procedures.

### 6. Verify Battery Identification and Status
Confirm that the installed battery is the correct approved type and is recognized by the ventilator. Review available normal battery status information without entering restricted service functions.

**Expected outcome:** The ventilator recognizes the installed battery and reports a plausible charging state.

### 7. Perform a Controlled AC-Loss Test
With no patient attached and using approved test conditions, remove AC input and observe whether the ventilator transitions to battery operation without rebooting or stopping ventilation.

Restore AC and confirm the device returns to external power and charging.

**Expected outcome:** Ventilation continues through the power transition and the battery supports operation. If it does, complete any required battery-performance verification.

### 8. Substitute a Known-Good Approved Battery When Appropriate
If the battery is removable by qualified Clinical Engineering personnel and substitution is permitted, install a known-good approved battery to distinguish a battery problem from a charging-system problem.

**Expected outcome:** Normal charging and backup operation with a known-good battery identifies the original battery as defective. Replace it according to approved procedures and complete final verification.

### 9. Escalate Charging-System or Transition Failure
If a known-good battery is not recognized, will not charge, or cannot support an AC interruption, stop external troubleshooting.

**Expected outcome:** The ventilator is removed from service for qualified evaluation of the internal charging or power-management system.

## If the Problem Persists

External AC power, power cord condition, battery installation, visible battery condition, charging state, and known-good battery substitution have been evaluated where appropriate. Remaining causes may involve internal charging circuitry, power management, battery sensing, internal connections, or another service-level fault.

The ventilator should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Philips documentation and approved test equipment
- Repaired only by qualified personnel

After repair or battery replacement, verify charging, AC-to-battery transition, battery-to-AC transition, ventilation continuity, alarms, and other required return-to-service checks.

## Clinical Use Tip

Verify transport and backup power before a ventilator is assigned to any situation where AC power could be interrupted.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Battery complaints should be separated into AC-source, battery, and charging-system causes using controlled tests and approved substitutions. Never test backup power on a patient-dependent ventilator, and escalate any unreliable power transition.

That is successful troubleshooting.
