---
schemaVersion: 1
title: "Mindray uMEC Series Patient Monitor - Sidestream CO2 Module Reports a Sampling-Line Occlusion With a Clear Line"
issueTitle: "Sidestream CO2 Module Reports a Sampling-Line Occlusion With a Clear Line"
description: "The sidestream CO2 system reports restricted sampling even though the visible sampling line appears open and unobstructed."
assetType: "Patient Monitor"
manufacturer: "Mindray"
model: "uMEC Series"
slug: "mindray-umec-series-sidestream-co2-module-reports-a-sampling-line-occlusion-with-a-clear-line"
dateAdded: "2026-10-23"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory staff reported a persistent sidestream CO2 sampling-line occlusion message even though the tubing appeared clear."
  cause: "Clinical Engineering found that the original sampling line remained restricted internally despite having no visible kink or fluid blockage."
  resolution: "Clinical Engineering replaced the sampling line with a known-good compatible line and verified stable CO2 waveform acquisition with no recurring occlusion indication."
helpfulDetails:
  - "Exact CO2 message displayed"
  - "Whether CO2 waveform or numeric values were present"
  - "When the occlusion occurred"
  - "Sampling-line condition and routing"
  - "Moisture or secretion contamination"
  - "Patient interface condition"
  - "Connector condition"
  - "Known-good sampling-line result"
  - "Known-good interface result"
  - "CO2 module reseating result"
  - "Comparison with another module or monitor"
  - "Final CO2 waveform and alarm status"
  - "Final equipment status"
---

## What This Guide Helps With

The sidestream CO2 system reports restricted sampling even though the visible sampling line appears open and unobstructed.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain CO2 Monitoring

If continuous capnography is clinically required, do not troubleshoot unreliable CO2 monitoring while the patient depends on it.

Transfer CO2 monitoring to another verified monitor or module, or establish the clinically approved alternate monitoring method before removing components for testing.

**Expected outcome:** Required ventilation monitoring continues safely while the affected CO2 system is evaluated.

### 2. Confirm the Exact Occlusion Condition

Confirm the displayed message or symptom and determine when it occurs. Note whether the occlusion appears immediately after connecting the sampling line, after several minutes, only with a particular patient interface, or continuously.

Observe whether a CO2 waveform or numeric value appears before the fault.

**Expected outcome:** The fault is confirmed and its relationship to the sampling setup is understood.

If the alert clears and stable CO2 sampling resumes without recurrence, continue functional verification before stopping.

### 3. Inspect the Entire Sampling Line

Inspect the sampling tubing from the patient connection to the module. Look for kinks, tight bends, pinching under equipment, collapsed tubing, contamination, fluid, secretions, damaged connectors, or tubing caught in bedrails or transport hardware.

A line can appear clear internally while still being mechanically restricted.

**Expected outcome:** The tubing is physically open, properly routed, dry, and undamaged.

If correcting a kink or routing problem restores stable sampling, verify the waveform and troubleshooting can stop.

### 4. Disconnect the Patient Interface From the Sampling Line

When clinically safe and the system is removed from patient dependence, separate the sampling line from the airway adapter, nasal cannula, or other patient interface.

Observe whether the occlusion condition clears with the distal interface removed.

**Expected outcome:** Testing helps determine whether the restriction originates in the patient interface or elsewhere in the sampling pathway.

If the alert clears when the interface is removed, replace or correct the affected external interface before reconnecting to a patient.

### 5. Check for Moisture and Secretions

Examine the sampling line, airway adapter, and any accessible moisture-control component for condensation, mucus, fluid, or contamination.

Do not attempt to blow compressed air through patient sampling components or reuse single-use contaminated items contrary to facility policy.

**Expected outcome:** The sampling path is clean and dry.

If replacing a wet or contaminated component resolves the occlusion and stable CO2 readings return, troubleshooting can stop after verification.

### 6. Verify the Sampling-Line Connections

