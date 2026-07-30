---
schemaVersion: 1
title: "Mortara ELI Series Electrocardiograph (EKG) Machine - Acquisition Module Or Patient Cable Not Recognized"
issueTitle: "Acquisition Module Or Patient Cable Not Recognized"
description: "Troubleshooting an unrecognized acquisition module or patient cable caused by connection, accessory, contamination, compatibility, or external cable damage."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "Mortara"
model: "ELI Series"
slug: "mortara-eli-series-acquisition-module-or-patient-cable-not-recognized"
dateAdded: "2026-07-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Mortara ELI Series EKG machine displayed no usable leads and did not recognize the connected patient cable."
  cause: "Clinical Engineering found a damaged patient cable connector that failed recognition while a known-good compatible cable operated normally."
  resolution: "Replaced the damaged patient cable, acquired a stable simulator ECG on all expected leads, and returned the unit to service."
helpfulDetails:
  - "Complete displayed message."
  - "Whether the module was never recognized or intermittently disconnected."
  - "Patient cable and acquisition module identifiers."
  - "Connector and strain-relief condition."
  - "Cleaning or fluid exposure history."
  - "Known-good accessory used."
  - "Lead-off behavior."
  - "Results of simulator testing."
  - "Final device status."
---

## What This Guide Helps With

Troubleshooting an unrecognized acquisition module or patient cable caused by connection, accessory, contamination, compatibility, or external cable damage.

## Step-by-Step Troubleshooting

### 1. Ensure Patient Safety and Continuity of Care

Do not continue relying on an EKG machine that cannot detect its acquisition module or patient cable when an ECG is clinically required.

Notify the responsible clinical staff. Move the patient to another verified EKG machine if the tracing cannot be obtained promptly. Do not delay time-sensitive cardiac assessment while troubleshooting.

**Expected outcome:** The patient’s ECG needs are supported by a verified alternate device before technical troubleshooting continues.

### 2. Confirm the Exact Reported Condition

Determine whether the ELI Series device:

- Does not detect the acquisition module at all.

- Detects the module intermittently.

- Displays lead-off indications for every lead.

- Recognizes one patient cable but not another.

- Developed the problem after cleaning, transport, cable replacement, or impact.

Restart the test workflow and record the complete displayed message or behavior.

**Expected outcome:** The failure is clearly identified as a recognition problem rather than poor electrode contact, individual lead failure, or general startup failure.

### 3. Inspect the Acquisition Module and Patient Cable

Remove the device from patient use before disconnecting or manipulating the cable.

Inspect the acquisition module, trunk cable, lead wires, strain reliefs, connector shell, and locking features for:

- Bent or recessed contacts.

- Cracked housings.

- Pinched or stretched cable sections.

- Fluid residue or dried cleaning solution.

- Loose connector parts.

- Evidence of impact or improper storage.

Do not use an accessory with exposed conductors, damaged insulation, corrosion, or loose connector hardware.

**Expected outcome:** The cable assembly is clean, dry, physically intact, and free of obvious damage. If damage is found, replace the affected accessory and stop troubleshooting after successful verification.

### 4. Reseat All External Connections

Power the EKG machine down using the normal shutdown process when possible.

Disconnect the acquisition module or patient cable from the device, inspect the mating connector, and reconnect it fully without forcing it. Confirm that any latch, locking collar, or keyed orientation is correctly engaged.

Reconnect removable lead-wire sets to the acquisition module where applicable.

**Expected outcome:** The accessory seats securely and is recognized after restart. If normal recognition returns consistently, troubleshooting can stop.

### 5. Check for Contamination or Moisture

Examine accessible connector surfaces for moisture, gel, lint, adhesive residue, disinfectant buildup, or debris.

Clean only with methods approved by the facility and manufacturer documentation. Allow all parts to dry completely before reconnecting. Do not spray liquid directly into connectors.

**Expected outcome:** Connector surfaces are dry and unobstructed, and the module is recognized consistently. If cleaning corrects the issue, complete final verification and stop.

### 6. Separate Recognition Failure From Lead-Off Conditions

Connect the patient cable to an approved ECG simulator or appropriately prepared test setup.

Observe whether the machine recognizes the acquisition module but reports individual or multiple leads off. If the module is recognized, inspect electrode clips, snaps, lead wires, and simulator connections rather than treating the issue as a total module-recognition failure.

**Expected outcome:** The device distinguishes between an attached module and individual lead-contact problems.

### 7. Test With a Known-Good Compatible Accessory

Use a known-good, compatible acquisition module or patient cable approved for the specific ELI Series configuration.

Do not substitute an accessory solely because the connector appears similar. Confirm compatibility through inventory records, labeling, or approved documentation.

**Expected outcome:**

If the known-good accessory is recognized, the original cable or module is defective and should be removed from use.

If neither accessory is recognized, the problem likely involves the EKG machine, configuration, or connector interface.

Troubleshooting may stop after the defective accessory is replaced and the system passes verification.

### 8. Verify Relevant Device Configuration

Review only normal operator-accessible configuration items related to acquisition hardware or connected accessories.

Confirm that no recent approved configuration change, software update, or device swap introduced an accessory mismatch. Do not enter restricted service menus or alter calibration data.

**Expected outcome:** The configured acquisition hardware matches the connected approved accessory.

### 9. Perform Final Functional Verification

Using a known-good acquisition module, patient cable, lead set, and ECG simulator:

Confirm the accessory is recognized at startup.

Verify all expected leads display.

Gently flex external cable sections to check for intermittent loss.

Acquire and review a test ECG.

Confirm no repeated recognition or lead-connection errors occur.

**Expected outcome:** The EKG machine consistently recognizes the acquisition system and produces a stable test tracing. The device may be returned to service after required inspection and documentation.

### 10. Escalate When Recognition Remains Unreliable

Remove the device from service if:

- Known-good compatible accessories are not recognized.

- Recognition is intermittent.

- The device connector is loose, damaged, contaminated internally, or recessed.

- The unit loses the module when the cable is lightly moved.

- A safe and complete ECG cannot be acquired.

**Expected outcome:** An unreliable EKG machine is prevented from returning to clinical use.

## If the Problem Persists

Common external causes involving seating, contamination, cable damage, lead connections, and accessory compatibility have been ruled out. The remaining fault may involve the device connector assembly, internal acquisition interface, software configuration, or another service-level condition.

The device should be:

- Removed from service.

- Labeled Out of Service.

- Sent for repair or bench evaluation.

- Evaluated using appropriate Mortara documentation and approved test equipment.

- Repaired or configured only by qualified personnel.

After repair, complete electrical safety testing when required, verify recognition with approved accessories, acquire a simulator ECG, and confirm stable operation before return to service.

Knowing when to stop external troubleshooting and escalate an unreliable acquisition path is proper troubleshooting.

## Clinical Use Tip

Move the patient to another verified EKG machine before troubleshooting any acquisition system that cannot reliably display all required leads.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient first, verify external cables and connections before assuming an internal failure, and remove the device from service when acquisition remains unreliable. Clear CCR documentation should identify the reported condition, confirmed cause, corrective action, and final functional test.

That is successful troubleshooting.
