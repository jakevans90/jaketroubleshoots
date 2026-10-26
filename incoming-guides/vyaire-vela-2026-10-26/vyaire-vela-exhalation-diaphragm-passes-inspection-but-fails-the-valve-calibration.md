---
schemaVersion: 1
title: "Vyaire VELA Ventilator - Exhalation Diaphragm Passes Inspection but Fails the Valve Calibration"
issueTitle: "Exhalation Diaphragm Passes Inspection but Fails the Valve Calibration"
description: "Addresses repeated exhalation-valve calibration failure when the diaphragm appears intact, including assembly, seating, circuit, connection, contamination, and configuration causes."
assetType: "Ventilator"
manufacturer: "Vyaire"
model: "VELA"
slug: "vyaire-vela-exhalation-diaphragm-passes-inspection-but-fails-the-valve-calibration"
dateAdded: "2026-10-26"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the Vyaire VELA repeatedly failed exhalation-valve calibration even though the diaphragm appeared intact."
  cause: "Clinical Engineering found the exhalation diaphragm was not fully seated in the valve assembly, preventing consistent calibration."
  resolution: "The diaphragm was correctly reseated, calibration completed successfully, and the ventilator passed functional and alarm verification before return to service."
helpfulDetails:
  - "Exact calibration message or failure point."
  - "Condition and orientation of the exhalation diaphragm."
  - "Exhalation assembly condition."
  - "Presence of moisture or contamination."
  - "Circuit configuration used during testing."
  - "External pneumatic connections inspected."
  - "Known-good diaphragm or assembly substitution."
  - "Related pressure, flow, or leak abnormalities."
  - "Calibration result before and after correction."
  - "Final functional and alarm test results."
  - "Final device status."
---

## What This Guide Helps With

Addresses repeated exhalation-valve calibration failure when the diaphragm appears intact, including assembly, seating, circuit, connection, contamination, and configuration causes.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Remove the Ventilator From Active Therapy
Do not troubleshoot an unreliable exhalation valve or calibration condition while a patient depends on the ventilator. Transfer ventilation to another verified device or approved backup method before proceeding.

Label or isolate the VELA from clinical use until the calibration issue is understood and final verification is completed.

**Expected outcome:** The patient is safely supported independently of the affected ventilator.

### 2. Confirm the Exact Calibration Failure
Repeat only the normal operator-accessible calibration or pre-use procedure required to reproduce the complaint. Record the displayed message, the point in the calibration where it fails, and whether the failure is consistent.

Do not repeatedly run calibration while changing multiple variables at once.

**Expected outcome:** The failure is confirmed and documented consistently. If calibration now completes normally and remains repeatable, continue with final functional verification before stopping.

### 3. Inspect the Exhalation Diaphragm and Valve Assembly Again
Remove the exhalation assembly according to normal approved handling procedures. Inspect the diaphragm for contamination, moisture, distortion, improper orientation, edge damage, sticking, or incomplete seating.

Inspect the mating surfaces and accessible valve components for debris or residue that could prevent free movement or sealing even when the diaphragm itself appears visually acceptable.

Reinstall the assembly carefully and confirm it is fully seated and secured.

**Expected outcome:** The diaphragm and exhalation assembly are clean, correctly oriented, undamaged, and properly seated. If reseating corrects the calibration failure, complete functional verification and troubleshooting can stop.

### 4. Check the Patient Circuit and External Pneumatic Connections
Inspect the breathing circuit configuration used during calibration. Look for loose connections, occluded tubing, water accumulation, damaged tubing, incorrect components, or an accessory that may interfere with expected flow or pressure.

Verify all external pneumatic connections required for the test are firmly connected.

**Expected outcome:** The circuit and external pneumatic path are correctly assembled, unobstructed, dry where appropriate, and leak-free. If correcting the circuit allows calibration to pass, proceed to final verification.

### 5. Substitute Known-Good External Components
When permitted by facility procedure, repeat the calibration using a known-good compatible exhalation diaphragm or complete approved exhalation assembly.

If the test setup includes a reusable circuit or test accessory, substitute a known-good compatible setup as well.

Change one item at a time so the cause can be identified.

**Expected outcome:** Calibration either passes with the known-good component, identifying the removed component as the likely cause, or continues to fail and points away from the external assembly.

### 6. Verify Ventilator Configuration and Test Conditions
Confirm the ventilator is in the correct operating state for the calibration and that no inappropriate circuit, mode, accessory, or configuration selection is affecting the test.

Do not enter restricted service menus or alter calibration constants without approved manufacturer documentation and authorization.

**Expected outcome:** The ventilator configuration and test conditions are appropriate for the calibration. If correcting a configuration issue restores successful calibration, continue with functional testing.

### 7. Check for Related Flow, Pressure, or Leak Symptoms
Observe whether other approved startup or functional checks indicate abnormal flow measurement, pressure behavior, leakage, or exhalation-valve operation.

A calibration failure accompanied by additional pneumatic abnormalities should not be treated as an isolated diaphragm problem.

**Expected outcome:** No additional abnormal pneumatic behavior is present. If related abnormalities are found, remove the ventilator from service and escalate rather than continuing external troubleshooting.

### 8. Perform Final Functional Verification
After any correction, repeat the applicable exhalation-valve calibration and normal pre-use verification using appropriate test equipment and facility procedures.

Verify stable ventilation, expected exhalation-valve behavior, appropriate pressure and flow response, and alarm functionality before return to service.

**Expected outcome:** Calibration completes successfully and the ventilator passes required functional testing. Troubleshooting can stop and the device may be returned to service according to facility policy.

### 9. Escalate an Unresolved Calibration Failure
If the diaphragm, exhalation assembly, breathing circuit, connections, and configuration have been ruled out and calibration still fails, stop external troubleshooting.

Do not proceed into internal pneumatic components, valve actuators, internal sensors, control electronics, or board-level repair without authorized service procedures.

**Expected outcome:** The unresolved ventilator is removed from service and routed for qualified bench evaluation.

## If the Problem Persists

Common external causes have been ruled out. The remaining possibilities may include an internal exhalation-valve control problem, pneumatic leak, pressure or flow sensing problem, calibration-control issue, or other service-level condition.

The ventilator should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Repaired, calibrated, or configured only by qualified personnel.

After service, complete all required calibration, operational, alarm, pneumatic, and return-to-service testing before clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A ventilator that cannot reliably complete its exhalation-valve calibration should never be placed on a patient even if the diaphragm looks normal.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient first, then work from the exhalation assembly and circuit inward. A visually acceptable diaphragm does not eliminate seating, sealing, connection, or configuration problems. Verify the correction before assuming an internal failure, escalate appropriately when calibration remains unsuccessful, and document exactly what was found and tested.

That is successful troubleshooting.
