---
schemaVersion: 1
title: "Eitan Medical Sapphire Infusion Pump - Drug Library, Protocol, or Configuration Will Not Load"
issueTitle: "Drug Library, Protocol, or Configuration Will Not Load"
description: "Troubleshoots failed drug-library, protocol, or configuration loading caused by file selection, connectivity, authorization, device status, or configuration workflow problems."
assetType: "Infusion Pump"
manufacturer: "Eitan Medical"
model: "Sapphire"
slug: "eitan-medical-sapphire-drug-library-protocol-or-configuration-will-not-load"
dateAdded: "2026-09-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Pharmacy reported a Sapphire pump would not receive the current approved drug-library update."
  cause: "Clinical Engineering found the pump was connected to an inactive network port during the update attempt."
  resolution: "Moved the pump to a verified active connection, completed the approved library transfer, and confirmed the expected configuration loaded successfully."
helpfulDetails:
  - "Exact update or configuration symptom"
  - "Displayed message"
  - "Current and expected configuration version"
  - "Device group or assignment"
  - "AC or battery status"
  - "Connection method used"
  - "Network port or cable tested"
  - "Whether other pumps were affected"
  - "Result of approved retry"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots failed drug-library, protocol, or configuration loading caused by file selection, connectivity, authorization, device status, or configuration workflow problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Approved Configuration
Do not alter a pump's clinical configuration or drug library while it is supporting active patient therapy.

If the pump cannot access required approved protocols, remove it from clinical use until the appropriate configuration is verified.

**Expected outcome:** No patient is exposed to an unverified or incomplete pump configuration.

### 2. Confirm the Exact Failure
Determine whether the issue involves:

- Drug library not present
- Protocol list missing
- Update will not begin
- Update starts but does not complete
- Pump rejects the configuration
- Expected version is not shown
- Only specific protocols are missing

Record any exact displayed message without interpreting undocumented codes.

**Expected outcome:** The configuration failure is clearly characterized.

### 3. Verify Device Identity and Intended Configuration
Confirm that the pump is the intended unit and belongs to the correct clinical environment or deployment group.

Do not load a library or configuration merely because another nearby pump uses it.

**Expected outcome:** The intended configuration target is confirmed. If the wrong device group or file was selected, correct the administrative workflow and verify the proper configuration.

### 4. Verify Pump Readiness
Confirm the pump is not actively infusing and is in the appropriate operational state for an authorized update.

Ensure adequate battery charge or reliable approved external power before beginning a configuration transfer.

**Expected outcome:** The pump is in a stable condition suitable for configuration work.

### 5. Check External Connection Method
If the update uses a network, cable, docking method, or approved accessory, inspect the external communication path.

Verify:

- Connections are secure
- Cables are undamaged
- Network access is available when required
- Approved interface accessories are being used

**Expected outcome:** The physical communication path is intact. If restoring the connection allows the update to complete, troubleshooting can stop.

### 6. Verify the Approved File or Assignment
Confirm that the intended library, protocol set, or configuration package is the currently approved version for the device according to the organization's controlled workflow.

Do not modify, rename, or manually manipulate configuration files to force acceptance.

**Expected outcome:** The correct approved configuration source is being used.

### 7. Compare With Another Device
When appropriate, determine whether another compatible Sapphire pump can receive or display the same approved configuration.

This helps separate a device-specific problem from a system-wide deployment problem.

**Expected outcome:** If multiple devices fail identically, investigate the configuration source, network, or deployment infrastructure rather than assuming an individual pump failure.

### 8. Retry Through the Approved Workflow
After correcting power, connectivity, or assignment issues, retry the library or configuration load using the organization's authorized process.

Do not use unauthorized service menus or configuration overrides.

**Expected outcome:** The transfer completes successfully and the expected library or configuration is present. If so, troubleshooting can stop after verification.

### 9. Verify the Loaded Configuration
Confirm that the pump displays the expected approved configuration, library, or protocol availability.

Perform required functional checks without altering clinical content.

**Expected outcome:** The correct approved configuration is present and the pump functions normally. If all verification passes, troubleshooting can stop.

### 10. Escalate Persistent Configuration Failure
If the correct approved configuration cannot be loaded despite verified power, connections, assignment, and authorized workflow, stop troubleshooting.

Do not bypass security, force unsupported files, or make undocumented configuration changes.

**Expected outcome:** The problem is escalated as a service, software, network, or configuration-management issue.

## If the Problem Persists

External connection, power, file-selection, assignment, and basic deployment issues have been ruled out. Remaining possibilities may involve pump software, network infrastructure, configuration compatibility, account permissions, server-side deployment, or another service-level condition.

The device should be:

- Removed from service if required clinical configuration is unavailable
- Labeled Out of Service when clinical deployment is not appropriate
- Sent for repair or bench evaluation when device-specific failure is suspected
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Verify the approved library or configuration and full pump functionality before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A pump that powers on normally is not necessarily ready for clinical use if its required approved drug library or protocol configuration is missing.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter; optional explanatory prose may follow. -->



## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Configuration problems require controlled troubleshooting because clinical settings and drug libraries affect patient safety. Verify the approved source, connectivity, assignment, and device state before escalating software or service-level concerns.

That is successful troubleshooting.
