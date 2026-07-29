---
schemaVersion: 1
title: "GE Healthcare MAC 5500 HD Electrocardiograph (EKG) Machine - MUSE Transmission Queue Stuck Or Records Not Reaching MUSE"
issueTitle: "MUSE Transmission Queue Stuck Or Records Not Reaching MUSE"
description: "Troubleshooting ECGs stuck in the transmission queue due to network, destination, record-status, interface, authentication, or MUSE availability problems."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "GE Healthcare"
model: "MAC 5500 HD"
slug: "ge-healthcare-mac-5500-hd-muse-transmission-queue-stuck-or-records-not-reaching-muse"
dateAdded: "2026-07-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that completed ECGs remained in the MAC 5500 HD transmission queue and were not visible in MUSE."
  cause: "Clinical Engineering found that the network cable at the wall jack was loose and the device had no stable network connection."
  resolution: "Clinical Engineering reseated the network cable, retransmitted the pending records, confirmed receipt in MUSE, and verified a successful test transmission."
helpfulDetails:
  - "Patient identifier and acquisition time"
  - "Queue status"
  - "Number of pending records"
  - "Wired or wireless connection"
  - "Network indicator status"
  - "Other devices affected"
  - "Transmission retry result"
  - "MUSE receipt confirmation"
  - "Duplicate-record check"
  - "Final device status"
---

## What This Guide Helps With

Troubleshooting ECGs stuck in the transmission queue due to network, destination, record-status, interface, authentication, or MUSE availability problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and ECG Records

Do not delete, repeat, or manually re-create an ECG until the original study location and transmission status are confirmed.

Notify clinical staff that MUSE delivery is delayed.

Preserve all locally stored ECGs.

Provide an approved alternate process for urgent ECG interpretation.

Confirm critical ECG findings are communicated through the facility’s downtime process.

**Expected outcome:** Patient care continues and original ECG records remain protected during the outage.

### 2. Confirm the Exact Transmission Condition

Determine whether:

- Records remain pending.

- Records show failed or unsuccessful status.

- The queue appears empty but MUSE has no record.

- Only one ECG is affected.

- All transmissions from the device are affected.

- Multiple electrocardiographs are experiencing the same issue.

- Record the patient identifier, acquisition time, and visible transmission status.

**Expected outcome:** The problem is defined as a local queue failure, missing receipt, individual-record issue, or system-wide outage.

### 3. Confirm the ECG Is Complete and Eligible for Transmission

Open the record using the normal workflow.

Verify:

- Required patient information is present.

- The record is saved and finalized as required.

- No prompt or incomplete-field condition is preventing transmission.

- The record can be viewed locally.

**Expected outcome:** The ECG is complete, readable, and eligible for transmission.

### 4. Check Basic Network Status

Inspect the device network connection.

For wired connections:

- Confirm the network cable is fully seated.

- Check for damaged connectors or cable strain.

- Verify link indicators when visible.

- Test the approved wall jack or cable with a known-good comparison when permitted.

For wireless connections:

- Confirm the expected wireless status is shown.

- Verify the unit is in an area with known coverage.

- Compare with another functioning device in the same location.

**Expected outcome:** The MAC 5500 HD has a stable connection to the intended network.

### 5. Compare With Another MAC System

Determine whether another MAC electrocardiograph can transmit from the same department.

Use an approved test record when needed.

Note whether the problem follows the location, network connection, or individual device.

Avoid sending duplicate real-patient studies solely for testing.

**Expected outcome:** A device-specific or infrastructure-wide problem is identified.

### 6. Retry Transmission Through the Normal Workflow

With the network stable:

- Select the pending record.

- Initiate the approved transmit or resend action.

- Observe the queue status.

- Do not repeatedly resend the same record without checking MUSE, because duplicates may result.

**Expected outcome:** The record leaves the pending queue and is confirmed in MUSE. If receipt is verified, troubleshooting can stop.

### 7. Confirm Actual Receipt in MUSE

Coordinate with an authorized MUSE user or support team.

Verify:

- Correct patient identity

- Acquisition date and time

- Device or location

- Study visibility and status

- Whether duplicate records were created

**Expected outcome:** The transmitted ECG is present in MUSE and correctly associated with the patient.

### 8. Restart the Electrocardiograph

If no records are actively transmitting:

- Preserve and document the pending queue.

- Shut down normally.

- Restart the device.

- Confirm network reconnection.

- Retry one pending record.

- Verify MUSE receipt before sending additional records.

**Expected outcome:** Queue processing resumes after restart without record loss or duplication.

### 9. Check Date, Time, and Destination Context

Verify that the device date, time, and configured clinical location appear correct.

Do not alter MUSE destination, network profile, security settings, or system configuration without authorization.

Incorrect time or location information can make a transmitted record difficult to locate even when transmission succeeded.

**Expected outcome:** The record is searched using the correct patient, time, and device information, and no simple identification mismatch remains.

### 10. Escalate a Broader Interface or Server Issue

When multiple devices cannot transmit:

- Contact MUSE, interface-engine, network, or server support.

- Provide affected device names, locations, times, and queue status.

- Preserve local records until support confirms safe transmission.

- Follow the facility downtime process.

**Expected outcome:** The responsible infrastructure team receives enough information to investigate without losing patient records.

### 11. Perform Final End-to-End Verification

After correction:

- Acquire an approved test ECG.

- Save and transmit it once.

- Confirm it leaves the local queue.

- Confirm the exact test record appears in MUSE.

- Verify previously pending patient records have also arrived.

- Check for duplicates.

**Expected outcome:** The complete MAC-to-MUSE path operates normally. The unit may be returned to service.

## If the Problem Persists

External network, workflow, patient-data, queue, and MUSE-search causes have been ruled out. The remaining possibilities may include device communication software failure, corrupted queue data, invalid configuration, interface-engine failure, MUSE service outage, network security changes, or internal communication hardware problems.

The device should be:

- Removed from service if reliable ECG delivery cannot be assured

- Labeled Out of Service

- Sent for repair or bench evaluation when the problem is device-specific

- Evaluated using appropriate GE Healthcare documentation and approved test equipment

- Repaired or configured only by qualified personnel

- Preserve all locally stored ECGs and coordinate with MUSE and IT support before making configuration changes. Return the unit to service only after end-to-end transmission and receipt are verified.

- Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

During a MUSE outage, ensure urgent ECGs receive timely clinical review through the approved downtime process rather than waiting for electronic transmission.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the original ECG, verify the local queue and network first, confirm actual receipt rather than assuming success, and involve MUSE or IT support promptly when the problem extends beyond one device.

That is successful troubleshooting.
