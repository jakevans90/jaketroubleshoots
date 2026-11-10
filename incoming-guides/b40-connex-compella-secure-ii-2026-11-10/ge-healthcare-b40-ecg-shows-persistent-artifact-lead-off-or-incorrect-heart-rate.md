---
schemaVersion: 1
title: "GE Healthcare B40 Patient Monitor - ECG Shows Persistent Artifact, Lead-Off, or Incorrect Heart Rate"
issueTitle: "ECG Shows Persistent Artifact, Lead-Off, or Incorrect Heart Rate"
description: "Troubleshoot ECG artifact, lead-off indications, or inaccurate heart rate caused by electrodes, lead wires, cables, settings, or interference."
assetType: "Patient Monitor"
manufacturer: "GE Healthcare"
model: "B40"
slug: "ge-healthcare-b40-ecg-shows-persistent-artifact-lead-off-or-incorrect-heart-rate"
dateAdded: "2026-11-10"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported persistent ECG artifact and intermittent lead-off indications on the B40 monitor."
  cause: "Clinical Engineering found a damaged ECG lead-wire connector that caused an intermittent connection."
  resolution: "Replaced the affected lead-wire set and verified stable simulated ECG waveforms, heart rate accuracy, and lead-off alarm operation."
helpfulDetails:
  - "Affected ECG leads"
  - "Exact artifact or lead-off behavior"
  - "Electrode condition"
  - "Lead-wire and trunk-cable inspection"
  - "Known-good cable substitutions"
  - "ECG filter and lead settings"
  - "Simulator waveform and heart rate"
  - "Environmental observations"
  - "Alarm verification"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoot ECG artifact, lead-off indications, or inaccurate heart rate caused by electrodes, lead wires, cables, settings, or interference.

## Step-by-Step Troubleshooting

### 1. Ensure Patient Safety and Monitoring Continuity
- Confirm that the patient's cardiac monitoring remains clinically appropriate.
- If the ECG signal or heart rate is unreliable, arrange another verified monitoring method.
- Notify clinical staff that the affected monitor should not be relied upon until the problem is corrected.
- Perform technical troubleshooting with an approved ECG simulator whenever possible.

Expected outcome: Reliable cardiac monitoring is maintained while the B40 is evaluated.

### 2. Confirm the Reported ECG Problem
- Identify whether the symptom is baseline wander, high-frequency artifact, lead-off, missing waveform, or incorrect heart rate.
- Determine which ECG leads are affected.
- Record whether the problem is continuous or intermittent.
- Ask whether it occurs during movement, procedures, or use of nearby equipment.

Expected outcome: The ECG failure is characterized and associated conditions are documented.

### 3. Inspect Electrodes and Patient Preparation Factors
- With clinical staff, verify that approved electrodes are being used.
- Check electrode expiration, adhesion, and visible gel condition.
- Confirm that electrode placement and skin preparation follow clinical policy.
- Replace questionable electrodes through the appropriate clinical workflow.

Expected outcome: Electrode contact and placement are appropriate, reducing contact-related artifact.

### 4. Inspect ECG Lead Wires
- Check lead wires for damaged insulation, loose snaps, corrosion, or broken connectors.
- Verify that each wire is securely attached.
- Look for excessive strain or pinching.
- Substitute a known-good compatible lead-wire set.

Expected outcome: Lead wires provide secure, reliable electrical connections. If the signal returns to normal and verification passes, troubleshooting can stop.

### 5. Inspect the ECG Trunk Cable
- Examine the patient cable for visible damage.
- Check the connection at the monitor or applicable parameter module.
- Verify that the cable is approved for the installed ECG configuration.
- Substitute a known-good compatible cable when available.

Expected outcome: Cable-related artifact or intermittent lead detection is eliminated.

### 6. Verify ECG Settings
- Confirm the selected lead and lead configuration.
- Review displayed ECG filter settings and the configured pacemaker detection mode where applicable.
- Verify that the monitor's settings match the intended clinical monitoring application.
- Do not use aggressive filtering simply to conceal a persistent signal problem.

Expected outcome: ECG processing settings are appropriate for the intended monitoring task.

### 7. Evaluate Environmental Interference
- Check for nearby electrical equipment, damaged power accessories, or cable routing that could contribute to interference.
- Verify that ECG cables are not unnecessarily bundled with power cords.
- Compare performance in a controlled test location when appropriate.
- Do not defeat protective grounding or electrical safety features.

Expected outcome: External electrical interference is reduced or ruled out.

### 8. Test With an ECG Simulator
- Connect an approved ECG simulator using compatible accessories.
- Select a known simulated waveform and heart rate.
- Compare the displayed waveform and heart rate with the simulator output.
- Verify lead-off detection using the approved procedure.
- Repeat with known-good cables if needed.

Expected outcome: The monitor displays a stable waveform and accurate simulated heart rate within applicable manufacturer requirements.

### 9. Verify ECG Alarm Operation
- Test applicable heart rate and lead-off alarms using approved simulation procedures.
- Confirm visual and audible alarm annunciation.
- Verify remote alarm transmission if required and supported.
- Restore the appropriate clinical configuration afterward.

Expected outcome: ECG measurement and alarm functions pass verification. If successful, document the correction and stop troubleshooting.

## If the Problem Persists

Electrodes, lead wires, patient cables, settings, and environmental causes have been evaluated. Remaining possibilities include ECG acquisition electronics, parameter module faults, signal-processing problems, or internal connection issues.

Remove the B40 from service, label it Out of Service, and arrange repair or bench evaluation. Qualified personnel should use manufacturer documentation and approved ECG simulation and electrical safety equipment. Internal repair or calibration must be performed only by qualified personnel.

Complete ECG performance and alarm verification before returning the monitor to clinical service. Knowing when external checks are exhausted is proper troubleshooting.

## Clinical Use Tip

A displayed heart rate does not prove that the ECG waveform is accurate. Always evaluate waveform quality and alarm behavior together.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

ECG problems should be approached by protecting cardiac monitoring first, then evaluating electrodes, cables, settings, and environmental interference. Confirm performance with an approved simulator before suspecting internal acquisition failure. Escalate unresolved faults and document the verified results.

That is successful troubleshooting.
