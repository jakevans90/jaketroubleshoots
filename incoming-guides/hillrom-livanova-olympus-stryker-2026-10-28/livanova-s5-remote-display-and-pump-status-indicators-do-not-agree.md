---
schemaVersion: 1
title: "LivaNova S5 Heart-Lung Machine - Remote Display and Pump Status Indicators Do Not Agree"
issueTitle: "Remote Display and Pump Status Indicators Do Not Agree"
description: "Troubleshoots disagreement between remote display information and pump status caused by connections, communication, configuration, display update, or component synchronization problems."
assetType: "Heart-Lung Machine"
manufacturer: "LivaNova"
model: "S5"
slug: "livanova-s5-remote-display-and-pump-status-indicators-do-not-agree"
dateAdded: "2026-10-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Perfusion reported that one S5 pump showed a running condition locally while the remote display continued to indicate that the pump was stopped."
  cause: "Clinical Engineering found the external communication cable at the remote display connection partially seated, causing intermittent status updates."
  resolution: "The cable was fully reseated and secured, and controlled start/stop testing confirmed matching pump status on the local and remote displays before return to service."
helpfulDetails:
  - "Pump position affected"
  - "Local status observed"
  - "Remote status observed"
  - "Whether the display was frozen or updating"
  - "Other pump channels affected"
  - "External cable and connector condition"
  - "Display power stability"
  - "Pump/display assignments"
  - "Known-good cable substitution"
  - "Alarm and status test results"
  - "Results before and after correction"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots disagreement between remote display information and pump status caused by connections, communication, configuration, display update, or component synchronization problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Use the Verified Local Pump Status

Conflicting pump indications can create a serious perfusion safety hazard.

Do not rely on a remote display whose information does not agree with directly verified pump operation. If the system is in clinical use, the perfusionist should use the verified primary/local pump information and established alternate monitoring until the discrepancy is resolved.

Do not disconnect active system components during patient support unless specifically directed by an approved clinical contingency procedure.

**Expected outcome:** Patient care is based only on verified pump information and the questionable remote indication is not used for clinical decisions.

### 2. Confirm Which Indications Disagree

Identify the exact discrepancy, such as:

- Pump running versus stopped
- Displayed pump speed
- Pump identity or position
- Direction of rotation
- Alarm or status indication
- Remote display frozen on an earlier value
- One pump incorrect while others agree
- All pump information incorrect

Compare the remote indication with direct observation and the primary control or local display.

**Expected outcome:** The affected status parameter and pump position are clearly identified.

### 3. Determine Whether the Remote Display Is Updating

Observe whether unrelated information on the remote display changes normally.

Check whether:

- The clock or other dynamic information changes
- Other pump values update
- Controls or pages respond normally
- The displayed value appears frozen
- Updates occur only intermittently

This helps distinguish a single-channel status problem from loss of the complete communication path.

**Expected outcome:** The problem is classified as a frozen display, intermittent communication issue, or disagreement limited to a particular pump/status value.

### 4. Inspect External Communication Connections

Once the system is safely available for technical evaluation, inspect external cables and connectors between the relevant system components.

Look for:

- Loose plugs
- Partially seated connectors
- Damaged cable jackets
- Bent or contaminated contacts
- Strain on connectors
- Incorrect connection points
- Evidence that equipment was recently moved or reconfigured

Reseat only connectors that are intended for normal external service access.

**Expected outcome:** External communication connections are secure and physically intact. If indications synchronize afterward, proceed to final verification.

### 5. Check Power and Status of the Remote Display

Verify that the remote display and associated external components have stable power and complete normal startup.

Look for:

- Intermittent power
- Rebooting
- Flickering
- Incomplete startup
- Unexpected blanking
- Abnormal external indicator behavior

If the display itself is unstable, address the power or display problem before interpreting pump-status discrepancies.

**Expected outcome:** The remote display remains powered and stable throughout testing.

### 6. Verify Pump and Display Assignments

Through normal authorized controls, confirm that pump identities and displayed assignments correspond to the actual physical pump positions.

A configuration or assignment mismatch may cause valid information from one pump to appear to represent another.

Do not alter restricted system configuration without approved documentation and authorization.

**Expected outcome:** Each displayed pump identity matches the intended physical pump and control channel.

### 7. Compare Multiple Pump Positions

Using a controlled test setup, compare local and remote indications for each available pump position.

Start and stop pumps individually as permitted and observe whether the corresponding remote indication changes correctly.

This helps determine whether the problem follows:

- One pump
- One connection
- One display field
- The entire remote interface

**Expected outcome:** Each tested pump produces the corresponding status change on both the local and remote displays.

### 8. Substitute Known-Good External Components Where Permitted

If the problem is isolated to an external communication cable or interchangeable accessory, substitute a known-good compatible component.

Do not interchange internal modules or open system enclosures as part of this external troubleshooting process.

**Expected outcome:** If synchronization is restored, the substituted external component identifies the likely cause.

### 9. Verify Alarm and Status Communication

In a controlled non-patient setup, verify relevant status transitions and applicable alarms through the complete intended display path.

Confirm that the remote display:

- Updates when pump state changes
- Identifies the correct pump
- Does not retain stale status
- Returns to the expected state after testing

**Expected outcome:** Local and remote indications remain synchronized during all tested status changes.

### 10. Stop and Escalate Any Persistent Disagreement

If remote and local pump indications still disagree, do not return the affected remote display function to clinical reliance.

A remote display that intermittently or consistently shows incorrect pump status must be treated as unreliable even if the pump itself operates correctly.

**Expected outcome:** The unreliable display or associated equipment is removed from service or clearly isolated from clinical use pending repair.

## If the Problem Persists

Common external causes involving cables, connectors, display power, channel assignment, and externally replaceable accessories have been ruled out.

Remaining possibilities may involve internal communication interfaces, system synchronization, display electronics, configuration data, software, or other service-level faults.

The affected equipment should be:

- Removed from service when the discrepancy could affect safe perfusion monitoring
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate LivaNova documentation and approved test equipment
- Configured or repaired only by qualified personnel
- Tested through the complete local-to-remote status path before return to service

Knowing when to stop troubleshooting a conflicting indication instead of assuming one display is correct is proper troubleshooting.

## Clinical Use Tip

When local and remote pump information disagree, the remote indication should not be used for clinical decision-making until the complete status path has been verified.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- rendered from front matter -->

## Final Thought

Conflicting pump indications must be treated as a safety issue because perfusion decisions depend on trustworthy status information. Verify the physical pump state, work through the external communication path logically, and escalate any disagreement that cannot be conclusively corrected and verified.

That is successful troubleshooting.
