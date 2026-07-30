---
schemaVersion: 1
title: "Mortara ELI Series Electrocardiograph (EKG) Machine - Report Format, PDF Export, Or File Export Failure"
issueTitle: "Report Format, PDF Export, Or File Export Failure"
description: "Troubleshooting incorrect reports or failed exports caused by format selection, storage media, file naming, configuration, capacity, or software problems."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "Mortara"
model: "ELI Series"
slug: "mortara-eli-series-report-format-pdf-export-or-file-export-failure"
dateAdded: "2026-07-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that PDF exports from the Mortara ELI Series machine were failing and no file appeared on the USB drive."
  cause: "Clinical Engineering found the USB drive had no available storage capacity."
  resolution: "Replaced the media with an approved USB device, exported a simulator ECG to PDF, verified file readability and report content, and returned the unit to service."
helpfulDetails:
  - "Exact export message."
  - "Record selected."
  - "Report format selected."
  - "Required content missing."
  - "Export destination."
  - "USB media condition and capacity."
  - "Filename behavior."
  - "Test record result."
  - "File open and readability result."
  - "Receiving-system result."
  - "Final device status."
---

## What This Guide Helps With

Troubleshooting incorrect reports or failed exports caused by format selection, storage media, file naming, configuration, capacity, or software problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data and Clinical Availability

Do not delay an urgent ECG because a preferred report format or export pathway is unavailable.

Use an approved alternate method such as printing, network transmission, internal storage, or another verified device. Protect all exported files as patient information.

**Expected outcome:** The ECG remains clinically available and patient data is not exposed or lost.

### 2. Confirm the Exact Report or Export Failure

Determine whether:

- The report prints in the wrong layout.

- Required demographics, measurements, or interpretation are missing.

- PDF export is unavailable.

- Export starts but does not complete.

- A file is created but cannot be opened.

- The filename or extension is unexpected.

- One record fails while other records export normally.

- Export fails only to USB, network, or a specific destination.

Record the exact message and selected output type.

**Expected outcome:** The issue is separated into report-template, export-destination, media, file, or software categories.

### 3. Verify the Correct Patient Record

Before exporting or printing, confirm:

- Patient name and identifier.

- Acquisition date and time.

- Correct ECG record.

- Correct report version.

- Correct destination.

**Expected outcome:** The intended ECG is selected and no unrelated patient record is exported.

### 4. Check the Selected Report Format

Review the normal print or export selection.

Confirm the chosen format is intended to include the required:

- Lead layout.

- Measurements.

- Interpretation.

- Demographics.

- Rhythm strip.

- Institution header.

- File type.

Compare with a working device if the expected format is unclear.

**Expected outcome:** The approved report template is selected. If correction restores the output, troubleshooting can stop after verification.

### 5. Verify Output Destination

Confirm whether the report is being sent to:

- Internal printer.

- USB storage.

- Network share.

- ECG management system.

- Approved export folder.

- Another configured destination.

Check that the selected destination is currently available.

**Expected outcome:** The intended output destination is correctly selected and accessible.

### 6. Inspect and Test USB Media When Applicable

For USB export:

Confirm approved media is used.

Reseat the device.

Check free capacity.

Inspect the USB port and connector.

Test with a known-good compatible USB device.

Avoid encrypted or unsupported media unless approved.

**Expected outcome:** The storage device is recognized and writable.

### 7. Check File Naming and Existing Files

Review whether the export destination already contains a file with the same name.

Check for invalid characters, excessively long names, duplicate filenames, or an unavailable patient ID field used in the filename. Do not rename patient files in a misleading way.

**Expected outcome:** The file can be created with an approved unique name.

### 8. Verify Storage Capacity

Confirm that both internal storage and the external destination have adequate available space.

Preserve required records before any authorized cleanup. Do not delete patient files without following retention requirements.

**Expected outcome:** Adequate storage is available for report generation and export.

### 9. Restart the EKG Machine

Confirm the ECG record is saved.

Perform a normal shutdown, disconnect removable media, restart the device, and retry the export using a known-good test record and approved destination.

**Expected outcome:** Report and export services initialize normally.

### 10. Test a Different Record

Export an approved test ECG or simulator-generated record.

If one record fails but others export normally, the problem may involve that record rather than the entire export function.

**Expected outcome:** The scope is identified as record-specific or device-wide.

### 11. Verify the Exported File

On an approved secured workstation:

Confirm the file is present.

Verify the file opens.

Confirm the patient identity.

Check report completeness and readability.

Confirm no unrelated records were included.

Verify the filename and date.

**Expected outcome:** The exported report is complete, readable, and associated with the correct test record.

### 12. Compare Local and Receiving-System Output

If the local report is correct but the receiving system displays it incorrectly, involve the ECG management, document-management, or interface team.

**Expected outcome:** The fault is isolated to the EKG machine or the downstream system.

### 13. Perform Final Functional Verification

Using approved test data:

- Acquire or select a simulator ECG.

- Generate the required report.

- Export it to the approved destination.

- Open and inspect the file.

Confirm required demographics and content.

Confirm successful receipt when transmitted.

**Expected outcome:** The complete report-generation and export pathway functions normally. Troubleshooting can stop.

### 14. Escalate Persistent Export or Format Failure

Remove the device from service or restrict it to an approved alternate workflow if required reports cannot be generated accurately or exported securely.

**Expected outcome:** Incorrect, incomplete, or misidentified ECG reports are not released into the clinical record.

## If the Problem Persists

Common causes involving record selection, report format, destination choice, USB media, capacity, filename conflicts, and temporary software state have been ruled out. The remaining issue may involve report-template configuration, export software, file-system corruption, destination permissions, network services, or an ECG management interface.

The device should be:

- Removed from service when required reporting cannot be completed safely.

- Labeled Out of Service.

- Sent for repair or bench evaluation when device-specific failure is suspected.

- Evaluated using appropriate Mortara documentation and approved test equipment.

- Repaired or configured only by qualified personnel.

Coordinate with information services or clinical applications when local files are correct but downstream reports are incomplete or altered.

After correction, verify report content, file generation, file readability, patient identification, and destination receipt.

Knowing when to stop protects the accuracy and confidentiality of patient records.

## Clinical Use Tip

Open and verify the exported ECG file before relying on it for the medical record or forwarding it to another system.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Preserve clinical access and patient confidentiality while verifying record selection, report template, destination, media, naming, and storage before assuming internal failure. Confirm the exported file itself and clearly document the correction and final verification.

That is successful troubleshooting.
