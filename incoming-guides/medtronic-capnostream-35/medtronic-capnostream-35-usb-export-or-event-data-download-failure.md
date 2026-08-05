---
schemaVersion: 1
title: "Medtronic Capnostream 35 Capnography Monitor - USB Export or Event Data Download Failure"
issueTitle: "USB Export or Event Data Download Failure"
description: "Troubleshoots failed USB recognition, export errors, missing files, or incomplete downloads caused by media, ports, storage, workflow, or software issues."
assetType: "Capnography Monitor"
manufacturer: "Medtronic"
model: "Capnostream 35"
slug: "medtronic-capnostream-35-usb-export-or-event-data-download-failure"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Capnostream 35 would not recognize the USB drive used to download event data."
  cause: "Clinical Engineering found that the original USB drive was full and could not accept additional files."
  resolution: "An approved USB device with available capacity was used, and successful export and file readability were verified on an approved workstation."
helpfulDetails:
  - "Exact export message"
  - "Record or date range selected"
  - "USB device type and approval status"
  - "Available USB capacity"
  - "Physical USB condition"
  - "Monitor port condition"
  - "Known-good media result"
  - "Transfer completion status"
  - "File name and readability"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots failed USB recognition, export errors, missing files, or incomplete downloads caused by media, ports, storage, workflow, or software issues.

## Step-by-Step Troubleshooting

### 1. Protect Patient Monitoring and Data

Do not interrupt active monitoring to troubleshoot an export problem. Transfer the patient to another verified monitor before restarting the unit or manipulating stored records.

Handle all exported patient data according to facility privacy, cybersecurity, and removable-media policies.

**Expected outcome:** Monitoring continues and protected health information remains controlled.

### 2. Confirm the Exact Export Failure

Determine whether the USB device is not recognized, the export option is unavailable, the transfer stops, the file is missing afterward, the monitor freezes, or the exported file cannot be opened.

Record any displayed message and the point where the process fails.

**Expected outcome:** The issue is defined as media recognition, selection, transfer, file creation, or file access.

### 3. Verify the Correct Export Workflow

Confirm that the desired patient, trend, event, and date range are selected before export. Verify that the user is following the authorized normal workflow and has appropriate access.

Do not use restricted service menus or unsupported software utilities.

**Expected outcome:** The export command is available and directed to the correct data set.

### 4. Inspect the USB Device

Check the removable media for physical damage, contamination, write protection, insufficient capacity, or use for unrelated software.

Use only facility-approved and compatible media. Do not connect unknown personal drives.

**Expected outcome:** The USB device is approved, undamaged, writable, and has sufficient available space.

### 5. Inspect the USB Port Externally

Examine the monitor’s USB port for bent contacts, debris, liquid, looseness, or enclosure damage. Do not insert tools or fluids into the port.

**Expected outcome:** The port appears clean, dry, and mechanically intact.

### 6. Reinsert the USB Device Correctly

Remove the USB device, wait for the monitor to complete any pending activity, and reconnect it firmly without excessive force. Allow time for recognition before starting the export.

**Expected outcome:** The monitor recognizes the USB device. If export then completes and the file is verified, troubleshooting can stop.

### 7. Test With Another Approved Known-Good USB Device

Use a second compatible, facility-approved USB device. Keep the exported data set small for the initial test when possible.

**Expected outcome:** The export succeeds with the known-good media, confirming the original USB device was incompatible, full, damaged, or corrupted. Troubleshooting can stop.

### 8. Verify Available Internal and USB Storage

Confirm that the monitor can access the selected record and that the USB device has enough free space. A damaged stored record or full internal memory may also interfere with export.

**Expected outcome:** Both source data and destination storage are available.

### 9. Complete and Verify a Controlled Export

Export a test record or approved nonclinical data set. After the monitor reports completion, safely remove the media according to normal workflow and verify that the expected file exists and can be opened on an approved workstation.

**Expected outcome:** The export completes, the file is present, and its contents correspond to the selected record. If successful, troubleshooting can stop.

### 10. Escalate Persistent Port or Software Failure

If multiple approved USB devices are not recognized or exports repeatedly fail, freeze, or produce corrupted files, remove the device from service when data export is required by the workflow.

Label it **Out of Service** and escalate for USB-port, software, storage, or configuration evaluation.

**Expected outcome:** A monitor with unreliable data transfer is prevented from use in workflows requiring dependable export.

## If the Problem Persists

External media, storage capacity, port condition, record selection, and workflow causes have been ruled out. Remaining categories include damaged USB hardware, internal storage corruption, software failure, incompatible configuration, or a service-level data-management problem.

The monitor should be removed from service when export is clinically or operationally required, labeled Out of Service, and evaluated using manufacturer documentation and approved service tools. Repair and software restoration should be performed only by qualified personnel.

After repair, verify recognition of approved media, successful export, file readability, patient-data integrity, stored-record access, and complete monitor functionality before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Verify the exported file before deleting or clearing the original patient record from the monitor.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the original data, confirm the authorized workflow, and test with approved known-good media before suspecting internal failure. Persistent export problems require escalation and precise documentation of the data selected, devices tested, and verification results.

That is successful troubleshooting.
