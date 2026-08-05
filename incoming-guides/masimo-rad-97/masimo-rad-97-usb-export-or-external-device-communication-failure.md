---
schemaVersion: 1
title: "Masimo Rad-97 Pulse Oximeter - USB Export Or External Device Communication Failure"
issueTitle: "USB Export Or External Device Communication Failure"
description: "USB export or external communication problems caused by media compatibility, cables, connectors, permissions, data format, configuration, or interface failure."
assetType: "Pulse Oximeter"
manufacturer: "Masimo"
model: "Rad-97"
slug: "masimo-rad-97-usb-export-or-external-device-communication-failure"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Rad-97 would not recognize a USB device during trend export."
  cause: "Clinical Engineering found that the USB device was not approved for the monitor and verified normal operation with a compatible hospital-controlled device."
  resolution: "Repeated the export using an approved USB device, confirmed the complete file on a secure workstation, verified normal monitoring and alarms, and returned the unit to service."
helpfulDetails:
  - "Exact displayed message"
  - "Type of USB or external device"
  - "Cable and connector condition"
  - "Approved compatibility status"
  - "Available external storage"
  - "Data selected for export"
  - "Date and time"
  - "Known-good accessory results"
  - "File verification results"
  - "Final device status"
---

## What This Guide Helps With

USB export or external communication problems caused by media compatibility, cables, connectors, permissions, data format, configuration, or interface failure.

## Step-by-Step Troubleshooting

### 1. Maintain Patient Monitoring

Do not interrupt active monitoring to troubleshoot data export. Confirm that local monitoring and alarms remain normal.

Transfer the patient to another verified monitor if the Rad-97 freezes, restarts, or becomes unreliable when an external device is connected.

Expected outcome: Patient monitoring remains safe and uninterrupted.

### 2. Confirm the Exact Failure

Determine whether the Rad-97 fails to recognize the USB device, cannot begin export, stops partway through, creates an unreadable file, or cannot communicate with a connected external system.

Record all displayed messages and the type of external device involved.

Expected outcome: The failure is reproduced and clearly categorized.

### 3. Inspect the USB Device, Cable, and Connector

Check the external device, cable, adapter, and Rad-97 port for damage, contamination, looseness, bent contacts, or evidence of fluid exposure.

Do not force a connector or use unapproved adapters.

Expected outcome: All external components are intact and fully connected.

### 4. Verify Approved Compatibility

Confirm that the media, cable, adapter, or external device is approved and compatible with the facility’s Rad-97 configuration.

Do not connect personal storage devices or unapproved equipment to a clinical device.

Expected outcome: Only approved compatible accessories remain connected.

### 5. Test With a Known-Good External Device

Use a known-good approved USB device, cable, or connected system.

Test the suspect accessory on another verified compatible device when permitted.

Expected outcome: The problem follows the external accessory or remains with the Rad-97.

### 6. Confirm Data Selection and Available Storage

Verify that valid data is selected for export and that the external storage device has sufficient available space.

Confirm that the expected export process is being used and that no required selection field is missing.

Expected outcome: The export begins and completes normally. If so, troubleshooting can stop after file verification.

### 7. Check Date, Time, and File Identification

Confirm that the Rad-97 date and time are correct so exported files can be found and associated properly.

Review the destination for a newly created file rather than relying only on the expected filename.

Expected outcome: The exported record is located with the correct timestamp.

### 8. Disconnect Other Nonessential Accessories

Remove additional external devices and communication cables, then retry using only the required known-good connection.

Expected outcome: Export or communication succeeds without accessory conflict.

### 9. Restart and Retest

Remove the unit from patient use, perform a normal restart, and retry the export or external communication process.

Expected outcome: The Rad-97 recognizes the external device and completes the process reliably.

### 10. Verify the Exported Data or External Communication

Open the exported file on an approved secure workstation or verify data reception at the intended external system.

Confirm completeness, correct patient association, date, time, and readability.

Expected outcome: The full data transfer is verified end to end.

### 11. Escalate Persistent Communication Failure

If the problem remains with multiple approved known-good accessories, stop external troubleshooting.

Expected outcome: The monitor is removed from workflows requiring USB or external communication and routed for qualified evaluation.

## If the Problem Persists

Common external causes involving incompatible media, damaged cables, insufficient storage, incorrect data selection, time settings, and accessory conflicts have been ruled out.

The remaining cause may involve the USB port, communication interface, software, data format, security configuration, or internal hardware. Remove the Rad-97 from service when the external communication feature is required, label it Out of Service, and send it for repair or bench evaluation.

Use current manufacturer documentation and approved test equipment. Protect patient data and follow facility cybersecurity requirements. Verify monitoring, alarms, export, and communication before return to service.

## Clinical Use Tip

Use only approved hospital-controlled storage devices and verify the exported file before assuming the data transfer was successful.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Keep patient monitoring separate from data-transfer troubleshooting, verify approved external accessories first, confirm the complete data path, and escalate failures that remain with the monitor.

That is successful troubleshooting.
