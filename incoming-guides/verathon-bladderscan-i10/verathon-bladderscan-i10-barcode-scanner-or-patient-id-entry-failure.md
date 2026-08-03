---
schemaVersion: 1
title: "Verathon BladderScan i10 Bladder Scanner - Barcode Scanner or Patient ID Entry Failure"
issueTitle: "Barcode Scanner or Patient ID Entry Failure"
description: "Addresses barcode recognition, patient ID entry, scanner connection, label quality, workflow, keyboard, configuration, and interface causes."
assetType: "Bladder Scanner"
manufacturer: "Verathon"
model: "BladderScan i10"
slug: "verathon-bladderscan-i10-barcode-scanner-or-patient-id-entry-failure"
dateAdded: "2026-08-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the barcode scanner illuminated but would not enter the patient ID."
  cause: "Clinical Engineering found that the barcode scanner cable was loose at the scanner interface."
  resolution: "Clinical Engineering reseated the cable, scanned multiple approved test barcodes, verified correct field entry, and confirmed normal patient ID workflow."
helpfulDetails:
  - "Barcode type and label condition"
  - "Scanner power or ready indication"
  - "Scanner window condition"
  - "Cable and port condition"
  - "Known-good barcode result"
  - "Manual entry result"
  - "External keyboard result"
  - "Exact displayed message"
  - "Approved configuration checked"
  - "Patient association test result"
  - "Final device status"
---

## What This Guide Helps With

Addresses barcode recognition, patient ID entry, scanner connection, label quality, workflow, keyboard, configuration, and interface causes.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification Integrity

Do not save a scan under an uncertain or incorrect patient identity. Pause the workflow and verify the patient using approved identifiers.

Use manual entry only when permitted by facility policy and when the patient identity can be confirmed accurately.

**Expected outcome:** No scan is associated with the wrong patient while troubleshooting occurs.

### 2. Confirm the Exact Entry Failure

Determine whether:

- The barcode scanner has no power
- It scans but enters no data
- It enters incomplete or incorrect characters
- Manual patient ID entry also fails
- One barcode type fails while others work
- The patient record is rejected after entry
- The problem occurs only in an interfaced workflow

Record any displayed message without assuming its cause.

**Expected outcome:** The issue is isolated to scanning, manual entry, data validation, or downstream interface workflow.

### 3. Verify the Correct Patient Entry Screen

Confirm that the cursor is active in the intended patient ID field and that the device is not waiting for operator login, required demographics, or another mandatory selection.

Exit unrelated menus and return to the normal patient-entry workflow.

**Expected outcome:** The system is ready to accept barcode or manual patient data.

### 4. Inspect the Barcode and Label

Verify that the barcode is not wrinkled, wet, torn, faded, overly glossy, curved, or covered by tape. Compare with a known-good facility barcode of the same supported type.

Do not create or alter patient identifiers outside the approved registration workflow.

**Expected outcome:** A clean, readable, supported barcode is available. If it scans correctly, the original label was the cause.

### 5. Inspect the Barcode Scanner and Connection

Check the scanner window, cable, connector, strain relief, and accessible port for dirt, damage, looseness, bent contacts, or contamination.

Clean the scanner window by the approved method and reseat the connection. Confirm the scanner receives power or gives its normal ready indication.

**Expected outcome:** The scanner is clean, powered, and securely connected. If scanning returns, proceed to final verification.

### 6. Test Scan Technique

Aim the scanner squarely at the barcode at a reasonable distance. Avoid excessive room glare, direct sunlight, curved wristbands, and rapid movement.

Test several known-good labels rather than repeatedly scanning one questionable barcode.

**Expected outcome:** The scanner consistently reads known-good labels when positioned correctly.

### 7. Test Manual Patient ID Entry

Use the approved onscreen keyboard or connected input device to enter a test identifier according to facility procedure.

Confirm that all characters register correctly and that the field accepts the expected format.

**Expected outcome:** Manual entry works normally. If barcode scanning alone fails, the problem is isolated to the scanner, label, connection, or barcode configuration.

### 8. Check External Keyboard or Input Device

If an external keyboard or accessory is used, inspect and reseat its connection. Disconnect nonessential input devices and retest the built-in entry method.

Use a known-good approved accessory when available.

**Expected outcome:** Patient data can be entered through at least one approved method, and a faulty external accessory can be isolated.

### 9. Verify Approved Configuration

Confirm that the patient ID field, barcode workflow, and permitted barcode types match the facility-approved configuration.

Do not alter barcode symbology, access control, network, or patient-data configuration without authorization and a documented change process.

**Expected outcome:** The observed configuration matches the approved baseline. Any mismatch is escalated to the authorized system administrator or service provider.

### 10. Restart and Retest

Complete or cancel the current workflow safely, restart the scanner, and return to patient entry. Test a known-good barcode and manual entry again.

**Expected outcome:** Patient ID entry works reliably after restart. If the problem returns, further service is required.

### 11. Perform Final Functional Verification

Verify that the device:

- Reads a known-good barcode
- Places data in the correct field
- Accepts approved manual entry
- Preserves the correct patient association
- Saves a test record as expected
- Does not duplicate or truncate the identifier

Use nonclinical test data or the approved test workflow.

**Expected outcome:** Patient identification is accurate and repeatable. The device may return to service.

## If the Problem Persists

External causes involving screen selection, label quality, scan technique, scanner window, cables, ports, manual entry, and external input devices have been ruled out.

The remaining cause may involve scanner hardware, USB or input circuitry, barcode configuration, user permissions, software, patient-data validation, or an external interface. Do not bypass patient identification controls or make undocumented configuration changes.

The device or affected accessory should be:

- Removed from service when accurate patient identification cannot be assured
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Verathon documentation and approved test equipment
- Repaired or configured only by qualified personnel

After correction, verify barcode entry, manual entry, patient association, record storage, and any connected information-system workflow before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never attach a bladder scan result to a patient record unless the displayed identifier has been independently verified.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Patient identification accuracy comes first. Verify the entry screen, label, scan technique, accessory connection, manual entry, and approved configuration before suspecting internal failure. Remove the device from service when accurate record association cannot be guaranteed and document the verified CCR clearly.

That is successful troubleshooting.

