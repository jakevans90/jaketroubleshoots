---
schemaVersion: 1
title: "Getinge Servo-u Ventilator - Event Log, Screen Capture, or Networked Case Data Will Not Export"
issueTitle: "Event Log, Screen Capture, or Networked Case Data Will Not Export"
description: "Helps isolate export failures caused by removable media, connections, permissions, configuration, network availability, destination systems, or data-transfer interruptions."
assetType: "Ventilator"
manufacturer: "Getinge"
model: "Servo-u"
slug: "getinge-servo-u-event-log-screen-capture-or-networked-case-data-will-not-export"
dateAdded: "2026-10-23"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that event logs from the Servo-u would not export to the approved USB device."
  cause: "Clinical Engineering found the original removable media was not accepting new files, while known-good approved media worked normally."
  resolution: "Replaced the faulty media, successfully exported and opened the event log, verified normal ventilator operation, and returned the device to service."
helpfulDetails:
  - "Type of data being exported"
  - "USB or network export method"
  - "Whether the data existed before export"
  - "Removable-media condition"
  - "Known-good media test result"
  - "External port condition"
  - "Network cable and link status"
  - "Room, wall jack, or network path tested"
  - "Whether other Servo-u units were affected"
  - "Receiving-system status"
  - "Whether the exported file was successfully opened"
  - "Results before and after correction"
  - "Final device status"
---

## What This Guide Helps With

Helps isolate export failures caused by removable media, connections, permissions, configuration, network availability, destination systems, or data-transfer interruptions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Separate Data Export From Ventilation
Do not interrupt active ventilation solely to troubleshoot an export problem.

If troubleshooting requires restarting the ventilator, disconnecting network infrastructure, or performing any action that could affect therapy, move the patient to verified alternate support first.

**Expected outcome:** Ventilation remains uninterrupted while the data-export problem is evaluated safely.

### 2. Confirm What Type of Export Is Failing
Determine whether the problem involves:

- Event log export
- Screen capture export
- Case or patient data transfer
- USB or removable-media export
- Networked data transfer
- More than one export method

Confirm whether the failure affects one specific file or all export attempts.

**Expected outcome:** The affected export path and data type are clearly identified.

### 3. Confirm That the Data Exists and Is Available to Export
Verify through normal user-accessible functions that the expected event, screen capture, or case data is present on the Servo-u.

Do not assume a transfer failure if the requested data was never stored or captured.

**Expected outcome:** The requested data is present and available for the intended export process.

If the data is not present, document that finding and distinguish a capture/storage issue from an export issue.

### 4. Inspect the Removable Media When USB Export Is Used
If export is being attempted to removable media, inspect the media and accessible USB connection for:

- Physical damage
- Loose fit
- Contamination
- Unsupported adapters or extension devices
- Media that is full or write-protected
- Media already known to be unreliable

Use only facility-approved removable media when required by cybersecurity policy.

**Expected outcome:** Approved removable media is physically intact, appropriately connected, and available for writing.

If replacing questionable media with approved known-good media allows the export to complete, verify the exported file and stop troubleshooting.

### 5. Test With Known-Good Approved Media
Use a known-good facility-approved removable device where permitted.

Do not connect unknown personal media to a clinical ventilator.

Attempt the same export again.

**Expected outcome:** The Servo-u successfully writes the requested data to known-good approved media.

If the known-good media works, remove the original media from use and stop troubleshooting after verifying file readability.

### 6. Inspect the Accessible Data Port
Inspect the applicable external data port for:

- Bent or damaged contacts
- Loose mounting
- Contamination
- Foreign material
- Evidence of fluid intrusion
- Intermittent connection when the plug is normally handled

Do not disassemble the ventilator to access the port internally.

**Expected outcome:** The external port is clean, intact, and holds the connector securely.

If an obvious external connection problem is corrected and export succeeds, verify the exported data before returning the device to normal use.

### 7. Verify Approved Export Workflow and Configuration
Confirm that the correct normal export function is being used and that the ventilator is not in a state that prevents the requested export.

Review only authorized user-accessible configuration.

