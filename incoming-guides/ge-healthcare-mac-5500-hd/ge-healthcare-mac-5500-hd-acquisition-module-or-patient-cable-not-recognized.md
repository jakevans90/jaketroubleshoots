---
schemaVersion: 1
title: "GE Healthcare MAC 5500 HD Electrocardiograph (EKG) Machine - Acquisition Module Or Patient Cable Not Recognized"
issueTitle: "Acquisition Module Or Patient Cable Not Recognized"
description: "Troubleshooting an unrecognized acquisition module or patient cable caused by loose connections, damage, contamination, incompatibility, or an external accessory failure."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "GE Healthcare"
model: "MAC 5500 HD"
slug: "ge-healthcare-mac-5500-hd-acquisition-module-or-patient-cable-not-recognized"
dateAdded: "2026-07-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the MAC 5500 HD did not recognize the acquisition module and could not acquire a 12-lead ECG."
  cause: "Clinical Engineering found that the patient cable connector was not fully seated and lost contact when the cable was repositioned."
  resolution: "Clinical Engineering reseated and secured the connector, verified stable recognition with an ECG simulator, and returned the unit to service."
helpfulDetails:
  - "Exact displayed message"
  - "Whether recognition failed at startup or during use"
  - "Acquisition module and patient cable tested"
  - "Connector and strain-relief condition"
  - "Results of known-good substitution"
  - "Whether the issue followed the accessory"
  - "Simulated ECG results"
  - "Final device status"
---

## What This Guide Helps With

Troubleshooting an unrecognized acquisition module or patient cable caused by loose connections, damage, contamination, incompatibility, or an external accessory failure.

## Step-by-Step Troubleshooting

### 1. Ensure Patient Safety and Continuity of Care

Do not rely on the MAC 5500 HD for diagnostic ECG acquisition when the acquisition module or patient cable is not consistently recognized.

Stop the current acquisition attempt.

Notify clinical staff that the ECG system is not ready for use.

Use another verified electrocardiograph when the ECG is clinically urgent.

Do not repeatedly connect or disconnect patient-applied cables while the patient remains connected.

**Expected outcome:** The patient is disconnected safely from unreliable equipment and ECG testing continues on another verified device when required.

### 2. Confirm the Exact Recognition Failure

Determine whether:

- The acquisition module is not detected at startup.

- The module disconnects intermittently.

- Lead waveforms are absent despite the module being displayed.

- The problem began after a cable, module, or accessory change.

- The issue occurs with every patient or only one setup.

- Record any displayed message without assuming that it identifies a failed internal component.

**Expected outcome:** The failure is clearly defined as a recognition, intermittent connection, or signal-path problem.

### 3. Perform a Controlled Restart

Disconnect the patient and power the electrocardiograph down normally.

Disconnect the acquisition module or patient cable.

Wait briefly for the unit to shut down completely.

Reconnect the accessory firmly.

Restart the device and observe whether the accessory is recognized.

Do not force connectors or use damaged connector hardware.

**Expected outcome:** The module or patient cable is detected normally after restart. If recognition remains stable, troubleshooting can stop after final verification.

### 4. Inspect the External Connectors

Inspect the device connection, acquisition module connector, cable strain reliefs, and connector pins or contacts.

Look for:

- Bent, recessed, loose, or contaminated contacts

- Cracked connector shells

- Damaged locking features

- Fluid residue

- Cable cuts, crushing, or severe twisting

- Loose strain reliefs

- Remove the accessory from use if electrical conductors, contacts, or insulation appear damaged.

**Expected outcome:** Connectors are clean, dry, undamaged, and seat securely. Any visibly defective cable or module is removed from service.

### 5. Verify Correct Connection and Seating

Reconnect the acquisition module or patient cable using the correct orientation.

Confirm the connector is fully inserted.

Verify any latch or locking feature engages.

Ensure the cable is not partially pulled out by its own weight.

Position the cable so it is not under tension.

**Expected outcome:** The connection remains secure when the cable is gently repositioned. If recognition returns and remains stable, troubleshooting can stop.

### 6. Check for Cable Movement or Intermittency

With no patient connected, observe the device while gently moving the cable near each strain relief and connector.

Do not sharply bend or twist the cable.

Watch for:

- Recognition appearing and disappearing

- Waveform channels dropping out

- Status changes when the cable is moved

- Unexpected restart or interface response

**Expected outcome:** Recognition remains stable during gentle movement. A repeatable dropout indicates the affected accessory should be replaced or sent for evaluation.

### 7. Substitute a Known-Good Compatible Accessory

When available, connect a verified compatible acquisition module or patient cable.

Use only accessories approved for the device configuration.

Change one component at a time.

Repeat startup and basic lead-signal verification.

**Expected outcome:** If the known-good accessory is recognized, the original accessory is the likely cause and should be removed from service. Troubleshooting can stop after documentation and final testing.

### 8. Test the Suspect Accessory on Another Compatible Unit

When safe and available, connect the suspect accessory to another verified compatible MAC system.

Do not transfer an accessory that is contaminated, physically damaged, or electrically unsafe.

**Expected outcome:** If the problem follows the accessory, remove that accessory from service. If the suspect accessory works normally elsewhere, the original electrocardiograph requires bench evaluation.

### 9. Perform Final Functional Verification

After correction:

- Confirm the acquisition module remains recognized.

- Connect an ECG simulator or approved test source.

- Verify all expected leads display consistently.

- Confirm there are no intermittent disconnects.

- Complete applicable electrical-safety and functional testing when an accessory or device repair was performed.

**Expected outcome:** The device consistently recognizes the accessory and acquires stable simulated ECG signals. The unit may be returned to service when all required tests pass.

## If the Problem Persists

Common external causes have been ruled out. The remaining possibilities may include an internal connector problem, interface circuitry fault, configuration issue, or another service-level failure.

The device should be:

- Removed from service

- Labeled Out of Service

- Sent for repair or bench evaluation

- Evaluated using appropriate GE Healthcare documentation and approved test equipment

- Repaired or configured only by qualified personnel

- Do not perform internal board-level repair or replace assemblies without the required service information and authorization. Return the electrocardiograph to service only after accessory recognition, ECG acquisition, and required safety testing are successfully completed.

- Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Move the patient to another verified ECG machine before troubleshooting an intermittent acquisition connection.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient first, define whether the failure follows the cable, module, or electrocardiograph, verify all external connections before assuming an internal defect, and document the final functional test and disposition clearly.

That is successful troubleshooting.
