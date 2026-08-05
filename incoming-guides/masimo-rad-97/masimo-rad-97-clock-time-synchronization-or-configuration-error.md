---
schemaVersion: 1
title: "Masimo Rad-97 Pulse Oximeter - Clock, Time Synchronization, Or Configuration Error"
issueTitle: "Clock, Time Synchronization, Or Configuration Error"
description: "Incorrect time or configuration caused by manual settings, profile mismatch, lost synchronization, network problems, power loss, or service-level configuration faults."
assetType: "Pulse Oximeter"
manufacturer: "Masimo"
model: "Rad-97"
slug: "masimo-rad-97-clock-time-synchronization-or-configuration-error"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Rad-97 clock was incorrect and trend records appeared under the wrong time."
  cause: "Clinical Engineering found that the device was assigned an incorrect time zone after being transferred from another department."
  resolution: "Applied the authorized facility time-zone configuration, synchronized the clock, verified time retention and trend timestamps after restart, and returned the device to service."
helpfulDetails:
  - "Displayed date and time"
  - "Facility reference time"
  - "Time zone and daylight-saving status"
  - "Active profile"
  - "Network connection status"
  - "Recent power or battery event"
  - "Whether settings survived restart"
  - "Trend and export timestamps"
  - "Receiving-system time"
  - "Final configuration and device status"
---

## What This Guide Helps With

Incorrect time or configuration caused by manual settings, profile mismatch, lost synchronization, network problems, power loss, or service-level configuration faults.

## Step-by-Step Troubleshooting

### 1. Assess the Clinical Impact

Confirm whether incorrect time affects trend review, patient association, network communication, alarm records, or exported data.

Do not rely on incorrectly timestamped records for clinical decisions without independent verification.

Expected outcome: The effect on patient care and data integrity is understood.

### 2. Confirm the Exact Error

Record the displayed date, time, time zone, configuration message, and whether the error returns after restart.

Compare the Rad-97 with an approved facility time source.

Expected outcome: The amount and type of time or configuration error are documented.

### 3. Verify the Active Profile

Confirm that the device is using the approved clinical profile for its department and patient population.

Compare it with another authorized Rad-97. Do not alter protected alarm or network settings without approval.

Expected outcome: The correct profile is active or an approved profile mismatch is identified.

### 4. Check Time Zone and Daylight-Saving Settings

Verify that the configured time zone and daylight-saving behavior match facility policy.

Avoid making manual corrections when the device is expected to synchronize automatically unless authorized.

Expected outcome: Basic time settings match the facility standard.

### 5. Verify Network Connection

If automatic time synchronization is expected, check that the Rad-97 is connected to the approved network and communicating normally.

Compare with another device in the same location.

Expected outcome: Network connectivity is available for synchronization.

### 6. Perform an Approved Time Synchronization

Use the normal authorized synchronization or configuration method supported by the facility.

Do not access undocumented service menus or change network security settings.

Expected outcome: The Rad-97 displays the correct date and time.

### 7. Restart and Check Time Retention

After correcting the time through approved methods, perform a normal restart and verify that the date, time, and profile remain correct.

Expected outcome: Settings are retained after restart. If so, troubleshooting can stop after functional verification.

### 8. Check AC and Battery History

Determine whether the unit recently experienced a prolonged power loss, fully depleted battery, battery replacement, or storage period.

Verify normal charging and battery operation.

Expected outcome: A power-related event explains the lost time or configuration without evidence of continuing failure.

### 9. Verify Trend and Export Timestamps

Create a controlled test record and confirm that displayed trends, exported data, and receiving systems show the correct time.

Expected outcome: Time is correct throughout the complete data path.

### 10. Compare Configuration With an Approved Device

Review only accessible, authorized settings relevant to time and profile configuration.

Document any unexplained differences for escalation rather than changing restricted parameters.

Expected outcome: The affected device matches the approved configuration.

### 11. Escalate Recurrent Time or Configuration Loss

If the Rad-97 loses its clock or settings after restart, power removal, or normal operation, remove it from workflows requiring reliable records or communication.

Expected outcome: The device is routed for qualified service evaluation.

## If the Problem Persists

Common external causes such as incorrect time zone, profile mismatch, network disconnection, synchronization failure, and recent power loss have been ruled out.

The remaining cause may involve internal timekeeping, configuration storage, software, network authentication, or another service-level condition. Remove the device from service when accurate timestamps or configuration are clinically required, label it Out of Service, and send it for bench evaluation.

Use current manufacturer documentation and approved tools. Only authorized personnel should alter protected profiles, network settings, or configuration files. Verify time retention, trends, alarms, and communication before return to service.

## Clinical Use Tip

Incorrect device time can make otherwise valid trend and alarm records appear missing or associated with the wrong event.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Treat incorrect time as a data-integrity issue, verify approved settings and synchronization before assuming internal failure, restrict configuration changes to authorized personnel, and document end-to-end timestamp verification.

That is successful troubleshooting.
