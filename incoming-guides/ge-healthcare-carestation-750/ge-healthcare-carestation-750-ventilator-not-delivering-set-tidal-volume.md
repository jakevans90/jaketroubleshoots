---
schemaVersion: 1
title: "GE Healthcare Carestation 750 Anesthesia Machine - Ventilator Not Delivering Set Tidal Volume"
issueTitle: "Ventilator Not Delivering Set Tidal Volume"
description: "Delivered tidal volume differs from the set value because of circuit leaks, compliance, flow measurement, settings, accessories, or gas-delivery problems."
assetType: "Anesthesia Machine"
manufacturer: "GE Healthcare"
model: "Carestation 750"
slug: "ge-healthcare-carestation-750-ventilator-not-delivering-set-tidal-volume"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Anesthesia staff reported that the Carestation 750 was delivering substantially less tidal volume than the selected setting during setup."
  cause: "Clinical Engineering found a cracked breathing-circuit hose causing significant volume loss during ventilation."
  resolution: "The circuit was replaced, ventilation was tested with a test lung, expected volume delivery was restored, and system checkout passed."
helpfulDetails:
  - "Ventilation mode"
  - "Set and measured volumes"
  - "Inspired versus expired volume"
  - "Airway pressure behavior"
  - "Circuit and filter condition"
  - "Leak-test results"
  - "Flow calibration result"
  - "Gas supply status"
  - "Known-good substitutions"
  - "Test-lung or analyzer findings"
  - "Final checkout result"
  - "Final device status"
---

## What This Guide Helps With
Delivered tidal volume differs from the set value because of circuit leaks, compliance, flow measurement, settings, accessories, or gas-delivery problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Ventilation
Do not troubleshoot unreliable ventilation while a patient depends on the affected machine. If inadequate ventilation is suspected during a case, immediately provide appropriate alternate ventilation and follow clinical escalation procedures.

Remove the Carestation 750 from service if reliable ventilation cannot be confirmed.

**Expected outcome:** The patient is supported by a verified ventilation method and the anesthesia machine can be evaluated safely.

### 2. Confirm the Reported Volume Discrepancy
Record:

- Selected ventilation mode
- Set tidal volume when applicable
- Displayed inspired and expired volumes
- Airway pressure behavior
- Whether the condition occurs continuously or intermittently
- Any associated alarms

Test the machine with an appropriate test lung or approved analyzer rather than a patient.

**Expected outcome:** The volume discrepancy is reproduced under controlled conditions. If delivered volume is appropriate during testing and no fault can be reproduced, investigate the original setup and document findings.

### 3. Inspect the Breathing Circuit for Leaks
Check all circuit connections, patient wye, reservoir bag, filters, sampling adapters, and other accessories for looseness, cracks, open ports, or damage.

Reseat accessible connections and replace visibly damaged disposable components.

**Expected outcome:** The circuit is intact and leak-free externally. If correcting a leak restores expected volume delivery, troubleshooting can stop after final verification.

### 4. Verify the Breathing System Is Properly Assembled
Check that externally removable breathing-system components are correctly installed and fully seated.

Inspect accessible seals and connections without deep disassembly.

**Expected outcome:** The breathing system is properly assembled. Correcting an improperly seated component that restores volume delivery resolves the issue.

### 5. Check Ventilation Settings and Patient/Test-Lung Conditions
Verify the selected ventilation mode and all relevant settings are appropriate for the intended test.

Confirm that pressure limits, PEEP, rate, inspiratory settings, or other accessible controls are not restricting delivery.

**Expected outcome:** Settings are appropriate and do not explain the reduced tidal volume. If an incorrect setting is corrected and expected ventilation returns, troubleshooting can stop.

### 6. Inspect External Circuit Resistance and Compliance
Look for:

- Kinked tubing
- Occluded filters
- Water accumulation
- Excessively complex accessory setups
- Compressed or obstructed breathing hoses

Replace questionable components with compatible known-good items.

**Expected outcome:** The circuit presents no obvious abnormal resistance or leak. If replacing an accessory restores expected volume, the external cause is confirmed.

### 7. Evaluate Flow Measurement
Observe whether inspired and expired volume readings appear stable and plausible during controlled ventilation.

If the Carestation 750 provides an approved flow-sensor calibration or checkout procedure accessible to Clinical Engineering, perform it according to manufacturer documentation.

**Expected outcome:** Flow measurement is stable and calibration completes successfully. If calibration restores normal volume delivery and verification passes, troubleshooting can stop.

### 8. Verify Gas Supply Availability
Confirm required gas sources are properly connected and that there are no concurrent supply warnings or obvious hose problems.

Do not assume the ventilator itself has failed until external gas availability is verified.

**Expected outcome:** Gas supplies are available and stable. Correcting an external supply issue that restores ventilation resolves the problem.

### 9. Test With Known-Good External Components
Use a compatible known-good circuit, test lung, filter, and other easily substituted accessories to isolate the anesthesia machine from questionable external components.

**Expected outcome:** If normal tidal volume returns with known-good components, replace the defective external item. If the discrepancy remains, proceed to escalation.

### 10. Perform Final Ventilation Verification
After correction, test the Carestation 750 with an appropriate breathing-system analyzer or test lung.

Verify delivered volume, pressure behavior, alarms, breathing-system integrity, and the relevant checkout functions before clinical use.

**Expected outcome:** Ventilation is stable and consistent with the configured test conditions. Troubleshooting can stop when all required checks pass.

### 11. Escalate Persistent Volume-Delivery Problems
If the problem continues after circuits, settings, accessories, sensors, and gas sources have been checked, stop external troubleshooting.

**Expected outcome:** The machine is removed from clinical use for qualified service evaluation.

## If the Problem Persists
Common external causes have been ruled out. Possible remaining categories include internal flow measurement, ventilator control, pneumatic delivery, valve function, breathing-system interfaces, or configuration requiring manufacturer-level evaluation.

The Carestation 750 should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired or configured only by qualified personnel

After repair, complete appropriate ventilation-performance, leak, alarm, gas-delivery, and return-to-service testing.

Stopping when reliable ventilation cannot be verified is proper troubleshooting.

## Clinical Use Tip
A displayed volume should never be accepted as proof of adequate ventilation without confirming the complete breathing system and patient ventilation clinically.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Protect ventilation first and verify the complete external breathing path before suspecting internal ventilator failure. Work logically through leaks, settings, resistance, measurement, and gas availability, then verify performance with appropriate test equipment and document the outcome.

That is successful troubleshooting.
