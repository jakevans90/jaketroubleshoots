---
schemaVersion: 1
title: "Fresenius Kabi Ivenix Infusion System Infusion Pump - Event Log, Device Clock, or Infusion-History Export Is Incorrect"
issueTitle: "Event Log, Device Clock, or Infusion-History Export Is Incorrect"
description: "Incorrect timestamps, missing infusion history, incomplete exports, time synchronization problems, device identity errors, or connectivity issues affecting records."
assetType: "Infusion Pump"
manufacturer: "Fresenius Kabi"
model: "Ivenix Infusion System"
slug: "fresenius-kabi-ivenix-infusion-system-event-log-device-clock-or-infusion-history-export-is-incorrect"
dateAdded: "2026-11-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that infusion-history records exported from one Ivenix pump appeared one hour later than the events actually occurred."
  cause: "Clinical Engineering found the pump's displayed clock was offset from the facility time while other fleet devices were correct."
  resolution: "Escalated the clock-synchronization issue through the approved support process, verified corrected time against the facility reference, generated a controlled test event, confirmed matching local and exported timestamps, and returned the pump to service."
helpfulDetails:
  - "Exact clock or history discrepancy"
  - "Device time compared with facility reference"
  - "Amount and direction of time offset"
  - "Whether other pumps are affected"
  - "Network connection status"
  - "Device/fleet identity"
  - "Local history present or missing"
  - "Export destination"
  - "Controlled test-event time"
  - "Local versus exported timestamp"
  - "Whether records were preserved for investigation"
  - "Final clock and export verification"
  - "Final device status"
---

## What This Guide Helps With

Incorrect timestamps, missing infusion history, incomplete exports, time synchronization problems, device identity errors, or connectivity issues affecting records.

## Step-by-Step Troubleshooting

### 1. Preserve Clinical and Investigative Data

If the pump is involved in a patient-safety event, suspected delivery discrepancy, or formal investigation, do not reset, clear, overwrite, or alter data unnecessarily. Follow facility evidence-preservation procedures.

Expected outcome: Relevant device information remains available for clinical, risk-management, or service review.

### 2. Confirm the Exact Data Problem

Determine whether the issue is an incorrect clock, wrong date, shifted timestamps, missing event-log entries, incomplete infusion history, failed export, duplicate data, or information assigned to the wrong device.

Expected outcome: The record problem is clearly characterized.

### 3. Verify the Current Device Clock

Compare the displayed device time and date with the facility's authoritative time source. Note whether the offset is minutes, hours, a time-zone difference, or an incorrect date.

Expected outcome: The clock is confirmed correct or the amount and pattern of error are documented.

### 4. Check Whether Other Devices Are Affected

Compare another Ivenix pump in the same environment. Determine whether multiple pumps show the same time or export problem.

Expected outcome: A device-specific issue is separated from a fleet-management, network-time, server, or integration problem.

### 5. Verify Network Connectivity

If the device normally receives time or exports records through the network, confirm expected network connectivity.

Expected outcome: The pump can communicate with the required infrastructure.

### 6. Confirm Device Identity and Assignment

Verify the pump's asset identity, network identity, and fleet record. Check that exported information is not being associated with a duplicate, retired, or incorrectly assigned device record.

Expected outcome: Device identity is correct throughout the management system.

### 7. Check Export Destination and Workflow

Confirm whether the expected destination is the fleet-management system, integration server, EMR, service application, or another approved repository. Verify that the correct export method is being used.

Expected outcome: The record is being sent through the intended workflow.

### 8. Check for Available Storage or Pending Data Status

Using normal approved device or management-system functions, determine whether events appear locally but remain pending for upload, or whether the records are missing locally as well.

Expected outcome: The failure is localized to data generation, local storage, or transmission.

### 9. Perform a Controlled Test Event

Outside patient use, create a benign, documented test event through normal pump operation and note the exact time.

Expected outcome: The event appears in the expected local history with an accurate timestamp and, when applicable, exports to the expected destination.

### 10. Perform a Normal Restart if Appropriate

If no investigation requires preserving the current operating state, perform a normal restart and allow the pump to reconnect. Do not factory-reset, clear logs, or alter protected clock settings without authorization.

Expected outcome: The clock and data services initialize normally.

### 11. Compare Local and Exported Records

Compare the timestamp and content of the controlled event on the pump with the exported record.

Expected outcome: Local and remote records agree. If the local record is correct but the exported record is not, escalate toward the interface or server system rather than assuming pump failure.

### 12. Verify Clock Synchronization After Correction

If an approved correction is made to time synchronization, network configuration, or device assignment, repeat the controlled event and verify that new records remain accurate.

Expected outcome: Subsequent events use the correct date, time, identity, and export path.

### 13. Escalate Without Destroying Evidence

If event history remains incorrect or unavailable, preserve relevant records and escalate to Fresenius Kabi support, Clinical Engineering leadership, IT/integration, risk management, or other appropriate teams depending on the situation.

Expected outcome: The issue is transferred with preserved evidence and documented observations.

## If the Problem Persists

Common external causes such as incorrect device assignment, disconnected networking, incorrect export workflow, temporary communication failure, and obvious clock mismatch have been ruled out. Persistent problems may involve time synchronization, fleet-management infrastructure, local storage, device software, interface middleware, database handling, or other service-level configuration.

Remove the pump from service if accurate event history or record integrity is required and cannot be assured, particularly when the device is being evaluated after a clinical event. Label it Out of Service and preserve relevant information.

Evaluate the device using appropriate Fresenius Kabi documentation, approved software tools, and qualified personnel. Do not clear event logs or perform resets that could destroy required records unless specifically authorized.

Return to service only after clock accuracy, event generation, history retention, and required export functions are verified.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

When reviewing a pump after a clinical event, record the observed device clock offset before making any authorized correction so timestamps can be interpreted accurately.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Treat pump history as potentially important clinical evidence. Preserve data first, verify time and device identity before assuming internal failure, trace the complete export path, and escalate without destroying information.

That is successful troubleshooting.
