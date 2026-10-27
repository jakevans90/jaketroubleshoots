---
schemaVersion: 1
title: "Philips PageWriter TC70 Electrocardiograph (EKG) Machine - Archive Database Is Available but an ECG Cannot Be Reopened for Review"
issueTitle: "Archive Database Is Available but an ECG Cannot Be Reopened for Review"
description: "Troubleshoots inaccessible archived ECGs when the archive remains available, including record selection, storage, database access, connectivity, and record-specific problems."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "Philips"
model: "PageWriter TC70"
slug: "philips-pagewriter-tc70-archive-database-is-available-but-an-ecg-cannot-be-reopened-for-review"
dateAdded: "2026-10-27"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that an archived ECG appeared in the PageWriter TC70 database but could not be reopened for review."
  cause: "Clinical Engineering found the PageWriter had lost its normal network connection to the configured archive resource while local archive navigation remained available."
  resolution: "Clinical Engineering restored the external network connection, verified the affected ECG and additional archived ECGs opened normally, and confirmed new ECG acquisition and archive access before returning the device to service."
helpfulDetails:
  - "Patient or record identifiers used to locate the ECG"
  - "Acquisition date and time"
  - "Whether one or multiple records were affected"
  - "Whether other archived ECGs opened normally"
  - "Device stability during archive access"
  - "Local storage/archive status"
  - "Whether the ECG was available in MUSE"
  - "Network connection status"
  - "Results from another workstation or PageWriter"
  - "Actions taken without altering stored records"
  - "Final archive and acquisition verification"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots inaccessible archived ECGs when the archive remains available, including record selection, storage, database access, connectivity, and record-specific problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Records and Clinical Workflow

Do not delete, overwrite, reinitialize, or otherwise alter stored ECG data while investigating an archive-access complaint.

If the ECG is clinically needed and cannot be retrieved from this device, use the approved clinical record system, MUSE, or another authorized source when available.

**Expected outcome:** Existing ECG records are protected while clinical access to necessary information is maintained through an appropriate alternative.

### 2. Confirm the Exact Archive Problem

Determine whether:

- One ECG cannot be reopened
- Multiple ECGs are affected
- All archived ECGs are inaccessible
- The record appears in the archive but fails when selected
- The record opens but waveform or demographic data are incomplete
- The problem occurs only with transmitted or older records

Do not assume the database is corrupt because a single record cannot be reviewed.

**Expected outcome:** The problem is characterized as record-specific, range-specific, or archive-wide.

### 3. Confirm Normal PageWriter Operation

Verify the PageWriter TC70 starts normally, responds to controls, and allows access to other standard functions.

If the device is freezing, restarting, or displaying broader storage-related symptoms, stop treating the condition as an isolated ECG-review problem.

**Expected outcome:** The device remains stable while archive functions are tested. If the whole system is unstable, remove it from service and escalate.

### 4. Verify the Correct Patient and ECG Record

Confirm the intended record using available identifiers such as:

- Patient name
- Patient identifier
- Acquisition date and time
- ECG type or encounter information

Be cautious with patients who have multiple ECGs or similar demographic information.

**Expected outcome:** The correct ECG record has been positively identified. If the originally selected record was incorrect and the intended ECG opens normally, troubleshooting can stop.

### 5. Test Other Archived ECG Records

Attempt to open several other appropriate archived ECGs from different acquisition times.

Do not alter or delete records during testing.

**Expected outcome:** Other records either open normally, indicating a record-specific issue, or exhibit the same problem, suggesting a broader archive/database issue.

### 6. Restart the PageWriter Normally

When patient care permits, perform a normal shutdown and restart.

Return to the archive and attempt to reopen the same record.

Do not interrupt power during startup or storage activity.

**Expected outcome:** Archive access remains available and the ECG opens normally after restart. If the issue is resolved and repeated access succeeds, troubleshooting can stop after verification.

### 7. Check Available Storage or Archive Status

Review the normal user-accessible storage or archive status for indications that capacity is limited or that records have been archived, transferred, or otherwise managed by the configured workflow.

Do not delete clinical data merely to test whether storage capacity is involved.

**Expected outcome:** The archive is accessible and storage status does not indicate an obvious condition requiring approved records-management action.

### 8. Determine Whether the ECG Exists Elsewhere

If the device normally transfers ECGs to MUSE or another institutional repository, verify whether the affected ECG can be found and opened there.

This determines whether the problem affects the original ECG data or only local reopening on the PageWriter.

**Expected outcome:** The ECG is either confirmed intact in the central system or identified as unavailable across the workflow. If it is available centrally, protect that record and focus troubleshooting on local archive access.

### 9. Verify Network Connectivity When Archive Access Depends on It

If the archive or record-review workflow depends on MUSE or another network resource, verify the external network connection and normal communication status.

Do not change network infrastructure settings without authorization.

**Expected outcome:** The PageWriter has the connectivity required for its configured archive workflow. If restoring connectivity restores record access, verify several records and stop troubleshooting.

### 10. Compare With Another Known-Good Device or Workstation

When appropriate, attempt to access the same centrally stored ECG from another authorized system.

Also determine whether another PageWriter TC70 can access equivalent archive functions.

**Expected outcome:** The comparison helps identify whether the problem follows one record, one PageWriter, or the shared archive environment.

### 11. Avoid Destructive Database Actions

Do not:

- Delete the affected ECG
- Clear the archive
- Reinitialize storage
- Restore or replace databases
- Perform undocumented database repair
- Modify restricted service settings

unless these actions are specifically authorized under an approved service procedure and data-retention requirements have been addressed.

**Expected outcome:** Patient records remain preserved while the fault is escalated appropriately.

### 12. Perform Final Functional Verification

If the problem is corrected:

1. Confirm the affected ECG can be opened.
2. Review another archived ECG.
3. Exit and reopen the archive.
4. Confirm normal new ECG acquisition.
5. Verify normal transmission or storage workflow when applicable.
6. Confirm no patient data were lost or incorrectly associated during troubleshooting.

**Expected outcome:** Archived records can be reliably opened and normal ECG acquisition and storage remain functional. Troubleshooting can stop and the device may be returned to service according to department policy.

### 13. Escalate Unresolved Archive Access Problems

If one or more ECGs remain inaccessible after record identification, restart, storage review, network verification, and central-system comparison, stop external troubleshooting.

Preserve the device and record state for further evaluation.

**Expected outcome:** The problem is escalated without risking additional patient data.

## If the Problem Persists

Common external and workflow causes have been ruled out. Remaining possibilities may include a record-specific database problem, local storage issue, database indexing problem, application/software issue, communication problem, or MUSE/infrastructure condition.

The PageWriter TC70 should be:

- Removed from service when reliable record storage or retrieval cannot be assured.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation when the issue is device-specific.
- Evaluated using appropriate Philips documentation and approved test equipment.
- Repaired, restored, or configured only by qualified personnel.

Any database or storage repair must preserve applicable patient-data and institutional record-retention requirements. Verify ECG acquisition, storage, reopening, and any required transmission functions before return to service.

Knowing when to stop before performing potentially destructive data actions is proper troubleshooting.

## Clinical Use Tip

Never delete or rebuild ECG storage as an exploratory troubleshooting step when patient records may still reside on the device; preserve the data and escalate.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- rendered from front matter -->

## Final Thought

Archived ECG problems require careful protection of patient data. Verify the record, device stability, storage status, network path, and central archive before assuming database failure. Avoid destructive actions, escalate appropriately, and document what was tested and preserved.

That is successful troubleshooting.
