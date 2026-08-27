---
schemaVersion: 1
title: "GE Healthcare MAC 7 Electrocardiograph (EKG) Machine - Patient ID or Barcode Scanner Entry Failure"
issueTitle: "Patient ID or Barcode Scanner Entry Failure"
description: "Troubleshooting patient ID entry or barcode scanning failures caused by barcode quality, scanner connection, input selection, data format, or workflow configuration."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "GE Healthcare"
model: "MAC 7"
slug: "ge-healthcare-mac-7-patient-id-or-barcode-scanner-entry-failure"
dateAdded: "2026-08-27"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the MAC 7 would not accept patient ID barcodes even though manual entry remained available."
  cause: "Clinical Engineering found the external barcode scanner had an intermittent cable connection and failed with multiple known-good labels."
  resolution: "Replaced the defective scanner and verified successful scanning and correct patient ID field population using approved test data."
helpfulDetails:
  - "Manual entry result."
  - "Scanner response."
  - "Barcode source."
  - "Known-good barcode tested."
  - "Scanner cable and connector condition."
  - "Known-good scanner substitution."
  - "Fields affected."
  - "Whether scanned data was rejected or misdirected."
  - "Departments or label sources affected."
  - "Final workflow verification."
  - "Final device status."
---

## What This Guide Helps With

Troubleshooting patient ID entry or barcode scanning failures caused by barcode quality, scanner connection, input selection, data format, or workflow configuration.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification Accuracy

Do not acquire or transmit a diagnostic ECG under an incorrect patient identity merely to work around an entry problem.

If patient identification cannot be reliably entered and verified, use another approved workflow or another verified ECG system.

**Expected outcome:** No ECG is associated with an uncertain or incorrect patient record.

### 2. Confirm the Exact Entry Failure

Determine whether manual patient ID entry fails, barcode scanning fails, or both.

Confirm whether the scanner produces no response, reads the barcode incorrectly, or reads data that the MAC 7 does not accept.

**Expected outcome:** The problem is separated into scanner hardware, barcode quality, or data-entry/workflow categories.

### 3. Test Manual Patient Entry

Using non-patient test information, verify that the keyboard or touchscreen can enter text into the appropriate field.

**Expected outcome:** Manual entry works normally. If manual entry also fails, troubleshoot the affected control input rather than assuming a scanner problem.

### 4. Inspect the Barcode

Confirm that the barcode is readable, undamaged, appropriately printed, and not obscured by wrinkles, glare, contamination, or excessive curvature.

Test a known-good barcode used successfully in the same workflow if available.

**Expected outcome:** The scanner reads a known-good barcode consistently. If only the original barcode fails, the problem is likely with the label or barcode source.

### 5. Inspect and Reseat the Scanner Connection

If an external scanner is used, inspect its accessible cable and connector for damage and reseat the connection.

Avoid forcing connectors or using adapters not approved for the system.

**Expected outcome:** The scanner powers or initializes normally and produces consistent scan attempts.

### 6. Substitute a Known-Good Scanner When Appropriate

If a compatible approved scanner is available, substitute it without changing other configuration.

**Expected outcome:** The known-good scanner reads accepted barcodes successfully. If so, remove the original scanner from service.

### 7. Verify Accessible Input and Workflow Settings

Confirm that the intended patient-entry method is enabled and that no obvious user-accessible setting has been changed.

Do not alter restricted configuration, patient-identity mapping, or integration settings without authorization.

**Expected outcome:** The MAC 7 is configured for the expected patient-entry workflow.

### 8. Compare Barcode Content With the Expected Workflow

If the scanner visibly reads data but the MAC 7 rejects it, determine whether the issue affects all barcodes or only those from one registration source or label type.

Coordinate with the appropriate clinical application or IT team if the failure appears related to barcode formatting or patient-data workflow.

**Expected outcome:** A device-local scanning problem is distinguished from a barcode-generation or enterprise workflow issue.

### 9. Perform Final Patient-ID Workflow Verification

Using approved test data, confirm manual entry, barcode scanning if applicable, correct field population, and accurate review of the entered identifier before acquisition.

**Expected outcome:** Patient identification can be entered and verified accurately and consistently. The device may return to service when the workflow is proven reliable.

### 10. Escalate Persistent Entry Failure

If manual input works but multiple known-good scanners or valid barcodes fail, or data consistently enters the wrong fields, stop external troubleshooting.

**Expected outcome:** The problem is escalated for configuration, software, interface, or hardware evaluation.

## If the Problem Persists

Common barcode quality, scanner connection, accessory, and user-accessible workflow causes have been ruled out. Remaining possibilities include scanner-interface configuration, software behavior, patient-data mapping, enterprise integration, or internal hardware problems.

The device should be:

- Removed from service when reliable patient identification cannot be assured.
- Labeled Out of Service when appropriate.
- Sent for repair or bench evaluation if a device fault is suspected.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Configured only by qualified and authorized personnel.

If the problem involves registration or patient-data integration rather than the ECG hardware, coordinate with the appropriate IT or clinical systems team. Complete end-to-end patient-identity verification before return to normal workflow. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Always verify the displayed patient identity after a barcode scan; a successful scan does not by itself prove the correct patient information populated the intended field.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Patient identification errors can create greater risk than a failed scan itself. Verify the barcode, scanner, controls, and complete data-entry path before escalating suspected configuration or integration problems.

That is successful troubleshooting.
