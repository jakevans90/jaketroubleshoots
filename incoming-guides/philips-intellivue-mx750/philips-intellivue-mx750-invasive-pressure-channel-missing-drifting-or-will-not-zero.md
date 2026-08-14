---
schemaVersion: 1
title: "Philips IntelliVue MX750 Patient Monitor - Invasive Pressure Channel Missing, Drifting, or Will Not Zero"
issueTitle: "Invasive Pressure Channel Missing, Drifting, or Will Not Zero"
description: "Troubleshoots missing, drifting, or non-zeroing invasive pressure caused by transducers, cables, setup, leveling, stopcocks, connections, or measurement hardware."
assetType: "Patient Monitor"
manufacturer: "Philips"
model: "IntelliVue MX750"
slug: "philips-intellivue-mx750-invasive-pressure-channel-missing-drifting-or-will-not-zero"
dateAdded: "2026-08-14"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that one invasive pressure channel on the IntelliVue MX750 would not zero."
  cause: "Clinical Engineering found the pressure interface cable was not fully seated at the measurement module."
  resolution: "Clinical Engineering reseated the cable and verified channel recognition, successful zeroing, stable simulated pressure waveform, and alarm function."
helpfulDetails:
  - "Pressure channel affected"
  - "Whether the channel was visible"
  - "Zeroing behavior"
  - "Transducer level and stopcock position"
  - "Cable and connector condition"
  - "Known-good cable or transducer result"
  - "Alternate pressure input result"
  - "Simulator test result"
  - "Waveform stability after correction"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots missing, drifting, or non-zeroing invasive pressure caused by transducers, cables, setup, leveling, stopcocks, connections, or measurement hardware.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Reliable Pressure Monitoring
If the invasive pressure is being used for critical clinical decisions and is missing, unstable, or unable to zero, establish another verified monitoring method before troubleshooting.

**Expected outcome:** Clinical care does not depend on an unreliable pressure channel.

### 2. Confirm the Exact Pressure Failure
Determine whether the channel is absent, waveform is missing, values drift, zeroing fails, or the issue affects only one transducer or pressure input.

**Expected outcome:** The complaint is narrowed to detection, waveform acquisition, setup, or zeroing.

### 3. Inspect the Transducer and Cable Connections
Check the pressure transducer cable, adapter cable, module connection, connector pins, strain reliefs, and accessible interfaces for looseness, contamination, moisture, or physical damage.

**Expected outcome:** All connections are intact and fully seated. If reseating restores the channel, proceed to verification.

### 4. Verify the Fluid System and Stopcock Position
Working within facility policy and without disrupting patient care, confirm that the transducer setup is connected appropriately, stopcocks are positioned correctly, tubing is not kinked, and the system is not obviously leaking or obstructed.

**Expected outcome:** The external fluid path is correctly arranged for monitoring and zeroing.

### 5. Verify Transducer Level and Zeroing Conditions
Confirm the transducer is leveled according to clinical practice and that the zeroing pathway is correctly opened to atmospheric pressure when zeroing is performed. Avoid changing unrelated calibration settings.

**Expected outcome:** The channel zeros normally and returns to a plausible waveform when reconnected to the patient system.

### 6. Substitute Known-Good External Components
If appropriate, use a known-good compatible transducer cable or test transducer to determine whether the failure follows the accessory.

**Expected outcome:** The pressure channel operates normally with known-good external components. If so, remove the defective accessory from use.

### 7. Test Another Compatible Pressure Input
When multiple compatible inputs are available, connect the test setup to another approved pressure channel or module input.

**Expected outcome:** The pressure signal works on another channel. A failure isolated to one input suggests a channel-specific monitor or module problem.

### 8. Test With a Pressure Simulator
Remove the monitor from patient use and connect an approved invasive-pressure simulator using known-good cables. Verify channel recognition, zero capability, stable waveform, numeric pressure display, and alarms.

**Expected outcome:** The pressure channel responds normally to a controlled simulated input.

### 9. Perform Final Functional Verification
After correction, verify stable channel recognition, successful zeroing, pressure waveform, numeric readings, labeling, and applicable alarms.

**Expected outcome:** The invasive pressure channel remains stable and functional. If so, troubleshooting is complete.

### 10. Escalate Persistent Pressure Channel Problems
If external connections, transducer setup, leveling, stopcocks, cables, alternate inputs, and simulator testing do not resolve the issue, stop external troubleshooting.

**Expected outcome:** The affected monitor or measurement module is removed from service for qualified bench evaluation.

## If the Problem Persists
Common external pressure-monitoring causes have been ruled out. The remaining problem may involve the pressure measurement interface, module electronics, internal communication, configuration, or service-level calibration.

The affected equipment should be:
- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Philips documentation and approved pressure-simulation equipment
- Repaired, configured, or calibrated only by qualified personnel

Following repair, verify pressure-channel detection, zeroing, simulated accuracy, waveform stability, and alarms before return to service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
Always verify transducer level and stopcock position before treating a drifting or abnormal invasive pressure value as a monitor failure.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Check the patient-side setup, level, zero pathway, cables, and measurement input before assuming internal failure. Verify the complete pressure-monitoring chain and escalate unresolved channel faults appropriately.

That is successful troubleshooting.
