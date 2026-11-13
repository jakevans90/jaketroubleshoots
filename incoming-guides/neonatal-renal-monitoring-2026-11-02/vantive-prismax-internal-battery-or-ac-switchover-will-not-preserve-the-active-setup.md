---
schemaVersion: 1
title: "Vantive PrisMax Continuous Renal Replacement Therapy (CRRT) - Internal Battery or AC Switchover Will Not Preserve the Active Setup"
issueTitle: "Internal Battery or AC Switchover Will Not Preserve the Active Setup"
description: "PrisMax shuts down, restarts, or loses setup information when AC power is interrupted because of external power, battery, charging, or service-level problems."
assetType: "Continuous Renal Replacement Therapy (CRRT)"
manufacturer: "Vantive"
model: "PrisMax"
slug: "vantive-prismax-internal-battery-or-ac-switchover-will-not-preserve-the-active-setup"
dateAdded: "2026-11-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the PrisMax shut down and lost the active setup when the AC power cord was disconnected for transport."
  cause: "Clinical Engineering found that the internal battery was not maintaining operation after adequate charging, while the AC source and power cord tested normally."
  resolution: "Clinical Engineering removed the unit from service for qualified battery-system repair and documented that battery and AC-transfer verification are required before return to clinical use."
helpfulDetails:
  - "Whether the device shut down or restarted"
  - "Whether the active setup was retained"
  - "AC and battery indications before the event"
  - "Outlet test result"
  - "Power-cord and inlet condition"
  - "Recent storage or charging history"
  - "Behavior during controlled AC removal"
  - "Behavior when AC was restored"
  - "Known-good unit comparison"
  - "Unusual heat, odor, swelling, or damage"
  - "Final device status"
---

## What This Guide Helps With

PrisMax shuts down, restarts, or loses setup information when AC power is interrupted because of external power, battery, charging, or service-level problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Before Testing Power Transfer
Do not deliberately disconnect AC power from a PrisMax supporting a patient solely to test battery operation or power switchover.

If power reliability is questionable during active therapy, transfer therapy to another verified unit according to clinical procedures before testing.

**Expected outcome:** No patient depends on a device with an unverified battery or AC switchover function.

### 2. Confirm the Exact Reported Behavior
Determine what staff observed when AC power was lost or disconnected:
- Unit immediately powered off
- Unit restarted
- Active setup was lost
- Unit operated briefly and then shut down
- Battery indication was absent or unexpected
- Unit did not recognize restoration of AC power

Record any displayed messages exactly.

**Expected outcome:** The reported failure mode is clearly defined before battery testing begins.

### 3. Verify the AC Source and Power Cord
Inspect the power cord, plug, and equipment inlet for looseness, damage, contamination, or overheating.

Confirm the receptacle provides stable power using approved test methods.

A loose plug or intermittent outlet can mimic a battery or switchover problem.

**Expected outcome:** AC power is stable and the external power path is reliable. If correcting an AC connection eliminates the issue, troubleshooting can stop after verification.

### 4. Observe Battery and AC Status Indications
With the device connected to verified AC power, review the normal operator-visible indications showing AC and battery status.

Look for evidence that the device recognizes external power and that the battery is present or charging as applicable.

Do not enter restricted service screens to alter battery configuration.

**Expected outcome:** The device correctly recognizes AC operation and presents a normal battery status. Missing or abnormal battery recognition requires further evaluation.

### 5. Allow Appropriate Charging Before Testing
If the device has recently been stored, disconnected from AC, or transported for an extended period, allow the battery to charge in accordance with approved manufacturer and facility procedures before concluding that the battery has failed.

Do not assume a discharged battery is defective without confirming adequate charging opportunity.

**Expected outcome:** The battery reaches a condition suitable for controlled evaluation. If battery operation becomes normal after charging, document the discharged state and verify switchover.

### 6. Inspect External Signs of Battery or Power-System Problems
Check for:
- Unexpected heat
- Swelling or deformation accessible without disassembly
- Odor
- Damage around the enclosure
- Evidence of liquid intrusion
- Repeated power cycling
- Abnormal charging indications

If any sign of battery damage, overheating, or electrical distress is present, stop testing and remove the device from service.

**Expected outcome:** No visible or sensory evidence indicates an unsafe battery or power condition.

### 7. Perform a Controlled AC-to-Battery Transfer Test
With no patient connected and the device in an appropriate controlled setup, verify that the system is stable on AC power.

Using approved testing practice, remove AC power and observe whether the system transitions to battery operation without an unexpected shutdown, restart, or loss of the active setup.

Do not conduct endurance testing beyond manufacturer-approved procedures.

**Expected outcome:** The PrisMax remains powered and preserves the active setup during the controlled transfer. If it does, continue with restoration-of-AC testing.

### 8. Verify Transfer Back to AC Power
Reconnect the unit to a verified AC source and confirm that:
- AC operation is recognized
- The system remains running
- The active setup remains intact
- Battery status responds appropriately
- No unexpected restart occurs

**Expected outcome:** Transition back to AC power is seamless and the setup remains preserved. Successful transfer in both directions indicates normal switchover function.

### 9. Compare With a Known-Good Unit When Appropriate
If operator-visible battery behavior appears questionable but no specifications are available at the bench, compare general status behavior with another known-good PrisMax under the same controlled conditions.

Do not use comparison to substitute for required manufacturer performance testing.

**Expected outcome:** The affected unit behaves consistently with a known-good system. Significant differences support escalation for service evaluation.

### 10. Perform Final Functional Verification
Before returning the device to service, verify:
- Reliable AC operation
- Correct recognition of AC connection and removal
- Controlled battery operation
- Preservation of the active setup during switchover
- Normal restoration to AC operation
- Stable touchscreen and controls
- Normal startup and alarm functions

Complete any manufacturer-required battery, electrical-safety, or return-to-service testing applicable to the work performed.

**Expected outcome:** Power transitions occur reliably without unexpected shutdown, restart, or loss of setup. The device can be returned to service only after all required checks pass.

### 11. Escalate Failed Battery or Switchover Performance
If the PrisMax cannot preserve operation or setup during controlled AC interruption after external power and charging conditions have been verified, remove it from service.

Do not perform unauthorized internal battery-circuit repair, charging-system adjustment, or board-level troubleshooting.

**Expected outcome:** The device is routed for qualified battery and internal power-system evaluation.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve the battery, charging circuitry, internal power distribution, battery communication, power-management electronics, software, or another service-level condition.

The device should be:
- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Following service, perform appropriate battery, AC-transfer, electrical-safety, alarm, and functional testing before returning the device to clinical use.

Knowing when unreliable backup power requires removal from service is proper troubleshooting.

## Clinical Use Tip

Verify backup-power capability before transport or any situation where the PrisMax may be disconnected from facility AC power.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Backup power on a CRRT system is a patient-safety function. Verify the AC source, connections, charging condition, and controlled power transfer before assuming an internal failure, and remove the unit from service whenever reliable switchover cannot be demonstrated.

That is successful troubleshooting.
