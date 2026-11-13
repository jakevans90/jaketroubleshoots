---
schemaVersion: 1
title: "ICU Medical Plum Duo Infusion Pump - Alarm Speaker, Status Light, or Nurse-Call Output Fails"
issueTitle: "Alarm Speaker, Status Light, or Nurse-Call Output Fails"
description: "Troubleshoots failed local or remote alarm annunciation caused by settings, connections, external infrastructure, accessories, or pump hardware."
assetType: "Infusion Pump"
manufacturer: "ICU Medical"
model: "Plum Duo"
slug: "icu-medical-plum-duo-alarm-speaker-status-light-or-nurse-call-output-fails"
dateAdded: "2026-11-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that pump alarms sounded locally but did not appear through the room nurse-call connection."
  cause: "Clinical Engineering found the external nurse-call cable intermittently open near the connector."
  resolution: "Replaced the defective cable and verified alarm activation locally and at the nurse-call receiving station."
helpfulDetails:
  - "Failed alarm function"
  - "Alarm test performed"
  - "Alarm-volume setting"
  - "Speaker result"
  - "Status-light result"
  - "Nurse-call cable condition"
  - "Known-good cable result"
  - "Known-good room/interface result"
  - "Receiving station response"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots failed local or remote alarm annunciation caused by settings, connections, external infrastructure, accessories, or pump hardware.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Provide Alternate Alarm Coverage
Do not leave a patient dependent on an infusion pump whose required audible, visual, or remote alarm path is unreliable. Transfer therapy or provide another verified alarm method until the pump is evaluated.

**Expected outcome:** Clinicians retain reliable notification of infusion alarms.

### 2. Confirm Which Alarm Function Failed
Determine whether the problem affects the speaker, status light, nurse-call output, or multiple alarm paths. Identify whether the failure occurs during startup testing, a user-accessible test, or a genuine alarm condition.

**Expected outcome:** The failed annunciation path is clearly identified.

### 3. Verify Basic Pump Operation
Confirm normal startup, responsive controls, and absence of other system faults.

**Expected outcome:** The pump is otherwise operational and stable enough for alarm testing.

### 4. Check Permitted Alarm Settings
Review user-accessible alarm-volume and related configuration settings without entering unauthorized service modes. Confirm the speaker has not been set or configured in a way that explains the complaint.

**Expected outcome:** Alarm settings are appropriate for testing.

If correcting an authorized setting restores normal alarm behavior, verify the complete alarm path before return to service.

### 5. Test Local Audible and Visual Alarms
Using an approved functional test, verify the pump produces the expected audible and visual alarm indications.

**Expected outcome:** The speaker and status light respond consistently during a valid alarm condition.

If either local indicator fails, remove the device from service.

### 6. Inspect the Nurse-Call Cable and Connection
If remote nurse call is the issue, inspect the external cable, connector, adapter, and pump port for looseness, damage, bent contacts, contamination, or strain.

**Expected outcome:** The external nurse-call connection is secure and undamaged.

### 7. Use a Known-Good Nurse-Call Cable or Test Fixture
Substitute a verified compatible cable or approved test fixture.

**Expected outcome:** The nurse-call output activates correctly with the known-good connection.

If the known-good cable resolves the issue, replace or remove the defective external cable from service.

### 8. Compare With Another Pump at the Same Nurse-Call Point
When practical, connect a verified pump to the same approved nurse-call interface.

**Expected outcome:** The infrastructure responds normally to the known-good pump.

If multiple pumps fail at the same location, escalate to the appropriate nurse-call or facilities support team.

### 9. Test the Suspect Pump on a Known-Good Interface
Move the pump to a verified nurse-call test point or approved fixture and repeat testing.

**Expected outcome:** The pump activates the remote alarm path correctly.

If it fails on a known-good interface, the device requires further service evaluation.

### 10. Complete Final Alarm Verification
Verify local audible alarm, visual status indication, and nurse-call output where equipped and required. Confirm restoration at the receiving nurse-call system when testing the remote path.

**Expected outcome:** All required alarm paths operate correctly from pump to receiving endpoint.

## If the Problem Persists

If settings, cables, connectors, test fixtures, and receiving infrastructure have been verified, a persistent alarm speaker, status light, or nurse-call failure may involve internal annunciator hardware, output circuitry, configuration, or another service-level fault.

The pump should be:

- Removed from service
- Labeled **Out of Service**
- Sent for bench evaluation
- Evaluated using approved ICU Medical procedures and test equipment
- Repaired or configured only by qualified personnel
- Fully alarm-tested before return to service

A pump that cannot reliably alert caregivers should not be returned to clinical use.

## Clinical Use Tip

When nurse call is involved, verify the complete path from the pump alarm through the receiving station rather than testing only the pump connector.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Alarm troubleshooting must verify both the local annunciators and any external communication path. Check configuration, cables, and infrastructure before assuming pump hardware failure, and never return a device with unreliable alarm notification to service.

That is successful troubleshooting.
