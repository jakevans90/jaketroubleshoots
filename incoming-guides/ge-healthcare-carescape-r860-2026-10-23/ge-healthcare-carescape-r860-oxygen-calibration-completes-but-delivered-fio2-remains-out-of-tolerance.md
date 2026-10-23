---
schemaVersion: 1
title: "GE Healthcare CARESCAPE R860 Ventilator - Oxygen Calibration Completes but Delivered FiO2 Remains Out of Tolerance"
issueTitle: "Oxygen Calibration Completes but Delivered FiO2 Remains Out of Tolerance"
description: "Addresses incorrect delivered FiO2 after successful calibration, including gas supply, sensor, circuit, accessory, configuration, and environmental causes."
assetType: "Ventilator"
manufacturer: "GE Healthcare"
model: "CARESCAPE R860"
slug: "ge-healthcare-carescape-r860-oxygen-calibration-completes-but-delivered-fio2-remains-out-of-tolerance"
dateAdded: "2026-10-23"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the CARESCAPE R860 completed oxygen calibration but independent testing showed delivered FiO2 did not match the selected setting."
  cause: "Clinical Engineering found the oxygen supply hose was not fully seated, causing unstable gas delivery during functional testing."
  resolution: "The hose connection was corrected and the ventilator was retested with approved equipment, confirming stable ventilation and accurate oxygen delivery before return to service."
helpfulDetails:
  - "Selected and measured FiO2"
  - "Independent analyzer reading"
  - "Oxygen and air source used"
  - "Gas hose and connector condition"
  - "Circuit and accessory configuration"
  - "Test lung used"
  - "Calibration result"
  - "Known-good substitutions performed"
  - "Whether the issue followed the device or the gas source"
  - "Results at multiple FiO2 settings"
  - "Final functional-test results"
  - "Final device status"
---

## What This Guide Helps With

Addresses incorrect delivered FiO2 after successful calibration, including gas supply, sensor, circuit, accessory, configuration, and environmental causes.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Ventilation
Do not troubleshoot an unreliable oxygen-delivery condition while a patient depends on the ventilator. Transfer the patient to another verified ventilator or establish an appropriate alternate ventilation method before continuing.

Label or isolate the CARESCAPE R860 if delivered oxygen concentration cannot be trusted.

**Expected outcome:** The patient is safely supported by alternate equipment and the suspect ventilator is available for controlled evaluation. If patient safety and reliable ventilation are restored using another device, proceed with bench troubleshooting only.

### 2. Confirm the Exact Reported Condition
Determine how the FiO2 discrepancy was identified. Record the commanded oxygen setting, displayed measured value, independent analyzer result if available, operating mode, and whether the discrepancy occurs continuously or only at specific settings.

Repeat the condition using an approved test lung and appropriate oxygen-analysis equipment rather than relying solely on the ventilator display.

**Expected outcome:** The reported FiO2 error is either reproduced under controlled conditions or cannot be reproduced. If independent testing confirms acceptable oxygen delivery across the required operating checks, document the result and stop troubleshooting.

### 3. Verify Medical Gas Sources
Confirm that oxygen and air supplies are properly connected, fully seated, undamaged, and connected to the correct source.

Inspect external hoses and fittings for kinks, damaged connectors, contamination, loose fittings, or evidence of leakage. Verify the facility gas source is available and suitable using approved methods.

If cylinders are being used, confirm they contain adequate pressure and are correctly connected.

**Expected outcome:** Required gas sources are available, correctly connected, and stable. If correcting a loose, restricted, depleted, or incorrect supply restores accurate FiO2, verify operation and stop troubleshooting.

### 4. Check for Cross-Connection or Source Problems
Confirm oxygen and air hoses have not been reversed and that wall outlets, regulators, or supply manifolds correspond to the intended gas.

When practical, compare operation using another verified gas outlet or approved supply source to help isolate the ventilator from the facility infrastructure.

**Expected outcome:** Gas identity and source integrity are confirmed. If changing to a verified supply restores correct oxygen delivery, address the external gas-source issue and stop ventilator troubleshooting.