Do not change protected settings, enable unsupported interfaces, or enter restricted service menus merely to make an export work.

**Expected outcome:** The requested export method is available and correctly selected.

If correcting an approved workflow selection resolves the issue, verify that the resulting file contains the intended data.

### 8. Check Network Connectivity for Networked Exports
If case data is sent through the network, verify the basic physical network path.

Check:

- Network cable seating
- Visible cable damage
- Wall jack or approved network connection
- Link indication when available
- Whether other devices on the same approved infrastructure are communicating normally

Do not move the ventilator to an unauthorized network connection.

**Expected outcome:** The physical network connection is present and stable.

If reseating or replacing a damaged external network cable restores transfer, verify successful delivery and stop troubleshooting.

### 9. Determine Whether the Problem Follows the Device or Infrastructure
Where operationally appropriate, compare the affected Servo-u with another similarly configured unit on the same network path or compare the same ventilator on another approved connection.

Coordinate with IT or clinical systems personnel before changing network locations or ports.

**Expected outcome:** The comparison helps determine whether the failure is isolated to the ventilator, a specific network connection, or the receiving system.

If multiple devices fail on the same path, escalate to the appropriate network or application support team rather than servicing the ventilator unnecessarily.

### 10. Verify the Receiving System
For networked case-data transfer, confirm with the responsible IT, integration, or clinical systems team that the destination service is available and expecting data.

Possible external categories include:

- Destination server unavailable
- Network segment or port issue
- Interface service stopped
- Authorization or certificate problem
- Configuration mismatch
- Storage or receiving application issue

Clinical Engineering should not make unsupported server or network configuration changes.

**Expected outcome:** The receiving infrastructure is confirmed operational or the infrastructure fault is identified for escalation.

If the destination system was unavailable and data transfer succeeds after infrastructure restoration, verify the complete path and stop troubleshooting.

### 11. Verify Exported Data
A completed export indication alone is not sufficient.

Confirm that the resulting file or transferred case data:

- Exists at the intended destination
- Opens or is recognized by the approved receiving system
- Contains the expected event, image, or case information
- Is associated with the intended device or case when applicable

Follow facility privacy and data-handling requirements.

**Expected outcome:** The requested information is successfully exported and usable at the intended destination.

If verified, troubleshooting can stop.

### 12. Perform Final Functional Verification
If any device connection or configuration was changed during troubleshooting, verify normal Servo-u operation afterward.

Confirm:

- Ventilator functions normally
- No new communication or system alarms are present
- Export remains reproducible
- Network connection is stable when required
- No unauthorized settings were changed

**Expected outcome:** Both ventilation and the intended export function operate normally.

### 13. Escalate Persistent Export Failures
If approved media, external connections, workflow, network availability, and receiving infrastructure have been ruled out, stop external troubleshooting.

Do not attempt internal board repair, unsupported software modification, or unauthorized network configuration changes.

**Expected outcome:** The device is appropriately escalated for qualified technical evaluation.

## If the Problem Persists

Common external causes have been ruled out. The remaining issue may involve internal storage, the data interface, software, protected configuration, network configuration, security credentials, or communication between the ventilator and the receiving infrastructure.

If the export function is required for safe clinical workflow, regulatory documentation, or patient-data continuity and cannot be reliably performed, the affected function should be treated as unavailable until repaired.

The device should be:

- Removed from service when the failed function affects required clinical use or documentation
- Labeled Out of Service when appropriate
- Sent for repair or bench evaluation when a device-level fault is suspected
- Evaluated using appropriate Getinge documentation and approved test equipment
- Repaired or configured only by qualified personnel

Coordinate with IT, cybersecurity, integration, or application support when evidence points to infrastructure rather than the ventilator.

Return the device to service only after required communication and export functions have been verified.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Before declaring a data export successful, confirm the information actually reached and can be opened at the intended destination without disrupting active ventilation.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Treat export problems as an end-to-end data-path issue rather than immediately blaming the ventilator. Protect ventilation, verify the data, media, connections, network, and destination in logical order, escalate at the correct boundary, and document the verified result.

That is successful troubleshooting.
