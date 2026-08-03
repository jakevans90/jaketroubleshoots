---
schemaVersion: 1
title: "Verathon BladderScan i10 Bladder Scanner - Patient Record Storage Full or Saved Scan Retrieval Failure"
issueTitle: "Patient Record Storage Full or Saved Scan Retrieval Failure"
description: "Addresses full storage, missing saved scans, filters, patient selection, permissions, date settings, synchronization, and record-management causes."
assetType: "Bladder Scanner"
manufacturer: "Verathon"
model: "BladderScan i10"
slug: "verathon-bladderscan-i10-patient-record-storage-full-or-saved-scan-retrieval-failure"
dateAdded: "2026-08-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that recent saved bladder scans could not be found in the patient record list."
  cause: "Clinical Engineering found that the record search was limited by an incorrect date filter after the device clock had been corrected."
  resolution: "Clinical Engineering updated the search range, located the records, saved and retrieved a test scan, and verified normal record access."
helpfulDetails:
  - "Exact storage or retrieval message"
  - "Patient ID and search criteria used"
  - "Date and time displayed"
  - "Logged-in access level"
  - "Storage status"
  - "Test record save result"
  - "Test record retrieval result"
  - "Local versus external record location"
  - "Transfer or queue status"
  - "Data-management action performed"
  - "Final device status"
---

## What This Guide Helps With

Addresses full storage, missing saved scans, filters, patient selection, permissions, date settings, synchronization, and record-management causes.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data Integrity

Do not delete records, clear storage, reset the device, or alter patient information until retention requirements and data-transfer status are confirmed.

Use another verified scanner if new scans cannot be safely saved or correctly associated with the patient.

**Expected outcome:** Existing patient records are protected while troubleshooting proceeds.

### 2. Confirm the Exact Record Problem

Determine whether:

- New scans cannot be saved
- A storage-full warning appears
- One patient record is missing
- All saved records are unavailable
- Records appear under the wrong date or patient
- Retrieval fails only after login
- Records are present locally but not in an external system

Record the exact message and workflow used.

**Expected outcome:** The issue is isolated to saving, local retrieval, filtering, permissions, date indexing, or external transfer.

### 3. Verify Patient and Search Criteria

Confirm the patient identifier, operator, date range, record type, and other visible filters. Clear unnecessary filters using normal user controls.

Search using a known recent test record or a record whose details are confirmed.

**Expected outcome:** The intended record appears when correct search criteria are used. If so, troubleshooting can stop after verification.

### 4. Check Date and Time

Verify that the scanner’s displayed date and time are correct. An incorrect clock may place saved scans outside the expected search range.

Do not change protected time synchronization or network settings without authorization.

**Expected outcome:** The device time is accurate or the record is located under the date when it was actually stored.

### 5. Verify User Access

Confirm that the logged-in operator has permission to view, retrieve, or manage the required records. Test using an authorized account according to facility procedure.

Do not share credentials or bypass access controls.

**Expected outcome:** Authorized users can access the expected record functions.

### 6. Review Storage Status

Use the normal information or record-management screen to check whether storage is near capacity or full. Do not assume that deleting one record is an acceptable solution.

Confirm whether records have been successfully exported, printed, archived, or transferred before any authorized deletion.

**Expected outcome:** The available storage condition is known and data retention requirements remain protected.

### 7. Verify Save Completion

Create a nonclinical test record using the approved test workflow. Confirm that the device indicates a successful save and that the record can immediately be retrieved.

Do not create test data under a real patient.

**Expected outcome:** New records save and retrieve normally. If the test record works, the issue may be limited to earlier records, filters, or patient identifiers.

### 8. Check External Data Transfer Status

If records are expected to transfer to another system, verify that the network, interface, destination, and queue are available. Confirm whether the record remains on the device, is pending, or transferred successfully.

Do not delete local records merely because the external system has not displayed them.

**Expected outcome:** The local and external record locations are understood, and transfer failure is distinguished from local storage failure.

### 9. Restart and Recheck Records

Exit the patient workflow and restart the scanner normally. Log in with an authorized account and repeat the record search.

Do not perform factory resets, database repair, or storage formatting.

**Expected outcome:** Saved records and storage functions return after restart. If retrieval remains unreliable, remove the device from service.

### 10. Follow Authorized Data-Management Procedures

If storage is confirmed full, follow the facility-approved and manufacturer-supported process for exporting, archiving, or deleting eligible records.

Verify successful transfer and required retention before removing any data. Maintain an audit trail when required.

**Expected outcome:** Space is restored without losing required clinical records, and new records save normally.

### 11. Perform Final Functional Verification

Confirm that the scanner can:

- Save a test scan
- Retrieve the same scan
- Search by approved criteria
- Display correct patient information
- Preserve date and time
- Transfer or print the record when required
- Report available storage normally

**Expected outcome:** Record storage and retrieval are accurate, repeatable, and compliant. The device may return to service.

## If the Problem Persists

External causes involving filters, patient identifiers, date and time, user permissions, storage status, record workflow, and external transfer have been ruled out.

The remaining cause may involve storage corruption, database software, internal memory, access configuration, interface synchronization, or another service-level condition. Do not format storage, reset the database, or remove clinical data without approved backup and authorization.

The device should be:

- Removed from service when records cannot be reliably saved or retrieved
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Verathon documentation and approved test equipment
- Repaired or configured only by qualified personnel

After service, verify record creation, retrieval, patient association, export, storage capacity reporting, and data integrity before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Confirm that a scan is saved under the correct patient before ending the examination or clearing the screen.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Patient records must be protected throughout troubleshooting. Verify search criteria, time, permissions, storage status, and transfer paths before assuming memory failure. Avoid destructive actions, escalate unresolved data problems, and document the consistent CCR and final data-integrity checks.

That is successful troubleshooting.

