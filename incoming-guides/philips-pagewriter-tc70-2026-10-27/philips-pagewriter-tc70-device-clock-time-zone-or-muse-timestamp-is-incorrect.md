---
schemaVersion: 1
title: "Philips PageWriter TC70 Electrocardiograph (EKG) Machine - Device Clock, Time Zone, or MUSE Timestamp Is Incorrect"
issueTitle: "Device Clock, Time Zone, or MUSE Timestamp Is Incorrect"
description: "Troubleshoots incorrect ECG timestamps caused by device clock settings, time-zone configuration, synchronization, network conditions, or MUSE integration."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "Philips"
model: "PageWriter TC70"
slug: "philips-pagewriter-tc70-device-clock-time-zone-or-muse-timestamp-is-incorrect"
dateAdded: "2026-10-27"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that ECGs transmitted from the PageWriter TC70 appeared in MUSE with the wrong acquisition time."
  cause: "Clinical Engineering found the PageWriter TC70 was configured with an incorrect time-zone setting while its displayed local clock appeared correct."
  resolution: "Clinical Engineering corrected the authorized time-zone configuration and verified a test ECG displayed the correct acquisition timestamp on both the PageWriter TC70 and MUSE."
helpfulDetails:
  - "Displayed device date and time"
  - "Configured time zone"
  - "Reliable time source used for comparison"
  - "Whether the error persists after restart"
  - "Difference between device and MUSE timestamps"
  - "Network connection status"
  - "Whether other PageWriter units are affected"
  - "Configuration changes observed"
  - "Test ECG acquisition time"
  - "MUSE receipt/display time"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots incorrect ECG timestamps caused by device clock settings, time-zone configuration, synchronization, network conditions, or MUSE integration.

## Step-by-Step Troubleshooting

### 1. Protect Patient Records and Clinical Workflow

An incorrect timestamp can affect record chronology and ECG identification. If the time discrepancy could create uncertainty about when an ECG was acquired, notify the appropriate clinical area and avoid relying on the incorrect timestamp for time-critical decisions.

Use another verified system when necessary until the timing issue is understood.

**Expected outcome:** Staff are aware of any timestamp reliability concern and patient records are protected from avoidable misidentification.

### 2. Confirm Where the Time Is Incorrect

Determine whether the incorrect time appears:

- On the PageWriter TC70 itself
- On a newly acquired ECG
- Only after transfer to MUSE
- In exported or archived ECG records
- After every restart
- Only around a time-zone or daylight-saving change

Compare a current test acquisition against a reliable institutional time source.

**Expected outcome:** The problem is localized to the PageWriter display, ECG record, transmitted MUSE record, or multiple locations. This determines whether troubleshooting should focus on the device or integration path.

### 3. Verify the Device Date, Time, and Time Zone

Review the normal authorized date, time, and time-zone configuration on the PageWriter TC70.

Confirm all three are appropriate for the facility. A clock can show the apparently correct local time while having the wrong time-zone configuration, causing transferred timestamps to differ.

Do not change unrelated configuration settings.

**Expected outcome:** Date, local time, and time zone agree with the institutional standard. If correcting an authorized setting resolves both local and transmitted timestamps, proceed to final verification.

### 4. Check Whether the Error Returns After Restart

After documenting current settings, perform a normal restart when clinically appropriate.

Recheck the displayed time and time zone after startup.

**Expected outcome:** Correct clock information remains retained after restart. If the settings immediately revert or drift significantly, remove the device from routine use as appropriate and escalate for service-level evaluation.

### 5. Determine Whether Network Synchronization Is Expected

Confirm from local configuration records or approved documentation whether the PageWriter TC70 receives time through a network or institutional synchronization source.

If synchronization is expected, verify that normal network connectivity is present before changing device settings repeatedly.

**Expected outcome:** The device either has the required network connection for synchronization or is correctly operating under its intended local time configuration.

