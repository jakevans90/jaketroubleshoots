---
schemaVersion: 1
title: "Getinge Cardiosave Hybrid / Rescue Intra-Aortic Balloon Pump - ECG Lead Signal Noisy, Intermittent, or Incorrectly Triggering"
issueTitle: "ECG Lead Signal Noisy, Intermittent, or Incorrectly Triggering"
description: "Troubleshoots unstable ECG triggering caused by electrodes, lead wires, patient cables, connections, interference, positioning, or external signal problems."
assetType: "Intra-Aortic Balloon Pump"
manufacturer: "Getinge"
model: "Cardiosave Hybrid / Rescue"
slug: "getinge-cardiosave-hybrid-rescue-ecg-lead-signal-noisy-intermittent-or-incorrectly-triggering"
dateAdded: "2026-09-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported intermittent ECG artifact causing unreliable balloon triggering."
  cause: "Clinical Engineering found an intermittent external ECG lead wire."
  resolution: "Clinical Engineering replaced the lead set, verified a clean ECG and stable triggering with simulation, completed functional testing, and returned the unit to service."
helpfulDetails:
  - "ECG appearance"
  - "Trigger source"
  - "Electrode condition"
  - "Lead-wire condition"
  - "Patient-cable condition"
  - "Whether movement affected the signal"
  - "Nearby interference sources"
  - "Known-good substitutions"
  - "ECG simulator results"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots unstable ECG triggering caused by electrodes, lead wires, patient cables, connections, interference, positioning, or external signal problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Unreliable Triggering

An unstable ECG trigger can result in inappropriate balloon timing. If counterpulsation is unreliable, notify the clinical team and ensure the patient has safe ongoing support before extended troubleshooting.

**Expected outcome:** Reliable patient support is maintained while the trigger problem is investigated.

### 2. Confirm the Exact ECG Problem

Observe whether the Cardiosave ECG is absent, noisy, intermittently dropping out, displaying excessive artifact, or triggering inconsistently. Document the selected trigger source and whether the problem changes with patient movement.

**Expected outcome:** The ECG failure mode is clearly identified.

### 3. Inspect ECG Electrodes and Lead Attachment

Coordinate with clinical staff to verify that electrodes are properly attached and have appropriate skin contact. Look for detached, dried, loose, or displaced electrodes.

Clinical Engineering should not unnecessarily disturb a stable patient setup.

**Expected outcome:** Electrode contact is reliable. If replacing or resecuring an electrode restores a stable ECG and trigger, verify operation and stop troubleshooting.

### 4. Inspect Lead Wires

Check accessible lead wires for cuts, stretched conductors, damaged snaps, bent contacts, contamination, or intermittent behavior.

**Expected outcome:** Lead wires are physically intact. Replace a suspect lead set with an approved known-good set when appropriate.

### 5. Inspect the ECG Patient Cable and Connector

Verify that the cable is fully seated and that the connector is free of damage, contamination, and excessive strain.

Gently manipulate the external cable while observing an off-patient test setup when intermittent damage is suspected.

**Expected outcome:** The connection remains stable. If replacing an external cable restores reliable ECG acquisition, troubleshooting can stop after verification.

### 6. Check for External Interference

Identify nearby equipment or cable routing that may introduce artifact. Keep ECG leads and cables away from obvious sources of electrical interference when possible.

**Expected outcome:** ECG quality remains stable when external interference is removed or minimized.

### 7. Verify Trigger Selection and Signal Availability

Confirm that ECG triggering is actually selected when ECG triggering is expected and that the displayed ECG has sufficient stability for the system to use it reliably.

Do not make unnecessary clinical configuration changes.

**Expected outcome:** The selected trigger source corresponds to a stable available signal.

### 8. Test With an Approved ECG Simulator

After removing the Cardiosave from active patient dependence, connect an approved ECG simulator and verify stable waveform acquisition and consistent triggering.

**Expected outcome:** Stable triggering with simulation indicates that the Cardiosave ECG input is functional and the original problem was likely external or patient-side. Continued instability requires escalation.

### 9. Perform Final Functional Verification

Verify ECG acquisition, trigger stability, timing response, alarms, display, controls, and applicable return-to-service checks.

**Expected outcome:** The ECG remains stable throughout testing. Troubleshooting can stop.

### 10. Escalate Persistent ECG Input Failure

If the Cardiosave cannot reliably acquire or trigger from a known-good simulated ECG signal, remove it from service.

**Expected outcome:** Internal signal-processing or input problems are referred for qualified service evaluation.

## If the Problem Persists

Electrodes, lead wires, patient cables, connectors, trigger selection, and external interference have been ruled out. Remaining possibilities include an internal ECG input, signal-processing, configuration, or software problem.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate Getinge documentation and approved ECG simulation equipment
- Repaired or configured only by qualified personnel

Complete applicable ECG, trigger, timing, alarm, operational, and electrical safety testing before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Always verify the ECG signal itself before investigating balloon timing; a timing complaint may originate from a damaged lead, electrode, or patient cable.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- ECG appearance
- Trigger source
- Electrode condition
- Lead-wire condition
- Patient-cable condition
- Whether movement affected the signal
- Nearby interference sources
- Known-good substitutions
- ECG simulator results
- Final device status

## Final Thought

Stable triggering begins with a reliable ECG signal. Protect the patient, inspect electrodes, leads, cables, connections, and interference before suspecting the Cardiosave electronics, and escalate any failure that persists with a known-good simulator.

That is successful troubleshooting.
