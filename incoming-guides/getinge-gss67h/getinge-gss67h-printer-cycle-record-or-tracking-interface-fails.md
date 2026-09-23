---
schemaVersion: 1
title: "Getinge GSS67H Sterilizer - Printer, Cycle Record, or Tracking Interface Fails"
issueTitle: "Printer, Cycle Record, or Tracking Interface Fails"
description: "Use this guide when cycle documentation will not print, save, display, export, or transfer to an installed tracking system."
assetType: "Sterilizer"
manufacturer: "Getinge"
model: "GSS67H"
slug: "getinge-gss67h-printer-cycle-record-or-tracking-interface-fails"
dateAdded: "2026-09-23"
taxonomyMode: "reuse"
ccr:
  complaint: "Sterile Processing reported the Getinge GSS67H completed cycles but the local cycle record would not print."
  cause: "Clinical Engineering found the printer paper was incorrectly seated and was not feeding through the accessible printer path."
  resolution: "Clinical Engineering correctly installed the approved paper, generated a new cycle record, verified complete printing, and returned the documentation function to service."
helpfulDetails:
  - "Printing, storage, or tracking function affected"
  - "Whether cycles completed normally"
  - "Printer supply condition"
  - "Cable or network-link condition"
  - "Other systems affected"
  - "Interface destination"
  - "Recent configuration changes"
  - "Test-record result"
  - "Historical-record availability"
  - "Final device status"
---
## What This Guide Helps With

Use this guide when cycle documentation will not print, save, display, export, or transfer to an installed tracking system.

## Step-by-Step Troubleshooting

### 1. Protect Process Documentation
Determine whether the documentation failure prevents the facility from verifying or releasing sterilized loads. If required cycle records are unavailable, follow Sterile Processing policy before releasing affected loads.

**Expected outcome:** Instrument-processing decisions are not made without required cycle documentation.

### 2. Confirm the Exact Failure
Identify whether the problem affects the local printer, displayed cycle record, saved record, barcode or tracking interface, or network transfer.

Determine whether cycles themselves complete normally.

**Expected outcome:** The documentation problem is separated from a sterilization-process failure.

### 3. Check Printer Supplies and Physical Condition
For local printing problems, verify approved paper or other required consumables are correctly installed and not jammed.

Inspect accessible printer covers and feed areas for obvious obstruction.

**Expected outcome:** The printer has proper supplies and a clear paper path. If correcting a paper issue restores printing, verify a complete record and stop troubleshooting.

### 4. Check Accessible Data Connections
Inspect Ethernet, serial, USB, or other installed external data connections as applicable for loose connectors, damage, or accidental disconnection.

Do not alter network architecture or protected configuration without authorization.

**Expected outcome:** External communication connections are secure. If reseating an approved connection restores communication, verify record transfer and stop troubleshooting.

### 5. Verify Connected-System Availability
Determine whether the problem is isolated to the sterilizer or whether the tracking system, server, switch, printer service, or interface used by other equipment is also unavailable.

Coordinate network or application outages with the responsible IT or integration team.

**Expected outcome:** Infrastructure problems are separated from sterilizer-specific faults.

### 6. Verify Basic Configuration
Confirm the expected printer or interface is selected and that no recent authorized change has altered the documented configuration.

Do not enter restricted service menus or change network parameters without approved documentation.

**Expected outcome:** The expected approved configuration is still in use.

### 7. Generate a New Test Record
When safe, perform an approved test cycle or record-generation function and determine whether the new record prints, saves, or transfers normally.

**Expected outcome:** A complete cycle record is produced and reaches its expected destination. If successful, troubleshooting can stop.

### 8. Verify Historical Record Availability
If applicable, confirm recent stored records remain accessible and that the failure did not result in unintended loss of required process documentation.

**Expected outcome:** Record integrity is confirmed or the loss is documented and escalated appropriately.

### 9. Escalate Persistent Documentation Failure
If supplies, cables, connected systems, and approved configuration are normal but the problem persists, escalate to qualified sterilizer service, IT, or the tracking-system owner as appropriate.

**Expected outcome:** The correct technical owner receives a clearly isolated documentation or communication problem.

## If the Problem Persists

Common external printer, cable, connectivity, and infrastructure issues have been ruled out. Remaining causes may involve an internal printer assembly, storage subsystem, interface module, software configuration, network configuration, or integration service.

The sterilizer should be:

- Removed from service when required documentation cannot be reliably produced and facility policy requires it for release.
- Labeled Out of Service when applicable.
- Sent for repair or qualified evaluation.
- Evaluated using manufacturer documentation and approved service tools.
- Configured or repaired only by qualified personnel.
- Verified for complete cycle-record generation and interface communication before return to unrestricted service.

Appropriate escalation between Clinical Engineering, IT, and Sterile Processing is part of successful troubleshooting.

## Clinical Use Tip

Verify the complete documentation path, not just the sterilizer display, when cycle records are required for load release or traceability.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Separate process performance from documentation failure, then check simple printer, cable, configuration, and infrastructure causes before assuming an internal fault. Verify the complete record path and document any operational restrictions clearly.

That is successful troubleshooting.
