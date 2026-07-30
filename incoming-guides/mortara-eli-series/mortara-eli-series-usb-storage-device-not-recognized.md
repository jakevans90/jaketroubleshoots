---
schemaVersion: 1
title: "Mortara ELI Series Electrocardiograph (EKG) Machine - USB Storage Device Not Recognized"
issueTitle: "USB Storage Device Not Recognized"
description: "Troubleshooting an unrecognized USB storage device caused by media compatibility, connection, formatting, file-system, port, or workflow problems."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "Mortara"
model: "ELI Series"
slug: "mortara-eli-series-usb-storage-device-not-recognized"
dateAdded: "2026-07-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Mortara ELI Series EKG machine did not recognize the USB drive used for ECG export."
  cause: "Clinical Engineering found that the original USB drive was defective and was also unreadable on an approved workstation."
  resolution: "Replaced the drive with approved compatible media, verified successful ECG file export and readability, and returned the unit to service."
helpfulDetails:
  - "Exact displayed message."
  - "USB device type and identifier."
  - "Whether the media worked previously."
  - "Available storage capacity."
  - "Approved workstation test result."
  - "Known-good USB result."
  - "Port condition."
  - "Export file type attempted."
  - "Restart result."
  - "Final export and file-verification status."
---

## What This Guide Helps With

Troubleshooting an unrecognized USB storage device caused by media compatibility, connection, formatting, file-system, port, or workflow problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data and Continuity of Care

Do not delay an urgent ECG because removable storage is unavailable.

Use the approved alternate workflow for printing, internal storage, network transmission, or another verified EKG machine. Treat every USB device as containing protected patient information.

**Expected outcome:** Clinical care continues while patient data remains protected.

### 2. Confirm the Exact USB Failure

Determine whether:

- The USB device is not detected at all.

- It is detected but cannot be written to.

- Files cannot be opened or exported.

- The device was previously usable on the same EKG machine.

- The problem affects one USB device or all tested media.

- The port powers another approved accessory, if applicable.

Record any displayed message and the exact export or import operation attempted.

**Expected outcome:** The problem is categorized as detection, write access, file compatibility, storage capacity, or port failure.

### 3. Verify the Correct USB Port and Workflow

Confirm the storage device is inserted into the port intended for removable media rather than a scanner, service, or accessory connection.

Open the normal export, import, or archive function and verify the machine is actually waiting for removable media.

**Expected outcome:** The correct port and approved workflow are being used.

### 4. Inspect the USB Device and Port

Remove the USB device and inspect it for:

- Bent or damaged contacts.

- Cracked housing.

- Loose connector movement.

- Contamination or moisture.

- Evidence of impact.

- A body shape that prevents full insertion.

- Inspect the device port externally with adequate lighting. Do not insert tools or attempt internal straightening.

**Expected outcome:** The USB device inserts fully and the port has no obvious external damage. If physical damage is present, stop and remove the affected item from use.

### 5. Reseat the USB Device

Exit the export or import screen, remove the USB device, wait briefly, and reinsert it fully.

Reopen the normal removable-storage workflow. Avoid repeated rapid insertion and removal.

**Expected outcome:** The device is detected and displayed as an available destination. If recognition returns and export succeeds, troubleshooting can stop after verification.

### 6. Check Available Storage Capacity

Verify the USB device has sufficient free space using an approved workstation when facility policy permits.

Remove unnecessary files only when authorized. Do not delete patient information without following retention and privacy requirements.

**Expected outcome:** Adequate free space is available for the intended export.

### 7. Verify Approved Media and File-System Compatibility

Use a facility-approved USB device known to function with the same ELI Series configuration.

Avoid encrypted, password-protected, bootable, multi-partition, unusually large, or security-managed media unless specifically approved.

Do not reformat media containing patient data without authorization and confirmed backup.

**Expected outcome:** A known-good, appropriately prepared USB device is recognized.

### 8. Test the Original USB Device on an Approved Workstation

When permitted, connect the original USB device to a secured facility workstation.

Check whether the workstation recognizes it and whether files can be read or written. Follow cybersecurity requirements and do not connect unknown personal media.

**Expected outcome:**

If the workstation also fails to recognize the device, the USB media is likely defective.

If the workstation recognizes it but the EKG machine does not, compatibility or device-port issues remain.

### 9. Test Multiple Approved USB Devices

Test at least one additional known-good approved USB device.

**Expected outcome:**

If other media works, remove the original USB device from use.

If no approved media is recognized, suspect the EKG port, software state, or configuration.

Troubleshooting can stop after defective media is replaced and a successful export is verified.

### 10. Restart the EKG Machine

Confirm no ECG acquisition, save, export, or transmission is active.

Perform a normal shutdown, disconnect removable media, restart the device, and insert the known-good USB device only after startup is complete.

**Expected outcome:** The USB interface initializes normally and recognizes approved media.

### 11. Perform a Controlled Export Test

Using approved nonclinical test data or a permitted test record:

- Export the file.

Confirm the operation completes without an error.

Safely remove the USB device using the available workflow.

Verify the file on an approved workstation.

Confirm no unrelated patient files were altered.

**Expected outcome:** The export completes and the expected file is readable. The device may return to service.

### 12. Escalate a Suspected Port or Software Failure

Remove the device from service or restrict its use if USB export is required for the clinical workflow and no approved media is recognized.

**Expected outcome:** A device with an unresolved data-export pathway is not returned without an approved alternate workflow.

## If the Problem Persists

External media damage, improper insertion, insufficient capacity, incompatible media, and temporary initialization problems have been ruled out. The remaining issue may involve the USB port, device software, file-system support, export configuration, cybersecurity controls, or internal interface hardware.

The device should be:

- Removed from service when USB functionality is required and no approved workaround exists.

- Labeled Out of Service.

- Sent for repair or bench evaluation.

- Evaluated using appropriate Mortara documentation and approved test equipment.

- Repaired or configured only by qualified personnel.

After repair, verify recognition with approved media, complete a controlled export, confirm file readability, and protect all patient data.

Knowing when to stop external troubleshooting and escalate protects both the device and patient information.

## Clinical Use Tip

Use only facility-approved removable media and maintain physical control of any USB device containing ECG records.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain continuity of care and protect patient data while checking approved media, physical connections, capacity, compatibility, and workflow before assuming internal failure. Escalate unresolved port or software problems and document the verified cause and final export test.

That is successful troubleshooting.
