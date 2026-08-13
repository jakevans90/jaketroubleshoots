---
schemaVersion: 1
title: "GE Healthcare B105 / B125 / B155 Series Patient Monitor - ECG Lead-Off, Artifact, or No Waveform"
issueTitle: "ECG Lead-Off, Artifact, or No Waveform"
description: "Troubleshoots ECG lead-off messages, noisy traces, intermittent signals, missing waveforms, patient cable problems, electrodes, placement, and external interference."
assetType: "Patient Monitor"
manufacturer: "GE Healthcare"
model: "B105 / B125 / B155 Series"
slug: "ge-healthcare-b105-b125-b155-series-ecg-lead-off-artifact-or-no-waveform"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported intermittent ECG lead-off indications and excessive artifact on the B105 monitor."
  cause: "Clinical Engineering found an intermittent ECG lead-wire set that produced artifact when the cable was moved."
  resolution: "Replaced the defective lead-wire set, verified a stable simulated ECG waveform and heart-rate display, tested ECG alarms, and returned the monitor to service."
helpfulDetails:
  - "Exact lead-off message"
  - "Leads affected"
  - "Whether artifact occurred with movement"
  - "Electrode condition"
  - "ECG cable and lead-wire condition"
  - "Known-good accessory substitutions"
  - "ECG configuration observed"
  - "Simulator test result"
  - "Connector condition"
  - "Alarm verification"
  - "Results before and after correction"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots ECG lead-off messages, noisy traces, intermittent signals, missing waveforms, patient cable problems, electrodes, placement, and external interference.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Confirm an Alternate Assessment Method
If reliable ECG monitoring is clinically required and the monitor is not producing dependable ECG information, ensure the patient is monitored by another verified device or appropriate clinical method before technical troubleshooting.

Do not troubleshoot unreliable monitoring while a patient depends on it.

**Expected outcome:** The patient has reliable monitoring while the affected ECG path is evaluated.

### 2. Confirm the Exact ECG Complaint
Determine whether the reported problem is:
- Lead-off indication
- No ECG waveform
- Excessive artifact
- Intermittent waveform
- One lead missing
- Heart rate unavailable or unstable
- Problem occurring only during movement

Observe which leads or channels are affected.

**Expected outcome:** The exact ECG failure pattern is identified.

### 3. Inspect the ECG Patient Cable and Lead Wires
Inspect the ECG trunk cable, lead wires, connectors, strain reliefs, and accessible contacts for:
- Cuts
- Cracks
- Bent contacts
- Loose connectors
- Fluid contamination
- Damaged snaps or clips
- Intermittent behavior when the cable is gently moved

Reseat all external ECG connections.

**Expected outcome:** ECG cables and lead wires are intact and securely connected.

If reseating a loose connection restores a stable waveform, complete final verification and troubleshooting can stop.

### 4. Check Electrodes and Patient Connections
Coordinate with clinical staff to verify that:
- Electrodes are present
- Electrodes have not dried out or detached
- Lead wires are attached securely
- Skin contact is adequate
- Electrode placement is clinically appropriate

Clinical staff should manage patient skin preparation and electrode placement as appropriate.

**Expected outcome:** Each required lead has a secure conductive patient connection.

If replacing a loose or degraded electrode corrects the waveform, verify all displayed leads and troubleshooting can stop.

### 5. Verify the Selected ECG Configuration
Confirm that the monitor is configured for the ECG lead set and monitoring arrangement actually connected.

Do not alter clinical settings unnecessarily. Record existing settings before making any authorized correction.

**Expected outcome:** The monitor configuration corresponds with the connected ECG cable and intended clinical monitoring setup.

If an incorrect external configuration caused the issue, restore the correct setting and verify normal operation.

### 6. Check for Motion and Environmental Artifact
Determine whether artifact occurs primarily during:
- Patient movement
- Bed movement
- Cable movement
- Electrosurgery or other electrical equipment operation
- Poorly secured lead wires
- Contact with damaged or contaminated cables

Route cables to reduce tension and unnecessary movement.

**Expected outcome:** The ECG waveform remains stable under normal conditions without avoidable external interference.

If correcting cable routing or an environmental source resolves the artifact, troubleshooting can stop after verification.

### 7. Substitute Known-Good ECG Accessories
When available, substitute compatible known-good components systematically:
- Lead wires
- ECG trunk/patient cable
- Approved simulator connection during bench testing

Change one item at a time so the cause can be identified.

**Expected outcome:** A known-good accessory produces a stable ECG waveform.

If the problem follows an ECG cable or lead-wire set, replace that accessory and proceed to final verification.

### 8. Test With an ECG Simulator Off-Patient
Connect an approved patient simulator using known-good ECG accessories.

Verify that the monitor displays a stable ECG waveform and heart-rate value without lead-off indications.

Do not use simulator testing as a substitute for checking the patient-side electrode and cable path when the original problem occurred clinically.

**Expected outcome:** The monitor correctly detects and displays the simulated ECG signal.

If simulator performance is normal, the monitor is likely functioning and attention should return to patient electrodes, cables, environment, or application conditions.

### 9. Check the Monitor ECG Input Externally
Inspect the accessible monitor ECG connection for debris, contamination, physical damage, or looseness.

Do not probe, disassemble, or attempt internal connector repair without approved service procedures.

**Expected outcome:** The ECG input is clean, intact, and securely retains the appropriate connector.

### 10. Perform Final Functional Verification
After correction, verify:
- Stable ECG waveform
- Appropriate lead identification
- Reliable heart-rate display
- No persistent lead-off condition
- Expected alarm response using an approved test method
- Stable operation when cables are moved normally

**Expected outcome:** ECG monitoring and associated alarms function reliably.

If all checks pass, document the cause and return the monitor to service.

### 11. Escalate Persistent ECG Failure
If a known-good ECG cable and simulator do not produce reliable ECG monitoring, or the input connector is damaged, stop external troubleshooting.

**Expected outcome:** A monitor with unresolved ECG failure is removed from clinical availability and sent for service.

## If the Problem Persists

Electrodes, cables, lead wires, configuration, environmental factors, and known-good simulated inputs have been evaluated. Remaining possibilities may include the monitor's ECG acquisition circuitry, input interface, configuration, or another internal service-level issue.

The monitor should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired or configured only by qualified personnel

Following repair, verify ECG acquisition, lead detection, heart-rate processing, applicable alarms, and other required return-to-service functions.

Knowing when an ECG problem has moved beyond accessories and external connections is proper troubleshooting.

## Clinical Use Tip

A displayed heart rate does not prove the ECG waveform is clinically reliable; verify the waveform quality and complete ECG signal path after any repair.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**




## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient, follow the ECG signal path from electrodes to monitor, eliminate cable and environmental causes before suspecting internal acquisition hardware, and verify both waveform and alarm performance before returning the device to use.

That is successful troubleshooting.
