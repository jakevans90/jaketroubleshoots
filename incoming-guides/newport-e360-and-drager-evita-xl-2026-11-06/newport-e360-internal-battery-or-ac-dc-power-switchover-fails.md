---
schemaVersion: 1
title: "Newport e360 Ventilator - Internal Battery or AC/DC Power Switchover Fails"
issueTitle: "Internal Battery or AC/DC Power Switchover Fails"
description: "Addresses battery charging, backup-power, and power-source transfer problems caused by AC supply, cords, external DC sources, connections, or battery condition."
assetType: "Ventilator"
manufacturer: "Newport"
model: "e360"
slug: "newport-e360-internal-battery-or-ac-dc-power-switchover-fails"
dateAdded: "2026-11-06"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the Newport e360 shut down when AC power was disconnected for transport preparation."
  cause: "Clinical Engineering found the internal battery would not support ventilator operation despite verified AC charging."
  resolution: "The battery was replaced using an approved service procedure, power switchover was verified off-patient, and ventilation and alarms passed final testing."
helpfulDetails:
  - "AC outlet tested"
  - "Power-cord condition"
  - "AC recognition status"
  - "Battery charging indication"
  - "Battery behavior"
  - "External DC source and cable tested"
  - "Switchover behavior"
  - "Unexpected reboot or shutdown"
  - "Electrical-safety results"
  - "Final device status"
---

## What This Guide Helps With

Addresses battery charging, backup-power, and power-source transfer problems caused by AC supply, cords, external DC sources, connections, or battery condition.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Before Testing Power Sources
Do not deliberately disconnect power from a ventilator supporting a patient to test battery operation. Move the patient to a verified ventilator or provide suitable backup ventilation first.

Confirm whether the complaint involves charging, battery operation, AC loss switchover, external DC operation, or unexpected shutdown.

**Expected outcome:** The patient is protected and the exact power-related complaint is understood.

### 2. Inspect the AC Power Cord and Connection
Check the power cord, plug, strain relief, and ventilator power inlet for visible damage, looseness, heat discoloration, or contamination.

**Expected outcome:** The AC connection is secure and undamaged. If correcting a loose connection restores normal charging and operation, troubleshooting can stop after verification.

### 3. Verify the AC Outlet
Test the outlet with appropriate electrical-safety or outlet-testing equipment, or move the ventilator to a known-good approved receptacle.

**Expected outcome:** A reliable AC source is confirmed. If the ventilator operates normally on another outlet, refer the original receptacle or branch-circuit concern to the appropriate facilities personnel.

### 4. Confirm AC Operation and Charging Indication
Power the ventilator from verified AC and observe normal startup, AC status, and battery charging indications.

Do not rely solely on a staff report that the unit had been plugged in.

**Expected outcome:** The ventilator recognizes AC power and indicates expected battery charging behavior. Failure to recognize verified AC requires escalation after external connections are checked.

### 5. Inspect Any External DC Power Setup
If external DC operation is part of the complaint, inspect the approved DC cable, connector, source, and any externally accessible fuse or adapter allowed by facility procedures.

Use only compatible approved accessories.

**Expected outcome:** The external DC source and cable are correctly connected and functional. A known-good approved cable or source restores operation if the original accessory was defective.

### 6. Evaluate Battery Condition
With the ventilator off-patient, review the available battery status indication. Look for failure to charge, rapid depletion, inability to support operation, or an abnormal battery condition.

Do not open or rebuild the battery pack.

**Expected outcome:** The battery accepts charge and shows usable status. A battery that remains unable to support operation after verified charging should be replaced or evaluated according to approved service procedures.

### 7. Test Power Switchover Off-Patient
Using an appropriate test lung and controlled bench setup, verify transfer between approved power sources according to facility and manufacturer procedures.

Observe for rebooting, ventilation interruption, alarm behavior, or loss of display.

**Expected outcome:** Ventilation continues appropriately through the tested power transition and the ventilator provides the expected power-source indication or alarm. If switchover works repeatedly, the issue is resolved.

### 8. Verify Battery Backup Function
Where approved, operate the ventilator from internal battery long enough to confirm stable backup operation without making assumptions about total runtime beyond manufacturer-defined testing procedures.

**Expected outcome:** The ventilator remains operational and stable on internal battery during the functional test.

### 9. Perform Final Electrical and Functional Verification
After correction, perform required electrical-safety testing, verify charging, confirm power-source transfer, and verify basic ventilation and alarms.

**Expected outcome:** All tested power modes function normally with no interruption to ventilation.

### 10. Escalate an Unresolved Power Failure
If known-good AC, approved DC sources, cables, and battery replacement or approved battery evaluation do not resolve the problem, stop external troubleshooting.

**Expected outcome:** The ventilator is removed from service rather than being used with unreliable backup power.

## If the Problem Persists

External power sources, cords, approved DC accessories, and battery condition have been evaluated. Remaining causes may involve internal power conversion, charging circuitry, source-transfer control, battery monitoring, or other service-level faults.

Remove the ventilator from service, label it **Out of Service**, and send it for bench evaluation using Newport documentation and approved electrical test equipment. Internal power-system repair should be performed only by qualified personnel.

Return the device to service only after required electrical-safety testing, charging verification, power-transfer testing, ventilation testing, and alarm verification pass.

## Clinical Use Tip

Never test ventilator backup-power transfer by disconnecting AC while a patient depends on the ventilator.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Power problems require patient protection first, followed by verification of the outlet, cords, external power sources, battery condition, and controlled switchover testing before internal failure is suspected.

That is successful troubleshooting.