### 6. Verify Network Connectivity When Relevant

If the device normally communicates with MUSE or hospital infrastructure, verify the external network path:

- Network cable or approved wireless connection, as applicable
- Link status
- Expected network connection
- Ability to perform normal permitted communication functions

Do not change VLANs, IP configuration, DNS, domain settings, or infrastructure parameters unless authorized and within your support responsibility.

**Expected outcome:** The PageWriter has its normal network connectivity. If connectivity restoration corrects time synchronization, repeat timestamp testing and stop troubleshooting when stable.

### 7. Compare Local and MUSE Timestamps

Acquire a non-patient test ECG using the correct device clock and note the acquisition time.

Transfer it through the normal workflow and compare:

- Time displayed on PageWriter
- Acquisition time stored with the ECG
- Time displayed in MUSE

This helps identify whether the discrepancy occurs before or after transmission.

**Expected outcome:** All systems show a consistent acquisition time. If PageWriter is correct but MUSE shows a different timestamp, preserve the test details and escalate the integration/server side rather than repeatedly changing the ECG machine.

### 8. Compare With Another PageWriter TC70

If another correctly functioning PageWriter TC70 uses the same network and MUSE environment, compare its date, time-zone configuration, and timestamp behavior without copying settings blindly.

A facility-wide discrepancy suggests an infrastructure or integration issue rather than failure of one ECG machine.

**Expected outcome:** The comparison indicates whether the problem is isolated to one device or shared across the environment.

### 9. Verify Authorized Configuration

If the PageWriter is the only affected unit, compare its authorized configuration with the facility standard or approved configuration record.

Correct only settings you are authorized to change.

Do not use undocumented service menus or make unrelated configuration changes.

**Expected outcome:** The PageWriter configuration matches the approved institutional configuration. If the correction restores proper timestamps, proceed to final verification.

### 10. Perform Final Timestamp Verification

After correction:

1. Confirm the device date, time, and time zone.
2. Restart the device if appropriate.
3. Confirm the settings remain correct.
4. Acquire a test ECG.
5. Transfer it through the normal MUSE workflow.
6. Verify the displayed and archived timestamps agree with the institutional time source.

**Expected outcome:** Device and MUSE timestamps are consistent and remain correct after restart. Troubleshooting can stop and the device may be returned to service according to department policy.

### 11. Escalate Persistent Timestamp Errors

If the PageWriter clock is correct but MUSE timestamps remain incorrect, or if the device cannot retain correct clock information, stop routine external troubleshooting.

Coordinate with the appropriate Clinical Engineering, IT, integration, or Philips support resource based on where the discrepancy occurs.

**Expected outcome:** The affected system is appropriately escalated without making unsupported configuration changes.

## If the Problem Persists

Common external and authorized configuration causes have been ruled out. Remaining categories may include device time-retention problems, network time synchronization, MUSE/integration configuration, server-side time-zone handling, or another service-level issue.

The affected PageWriter TC70 should be:

- Removed from service when timestamp accuracy cannot be assured for the intended workflow.
- Labeled **Out of Service** when removed.
- Sent for repair or bench evaluation when the problem is device-specific.
- Evaluated using appropriate Philips documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

If the PageWriter time is correct and the discrepancy occurs only after transfer, escalation may instead involve the MUSE or IT/integration environment. Complete end-to-end timestamp verification before return to service.

Knowing when to stop altering the device and escalate the correct part of the system is proper troubleshooting.

## Clinical Use Tip

When troubleshooting timestamp discrepancies, compare the acquisition time at the PageWriter and the received time in MUSE so a downstream integration problem is not mistaken for an ECG-machine fault.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- rendered from front matter -->

## Final Thought

Timestamp troubleshooting requires verification across the complete ECG workflow. Confirm the device clock, time zone, synchronization path, network status, and MUSE result before assuming internal failure. Escalate the correct system and document the comparison clearly.

That is successful troubleshooting.