Disconnect and reconnect the sampling line at the module using the normal external connection method. Confirm the fitting seats completely and is not cross-threaded, damaged, partially engaged, or contaminated.

Inspect accessible connector surfaces for visible obstruction.

**Expected outcome:** The sampling line is securely and correctly connected to the module.

If proper reconnection clears the fault and sampling remains stable, troubleshooting can stop.

### 7. Substitute a Known-Good Compatible Sampling Line

Replace the apparently clear line with a known-good compatible sampling line.

Do not assume that visual inspection proves that a narrow internal lumen is unrestricted.

**Expected outcome:** The known-good line either restores normal sampling or reproduces the same occlusion fault.

If a known-good line resolves the problem, discard or remove the original defective consumable according to facility procedure and verify normal CO2 operation.

### 8. Substitute the External Patient Interface

If the symptom persists, use a known-good compatible airway adapter, cannula, or other external sampling interface appropriate to the test setup.

Do not use patient-contaminated components for cross-testing between patients.

**Expected outcome:** The test isolates the patient interface from the line and module.

If replacing the interface resolves the fault, the external accessory is the likely cause and troubleshooting can stop following functional verification.

### 9. Inspect Accessible Module Interfaces

Inspect the CO2 module and accessible sampling inlet for obvious contamination, liquid exposure, damaged fittings, or debris.

Do not insert tools, wires, cleaning objects, or pressurized gas into the sampling inlet unless specifically authorized by approved manufacturer service documentation.

**Expected outcome:** The accessible module interface is clean, dry, intact, and free of visible obstruction.

Visible liquid intrusion or physical damage is reason to remove the module from service.

### 10. Reseat the CO2 Module or External Connection

If the uMEC configuration uses a removable CO2 module or external module connection, disconnect and reseat it only while the monitor is not supporting patient-dependent CO2 monitoring.

Inspect accessible module cables or connectors for damage and ensure they are fully seated.

**Expected outcome:** The module is correctly connected and recognized by the monitor.

If reseating restores normal sampling and the fault does not recur, continue to final verification.

### 11. Compare With a Known-Good Module or Monitor

Where compatible equipment and facility procedures allow, test the sampling setup with a known-good module or test the suspect module on another approved compatible system.

Use clean test components and avoid changing configuration unrelated to the fault.

**Expected outcome:** The symptom can be isolated to the disposable sampling path, the module, or the monitor connection.

If the occlusion follows the CO2 module despite known-good external components, remove the module from service for bench evaluation.

### 12. Perform Final Functional Verification

Using an approved test method, verify that the system draws a sample without an occlusion indication and produces a stable CO2 response or waveform.

Confirm that the sampling line remains unrestricted during normal positioning and that no related CO2 alarm or module fault returns.

**Expected outcome:** The CO2 system samples consistently and provides stable monitoring without false occlusion indications.

If these checks pass, the device can be returned to service according to facility procedure.

## If the Problem Persists

If the sampling line, patient interface, moisture contamination, accessible connections, module seating, and known-good substitutions have been checked, common external causes have been ruled out.

A persistent occlusion indication may involve the module's internal sampling path, pump, pressure sensing, internal contamination, calibration, or another service-level condition. Do not disassemble the CO2 module or attempt to clear its internal pneumatic pathway without authorized service instructions.

The affected monitor or module should be:

- Removed from service when reliable CO2 monitoring cannot be confirmed.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

After repair, verify CO2 sampling, waveform response, applicable alarms, and overall monitor operation before return to service.

Knowing when known-good external components have ruled out the patient sampling path and the fault requires escalation is proper troubleshooting.

## Clinical Use Tip

A sampling line that looks visually clear may still be internally restricted; use a known-good compatible line before assuming the CO2 module has failed.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain ventilation monitoring first, then isolate the sampling path one external component at a time. A visually clear line is not proof of an unrestricted lumen, so verify with known-good components before suspecting internal module failure, and escalate persistent faults with clear CCR documentation.

That is successful troubleshooting.