### 5. Inspect the Patient Circuit and External Accessories
Inspect the breathing circuit, humidifier arrangement, filters, adapters, nebulizer components, test lung connections, and other inline accessories.

Look for leaks, incorrect assembly, excessive resistance, damaged tubing, loose connections, or an accessory installed in a way that may affect gas delivery or analyzer sampling.

Replace questionable disposable components with known-good compatible components when appropriate.

**Expected outcome:** The circuit and accessories are intact and correctly assembled. If replacing or repositioning an external component restores accurate FiO2, complete functional verification and stop troubleshooting.

### 6. Verify Oxygen Measurement Method
Inspect the independent oxygen analyzer and its sampling setup before concluding that the ventilator is inaccurate.

Confirm the analyzer is suitable for the test, has been prepared according to its approved procedure, and is sampling from an appropriate location without leaks or dilution from ambient air.

Compare with a second known-good analyzer when available.

**Expected outcome:** The independent measurement method is verified. If the discrepancy is traced to the analyzer or sampling arrangement, correct the test setup and stop troubleshooting once ventilator performance is confirmed.

### 7. Review Ventilator Settings and Configuration
Verify the intended FiO2 setting and any relevant ventilation configuration without entering restricted service menus or changing unauthorized parameters.

Confirm the observed value is not being affected by a temporary operating condition, recent setting change, startup sequence, or test configuration.

**Expected outcome:** The ventilator is configured as intended and the test is being performed under stable conditions. If correcting a setting or test condition resolves the discrepancy, verify operation and stop troubleshooting.

### 8. Repeat Approved Oxygen Calibration
If appropriate and within Clinical Engineering authorization, repeat the oxygen calibration using the manufacturer-approved procedure and required test setup.

Do not interpret a successful calibration message as proof that delivered oxygen is accurate. Calibration must be followed by independent functional verification.

**Expected outcome:** Calibration completes normally and independent measurement confirms acceptable delivered oxygen. If accuracy is restored, complete final verification and stop troubleshooting.

### 9. Compare Multiple FiO2 Settings
Using approved test equipment and a test lung, verify oxygen delivery at multiple clinically relevant settings rather than checking only one point.

Observe whether the discrepancy is constant, increases at higher oxygen settings, appears only after warm-up, or changes with gas-source substitution.

Do not attempt internal adjustment or component-level repair based on the pattern alone.

**Expected outcome:** Delivered oxygen tracks commanded settings consistently during functional testing. If it does, document the final results and return the ventilator to service according to local policy.

### 10. Perform Final Functional Verification
After any external correction, perform the required ventilator functional checks using approved test equipment.

Verify stable ventilation, oxygen measurement, alarm operation, circuit integrity, and normal startup behavior as applicable.

**Expected outcome:** The ventilator operates normally and oxygen delivery is independently verified. Troubleshooting is complete and the device may be returned to service only after all required checks pass.

## If the Problem Persists

If delivered FiO2 remains inaccurate after gas sources, hoses, circuit components, accessories, measurement setup, settings, and approved calibration have been verified, common external causes have been ruled out.

Possible remaining categories include internal gas-control, oxygen-measurement, pneumatic, calibration, or service-level faults. Do not assume a specific internal component has failed without manufacturer-directed testing.

The ventilator should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Do not return the ventilator to clinical use until oxygen delivery, ventilation performance, alarms, and all required return-to-service checks have passed.

Knowing when to stop external troubleshooting and escalate an unreliable oxygen-delivery condition is proper troubleshooting.

## Clinical Use Tip

Never rely on a ventilator with questionable oxygen delivery when another verified ventilator can maintain the patient's respiratory support.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

FiO2 complaints require patient protection first, followed by verification of gas sources, external connections, circuits, accessories, settings, calibration, and independent measurement before internal failure is suspected. Accurate testing, appropriate escalation, and clear CCR documentation protect both the patient and the service process.

That is successful troubleshooting.
