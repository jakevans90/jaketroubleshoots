---
schemaVersion: 1
title: "Getinge Flow-e Anesthesia Machine - Battery Will Not Charge or Support an Orderly Shutdown"
issueTitle: "Battery Will Not Charge or Support an Orderly Shutdown"
description: "The internal battery does not charge, is not recognized, or cannot maintain the machine long enough for expected power-transition or shutdown behavior."
assetType: "Anesthesia Machine"
manufacturer: "Getinge"
model: "Flow-e"
slug: "getinge-flow-e-battery-will-not-charge-or-support-an-orderly-shutdown"
dateAdded: "2026-11-12"
taxonomyMode: "reuse"
ccr:
  complaint: "Anesthesia staff reported that the Flow-e battery would not support the machine when AC power was disconnected during checkout."
  cause: "Clinical Engineering verified normal AC input and found the installed battery unable to maintain operation during controlled testing."
  resolution: "Replaced the battery using the approved service procedure, verified charging and AC-to-battery transfer, completed checkout, and returned the machine to service."
helpfulDetails:
  - "Battery status indication"
  - "AC receptacle tested"
  - "Power-cord condition"
  - "Charging indication"
  - "AC-to-battery transition result"
  - "Shutdown behavior"
  - "Battery condition information"
  - "Battery replacement performed"
  - "Checkout and electrical-safety results"
  - "Final device status"
---

## What This Guide Helps With

The internal battery does not charge, is not recognized, or cannot maintain the machine long enough for expected power-transition or shutdown behavior.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Power Loss
Do not troubleshoot an anesthesia machine with unreliable backup power while it is supporting a patient.

If loss of AC power could interrupt ventilation, monitoring, or gas delivery, move the patient to a verified alternative system before testing the battery.

**Expected outcome:** Patient support is independent of the affected machine.

### 2. Confirm the Complaint
Determine whether the battery fails to charge, shows an abnormal status, immediately discharges during AC removal, or cannot support an orderly machine shutdown.

**Expected outcome:** The specific battery symptom is documented and reproducible.

### 3. Verify the AC Source
Confirm the Flow-e is connected to a known-good hospital-grade receptacle and that the receptacle has power.

Inspect the machine's power cord and plug for damage, looseness, overheating, or contamination.

**Expected outcome:** Reliable AC power is reaching the machine. If restoring AC power resolves the charge complaint, continue with battery verification before return to service.

### 4. Verify Charging Indication
With AC connected, observe the machine's normal battery and charging indications.

Allow charging under normal approved conditions rather than judging battery condition immediately after connection.

**Expected outcome:** The machine indicates that external power is present and the battery is charging or appropriately charged.

### 5. Inspect External Power Connections
Check accessible power-cord connections and strain reliefs for looseness or intermittent contact. Gently verify normal connection stability without stressing the cable.

**Expected outcome:** AC input remains stable when the cord is in its normal position. An intermittent or damaged cord requires replacement or repair before further testing.

### 6. Check Environmental Conditions
Confirm the machine has not recently been stored or operated in conditions that could adversely affect battery charging, such as unusual heat or cold.

Allow the device to return to an appropriate operating environment before retesting.

**Expected outcome:** Battery testing occurs under normal environmental conditions.

### 7. Perform a Controlled AC-to-Battery Transition Test
With the machine not connected to a patient and configured for approved bench testing, remove AC power and observe whether operation transitions appropriately to battery power.

Do not intentionally exhaust the battery outside approved service testing.

**Expected outcome:** The machine remains operational as intended during the transition and provides appropriate power-status indication.

### 8. Verify Orderly Shutdown Behavior
If the complaint specifically involves shutdown capability, verify according to the applicable manufacturer procedure that the battery supports the intended orderly shutdown sequence.

**Expected outcome:** The machine transitions and shuts down normally under the approved test procedure. If it cannot, remove it from service.

### 9. Inspect Battery Status Through Normal Service Information
Review battery condition information available through authorized normal technical procedures.

Do not modify protected battery parameters or use unauthorized service menus.

**Expected outcome:** Battery status is consistent with acceptable operation. A battery identified as degraded should be replaced using approved service procedures.

### 10. Complete Functional and Electrical Verification
After correction or approved battery replacement, verify charging, AC-to-battery transfer, battery operation, normal shutdown behavior, and applicable electrical-safety requirements.

**Expected outcome:** Power operation is reliable and all required tests pass before return to service.

## If the Problem Persists

External AC source, power cord, operating environment, charging opportunity, and accessible power connections have been ruled out. Remaining causes may include a degraded battery, charging circuitry, internal power supply, battery interface, or other service-level power problem.

The device should be:

- Removed from service if backup power cannot be verified.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using approved Getinge documentation and electrical test equipment.
- Repaired or have the battery replaced only by qualified personnel.

Do not rely on AC-only operation when the machine is expected to provide battery-supported transition or shutdown capability.

Return to service only after full power, battery, machine checkout, and applicable electrical-safety testing are successful.

## Clinical Use Tip

Verify backup power before a case if the anesthesia machine may need to tolerate transfer, outlet interruption, or facility power disturbances.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Start with the external AC source before blaming the battery, verify backup operation under controlled conditions, remove the machine from service when power transition is unreliable, and document both the correction and final power testing.

That is successful troubleshooting.
