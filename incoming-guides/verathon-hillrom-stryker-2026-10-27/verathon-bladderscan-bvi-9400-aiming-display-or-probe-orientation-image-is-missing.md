---
schemaVersion: 1
title: "Verathon BladderScan BVI 9400 Bladder Scanner - Aiming Display or Probe Orientation Image Is Missing"
issueTitle: "Aiming Display or Probe Orientation Image Is Missing"
description: "Troubleshoots a missing aiming or orientation display caused by scan state, probe connection, positioning, controls, or an external hardware problem."
assetType: "Bladder Scanner"
manufacturer: "Verathon"
model: "BladderScan BVI 9400"
slug: "verathon-bladderscan-bvi-9400-aiming-display-or-probe-orientation-image-is-missing"
dateAdded: "2026-10-27"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the BladderScan BVI 9400 completed scans but the probe aiming/orientation image was not displayed."
  cause: "Clinical Engineering found the probe connection was not fully seated, causing intermittent probe communication during the scan workflow."
  resolution: "Clinical Engineering reseated the probe connection, inspected the cable and connector, completed repeated test scans with normal aiming display operation, and returned the scanner to service."
helpfulDetails:
  - "Whether the aiming image was always or intermittently missing"
  - "Scan screen or operating state when the problem occurred"
  - "Probe and cable condition"
  - "Probe connector condition"
  - "Results after reseating the probe"
  - "Known-good comparison results"
  - "Display behavior during startup"
  - "Settings observed"
  - "Results of repeated test scans"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots a missing aiming or orientation display caused by scan state, probe connection, positioning, controls, or an external hardware problem.

## Step-by-Step Troubleshooting
### 1. Protect the Patient and Maintain Clinical Workflow

Do not continue relying on the BladderScan BVI 9400 if the missing aiming information prevents the operator from confidently positioning the probe or obtaining a reliable bladder measurement. Move clinical use to another verified bladder scanner if needed.

Inspect the scanner and probe for obvious impact damage, fluid intrusion, cracked housings, or damaged cables before further testing.

**Expected outcome:** The patient is not dependent on questionable scan results, and the scanner is safe for external troubleshooting. If physical damage or contamination creates a safety concern, remove the device from service and stop troubleshooting.

### 2. Confirm the Exact Reported Condition

Ask staff whether the aiming/orientation image is:

- Missing for every scan
- Missing only before or after acquisition
- Intermittent
- Replaced by another screen or message
- Associated with otherwise normal volume measurements

Reproduce the complaint without using the device for patient-care decisions.

**Expected outcome:** The missing display condition is confirmed and its timing within the scan workflow is understood. If the display appears normally and repeated test scans function correctly, document the findings and troubleshooting can stop.

### 3. Verify Normal Startup and Display Operation

Power the unit on normally and observe the complete startup sequence. Verify that the main display is readable and that other graphics, menus, text, and screen elements appear normally.

A broader display problem may indicate that the complaint is not limited to the aiming image.

**Expected outcome:** The scanner starts normally and general display functions are intact. If the entire display is abnormal, address the broader display problem rather than treating this as an aiming-image-only issue.

### 4. Inspect the Probe and Probe Connection

Inspect the probe, cable, strain relief, and external connector for:

- Loose connection
- Bent or damaged connector features
- Pinched or cut cable insulation
- Contamination
- Evidence of repeated pulling or twisting

Disconnect and reconnect the probe only as permitted by normal external service handling, ensuring the connection is fully seated.

**Expected outcome:** The probe connection is secure and externally undamaged. If reseating the connection restores the aiming display consistently, verify repeated operation and troubleshooting can stop.

### 5. Verify the Scanner Is in the Correct Scan State

Confirm that the unit is in its normal scanning workflow rather than a review, settings, saved-exam, or other non-scanning screen.

Operate the normal controls through a test scan and observe when the orientation or aiming information should become available.

Do not enter unauthorized service menus or alter unrelated configuration.

**Expected outcome:** The device reaches its normal scan state and the expected aiming/orientation information appears. If normal workflow restores the display consistently, troubleshooting can stop after functional verification.

### 6. Check Probe Positioning and Scan Technique During a Controlled Test

Using an appropriate test setup or nonclinical verification method, hold the probe in a stable orientation and initiate a scan. Avoid unusual probe angles, movement, or incomplete probe contact that could make normal orientation information difficult to interpret.

This step distinguishes a missing display from a positioning-related presentation problem.

**Expected outcome:** Orientation information appears consistently during properly performed test scans. If it does, verify repeated scans and return the unit to service only after satisfactory functional testing.

### 7. Check Controls and User-Accessible Settings

Review normal user-accessible settings that could affect display presentation. Verify no obvious setting or screen state is suppressing or changing the expected scan display.

Do not change configuration simply to experiment. Record existing settings before making any authorized correction.

**Expected outcome:** User-accessible settings are appropriate and the aiming display operates normally. If an authorized settings correction resolves the problem, repeat functional testing and troubleshooting can stop.

### 8. Compare With a Known-Good Compatible Probe or Unit When Available

If approved by your facility and compatible equipment is available, compare operation using a known-good compatible probe or compare the suspect probe on another appropriate BVI 9400.

Do not interchange accessories unless compatibility is established.

**Expected outcome:** The comparison determines whether the symptom follows the probe or remains with the scanner. If a known-good approved accessory restores normal operation, replace the defective accessory and complete final verification.

### 9. Perform Final Functional Verification

After any correction, perform multiple controlled scans and verify:

- The aiming/orientation display appears consistently
- Probe movement is represented normally
- The display remains stable
- Scans complete normally
- No new faults appear

**Expected outcome:** The aiming display works consistently through repeated test scans. If all checks pass, the device may be returned to service according to facility procedure and troubleshooting can stop.

### 10. Escalate if the Display Remains Missing

If the aiming/orientation image remains absent after external connections, probe condition, workflow, positioning, controls, and accessible settings have been verified, do not proceed into internal display electronics or probe circuitry without appropriate manufacturer service documentation.

**Expected outcome:** An unresolved device is removed from clinical use and routed for qualified service evaluation.

## If the Problem Persists
Common external causes have been ruled out. The remaining possibilities may involve the probe assembly, display subsystem, scanner electronics, stored configuration, or another service-level condition that cannot be confirmed through safe external troubleshooting.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

After repair, verify normal startup, probe recognition, aiming/orientation presentation, scan completion, and overall functional performance before returning the unit to clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip
Do not base a clinical bladder-volume decision on a scan when missing orientation information prevents confidence in correct probe positioning.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Protect the patient first, then verify the scan workflow, probe connection, positioning, controls, and settings before assuming an internal failure. Escalate unresolved faults appropriately and document the complaint, confirmed cause, corrective action, and final verification clearly.

That is successful troubleshooting.
