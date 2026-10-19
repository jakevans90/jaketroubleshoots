---
schemaVersion: 1
title: "GE Healthcare CASE Stress Test System - Patient Cable, Lead, or Sensor Is Not Detected"
issueTitle: "Patient Cable, Lead, or Sensor Is Not Detected"
description: "ECG patient connections or configured sensors are not recognized, preventing expected signal acquisition during preparation for a stress study."
assetType: "Stress Test System"
manufacturer: "GE Healthcare"
model: "CASE"
slug: "ge-healthcare-case-patient-cable-lead-or-sensor-is-not-detected"
dateAdded: "2026-10-19"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that multiple ECG leads were not detected during setup of the GE Healthcare CASE system."
  cause: "Clinical Engineering found damage at the patient lead-set connector that caused intermittent contact."
  resolution: "Replaced the damaged lead set with a verified compatible accessory and confirmed stable detection of all required ECG channels."
helpfulDetails:
  - "Specific lead or sensor affected"
  - "Whether one or all channels were affected"
  - "Electrode condition"
  - "Patient cable and leadwire condition"
  - "Connector condition"
  - "Known-good accessory substitution results"
  - "Acquisition interface status"
  - "Results using a simulator or test source"
  - "Final device status"
---

## What This Guide Helps With
ECG patient connections or configured sensors are not recognized, preventing expected signal acquisition during preparation for a stress study.

## Step-by-Step Troubleshooting
### 1. Protect the Patient Before Troubleshooting
Do not troubleshoot an unreliable patient connection while the patient depends on CASE for monitoring during exercise. Stop the study or move monitoring to a verified alternate system as clinically appropriate.

**Expected outcome:** The patient is not dependent on an unreliable signal path while troubleshooting proceeds.

### 2. Confirm Which Connection Is Not Detected
Identify the exact cable, lead, electrode channel, or configured sensor reported as unavailable. Determine whether the problem affects one lead, several leads, all ECG acquisition, or another connected patient measurement.

Review the displayed indication without assuming the patient cable itself has failed.

**Expected outcome:** The failure is narrowed to a specific patient connection or the entire acquisition path.

### 3. Inspect Patient Preparation and Electrode Connections
For ECG-related complaints, verify electrodes are correctly positioned, firmly attached, and connected to the intended leadwires. Inspect for dried, loose, contaminated, or damaged electrodes and replace consumables when appropriate.

**Expected outcome:** All patient-side connections are secure and suitable for acquisition. If proper electrode replacement restores detection, verify the signal and stop troubleshooting.

### 4. Inspect the Patient Cable and Leadwires
Examine accessible cables, leadwires, connectors, strain reliefs, and pins for contamination, bent contacts, cracking, cuts, loose fittings, or other damage. Ensure connections are fully seated at both the patient lead set and acquisition interface.

Do not use damaged patient-connected accessories.

**Expected outcome:** External cabling is intact and securely connected. If reseating an intact connection restores detection, verify stable acquisition and stop troubleshooting.

### 5. Check for Incorrect or Incompatible Accessories
Confirm the attached cable, lead set, or sensor is intended for the installed CASE acquisition configuration. Compare part identification and connector type with a known working setup or approved documentation when necessary.

**Expected outcome:** The correct compatible accessory is connected. An incompatible accessory is removed from service rather than forced into use.

### 6. Test With a Known-Good Accessory
When available, substitute a verified compatible patient cable, lead set, or sensor. Keep the remainder of the setup unchanged so the test isolates the suspected accessory.

**Expected outcome:** If detection returns with the known-good accessory, the original accessory is the likely external cause and should be removed from use. Troubleshooting can stop after functional verification.

### 7. Verify the Acquisition Interface Connection
Check the external connection between the patient acquisition hardware and the CASE workstation or associated interface. Confirm connectors are fully seated and cables are not under tension or physically damaged.

Do not open the acquisition hardware.

**Expected outcome:** The acquisition interface is securely connected and recognized by the system.

### 8. Restart the Affected External Interface if Appropriate
With no patient dependent on the system, perform a normal supported restart of the CASE workstation and externally powered acquisition components when applicable. Do not enter unauthorized service menus or alter configuration parameters.

**Expected outcome:** The patient interface initializes normally and the previously missing connection is recognized.

### 9. Perform Final Signal Verification
Connect an appropriate simulator or approved test source when applicable and verify expected ECG channel detection and stable acquisition. Confirm all clinically required leads or sensors are available before release.

**Expected outcome:** Required patient inputs are consistently detected. The issue is resolved and troubleshooting can stop.

## If the Problem Persists
Patient preparation, consumables, cables, connectors, compatible accessories, and accessible acquisition connections have been checked. A persistent problem may involve the acquisition module, interface electronics, software recognition, configuration, or another service-level fault.

Remove the affected CASE system or acquisition component from service, label it **Out of Service**, and send it for repair or bench evaluation. Use appropriate manufacturer documentation and approved test equipment. Repair or configuration changes should be performed only by qualified personnel.

Complete functional verification of all required patient inputs before return to service.

## Clinical Use Tip
Verify stable ECG acquisition before exercise begins; a lead that is intermittently detected at rest may fail completely once the patient starts moving.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Start at the patient connection and work backward through consumables, cables, and interfaces before suspecting internal acquisition hardware. Protect the patient, isolate the failing part logically, verify the corrected signal path, and document the result.

That is successful troubleshooting.
