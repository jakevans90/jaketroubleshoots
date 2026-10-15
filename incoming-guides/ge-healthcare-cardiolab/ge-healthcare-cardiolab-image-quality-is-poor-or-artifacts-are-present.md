---
schemaVersion: 1
title: "GE Healthcare CardioLab Electrophysiology Recording System - Image Quality Is Poor or Artifacts Are Present"
issueTitle: "Image Quality Is Poor or Artifacts Are Present"
description: "Displayed or recorded CardioLab waveforms appear noisy, distorted, or artifact-contaminated because of electrodes, leads, grounding, connections, positioning, or interference."
assetType: "Electrophysiology Recording System"
manufacturer: "GE Healthcare"
model: "CardioLab"
slug: "ge-healthcare-cardiolab-image-quality-is-poor-or-artifacts-are-present"
dateAdded: "2026-10-15"
taxonomyMode: "reuse"
ccr:
  complaint: "EP staff reported heavy artifact on CardioLab surface ECG channels during patient monitoring."
  cause: "Clinical Engineering found a damaged external ECG patient cable that produced intermittent noise when moved."
  resolution: "The cable was replaced with an approved known-good cable, stable simulated signals were verified on all affected channels, and the system was returned to service."
helpfulDetails:
  - "Channels affected"
  - "Whether surface or intracardiac signals were involved"
  - "Electrode and lead condition"
  - "Patient-cable condition"
  - "Cable routing"
  - "Nearby equipment operating"
  - "Known-good substitution results"
  - "Relevant display settings"
  - "Simulator results"
  - "Whether movement changed the artifact"
  - "Final waveform quality"
  - "Final device status"
---

## What This Guide Helps With

Displayed or recorded CardioLab waveforms appear noisy, distorted, or artifact-contaminated because of electrodes, leads, grounding, connections, positioning, or interference.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Confirm Reliable Monitoring

If poor signal quality makes CardioLab unreliable for clinical interpretation, provide another verified monitoring method before troubleshooting the affected signal path.

Determine whether staff are describing electrophysiology waveforms or images from another integrated imaging system.

**Expected outcome:** Patient monitoring remains reliable and the affected signal or image source is identified.

### 2. Confirm Which Channels or Displays Are Affected

Determine whether the artifact affects all channels, surface ECG only, intracardiac signals, a specific catheter input, one display, or recorded data only.

Ask when the artifact appears and whether it changes with patient movement, equipment movement, ablation, pacing, or operation of nearby electrical equipment.

**Expected outcome:** The artifact is narrowed to a specific signal path or environmental condition.

If the apparent problem is limited to one display setting and correct signal quality is confirmed elsewhere, address the display condition and stop troubleshooting after verification.

### 3. Inspect Electrodes, Leads, and Patient Connections

With clinical staff involvement as appropriate, inspect accessible ECG electrodes, lead wires, patient cables, catheter-interface connections, and other external signal accessories.

Look for loose connections, dried or poorly adherent electrodes, damaged insulation, contaminated connectors, or cable strain.

**Expected outcome:** Patient-connected accessories are secure, appropriate, and in good physical condition.

If replacing or reconnecting an external accessory eliminates the artifact, verify stable signals and stop troubleshooting.

### 4. Check Cable Routing and Positioning

Separate signal cables from mains cords, motors, power supplies, electrosurgical cables, and other likely interference sources where practical.

Avoid coiling excess patient-signal cable around powered equipment.

**Expected outcome:** Signal cables are routed to minimize avoidable electrical interference.

If repositioning cables removes the artifact, confirm the signal remains stable and stop troubleshooting.

### 5. Evaluate Environmental Electrical Interference

Determine whether the artifact changes when nearby nonessential equipment is powered off or moved away, provided this can be done without affecting patient care.

Do not disable required clinical equipment simply to improve a signal.

**Expected outcome:** External interference is either identified or ruled out.

If a specific external source is confirmed, correct the environmental condition and verify CardioLab signal quality.

### 6. Compare With Known-Good External Accessories

Where approved, substitute a known-good compatible lead, cable, or external interface component for the suspected item.

Change one item at a time so the cause remains identifiable.

**Expected outcome:** A defective external accessory is isolated or ruled out.

If the known-good accessory restores normal waveforms, remove the defective accessory from service and stop troubleshooting after verification.

### 7. Check Display and Signal Settings

Verify externally accessible CardioLab display, gain, scale, filter, channel selection, and other user-facing settings are appropriate for the intended signal.

Do not alter protected clinical configuration or service-level filtering solely to hide a hardware problem.

**Expected outcome:** Display and signal settings are appropriate and do not artificially create or exaggerate the reported artifact.

If correcting an accidental setting change restores expected waveform appearance, verify recording quality and stop troubleshooting.

### 8. Perform Controlled Signal Verification

Use an approved ECG or electrophysiology simulator, test source, or manufacturer-supported method to evaluate the external signal path.

Compare the test signal across affected and unaffected channels when useful.

**Expected outcome:** CardioLab displays and records a stable expected test signal without unexplained artifact.

If testing passes consistently, troubleshooting is complete.

### 9. Escalate Persistent Artifact

If artifact remains with known-good external accessories and a controlled test source, remove the affected system or channel from service as clinically appropriate.

Do not perform board-level amplifier, isolation, or acquisition repair without authorized service procedures.

**Expected outcome:** Persistent internal or infrastructure-related signal problems are escalated safely.

## If the Problem Persists

Electrodes, external leads, cable routing, environmental interference, accessories, and basic display settings have been ruled out. Remaining possibilities may involve acquisition electronics, grounding or infrastructure, internal signal processing, software, or another service-level condition.

The CardioLab system should be:

- Removed from service when clinically unreliable.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved signal simulators or test equipment.
- Repaired or configured only by qualified personnel.

Verify all affected signal paths before return to service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never accept a visually plausible waveform if artifact makes the signal clinically unreliable; provide another verified monitoring path until CardioLab is proven stable.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Poor CardioLab signal quality should be approached from the patient connection outward. Verify electrodes, cables, routing, environmental interference, accessories, and settings before suspecting acquisition electronics, then document the proven cause and final signal verification.

That is successful troubleshooting.
