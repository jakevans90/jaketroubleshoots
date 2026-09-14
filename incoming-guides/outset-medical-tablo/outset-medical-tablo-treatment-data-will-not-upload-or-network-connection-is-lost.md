---
schemaVersion: 1
title: "Outset Medical Tablo Hemodialysis (HD) Machine - Treatment Data Will Not Upload or Network Connection Is Lost"
issueTitle: "Treatment Data Will Not Upload or Network Connection Is Lost"
description: "Troubleshoot treatment-data upload and connectivity problems caused by network availability, configuration, signal, infrastructure, or communication-path interruptions."
assetType: "Hemodialysis (HD) Machine"
manufacturer: "Outset Medical"
model: "Tablo"
slug: "outset-medical-tablo-treatment-data-will-not-upload-or-network-connection-is-lost"
dateAdded: "2026-09-14"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported the Tablo completed treatments normally but treatment records were no longer uploading to the expected system."
  cause: "Clinical Engineering found the device had lost its approved network connection after being moved to a different treatment area."
  resolution: "Returned the unit to the approved connected location, verified network connectivity and successful treatment-data transfer, and confirmed normal operation with staff."
helpfulDetails:
  - "Exact network or upload message"
  - "Connected or disconnected status"
  - "Wired or wireless communication"
  - "Room or location"
  - "Whether other devices are affected"
  - "Recent network or location changes"
  - "Whether treatment data is retained locally"
  - "Receiving application or system affected"
  - "Results after reconnection or restart"
  - "Final communication status"
---

## What This Guide Helps With

Troubleshoot treatment-data upload and connectivity problems caused by network availability, configuration, signal, infrastructure, or communication-path interruptions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve the Clinical Record

A network problem should not distract from safe dialysis treatment. Do not interrupt functioning therapy solely to troubleshoot data connectivity unless clinical workflow requires it.

Ensure required treatment information is preserved or documented using the facility's approved downtime process when electronic transfer is unavailable.

**Expected outcome:** Patient care continues safely and required treatment documentation is not lost because of the network issue.

### 2. Confirm the Exact Connectivity Problem

Determine whether the Tablo:

- Shows no network connection
- Loses connection intermittently
- Connects but treatment data does not upload
- Uploads some treatments but not others
- Cannot reach the expected destination
- Developed the problem after relocation or infrastructure changes

Record any displayed network or upload message.

**Expected outcome:** The problem is separated into device connectivity versus data-transfer failure.

### 3. Check the Device's Normal Network Status

Review user-accessible network status indicators without changing protected configuration.

Note whether the machine appears connected, disconnected, or intermittently connected.

**Expected outcome:** The current connectivity state is documented. If the device reconnects and pending data transfers normally, troubleshooting can stop after verification.

### 4. Inspect Accessible Network Connections

If the installation uses accessible physical connections, inspect them for looseness, damage, contamination, or strain. If communication is wireless, confirm the machine is located where the approved network is expected to be available.

Do not connect the device to an unapproved network.

**Expected outcome:** The external communication path is physically intact and appropriate for the installation.

### 5. Compare With Other Devices or Locations

Determine whether other Tablo systems or approved networked equipment in the same area are also affected.

If multiple devices lose connectivity simultaneously, involve the appropriate IT or network support team before assuming a Tablo hardware problem.

**Expected outcome:** The issue is narrowed to the individual machine or shared network infrastructure.

### 6. Check for Recent Infrastructure or Location Changes

Ask whether the device was recently moved, the network was changed, maintenance occurred, credentials or certificates were updated, or a clinical interface experienced downtime.

Avoid making undocumented network configuration changes.

**Expected outcome:** Any infrastructure-related change associated with the onset of the problem is identified.

### 7. Perform a Normal Reconnection or Restart When Appropriate

When the machine is not supporting a patient and normal workflow permits it, use standard user-accessible controls to reconnect or perform a controlled restart.

Do not repeatedly reboot an active treatment system just to restore data transfer.

**Expected outcome:** The device reconnects and normal data transmission resumes. If it does, verify successful upload before stopping troubleshooting.

### 8. Verify the Complete Data Path

Confirm not only that the device indicates connectivity, but also that the expected treatment data reaches its intended clinical destination when a valid test or completed record is available.

Coordinate with IT or application support when the device is connected but the receiving system does not show the record.

**Expected outcome:** The complete communication path is confirmed from the Tablo to the intended receiving system.

### 9. Document Any Downtime or Delayed Upload

If data transfer was delayed, confirm clinical staff have followed appropriate documentation procedures and that records are reconciled after connectivity returns.

**Expected outcome:** No required treatment documentation is omitted because of the outage.

### 10. Escalate Persistent Connectivity Failure

If accessible connections, device status, location, and facility network availability appear normal but the Tablo cannot maintain communication or upload records, escalate appropriately.

**Expected outcome:** Device-level communication, configuration, application, security, or infrastructure causes are investigated by qualified technical teams.

## If the Problem Persists

Common external connection, location, network-availability, and temporary communication causes have been ruled out. A persistent failure may involve device network hardware, application services, cybersecurity configuration, certificates, interface services, account provisioning, or facility network infrastructure.

The device should be:

- Removed from service if the connectivity failure prevents required safe clinical use or documentation
- Labeled **Out of Service** when removal is necessary
- Sent for repair or bench evaluation if a machine-specific hardware fault is suspected
- Evaluated using appropriate Outset Medical documentation and approved network diagnostic methods
- Configured or repaired only by qualified personnel

Coordinate with IT, interface, cybersecurity, or vendor support when appropriate. Verify the complete data-transfer path before declaring the issue resolved. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A connected network indicator alone is not enough; confirm required treatment data actually reaches the intended clinical record or receiving application.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Connectivity troubleshooting should distinguish device problems from shared infrastructure and application problems without compromising ongoing dialysis care. Verify the complete communication path, preserve treatment documentation during outages, escalate to the correct technical team, and document the final resolution clearly.

That is successful troubleshooting.
