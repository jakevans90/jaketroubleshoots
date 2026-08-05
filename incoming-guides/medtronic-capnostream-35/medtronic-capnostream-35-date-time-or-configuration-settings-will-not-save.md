---
schemaVersion: 1
title: "Medtronic Capnostream 35 Capnography Monitor - Date, Time, or Configuration Settings Will Not Save"
issueTitle: "Date, Time, or Configuration Settings Will Not Save"
description: "Addresses settings that revert, fail to store, or display incorrectly because of access level, shutdown method, synchronization, software, or internal retention problems."
assetType: "Capnography Monitor"
manufacturer: "Medtronic"
model: "Capnostream 35"
slug: "medtronic-capnostream-35-date-time-or-configuration-settings-will-not-save"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Capnostream 35 clock returned to the wrong time after each restart."
  cause: "Clinical Engineering found that the monitor was receiving an incorrect time from its configured network synchronization source."
  resolution: "The network time source was corrected through the authorized support team, and accurate time retention and event timestamps were verified after restart."
helpfulDetails:
  - "Exact setting that reverted"
  - "Point when the setting changed back"
  - "User access level"
  - "Save or apply action used"
  - "AC and battery condition"
  - "Normal restart result"
  - "Network or synchronization status"
  - "Comparison with approved configuration"
  - "Stored-event timestamp result"
  - "Final device status"
---

## What This Guide Helps With

Addresses settings that revert, fail to store, or display incorrectly because of access level, shutdown method, synchronization, software, or internal retention problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stored Clinical Data

Do not change time, date, alarm defaults, or monitoring configuration while the device is actively recording patient data unless the change is clinically authorized.

Move the patient to another verified monitor before restarting the unit or testing persistent setting changes.

**Expected outcome:** Patient monitoring and data timestamps remain protected.

### 2. Confirm Which Setting Does Not Save

Determine whether the date, time, time zone, alarm limits, display layout, patient type, communication settings, or another configuration value reverts.

Identify whether the setting changes immediately, after exiting the menu, after restart, after battery operation, or after network connection.

**Expected outcome:** The affected setting and the exact point of reversion are identified.

### 3. Verify User Access and Allowed Configuration

Confirm that the person making the change has the required access and that the setting is intended to be editable from the normal interface.

Do not enter unauthorized service menus or bypass protected configuration controls.

**Expected outcome:** The change is attempted through an authorized menu with sufficient access.

### 4. Confirm the Save or Apply Action

Repeat the change using the normal workflow and verify that any required Apply, Confirm, Save, or exit action is completed before leaving the menu.

**Expected outcome:** The new value remains visible after returning to the main screen. If it remains after restart, troubleshooting can stop.

### 5. Check Date, Time Zone, and Synchronization Source

Determine whether the monitor receives time from a network, central station, server, or other configured source. An external synchronization source may overwrite local settings.

Do not disable network synchronization without authorization from Clinical Engineering, IT, or the responsible clinical systems team.

**Expected outcome:** The active time source is understood, and the monitor retains the correct authorized time.

### 6. Verify Power and Shutdown Method

Confirm that AC power and battery operation are stable. Save the setting, shut the monitor down normally, wait briefly, and restart it.

An abrupt loss of power may prevent a setting change from being committed.

**Expected outcome:** The setting remains correct after a normal shutdown and restart. If so, troubleshooting can stop.

### 7. Disconnect Nonessential Network or USB Connections

When authorized and clinically safe, disconnect nonessential communication or USB connections and repeat the test. This helps determine whether an external system is overwriting the configuration.

**Expected outcome:** The setting remains saved when disconnected, identifying an external synchronization or configuration source.

### 8. Compare With Facility Configuration Requirements

Verify whether the device is intentionally managed by a standard profile or centralized configuration. Compare the observed setting with another correctly configured Capnostream 35 without copying settings blindly.

**Expected outcome:** The monitor matches the approved facility configuration, or an unauthorized profile overwrite is identified.

### 9. Test Multiple Noncritical Settings

Change an approved noncritical display option and restart the unit to determine whether the retention failure affects one setting or all settings.

Restore the approved configuration after testing.

**Expected outcome:** Normal retention of other settings isolates the failure. Widespread reversion suggests a broader software or internal retention problem.

### 10. Remove From Service if Critical Settings Cannot Be Retained

If date, time, alarm, or required configuration settings repeatedly revert after correct authorized saving, remove the monitor from service and label it **Out of Service**.

Escalate for software, configuration-memory, network-management, or internal power-retention evaluation.

**Expected outcome:** A monitor that cannot reliably retain required settings is prevented from clinical use.

## If the Problem Persists

Access, save workflow, power, synchronization, and centralized configuration causes have been ruled out. Remaining possibilities include software corruption, internal configuration-memory failure, retention-power problems, or service-level profile conflicts.

The device should be removed from service, labeled Out of Service, and evaluated using manufacturer documentation and approved service tools. Configuration restoration or internal repair should be performed only by qualified personnel and coordinated with IT when network management is involved.

After repair, verify date and time retention, approved configuration, alarm settings, restart behavior, network synchronization, stored-data timestamps, and complete monitoring functionality before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Incorrect time settings can mislabel stored trends and events even when live monitoring appears normal.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Verify authorization, save workflow, power, and external synchronization before assuming internal memory failure. Critical settings must remain correct after restart, and unresolved retention problems require removal from service, coordinated escalation, and clear documentation.

That is successful troubleshooting.
