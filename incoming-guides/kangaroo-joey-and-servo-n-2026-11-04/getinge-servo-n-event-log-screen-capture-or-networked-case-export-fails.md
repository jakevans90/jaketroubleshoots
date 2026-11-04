---
schemaVersion: 1
title: "Getinge Servo-n Ventilator - Event Log, Screen Capture, or Networked Case Export Fails"
issueTitle: "Event Log, Screen Capture, or Networked Case Export Fails"
description: "Troubleshoots failed data retrieval or export caused by storage media, connections, network availability, configuration, destination access, or service-level faults."
assetType: "Ventilator"
manufacturer: "Getinge"
model: "Servo-n"
slug: "getinge-servo-n-event-log-screen-capture-or-networked-case-export-fails"
dateAdded: "2026-11-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that screen captures were available on the Servo-n but could not be exported to the network destination."
  cause: "Clinical Engineering found the ventilator's external network cable was disconnected at the wall jack while local data storage remained functional."
  resolution: "The network cable was reconnected, successful case export was verified at the destination, and the ventilator remained available for clinical use."
helpfulDetails:
  - "Event log, screen capture, or case export affected"
  - "Local data availability"
  - "Displayed message"
  - "Removable media tested"
  - "Network cable condition"
  - "Port or link status"
  - "Whether other ventilators are affected"
  - "Destination availability"
  - "IT or Clinical Integration findings"
  - "Date/time or device assignment observed"
  - "Successful final export"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots failed data retrieval or export caused by storage media, connections, network availability, configuration, destination access, or service-level faults.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Separate Data Failure From Ventilation
Confirm that the reported problem involves event data, screenshots, or network export rather than ventilation, alarms, or monitoring.

Do not interrupt active ventilation solely to troubleshoot a documentation or export problem.

If troubleshooting requires restarting or disconnecting the ventilator, remove it from patient dependency first.

**Expected outcome:** Patient care remains unaffected while the data problem is investigated.

### 2. Confirm the Exact Export Failure
Determine whether the failure affects:
- Event log access
- Screen capture
- Local export
- Removable media
- Networked case export
- One destination only
- All data-export functions

Record any displayed message.

**Expected outcome:** The failed function and destination are clearly identified.

### 3. Verify That the Data Exists Locally
Before troubleshooting the network, verify that the expected event, screen capture, or case information is available locally when normal device functions permit.

**Expected outcome:** The problem is differentiated between data creation/storage and data transfer.

### 4. Inspect External Media
If removable media is used, verify:
- Correct approved media type
- Proper insertion
- Adequate physical condition
- No obvious connector damage
- Media is not write-protected when writing is required

Test with known-good approved media when available.

**Expected outcome:** Local export succeeds or the external media is ruled out.

### 5. Inspect Network and Data Connections
Check accessible Ethernet, interface, or other data cables for:
- Loose connections
- Broken latches
- Damaged cable
- Incorrect port
- Disconnected wall jack
- Link indication when applicable

Reseat connections.

**Expected outcome:** The physical network path is intact.

### 6. Determine Whether the Problem Is Device-Specific
Compare the affected Servo-n with another known-working device using the same network or export destination when appropriate.

Also determine whether multiple devices are experiencing the same failure.

**Expected outcome:** The problem is localized to the individual ventilator or identified as a broader network/infrastructure issue.

### 7. Verify Network Availability With IT or Clinical Integration
If network export fails but local data functions work, coordinate with IT, Clinical Integration, or the responsible system administrator.

Verify:
- Destination availability
- Network port status
- Relevant device assignment
- Interface service availability
- Approved network configuration

Do not make undocumented network configuration changes.

**Expected outcome:** Infrastructure and destination availability are confirmed.

### 8. Verify Date, Time, and Device Identification
Check normal user-accessible date, time, and device-identification information when these are relevant to case association or export.

Do not alter settings without appropriate authorization.

**Expected outcome:** Records can be correctly associated with the intended device, event, and destination.

### 9. Test the Full Export Workflow
Repeat the intended event-log, screen-capture, or case-export workflow after correcting any external media, cable, network, or destination issue.

**Expected outcome:** The requested data transfers successfully and is readable at the destination. Troubleshooting can stop.

### 10. Perform Final Functional Verification
If the ventilator was restarted, disconnected, or removed from clinical use during troubleshooting, complete the appropriate pre-use and functional checks before return to service.

**Expected outcome:** Both ventilator operation and required data/export functions are verified.

## If the Problem Persists

External media, cables, network connectivity, destination availability, and normal configuration have been ruled out. The remaining problem may involve internal storage, network hardware, software, data corruption, interface configuration, or another service-level issue.

The Servo-n should be:
- Removed from the affected data workflow as appropriate
- Labeled Out of Service when the missing data capability is required for intended use or policy compliance
- Sent for repair or bench evaluation when device-specific failure is confirmed
- Evaluated with appropriate Getinge documentation and approved diagnostic tools
- Repaired or configured only by qualified personnel

Coordinate with IT or Clinical Integration when the problem lies outside the ventilator. Verify required data functions and ventilator performance before return to unrestricted service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Confirm whether the failure is local storage, physical connectivity, or the receiving system before changing ventilator network configuration.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Keep patient care separate from data troubleshooting, then verify local data, media, connections, network infrastructure, and destination availability before assuming an internal failure. Escalate appropriately and clearly document what was tested and restored.

That is successful troubleshooting.
