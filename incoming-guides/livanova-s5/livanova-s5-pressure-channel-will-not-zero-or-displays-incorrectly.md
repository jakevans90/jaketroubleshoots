---
schemaVersion: 1
title: "LivaNova S5 Heart-Lung Machine - Pressure Channel Will Not Zero or Displays Incorrectly"
issueTitle: "Pressure Channel Will Not Zero or Displays Incorrectly"
description: "Troubleshoots pressure channels that will not zero or display correctly by checking transducers, cables, stopcocks, setup, connections, and configuration."
assetType: "Heart-Lung Machine"
manufacturer: "LivaNova"
model: "S5"
slug: "livanova-s5-pressure-channel-will-not-zero-or-displays-incorrectly"
dateAdded: "2026-09-15"
taxonomyMode: "reuse"
ccr:
  complaint: "Perfusion reported that one S5 pressure channel would not zero during pre-case setup."
  cause: "Clinical Engineering found the external stopcock arrangement left residual pressure on the transducer during the zero attempt."
  resolution: "Clinical Engineering corrected the test setup and verified successful zeroing and stable pressure response using approved test equipment."
helpfulDetails:
  - "Pressure channel affected"
  - "Transducer type"
  - "Cable condition"
  - "Stopcock/tubing configuration"
  - "Whether the channel zeroed"
  - "Baseline reading"
  - "Known-good substitution results"
  - "Pressure test equipment used"
  - "Response to applied test pressure"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots pressure channels that will not zero or display correctly by checking transducers, cables, stopcocks, setup, connections, and configuration.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Use Verified Pressure Monitoring

Do not rely on an S5 pressure channel that cannot be zeroed or produces questionable values during patient care. Establish an alternate verified pressure-monitoring method before technical troubleshooting.

**Expected outcome:** Clinically important pressure remains monitored independently of the suspect channel.

Once the affected channel is removed from patient dependency, troubleshooting may continue.

### 2. Confirm the Exact Pressure Problem

Determine whether the channel:

- Will not zero.
- Displays an offset at atmospheric pressure.
- Shows unstable or drifting values.
- Is absent.
- Responds incorrectly to pressure changes.
- Fails only with one transducer or cable.

Record the displayed condition or message.

**Expected outcome:** The failure is categorized as zeroing, signal, stability, or accessory related.

If the channel zeros normally and passes controlled verification, troubleshooting can stop.

### 3. Verify the Transducer Setup

Inspect the pressure transducer and fluid path used for testing. Confirm:

- The correct compatible transducer is being used.
- The transducer is properly connected.
- The reference port is opened appropriately for the normal zeroing process.
- Stopcocks and tubing are arranged correctly.
- There is no obvious fluid blockage or trapped pressure during zeroing.

**Expected outcome:** The transducer is actually exposed to the correct zero-reference condition.

If correcting the external fluid setup allows successful zeroing, troubleshooting can stop after verification.

### 4. Inspect the Transducer and Cable

Check the transducer, interface cable, and connectors for:

- Damage
- Bent contacts
- Fluid contamination
- Loose connections
- Cable cuts
- Strain
- Corrosion

Replace visibly compromised external components with approved compatible parts.

**Expected outcome:** The external pressure-sensing components are intact and securely connected.

If replacement of a damaged transducer or cable restores normal operation, troubleshooting can stop after testing.

### 5. Reseat the Pressure Connection

With the equipment out of clinical use, disconnect and reconnect the approved external pressure interface. Ensure the connector is fully seated.

**Expected outcome:** The pressure channel detects the connected transducer consistently.

If reseating restores stable operation and successful zeroing, troubleshooting can stop.

### 6. Compare With Known-Good Components

Test a known-good compatible pressure transducer and cable on the suspect channel. When appropriate, test the suspect external components on another verified compatible channel.

**Expected outcome:** The fault follows an external transducer/cable or remains with the S5 pressure channel.

If the external component is identified as defective, replace it and verify the channel.

### 7. Verify Channel Selection and Configuration

Confirm the physical pressure input matches the displayed channel and that the channel is enabled in the normal system configuration.

Do not alter protected calibration parameters or pressure scaling without authorized procedures.

**Expected outcome:** The configured channel corresponds to the connected pressure input.

If correcting an authorized configuration mismatch resolves the issue, troubleshooting can stop.

### 8. Perform Controlled Pressure Verification

Using approved pressure test equipment and the appropriate manufacturer procedure, verify:

- Successful zeroing
- Stable baseline
- Predictable response to applied test pressure
- Return to zero
- No dropout during cable movement

Do not state that the channel is calibrated unless calibration has actually been completed using the required procedure and calibrated equipment.

**Expected outcome:** The pressure channel zeros correctly and provides stable, credible readings during controlled testing.

If all checks pass, troubleshooting is complete.

### 9. Escalate an Unresolved Pressure Fault

If the channel cannot zero or readings remain inaccurate after external transducer, tubing, cable, and setup causes are eliminated, remove the affected monitoring function from service.

Do not perform internal electronic adjustment without authorized procedures.

**Expected outcome:** An unverified pressure channel is not returned to patient monitoring.

## If the Problem Persists

Common transducer, fluid-path, cable, connection, and configuration causes have been ruled out. Remaining causes may involve internal input circuitry, signal conditioning, protected calibration, communication, or module-level failure.

The affected equipment should be:

- Removed from service.
- Labeled **Out of Service** if clinically required functionality is unavailable.
- Sent for repair or bench evaluation.
- Evaluated using appropriate LivaNova documentation and approved calibrated test equipment.
- Repaired or calibrated only by qualified personnel.

Complete zero, pressure-response, alarm, and functional verification before return to service.

Knowing when to stop rather than trusting an unverified pressure value is proper troubleshooting.

## Clinical Use Tip

Always confirm the transducer is truly open to the intended reference condition before treating a zeroing failure as an equipment fault.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect clinical pressure monitoring first, then verify the transducer, fluid path, connections, and channel configuration before suspecting internal electronics. Use approved test equipment for accuracy verification and escalate any channel that cannot be proven reliable.

That is successful troubleshooting.
