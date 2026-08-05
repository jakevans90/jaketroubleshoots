---
schemaVersion: 1
title: "Masimo Rad-97 Pulse Oximeter - Alarm Limits Or Profile Settings Will Not Save"
issueTitle: "Alarm Limits Or Profile Settings Will Not Save"
description: "Settings that revert or fail to save because of profile restrictions, user permissions, temporary changes, synchronization, software, or configuration storage faults."
assetType: "Pulse Oximeter"
manufacturer: "Masimo"
model: "Rad-97"
slug: "masimo-rad-97-alarm-limits-or-profile-settings-will-not-save"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that customized alarm limits returned to previous values after restarting the Rad-97."
  cause: "Clinical Engineering found that staff were making temporary patient-level changes without saving them to the authorized department profile."
  resolution: "Reviewed the approved profile workflow with department leadership, restored the correct profile, verified limit retention and alarm operation after restart, and returned the device to service."
helpfulDetails:
  - "Exact setting or alarm limit"
  - "When the setting reverted"
  - "Active profile"
  - "User access level"
  - "Save or confirmation messages"
  - "Patient discharge or profile-change behavior"
  - "Network or central configuration control"
  - "Comparison device results"
  - "Retention after restart"
  - "Final alarm test results"
---

## What This Guide Helps With

Settings that revert or fail to save because of profile restrictions, user permissions, temporary changes, synchronization, software, or configuration storage faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Verify Current Alarm Coverage

Do not leave a patient connected to a monitor with unverified alarm limits or an incorrect profile.

Use another verified monitor or have clinical staff confirm appropriate active limits before Clinical Engineering begins testing.

Expected outcome: The patient remains protected by verified alarm settings.

### 2. Confirm Which Setting Will Not Save

Identify the exact alarm limit, profile, display option, or configuration item that changes or reverts.

Determine whether it reverts immediately, after leaving the menu, after patient discharge, after profile change, or after restart.

Expected outcome: The save failure is reproduced and its timing is documented.

### 3. Verify User Permissions and Access Level

Confirm that the person attempting the change has the appropriate authorized access.

Do not bypass access controls or use restricted service credentials.

Expected outcome: The setting is being changed through an authorized user level.

### 4. Determine Whether the Change Is Temporary by Design

Compare the workflow with the approved facility configuration and another Rad-97.

Some patient-specific alarm changes may be temporary and may reset when a new patient, profile, or care area is selected.

Expected outcome: Expected temporary behavior is distinguished from an actual save failure.

### 5. Verify the Active Profile

Confirm that the correct profile is selected and that the requested alarm limits are permitted under that profile.

Do not modify protected profile parameters without authorization from the responsible clinical and systems owners.

Expected outcome: The correct approved profile is active.

### 6. Save Through the Normal Approved Workflow

Repeat the change using the complete normal save, confirmation, or profile-selection process.

Observe for warning messages or prompts indicating that the change was not accepted.

Expected outcome: The setting remains after leaving and reopening the menu. If so, troubleshooting can stop after further verification.

### 7. Check for Central or Network Configuration Control

Determine whether a connected central system or configuration-management process automatically applies approved settings.

Temporarily evaluate in coordination with the system owner rather than disconnecting or disabling managed configuration without authorization.

Expected outcome: A network-managed configuration source is identified or ruled out.

### 8. Restart and Verify Retention

With the monitor removed from patient use, restart it and confirm whether the authorized saved profile or setting remains.

Expected outcome: The approved configuration is retained after restart.

### 9. Compare With Another Approved Rad-97

Compare software behavior, profile naming, accessible settings, and retention with a known-good unit in the same department.

Do not copy settings informally or alter protected configurations.

Expected outcome: The problem is isolated to a workflow, profile, network source, or the affected monitor.

### 10. Verify Alarm Operation

Use approved test methods to confirm that the displayed alarm limits are active, alarms occur at the expected thresholds, and audible and visual indications function correctly.

Expected outcome: The saved settings are operational, not merely displayed.

### 11. Escalate Persistent Configuration Loss

If authorized settings repeatedly revert or cannot be retained after correct workflow, profile, restart, and network checks, remove the monitor from clinical use.

Expected outcome: The device is labeled Out of Service and sent for qualified configuration or repair evaluation.

## If the Problem Persists

Common causes involving user permissions, temporary patient-specific changes, active profiles, incomplete save workflow, and centrally managed configuration have been ruled out.

The remaining cause may involve configuration storage, software, profile corruption, network management, or another service-level condition. Remove the Rad-97 from service, label it Out of Service, and send it for bench evaluation using current manufacturer documentation and approved tools.

Only authorized personnel should repair or change alarm profiles. Complete alarm-limit retention, physiological alarm, technical alarm, and restart testing before return to service.

## Clinical Use Tip

Always verify the displayed alarm limits after selecting a profile or starting a new patient; do not assume previously entered limits were retained.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Unverified alarm settings are a patient-safety risk. Confirm profiles, permissions, and managed configuration before assuming failure, escalate recurring setting loss, and document functional alarm verification.

That is successful troubleshooting.
