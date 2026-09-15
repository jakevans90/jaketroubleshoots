---
schemaVersion: 1
title: "LivaNova S5 Heart-Lung Machine - Battery Backup, Power Supply, or CAN-Bus Communication Problem"
issueTitle: "Battery Backup, Power Supply, or CAN-Bus Communication Problem"
description: "Troubleshoots backup-power, external power, and system communication problems using power-source checks, module isolation, connections, and safe functional verification."
assetType: "Heart-Lung Machine"
manufacturer: "LivaNova"
model: "S5"
slug: "livanova-s5-battery-backup-power-supply-or-can-bus-communication-problem"
dateAdded: "2026-09-15"
taxonomyMode: "reuse"
ccr:
  complaint: "Perfusion reported that several S5 modules intermittently disappeared from the console during pre-case setup."
  cause: "Clinical Engineering found a shared external communication connector partially seated after the system had been moved."
  resolution: "Clinical Engineering reseated and secured the connector and verified stable module communication, repeated startup, and normal system operation."
helpfulDetails:
  - "AC or battery condition when failure occurred"
  - "Outlet verification"
  - "Power-cord condition"
  - "Backup-power indicators"
  - "Whether the system restarted"
  - "Modules affected"
  - "Exact communication or power message"
  - "External communication cable condition"
  - "Known-good substitutions or isolation performed"
  - "Results before and after correction"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots backup-power, external power, and system communication problems using power-source checks, module isolation, connections, and safe functional verification.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain a Fully Functional Backup System

Do not troubleshoot unstable S5 power or system communication while a patient depends on the affected equipment. A loss of power distribution or shared communication can affect multiple perfusion functions simultaneously.

Follow the perfusion contingency plan and transition to verified backup support as required.

If there is smoke, odor, overheating, arcing, liquid intrusion, or repeated power loss, remove power when clinically safe and take the system out of service.

**Expected outcome:** Patient support is maintained independently of the suspect S5 power or communication system.

Once safely isolated from clinical use, troubleshooting may continue.

### 2. Confirm the Failure Pattern

Determine whether the problem involves:

- Failure on AC power
- Failure on battery-supported power
- Battery not charging
- Unexpected transition to backup power
- Multiple modules disappearing simultaneously
- Intermittent module communication
- Complete system restart
- A single module versus system-wide CAN-bus communication loss

Record all displayed messages and indicator states.

**Expected outcome:** The failure is categorized as source-power, backup-power, or shared communication related.

If the system remains stable through repeated controlled tests after a correctable external condition is found, troubleshooting can stop.

### 3. Verify Facility AC Power

Inspect the power cord, plug, strain relief, and accessible input connections. Confirm the receptacle is powered using approved test equipment or a known-good source.

Check whether the problem occurs at one outlet only or follows the S5.

**Expected outcome:** A stable facility AC source is confirmed.

If an outlet or external power problem is identified and correction restores normal operation, troubleshooting can stop after system verification.

### 4. Inspect External Power Connections

With the S5 removed from service, inspect all accessible power connections associated with the console and connected modules.

Look for:

- Loose connectors
- Damage
- Heat discoloration
- Contamination
- Damaged cord insulation
- Strain at connection points

Do not open internal power supplies.

**Expected outcome:** External power connections are fully seated and free of visible damage.

If correcting an external power connection restores reliable operation, troubleshooting can stop after testing.

### 5. Evaluate Battery-Supported Operation

Using approved procedures, determine whether the system:

- Recognizes backup power.
- Indicates charging appropriately.
- Transfers between AC and backup power normally.
- Remains stable during the approved backup-power test.

Do not intentionally run backup batteries to exhaustion.

**Expected outcome:** Backup power is recognized and supports the system as intended during the approved test.

If a replaceable approved battery component is confirmed defective and replacement restores normal operation, troubleshooting can stop after verification.

### 6. Inspect External Communication Connections

Because shared CAN-bus communication problems may affect multiple modules, inspect accessible intermodule communication cables and connectors for:

- Partial seating
- Damage
- Fluid contamination
- Cable strain
- Crushed sections
- Loose retaining hardware

Reseat only approved external communication connections.

**Expected outcome:** External communication connections are secure and undamaged.

If reseating a communication connection restores all affected modules and stability is confirmed, troubleshooting can stop.

### 7. Determine Whether One Module Is Disrupting the System

If permitted by approved service procedures, identify whether the communication problem occurs only when a specific external module or cable is connected. Use controlled isolation or known-good substitution without altering protected internal bus termination or configuration.

Do not remove modules required for active clinical support.

**Expected outcome:** The problem is isolated to a specific external module/cable or remains system-wide.

If a defective external module connection or cable is identified and correction restores stable communication, troubleshooting can stop after final verification.

### 8. Verify Normal Configuration and Module Population

Confirm that connected modules match the normal system configuration and that no component has been intentionally removed, disabled, or reconfigured.

Do not change restricted CAN-bus parameters, internal addressing, or termination.

**Expected outcome:** Installed modules and the authorized configuration are consistent.

If an authorized configuration correction resolves communication, troubleshooting can stop.

### 9. Perform Final System Verification

After correction, verify:

- Stable operation on AC power.
- Appropriate battery/backup status.
- Normal transfer behavior using approved procedures.
- All required modules are recognized.
- Communication remains stable through repeated startup.
- No unexplained system resets occur.
- Required pumps, sensors, displays, and alarms function appropriately.

Complete all applicable return-to-service testing.

**Expected outcome:** The complete S5 system remains stable across approved power and communication checks.

If all checks pass, troubleshooting is complete.

### 10. Escalate Persistent Power or CAN-Bus Problems

If the system has repeated power loss, unexplained resets, battery-transfer problems, or persistent communication loss after external causes are ruled out, stop troubleshooting.

Do not open internal power supplies, repair bus electronics, change internal termination, or replace circuit boards without authorized service procedures.

**Expected outcome:** A system with unresolved shared power or communication risk remains unavailable for patient use.

## If the Problem Persists

Facility power, external power connections, backup-power behavior, module cabling, and normal configuration have been evaluated. Remaining possibilities may involve internal power distribution, battery-management circuitry, internal CAN-bus components, module electronics, or protected configuration.

The S5 should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate LivaNova documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Before return to service, complete applicable electrical safety, backup-power, communication, module-recognition, alarm, and full-system functional testing.

Knowing when to stop external troubleshooting is especially important when one fault can affect multiple perfusion functions.

## Clinical Use Tip

A shared power or communication problem can affect several S5 modules at once, so verify the complete heart-lung machine rather than only the first function that appeared to fail.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Shared power and communication faults deserve conservative handling because they can affect multiple perfusion functions simultaneously. Verify facility power and external connections first, isolate modules logically, avoid unauthorized internal bus work, complete full-system verification, and document the event clearly.

That is successful troubleshooting.
