---
schemaVersion: 1
title: "Mortara ELI Series Electrocardiograph (EKG) Machine - Date, Time, Or Network Time Synchronization Error"
issueTitle: "Date, Time, Or Network Time Synchronization Error"
description: "Troubleshooting incorrect ECG timestamps caused by manual settings, time zone, daylight saving, battery, network, server, or synchronization problems."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "Mortara"
model: "ELI Series"
slug: "mortara-eli-series-date-time-or-network-time-synchronization-error"
dateAdded: "2026-07-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that ECG reports from the Mortara ELI Series machine were displaying a time one hour earlier than the hospital clocks."
  cause: "Clinical Engineering found the device was configured with an incorrect daylight-saving setting."
  resolution: "Corrected the approved regional time setting, verified displayed and transmitted timestamps with a simulator ECG, and returned the unit to service."
helpfulDetails:
  - "Displayed date and time."
  - "Approved reference time."
  - "Size and direction of the offset."
  - "Time zone and daylight-saving setting."
  - "Manual or network synchronization mode."
  - "Network connection status."
  - "Configured time source."
  - "Power-cycle retention result."
  - "Printed and transmitted timestamps."
  - "Potentially affected ECG records."
  - "Final device status."
---

## What This Guide Helps With

Troubleshooting incorrect ECG timestamps caused by manual settings, time zone, daylight saving, battery, network, server, or synchronization problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Records and Clinical Workflow

Incorrect date or time can mislabel ECG chronology, affect secure network communication, and cause records to appear under the wrong encounter period.

Notify clinical staff if recent ECGs may have incorrect timestamps. Do not change the clock during an active acquisition, save, transmission, or patient-care event.

**Expected outcome:** Potentially affected records are identified and clinical staff understand the timestamp concern.

### 2. Confirm the Exact Time Error

Determine whether the device shows:

- Incorrect minutes or hours.

- Incorrect date.

- Wrong time zone.

- A one-hour daylight-saving difference.

- Time that resets after shutdown.

- Time that drifts gradually.

- A synchronization warning.

- Correct local time but incorrect transmitted record time.

Compare the device with an approved hospital time source.

**Expected outcome:** The problem is defined as offset, drift, reset, display-only, or synchronization failure.

### 3. Document Potentially Affected ECGs

Identify the approximate period during which the clock was incorrect.

Record any ECGs that may require annotation, correction, retransmission, or review according to facility policy. Do not alter completed medical records without authorization.

**Expected outcome:** Potential patient-record impact is contained before technical correction.

### 4. Verify Time Zone and Daylight-Saving Settings

Review normal authorized settings for:

- Time zone.

- Daylight-saving behavior.

- Date format.

- 12-hour or 24-hour display.

- Regional configuration.

Compare the affected device with a working ELI Series device in the same facility.

**Expected outcome:** Regional settings match the approved site configuration.

### 5. Determine Whether Time Is Manual or Network-Synchronized

Review the normal device configuration to determine whether the clock is:

- Set manually.

- Updated by a network time source.

- Managed through a central configuration.

- Dependent on an ECG management system or server.

Do not switch synchronization modes without authorization.

**Expected outcome:** The correct time-management pathway is identified.

### 6. Verify Network Connectivity

For network-synchronized devices, confirm the EKG machine is connected to the approved wired or wireless network.

Check whether it has a valid network status and whether other network functions work.

**Expected outcome:** The device has the connectivity required to reach its approved time source.

### 7. Check the Configured Time Source

Review only authorized fields showing the network time source or central server.

Compare with a working device or approved configuration record. Do not enter an unapproved public time server or alter enterprise network values independently.

**Expected outcome:** The device points to the approved current time source.

### 8. Restart and Observe Synchronization

After confirming network access and settings, perform a normal restart.

Allow sufficient time for normal network connection and synchronization. Compare the device time again with the hospital reference.

**Expected outcome:** Date and time update to the correct values and remain stable.

### 9. Check for Time Reset After Power Removal

Record the correct device time, perform a normal shutdown, disconnect AC power when appropriate, and restart under controlled bench conditions.

Observe whether the date or time resets, loses significant time, or returns to a default value.

**Expected outcome:** The device retains time through a normal power cycle. A reset suggests a service-level clock-retention problem.

### 10. Compare Displayed and Transmitted Timestamps

Acquire a simulator ECG using approved test patient data.

Verify:

- Time shown on the device.

- Time printed on the report.

- Time saved in local records.

- Time received by the ECG management system.

**Expected outcome:** All timestamps agree with the approved hospital time source and time zone.

### 11. Correct the Clock Through Approved Methods

When authorized, correct the date, time, time zone, or synchronization configuration through normal administrative controls.

Do not use restricted service menus or alter unrelated network settings.

**Expected outcome:** The device displays and records the correct date and time.

### 12. Escalate Persistent Drift or Synchronization Failure

Remove the device from service or restrict use if:

- Time repeatedly resets.

- The clock drifts significantly.

- Network synchronization repeatedly fails.

- Printed and transmitted timestamps differ.

- The correct time cannot be retained.

- Recent patient records may be incorrectly sequenced.

**Expected outcome:** The device is prevented from creating additional inaccurately timestamped ECGs.

## If the Problem Persists

External causes involving time zone, daylight-saving settings, approved time source, network connection, and restart synchronization have been ruled out. The remaining issue may involve the internal clock, clock-retention power, device software, certificate or network access, server configuration, or a central time-service problem.

The device should be:

- Removed from service when accurate timestamps cannot be assured.

- Labeled Out of Service.

- Sent for repair or bench evaluation when the issue is device-specific.

- Evaluated using appropriate Mortara documentation and approved test equipment.

- Repaired or configured only by qualified personnel.

Coordinate with clinical applications, network, cybersecurity, and health information management when patient records may be affected.

After correction, verify displayed, printed, stored, and transmitted timestamps before return to service.

Knowing when to stop and escalate protects the integrity of the medical record.

## Clinical Use Tip

Always verify the ECG timestamp against an approved hospital time source after replacing a battery, changing configuration, or restoring network connectivity.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Accurate time is part of patient-record integrity. Verify regional settings, synchronization method, network availability, and timestamp consistency before assuming internal clock failure. Escalate repeated drift or reset conditions and clearly document any potential record impact.

That is successful troubleshooting.
