---
schemaVersion: 1
title: "Getinge ED-Flow Endoscope Reprocessor (AER) - Barcode or Scope-ID Tracking Rejects a Valid Item"
issueTitle: "Barcode or Scope-ID Tracking Rejects a Valid Item"
description: "Troubleshoots valid barcode or scope-ID rejection caused by scanning, label condition, identification records, workflow selection, connectivity, or configuration mismatches."
assetType: "Endoscope Reprocessor (AER)"
manufacturer: "Getinge"
model: "ED-Flow"
slug: "getinge-ed-flow-barcode-or-scope-id-tracking-rejects-a-valid-item"
dateAdded: "2026-10-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Sterile Processing reported that a valid endoscope barcode was scanned successfully but the ED-Flow rejected the scope ID."
  cause: "Clinical Engineering found that the scope record contained an incorrect identifier that did not match the barcode on the endoscope."
  resolution: "Corrected the authorized tracking record, verified the scope was accepted and correctly associated with its cycle record, and returned the unit to service."
helpfulDetails:
  - "Exact rejection message."
  - "Type of identifier rejected."
  - "Scope ID involved."
  - "Label condition."
  - "Whether the scanner read the code."
  - "Known-good barcode test result."
  - "Selected workflow."
  - "Record status observed."
  - "Network/link status."
  - "Whether other ED-Flow units are affected."
  - "Results before and after correction."
  - "Final traceability status."
---

## What This Guide Helps With

Troubleshoots valid barcode or scope-ID rejection caused by scanning, label condition, identification records, workflow selection, connectivity, or configuration mismatches.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Traceability Record
Do not bypass required scope identification or traceability controls to force a reprocessing cycle.

If the affected scope cannot be properly associated with its processing record, use another approved scope or reprocessor while the tracking problem is investigated.

**Expected outcome:** Required reprocessing traceability is preserved.

### 2. Confirm What Is Being Rejected
Identify whether the rejected item is:
- Endoscope barcode.
- Scope ID.
- Operator ID.
- Accessory ID.
- Another required tracked item.

Record the exact displayed rejection message and determine whether the same identifier is accepted elsewhere in the department.

**Expected outcome:** The rejected identifier and point of failure are clearly established.

### 3. Inspect the Barcode or Identifier
Check the physical label or identifier for:
- Dirt or residue.
- Moisture.
- Scratches.
- Fading.
- Wrinkling.
- Partial obstruction.
- Poor print quality.
- Damage affecting readability.

Do not create an unapproved replacement identifier.

**Expected outcome:** The identifier is clean, legible, and physically intact.

### 4. Verify Scanner Condition and Positioning
Inspect the scanner or external reading device for obvious damage or contamination.

Try scanning another known-valid identifier using normal positioning and distance.

If multiple valid items fail to scan, focus on the scanner or interface rather than the original scope label.

**Expected outcome:** A known-valid barcode is read consistently.

### 5. Distinguish Read Failure From Database Rejection
Determine whether the scanner:
- Does not read the barcode at all, or
- Reads the identifier but the ED-Flow rejects it as invalid, unknown, or inappropriate for the selected workflow.

This distinction is important because successful reading with subsequent rejection points toward record, configuration, or integration issues rather than scanner optics.

**Expected outcome:** The failure is categorized as scanning versus validation.

### 6. Verify the Selected Workflow and Scope Association
Confirm that the correct reprocessing workflow, scope type, or related selection has been made before scanning the item.

Compare the accepted scope record with the physical scope identification.

Do not modify protected scope-processing parameters merely to make an identifier acceptable.

**Expected outcome:** The scanned scope corresponds to the correct configured workflow.

### 7. Check for Duplicate, Retired, or Incorrect Records
Using authorized tracking functions, verify that the identifier has not been:
- Entered incorrectly.
- Duplicated.
- Retired.
- Assigned to another scope.
- Associated with an incompatible record.

Avoid deleting or recreating records without approved documentation and authorization.

**Expected outcome:** The scope identifier matches one valid active record.

### 8. Verify External Tracking-System Connectivity
If scope validation depends on a connected tracking or network system, confirm that the ED-Flow has normal external connectivity and that other tracked items are being accepted.

Check accessible network cables and link indicators when applicable.

Determine whether other reprocessors or workstations are experiencing the same issue.

**Expected outcome:** The tracking path is available, or a broader infrastructure problem is identified.

### 9. Test With Another Known-Valid Scope ID
Scan another valid, compatible scope identifier.

If the second item is accepted, the issue is likely isolated to the original record or label.

If multiple valid scope IDs are rejected, suspect a system-wide tracking, configuration, scanner, or communication problem.

**Expected outcome:** The comparison isolates the fault to one identifier or the broader tracking system.

### 10. Correct Only Authorized External Record Issues
If an obvious administrative error is confirmed and Clinical Engineering is authorized to correct it, use the approved configuration process.

Do not access undocumented service menus or alter protected reprocessing logic.

**Expected outcome:** The valid scope identifier is correctly associated and accepted.

### 11. Perform Final Traceability Verification
Complete a controlled identification test and verify that:
- The scope ID is accepted.
- The correct scope record appears.
- The processing record associates with the intended scope.
- Required tracking information is retained.

**Expected outcome:** Scope identification and traceability operate correctly. Troubleshooting can stop after verification.

### 12. Remove From Service if Required Tracking Is Unreliable
If valid identifiers continue to be rejected and required traceability cannot be maintained, remove the affected ED-Flow from clinical use until the issue is corrected.

**Expected outcome:** Reprocessing does not continue with incomplete or unreliable traceability.

## If the Problem Persists

Common external causes including damaged labels, scanner contamination, incorrect workflow selection, record mismatch, duplicate identifiers, and basic network connectivity problems have been ruled out.

The remaining cause may involve tracking-system integration, database synchronization, configuration, scanner electronics, network infrastructure, or another service-level issue.

The device should be:
- Removed from service if required traceability cannot be maintained.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation as appropriate.
- Evaluated using appropriate Getinge documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Coordinate with the reprocessing tracking-system administrator or IT when the rejection appears to involve centralized records or communication.

Verify complete identification and record association before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Never bypass required scope identification merely to start a cycle; the reprocessing record must remain traceable to the correct endoscope.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- rendered from front matter -->

## Final Thought

Preserve patient safety and traceability, separate barcode-reading problems from record-validation problems, verify simple label and configuration causes first, escalate unresolved integration issues, and clearly document the verified correction.

That is successful troubleshooting.
