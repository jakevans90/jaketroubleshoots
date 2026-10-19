---
schemaVersion: 1
title: "GE Healthcare CASE Stress Test System - Signal Is Noisy, Intermittent, or Missing"
issueTitle: "Signal Is Noisy, Intermittent, or Missing"
description: "ECG or other acquired signals contain artifact, drop out intermittently, or disappear during stress-test preparation or acquisition."
assetType: "Stress Test System"
manufacturer: "GE Healthcare"
model: "CASE"
slug: "ge-healthcare-case-signal-is-noisy-intermittent-or-missing"
dateAdded: "2026-10-19"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported heavy ECG artifact and intermittent lead dropout when patients began exercising on the CASE system."
  cause: "Clinical Engineering found an intermittently open patient lead set that produced artifact when the cable moved."
  resolution: "Replaced the lead set and verified stable simulated ECG signals while gently moving the external cabling."
helpfulDetails:
  - "Channels affected"
  - "Whether noise was continuous or movement-related"
  - "Electrode and skin-contact condition"
  - "Cable and leadwire inspection findings"
  - "Known-good substitution results"
  - "Simulator results"
  - "Environmental conditions"
  - "Acquisition connection status"
  - "Results after correction"
  - "Final device status"
---

## What This Guide Helps With
ECG or other acquired signals contain artifact, drop out intermittently, or disappear during stress-test preparation or acquisition.

## Step-by-Step Troubleshooting
### 1. Protect the Patient and Stop Unsafe Testing
If signal quality becomes unreliable during an active stress study, do not continue exercising the patient while depending on questionable monitoring. Follow clinical protocol for stopping the study and provide verified alternate monitoring as needed.

**Expected outcome:** Clinical monitoring remains reliable while the CASE signal problem is investigated.

### 2. Reproduce and Characterize the Signal Problem
Determine which signals are affected and whether noise occurs continuously, only with movement, only during exercise, or only at a specific workstation or room. Observe whether all ECG channels or selected leads are affected.

**Expected outcome:** A repeatable pattern is identified. If the complaint cannot be reproduced, continue with inspection and functional verification before return to service.

### 3. Verify Electrode Application and Skin Contact
For ECG artifact, inspect electrode adhesion, placement, patient preparation, lead attachment, and cable routing. Replace questionable electrodes and ensure leads are not pulling on the electrodes.

**Expected outcome:** Patient-side contact is secure and signal quality improves when poor electrode contact was the cause. If stable acquisition is restored, troubleshooting can stop after verification.

### 4. Inspect Leadwires and Patient Cable
Check cables for cuts, cracked insulation, damaged strain reliefs, loose connectors, contamination, or intermittent behavior when gently repositioned. Do not aggressively flex cables while attached to a patient.

**Expected outcome:** Cabling remains stable during normal handling. A cable that causes repeatable dropouts should be removed from service.

### 5. Substitute Known-Good Patient Accessories
Replace the suspect lead set or patient cable with a verified compatible known-good accessory. Keep other variables unchanged.

**Expected outcome:** If the signal becomes stable with the known-good accessory, the original accessory is isolated as the cause. Verify all channels and stop troubleshooting.

### 6. Evaluate Cable Routing and Environmental Interference
Separate patient and acquisition cables from obvious sources of electrical interference, damaged power equipment, high-current cords, or other equipment that may be contributing to artifact. Verify cables are not bundled unnecessarily with power cords.

**Expected outcome:** Signal quality remains stable in an appropriate cable-routing environment.

### 7. Compare Patient Signal With a Simulator
When appropriate, disconnect the patient and connect an approved ECG simulator or other suitable test source to the acquisition path. Compare signal stability with the simulator connected.

**Expected outcome:** A clean, stable simulated signal indicates the CASE acquisition path is functioning and directs attention toward patient-side connections or environmental causes. Persistent noise with a simulator suggests a system-level problem.

### 8. Verify External Acquisition Connections
Inspect and reseat accessible connections between the acquisition device and CASE workstation. Confirm no cable is loose, stretched, crushed, or damaged.

**Expected outcome:** All acquisition connections remain secure without communication or signal interruption.

### 9. Perform Final Functional Verification
Verify clean, stable acquisition across required channels using approved test equipment or an appropriate controlled setup. Confirm signal quality remains acceptable during normal cable movement and workstation operation.

**Expected outcome:** Signals remain present and stable without excessive artifact or dropout. The issue is resolved and troubleshooting can stop.

## If the Problem Persists
Patient preparation, electrodes, leadwires, patient cables, environmental interference, known-good substitutions, and external acquisition connections have been ruled out. The remaining problem may involve acquisition hardware, grounding, workstation interface, system configuration, or another service-level condition.

Remove the affected system from service, label it **Out of Service**, and send it for repair or bench evaluation using appropriate GE Healthcare documentation and approved test equipment. Internal repair should be performed only by qualified personnel.

Do not return the system to clinical use until stable signal acquisition is verified.

## Clinical Use Tip
Stress testing creates substantial patient motion; verify cable routing and ECG stability under expected movement conditions before beginning exercise.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Signal complaints should be isolated from the patient outward, beginning with electrodes, motion, cables, and environment before internal failure is considered. Verify the full acquisition path after correction and document what actually caused the problem.

That is successful troubleshooting.
