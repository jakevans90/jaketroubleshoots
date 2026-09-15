---
schemaVersion: 1
title: "LivaNova S5 Heart-Lung Machine - Gas Blender, Timer, or Cardioplegia Module Communication Failure"
issueTitle: "Gas Blender, Timer, or Cardioplegia Module Communication Failure"
description: "Troubleshoots loss of communication with gas blender, timer, or cardioplegia functions by checking module power, cabling, connections, and system configuration."
assetType: "Heart-Lung Machine"
manufacturer: "LivaNova"
model: "S5"
slug: "livanova-s5-gas-blender-timer-or-cardioplegia-module-communication-failure"
dateAdded: "2026-09-15"
taxonomyMode: "reuse"
ccr:
  complaint: "Perfusion reported that the S5 cardioplegia module was not appearing on the system during pre-case setup."
  cause: "Clinical Engineering found the module communication cable partially disconnected after the system had been relocated."
  resolution: "Clinical Engineering reseated and secured the cable and verified stable module communication and normal cardioplegia-system functional checks."
helpfulDetails:
  - "Module affected"
  - "Whether one or multiple modules lost communication"
  - "Exact displayed message"
  - "Module power indicators"
  - "Cable and connector condition"
  - "Whether movement affected communication"
  - "Known-good cable/module substitution"
  - "Configuration observed"
  - "Results after repeated startup"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots loss of communication with gas blender, timer, or cardioplegia functions by checking module power, cabling, connections, and system configuration.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Provide Alternate Clinical Capability

Do not troubleshoot a failed gas-management, timer, or cardioplegia communication function while the patient depends on it. Immediately follow the perfusion contingency plan and provide a verified alternate method for the affected function.

If gas delivery or cardioplegia control itself is unreliable, treat the condition as a clinical equipment failure rather than only a display or communication problem.

**Expected outcome:** The affected clinical function is maintained using reliable alternate equipment or workflow.

Once the module is no longer required for active patient support, troubleshooting may continue.

### 2. Confirm Which Function Has Failed

Identify whether the communication problem affects:

- Gas blender
- Timer
- Cardioplegia module
- Multiple modules simultaneously

Determine whether the module:

- Does not appear at startup.
- Appears and then disappears.
- Operates locally but is not shown by the S5.
- Loses communication when equipment is moved.
- Fails after a configuration change.

Record any displayed message exactly.

**Expected outcome:** The fault is localized to one module or a shared communication path.

If normal communication is restored and remains stable through repeated testing, troubleshooting can stop.

### 3. Verify Module Power and Readiness

Confirm the affected module is powered and completes its normal startup behavior. Inspect obvious power indicators and normal controls.

**Expected outcome:** The module itself is powered and available to communicate.

If restoring external module power resolves communication, troubleshooting can stop after verification.

### 4. Inspect External Communication Connections

With the system out of clinical use, inspect accessible module communication cables and connectors for:

- Loose seating
- Damaged connector housings
- Bent or contaminated contacts visible externally
- Cable strain
- Cuts or crushing
- Fluid intrusion

Reseat approved external connectors.

**Expected outcome:** Communication cabling is securely connected and free of visible damage.

If reseating a connection restores reliable communication, troubleshooting can stop after repeated testing.

### 5. Determine Whether the Failure Is Shared

If multiple modules are affected, inspect common external communication paths, shared connection points, and system-wide power conditions before assuming several modules failed independently.

**Expected outcome:** The failure is identified as module-specific or associated with a shared external path.

If correcting a shared external connection restores all modules, troubleshooting can stop after verification.

### 6. Compare With Known-Good Components

When approved and compatible, substitute a known-good communication cable or module connection one component at a time.

Do not alter device identity or protected network settings without authorization.

**Expected outcome:** The communication loss follows an external cable/module or remains with the original system connection.

If a defective external cable is identified and replaced, troubleshooting can stop after final testing.

### 7. Verify Normal System Configuration

Confirm the installed module is expected in the active S5 configuration and has not been intentionally disabled or removed.

Do not enter restricted service configuration or change protected communication parameters without appropriate authorization.

**Expected outcome:** The installed hardware and normal configuration agree.

If correcting an authorized configuration issue restores module communication, troubleshooting can stop.

### 8. Perform Functional Verification

After communication is restored, verify:

- The module appears consistently.
- Status information updates normally.
- Commands or data expected through the normal interface are exchanged appropriately.
- Communication remains stable during repeated startup.
- No related module alarms remain.

For gas or cardioplegia functions, complete applicable functional checks before clinical use.

**Expected outcome:** Communication and the associated clinical function are stable and repeatable.

If all checks pass, troubleshooting is complete.

### 9. Escalate Persistent Communication Failure

If a module remains unavailable after external power, cabling, connections, and configuration are ruled out, remove the affected equipment from service.

Do not troubleshoot internal communication boards or module electronics at board level.

**Expected outcome:** A system with unresolved loss of a required clinical function is not returned to use.

## If the Problem Persists

Common power, cable, connector, and normal configuration causes have been eliminated. Remaining causes may involve internal module electronics, shared communication hardware, protected configuration, or internal bus faults.

The affected equipment should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate LivaNova documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Before return to service, verify both communication and the complete clinical function of the affected gas, timing, or cardioplegia system.

Knowing when a communication fault has crossed into a service-level problem is proper troubleshooting.

## Clinical Use Tip

Loss of a module display or communication path does not prove that the underlying therapy function is safe; verify the complete functional path before reuse.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Maintain the clinical function with reliable backup equipment first, then separate module power, cabling, shared communication paths, and configuration before assuming internal failure. Verify the complete associated function after communication returns and document the final result clearly.

That is successful troubleshooting.
