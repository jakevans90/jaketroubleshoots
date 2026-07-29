---
schemaVersion: 1
title: "GE Healthcare MAC 5500 HD Electrocardiograph (EKG) Machine - Patient ID Or Barcode Scanner Entry Failure"
issueTitle: "Patient ID Or Barcode Scanner Entry Failure"
description: "Troubleshooting failed patient-ID entry or barcode scanning caused by scanner power, connection, barcode quality, workflow, configuration, or input-device problems."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "GE Healthcare"
model: "MAC 5500 HD"
slug: "ge-healthcare-mac-5500-hd-patient-id-or-barcode-scanner-entry-failure"
dateAdded: "2026-07-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the barcode scanner activated but would not enter the patient ID into the MAC 5500 HD."
  cause: "Clinical Engineering found that the scanner cable was partially disconnected at the electrocardiograph."
  resolution: "Clinical Engineering reseated the scanner connection, verified accurate entry with an approved test barcode, and returned the unit to service."
helpfulDetails:
  - "Scanner indicator or aiming-light behavior"
  - "Barcode condition and type tested"
  - "Whether manual entry worked"
  - "Input field used"
  - "Scanner cable and connector condition"
  - "Known-good scanner results"
  - "Patient lookup or order-retrieval status"
  - "Whether other units were affected"
  - "Final verification result"
---

## What This Guide Helps With

Troubleshooting failed patient-ID entry or barcode scanning caused by scanner power, connection, barcode quality, workflow, configuration, or input-device problems.

## Step-by-Step Troubleshooting

### 1. Ensure Patient Identification Safety

Do not acquire or transmit an ECG under an unverified, incorrect, or incomplete patient identity.

Stop before saving or transmitting the ECG.

Confirm the patient using the facility-approved identification process.

Use manual entry only when permitted by policy and the information can be independently verified.

Prevent duplicate or mismatched records.

**Expected outcome:** No ECG is associated with the wrong patient while troubleshooting continues.

### 2. Confirm the Exact Entry Failure

Determine whether:

- The scanner has no power or indicator light.

- The scanner activates but does not read.

- The barcode reads but the information does not populate.

- Manual keyboard entry also fails.

- Only certain barcode labels fail.

- The issue occurs before acquisition, during order lookup, or during record editing.

**Expected outcome:** The problem is isolated to scanner activation, barcode decoding, data entry, or downstream patient-data handling.

### 3. Inspect the Barcode and Scanning Conditions

Inspect the patient wristband or printed barcode.

Check for:

- Wrinkles, smearing, fading, or damage

- Curvature around the wrist

- Glare or protective coverings

- Poor contrast

- Excessive scanning distance or angle

- An obstructed scanner window

- Use a clean, flat, known-readable facility barcode for comparison.

**Expected outcome:** A clear barcode can be scanned under normal lighting and positioning. If only the original label fails, request a replacement label and stop troubleshooting the device.

### 4. Verify Scanner Power and Connection

Inspect the scanner cable and connection to the MAC 5500 HD.

Confirm the connector is fully seated.

Inspect the cable, connector, and scanner housing for damage.

Verify any scanner indicator or aiming light operates.

Disconnect and reconnect the scanner only while the device is not being used for patient acquisition.

**Expected outcome:** The scanner powers normally and remains connected. If reseating restores operation, troubleshooting can stop after verification.

### 5. Restart the Scanner and Electrocardiograph

With no active patient record open:

- Exit the current patient-entry screen.

- Power down the electrocardiograph normally.

- Disconnect and reconnect the scanner.

- Restart the unit.

- Reopen patient entry and test a known-readable barcode.

**Expected outcome:** The scanner initializes and sends data normally after restart.

### 6. Compare Barcode and Manual Entry

Test patient-data entry without using real patient information.

Attempt scanner entry using an approved test barcode.

Attempt manual keyboard entry in the same field.

Confirm the cursor is active in the intended field.

Check whether the interface accepts ordinary text and numbers.

**Expected outcome:** If manual entry works but scanning does not, focus on the scanner, barcode format, or scanner configuration. If neither works, the device interface or software requires further evaluation.

### 7. Verify the Correct Workflow and Input Field

Confirm the operator is scanning into the intended patient-ID or order field.

Verify the correct patient-entry screen is open.

Clear any partially entered or hidden characters.

Confirm the record is not locked or already finalized.

Avoid scanning into free-text fields that do not trigger order or patient lookup.

**Expected outcome:** Scanned data appears in the intended field and can be accepted by the workflow. If correct field selection resolves the issue, troubleshooting can stop.

### 8. Substitute a Known-Good Compatible Scanner

When available, connect a verified compatible barcode scanner.

Do not change scanner programming, barcode symbology settings, prefixes, or suffixes unless authorized and supported by approved documentation.

**Expected outcome:** If the known-good scanner works, remove the original scanner from service. If both scanners fail, continue evaluating the electrocardiograph or system configuration.

### 9. Check for a Broader Patient-Data or Network Issue

Determine whether patient lookup or order retrieval is also failing.

Test whether manually entered patient data can be saved locally.

Check whether other MAC systems can retrieve the same patient or order.

Confirm network communication is available when lookup depends on the network.

Coordinate with the MUSE, interface, or IT support team when multiple devices are affected.

**Expected outcome:** The failure is identified as local scanner input or a broader patient-data interface problem.

### 10. Perform Final Functional Verification

After correction:

- Scan an approved test barcode.

- Confirm the correct characters populate the intended field.

- Verify no extra, missing, or transposed characters appear.

- Confirm the record can proceed through the normal workflow.

- Clear all test information before return to clinical use.

**Expected outcome:** Barcode and manual patient-ID entry work accurately and consistently. The unit may be returned to service.

## If the Problem Persists

External barcode, connection, positioning, and scanner causes have been ruled out. The remaining possibilities may include scanner programming incompatibility, device input-port failure, patient-data configuration, software corruption, or an interface problem.

The device should be:

- Removed from service if patient identity cannot be entered reliably

- Labeled Out of Service

- Sent for repair or bench evaluation

- Evaluated using appropriate GE Healthcare documentation and approved test equipment

- Repaired or configured only by qualified personnel

- Coordinate with MUSE, interface, or IT support when the scanner operates but patient lookup or order matching fails. Return the device to service only after accurate patient-data entry is verified.

- Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never transmit an ECG until the displayed patient identity has been matched to two approved patient identifiers.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Accurate patient identification is more important than completing the ECG quickly. Verify the label, scanner, connection, workflow, and interface before escalating, and document exactly how correct patient-data entry was confirmed.

That is successful troubleshooting.
