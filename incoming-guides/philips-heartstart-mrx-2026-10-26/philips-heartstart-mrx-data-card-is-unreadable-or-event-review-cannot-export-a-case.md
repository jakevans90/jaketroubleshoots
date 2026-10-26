---
schemaVersion: 1
title: "Philips HeartStart MRx Defibrillator - Data Card Is Unreadable or Event Review Cannot Export a Case"
issueTitle: "Data Card Is Unreadable or Event Review Cannot Export a Case"
description: "Troubleshoot unreadable removable media or failed case export caused by card condition, insertion, data availability, compatibility, or workstation-related problems."
assetType: "Defibrillator"
manufacturer: "Philips"
model: "HeartStart MRx"
slug: "philips-heartstart-mrx-data-card-is-unreadable-or-event-review-cannot-export-a-case"
dateAdded: "2026-10-26"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the HeartStart MRx data card could not be read when attempting to export a completed patient event."
  cause: "Clinical Engineering found the removable data card physically damaged and confirmed normal operation with compatible known-good media."
  resolution: "Removed the damaged card from use, verified event-storage and export operation with approved test media, and returned the MRx to service after functional verification."
helpfulDetails:
  - "Whether the card was recognized by the MRx"
  - "Whether the case appeared in Event Review"
  - "Card physical condition"
  - "Card insertion and seating"
  - "Known-good media results"
  - "External card-reader results"
  - "Workstation or application tested"
  - "Whether one or multiple cases were affected"
  - "Export results"
  - "Whether important data was preserved"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoot unreadable removable media or failed case export caused by card condition, insertion, data availability, compatibility, or workstation-related problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care Before Troubleshooting Data Functions

Do not interrupt active monitoring, pacing, defibrillation, or other patient care solely to troubleshoot event-data export.

If the MRx is otherwise clinically functional, address the data issue after the device is no longer supporting a patient. If broader operational problems are present, exchange the unit for another verified device.

**Expected outcome:** Data troubleshooting occurs without affecting patient care.

### 2. Confirm the Exact Failure

Determine whether:

- The MRx does not recognize the data card
- Event Review cannot locate the case
- A case is visible but will not export
- The card can be read in one location but not another
- Multiple cases or only one case are affected

Preserve existing event data whenever possible and avoid unnecessary formatting or deletion.

**Expected outcome:** The failure is narrowed to card recognition, stored case availability, export operation, or an external reader/workstation.

### 3. Verify Normal Device Operation

Confirm the MRx powers and operates normally and that the problem appears limited to data storage or export.

Check for abnormal restart, storage, display, control, or system behavior that could indicate a larger device problem.

**Expected outcome:** The device operates normally apart from the data-card or event-review complaint.

### 4. Inspect the Data Card

Remove the card only when appropriate and inspect it for:

- Physical damage
- Cracks or deformation
- Contamination
- Damaged contacts
- Improper insertion
- Evidence of liquid exposure

Do not force a card into the device or card reader.

**Expected outcome:** The card is physically intact, correctly oriented, and seats normally. If reseating restores reliable access, the issue is resolved after export verification.

### 5. Verify the Card Is the Correct Media

Confirm that the removable media being used is appropriate for the MRx and the organization's established data workflow.

Do not assume that an arbitrary card of similar physical size is compatible.

**Expected outcome:** The media matches the approved workflow and is recognized normally. If incorrect media was the cause, replace it with the approved media and stop troubleshooting after verification.

### 6. Determine Whether the Case Exists

Use the normal event-review functions to determine whether the expected patient event or case is actually present.

Confirm relevant date, time, case, and device information before concluding that export has failed.

**Expected outcome:** The intended case can be identified. If the case was simply selected incorrectly, successful review or export resolves the issue.

### 7. Compare With Known-Good Media

When permitted by organizational procedures, use a compatible known-good card to determine whether the problem follows the original card or remains with the MRx.

Do not overwrite or alter clinically important data during comparison testing.

**Expected outcome:** A known-good card is recognized and operates normally. If only the original card fails, remove that card from use and preserve it according to organizational data-handling procedures.

### 8. Check the External Reader or Review Workstation

If the MRx recognizes the card but a computer or review system does not, inspect the external side of the workflow.

Check:

- Card reader connection
- Reader condition
- Workstation recognition
- Appropriate application availability
- User access
- Destination storage availability
- Whether another approved workstation can read the same card

Do not install unauthorized software or modify protected workstation configurations.

**Expected outcome:** The card and case can be accessed through the approved review environment. If another reader or workstation succeeds, the problem is external to the MRx.

### 9. Test a Controlled Export

Using non-patient test data or an approved workflow when available, verify that the MRx can store and export event information through the normal process.

Avoid deleting existing patient-event information merely to create a test condition.

**Expected outcome:** Test data can be stored, recognized, and exported successfully. If so, the device data pathway is functional and troubleshooting can stop.

### 10. Complete Final Functional Verification

Confirm that:

- Compatible media is recognized
- Event data can be accessed
- An available case can be exported through the approved workflow
- The card can be removed and reinserted without intermittent recognition
- No broader device faults are present

**Expected outcome:** Data functions operate normally and the device may return to service if all required checks pass.

### 11. Escalate Persistent Data Failures

If known-good media is not recognized, cases cannot be accessed reliably, or export continues to fail after the external reader and workstation have been ruled out, stop external troubleshooting.

**Expected outcome:** The device is removed from service when data-management reliability is required and escalated for qualified evaluation.

## If the Problem Persists

Common media, insertion, workflow, reader, and workstation causes have been ruled out. Remaining causes may involve the device's storage interface, internal data-management functions, configuration, software, or another service-level condition.

The device should be:

- Removed from service when reliable event-data handling is required
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Philips documentation and approved test equipment
- Repaired or configured only by qualified personnel

Preserve clinically or legally important event data according to hospital policy. Perform required functional testing before returning the unit to service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not format, erase, or overwrite questionable media until clinically significant event information has been preserved or appropriately dispositioned.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect patient data while working methodically from the removable media outward through the complete export pathway. Verify the card, device, reader, and workstation before assuming an internal failure, and document both data preservation and final testing clearly.

That is successful troubleshooting.
