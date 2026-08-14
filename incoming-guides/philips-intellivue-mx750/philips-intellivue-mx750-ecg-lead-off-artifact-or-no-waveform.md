---
schemaVersion: 1
title: "Philips IntelliVue MX750 Patient Monitor - ECG Lead-Off, Artifact, or No Waveform"
issueTitle: "ECG Lead-Off, Artifact, or No Waveform"
description: "Troubleshoots ECG lead-off messages, artifact, or missing waveforms caused by electrodes, lead wires, cables, connections, placement, or interference."
assetType: "Patient Monitor"
manufacturer: "Philips"
model: "IntelliVue MX750"
slug: "philips-intellivue-mx750-ecg-lead-off-artifact-or-no-waveform"
dateAdded: "2026-08-14"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported intermittent ECG lead-off messages and heavy artifact on the Philips IntelliVue MX750."
  cause: "Clinical Engineering found an intermittent ECG lead-wire set that produced artifact when the cable was moved."
  resolution: "Clinical Engineering replaced the lead-wire set and verified stable simulated ECG, lead detection, heart-rate display, and alarm operation."
helpfulDetails:
  - "Exact lead-off indication"
  - "Leads affected"
  - "Electrode condition"
  - "Patient cable and lead-wire condition"
  - "Whether cable movement reproduced the issue"
  - "Known-good accessory results"
  - "Presence of motion or electrical interference"
  - "ECG source and lead selection observed"
  - "Simulator test result"
  - "Final waveform and alarm status"
---

## What This Guide Helps With
Troubleshoots ECG lead-off messages, artifact, or missing waveforms caused by electrodes, lead wires, cables, connections, placement, or interference.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Verify Rhythm by Another Method
If reliable ECG monitoring is clinically required and the MX750 is not providing dependable information, establish another verified monitoring method before troubleshooting.

**Expected outcome:** The patient remains appropriately monitored while the ECG problem is investigated.

### 2. Confirm the Exact ECG Complaint
Determine whether the issue is a lead-off indication, excessive artifact, intermittent waveform, flat line, missing waveform, or a problem limited to certain leads. Compare the displayed condition with the patient's clinical status.

**Expected outcome:** The problem is clearly characterized and false assumptions about patient rhythm are avoided.

### 3. Inspect and Replace Electrodes as Needed
Check electrode adhesion, expiration or storage condition if known, skin contact, dried gel, contamination, and placement. Replace questionable electrodes and prepare the skin according to facility practice.

**Expected outcome:** Electrodes make stable contact and lead-off or artifact indications clear. If the waveform becomes stable, proceed to final verification.

### 4. Inspect Lead Wires and Patient Cable
Examine lead wires, snaps, clips, cable insulation, connectors, strain reliefs, and the patient cable for contamination, cracking, stretched conductors, bent contacts, or intermittent connections.

**Expected outcome:** The ECG cable set is intact and securely connected. If a damaged accessory is found, replace it with an approved compatible accessory.

### 5. Reseat All ECG Connections
Disconnect and reconnect the accessible ECG patient cable and individual lead connections. Ensure connections are fully seated without forcing connectors.

**Expected outcome:** The monitor detects the connected leads and displays a stable waveform. If reseating resolves the issue, continue to verification.

### 6. Substitute Known-Good ECG Accessories
Use a known-good compatible patient cable, lead-wire set, or electrodes to isolate whether the problem follows an accessory.

**Expected outcome:** A stable ECG is obtained with known-good accessories. If the problem follows the original accessory, remove that accessory from service.

### 7. Check for Motion and Electrical Interference
Assess patient movement, loose cables, cable routing near electrically noisy equipment, poor electrode contact, and other nearby sources of artifact. Reposition cables and eliminate obvious interference where practical.

**Expected outcome:** Artifact decreases and the waveform remains stable. If the problem disappears after correcting positioning or interference, troubleshooting can stop after verification.

### 8. Verify ECG Setup Without Unauthorized Changes
Confirm the expected ECG source, lead selection, and clinically appropriate settings. Do not use service menus or alter protected configuration without authorization.

**Expected outcome:** ECG display settings support the intended monitoring configuration and are not masking an otherwise valid waveform.

### 9. Test With an ECG Simulator
Remove the monitor from patient use and connect an approved ECG simulator using known-good accessories. Verify stable waveform acquisition, heart-rate display, lead detection, and relevant alarms.

**Expected outcome:** Simulated ECG is displayed reliably. If the monitor passes with a simulator, the original problem was likely external to the monitor.

### 10. Escalate a Persistent ECG Failure
If electrodes, cables, lead wires, connections, interference, setup, and simulator testing do not restore reliable ECG operation, stop external troubleshooting.

**Expected outcome:** The monitor or affected measurement hardware is removed from service for qualified evaluation.

## If the Problem Persists
Common external ECG causes have been ruled out. The remaining issue may involve the ECG measurement interface, module hardware, internal communication, configuration, or another service-level problem.

The affected equipment should be:
- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Philips service documentation and approved ECG test equipment
- Repaired or configured only by qualified personnel

After repair, verify ECG acquisition, lead detection, heart-rate calculation, and relevant alarms before return to service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
Never interpret a questionable ECG waveform without correlating it to the patient and another reliable clinical indicator.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Start with electrodes and cables, distinguish true patient changes from artifact, verify the complete external ECG path before suspecting internal hardware, and document the final simulated or clinical verification clearly.

That is successful troubleshooting.
