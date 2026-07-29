---
schemaVersion: 1
title: "GE Healthcare MAC 5500 HD Electrocardiograph (EKG) Machine - Internal Memory Full Or Stored ECG Retrieval Failure"
issueTitle: "Internal Memory Full Or Stored ECG Retrieval Failure"
description: "Troubleshooting full internal storage or inaccessible ECG records caused by queued studies, incomplete transmission, filtering, workflow, software, or memory problems."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "GE Healthcare"
model: "MAC 5500 HD"
slug: "ge-healthcare-mac-5500-hd-internal-memory-full-or-stored-ecg-retrieval-failure"
dateAdded: "2026-07-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported a memory-full warning and were unable to save additional ECGs on the MAC 5500 HD."
  cause: "Clinical Engineering found multiple successfully archived ECGs remaining in local storage after prior transmission."
  resolution: "Clinical Engineering verified the records in MUSE, removed the confirmed archived copies through the approved workflow, and tested successful save, retrieval, and transmission of a new ECG."
helpfulDetails:
  - "Exact memory or retrieval message"
  - "Number and status of stored records"
  - "Search filters used"
  - "Pending transmission count"
  - "MUSE receipt verification"
  - "Records confirmed before deletion"
  - "Save and retrieval test result"
  - "Final available-storage status"
  - "Final device disposition"
---

## What This Guide Helps With

Troubleshooting full internal storage or inaccessible ECG records caused by queued studies, incomplete transmission, filtering, workflow, software, or memory problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Records and Maintain Clinical Workflow

Do not delete stored ECGs until their transmission, archival status, and patient association have been verified.

Notify clinical staff that storage or retrieval is impaired.

Use another verified electrocardiograph if the device cannot safely store a new ECG.

Do not continue acquiring studies if records may be overwritten, lost, or left unidentified.

Preserve any ECG that has not been confirmed in MUSE or the designated archive.

**Expected outcome:** New studies are redirected as needed and existing patient records are protected.

### 2. Confirm the Exact Memory or Retrieval Problem

Determine whether:

- A memory-full message is displayed.

- New ECGs cannot be saved.

- Stored records are missing from the visible list.

- Records appear but cannot be opened.

- Searches return no results.

- Records are waiting for transmission.

- The issue affects one record or the entire archive.

**Expected outcome:** The problem is categorized as storage capacity, record search, record access, or transmission backlog.

### 3. Verify Search and Filter Criteria

Review the stored-record search screen.

Clear unnecessary patient, date, status, or location filters.

Confirm the correct date range.

Search using verified patient identifiers.

Check for completed, pending, transmitted, or unconfirmed status categories as applicable.

Avoid creating a duplicate ECG until the original record status is known.

**Expected outcome:** The intended record appears when correct search criteria are used. If found and accessible, troubleshooting can stop after confirming its archival status.

### 4. Review the Transmission Queue

Check whether records are accumulating because they have not reached MUSE.

Identify records listed as pending, failed, or unsent.

Confirm network communication is available.

Do not delete queued records merely to clear memory.

Record the number and status of pending studies when visible.

**Expected outcome:** A transmission backlog is identified or ruled out as the cause of full storage.

### 5. Attempt Normal Transmission of Pending Records

When network service is available:

- Initiate the approved normal transmission process.

- Observe whether queued records leave the pending list.

- Confirm receipt in MUSE through the appropriate clinical or support workflow.

- Do not assume disappearance from the local queue guarantees successful archival.

**Expected outcome:** Pending studies transmit successfully and available storage increases. If normal operation returns, troubleshooting can stop after verification.

### 6. Restart the Electrocardiograph

When no record is actively being acquired, saved, or transmitted:

- Exit the patient workflow.

- Shut down normally.

- Restart the unit.

- Recheck stored-record access and memory status.

**Expected outcome:** The storage index and record list load normally after restart.

### 7. Compare One Record With Other Stored Records

Attempt to open several records with different dates or statuses.

Identify whether only one record is inaccessible.

Determine whether recently acquired records behave differently from older records.

Note whether the same record can be found in MUSE.

**Expected outcome:** The issue is isolated to a single record or confirmed as a broader internal-storage problem.

### 8. Verify MUSE Receipt Before Any Authorized Deletion

Before clearing records:

- Confirm the exact ECGs are present in MUSE or the approved archive.

- Match patient identifiers, acquisition date, and study time.

- Follow facility policy for local record deletion.

- Do not delete records that remain clinically or legally unverified.

**Expected outcome:** Only records confirmed as safely archived are eligible for authorized removal.

### 9. Clear Confirmed Archived Records Through the Approved Workflow

Qualified personnel may remove locally stored records only through the normal user-accessible workflow and according to policy.

Do not use unauthorized service menus, file-system tools, or forced memory-clearing procedures.

**Expected outcome:** Internal storage becomes available and new test records can be saved and retrieved normally.

### 10. Perform Final Functional Verification

After correction:

- Acquire or create an approved test ECG.

- Save the test record.

- Retrieve it from local storage.

- Transmit it when applicable.

- Confirm receipt in MUSE.

- Verify the local queue and memory status are normal.

**Expected outcome:** The device can save, retrieve, and transmit a test ECG without storage warnings. The unit may be returned to service.

## If the Problem Persists

Search filters, transmission backlog, normal restart, and authorized record-management causes have been ruled out. The remaining possibilities may include corrupted record indexing, internal storage failure, database corruption, software malfunction, or a MUSE/interface issue.

The device should be:

- Removed from service if it cannot reliably save or retrieve ECGs

- Labeled Out of Service

- Sent for repair or bench evaluation

- Evaluated using appropriate GE Healthcare documentation and approved test equipment

- Repaired or configured only by qualified personnel

- Coordinate with MUSE or application support before any action that could alter stored patient data. Return the unit to service only after save, retrieval, and transmission functions are verified.

- Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never delete a locally stored ECG until its correct patient identity and successful receipt in the permanent archive are confirmed.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Stored ECGs are patient records, not disposable files. Protect them, verify search and transmission status, remove only confirmed archived records through approved methods, and escalate suspected storage corruption appropriately.

That is successful troubleshooting.
