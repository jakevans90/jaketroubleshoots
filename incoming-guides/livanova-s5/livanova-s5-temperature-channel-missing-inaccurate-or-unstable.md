---
schemaVersion: 1
title: "LivaNova S5 Heart-Lung Machine - Temperature Channel Missing, Inaccurate, or Unstable"
issueTitle: "Temperature Channel Missing, Inaccurate, or Unstable"
description: "Troubleshoots absent, inaccurate, or unstable temperature readings by checking probes, adapters, connections, channel selection, positioning, and known-good comparisons."
assetType: "Heart-Lung Machine"
manufacturer: "LivaNova"
model: "S5"
slug: "livanova-s5-temperature-channel-missing-inaccurate-or-unstable"
dateAdded: "2026-09-15"
taxonomyMode: "reuse"
ccr:
  complaint: "Perfusion reported that one S5 temperature channel intermittently disappeared during equipment setup."
  cause: "Clinical Engineering found a damaged temperature-probe cable that opened intermittently when flexed near the connector."
  resolution: "Clinical Engineering replaced the probe with a known-good compatible probe and verified stable temperature indication during controlled testing."
helpfulDetails:
  - "Temperature channel affected"
  - "Probe and adapter used"
  - "Physical probe condition"
  - "Connector condition"
  - "Whether movement causes dropout"
  - "Comparison method"
  - "Known-good probe results"
  - "Channel configuration"
  - "Before-and-after readings"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots absent, inaccurate, or unstable temperature readings by checking probes, adapters, connections, channel selection, positioning, and known-good comparisons.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Use Verified Temperature Monitoring

Do not rely on a temperature channel known to be missing, unstable, or inaccurate during patient support. Provide an alternate verified temperature-monitoring method before technical troubleshooting.

**Expected outcome:** Patient temperature is monitored using reliable equipment while the affected channel is evaluated.

Once the suspect channel is no longer required clinically, troubleshooting may continue.

### 2. Confirm the Exact Temperature Problem

Determine whether the channel:

- Is completely absent.
- Displays an implausible value.
- Drifts slowly.
- Changes abruptly.
- Is intermittent when the cable moves.
- Differs from another clinically appropriate comparison source.
- Fails only on one probe or one system channel.

**Expected outcome:** The problem is isolated to a missing signal, unstable signal, or suspected accuracy discrepancy.

If readings are stable and consistent after reproducing the setup correctly, troubleshooting can stop.

### 3. Inspect the Temperature Probe

Inspect the probe and its accessible cable for:

- Cuts
- Kinks
- Damaged insulation
- Bent connector components
- Fluid intrusion
- Loose strain relief
- Visible contamination

Confirm the probe is compatible with the intended system input.

**Expected outcome:** The temperature probe and cable are compatible and physically intact.

If replacing a damaged probe with a known-good compatible probe restores stable readings, troubleshooting can stop after verification.

### 4. Check Probe and Adapter Connections

Verify the probe is fully connected to the correct temperature input. Inspect any external adapter or extension cable used in the signal path.

Reseat accessible connections and avoid unnecessary adapters when testing.

**Expected outcome:** The complete external temperature signal path is securely connected.

If reseating a connector restores stable readings, troubleshooting can stop after testing.

### 5. Verify Probe Position and Test Conditions

Ensure any comparison test uses the probe in a stable, appropriate test environment. Do not compare probes exposed to different thermal conditions and assume the channel is inaccurate.

**Expected outcome:** The reference and suspect readings are compared under equivalent, controlled conditions.

If the apparent discrepancy disappears under comparable conditions, troubleshooting can stop.

### 6. Compare With Known-Good Components

Use a known-good compatible probe on the suspect S5 channel. When appropriate, test the suspect probe on another verified compatible channel.

**Expected outcome:** The problem follows the probe/accessory or remains with the S5 channel.

If the problem follows the probe, replace the defective external component and verify normal operation.

### 7. Verify Channel Selection and Configuration

Confirm the displayed temperature source corresponds to the physical input being tested and that the expected channel is enabled in the normal configuration.

Do not change protected calibration constants without authorization.

**Expected outcome:** The displayed channel matches the connected probe and normal system configuration.

If correcting an authorized channel selection resolves the problem, troubleshooting can stop.

### 8. Perform Functional Verification

Using approved test equipment or an approved comparison method, verify:

- The channel is present.
- The displayed value is stable.
- Cable movement does not cause dropouts.
- A known-good probe produces consistent results.
- Other channels remain unaffected.

Do not claim calibration compliance unless the required calibrated test equipment and manufacturer procedure have been used.

**Expected outcome:** The temperature channel provides a stable and credible signal under controlled testing.

If all checks pass, troubleshooting is complete.

### 9. Escalate an Unresolved Temperature Channel Fault

If the channel remains missing, unstable, or cannot be verified against approved test equipment after external components are ruled out, remove the affected function from service.

Do not perform internal component replacement or calibration adjustment outside authorized procedures.

**Expected outcome:** An unverified temperature channel is not returned to clinical monitoring.

## If the Problem Persists

External probe, adapter, connection, positioning, and channel-selection causes have been ruled out. Remaining causes may involve internal signal conditioning, input circuitry, communication, protected calibration, or module-level failure.

The affected equipment should be:

- Removed from service.
- Labeled **Out of Service** if the system cannot safely operate without the channel.
- Sent for repair or bench evaluation.
- Evaluated using appropriate LivaNova documentation and approved calibrated test equipment.
- Repaired or calibrated only by qualified personnel.

Verify the complete temperature-monitoring path before return to service.

Knowing when an accuracy concern requires formal evaluation rather than further external troubleshooting is proper troubleshooting.

## Clinical Use Tip

When comparing temperature channels, verify both sensors are measuring the same controlled thermal condition before concluding that either channel is inaccurate.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Use verified alternate monitoring for the patient, then isolate the external probe and signal path before suspecting internal measurement electronics. Accuracy concerns require controlled comparison and appropriate test equipment, followed by clear escalation and documentation when the channel cannot be verified.

That is successful troubleshooting.
