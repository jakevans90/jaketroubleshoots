---
schemaVersion: 1
title: "Mindray TE X Ultrasound System - ECG Input or Physiologic Trace Is Missing or Unstable"
issueTitle: "ECG Input or Physiologic Trace Is Missing or Unstable"
description: "Troubleshoots missing or unstable physiologic traces caused by leads, cables, accessories, connections, settings, placement, or electrical interference."
assetType: "Ultrasound System"
manufacturer: "Mindray"
model: "TE X"
slug: "mindray-te-x-ecg-input-or-physiologic-trace-is-missing-or-unstable"
dateAdded: "2026-11-24"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the ECG trace on the TE X was intermittently noisy and disappeared during examinations."
  cause: "Clinical Engineering found damage at the strain relief of the external ECG patient cable."
  resolution: "Clinical Engineering replaced the damaged cable with an approved compatible cable and verified a stable ECG trace using approved test equipment."
helpfulDetails:
  - "Trace affected"
  - "Whether trace was missing or noisy"
  - "Cable and lead condition"
  - "Connector condition"
  - "Electrode/contact condition"
  - "Effect of cable movement"
  - "Known-good accessory result"
  - "Simulator result"
  - "Environmental interference noted"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots missing or unstable physiologic traces caused by leads, cables, accessories, connections, settings, placement, or electrical interference.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Use Appropriate Monitoring
Do not rely on the TE X physiologic trace as the sole monitoring pathway if it is missing or unstable. Maintain required patient monitoring using verified equipment.

Expected outcome: Appropriate clinical monitoring continues independently of the affected ultrasound input.

### 2. Confirm the Exact Trace Problem
Determine whether no waveform appears, the trace is intermittent, excessively noisy, obviously unstable, or disappears with cable movement.

Expected outcome: The symptom is clearly characterized before components are substituted.

### 3. Verify the Correct Input and Display Selection
Confirm the intended physiologic input is connected and that the corresponding trace is enabled through normal user controls.

Expected outcome: The selected trace appears when a valid signal is present.

### 4. Inspect Leads and Patient Cable
Inspect accessible leads, cable, connector, strain reliefs, and accessories for damage, contamination, bent contacts, or loose connections.

Expected outcome: The signal pathway is intact and securely connected. Damaged accessories are removed from use.

### 5. Verify Electrode and Patient Connections
When applicable and clinically appropriate, confirm electrodes are suitable, connected correctly, making good contact, and not dried out, loose, or positioned where motion creates excessive artifact.

Expected outcome: Stable signal contact produces a consistent trace.

### 6. Check for Cable Movement and Strain
Route the physiologic cable away from moving cart components, power cords, and areas where it can be pulled or pinched. Observe whether movement reproduces the instability.

Expected outcome: Normal cable movement does not interrupt the trace.

### 7. Check for Electrical Interference
Move nonessential interference sources away when appropriate and verify cables are separated from obvious high-noise equipment. Do not defeat protective grounding or modify electrical systems.

Expected outcome: The trace is stable in the normal clinical environment.

### 8. Use a Known-Good Accessory or Simulator
When appropriate, substitute a compatible known-good patient cable or use approved simulation/test equipment to determine whether the problem is accessory-related or remains with the TE X input.

Expected outcome: A stable simulated or known-good signal identifies the failing portion of the external pathway.

### 9. Perform Final Functional Verification
Verify a stable physiologic trace using approved test methods and confirm normal operation without intermittent loss or excessive noise.

Expected outcome: The trace remains stable. If the TE X cannot reliably display the test signal, remove the affected function or system from service.

## If the Problem Persists

Lead condition, cable integrity, connections, user settings, signal contact, environmental interference, and known-good testing have been addressed. Remaining causes may involve the physiologic input interface, internal signal processing, configuration, or other service-level electronics.

Remove the TE X from service if the physiologic function is required for its intended clinical use and cannot be verified. Label it **Out of Service** and obtain bench evaluation using appropriate Mindray documentation and approved simulators or test equipment.

Repairs should be performed only by qualified personnel. Complete applicable functional and safety testing before return to service.

## Clinical Use Tip

Always maintain a separate verified monitoring method when a physiologic trace used with ultrasound becomes unreliable.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain independent patient monitoring, verify the entire external signal pathway before suspecting internal electronics, and use controlled test signals to support safe repair decisions and documentation.

That is successful troubleshooting.
