---
schemaVersion: 1
title: "Getinge ROTAFLOW II Extracorporeal Membrane Oxygenation (ECMO) System - Network, Data Export, or Case Record Failure"
issueTitle: "Network, Data Export, or Case Record Failure"
description: "Troubleshoots missing case data, export failures, network connectivity, removable media, external cabling, configuration, and destination-system problems."
assetType: "Extracorporeal Membrane Oxygenation (ECMO) System"
manufacturer: "Getinge"
model: "ROTAFLOW II"
slug: "getinge-rotaflow-ii-network-data-export-or-case-record-failure"
dateAdded: "2026-09-16"
taxonomyMode: "reuse"
ccr:
  complaint: "ECMO staff reported the ROTAFLOW II case record would not transfer to the connected network destination after a case."
  cause: "Clinical Engineering found the external network cable partially disconnected at the device connection."
  resolution: "Reseated the network cable, completed an approved test record transfer to the intended destination, verified normal console operation, and returned the system to service."
helpfulDetails:
  - "Exact transfer or network message"
  - "Whether local case data was present"
  - "Wired connection status"
  - "Cable and connector condition"
  - "Network port tested"
  - "Approved media tested"
  - "Destination system involved"
  - "Whether other devices were affected"
  - "Configuration observed"
  - "IT or integration ticket number if applicable"
  - "Test record transfer result"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots missing case data, export failures, network connectivity, removable media, external cabling, configuration, and destination-system problems.

## Step-by-Step Troubleshooting
### 1. Protect Patient Support and Separate Data Failure From Therapy
Confirm pump operation, monitoring, and alarms remain available. A documentation or network failure should not interfere with ECMO support.

Provide an approved alternate method for recording required clinical information while troubleshooting.

**Expected outcome:** Clinical data is documented through an alternate workflow and ECMO support remains unaffected.

### 2. Confirm the Exact Data Failure
Determine whether the issue involves:
- Network connection
- Case record creation or storage
- Data export
- Transfer to another system
- Removable media
- Missing historical records
- Incorrect date or time affecting records
- Intermittent connection

Record any displayed message and the destination involved.

**Expected outcome:** The failure is narrowed to local recording, export, network transport, or destination-system behavior.

### 3. Verify Basic Console Operation
Confirm the ROTAFLOW II completes startup normally and can access normal case or data functions.

Do not make undocumented configuration changes to restore connectivity.

**Expected outcome:** Core console operation is normal and the fault is isolated to data handling or communication.

### 4. Inspect External Network or Data Connections
If wired connectivity is used, inspect the external cable and connectors for:
- Loose connections
- Broken locking tabs
- Damaged contacts
- Cuts or crushing
- Incorrect port connection
- Evidence of fluid contamination

Reseat connections when appropriate.

**Expected outcome:** The physical communication path is intact. If reseating a loose connection restores transfer, proceed to verification.

### 5. Check the Network Connection Point
Where applicable, verify the wall jack, switch connection, or approved network drop is active using hospital-approved methods.

Compare with a known-good connection when permitted.

Do not connect medical equipment to unauthorized networks.

**Expected outcome:** The external network path is available to the device.

### 6. Verify User-Accessible Network and Destination Information
Review the normal accessible configuration information required for communication, such as the selected destination or interface status.

Do not alter IP addressing, integration settings, protected configuration, or security parameters without authorization from the responsible IT or integration team.

**Expected outcome:** No obvious configuration mismatch is present, or an identified discrepancy is referred to the authorized team for correction.

### 7. Check Data Export Media When Applicable
If data is exported through approved removable media:
- Confirm the media is supported
- Inspect it for damage
- Verify it is properly inserted
- Confirm available storage when visible
- Test with known-good approved media if allowed

Do not use unknown or unauthorized removable media on clinical equipment.

**Expected outcome:** Export completes successfully to approved known-good media, or the failure is isolated to the system rather than the original media.

### 8. Verify the Receiving System
Coordinate with clinical IT or integration support to determine whether:
- The intended destination is available
- Other devices are experiencing similar failures
- The interface or network service is down
- Records are being received but not displayed
- An infrastructure change recently occurred

**Expected outcome:** A destination or infrastructure outage is distinguished from a ROTAFLOW II device fault.

### 9. Perform Final Data Verification
After correction, perform an approved test or non-patient record workflow and confirm:
- Case record is stored as expected
- Export completes
- Network status is normal when applicable
- Destination receives the test data when appropriate
- Date and time associated with the record are correct
- Core pump and alarm functions remain unaffected

**Expected outcome:** Data handling is reliable from the source through the intended destination. Troubleshooting can stop.

### 10. Escalate Persistent Communication or Record Failure
If physical connections, approved media, network availability, and destination status are normal but data transfer or recording still fails, escalate to Getinge service and the appropriate hospital IT or integration team.

**Expected outcome:** The unresolved issue is assigned to the correct technical group without making unauthorized configuration changes.

## If the Problem Persists
External cables, network availability, approved media, destination status, and normal user-accessible settings have been evaluated. Remaining possibilities include internal storage, communication hardware, software, interface configuration, cybersecurity controls, or infrastructure-level integration issues.

The affected device should be:

- Removed from service when the failure affects a required safety or clinical function
- Labeled **Out of Service** when continued use is not clinically or operationally acceptable
- Sent for repair or bench evaluation when a device-level fault is suspected
- Evaluated using appropriate Getinge documentation and approved test equipment
- Repaired or configured only by qualified personnel

Coordinate configuration or network changes with authorized IT and integration personnel. After corrective action, verify the complete data path before relying on electronic records.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
When ECMO electronic records are unavailable, maintain an approved alternate documentation method so critical pump, flow, pressure, and patient-support information is not lost.

## Work Order Documentation (CCR Method)
<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)
<!-- Helpful details come from front matter. -->

## Final Thought
Keep ECMO support and documentation continuity intact, verify physical and infrastructure causes before assuming an internal data fault, test the complete communication path, and escalate configuration issues to the appropriate authorized team.

That is successful troubleshooting.
