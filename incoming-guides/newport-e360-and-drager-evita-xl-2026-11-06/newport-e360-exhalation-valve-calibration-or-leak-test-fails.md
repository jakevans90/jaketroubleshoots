---
schemaVersion: 1
title: "Newport e360 Ventilator - Exhalation Valve Calibration or Leak Test Fails"
issueTitle: "Exhalation Valve Calibration or Leak Test Fails"
description: "Addresses failed exhalation-valve calibration or circuit leak testing caused by circuit setup, valve assembly, connections, accessories, or external leakage."
assetType: "Ventilator"
manufacturer: "Newport"
model: "e360"
slug: "newport-e360-exhalation-valve-calibration-or-leak-test-fails"
dateAdded: "2026-11-06"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Newport e360 repeatedly failed the exhalation valve calibration during setup."
  cause: "Clinical Engineering found the removable exhalation valve assembly was not fully seated, preventing the circuit from sealing correctly."
  resolution: "The valve assembly was correctly reseated, the calibration and leak test passed, and ventilation and alarm functions were successfully verified with a test lung."
helpfulDetails:
  - "Exact calibration or leak-test message"
  - "Circuit configuration used"
  - "Exhalation valve condition"
  - "Presence of moisture or contamination"
  - "Air and oxygen supply status"
  - "Known-good circuit or valve substitutions"
  - "Results before and after correction"
  - "Final functional-test results"
  - "Final device status"
---

## What This Guide Helps With

Addresses failed exhalation-valve calibration or circuit leak testing caused by circuit setup, valve assembly, connections, accessories, or external leakage.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Confirm the Reported Failure
Do not troubleshoot the ventilator while a patient depends on unreliable ventilation. Move the patient to another verified ventilator or appropriate backup ventilation method before testing.

Confirm whether the reported problem is an exhalation-valve calibration failure, circuit leak-test failure, or both. Record any displayed message exactly as shown.

**Expected outcome:** The patient is safely supported elsewhere and the exact failed test or symptom is identified. If the problem cannot be reproduced and all required checks pass, troubleshooting can stop after final verification.

### 2. Inspect the Breathing Circuit for Obvious Leaks
Inspect the inspiratory and expiratory limbs, connectors, humidification components, test lung, caps, adapters, and sampling connections. Look for loose fittings, cracks, improperly seated components, or open ports.

Verify that the circuit configuration matches the intended test setup.

**Expected outcome:** The circuit is complete, correctly connected, and visibly free of leakage. If correcting a loose or open connection allows the test to pass consistently, the issue is resolved and troubleshooting can stop after functional verification.

### 3. Inspect the Exhalation Valve Assembly
Remove the ventilator from clinical use and inspect the externally accessible exhalation valve components according to approved handling procedures. Confirm that the assembly is correctly installed, fully seated, clean, dry, and free of visible damage or contamination.

Do not disassemble internal pneumatic components beyond authorized service procedures.

**Expected outcome:** The exhalation valve is correctly installed and unobstructed. If reseating or replacing an approved removable valve component restores successful calibration, troubleshooting can stop after verification.

### 4. Check for Moisture or Contamination
Inspect the expiratory circuit and exhalation valve area for condensate, secretions, cleaning residue, or other material that could prevent proper valve movement or sealing.

Replace contaminated or questionable disposable components rather than attempting unauthorized repair.

**Expected outcome:** The gas path and valve components are clean and dry. If removing moisture or replacing a contaminated component restores the test, the problem is resolved.

### 5. Substitute a Known-Good Circuit or Valve Assembly
When available, install a compatible known-good breathing circuit and externally replaceable exhalation valve assembly.

Repeat the applicable calibration or leak check.

**Expected outcome:** A known-good setup passes testing. If the original accessory causes the failure and the replacement passes repeatedly, replace the defective accessory and stop troubleshooting after final verification.

### 6. Verify Gas Supply and Basic Ventilator Operation
Confirm that required air and oxygen supplies are connected, secure, and available to the ventilator. Verify normal startup and absence of unrelated supply or pressure alarms.

**Expected outcome:** The ventilator has stable required gas supplies and operates normally aside from the reported issue. Correcting an external gas-supply problem that restores calibration resolves the issue.

### 7. Repeat the Calibration or Leak Test
Using the correct external setup, repeat the required calibration or pre-use test. Do not bypass a failed test or alter unauthorized configuration parameters to force a pass.

**Expected outcome:** The ventilator completes the test successfully and consistently. If it does, proceed to final functional verification.

### 8. Perform Final Functional Verification
Connect an appropriate test lung and verify basic ventilation, exhalation, pressure behavior, volume response, and applicable alarms using approved test equipment and procedures.

**Expected outcome:** Ventilation and alarms function normally with no abnormal leakage or calibration failure. The ventilator may be returned to service only after required testing is successfully completed.

### 9. Escalate if the Failure Remains
If known-good external components and correct setup do not resolve the problem, stop external troubleshooting.

**Expected outcome:** The ventilator is removed from service for manufacturer-directed evaluation rather than being returned to clinical use with an unresolved calibration or leak-test failure.

## If the Problem Persists

Common external causes such as circuit leakage, incorrect assembly, moisture, accessory failure, and gas-supply problems have been ruled out. The remaining cause may involve internal pneumatic control, valve actuation, pressure or flow sensing, calibration, or another service-level fault.

Remove the ventilator from service, label it **Out of Service**, and send it for bench evaluation. Use appropriate Newport manufacturer documentation and approved test equipment. Internal repair or configuration changes should be performed only by qualified personnel.

Do not return the ventilator to service until the required calibration, leak testing, ventilation verification, and alarm testing have passed. Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A ventilator that cannot reliably control exhalation or pass its required leak check should never remain connected to a patient while troubleshooting continues.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient first, verify the external breathing circuit and exhalation components before suspecting internal failure, confirm the repair through functional testing, escalate unresolved failures appropriately, and clearly document what was found and corrected.

That is successful troubleshooting.
