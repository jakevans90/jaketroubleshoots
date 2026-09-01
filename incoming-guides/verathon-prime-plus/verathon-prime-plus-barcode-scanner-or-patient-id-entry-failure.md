---
schemaVersion: 1
title: "Verathon Prime Plus Bladder Scanner - Barcode Scanner or Patient ID Entry Failure"
issueTitle: "Barcode Scanner or Patient ID Entry Failure"
description: "Helps isolate barcode quality, scanner positioning, connection, patient-entry workflow, control-input, and configuration causes of patient identification failure."
assetType: "Bladder Scanner"
manufacturer: "Verathon"
model: "Prime Plus"
slug: "verathon-prime-plus-barcode-scanner-or-patient-id-entry-failure"
dateAdded: "2026-09-01"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported the Prime Plus would not read patient wristband barcodes but manual patient ID entry still worked."
  cause: "Clinical Engineering found the barcode scanner connection was loose at the accessible external connector."
  resolution: "Clinical Engineering reseated the connection, verified repeated reads with an approved test barcode, confirmed correct field population, and returned the scanner to service."
helpfulDetails:
  - "Whether barcode scanner activated"
  - "Barcode condition"
  - "Types of barcodes tested"
  - "Positioning attempts"
  - "Scanner or cable condition"
  - "Connector condition"
  - "Known-good barcode result"
  - "Manual entry result"
  - "Whether correct data populated"
  - "Final device status"
---
## What This Guide Helps With

Helps isolate barcode quality, scanner positioning, connection, patient-entry workflow, control-input, and configuration causes of patient identification failure.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification and Confirm the Complaint
Do not allow incorrect patient identification to be attached to an examination. If barcode entry is unreliable, use the facility-approved manual patient-identification process or another verified scanner.

Confirm whether:
- Barcode scanner does not activate
- Barcode is read but incorrect data appears
- Some barcodes work and others do not
- Manual patient ID entry also fails
- Patient fields cannot be selected or edited

**Expected outcome:** The exact identification failure is defined without risking assignment of data to the wrong patient.

### 2. Inspect the Barcode
Check the test barcode or patient wristband for:
- Damage
- Wrinkles
- Smearing
- Poor printing
- Reflective covering
- Curvature
- Obstruction

Use an approved test barcode when available rather than repeatedly scanning a patient's wristband during troubleshooting.

**Expected outcome:** A clean, readable barcode is available for testing. If replacing a damaged label restores reliable scanning, troubleshooting can stop after verification.

### 3. Verify Scanner Positioning
Attempt scanning at a normal working distance and angle. Avoid holding the scanner excessively close, far away, or at an extreme angle.

Ensure the barcode is adequately illuminated and unobstructed.

**Expected outcome:** The scanner recognizes the barcode consistently. If positioning corrects the issue, verify repeated successful scans and stop troubleshooting.

### 4. Inspect the Barcode Scanner and Connection
Inspect the barcode scanner housing, cable, accessible connector, or integrated scanning area as applicable for:
- Physical damage
- Loose connection
- Contamination
- Cracked lens or window
- Cable strain

Reseat accessible connections if appropriate.

**Expected outcome:** The barcode scanner is physically intact and securely connected. If reseating restores operation, verify repeated scans.

### 5. Compare With a Known-Good Barcode
Scan a known-good barcode that is compatible with the facility's normal workflow.

This helps distinguish a scanner problem from a single poor-quality barcode.

**Expected outcome:** The known-good barcode scans successfully. If only the original barcode fails, the scanner is functioning and the label or source data should be addressed.

### 6. Test Manual Patient ID Entry
Using an approved test workflow, determine whether patient ID can be entered manually through the normal operator-accessible controls.

Do not use real patient identifiers for unnecessary testing.

**Expected outcome:** Manual entry is accepted and displayed correctly. If manual entry also fails, the problem may involve the user interface, application, or configuration rather than the barcode reader alone.

### 7. Verify Authorized Workflow and Configuration
Confirm the normal patient-identification workflow is selected and that barcode use has not been unintentionally bypassed or changed within authorized operator-accessible settings.

Do not enter restricted service menus or alter institutional interface configuration without authorization.

**Expected outcome:** The scanner is using the approved identification workflow. If an authorized workflow correction restores scanning, document the change and proceed to final verification.

### 8. Perform Final Functional Verification
Using approved test data, confirm:
- Barcode scanner activates
- Barcode is read consistently
- Correct identifier populates the intended field
- Manual entry works if supported by workflow
- A representative exam can be associated with the correct test record

**Expected outcome:** Patient identification functions reliably and accurately. Troubleshooting can stop and the device may return to service.

## If the Problem Persists

Barcode condition, positioning, accessible connections, known-good barcode testing, manual entry, and authorized workflow checks have been completed. The remaining problem may involve the scanner hardware, application software, internal connection, barcode configuration, or hospital interface.

The device should be:
- Removed from service if reliable patient identification cannot be assured
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Verathon documentation and approved test equipment
- Repaired or configured only by qualified personnel

Coordinate with IT or interface support when the device reads barcodes correctly but mapped patient information is incorrect or unavailable.

Verify correct patient identification end to end before return to service.

## Clinical Use Tip

Never accept a partially correct or inconsistent patient identifier; verify the complete patient-identification path before attaching an exam to a record.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter; optional explanatory prose may follow. -->



## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Patient identification errors have direct clinical and documentation consequences. Rule out barcode quality, positioning, and external connection issues first, verify the complete identification workflow, and remove the scanner from service whenever accurate patient association cannot be assured.

That is successful troubleshooting.
