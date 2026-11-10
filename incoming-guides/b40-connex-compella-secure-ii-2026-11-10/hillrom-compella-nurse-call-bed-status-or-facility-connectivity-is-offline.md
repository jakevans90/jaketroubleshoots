---
schemaVersion: 1
title: "Hillrom Compella Hospital Bed - Nurse Call, Bed Status, or Facility Connectivity Is Offline"
issueTitle: "Nurse Call, Bed Status, or Facility Connectivity Is Offline"
description: "Troubleshoot missing nurse-call communication, bed-status reporting, or facility connectivity caused by cables, interfaces, configuration, or infrastructure problems."
assetType: "Hospital Bed"
manufacturer: "Hillrom"
model: "Compella"
slug: "hillrom-compella-nurse-call-bed-status-or-facility-connectivity-is-offline"
dateAdded: "2026-11-10"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that the Compella patient nurse-call button did not generate a call at the nursing station."
  cause: "Clinical Engineering found the external nurse-call communication cable partially disconnected from the room interface."
  resolution: "Secured the cable and verified successful patient call transmission, correct room identification, and acknowledgment at the nursing station."
helpfulDetails:
  - "Nurse-call or bed-status function affected"
  - "Room and receiving station"
  - "Bed power condition"
  - "Communication cable condition"
  - "Wall interface condition"
  - "Known-good cable results"
  - "Comparison room or bed tested"
  - "Configuration or assignment observed"
  - "Receiving station test results"
  - "Final equipment status"
---

## What This Guide Helps With

Troubleshoot missing nurse-call communication, bed-status reporting, or facility connectivity caused by cables, interfaces, configuration, or infrastructure problems.

## Step-by-Step Troubleshooting

### 1. Maintain Patient Communication and Monitoring

An unavailable nurse-call connection can prevent patient requests or bed alerts from reaching staff.

- Inform nursing that the affected communication function is unreliable.
- Establish an approved alternate patient communication method.
- Arrange appropriate monitoring when remote bed-status or alarm reporting is unavailable.
- Do not rely on unverified remote notifications.
- Remove the bed from service if required communication safety functions cannot be maintained.

Expected outcome: Patient communication and monitoring needs are maintained independently of the failed connection.

### 2. Confirm Which Communication Function Is Offline

Determine whether the problem affects nurse call, bed status, or another facility interface.

- Ask whether patient-initiated calls fail.
- Determine whether bed-exit or other supported status information is missing.
- Identify whether the issue occurs at one room or multiple locations.
- Record any displayed communication message.
- Determine whether the problem began after moving the bed.

Expected outcome: The failed communication path and affected destination are identified.

### 3. Verify Bed Power and Local Operation

Check the bed's electrical condition.

- Confirm AC power availability.
- Inspect the power cord and plug.
- Check relevant system indicators.
- Verify that local controls operate normally.
- Confirm that local alarm or status functions respond where applicable.

Expected outcome: The bed is powered and its local functions operate correctly.

### 4. Inspect External Communication Connections

Examine the accessible communication interface.

- Check the bed communication cable for damage.
- Verify that connectors are fully seated.
- Inspect connector pins and housings without disassembly.
- Look for crushed, stretched, or pinched cables.
- Confirm that the correct facility-approved cable is being used.

Expected outcome: The external communication connection is intact and secure.

### 5. Verify the Room Interface

Check the facility connection point.

- Inspect the wall receptacle or approved interface module.
- Confirm that the bed is connected to the intended port.
- Look for visible damage or loose connections.
- Identify whether the interface requires an approved adapter.
- Do not bypass or modify facility communication wiring.

Expected outcome: The room connection is physically intact and appropriate for the bed.

### 6. Isolate the Bed, Cable, and Facility Connection

Use controlled comparisons when approved.

- Test with a compatible known-good communication cable.
- Compare with a verified bed using the same room interface, if operationally appropriate.
- Test the affected bed at another approved connection point when permitted.
- Record whether the failure follows the bed, cable, or room.
- Coordinate any room-interface testing with the responsible facilities or communication team.

Expected outcome: The fault is narrowed to the bed, external accessory, or facility infrastructure.

### 7. Verify Approved Configuration and Assignment

Check configuration information accessible through authorized procedures.

- Confirm the correct bed or room assignment where applicable.
- Verify the intended communication mode.
- Check for an incorrect or missing facility interface association.
- Coordinate network or system-side configuration with the responsible team.
- Do not alter protected settings, network parameters, or service configuration without authorization.

Expected outcome: The bed and facility system have the correct approved communication configuration.

### 8. Test the Complete Communication Path

After correcting an external issue:

- Initiate an approved nurse-call test.
- Confirm that the receiving station receives the call.
- Verify call identification and location where supported.
- Test applicable bed-status or remote alarm reporting.
- Confirm that the receiving system displays the expected information.
- Coordinate acknowledgment with clinical staff.

Expected outcome: Communication reaches the intended destination accurately and reliably.

Troubleshooting can stop when the complete affected communication path is verified.

## If the Problem Persists

If power, external cables, room interfaces, authorized configuration, and known-good comparisons have been checked, common external causes have been ruled out.

Possible service-level categories include the bed communication interface, facility nurse-call infrastructure, gateway configuration, network connectivity, or system integration.

The affected equipment should be:

- Removed from service and labeled Out of Service when required communication functions cannot be safely maintained.
- Sent for qualified repair or bench evaluation if the fault follows the bed.
- Evaluated using Hillrom documentation and approved test equipment.
- Repaired or configured only by qualified personnel.
- Escalated to Facilities, IT, nurse-call support, or the integration vendor when the fault follows the infrastructure.
- Returned to service only after successful end-to-end communication verification.

A working local button does not establish that the receiving station received the call.

## Clinical Use Tip

Always confirm nurse-call and bed-status messages at the receiving station rather than relying only on local bed indicators.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Reliable bed communication requires verification of both the local device and the receiving infrastructure. Maintain alternate patient communication, check cables and connections before assuming internal failure, escalate appropriately, and document end-to-end test results.

That is successful troubleshooting.
