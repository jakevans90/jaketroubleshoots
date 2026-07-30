---
schemaVersion: 1
title: "Mortara ELI Series Electrocardiograph (EKG) Machine - Internal Memory Full Or Stored ECG Retrieval Failure"
issueTitle: "Internal Memory Full Or Stored ECG Retrieval Failure"
description: "Troubleshooting full internal storage or unavailable ECG records caused by backlog, filters, patient search, transmission, archive, or software problems."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "Mortara"
model: "ELI Series"
slug: "mortara-eli-series-internal-memory-full-or-stored-ecg-retrieval-failure"
dateAdded: "2026-07-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Mortara ELI Series EKG machine displayed a memory-full warning and would not save additional ECGs."
  cause: "Clinical Engineering found a backlog of completed ECGs that had not transmitted during a prior network interruption."
  resolution: "Confirmed the records transmitted successfully, removed only approved completed records, verified normal storage capacity, and completed a test ECG save-and-retrieval check."
helpfulDetails:
  - "Complete storage warning."
  - "Available memory status."
  - "Number of pending or unsent ECGs."
  - "Patient ID and acquisition date searched."
  - "Filters used."
  - "Transmission destination status."
  - "Records preserved before deletion."
  - "Records removed under approved workflow."
  - "Test ECG save and retrieval result."
  - "Final device status."
---

## What This Guide Helps With

Troubleshooting full internal storage or unavailable ECG records caused by backlog, filters, patient search, transmission, archive, or software problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Stored ECG Records

Do not delete, overwrite, or clear ECG records until required records are confirmed transmitted, printed, archived, or otherwise preserved according to facility policy.

If the device cannot save a clinically required ECG, use another verified EKG machine or the approved downtime process.

**Expected outcome:** Patient care continues and existing ECG records are protected from accidental loss.

### 2. Confirm the Exact Storage or Retrieval Problem

Determine whether:

- The device reports memory full.

- New ECGs cannot be saved.

- Previously acquired ECGs do not appear.

- A specific patient record cannot be found.

- Records appear but cannot be opened, printed, exported, or transmitted.

- The issue began after a network or transmission outage.

Record the complete displayed message.

**Expected outcome:** The issue is identified as capacity, search, access, transmission backlog, or record-integrity failure.

### 3. Verify the Correct Patient and Search Criteria

Confirm the operator is using the correct:

- Patient ID.

- Patient name spelling.

- Date range.

- Acquisition date.

- Department, location, or user filter.

- Stored-record category.

- Remove unnecessary filters and repeat the search.

**Expected outcome:** The intended ECG appears when correct search criteria are used. If found and accessible, troubleshooting can stop.

### 4. Check Whether Records Are Stored Locally or Remotely

Determine whether the expected ECG should be:

- In the EKG machine’s local memory.

- In a transmitted queue.

- In an ECG management system.

- On removable media.

- In a printed-only workflow.

Confirm that the record was actually saved before the device was powered down or moved.

**Expected outcome:** The search is directed to the correct storage location rather than assuming every ECG remains on the device.

### 5. Review Storage Status Through Normal Menus

Use only normal authorized functions to review:

- Available storage.

- Number of pending records.

- Sent and unsent ECGs.

- Exported or archived records.

- Failed transmission queue entries.

Do not clear storage or alter retention settings without authorization.

**Expected outcome:** The device indicates whether storage capacity is exhausted by unsent or retained records.

### 6. Check for a Transmission Backlog

Verify whether ECGs are waiting to transmit because of:

- Network interruption.

- Incorrect destination.

- Server or interface downtime.

- Device location or profile mismatch.

- Authentication or connectivity failure.

Compare with another working ELI Series device on the same network when available.

**Expected outcome:** A communication backlog is identified before records are deleted.

### 7. Preserve Required Records

Before removing records, confirm they have been successfully transferred or otherwise retained.

When authorized:

- Transmit pending ECGs.

- Export required records to approved media.

- Print required records.

Confirm receipt in the destination system.

Document any record that could not be preserved.

**Expected outcome:** Required ECGs are safely retained outside the device before storage is cleared.

### 8. Remove Records Only Through Approved Workflow

Delete or purge ECG records only when:

- Facility retention policy permits it.

- Records are confirmed transmitted or archived.

- The operator has appropriate authorization.

- The normal device workflow is used.

Do not perform bulk deletion solely to silence a memory warning without confirming record disposition.

**Expected outcome:** Sufficient storage is restored without losing required patient records.

### 9. Restart and Recheck Memory Status

After approved record management is complete, perform a normal shutdown and restart.

Review storage status and repeat the record search.

**Expected outcome:** The memory warning clears, available capacity is restored, and stored ECGs can be opened normally.

### 10. Acquire and Retrieve a Test ECG

Using approved test data and an ECG simulator:

- Acquire a test ECG.

- Save it.

Exit the record.

Search for it.

Open it.

Print, transmit, or export it as required.

Confirm successful receipt or output.

**Expected outcome:** The complete acquire-save-retrieve-output pathway works normally. Troubleshooting can stop.

### 11. Escalate Missing or Inaccessible Records

Immediately escalate if:

- Required patient ECGs appear missing.

- The device reports storage errors despite adequate capacity.

- Records cannot be opened or exported.

- The device repeatedly fills because transmissions do not complete.

Record dates, names, or identifiers appear corrupted.

The device freezes during retrieval.

**Expected outcome:** Potential data loss or record corruption is handled through the appropriate technical and clinical channels.

## If the Problem Persists

Common causes involving search filters, local versus remote storage, transmission backlog, and authorized record cleanup have been ruled out. The remaining problem may involve database corruption, internal storage failure, software instability, network services, destination configuration, or an ECG management interface.

The device should be:

- Removed from service when it cannot reliably save or retrieve required ECGs.

- Labeled Out of Service.

- Sent for repair or bench evaluation.

- Evaluated using appropriate Mortara documentation and approved test equipment.

- Repaired or configured only by qualified personnel.

Coordinate with information services, cybersecurity, and the ECG management system team when records are missing from the destination system. Preserve logs and avoid further deletion.

After repair, verify acquisition, saving, retrieval, printing, transmission, and export as applicable.

Knowing when to stop external troubleshooting is especially important when patient records may be at risk.

## Clinical Use Tip

Confirm an ECG is received at its intended destination before deleting it from local device memory.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Patient records must be protected while troubleshooting storage. Verify search criteria, record location, transmission status, and preservation before removing data or assuming internal failure. Escalate suspected corruption or missing records and document every action clearly.

That is successful troubleshooting.
