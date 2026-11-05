---
schemaVersion: 1
title: "Hamilton C2 Ventilator - Battery Will Not Charge, Switch Over, or Support Transport"
issueTitle: "Battery Will Not Charge, Switch Over, or Support Transport"
description: "Troubleshoots charging, battery recognition, AC-to-battery switchover, and short transport runtime caused by power, connection, battery, or configuration problems."
assetType: "Ventilator"
manufacturer: "Hamilton"
model: "C2"
slug: "hamilton-c2-battery-will-not-charge-switch-over-or-support-transport"
dateAdded: "2026-11-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the Hamilton C2 would not remain operating when disconnected from AC power."
  cause: "Clinical Engineering found that the installed battery would not support load, while a known-good battery operated normally."
  resolution: "Replaced the defective battery, verified charging and AC-to-battery switchover, and confirmed uninterrupted ventilation and normal alarms with a test lung."
helpfulDetails:
  - "AC or battery status"
  - "Outlet tested"
  - "Power-cord condition"
  - "Battery detected or not detected"
  - "Charging indication"
  - "Physical battery condition"
  - "Known-good battery substitution"
  - "Switchover result"
  - "Runtime test result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots charging, battery recognition, AC-to-battery switchover, and short transport runtime caused by power, connection, battery, or configuration problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Before Testing Power Sources

Do not remove AC power from a ventilator supporting a patient when battery reliability is uncertain.

Move the patient to another verified ventilator before battery switchover or runtime testing.

**Expected outcome:** Ventilation is maintained while the affected C2 can be tested safely.

### 2. Confirm the Battery Symptom

Determine whether the battery is not detected, will not charge, fails to switch over when AC is removed, discharges rapidly, or causes shutdown.

Record battery indicators and displayed messages.

**Expected outcome:** The exact battery failure mode is identified.

### 3. Verify AC Power and Power Cord Condition

Connect the ventilator directly to a known-good approved outlet. Inspect the power cord, plug, strain relief, and inlet for visible damage or looseness.

Avoid relying on an unverified extension cord or power strip.

**Expected outcome:** The ventilator receives stable AC power and indicates AC operation appropriately.

If normal charging resumes on a known-good outlet, correct the external power issue and complete verification.

### 4. Inspect Battery Installation and External Contacts

With the device safely removed from clinical use, verify that accessible battery modules are correctly installed and fully seated.

Inspect accessible contacts and battery housings for contamination, damage, swelling, cracking, or overheating.

**Expected outcome:** Batteries are properly installed with no visible physical defect.

Any swollen, damaged, overheated, or leaking battery requires removal from service according to facility battery-handling policy.

### 5. Allow Charging Under Normal Conditions

Connect the ventilator to verified AC power and observe whether charging status appears normally.

Do not assume a depleted battery is defective until it has been given an appropriate opportunity to charge under manufacturer-approved conditions.

**Expected outcome:** Charging is recognized and progresses normally.

If charging status remains absent, continue troubleshooting.

### 6. Compare or Substitute a Known-Good Compatible Battery

If permitted by facility policy, substitute a known-good compatible battery module.

Repeat charging and off-AC switchover checks on the bench.

**Expected outcome:** The problem either follows the battery or remains with the ventilator.

If the known-good battery operates normally, replace the defective battery and proceed with final verification.

### 7. Test AC-to-Battery Switchover on the Bench

With a test lung attached and the patient absent, operate the ventilator on AC power and perform the approved switchover check.

Verify that ventilation continues during transition and that appropriate power-source indications and alarms occur.

**Expected outcome:** Ventilation continues without interruption during normal power-source transition.

If switchover fails, remove the ventilator from service.

### 8. Verify Transport Runtime as Required

If short runtime was reported, evaluate battery performance using the facility or manufacturer-approved battery test method.

Do not estimate remaining battery capacity based only on a brief bench observation.

**Expected outcome:** Battery performance meets applicable service criteria.

If the battery cannot support required operation, replace it or escalate the ventilator for service.

### 9. Perform Final Functional Verification

Verify AC operation, charging indication, battery recognition, switchover, alarms, and continued ventilation with a test lung.

**Expected outcome:** Both AC and battery functions operate reliably and all relevant checks pass.

If successful, return the ventilator to service according to policy.

## If the Problem Persists

If the C2 will not charge, recognize, switch to, or operate reliably from known-good batteries after external AC power and battery installation have been verified, the issue may involve internal charging circuitry, power-management components, battery interfaces, or internal power distribution.

The ventilator should be:

- Removed from service
- Labeled **Out of Service**
- Sent for qualified bench evaluation
- Tested using Hamilton service documentation and approved electrical test equipment
- Repaired only by qualified personnel
- Verified for charging, switchover, alarms, and ventilation before return to service

## Clinical Use Tip

A ventilator intended for transport should never leave a reliable AC source until battery status and switchover have been verified.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Battery problems become patient-safety issues during transport or power interruption. Verify the external AC source and battery itself before assuming an internal charging failure, and do not return the ventilator to service without successful switchover verification.

That is successful troubleshooting.
