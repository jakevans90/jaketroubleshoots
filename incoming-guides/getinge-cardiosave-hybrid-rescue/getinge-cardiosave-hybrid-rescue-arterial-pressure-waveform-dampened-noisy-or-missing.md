---
schemaVersion: 1
title: "Getinge Cardiosave Hybrid / Rescue Intra-Aortic Balloon Pump - Arterial Pressure Waveform Dampened, Noisy, or Missing"
issueTitle: "Arterial Pressure Waveform Dampened, Noisy, or Missing"
description: "Troubleshoots arterial pressure waveform problems caused by transducer setup, cables, tubing, connections, positioning, interference, or external signal-path faults."
assetType: "Intra-Aortic Balloon Pump"
manufacturer: "Getinge"
model: "Cardiosave Hybrid / Rescue"
slug: "getinge-cardiosave-hybrid-rescue-arterial-pressure-waveform-dampened-noisy-or-missing"
dateAdded: "2026-09-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported an intermittently noisy arterial pressure waveform on the Cardiosave."
  cause: "Clinical Engineering found damage near the connector of the external pressure interface cable."
  resolution: "Clinical Engineering replaced the damaged cable, verified a stable pressure waveform with approved simulation, completed functional testing, and returned the unit to service."
helpfulDetails:
  - "Whether waveform was missing, dampened, or noisy"
  - "Trigger source in use"
  - "External pressure cable condition"
  - "Transducer and tubing observations"
  - "Known-good cable or test-source results"
  - "Presence of electrical interference"
  - "Simulator results"
  - "Behavior before and after correction"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots arterial pressure waveform problems caused by transducer setup, cables, tubing, connections, positioning, interference, or external signal-path faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Reliable Monitoring

If the Cardiosave pressure waveform is unreliable during active support, ensure the clinical team has another verified method of arterial pressure monitoring and that balloon timing remains safe.

Do not continue relying on an unreliable waveform for patient support decisions.

**Expected outcome:** Reliable alternate monitoring is available while the waveform problem is investigated.

### 2. Confirm the Waveform Condition

Determine whether the waveform is completely absent, intermittently missing, excessively noisy, flattened, or unusually dampened. Note whether the condition began after patient movement, transducer adjustment, transport, or cable manipulation.

**Expected outcome:** The symptom is clearly categorized. If the waveform is stable and correct after simple reconnection, verify operation and stop troubleshooting.

### 3. Inspect the External Pressure Cable

Check the pressure cable and connectors for incomplete seating, strain, cuts, damaged contacts, contamination, or intermittent behavior when gently moved.

**Expected outcome:** The cable is secure and undamaged. If a known-good approved cable restores the waveform, verify stable operation and stop troubleshooting.

### 4. Verify the External Transducer Setup

Confirm with clinical staff that the pressure transducer is connected, powered as required, and physically positioned according to the clinical setup. Inspect accessible connectors without changing the patient's invasive line configuration.

**Expected outcome:** The transducer setup is externally complete and connected.

### 5. Inspect Accessible Pressure Tubing

With clinical staff responsible for the patient line, look for visibly kinked tubing, closed or incorrectly positioned stopcocks, air, loose connections, or other obvious causes of damping or signal loss.

Clinical Engineering should not independently manipulate the invasive arterial line.

**Expected outcome:** No obvious external line restriction or disconnection is present. Clinical staff should correct patient-line conditions within their scope.

### 6. Check for Electrical Noise

Observe whether the waveform deteriorates when nearby equipment operates or when cables are routed near potential interference sources. Separate signal cables from obvious external interference where practical.

**Expected outcome:** The waveform remains stable independent of nearby equipment. If cable routing eliminates noise, verify continued stability and stop troubleshooting.

### 7. Compare With Another Verified Pressure Source

When appropriate and authorized, compare the pressure signal using a known-good approved transducer, cable, simulator, or equivalent test source after the unit is removed from patient dependence.

**Expected outcome:** A normal waveform with the test source isolates the problem to external patient-side components. Continued abnormality indicates a pump-side issue.

### 8. Verify Pressure Display and Processing Off-Patient

Use approved pressure simulation equipment to verify that the Cardiosave displays and responds to a stable pressure input appropriately.

Do not adjust calibration outside approved procedures.

**Expected outcome:** The simulated waveform is displayed clearly and consistently. If so, external clinical signal-path factors are more likely.

### 9. Perform Final Functional Verification

After correcting the cause, verify stable waveform display, trigger behavior if pressure triggering is used, alarms, controls, and overall operation.

**Expected outcome:** The pressure waveform remains stable throughout testing. Troubleshooting can stop.

### 10. Escalate an Internal Signal-Path Problem

If a known-good simulated input remains absent, noisy, or distorted, remove the Cardiosave from service.

**Expected outcome:** The problem is escalated for qualified internal evaluation rather than continued external troubleshooting.

## If the Problem Persists

External pressure cables, transducer setup, tubing conditions, connections, and interference have been evaluated. Remaining possibilities include an internal pressure input, signal-processing, connector, configuration, or display-related problem.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate Getinge documentation and approved pressure simulation equipment
- Repaired or configured only by qualified personnel

Complete applicable pressure-input, alarm, trigger, operational, and electrical safety testing before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

If the Cardiosave arterial waveform is questionable, ensure a reliable independent pressure-monitoring source is available before troubleshooting the IABP signal path.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Whether waveform was missing, dampened, or noisy
- Trigger source in use
- External pressure cable condition
- Transducer and tubing observations
- Known-good cable or test-source results
- Presence of electrical interference
- Simulator results
- Behavior before and after correction
- Final device status

## Final Thought

An arterial waveform problem can affect both monitoring and timing. Maintain alternate monitoring, verify the complete external pressure signal path before suspecting internal failure, and escalate the Cardiosave if a known-good simulated signal is not processed correctly.

That is successful troubleshooting.
