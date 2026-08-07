---
schemaVersion: 1
title: "ZOLL Propaq MD Defibrillator - ECG Lead-Off, Artifact, or No Waveform"
issueTitle: "ECG Lead-Off, Artifact, or No Waveform"
description: "ECG leads appear disconnected, the waveform is absent, or excessive artifact occurs because of electrodes, cables, connections, placement, settings, or environment."
assetType: "Defibrillator"
manufacturer: "ZOLL"
model: "Propaq MD"
slug: "zoll-propaq-md-ecg-lead-off-artifact-or-no-waveform"
dateAdded: "2026-08-07"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported persistent ECG lead-off messages and an intermittent waveform during monitoring."
  cause: "Clinical Engineering found an intermittent ECG patient cable that reproduced the lead-off condition during controlled testing."
  resolution: "The defective ECG cable was replaced and the Propaq MD passed simulator testing with stable waveforms and proper lead-off detection."
helpfulDetails:
  - "Exact lead-off indication"
  - "Leads affected"
  - "Waveform behavior"
  - "Electrode condition"
  - "Cable and lead-wire condition"
  - "Patient versus simulator result"
  - "Known-good cable substitution"
  - "Lead selection observed"
  - "Artifact during cable movement"
  - "Environmental interference noted"
  - "Alarm behavior"
  - "Final device status"
---

## What This Guide Helps With

ECG leads appear disconnected, the waveform is absent, or excessive artifact occurs because of electrodes, cables, connections, placement, settings, or environment.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Monitoring
If reliable ECG monitoring is clinically required, move the patient to another verified monitoring method before troubleshooting an unreliable ECG channel.

Do not troubleshoot intermittent or absent ECG monitoring while the patient depends solely on the affected signal.

**Expected outcome:** Continuous patient monitoring is maintained independently of the affected ECG function.

### 2. Confirm the Exact ECG Complaint
Determine whether staff reported:

- Lead-off indication
- No waveform
- Intermittent waveform
- Excessive artifact
- One lead missing
- All leads missing
- Problem occurring only during movement
- Problem occurring only with a particular cable or patient

Reproduce the condition using an ECG simulator when appropriate.

**Expected outcome:** The failure is narrowed to a specific signal condition rather than treated as a general ECG failure.

### 3. Verify ECG Monitoring Is Selected and Configured Appropriately
Check that the intended ECG source and lead selection are active and that the display has not simply been switched to another monitoring source.

Review visible settings without making unauthorized configuration changes.

**Expected outcome:** The intended ECG lead is selected and expected to appear on the display. If correcting the lead selection restores a stable waveform, troubleshooting can stop after verification.

### 4. Inspect Electrodes and Patient-Side Connections
When evaluating a clinical setup, inspect for:

- Dried or expired electrodes
- Poor skin contact
- Loose snaps
- Incorrect lead placement
- Excess hair, moisture, lotions, or contamination interfering with adhesion
- Disconnected individual lead wires

Replace questionable disposable electrodes as appropriate.

**Expected outcome:** All electrodes have secure electrical and mechanical contact. If the waveform becomes stable, verify all required leads and stop troubleshooting.

### 5. Inspect the ECG Cable and Lead Wires
Examine the patient cable and individual lead wires for:

- Cuts
- Crushed sections
- Exposed conductors
- Bent or contaminated contacts
- Loose connectors
- Strain damage
- Intermittency when gently repositioned

Do not continue using visibly damaged patient cables.

**Expected outcome:** The cable assembly is intact and connections remain stable during normal handling.

### 6. Reseat All Accessible ECG Connections
Disconnect and firmly reconnect the ECG patient cable and lead-wire connections.

Check for contamination or foreign material before reconnecting.

**Expected outcome:** Connections seat securely without intermittent lead-off indications. If reseating resolves the problem, complete simulator or patient-equivalent verification and stop troubleshooting.

### 7. Substitute Known-Good ECG Accessories
Use a known-good compatible patient cable, lead set, and test electrodes or ECG simulator connection as appropriate.

Change one component at a time when practical.

**Expected outcome:** A defective external accessory is isolated. If known-good accessories restore stable ECG monitoring, replace the faulty accessory and complete final verification.

### 8. Evaluate Artifact Sources
If a waveform is present but noisy, check for:

- Patient movement
- Poor electrode adhesion
- Cable movement
- Nearby electrical equipment
- Damaged leads
- Poor grounding or environmental electrical interference

Use an ECG simulator to separate device-related artifact from patient or environmental artifact.

**Expected outcome:** The simulator produces a stable waveform. If artifact occurs only in the clinical setup, correct the external source rather than assuming an internal monitor failure.

### 9. Perform Final Functional Verification
Using appropriate test equipment:

- Verify ECG waveform display
- Verify multiple lead selections when applicable
- Confirm lead-off detection
- Confirm stable operation while gently manipulating external cables
- Confirm alarms and displayed values behave appropriately for the test setup

**Expected outcome:** ECG monitoring is stable, repeatable, and free of abnormal artifact. Troubleshooting can stop.

### 10. Escalate Persistent ECG Failure
If a no-waveform, lead-off, or artifact condition persists with a verified simulator and known-good compatible cables, remove the unit from service.

**Expected outcome:** A device-side ECG acquisition problem is referred for qualified service evaluation.

## If the Problem Persists

After electrodes, patient preparation, lead placement, settings, cables, connections, known-good substitutions, simulator testing, and environmental factors are ruled out, the remaining cause may involve the ECG acquisition path, connector interface, configuration, or another internal service-level issue.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Perform applicable ECG, alarm, monitoring, defibrillator, and electrical safety verification before returning the unit to clinical service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Confirm the complete ECG signal path from electrode to displayed waveform before returning the unit to patient monitoring.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain reliable patient monitoring, work from electrodes and cables inward, verify the signal with controlled test equipment before suspecting internal acquisition failure, escalate unresolved problems, and document the complete troubleshooting path.

That is successful troubleshooting.
