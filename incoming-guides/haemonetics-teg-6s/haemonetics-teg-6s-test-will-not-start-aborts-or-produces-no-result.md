---
schemaVersion: 1
title: "Haemonetics TEG 6s Viscoelastic Hemostasis Analyzer - Test Will Not Start, Aborts, or Produces No Result"
issueTitle: "Test Will Not Start, Aborts, or Produces No Result"
description: "Troubleshoots assay startup, aborted testing, missing results, cartridge, sample, software, power, and workflow conditions before service-level repair is considered."
assetType: "Viscoelastic Hemostasis Analyzer"
manufacturer: "Haemonetics"
model: "TEG 6s"
slug: "haemonetics-teg-6s-test-will-not-start-aborts-or-produces-no-result"
dateAdded: "2026-09-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that TEG 6s tests would begin but abort before producing a result."
  cause: "Clinical Engineering found intermittent cartridge seating caused by debris in the accessible loading area."
  resolution: "Cleaned the accessible cartridge area using approved practices, verified repeated successful cartridge recognition and test initiation, and returned the analyzer to service after functional verification."
helpfulDetails:
  - "Exact displayed message."
  - "Stage where the test stopped."
  - "Cartridge type and lot."
  - "Sample condition."
  - "Number of failed attempts."
  - "Known-good cartridge result."
  - "Local result availability."
  - "LIS or TEG Manager result availability."
  - "Power stability."
  - "Restart result."
  - "Final device status."
---
## What This Guide Helps With

Troubleshoots assay startup, aborted testing, missing results, cartridge, sample, software, power, and workflow conditions before service-level repair is considered.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Confirm the Failure

Do not rely on an analyzer that is aborting tests or failing to produce results when clinical decisions depend on timely coagulation data. Route testing to another verified analyzer or approved laboratory method as needed.

Determine:
- Whether the test never begins.
- Whether it begins and aborts.
- Whether the run appears complete but no result is displayed.
- Whether all assays or only one cartridge type is affected.
- Whether the failure is intermittent or repeatable.

**Expected outcome:** The failure pattern is clearly established.

### 2. Review the Displayed Message or Test Status

Record the exact message, screen state, or stage at which the test stops.

Do not paraphrase an error if exact wording is available.

**Expected outcome:** A specific failure point is documented and can be correlated with later troubleshooting.

### 3. Verify Cartridge Condition and Seating

Remove and inspect the cartridge for damage, contamination, incorrect type, or poor seating. Install an appropriate known-good cartridge.

**Expected outcome:** The analyzer recognizes and accepts the known-good cartridge. If the test starts and completes normally, the cartridge was the likely external cause.

### 4. Verify Sample Condition and Loading

Check that the specimen is suitable, adequate, and transferred correctly using approved laboratory practice.

Look for:
- Insufficient specimen.
- Visible clotting.
- Bubbles.
- Leakage.
- Incomplete sample transfer.

**Expected outcome:** The sample is appropriate and loads normally. Correct an evident sample issue before further analyzer troubleshooting.

### 5. Confirm Required Test Information Is Complete

Verify that required test setup information has been entered or acquired correctly, including patient or specimen identification where applicable.

Do not alter protected configuration settings solely to make the assay start.

**Expected outcome:** No missing workflow information is preventing test initiation.

### 6. Verify Analyzer Power and Stability

Confirm:
- Power connection is secure.
- Analyzer remains powered without flicker or restart.
- No unrelated system error is present.
- Startup completed normally.

If appropriate, perform a controlled normal restart.

**Expected outcome:** The analyzer reaches a stable ready condition.

### 7. Check for Software or Interface Delays

If the analyzer appears responsive but a test will not progress, confirm the local interface is not frozen and that required screens respond normally.

If result transfer is delayed but the analyzer itself shows a completed result, treat communication separately rather than assuming the assay failed.

**Expected outcome:** Local analyzer operation and external result transmission are distinguished.

### 8. Repeat With a Known-Good Test Setup

When laboratory policy permits, use an appropriate known-good cartridge and suitable verification material or specimen.

**Expected outcome:** A complete test sequence progresses from cartridge recognition through result generation without aborting.

### 9. Verify Result Availability

Confirm the completed result appears where expected on the analyzer. If local results are present but absent from LIS or TEG Manager, the analyzer test itself may be functioning and the problem should be handled as a communication issue.

**Expected outcome:** The analyzer generates and displays a valid local result. If so, test-generation troubleshooting can stop.

### 10. Escalate Persistent Aborts or Missing Results

If multiple appropriate cartridges and samples fail, or the analyzer repeatedly aborts without an external cause, remove it from service.

**Expected outcome:** The analyzer is prevented from producing potentially unreliable clinical testing until qualified evaluation is completed.

## If the Problem Persists

External causes involving cartridge condition, sample quality, setup information, power stability, software responsiveness, and external result interfaces have been ruled out. The remaining issue may involve internal test control, cartridge interface, software, sensing, processing, or another service-level function.

The device should be:
- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Complete appropriate functional and return-to-service testing before release.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A locally completed result and a result missing from the LIS are different failures; confirm where the testing path actually stops before removing the analyzer unnecessarily.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Exact displayed message.
- Stage where the test stopped.
- Cartridge type and lot.
- Sample condition.
- Number of failed attempts.
- Known-good cartridge result.
- Local result availability.
- LIS or TEG Manager result availability.
- Power stability.
- Restart result.
- Final device status.

## Final Thought

Separate test-generation failures from communication failures, rule out cartridge and specimen problems first, verify successful operation before return to service, and escalate recurrent aborts rather than accepting intermittent performance.

That is successful troubleshooting.
