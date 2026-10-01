---
schemaVersion: 1
title: "Elekta Versa HD Radiation Therapy System - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "An imaging study cannot save, reconstruct, or export because of workflow, storage, workstation, network, destination, or communication problems."
assetType: "Radiation Therapy System"
manufacturer: "Elekta"
model: "Versa HD"
slug: "elekta-versa-hd-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-10-01"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that a Versa HD imaging study completed acquisition but would not export to the configured destination."
  cause: "Clinical Engineering found that the affected workstation had lost its external network connection."
  resolution: "Clinical Engineering restored the network connection, exported the existing study successfully, and verified correct receipt at the destination before return to service."
helpfulDetails:
  - "Whether save, reconstruction, or export failed"
  - "Exact displayed message"
  - "Patient or study affected"
  - "Whether other studies are affected"
  - "Workstation responsiveness"
  - "Visible storage or queue status"
  - "Network link condition"
  - "Destination availability"
  - "Whether existing data was preserved"
  - "Successful receipt after correction"
  - "Final system status"
---
## What This Guide Helps With

An imaging study cannot save, reconstruct, or export because of workflow, storage, workstation, network, destination, or communication problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data and Treatment Workflow

Do not delete studies, repeat patient imaging, or create replacement records until the existing data and clinical impact are understood.

If imaging is required for treatment decisions, follow the department's approved downtime or alternative workflow.

**Expected outcome:** Existing patient data is protected and unnecessary repeat imaging is avoided.

### 2. Identify the Failed Operation

Determine whether the study fails to save locally, fails during reconstruction, cannot be opened after reconstruction, or fails only during export.

Record the exact message and the point where processing stops.

**Expected outcome:** The problem is narrowed to saving, reconstruction, local storage, or export.

### 3. Verify Study and Patient Context

Confirm that the correct patient and study are active and that the acquisition completed normally.

Check whether the problem affects one study or all newly acquired studies.

**Expected outcome:** An isolated record problem is distinguished from a system-wide processing failure.

### 4. Check Workstation Responsiveness

Verify that the acquisition or review workstation is responsive and that no related application is frozen.

Check accessible indicators for abnormal workstation behavior.

**Expected outcome:** The processing workstation is functioning normally or a workstation problem is identified.

### 5. Check Visible Storage Status

Review normal user-accessible indicators for storage availability, queue status, or pending processing.

Do not delete clinical data merely to create space unless following an approved data-management procedure.

**Expected outcome:** No obvious user-visible storage condition is blocking study processing.

### 6. Inspect External Network Connections

If the failure involves export or remote storage, check accessible network cables, link status, and connection to the hospital network.

**Expected outcome:** The physical network path is intact.

### 7. Verify Destination Availability

Confirm that the intended PACS, oncology information system, archive, or other destination is available.

Determine whether other systems are successfully sending to the same destination.

**Expected outcome:** The destination is available or an external server/interface outage is identified.

### 8. Retry the Appropriate Operation

After correcting any external workstation, network, or destination issue, retry the save, reconstruction, or export using the existing study when appropriate.

Avoid repeating the patient acquisition unless clinically necessary and authorized.

**Expected outcome:** The existing study processes successfully without requiring unnecessary reacquisition.

### 9. Confirm Data Integrity

Verify that the completed reconstruction appears correct and that exported data arrives at the intended destination under the correct patient and study.

**Expected outcome:** The full study-processing path is successful. Troubleshooting can stop once integrity and receipt are confirmed.

### 10. Escalate Persistent Processing Failure

If studies continue to fail after workstation, visible storage, network, and destination checks, stop troubleshooting.

**Expected outcome:** The affected workflow is removed from clinical use and referred for qualified service or IT evaluation.

## If the Problem Persists

External causes have been ruled out. Remaining possibilities may involve application services, local storage hardware, reconstruction processing, databases, system software, network configuration, interface services, or other service-level conditions.

The Versa HD should be:

- Removed from affected clinical workflow if study integrity cannot be assured.
- Labeled Out of Service when safe treatment depends on the unavailable function.
- Evaluated using appropriate Elekta and institutional IT documentation.
- Repaired or configured only by qualified personnel.
- Verified with an end-to-end test before normal clinical use resumes.

Do not delete patient data, alter databases, or perform unsupported recovery procedures.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Preserve the original study whenever possible; repeating patient imaging should not be the first response to a save, reconstruction, or export problem.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect existing patient data, identify exactly where processing stops, and verify workstation, storage, network, and destination conditions before assuming an internal system failure. Escalate unresolved processing faults with clear documentation.

That is successful troubleshooting.
