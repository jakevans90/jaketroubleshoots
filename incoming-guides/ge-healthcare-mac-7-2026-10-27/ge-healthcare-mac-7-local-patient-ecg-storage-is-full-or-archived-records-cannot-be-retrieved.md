---
schemaVersion: 1
title: "GE Healthcare MAC 7 Electrocardiograph (EKG) Machine - Local Patient/ECG Storage Is Full or Archived Records Cannot Be Retrieved"
issueTitle: "Local Patient/ECG Storage Is Full or Archived Records Cannot Be Retrieved"
description: "Troubleshoot full local ECG storage or inaccessible archived records, including retained studies, search criteria, workflow, connectivity, configuration, and storage-management causes."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "GE Healthcare"
model: "MAC 7"
slug: "ge-healthcare-mac-7-local-patient-ecg-storage-is-full-or-archived-records-cannot-be-retrieved"
dateAdded: "2026-10-27"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the MAC 7 displayed a local storage-full condition and would not reliably save additional ECGs."
  cause: "Clinical Engineering found numerous previously transmitted ECGs remaining in local storage while network communication and MUSE transmission were operating normally."
  resolution: "Verified transmission status, followed the approved record-management process to clear eligible local records, and confirmed successful storage and retrieval of a test ECG."
helpfulDetails:
  - "Exact storage or archive message."
  - "Approximate local storage condition shown by the device."
  - "Whether new ECGs could be saved."
  - "Whether affected records were local or remotely archived."
  - "Patient/search criteria used."
  - "Transmission status."
  - "MUSE connectivity."
  - "Network connection tested."
  - "Configuration observations."
  - "Records affected before and after correction."
  - "Controlled test results."
  - "Final device status."
---

## What This Guide Helps With

Troubleshoot full local ECG storage or inaccessible archived records, including retained studies, search criteria, workflow, connectivity, configuration, and storage-management causes.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Existing Records

Do not delete patient ECGs solely to clear a storage warning unless retention and transmission status have been verified according to facility policy.

If the MAC 7 cannot reliably save a newly acquired ECG, move clinical testing to another verified device or approved workflow.

**Expected outcome:** Patient care continues without risking loss or inappropriate deletion of ECG records.

### 2. Confirm the Exact Storage or Retrieval Problem

Determine whether:

- The device reports that local storage is full.
- New ECGs cannot be stored.
- Previously stored ECGs are missing from the expected list.
- A specific archived record cannot be found.
- All archived records are unavailable.
- Records appear locally but cannot be transmitted or retrieved elsewhere.

Record any displayed storage or archive message exactly.

**Expected outcome:** The issue is classified as storage capacity, local retrieval, search/filtering, transmission, or broader data-management failure.

### 3. Verify Search and Record Selection

For an archived-record complaint, confirm the search is being performed using the correct patient and study information.

Check for:

- Incorrect patient identifier.
- Incorrect date or time range.
- Wrong patient selected.
- Active filters that exclude the desired ECG.
- Confusion between locally stored and remotely archived records.

Do not modify patient demographics merely to locate a record.

**Expected outcome:** The correct record-selection criteria are being used. If the ECG becomes available after correcting the search or filter, verify the record and stop troubleshooting.

### 4. Determine Whether Records Are Local or Already Transmitted

Verify whether affected ECGs are expected to reside on the MAC 7, in MUSE, or in another approved archive.

Where permitted, confirm successful transmission status before performing any storage-management action.

A full local store can be a workflow problem if completed ECGs are not being transferred or cleared through the approved process.

**Expected outcome:** The expected storage location and transmission status of the records are known.

### 5. Verify Network Connectivity

If records should be transmitted to or retrieved through MUSE, verify the external network path.

Inspect:

- Ethernet cable and connectors when wired.
- Network connection indicators.
- Approved wireless connectivity when applicable.
- Whether other MUSE functions work normally.

Use a known-good approved cable or connection when practical.

**Expected outcome:** Network connectivity is stable. If restoring connectivity allows queued records to transfer or archived records to become available, verify the workflow and stop troubleshooting.

### 6. Review Local Storage Through the Normal User Workflow

Using normal authorized controls, review the local patient/ECG record list and determine whether a large number of completed studies remain stored.

Do not indiscriminately delete clinical records.

Follow institutional retention and data-management requirements before removing any ECG from local storage.

**Expected outcome:** Clinical Engineering determines whether legitimate stored data is consuming available local capacity without altering required records.

### 7. Verify Authorized Storage and Archive Configuration

Compare relevant storage, archive, and communication settings with facility standards or a known-good MAC 7.

Do not change retention rules, destinations, or record-management configuration without authorization.

**Expected outcome:** The device is configured for the intended storage and archival workflow. If an authorized configuration correction restores normal operation, verify storage and retrieval before stopping.

### 8. Perform a Controlled Storage and Retrieval Test

Using an approved test workflow, verify that the MAC 7 can:

1. Acquire an ECG using an ECG simulator when appropriate.
2. Store the test ECG.
3. Locate the stored ECG.
4. Transmit or archive the test ECG if required.
5. Retrieve or confirm the record through the intended workflow.

Avoid creating unnecessary clinical records in production systems.

**Expected outcome:** New records can be stored, located, and processed normally. If successful and storage capacity is no longer impaired, troubleshooting can stop.

### 9. Escalate Persistent Storage or Archive Failures

If available capacity remains abnormal, records cannot be accessed reliably, or the MAC 7 cannot safely store new ECGs, remove the device from clinical service.

Do not perform unsupported file-system manipulation, internal storage replacement, or undocumented data deletion.

**Expected outcome:** Potential patient-data loss or inability to save new ECGs is prevented while the problem is escalated.

## If the Problem Persists

If record selection, expected storage location, local record status, network connectivity, and authorized configuration have been checked, common external causes have been ruled out.

Possible remaining categories include local storage corruption, application or database problems, MUSE/archive communication, infrastructure issues, or a service-level storage failure.

The MAC 7 should be:

- Removed from service if new patient ECGs cannot be reliably stored or retrieved.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Protect existing patient data during service. Do not erase, initialize, or replace storage without following approved data-retention and service procedures.

Before return to service, verify ECG acquisition, local storage, record retrieval, transmission, and archive workflow.

Knowing when to stop external troubleshooting and protect stored clinical data is proper troubleshooting.

## Clinical Use Tip

Confirm a patient ECG is safely stored or transmitted before removing records or performing any action that could affect local data.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- rendered from front matter -->

## Final Thought

Protect patient records first, verify search criteria, data location, transmission, and external connectivity before assuming storage hardware has failed, and document any record-management action carefully.

That is successful troubleshooting.
