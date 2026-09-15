---
schemaVersion: 1
title: "LivaNova S5 Heart-Lung Machine - Roller Pump Will Not Run or Speed Is Unstable"
issueTitle: "Roller Pump Will Not Run or Speed Is Unstable"
description: "Troubleshoots a roller pump that will not start or maintain stable speed, emphasizing controls, tubing setup, connections, and safe external checks."
assetType: "Heart-Lung Machine"
manufacturer: "LivaNova"
model: "S5"
slug: "livanova-s5-roller-pump-will-not-run-or-speed-is-unstable"
dateAdded: "2026-09-15"
taxonomyMode: "reuse"
ccr:
  complaint: "Perfusion reported that an S5 roller pump speed fluctuated during pre-case setup."
  cause: "Clinical Engineering found the pump tubing twisted where it entered the roller head, creating uneven mechanical loading."
  resolution: "Clinical Engineering corrected the tubing routing and verified smooth, stable pump operation through repeated speed changes during bench testing."
helpfulDetails:
  - "Pump channel affected"
  - "Whether the pump started"
  - "Displayed versus observed speed behavior"
  - "Tubing type and condition"
  - "Tubing position in the pump head"
  - "Noise or vibration"
  - "External cable condition"
  - "Known-good comparison results"
  - "Whether instability occurred only under load"
  - "Final functional test result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots a roller pump that will not start or maintain stable speed, emphasizing controls, tubing setup, connections, and safe external checks.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Perfusion

Do not troubleshoot an unreliable roller pump while it is supporting a patient. If the condition develops during bypass, immediately follow the perfusion contingency plan and transition flow to a verified alternate pumping method or backup system.

Stop using any pump exhibiting uncontrolled speed, unexpected starts or stops, severe mechanical noise, smoke, odor, or visible damage.

**Expected outcome:** Patient circulation is supported by reliable equipment before technical troubleshooting begins.

Once the affected pump is isolated from patient support, troubleshooting may continue.

### 2. Confirm the Reported Pump Behavior

Determine whether the pump:

- Does not start.
- Starts but immediately stops.
- Runs intermittently.
- Displays changing speed while mechanically stable.
- Physically surges or varies speed.
- Responds inconsistently to its control.
- Fails only under tubing load.

Record any system message or alarm exactly.

**Expected outcome:** The failure is clearly characterized as command, display, load-related, or actual mechanical speed instability.

If the pump operates normally during controlled reproduction and remains stable through verification, troubleshooting can stop.

### 3. Inspect the Pump Head and Tubing Setup

With the pump stopped and removed from clinical use, inspect the accessible pump head and tubing path. Verify:

- Correct compatible tubing is being used.
- Tubing is seated correctly.
- Tubing is not twisted, kinked, flattened, or excessively stretched.
- No foreign material is interfering with roller movement.
- The pump head area is clean and unobstructed.

Do not adjust occlusion beyond authorized procedures.

**Expected outcome:** The pump head rotates freely through its normal accessible range and the tubing is properly positioned.

If correcting tubing placement restores smooth, stable operation, troubleshooting can stop after final verification.

### 4. Verify Pump Controls

Confirm the pump's normal operating controls are enabled and positioned correctly. Check for:

- Stop or standby state
- Speed control position
- Direction selection when applicable
- Any externally accessible emergency or safety control that may inhibit operation

Do not bypass safety interlocks.

**Expected outcome:** The pump is commanded to run using normal controls and no external control state is preventing operation.

If correcting a control setting restores normal speed control, troubleshooting can stop after verification.

### 5. Inspect External Connections

Inspect accessible cables and connectors associated with the pump module for looseness, damage, contamination, or strain. Reseat approved external connectors with the system safely out of clinical use.

**Expected outcome:** Pump power and communication connections are secure and undamaged.

If reseating an external connection restores reliable operation, troubleshooting can stop after repeated functional testing.

### 6. Compare With a Known-Good Setup

When permitted, test the pump using a known-good compatible tubing setup or compare the suspect pump channel with another functioning S5 roller pump under controlled bench conditions.

Do not use patient circuits for troubleshooting.

**Expected outcome:** The problem is shown to follow the tubing/accessory setup or remain with the pump assembly.

If an external setup issue is identified and corrected, troubleshooting can stop once performance is verified.

### 7. Observe Operation Without Excessive Load

Using approved test conditions, command the pump through a reasonable operating range and observe whether rotation is smooth and responsive.

Stop testing immediately if there is:

- Grinding
- Binding
- Irregular rotation
- Sudden speed change
- Excessive vibration
- Burning odor
- Unexpected shutdown

**Expected outcome:** The pump responds smoothly and consistently to speed commands without abnormal sound or vibration.

If operation remains stable through the controlled test, proceed to final verification.

### 8. Perform Final Functional Verification

Verify:

- Pump starts and stops correctly.
- Speed control changes are predictable.
- Displayed speed is stable.
- Mechanical rotation appears consistent.
- Tubing remains properly retained.
- Relevant alarms or safety functions are available.

Complete required return-to-service testing before clinical use.

**Expected outcome:** Roller pump operation is stable, controllable, and repeatable.

If all checks pass, troubleshooting is complete.

### 9. Escalate Persistent Pump Instability

If the pump will not run, speed remains unstable, or abnormal mechanical behavior persists after external setup, controls, and connections are ruled out, remove it from service.

Do not disassemble the drive mechanism, motor, encoder, control electronics, or internal pump assembly without authorized service procedures.

**Expected outcome:** An unreliable pump is prevented from returning to patient use.

## If the Problem Persists

Common tubing, control, connection, and external load causes have been ruled out. Remaining causes may involve the pump drive mechanism, internal speed sensing, motor control, internal communication, or protected configuration.

The affected S5 pump/system should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate LivaNova documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Return-to-service testing should confirm stable pump control, correct direction, alarm function, and reliable operation before clinical release.

Knowing when to stop external troubleshooting is especially important when pump speed cannot be trusted.

## Clinical Use Tip

Any unexplained roller-pump speed change during bypass requires immediate transition to the established perfusion backup method rather than continued troubleshooting on the patient.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Maintain perfusion with reliable equipment first, then work from tubing placement and controls through connections and controlled comparison testing. Never assume an internal drive failure before external loading conditions are eliminated, and never return an unstable pump to clinical use without verification and clear documentation.

That is successful troubleshooting.
