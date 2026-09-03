---
schemaVersion: 1
title: "Zimmer Biomet A.T.S. 4000 Pneumatic Tourniquet System - IVRA Cuff Lockout or Dual-Cuff Switching Problem"
issueTitle: "IVRA Cuff Lockout or Dual-Cuff Switching Problem"
description: "Troubleshoots dual-cuff control, switching, or lockout problems involving cuff connections, channel selection, controls, setup, and device-level interlock functions."
assetType: "Pneumatic Tourniquet System"
manufacturer: "Zimmer Biomet"
model: "A.T.S. 4000"
slug: "zimmer-biomet-ats-4000-ivra-cuff-lockout-or-dual-cuff-switching-problem"
dateAdded: "2026-09-03"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that the A.T.S. 4000 would not switch control between the two connected cuffs during setup."
  cause: "Clinical Engineering found one cuff hose connected incompletely, preventing normal operation of that channel."
  resolution: "Reseated and inspected both cuff hoses and verified normal independent channel operation and dual-cuff switching during functional testing."
helpfulDetails:
  - "Exact lockout or status message"
  - "Which cuff or channel was affected"
  - "Hose and port assignments"
  - "Cuff and hose condition"
  - "Control response"
  - "Whether each channel worked independently"
  - "Known-good accessory results"
  - "Setup observed"
  - "Functional verification results"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots dual-cuff control, switching, or lockout problems involving cuff connections, channel selection, controls, setup, and device-level interlock functions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Before Investigating Cuff Switching
Do not troubleshoot an unreliable IVRA or dual-cuff control condition while the patient depends on the affected cuff sequence. Follow the clinical contingency process and use a verified alternate system when required.
**Expected outcome:** Patient safety and intended vascular control are maintained independently of the affected device.

### 2. Confirm the Exact Reported Behavior
Determine whether a cuff will not inflate, will not deflate, cannot be selected, remains locked out, or switching between cuffs does not behave as expected. Record the displayed status and which cuff or channel is involved.
**Expected outcome:** The specific switching or lockout behavior is clearly defined.

### 3. Verify Both Cuff Connections
Confirm each cuff hose is connected to the intended port and fully seated. Check that connections have not been crossed, left partially engaged, or placed under tension.
**Expected outcome:** Both cuff circuits are correctly and securely connected.

### 4. Inspect Both Cuffs and Hoses
Examine the complete accessible pneumatic path for damaged fittings, leaks, kinks, compressed hoses, or visibly compromised cuffs.
**Expected outcome:** Both external pneumatic circuits are intact and unobstructed.

### 5. Verify Normal Control Response
Confirm the relevant touchscreen or control inputs respond normally and that the intended cuff selection can be made through standard operator-accessible controls. Do not bypass lockouts or defeat safety interlocks.
**Expected outcome:** Controls respond normally and safety-related lockout behavior is not being intentionally overridden.

### 6. Review the Observed Setup Without Changing Restricted Configuration
Confirm the device is being used in the intended clinical configuration and that the complaint is not caused by an incorrect visible setup or channel selection. Do not access unauthorized configuration or service menus.
**Expected outcome:** The normal operating setup is appropriate for the intended dual-cuff function.

### 7. Test With Known-Good External Components
With the device removed from patient use, substitute known-good compatible cuffs and hoses as necessary to determine whether the condition follows an external component.
**Expected outcome:** Normal switching with known-good accessories isolates the issue to the original cuff or hose.

### 8. Verify Each Channel Individually
Under controlled bench conditions, verify that each channel can perform normal external inflation and deflation functions independently before evaluating switching behavior.
**Expected outcome:** Both channels operate normally on their own. A single-channel failure should be addressed before further switching evaluation.

### 9. Perform Controlled Dual-Cuff Functional Verification
Using appropriate manufacturer documentation and an approved test setup, verify that the normal dual-cuff controls and permitted interlocks function correctly without bypassing safety features.
**Expected outcome:** Cuff selection, permitted switching, indicators, and alarms behave normally. Troubleshooting can stop after successful verification.

### 10. Escalate Persistent Lockout or Switching Failure
If correct external setup and known-good accessories do not restore normal behavior, the condition has exceeded safe external troubleshooting.
**Expected outcome:** The A.T.S. 4000 is removed from service and sent for qualified bench evaluation.

## If the Problem Persists

External cuffs, hoses, connections, control inputs, and basic setup have been ruled out. Remaining causes may involve an internal safety interlock, control logic, pneumatic channel, configuration, sensing, or other service-level condition.

Remove the system from service, label it **Out of Service**, and evaluate it using appropriate Zimmer Biomet service documentation and approved test equipment. Do not bypass safety lockouts or perform unauthorized internal modifications.

Before return to service, verify both cuffs, both channels, applicable interlocks, alarms, indicators, inflation, and deflation functions.

## Clinical Use Tip

Never bypass or defeat a tourniquet safety lockout in order to continue an IVRA or dual-cuff procedure.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Exact lockout or status message
- Which cuff or channel was affected
- Hose and port assignments
- Cuff and hose condition
- Control response
- Whether each channel worked independently
- Known-good accessory results
- Setup observed
- Functional verification results
- Final device status

## Final Thought

Dual-cuff and IVRA problems require special attention to patient safety and system interlocks. Verify external setup first, never defeat protective functions, and escalate unresolved switching or lockout behavior for qualified service.

That is successful troubleshooting.
