---
schemaVersion: 1
title: "LivaNova S5 Heart-Lung Machine - Case Record or Data-Management Export Fails"
issueTitle: "Case Record or Data-Management Export Fails"
description: "Troubleshoots failed case-data export caused by media, connections, destination availability, configuration, storage, or external data-management system problems."
assetType: "Heart-Lung Machine"
manufacturer: "LivaNova"
model: "S5"
slug: "livanova-s5-case-record-or-data-management-export-fails"
dateAdded: "2026-10-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Perfusion reported that completed S5 case records were available on the system but would not export to the designated data-management destination."
  cause: "Clinical Engineering found the external data cable partially disconnected at the receiving interface."
  resolution: "The connection was reseated and secured, and a controlled test record exported successfully and was verified at the destination."
helpfulDetails:
  - "Whether the record exists locally"
  - "Exact displayed export message"
  - "Export method used"
  - "Cable and connector condition"
  - "Removable media used, if applicable"
  - "Known-good substitution results"
  - "Local storage indication"
  - "Destination system availability"
  - "Network or infrastructure status"
  - "Whether one or all records are affected"
  - "Test-export result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots failed case-data export caused by media, connections, destination availability, configuration, storage, or external data-management system problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Separate Data Failure From Pumping Function

Do not interrupt active extracorporeal support solely to troubleshoot case-data export.

If the S5 is currently supporting a patient and pumping functions remain normal, document the export problem and defer technical troubleshooting until the system can be safely evaluated without affecting patient care.

**Expected outcome:** Clinical support continues safely and data troubleshooting occurs only when it cannot interfere with perfusion operation.

### 2. Confirm the Exact Export Failure

Determine whether:

- A case record is visible locally but will not export
- No case record is being created
- Export begins but stops
- The destination does not recognize the file
- Only one case is affected
- All exports fail
- The problem occurs with removable media, network transfer, or another data-management path

Record any exact on-screen message without interpreting it beyond what is displayed.

**Expected outcome:** The failure is narrowed to record creation, local storage, transfer, or destination access.

### 3. Verify the Case Record Exists Locally

Using normal authorized controls, confirm that the expected case or record is present and can be opened or reviewed locally where applicable.

If the record itself is missing, an export problem cannot be distinguished from a case-recording or storage problem until that issue is investigated.

**Expected outcome:** The intended case record exists locally and is available for export.

### 4. Inspect External Connections and Export Media

For a physical export path, inspect the applicable external components for:

- Loose connection
- Damaged connector
- Bent or contaminated contacts
- Damaged cable
- Improperly inserted media
- Unsupported or suspect media
- Visible physical damage

Reconnect securely and retry using normal controls.

**Expected outcome:** The physical export connection or media is correctly installed and undamaged.

### 5. Try a Known-Good Approved Export Device or Cable

When applicable, test with a known-good compatible cable, removable storage device, interface, or destination connection that is approved for the environment.

Do not connect unapproved personal storage devices or alter cybersecurity controls.

**Expected outcome:** Export succeeds with the known-good component, identifying the original external accessory or connection as the cause.

### 6. Verify Available Storage and Record Status

Check normal user-accessible indications for local storage availability and whether the case record has completed saving.

Avoid deleting clinical records merely to create space unless this is performed under the facility's approved data-retention and service procedures.

**Expected outcome:** The source record is complete and the device has adequate normal operating storage for the required data function.

### 7. Check Normal Data-Management Configuration

Review authorized, normally accessible settings relevant to the export path.

Verify that the selected export destination, data-management connection, and applicable communication settings match the intended workflow.

Do not modify restricted network parameters, cybersecurity settings, service configuration, or protected system files without authorization.

**Expected outcome:** The export destination and normal configuration correspond to the intended data path.

### 8. Verify the Receiving System or Destination

If data is being sent to another workstation, server, or clinical data-management system, determine whether that destination is available.

Check:

- Destination powered on
- Network or interface connection present
- Other systems able to reach the destination
- Adequate destination storage if this can be verified
- No known infrastructure outage
- Correct destination selected

Coordinate with IT or the responsible clinical data-management team when appropriate.

**Expected outcome:** The receiving system is available and capable of accepting data.

### 9. Perform a Controlled Test Export

Using a suitable non-patient test record or approved test workflow, perform another export.

Determine whether the failure:

- Follows one specific record
- Occurs with all records
- Occurs only through one export method
- Occurs only with one destination

Avoid unnecessary copying of protected patient information during testing.

**Expected outcome:** The export completes and the resulting record is accessible at the intended destination. If so, troubleshooting can stop after documentation.

### 10. Stop and Escalate Persistent Data Failures

If records are present locally but repeatedly fail to export after external connections, media, destination availability, and normal configuration have been verified, escalate the issue.

Do not modify internal storage, operating-system files, protected networking, or data-management software outside approved service procedures.

**Expected outcome:** Persistent data problems are escalated without risking stored clinical information or system operation.

## If the Problem Persists

Common external causes involving media, cables, record availability, storage status, destination access, and normal configuration have been ruled out.

Remaining categories may include internal storage, application software, communication interfaces, database integrity, network infrastructure, permissions, or data-management integration.

The device should be:

- Removed from the affected data-management workflow as necessary
- Labeled Out of Service if the failure compromises required clinical documentation or facility policy
- Sent for repair or bench evaluation when hardware or local system failure is suspected
- Evaluated using appropriate LivaNova documentation and approved tools
- Coordinated with IT or data-management support when infrastructure is involved
- Returned to full service only after successful test export and confirmation that the intended destination can access the record

Knowing when to stop before altering protected data or system configuration is proper troubleshooting.

## Clinical Use Tip

A functioning pump does not make a failed case-record pathway acceptable when electronic perfusion documentation is required; preserve local records until export is verified.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- rendered from front matter -->

## Final Thought

Case-record troubleshooting should protect both the patient and the integrity of stored clinical information. Verify the simple physical and destination-side causes first, avoid unauthorized changes to protected systems, and escalate persistent data-management problems with clear documentation.

That is successful troubleshooting.
