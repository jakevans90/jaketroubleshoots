---
schemaVersion: 1
title: "Masimo Rad-97 Pulse Oximeter - Trend Memory Full Or Stored Data Retrieval Failure"
issueTitle: "Trend Memory Full Or Stored Data Retrieval Failure"
description: "Trend storage or retrieval problems caused by full memory, filters, patient selection, date settings, software state, export issues, or internal storage faults."
assetType: "Pulse Oximeter"
manufacturer: "Masimo"
model: "Rad-97"
slug: "masimo-rad-97-trend-memory-full-or-stored-data-retrieval-failure"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that recent Rad-97 trend data could not be found and the device indicated that storage was full."
  cause: "Clinical Engineering found that older retained records had filled available trend storage and confirmed the expected recent record was listed under an incorrect date range."
  resolution: "Preserved required records, completed an authorized memory-clearing process, corrected the date range selection, verified new trend storage and retrieval, and returned the device to service."
helpfulDetails:
  - "Exact storage or retrieval message"
  - "Expected patient and date range"
  - "Device date and time"
  - "Memory or storage status"
  - "Filters selected"
  - "New test record results"
  - "Export device or system tested"
  - "Data-preservation approval"
  - "Results after restart"
  - "Final save, retrieve, and export verification"
---

## What This Guide Helps With

Trend storage or retrieval problems caused by full memory, filters, patient selection, date settings, software state, export issues, or internal storage faults.

## Step-by-Step Troubleshooting

### 1. Protect Active Patient Monitoring

Do not interrupt current monitoring solely to investigate stored data. Confirm that current values and alarms remain functional.

Use another verified monitor if the Rad-97 is freezing, restarting, or otherwise affecting active care.

Expected outcome: Current patient monitoring remains uninterrupted.

### 2. Confirm the Exact Data Problem

Determine whether the device reports full memory, cannot save new trends, cannot display stored records, shows missing time periods, or fails only during export.

Record the displayed message and the data range clinical staff expected to retrieve.

Expected outcome: The storage or retrieval failure is clearly defined.

### 3. Verify Correct Patient and Date Selection

Check that the correct patient record, date range, trend type, and display filter are selected.

Review the device date and time for obvious errors that could place records under an unexpected timestamp.

Expected outcome: The expected data becomes visible after correcting selection or time-range filters. If so, troubleshooting can stop.

### 4. Check Current Storage Status

Review available storage indicators using normal operator-accessible menus.

Do not delete records without authorization and facility policy. Confirm whether required data has already been transferred or retained elsewhere before any approved clearing action.

Expected outcome: The storage condition is identified without losing required clinical information.

### 5. Confirm the Device Is Saving New Data

Create a controlled test record using approved methods and verify whether new trend data appears with the correct timestamp.

Expected outcome: New data is saved and retrieved normally, indicating the issue may be limited to older records or filtering.

### 6. Restart the Device Safely

Transfer active monitoring to another device and perform a normal shutdown and restart.

Recheck stored data and available memory after startup.

Expected outcome: Data retrieval resumes and the device remains stable. If successful, continue to final verification.

### 7. Check Export Media or Connected Systems

If retrieval fails only during export, inspect the approved USB device, cable, external system, or communication path.

Test with a known-good compatible export device according to facility policy.

Expected outcome: Stored data exports successfully or the problem is isolated to external media or communication.

### 8. Compare With an Approved Rad-97

Compare normal data menu behavior, filters, profile, time settings, and storage workflow with another approved Rad-97.

Do not copy or change protected settings without authorization.

Expected outcome: A configuration or workflow difference is identified and corrected through approved methods.

### 9. Preserve Required Data Before Clearing Memory

If memory is confirmed full, coordinate with clinical leadership, health information management, or the responsible system owner before deleting or clearing data.

Follow approved facility and manufacturer procedures only.

Expected outcome: Required data is retained and storage is restored without unauthorized deletion.

### 10. Verify Storage and Retrieval

Create, save, retrieve, and, when required, export a new controlled test record.

Confirm correct date, time, patient association, and trend display.

Expected outcome: Trend storage and retrieval operate normally.

### 11. Escalate Persistent Storage Failure

If the Rad-97 cannot reliably save or retrieve data after approved memory, filter, time, restart, and export checks, remove it from workflows that require trend storage.

Expected outcome: The device is routed for qualified service evaluation.

## If the Problem Persists

External and workflow causes such as record selection, date range, filters, full memory, connected media, and receiving-system availability have been ruled out.

The remaining cause may involve internal storage, database corruption, software, configuration, or another service-level condition. Remove the device from service when stored data is clinically or operationally required, label it Out of Service, and send it for bench evaluation.

Use current manufacturer documentation and approved tools. Protect retained patient data, follow privacy requirements, and complete data-storage and monitoring verification before return to service.

## Clinical Use Tip

Never clear trend memory until required patient information has been preserved and the deletion is authorized under facility policy.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect current monitoring and stored patient information, verify selection and storage conditions before assuming memory failure, escalate persistent data problems, and document all preservation and verification steps.

That is successful troubleshooting.
