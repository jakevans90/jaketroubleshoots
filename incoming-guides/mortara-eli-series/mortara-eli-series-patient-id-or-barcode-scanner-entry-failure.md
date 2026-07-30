---
schemaVersion: 1
title: "Mortara ELI Series Electrocardiograph (EKG) Machine - Patient ID Or Barcode Scanner Entry Failure"
issueTitle: "Patient ID Or Barcode Scanner Entry Failure"
description: "Troubleshooting failed patient entry or barcode scanning caused by scanner, connection, barcode quality, workflow, configuration, or interface problems."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "Mortara"
model: "ELI Series"
slug: "mortara-eli-series-patient-id-or-barcode-scanner-entry-failure"
dateAdded: "2026-07-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Mortara ELI Series EKG machine did not respond when patient wristband barcodes were scanned."
  cause: "Clinical Engineering found the barcode scanner cable was not fully seated at the device connection."
  resolution: "Reseated the scanner connection, verified correct patient ID entry with approved test barcodes, and returned the unit to service."
helpfulDetails:
  - "Whether manual entry worked."
  - "Scanner light or tone behavior."
  - "Barcode type and label condition."
  - "Scanner model and connection type."
  - "Exact displayed message."
  - "Fields populated incorrectly or not at all."
  - "Known-good scanner result."
  - "Network and patient-lookup status."
  - "Comparison with another device."
  - "Final patient-entry verification."
---

## What This Guide Helps With

Troubleshooting failed patient entry or barcode scanning caused by scanner, connection, barcode quality, workflow, configuration, or interface problems.

## Step-by-Step Troubleshooting

### 1. Ensure Patient Safety and Correct Patient Identification

Do not acquire or transmit an ECG under an unverified or incorrect patient identity.

If the ECG is clinically urgent, follow the facility’s approved unidentified-patient or downtime workflow. Confirm the patient using required identifiers before proceeding.

**Expected outcome:** The patient receives timely care without creating a mislabeled ECG record.

### 2. Confirm the Exact Entry Failure

Determine whether:

- Manual keyboard entry works but barcode scanning fails.

- Neither manual nor scanned entry is accepted.

- The scanner produces no light, tone, or response.

- The scanner reads the barcode but places data in the wrong field.

- The device rejects only certain barcode labels.

- The patient record is found but cannot be selected or saved.

Record the complete displayed message and the point in the workflow where failure occurs.

**Expected outcome:** The issue is separated into scanner hardware, barcode readability, field mapping, patient-search, or device-input categories.

### 3. Verify Manual Patient Entry

Attempt to enter a test patient identifier through the normal patient-information screen using approved nonclinical test data.

Check for unresponsive keys, touch controls, frozen fields, or characters appearing incorrectly.

**Expected outcome:**

If manual entry works, focus on the scanner, barcode, or mapping.

If manual entry also fails, investigate controls, software state, workflow restrictions, or configuration.

### 4. Inspect the Barcode Scanner and Cable

Remove the scanner from clinical use if its cable or housing is damaged.

Inspect for:

- Loose USB or accessory connection.

- Bent connector contacts.

- Pinched cable sections.

- Cracked housing or scan window.

- Contamination on the scan window.

- Fluid exposure.

- Strain-relief damage.

Reconnect the scanner securely and restart the normal patient-entry workflow.

**Expected outcome:** The scanner is physically intact, securely connected, and powers or initializes normally. If reseating restores operation, complete verification and stop.

### 5. Clean and Test the Scanner Window

Clean the scan window using an approved method and allow it to dry.

Test several facility-issued labels with clear printing. Hold the scanner at different reasonable distances and angles without touching the patient or contaminated surfaces.

**Expected outcome:** A valid, clearly printed barcode is read consistently. If only damaged or low-contrast labels fail, the EKG machine may be functioning normally.

### 6. Examine the Barcode Label

Confirm that the problem barcode is:

- Complete and not cut off.

- Flat and not wrapped around a curved surface.

- Free of smearing, wrinkles, glare, or moisture.

- Printed at a readable contrast.

- The expected barcode type for the configured workflow.

Compare it with a known-good label from the same facility system.

**Expected outcome:** The barcode is suitable for scanning and matches the established patient-identification workflow.

### 7. Test a Known-Good Compatible Scanner

Connect a known-good scanner approved for use with the ELI Series device.

Do not assume any USB barcode scanner will be compatible. Use the same scanner model or a facility-approved equivalent when possible.

**Expected outcome:**

If the known-good scanner works, remove the original scanner from service.

If both scanners fail, continue with device and configuration checks.

Troubleshooting can stop once the defective scanner is replaced and patient-entry operation is verified.

### 8. Check Input Focus and Workflow Position

Confirm that the cursor or active field is located in the correct patient ID field before scanning.

Exit and reopen the patient-entry screen. Confirm that a modal message, search window, or incomplete prior record is not preventing input.

**Expected outcome:** Scanned data appears in the intended field and can be accepted or used for patient search.

### 9. Verify Patient-Identification Configuration

Review normal authorized settings related to:

- Patient ID field requirements.

- Barcode input.

- Demographic field order.

- Leading zeros or character length.

- Patient-search workflow.

- Site or department configuration.

Compare the affected device with a working ELI Series unit in the same department when available. Do not change restricted settings without authorization.

**Expected outcome:** The device’s patient-entry configuration matches the approved facility workflow.

### 10. Check Network-Dependent Patient Lookup

If barcode scanning enters an identifier but patient data does not populate, determine whether the device requires a network or order-management connection.

Verify:

- Network status.

- Correct department or location.

- Availability of the patient/order interface.

- Whether other EKG machines can retrieve the same patient.

- Whether manual demographic entry still works.

**Expected outcome:** The issue is identified as local scanner input or a broader patient-data interface problem.

### 11. Perform Final Functional Verification

Using approved test data:

- Scan a valid barcode.

Confirm the correct identifier appears.

Verify demographics populate in the correct fields when applicable.

Confirm the data can be accepted without altering a live patient record.

Verify manual entry remains functional.

**Expected outcome:** Patient ID entry works accurately and consistently. Troubleshooting can stop and the device may return to service after documentation.

### 12. Escalate Unresolved Identification Failures

Remove the device from service or restrict it according to facility policy if it cannot reliably capture, display, or retain correct patient identity.

**Expected outcome:** The device is not used in a way that could create a mislabeled or misrouted ECG.

## If the Problem Persists

Common external causes involving scanner seating, cable damage, scan-window contamination, label quality, input focus, and known-good substitutions have been ruled out. The remaining issue may involve device software, barcode configuration, field mapping, patient-order interfaces, network services, or internal input hardware.

The device should be:

- Removed from service when reliable identification cannot be assured.

- Labeled Out of Service.

- Sent for repair or bench evaluation.

- Evaluated using appropriate Mortara documentation and approved test equipment.

- Repaired or configured only by qualified personnel.

Coordinate with the ECG management system, interface, network, or applications team when the device reads the barcode correctly but cannot retrieve patient data.

Knowing when to stop external troubleshooting and protect record integrity is proper troubleshooting.

## Clinical Use Tip

Never transmit an ECG until the patient name and required identifiers displayed on the EKG machine have been independently verified.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect patient identity before convenience or speed. Confirm barcode quality, scanner condition, workflow position, and configuration before assuming internal failure, and escalate any problem that could misidentify an ECG. Document the complete complaint, verified cause, correction, and final test.

That is successful troubleshooting.
