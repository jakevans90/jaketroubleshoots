---
schemaVersion: 1
title: "GE Healthcare B105 / B125 / B155 Series Patient Monitor - Invasive Pressure Channel Missing, Drifting, or Will Not Zero"
issueTitle: "Invasive Pressure Channel Missing, Drifting, or Will Not Zero"
description: "Troubleshoots missing invasive pressure channels, zeroing problems, unstable baselines, transducer cables, connections, setup, and external pressure-monitoring components."
assetType: "Patient Monitor"
manufacturer: "GE Healthcare"
model: "B105 / B125 / B155 Series"
slug: "ge-healthcare-b105-b125-b155-series-invasive-pressure-channel-missing-drifting-or-will-not-zero"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that the B155 arterial pressure channel intermittently disappeared and would not consistently zero."
  cause: "Clinical Engineering found an intermittent reusable invasive pressure cable and confirmed stable operation with a known-good cable."
  resolution: "Replaced the defective pressure cable, verified channel detection, stable zero and simulated pressure response, tested applicable alarms, and returned the monitor to service."
helpfulDetails:
  - "Pressure channel affected"
  - "Whether the channel was missing or drifting"
  - "Zero attempt result"
  - "Transducer and cable condition"
  - "Patient-side setup observations"
  - "Channel configuration"
  - "Known-good cable result"
  - "Simulator result"
  - "Other pressure input comparison"
  - "Alarm verification"
  - "Results before and after correction"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots missing invasive pressure channels, zeroing problems, unstable baselines, transducer cables, connections, setup, and external pressure-monitoring components.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Pressure Monitoring
If invasive pressure monitoring is clinically required and the channel is absent, drifting, or cannot be zeroed reliably, ensure another verified monitoring method is available before technical troubleshooting.

Do not disconnect or manipulate an active invasive pressure system without coordination with appropriate clinical staff.

**Expected outcome:** Patient monitoring remains continuous while the affected pressure channel is evaluated safely.

### 2. Confirm the Exact Pressure Complaint
Determine whether:
- The pressure channel is missing
- The transducer is not detected
- The channel will not zero
- The displayed baseline drifts
- The waveform is absent
- Values are implausible
- The problem follows a particular transducer, cable, or monitor input

Identify which invasive pressure channel is affected.

**Expected outcome:** The failure pattern and affected signal path are clearly identified.

### 3. Inspect the External Transducer Cable
Inspect the reusable pressure cable and connectors for:
- Cuts
- Bent contacts
- Contamination
- Loose fittings
- Strain-relief damage
- Intermittent operation when gently moved

Reseat accessible monitor and transducer cable connections.

**Expected outcome:** The cable is intact and fully seated.

If reseating restores a stable channel, continue to functional verification.

### 4. Verify the Disposable Transducer Setup With Clinical Staff
Coordinate with clinical personnel to verify the patient-side pressure setup is assembled and positioned appropriately.

Check externally for:
- Loose connection between transducer and reusable cable
- Incorrect physical positioning
- Closed or incorrectly positioned stopcocks
- Air or obvious setup issues requiring clinical correction
- A transducer that has not been properly exposed to atmospheric pressure for zeroing

Clinical personnel should manage the patient-connected fluid path.

**Expected outcome:** The pressure system is appropriately configured for the clinical zeroing process.

If correcting the clinical setup allows a stable zero and waveform, troubleshooting can stop after verification.

### 5. Verify Channel Configuration
Confirm that the pressure parameter is enabled and assigned appropriately for the connected input.

Avoid changing clinical labels or configuration unnecessarily. Record existing configuration before authorized adjustments.

**Expected outcome:** The connected invasive pressure input is configured and available for display.

If the channel was disabled or incorrectly assigned and authorized correction restores it, verify function and stop troubleshooting.

### 6. Attempt a Proper Zero With Clinical Coordination
With the transducer appropriately positioned and open to atmosphere according to clinical procedure, initiate the normal zero operation.

Observe whether zeroing:
- Completes normally
- Is rejected
- Produces an unstable baseline
- Works temporarily and then drifts

Do not attempt to compensate for drift by repeatedly zeroing a faulty system.

**Expected outcome:** The channel accepts a stable zero under appropriate conditions.

### 7. Substitute a Known-Good Pressure Cable
Use a compatible known-good reusable invasive pressure cable when available.

If the issue resolves, retest the original cable to confirm the failure follows it before replacement.

**Expected outcome:** A known-good cable provides stable channel recognition and zeroing.

If the problem follows the cable, replace the defective cable and proceed to final verification.

### 8. Use an Approved Pressure Simulator
Off-patient, connect an approved invasive pressure simulator or test setup using known-good accessories.

Verify:
- Channel detection
- Successful zero
- Stable baseline
- Stable pressure waveform or simulated value
- Absence of unexplained drift

Do not perform unauthorized calibration adjustments.

**Expected outcome:** The monitor accurately and consistently responds to the controlled pressure input within the applicable approved test procedure.

### 9. Compare Another Pressure Input When Available
If the monitor configuration provides another appropriate invasive pressure input, use a controlled off-patient comparison according to facility procedures.

This can help determine whether the problem follows a cable/transducer or remains associated with one monitor input.

**Expected outcome:** The fault can be localized to an external component or a particular monitor channel without internal disassembly.

### 10. Perform Final Functional Verification
After correction, verify:
- Pressure channel availability
- Stable zero
- Stable waveform
- Appropriate response to approved simulated pressure
- No unexplained drift
- Secure cable connections
- Applicable pressure alarms

**Expected outcome:** The invasive pressure channel performs consistently and is ready for clinical use.

If all checks pass, document and return the monitor to service.

### 11. Escalate Persistent Pressure-Channel Failure
If the channel remains missing, will not zero, or drifts when connected to known-good accessories and approved pressure test equipment, stop external troubleshooting.

**Expected outcome:** The monitor is removed from service for qualified evaluation.

## If the Problem Persists

External transducers, reusable cables, configuration, zeroing conditions, and controlled simulator inputs have been evaluated. Remaining possibilities may involve the invasive pressure input circuitry, connector interface, parameter hardware, calibration, configuration, or another service-level fault.

The monitor should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved pressure test equipment
- Repaired, calibrated, or configured only by qualified personnel

After repair, verify all affected invasive pressure channels, zero function, pressure response, alarms, and required overall monitor operation before return to service.

Knowing when repeated zeroing is masking rather than solving a pressure-monitoring problem is proper troubleshooting.

## Clinical Use Tip

Do not manipulate the patient-connected fluid path solely for equipment troubleshooting; coordinate zeroing and transducer setup changes with the responsible clinical team.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**




## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Preserve patient safety and the sterile clinical pressure setup, verify transducers, cables, positioning, zeroing conditions, and configuration before suspecting internal hardware, and escalate any channel that cannot remain stable under controlled testing.

That is successful troubleshooting.
