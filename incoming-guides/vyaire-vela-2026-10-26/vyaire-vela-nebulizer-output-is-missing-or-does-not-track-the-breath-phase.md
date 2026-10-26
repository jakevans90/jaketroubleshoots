---
schemaVersion: 1
title: "Vyaire VELA Ventilator - Nebulizer Output Is Missing or Does Not Track the Breath Phase"
issueTitle: "Nebulizer Output Is Missing or Does Not Track the Breath Phase"
description: "Addresses absent or incorrectly timed nebulizer output caused by setup, tubing, nebulizer, settings, circuit connection, or ventilator synchronization problems."
assetType: "Ventilator"
manufacturer: "Vyaire"
model: "VELA"
slug: "vyaire-vela-nebulizer-output-is-missing-or-does-not-track-the-breath-phase"
dateAdded: "2026-10-26"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the Vyaire VELA nebulizer would activate but produced no visible aerosol during breaths."
  cause: "Clinical Engineering found the nebulizer supply tubing kinked near the circuit connection."
  resolution: "The tubing was repositioned and inspected, normal breath-synchronized nebulizer output was restored, and ventilation and alarm functions were verified before return to service."
helpfulDetails:
  - "Whether output was absent, weak, continuous, or mistimed."
  - "Ventilation mode when the issue occurred."
  - "Nebulizer type and condition."
  - "Tubing condition and connections."
  - "Circuit configuration and connection point."
  - "Known-good nebulizer substitution result."
  - "Breath triggering or detection behavior."
  - "Leak or circuit abnormalities."
  - "Nebulizer behavior before and after correction."
  - "Final ventilation and alarm verification."
  - "Final device status."
---

## What This Guide Helps With

Addresses absent or incorrectly timed nebulizer output caused by setup, tubing, nebulizer, settings, circuit connection, or ventilator synchronization problems.

## Step-by-Step Troubleshooting

### 1. Maintain Therapy Before Troubleshooting
Do not interrupt required ventilation or medication delivery while troubleshooting the nebulizer function on a patient-connected ventilator.

If medication delivery is clinically necessary, coordinate an approved alternative delivery method and transfer the patient to another verified ventilator if ventilator reliability is in question.

**Expected outcome:** Ventilation and required medication therapy continue safely while the VELA is evaluated separately.

### 2. Confirm the Exact Complaint
Determine whether nebulizer output is completely absent, weak, continuous, intermittent, or present at the wrong point in the respiratory cycle.

Record the selected nebulizer function and the ventilator operating mode when the problem occurs.

**Expected outcome:** The behavior is clearly characterized and reproducible. If normal synchronized operation is observed during controlled testing, complete verification before stopping.

### 3. Verify Nebulizer Setup and Connections
Inspect the nebulizer, connecting tubing, circuit connection point, medication cup or reservoir when applicable, and any required external accessories.

Check for loose tubing, kinked tubing, disconnected fittings, incorrect circuit placement, contamination, or liquid where it should not be.

**Expected outcome:** The nebulizer setup is complete, correctly connected, unobstructed, and positioned appropriately. If correcting the setup restores output, proceed to final verification.

### 4. Inspect the Nebulizer Device
Check the compatible nebulizer for visible damage, cracks, blockage, contamination, incorrect assembly, or signs that it cannot generate aerosol normally.

If the nebulizer uses a disposable component, confirm that the appropriate compatible component is being used.

**Expected outcome:** The nebulizer is correctly assembled and appears serviceable. A damaged or obstructed nebulizer is replaced before further ventilator troubleshooting.

### 5. Substitute a Known-Good Nebulizer and Tubing
Use a known-good compatible nebulizer and connecting tubing when available.

Change only the nebulizer assembly first so the source of the failure can be isolated.

**Expected outcome:** If normal aerosol output and timing return with the known-good setup, the original nebulizer or tubing was the likely cause and ventilator troubleshooting can stop after verification.

### 6. Verify the Nebulizer Function Is Correctly Enabled
Confirm the intended nebulizer function has actually been enabled through normal operator controls and that the current mode or settings support the requested function.

Do not alter restricted service parameters to force nebulizer operation.

**Expected outcome:** The nebulizer function is properly selected for the current test condition. If correcting the selection restores normal output, continue to functional verification.

### 7. Verify Breath Detection and Triggering
If nebulizer output is expected to track a respiratory phase, confirm that the ventilator is correctly detecting or delivering breaths on a test lung.

Look for abnormal triggering, severe auto-triggering, failure to detect patient effort during simulation, major circuit leak, or another condition that could interfere with timing.

**Expected outcome:** Breath delivery and detection are stable and consistent. If correcting an external circuit or triggering problem restores synchronized nebulization, troubleshooting can stop after verification.

### 8. Inspect the Circuit for Leaks or Incorrect Configuration
Check for loose circuit connections, excessive leaks, incorrect accessories, unusual resistance, or components placed incorrectly in the circuit.

A significant circuit problem may affect both ventilator breath detection and nebulizer synchronization.

**Expected outcome:** The test circuit is assembled correctly and demonstrates stable breath delivery without an abnormal leak. If the nebulizer now follows the expected breath phase, proceed to final testing.

### 9. Perform Functional Verification on a Test Lung
Operate the ventilator on an appropriate test lung or simulator. Activate the nebulizer using normal controls and observe whether aerosol output begins, remains stable, and follows the expected breath-related behavior.

Verify that normal ventilation and alarms remain functional during the test.

**Expected outcome:** Nebulizer output is present and behaves consistently with the selected ventilator function. Troubleshooting can stop when operation is repeatable and the ventilator passes required testing.

### 10. Escalate an Unresolved Nebulizer Failure
If the nebulizer, tubing, circuit setup, control selection, and breath detection have been verified but output remains absent or mistimed, remove the ventilator from service.

Do not disassemble internal pneumatic controls, nebulizer valves, timing circuits, or control boards without approved service procedures.

**Expected outcome:** The unresolved ventilator is routed for qualified bench evaluation.

## If the Problem Persists

Common external nebulizer and circuit causes have been ruled out. Remaining possibilities may include an internal nebulizer-control valve, pneumatic source problem, breath-synchronization issue, internal sensing problem, or control-system condition.

The ventilator should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

After repair, verify ventilation, nebulizer operation, timing behavior, alarms, and all required return-to-service functions before clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

If aerosol therapy is required immediately, maintain ventilation and use an approved alternative medication-delivery method rather than delaying therapy to troubleshoot the ventilator.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Nebulizer complaints often originate in the nebulizer, tubing, circuit, or breath-detection conditions rather than an internal ventilator fault. Protect therapy first, isolate each external variable logically, verify synchronized operation, and escalate when the ventilator itself remains unable to provide reliable nebulization.

That is successful troubleshooting.
