---
schemaVersion: 1
title: "Boston Scientific OPAL HDx Electrophysiology Mapping System - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "Troubleshoots study-save, processing, or export failures involving workflow state, storage, patient data, network destinations, external media, and workstation stability."
assetType: "Electrophysiology Mapping System"
manufacturer: "Boston Scientific"
model: "OPAL HDx"
slug: "boston-scientific-opal-hdx-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-10-15"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that an OPAL HDx study saved locally but would not export to the configured network destination."
  cause: "Clinical Engineering found that the workstation's external network connection had been disconnected."
  resolution: "Clinical Engineering restored the network connection, repeated the export, verified receipt at the configured destination, and confirmed normal study handling."
helpfulDetails:
  - "Exact save, processing, or export failure"
  - "Exact message displayed"
  - "Study affected"
  - "Whether local save works"
  - "Workstation responsiveness"
  - "Network connection status"
  - "Destination availability"
  - "Approved external media used"
  - "Whether other studies are affected"
  - "Final save and export verification"
---

## What This Guide Helps With

Troubleshoots study-save, processing, or export failures involving workflow state, storage, patient data, network destinations, external media, and workstation stability.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Existing Data

Do not immediately restart, power-cycle, or disconnect the workstation if unsaved procedure data may still be recoverable.

Coordinate with the clinical team and preserve the current study state whenever possible.

**Expected outcome:** Available clinical data is protected while the failure is investigated.

### 2. Confirm Which Function Failed

Determine whether the system cannot:

- Save the active study
- Reopen or process saved data
- Complete a reconstruction or processing step
- Export the study
- Send information to a configured destination
- Access previously stored studies

Record the exact message and workflow step.

**Expected outcome:** The failed function and affected study are identified.

### 3. Determine Whether the Problem Affects One Study or All Studies

Check whether the failure:

- Occurs only with the current study
- Affects multiple studies
- Began after a workstation freeze
- Appears only when exporting
- Appears only with one destination

Do not create unnecessary test patient records in a production system.

**Expected outcome:** The issue is narrowed to a single study, application workflow, storage function, or external destination.

### 4. Verify Required Study Information

Confirm that necessary patient and study information has been entered correctly for the local workflow.

Do not alter patient identifiers simply to force a save or export.

**Expected outcome:** Required study information is present and consistent.

### 5. Check Workstation Responsiveness

Verify the workstation remains responsive and that normal controls operate.

If the system is freezing or severely delayed, avoid repeated save commands that may create additional uncertainty.

**Expected outcome:** Workstation stability is confirmed or identified as part of the problem.

### 6. Check External Network or Destination Connections

If saving locally works but export fails, inspect the external network connection and determine whether the configured receiving destination is available.

Coordinate with IT or the system owner if a server, archive, or integration endpoint may be unavailable.

**Expected outcome:** Local study processing is separated from network or destination failure.

### 7. Check Approved External Media When Used

If an approved external export device or removable medium is part of the workflow, verify it is:

- Properly connected
- Recognized by the system
- Appropriate for the intended workflow
- Not visibly damaged

Do not connect unauthorized media to a clinical system.

**Expected outcome:** The external export path is available or isolated as the cause.

### 8. Avoid Unapproved File Manipulation

Do not manually delete system files, alter database content, modify operating-system storage, or use unsupported utilities to free space or recover a study.

If the system reports a storage-related problem that cannot be corrected through approved user-accessible functions, escalate.

**Expected outcome:** Study integrity is protected and unsupported actions are avoided.

### 9. Retry the Workflow After Correcting the External Cause

After restoring a network connection, destination, approved media, or other external dependency, retry the affected save or export operation.

Verify the study is actually present at the intended destination.

**Expected outcome:** Study processing completes and the data is accessible where expected. Troubleshooting can stop.

### 10. Perform Final Functional Verification

With no patient dependent on the system, verify an approved test workflow can:

- Create or access a study as appropriate
- Perform required processing
- Save normally
- Export through the intended supported path

**Expected outcome:** Study handling functions operate consistently without freezes or errors.

### 11. Escalate Persistent Study-Handling Failures

If the study cannot be saved, processed, reconstructed, or exported after external workflow, network, and destination causes are ruled out, remove the system from service when the failure compromises clinical operation or data integrity.

Do not perform unsupported database or operating-system repair.

**Expected outcome:** The system and any affected clinical data are referred for qualified support without additional risk to study integrity.

## If the Problem Persists

Common external workflow, patient-data, network, destination, media, and workstation causes have been ruled out. The remaining problem may involve application software, internal storage, database integrity, system configuration, workstation hardware, or another service-level condition.

The device should be:

- Removed from service when reliable study storage cannot be assured
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Protect affected clinical data and involve the appropriate manufacturer or information-systems support team before attempting recovery. Verify complete save, processing, and export functions before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Before rebooting a mapping workstation with a save or export problem, determine whether unsaved procedural data could be lost.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the study data before taking corrective action, identify whether the failure is local or external, and verify network and workflow dependencies before assuming an internal storage problem. Escalate appropriately when data integrity or reliable study handling cannot be assured.

That is successful troubleshooting.
