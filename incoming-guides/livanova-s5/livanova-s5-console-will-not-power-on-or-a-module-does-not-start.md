---
schemaVersion: 1
title: "LivaNova S5 Heart-Lung Machine - Console Will Not Power On or a Module Does Not Start"
issueTitle: "Console Will Not Power On or a Module Does Not Start"
description: "Troubleshoots loss of console power or a module that fails to initialize, focusing on external power, connections, configuration, and safe substitution."
assetType: "Heart-Lung Machine"
manufacturer: "LivaNova"
model: "S5"
slug: "livanova-s5-console-will-not-power-on-or-a-module-does-not-start"
dateAdded: "2026-09-15"
taxonomyMode: "reuse"
ccr:
  complaint: "Perfusion reported that the LivaNova S5 console powered on but one installed module did not start."
  cause: "Clinical Engineering found the affected module's external connection partially seated after the console had been moved."
  resolution: "Clinical Engineering reseated and secured the connection, completed repeated startup and functional checks, and verified the module initialized normally."
helpfulDetails:
  - "Entire console or specific module affected"
  - "AC receptacle tested"
  - "Power cord and connector condition"
  - "Indicators observed during startup"
  - "Any displayed message"
  - "Whether the system had recently been moved or reconfigured"
  - "Known-good cable or module substitutions"
  - "AC versus battery-supported behavior"
  - "Results of repeated startups"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots loss of console power or a module that fails to initialize, focusing on external power, connections, configuration, and safe substitution.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Perfusion Capability

Do not troubleshoot an S5 console or module while a patient depends on the affected function. If the problem occurs during a case, immediately follow the facility perfusion contingency plan and transfer the affected function to verified backup equipment.

If there is smoke, unusual odor, excessive heat, liquid intrusion, arcing, or visible electrical damage, disconnect the equipment from power when clinically safe and remove it from service.

**Expected outcome:** Patient support is maintained independently of the malfunctioning console or module.

If clinical support has been safely transferred and the affected equipment is no longer required for patient care, troubleshooting may continue.

### 2. Confirm the Exact Power or Startup Failure

Identify whether:

- The entire console is unpowered.
- Some modules start while one module remains inactive.
- The system begins startup but stops before normal operation.
- Indicators illuminate briefly and then extinguish.
- The failure follows movement, cleaning, reconfiguration, or connection of another component.

Record any displayed message or abnormal indicator exactly as shown.

**Expected outcome:** The failure is isolated to the complete console, a specific module, or the startup sequence.

If the system starts normally after confirming the reported condition and remains stable through functional verification, troubleshooting can stop.

### 3. Verify Facility AC Power

Inspect the power cord, plug, strain relief, and accessible power connections for damage or looseness. Confirm the device is connected to an appropriate powered receptacle and verify the receptacle using approved test equipment or a known-good facility power source.

Avoid using unapproved extension cords or adapters.

**Expected outcome:** Stable facility power is available and the external power path is intact.

If restoring a loose or unavailable AC source returns the system to normal operation and verification passes, troubleshooting can stop.

### 4. Inspect External Power and Module Connections

With the system safely removed from clinical use, inspect accessible console and module connections. Look for:

- Partially seated connectors
- Bent or damaged connector shells
- Contamination
- Pin damage visible without disassembly
- Loose retaining hardware
- Cable strain or crushing

Reseat only user-accessible or service-approved external connections.

**Expected outcome:** All required external connections are secure, clean, and undamaged.

If reseating an external connection restores normal startup and repeated power cycles are successful, troubleshooting can stop.

### 5. Isolate the Affected Module

Determine whether the startup problem remains associated with one module, cable, or console position. When permitted by approved procedures, compare operation using a known-good compatible module, cable, or connection point.

Do not interchange components unless compatibility is established.

**Expected outcome:** The problem either follows the suspect external component or remains with the console/module position.

If a known-good substitution identifies a defective external component and the system operates normally after replacement, troubleshooting can stop after final verification.

### 6. Check Controls and System Configuration

Verify that externally accessible power controls, module enable states, and normal clinical configuration are appropriate. Confirm no component has been intentionally disabled, disconnected, or removed from the configured system.

Do not enter restricted service menus or alter protected configuration parameters without authorization.

**Expected outcome:** The system is configured for the installed modules and no obvious control or configuration condition prevents startup.

If correcting an authorized configuration issue restores normal startup, troubleshooting can stop after verification.

### 7. Evaluate Battery-Supported Startup Behavior

If the system incorporates battery-backed operation, compare behavior on verified AC power and battery-supported operation as permitted by approved procedures. Note whether the problem occurs only during one power source condition.

Do not intentionally deplete backup power needed for clinical readiness.

**Expected outcome:** The console and installed modules behave consistently on the available approved power sources.

If the failure is isolated to an external power source or replaceable approved battery component and correction restores normal operation, troubleshooting can stop.

### 8. Perform Final Functional Verification

After correction, power-cycle the system according to normal operating procedures and verify:

- Console startup completes.
- Required modules initialize.
- Displays and indicators operate.
- No unexpected alarms or communication failures remain.
- Pumps and monitoring modules required for clinical use respond appropriately during a controlled test.

Complete applicable return-to-service testing before releasing the system.

**Expected outcome:** The S5 completes startup reliably and all required modules are available and stable.

If all checks pass, troubleshooting is complete.

### 9. Escalate an Unresolved Startup Failure

If the console remains unpowered, startup repeatedly fails, or a module remains unavailable after external causes are ruled out, stop troubleshooting.

Do not proceed into internal power supplies, backplanes, circuit boards, or internal communication hardware unless specifically authorized and trained for manufacturer-level service.

**Expected outcome:** The device remains controlled and unavailable for clinical use until qualified service evaluation is completed.

## If the Problem Persists

Common external power, connection, configuration, and interchangeable accessory causes have been ruled out. The remaining possibilities may involve internal power distribution, module electronics, internal communications, protected configuration, or another service-level fault.

The affected S5 system should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate LivaNova documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

After service, complete applicable electrical safety, operational, alarm, module communication, and functional testing before returning the system to clinical use.

Knowing when to stop external troubleshooting and escalate a heart-lung machine fault is proper troubleshooting.

## Clinical Use Tip

A partially functional heart-lung machine should not be considered clinically ready; verify every required perfusion function before the system is assigned to a case.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient first, then isolate the failure logically from facility power through external connections, modules, and configuration before suspecting internal electronics. Verify the complete system after correction, escalate unresolved faults appropriately, and document the complaint, cause, and resolution clearly.

That is successful troubleshooting.
