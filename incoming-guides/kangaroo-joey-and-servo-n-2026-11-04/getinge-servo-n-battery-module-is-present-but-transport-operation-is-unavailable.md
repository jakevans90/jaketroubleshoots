---
schemaVersion: 1
title: "Getinge Servo-n Ventilator - Battery Module Is Present but Transport Operation Is Unavailable"
issueTitle: "Battery Module Is Present but Transport Operation Is Unavailable"
description: "Troubleshoots unavailable battery-powered transport operation caused by charging, module seating, battery condition, power configuration, or service-level faults."
assetType: "Ventilator"
manufacturer: "Getinge"
model: "Servo-n"
slug: "getinge-servo-n-battery-module-is-present-but-transport-operation-is-unavailable"
dateAdded: "2026-11-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the Servo-n detected its battery module but would not remain operating when disconnected from AC power."
  cause: "Clinical Engineering found the installed battery module failed controlled battery-operation testing while a known-good battery operated normally."
  resolution: "The defective battery module was replaced, AC-to-battery transition was verified successfully, and the ventilator was returned to service."
helpfulDetails:
  - "AC power status"
  - "Battery recognition status"
  - "Charging indication"
  - "Battery physical condition"
  - "Module seating condition"
  - "Known-good battery result"
  - "AC-to-battery transfer result"
  - "Unexpected shutdown behavior"
  - "Final transport-readiness status"
---

## What This Guide Helps With

Troubleshoots unavailable battery-powered transport operation caused by charging, module seating, battery condition, power configuration, or service-level faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Before Testing Battery Operation
Do not remove AC power from a ventilator supporting a patient merely to test a questionable battery system.

Move the patient to another verified ventilator or ensure an approved backup ventilation method is immediately available before technical battery testing.

**Expected outcome:** Battery troubleshooting can be performed without risking interruption of ventilation.

### 2. Confirm the Exact Reported Condition
Determine whether the Servo-n:
- Detects the battery but will not operate from it
- Reports the module as unavailable
- Shuts down immediately when AC is removed
- Operates only briefly
- Will not indicate charging

Document battery indications while connected to AC.

**Expected outcome:** The battery failure mode is clearly identified.

### 3. Verify AC Power and Charging Conditions
Connect the ventilator to a known-good approved AC source.

Inspect:
- Power cord
- Cord retention
- Plug condition
- Outlet condition
- AC power indication
- Battery charging indication

**Expected outcome:** The ventilator operates normally from AC and recognizes external power.

### 4. Inspect and Reseat the Battery Module
With the ventilator in a safe bench condition, inspect the accessible battery module for:
- Incomplete seating
- Damaged housing
- Contaminated contacts
- Swelling
- Heat damage
- Cracked latches or retention features

Reseat the module according to approved procedures.

**Expected outcome:** The battery module is fully secured and recognized. If transport operation becomes available, troubleshooting can stop after verification.

### 5. Allow the Battery to Charge
If the battery has been deeply discharged or stored, allow it to charge under normal approved conditions before judging runtime.

Do not assume a battery is defective solely because it was initially depleted.

**Expected outcome:** Battery status progresses normally and the module becomes available for battery operation.

### 6. Test With a Known-Good Compatible Battery Module
When available, install a known-good approved battery module and repeat the test.

Do not use damaged, swollen, overheated, or questionable batteries.

**Expected outcome:** If the known-good battery supports normal operation, the original battery module is the likely failed replaceable component and should be removed from service.

### 7. Verify Battery Operation Under Controlled Conditions
With the ventilator removed from patient use and an appropriate test setup connected, verify transition from AC to battery and back to AC.

Observe for:
- Unexpected shutdown
- Battery recognition loss
- Alarm abnormalities
- Intermittent power cycling

**Expected outcome:** The ventilator transfers to battery power without interruption and returns to AC operation normally. Troubleshooting can stop.

### 8. Perform Final Transport-Readiness Verification
Confirm the battery is recognized, appropriately charged, retained securely, and capable of supporting the required transport workflow according to facility and manufacturer requirements.

**Expected outcome:** Battery transport operation is available and dependable.

## If the Problem Persists

External power, battery seating, charging conditions, and known-good battery substitution have been checked. The remaining problem may involve charging circuitry, battery communication, power-management hardware, internal connections, or another service-level condition.

The Servo-n should be:
- Removed from transport service
- Labeled Out of Service if battery backup is required for intended use
- Sent for repair or bench evaluation
- Evaluated using appropriate Getinge service documentation and approved test equipment
- Repaired only by qualified personnel

After repair, verify AC operation, battery charging, battery recognition, AC-to-battery transition, and required ventilator performance before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Never begin patient transport with a Servo-n when the battery system is unavailable, unreliable, or insufficiently verified.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Treat reliable backup power as part of ventilator safety. Verify AC power, charging, seating, and the battery itself before assuming an internal power-system fault, and escalate any unreliable transport-power condition.

That is successful troubleshooting.
