---
schemaVersion: 1
title: "GE Healthcare MAC 7 Electrocardiograph (EKG) Machine - Waveforms Are Clipped or Mis-scaled After Gain/Filter Configuration Changes"
issueTitle: "Waveforms Are Clipped or Mis-scaled After Gain/Filter Configuration Changes"
description: "Troubleshoot clipped, compressed, enlarged, or otherwise mis-scaled ECG waveforms following gain, filter, display, or acquisition configuration changes."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "GE Healthcare"
model: "MAC 7"
slug: "ge-healthcare-mac-7-waveforms-are-clipped-or-mis-scaled-after-gain-filter-configuration-changes"
dateAdded: "2026-10-27"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that ECG waveforms appeared enlarged and clipped after configuration changes were made on the MAC 7."
  cause: "Clinical Engineering found that the ECG gain configuration differed from the facility's approved MAC 7 configuration while the simulator signal and patient cable tested normally."
  resolution: "Restored the approved gain configuration and verified normal unclipped waveforms on the display, acquired ECG, and printed report using an ECG simulator."
helpfulDetails:
  - "Whether clipping affected all or selected leads."
  - "Live display versus acquired ECG appearance."
  - "Print or stored-record appearance."
  - "Gain setting observed."
  - "Filter configuration observed."
  - "Recent configuration changes."
  - "Patient cable condition."
  - "Known-good cable substitution."
  - "ECG simulator used."
  - "Known-good device comparison."
  - "Results before and after configuration correction."
  - "Transmission or stored-record verification."
  - "Final device status."
---

## What This Guide Helps With

Troubleshoot clipped, compressed, enlarged, or otherwise mis-scaled ECG waveforms following gain, filter, display, or acquisition configuration changes.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Diagnostic ECG Quality

Do not rely on an ECG tracing that appears clipped, distorted, or incorrectly scaled for clinical interpretation.

If a diagnostic ECG is immediately required, use another verified electrocardiograph or restore an approved known-good configuration before acquiring the clinical tracing.

**Expected outcome:** Clinical decisions are not based on a questionable waveform presentation.

### 2. Confirm the Exact Waveform Problem

Determine whether the abnormal appearance affects:

- The live waveform display.
- The printed ECG.
- The stored ECG.
- The transmitted ECG.
- All leads or selected leads.
- One patient or every acquisition.

Confirm that the issue began after a gain, filter, or related configuration change.

**Expected outcome:** The problem is localized to display, acquisition, printing, stored data, or configuration. If the waveform is normal throughout the complete workflow, troubleshooting can stop.

### 3. Inspect the Patient Cable and Lead Connections

Before assuming a configuration problem, inspect the ECG patient cable, lead wires, and external connections.

Check for:

- Loose connectors.
- Damaged lead wires.
- Bent or contaminated contacts.
- Incorrect lead placement during testing.
- Intermittent connections.

For bench testing, use an approved ECG simulator and known-good patient cable when available.

**Expected outcome:** External ECG signal connections are intact and stable. If replacing or reseating an external cable restores normal waveforms, verify all leads and stop troubleshooting.

### 4. Use a Controlled ECG Simulator Signal

Connect an approved ECG simulator and select a stable test waveform appropriate for functional verification.

A simulator removes patient movement, skin preparation, electrode condition, and physiologic variation from the troubleshooting process.

**Expected outcome:** The MAC 7 receives a stable, repeatable input signal suitable for evaluating gain and waveform presentation.

### 5. Verify Gain Settings

Review the currently selected gain or amplitude setting through the normal authorized controls.

Compare it with:

- The approved clinical default.
- A known-good MAC 7.
- The expected facility ECG configuration.

If the setting was recently changed, restore the authorized known-good value rather than guessing at a replacement configuration.

**Expected outcome:** Waveform amplitude appears appropriate and is not artificially enlarged, compressed, or clipped. If restoring the approved gain resolves the problem, complete final verification and stop troubleshooting.

### 6. Verify Filter Configuration

Review the active ECG filter configuration and compare it with the approved clinical configuration.

Filters can change waveform appearance, but Clinical Engineering should not select arbitrary settings simply to make a tracing appear better.

Restore only documented facility or manufacturer-approved settings.

**Expected outcome:** Active filtering matches the intended diagnostic configuration. If the waveform returns to normal after an authorized correction, verify acquisition, printout, and storage before stopping.

### 7. Check Display and Acquisition Configuration Separately

Determine whether the live display configuration differs from the configuration applied to acquired or printed ECGs.

Acquire a simulator ECG and compare:

- Live waveform appearance.
- Acquired waveform.
- Printed report when applicable.
- Stored record.
- Transmitted record when part of the workflow.

**Expected outcome:** The waveform is scaled consistently through the intended clinical workflow, or the problem is isolated to a specific stage.

### 8. Compare With a Known-Good Device

Using the same ECG simulator and, when appropriate, the same known-good patient cable, compare the signal on another MAC 7 or equivalent verified electrocardiograph.

Do not change multiple settings simultaneously during the comparison.

**Expected outcome:** A known-good comparison confirms whether the abnormal appearance follows the MAC 7 configuration/device or the external signal path.

### 9. Restore the Approved Configuration if Available

If the issue began after configuration changes and the approved previous configuration is documented, restore the relevant authorized settings.

Do not perform an undocumented factory reset or alter unrelated clinical configuration.

After restoration, restart the unit normally if required by the approved workflow.

**Expected outcome:** The device returns to its established clinical configuration and displays the simulator waveform normally.

### 10. Perform Final Functional Verification

With the approved ECG simulator:

1. Verify stable waveforms on all expected leads.
2. Confirm waveforms are not clipped.
3. Confirm amplitude presentation is appropriate.
4. Verify the intended filter and gain configuration.
5. Acquire an ECG.
6. Review the stored or printed waveform.
7. Verify transmission if networked ECG transfer is part of the clinical workflow.

**Expected outcome:** Waveforms remain correctly presented through display, acquisition, output, and storage. If all checks pass, troubleshooting can stop and the MAC 7 may be returned to service according to facility policy.

### 11. Escalate Persistent Waveform Distortion

If clipping or abnormal scaling remains with an approved simulator, known-good patient cable, and verified configuration, remove the MAC 7 from service.

Do not compensate for an unexplained hardware or software problem by creating nonstandard clinical settings.

**Expected outcome:** A potentially unreliable diagnostic ECG device is prevented from returning to patient use until evaluated further.

## If the Problem Persists

If the patient cable, simulator input, gain settings, filter configuration, display/acquisition configuration, and approved defaults have been verified, common external causes have been ruled out.

Remaining categories may include signal-processing software, stored configuration corruption, acquisition circuitry, display processing, or another internal service-level problem.

The MAC 7 should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate manufacturer documentation and approved ECG test equipment.
- Repaired or configured only by qualified personnel.

Do not perform internal board-level troubleshooting or compensate for unresolved distortion by changing clinical gain or filter settings outside approved standards.

Before return to service, perform a complete ECG functional test using a calibrated or otherwise approved simulator and verify display, acquisition, stored output, print output when applicable, and transmission.

Knowing when a waveform problem has moved beyond safe configuration troubleshooting is proper troubleshooting.

## Clinical Use Tip

After changing ECG gain or filters, verify an acquired tracing with an ECG simulator rather than judging correct operation from the live display alone.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- rendered from front matter -->

## Final Thought

Protect diagnostic ECG quality, verify the external signal path and approved configuration before assuming internal failure, use a controlled simulator for confirmation, and escalate any unexplained waveform distortion.

That is successful troubleshooting.
