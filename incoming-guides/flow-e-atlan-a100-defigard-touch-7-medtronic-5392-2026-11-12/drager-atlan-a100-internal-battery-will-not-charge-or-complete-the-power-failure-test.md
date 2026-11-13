---
schemaVersion: 1
title: "Drager Atlan A100 Anesthesia Machine - Internal Battery Will Not Charge or Complete the Power-Failure Test"
issueTitle: "Internal Battery Will Not Charge or Complete the Power-Failure Test"
description: "Addresses battery charging or backup-power failures caused by AC supply, power connections, charge state, prolonged storage, or battery/power-system faults."
assetType: "Anesthesia Machine"
manufacturer: "Drager"
model: "Atlan A100"
slug: "drager-atlan-a100-internal-battery-will-not-charge-or-complete-the-power-failure-test"
dateAdded: "2026-11-12"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that the Drager Atlan A100 battery would not charge and the machine failed the scheduled power-failure test."
  cause: "Clinical Engineering found the AC power cord was not fully seated at the machine inlet, preventing reliable charging."
  resolution: "Clinical Engineering secured the power connection, verified AC recognition and battery charging, completed the approved power-failure and system tests successfully, and returned the machine to service."
helpfulDetails:
  - "Exact battery or power message"
  - "AC outlet tested"
  - "Power-cord and inlet condition"
  - "AC recognition status"
  - "Battery indication before charging"
  - "Whether the machine had been stored or unplugged"
  - "Charge behavior"
  - "Power-failure test result"
  - "AC-to-battery and battery-to-AC transition"
  - "Final system-test result"
  - "Final device status"
---

## What This Guide Helps With

Addresses battery charging or backup-power failures caused by AC supply, power connections, charge state, prolonged storage, or battery/power-system faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Avoid Unverified Backup Power
Do not intentionally remove AC power to test an unreliable battery while a patient depends on the machine. Transfer the patient to another verified anesthesia system before testing backup operation.

**Expected outcome:** Patient ventilation and anesthesia are independent of the battery under investigation.

### 2. Confirm the Exact Battery Problem
Determine whether the battery fails to charge, reports an unexpectedly low state of charge, immediately shuts down during AC loss, or fails the machine's normal power-failure test.

Record any displayed battery or power message exactly.

**Expected outcome:** The reported failure is clearly identified and reproducible under controlled conditions.

### 3. Verify the AC Source
Confirm the machine is connected to a known-good AC outlet. Inspect the power cord, plug, inlet, and strain relief for damage or looseness.

Test the outlet using the facility's approved method when appropriate.

**Expected outcome:** Stable AC power is available to the machine. If the outlet is defective, correct or escalate the facility power issue before evaluating the battery.

### 4. Confirm the Machine Recognizes AC Power
With the machine connected to verified AC, confirm that its normal power indicators show AC operation and that there is evidence the battery is being charged when appropriate.

A machine that does not recognize AC may have a power-input problem rather than a battery problem.

**Expected outcome:** The Atlan A100 recognizes AC operation normally.

### 5. Allow an Appropriate Charging Opportunity
If the machine has been unplugged, stored, or recently discharged, leave it connected to verified AC according to normal facility and manufacturer charging practices before repeating the battery test.

Do not declare a battery defective solely because it was tested immediately after prolonged storage or discharge.

**Expected outcome:** The indicated battery state improves after charging. If it does and the subsequent test passes, continue to final verification.

### 6. Inspect for External Power Interruptions
Check for a loose plug, switched or intermittent outlet, damaged cord, power strip issues if one is authorized, or repeated movement that may interrupt AC connection.

**Expected outcome:** The machine receives continuous AC power without intermittent loss.

### 7. Perform the Normal Power-Failure Test
With the machine out of patient use and following the approved test sequence, verify that it transitions to battery operation as intended when AC is removed.

Observe indications, alarms, and whether the machine remains operational long enough to complete the required test. Do not invent a runtime requirement; use the applicable manufacturer or facility procedure.

**Expected outcome:** The machine transfers to battery operation and completes the required power-failure verification.

### 8. Reconnect AC and Verify Charging Resumes
Reconnect the machine to AC and verify that normal AC operation resumes and battery charging indications return appropriately.

**Expected outcome:** Power transition back to AC is normal and charging resumes.

### 9. Complete Final Functional Verification
Perform the required system test and confirm normal display, alarms, ventilation, power indications, and transition behavior.

If battery replacement or internal power repair has occurred, complete all applicable post-service testing before return to service.

**Expected outcome:** The machine operates normally on AC and successfully completes the required backup-power test. Troubleshooting can stop.

### 10. Escalate a Persistent Battery or Charging Failure
If the AC source, cord, charging opportunity, and test procedure are verified but the battery will not charge or support the required test, remove the machine from service.

Do not open battery packs or perform unauthorized internal power-supply repair.

**Expected outcome:** The device is referred for qualified battery and internal power-system evaluation.

## If the Problem Persists

Common external causes such as outlet failure, damaged power cord, interrupted AC connection, insufficient charge time, and incorrect test conditions have been ruled out. The remaining fault may involve the battery, charging circuit, internal power supply, power-management electronics, or associated connections.

The device should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate Drager documentation and approved electrical-safety and functional test equipment.
- Repaired or have the battery replaced only by qualified personnel.
- Fully tested for charging, AC/battery transition, alarms, electrical safety as applicable, ventilation, and system operation before return to service.

A machine that cannot provide verified backup power should not be considered ready for clinical use.

## Clinical Use Tip

Never create a deliberate AC-power failure on an anesthesia machine that is actively supporting a patient.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Backup-power failures should be approached by verifying the external AC path and charge condition before assuming battery or internal power-system failure. Protect the patient, test under controlled conditions, escalate unresolved failures, and document the final verification clearly.

That is successful troubleshooting.
