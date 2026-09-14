---
schemaVersion: 1
title: "Advanced Sterilization Products (ASP) STERRAD 100NX Sterilizer - Printer, Barcode Scanner, USB, or Cycle Record Failure"
issueTitle: "Printer, Barcode Scanner, USB, or Cycle Record Failure"
description: "Troubleshoot cycle-documentation and peripheral failures involving printing, barcode scanning, USB transfer, or missing records before assuming internal control failure."
assetType: "Sterilizer"
manufacturer: "Advanced Sterilization Products (ASP)"
model: "STERRAD 100NX"
slug: "advanced-sterilization-products-asp-sterrad-100nx-printer-barcode-scanner-usb-or-cycle-record-failure"
dateAdded: "2026-09-14"
taxonomyMode: "reuse"
ccr:
  complaint: "Sterile Processing reported that the STERRAD 100NX completed cycles normally but would not print the cycle record."
  cause: "Clinical Engineering found the printer paper was incorrectly loaded while the stored cycle record remained available on the sterilizer."
  resolution: "The printer media was reloaded correctly and a subsequent verification cycle produced a complete printed record."
helpfulDetails:
  - "Peripheral affected"
  - "Whether sterilization cycle completed"
  - "Record visible locally"
  - "Printer media condition"
  - "Cable condition"
  - "Scanner test result"
  - "USB device tested"
  - "Known-good substitution result"
  - "Restart result"
  - "Whether traceability was maintained"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoot cycle-documentation and peripheral failures involving printing, barcode scanning, USB transfer, or missing records before assuming internal control failure.

## Step-by-Step Troubleshooting

### 1. Protect Traceability and Sterile Processing Records

Do not ignore missing cycle documentation when the facility depends on it for sterilization traceability or load release.

Follow facility procedures for manual documentation or alternate record capture while troubleshooting.

**Expected outcome:** Instrument processing remains traceable even while a peripheral or documentation function is unavailable.

### 2. Identify the Exact Function That Failed

Determine whether the problem involves:

- Printer output
- Paper feeding
- Barcode scanner input
- USB recognition
- USB export
- Missing stored cycle record
- Incomplete record
- Multiple functions simultaneously

**Expected outcome:** The failure is narrowed to one peripheral, storage/export function, or a broader system issue.

### 3. Verify the Sterilization Cycle Itself Completed Normally

Confirm whether the cycle successfully completed and whether only the documentation function failed.

Do not confuse a peripheral failure with a failed sterilization process.

**Expected outcome:** The clinical significance of the problem is understood: process failure versus documentation failure.

### 4. Check External Peripheral Connections

Inspect accessible external cables and connectors for:

- Loose connections
- Bent or damaged plugs
- Pinched cables
- Contamination
- Strain
- Unapproved adapters

Reseat user-accessible connectors only when safe and intended for normal external connection.

**Expected outcome:** All peripheral connections are secure and undamaged.

### 5. Check Printer Consumables and Basic Condition

For printer complaints, verify accessible consumables and normal paper loading.

Inspect for obvious jams, damaged paper, or a cover that is not fully closed.

Do not disassemble the printer mechanism beyond normal accessible areas.

**Expected outcome:** The printer has usable media and no obvious external jam or loading problem.

### 6. Check Barcode Scanner Condition

Inspect the scanner window and cable for contamination or damage. Test an approved, clearly printed barcode that is known to scan elsewhere if available.

**Expected outcome:** A known-good barcode is read reliably.

If cleaning an accessible scanner window or reseating the connection restores scanning, verify the function and troubleshooting can stop.

### 7. Check USB Device and Port Externally

For USB problems, verify the approved device is correctly inserted and not physically damaged.

If facility policy allows, compare with another known-good approved USB device.

Do not use unknown personal storage media on clinical equipment.

**Expected outcome:** The sterilizer detects the approved USB device and can complete the intended export function.

### 8. Verify Record Availability on the Sterilizer

Determine whether the cycle record is visible or stored locally even though it cannot print or export.

This helps separate record-generation problems from printer or USB problems.

**Expected outcome:** The record either exists locally, indicating a peripheral/export issue, or is also missing, indicating a broader documentation problem.

### 9. Restart Only When Operationally Appropriate

If the device is idle and facility procedures allow, perform a normal controlled restart to clear a transient peripheral interface problem.

Do not power-cycle during an active cycle or while record-writing activity is underway.

**Expected outcome:** The sterilizer returns to normal operation and the affected peripheral function is restored.

If the failure clears and a new verification record prints, scans, or exports normally, troubleshooting can stop.

### 10. Escalate Persistent Documentation or Peripheral Failure

If known-good external devices and connections do not resolve the issue, remove the affected peripheral function from use and determine whether the sterilizer itself must be removed from service based on facility traceability requirements.

Possible service-level categories include interface electronics, internal printer hardware, storage, operating software, or control-system communication.

**Expected outcome:** Required sterilization documentation is not compromised by continuing to operate an inadequately documented system.

## If the Problem Persists

External connections, consumables, media, approved USB devices, scanner condition, and basic operating state have been checked.

The sterilizer should be:

- Removed from service when required documentation or traceability cannot be maintained
- Labeled Out of Service when the device cannot safely remain in workflow
- Sent for repair or qualified service evaluation
- Evaluated using ASP documentation and approved test equipment
- Repaired or configured only by qualified personnel

Following repair, verify cycle record creation, print or export functionality as applicable, and facility-required documentation before return to service.

Knowing when a documentation failure becomes a clinical workflow risk is proper troubleshooting.

## Clinical Use Tip

If electronic or printed cycle documentation is required for load release, use the facility-approved backup process rather than releasing loads without traceability.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Peripheral failures should be separated from true sterilization-process failures. Verify the cycle, check connections and consumables, compare known-good accessories, and confirm whether records exist locally before escalating. Traceability must remain intact throughout the troubleshooting process.

That is successful troubleshooting.
