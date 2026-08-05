---
schemaVersion: 1
title: "Medtronic Capnostream 35 Capnography Monitor - Internal Memory Full or Stored Trend Retrieval Failure"
issueTitle: "Internal Memory Full or Stored Trend Retrieval Failure"
description: "Addresses full storage, missing trends, retrieval errors, or inaccessible records caused by workflow, filters, date settings, export needs, or software problems."
assetType: "Capnography Monitor"
manufacturer: "Medtronic"
model: "Capnostream 35"
slug: "medtronic-capnostream-35-internal-memory-full-or-stored-trend-retrieval-failure"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that the Capnostream 35 displayed a memory-full condition and would not save additional trend records."
  cause: "Clinical Engineering confirmed that the internal storage contained retained completed-patient records and had reached available capacity."
  resolution: "Required records were exported, authorized old records were removed, and successful storage and retrieval of a new test record were verified."
helpfulDetails:
  - "Exact storage or retrieval message"
  - "Memory status"
  - "Patient or record searched"
  - "Date and time settings"
  - "Filters applied"
  - "Whether other records opened"
  - "Data exported before deletion"
  - "Authorized records cleared"
  - "New test-record result"
  - "Final device status"
---

## What This Guide Helps With

Addresses full storage, missing trends, retrieval errors, or inaccessible records caused by workflow, filters, date settings, export needs, or software problems.

## Step-by-Step Troubleshooting

### 1. Protect Active Monitoring and Preserve Records

Do not interrupt patient monitoring or delete stored data while the monitor is in active use. Move the patient to another verified monitor before restarting the device or performing data-management actions.

Determine whether records are required for clinical care, legal retention, quality review, or transfer before deleting or clearing anything.

**Expected outcome:** Patient monitoring and required stored information are protected.

### 2. Confirm the Exact Storage Problem

Determine whether the monitor reports full memory, cannot save new trends, cannot locate a specific patient record, displays blank trend lists, freezes during retrieval, or shows stored data with incorrect dates.

Record the exact displayed message.

**Expected outcome:** The problem is defined as capacity, search, display, date, export, or software-related.

### 3. Verify Date, Time, and Patient Selection

Confirm that the monitor date and time are correct and that the proper patient, event period, and trend range are selected. Incorrect time settings can make records appear missing.

Do not change timestamps without considering the effect on active or stored clinical records.

**Expected outcome:** The correct search period and patient context display the expected data. If records are found, troubleshooting can stop.

### 4. Review Available Storage Status

Use normal accessible menus to review memory or storage status. Determine whether the monitor is actually full or whether retrieval is failing despite available capacity.

Do not enter restricted service menus or alter protected database settings.

**Expected outcome:** Available capacity and storage condition are confirmed.

### 5. Attempt Retrieval of Another Known Record

Open another recent stored trend or event to determine whether the issue affects one record or all stored data.

**Expected outcome:** Successful retrieval of other records isolates the issue to a specific record or search period. If normal function is otherwise confirmed, document the limitation and stop troubleshooting as appropriate.

### 6. Verify Data Filters and Display Options

Check whether event type, date range, patient category, or trend-display filters are excluding the expected information. Return filters to an appropriate normal view.

**Expected outcome:** Stored records appear after correcting the filter or display selection. If so, troubleshooting can stop.

### 7. Export Required Data Before Clearing Space

When memory is full and data must be retained, export required records using an approved compatible USB device and authorized workflow before deleting anything.

Confirm that the exported file is present and readable according to facility procedure.

**Expected outcome:** Required records are preserved before storage is cleared.

### 8. Clear or Manage Stored Data Only When Authorized

Use the normal authorized workflow to remove records that are no longer required, following facility data-retention and patient-privacy policies.

Do not perform an unapproved reset or bulk deletion.

**Expected outcome:** Sufficient storage becomes available and the monitor saves and retrieves new trend data normally. If so, troubleshooting can stop after verification.

### 9. Restart and Test New Data Storage

After preserving required records, restart the monitor normally if needed. Generate a controlled test record or trend using approved test equipment, then verify that it can be saved, located, opened, and exported.

**Expected outcome:** New data is stored and retrieved normally. If successful, complete documentation and return-to-service testing.

### 10. Escalate Persistent Storage or Retrieval Failure

If records remain inaccessible, new data cannot be stored, or the system freezes during retrieval after authorized storage management, remove the monitor from service and label it **Out of Service** when the function is required by the clinical workflow.

Escalate for software, database, internal storage, or configuration evaluation.

**Expected outcome:** A monitor with unreliable clinical data storage is withheld from workflows that depend on stored trends.

## If the Problem Persists

External workflow, filter, date, and capacity causes have been ruled out. Remaining categories include corrupted records, internal storage failure, database malfunction, software corruption, or protected configuration problems.

The device should be removed from service when stored data is required for safe clinical operation, labeled Out of Service, and evaluated using manufacturer documentation and approved service tools. Data recovery or software repair should be performed only by qualified personnel.

After repair, verify data recording, retrieval, deletion controls, date and time integrity, USB export, patient privacy safeguards, and full monitoring operation before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Before clearing memory, confirm whether stored trend data must be retained or exported under facility policy.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Preserve patient data before managing storage, verify filters and timestamps before assuming records are lost, and test both saving and retrieval after correction. Escalate suspected storage corruption and document every data-handling action clearly.

That is successful troubleshooting.
