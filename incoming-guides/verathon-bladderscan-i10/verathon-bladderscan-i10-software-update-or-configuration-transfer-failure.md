---
schemaVersion: 1
title: "Verathon BladderScan i10 Bladder Scanner - Software Update or Configuration Transfer Failure"
issueTitle: "Software Update or Configuration Transfer Failure"
description: "Addresses failed updates or configuration transfers caused by power, media, files, connection, compatibility, authorization, or network conditions."
assetType: "Bladder Scanner"
manufacturer: "Verathon"
model: "BladderScan i10"
slug: "verathon-bladderscan-i10-software-update-or-configuration-transfer-failure"
dateAdded: "2026-08-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical Engineering reported that the BladderScan i10 would not recognize the approved software update package."
  cause: "Clinical Engineering found that the update file had been copied into an incorrect folder on the approved USB device."
  resolution: "Clinical Engineering placed the authorized package in the required media location, completed the update, and verified startup, scanning, record storage, and approved configuration."
helpfulDetails:
  - "Update or configuration package version"
  - "Current device software version"
  - "Approval or change record"
  - "Exact failure message"
  - "Step where failure occurred"
  - "Power source and battery status"
  - "Media, cable, or network used"
  - "File source and integrity check"
  - "Available storage"
  - "Authorized account used"
  - "Post-update functional test results"
  - "Final device status"
---

## What This Guide Helps With

Addresses failed updates or configuration transfers caused by power, media, files, connection, compatibility, authorization, or network conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Device and Clinical Workflow

Remove the scanner from clinical use before starting or troubleshooting an update or configuration transfer. Provide another verified scanner for patient care.

Do not interrupt power, remove media, disconnect cables, or restart the device while an update is actively applying unless approved recovery instructions specifically require it.

**Expected outcome:** Patient care continues and the device is protected from an incomplete update.

### 2. Confirm the Failed Process

Determine whether the problem involves:

- Software download
- Update-file recognition
- Installation start
- Installation interruption
- Restart after update
- Configuration export
- Configuration import
- Transfer between devices
- Network-based deployment

Record the exact message, file source, step reached, and current software state.

**Expected outcome:** The failure is identified as file, media, communication, authorization, installation, or restart related.

### 3. Verify Authorization and Change Control

Confirm that the update or configuration transfer is approved by the facility and supported for the exact BladderScan i10 hardware and current software version.

Verify that the installer, configuration package, or instructions came from an authorized source.

**Expected outcome:** The planned change is authorized, applicable, and traceable.

### 4. Confirm Stable Power

Connect the scanner to approved external power and verify charging or power indicators. Ensure that the cart, dock, outlet, and power supply are stable.

Do not perform an update using a depleted battery or intermittent dock connection.

**Expected outcome:** Stable power is available for the entire update and restart process.

### 5. Inspect the Transfer Media or Cable

Inspect the approved USB device, cable, port, or network connection for damage, contamination, looseness, or improper seating.

Do not use unknown, unapproved, encrypted, or damaged media.

**Expected outcome:** The transfer path is secure and physically intact.

### 6. Verify the File or Package

Confirm the file name, version, package structure, media location, and compatibility against approved documentation. Verify that the file was fully copied and not renamed, compressed, or altered unexpectedly.

Do not modify update files or configuration packages.

**Expected outcome:** The device is presented with a complete and compatible package.

### 7. Check Available Storage

Using normal system information screens, confirm that adequate storage is available for the update or transfer.

Do not delete patient records or system files to create space unless an authorized data-management procedure has been completed.

**Expected outcome:** Storage capacity is not preventing the process.

### 8. Check User Access and Administrative Rights

Confirm that the logged-in account has the authorized permission to perform the update or configuration transfer.

Do not use shared credentials, bypass access control, or attempt unauthorized privilege escalation.

**Expected outcome:** The process is initiated under the correct authorized account.

### 9. Retry From a Known-Good Source

When approved, copy the authorized package to known-good compatible media or use a verified cable or network connection. Repeat the process from the beginning according to the approved instructions.

**Expected outcome:** The device recognizes and completes the transfer. If the same failure recurs, stop repeated attempts.

### 10. Verify Configuration Scope

For configuration transfer, confirm that the source and destination devices are the correct models and approved software levels. Review which settings are intended to transfer.

Do not overwrite site-specific network, security, patient-data, or access settings without documented approval.

**Expected outcome:** Only the intended compatible configuration is transferred.

### 11. Observe the Restart and Post-Update State

After a completed update, allow the device to restart normally. Confirm that it reaches the normal startup screen and displays the intended approved software or configuration state.

Do not repeatedly power cycle a device stuck during update recovery.

**Expected outcome:** The scanner starts normally with the approved version or configuration.

### 12. Complete Return-to-Service Verification

Verify:

- Normal startup
- User login
- Probe recognition
- Scan initiation and completion
- Patient ID entry
- Record saving and retrieval
- Printer or interface functions when applicable
- Date, time, and approved configuration
- No update or configuration warning

**Expected outcome:** The scanner functions normally with the approved change and may return to service.

## If the Problem Persists

External causes involving authorization, power, transfer media, cables, file integrity, compatibility, storage, user access, and network connection have been ruled out.

The remaining cause may involve corrupted software, bootloader or recovery state, internal storage, configuration database, security controls, or another service-level condition. Do not attempt unsupported recovery, factory reset, firmware downgrade, or internal memory replacement.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Verathon documentation and approved test equipment
- Repaired or configured only by qualified personnel

After recovery, complete software-version confirmation, configuration review, functional testing, data handling checks, and all required return-to-service documentation.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never perform a software update or configuration transfer on the only bladder scanner available for immediate patient care.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Control the clinical impact first, then verify authorization, stable power, file compatibility, transfer media, storage, and access permissions. Avoid unsupported recovery actions, escalate failed updates appropriately, and document the approved change and complete return-to-service verification.

That is successful troubleshooting.

