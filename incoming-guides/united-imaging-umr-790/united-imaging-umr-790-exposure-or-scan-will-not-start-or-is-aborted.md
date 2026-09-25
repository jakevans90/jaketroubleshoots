---
schemaVersion: 1
title: "United Imaging uMR 790 MRI System - Exposure or Scan Will Not Start or Is Aborted"
issueTitle: "Exposure or Scan Will Not Start or Is Aborted"
description: "Troubleshoots MRI scans that will not begin or terminate unexpectedly because of setup, interlocks, coils, communication, patient motion, or system readiness."
assetType: "MRI System"
manufacturer: "United Imaging"
model: "uMR 790"
slug: "united-imaging-umr-790-exposure-or-scan-will-not-start-or-is-aborted"
dateAdded: "2026-09-25"
taxonomyMode: "reuse"
ccr:
  complaint: "MRI staff reported that the uMR 790 scan repeatedly aborted immediately after acquisition began."
  cause: "Clinical Engineering found an intermittently seated external coil connection that caused the selected coil to lose readiness."
  resolution: "The connection was corrected, the coil remained recognized, and a controlled scan completed without interruption before return to service."
helpfulDetails:
  - "Exact abort message"
  - "Point in the scan when failure occurs"
  - "Protocol or sequence involved"
  - "Coil and accessory setup"
  - "Patient and table position"
  - "Whether the failure is reproducible"
  - "Cooling or environmental warnings"
  - "Known-good accessory results"
  - "Test scan result"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots MRI scans that will not begin or terminate unexpectedly because of setup, interlocks, coils, communication, patient motion, or system readiness.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Repeated Scan Attempts
Do not repeatedly attempt an unreliable examination while a patient depends on the system.

Assess the patient, remove them from the scanner if necessary, and arrange continuity of care if the examination cannot proceed safely.

**Expected outcome:** The patient is safe and troubleshooting can proceed without unnecessary repeated scan attempts.

### 2. Confirm When the Scan Fails
Determine whether the scan:
- Never starts
- Stops during preparation
- Begins and immediately aborts
- Fails only on one sequence
- Fails with one coil or accessory
- Aborts intermittently

Record the exact displayed message or sequence of events.

**Expected outcome:** The failure point is identified and can guide external troubleshooting.

### 3. Verify Overall System Readiness
Confirm the scanner, workstation, table position, selected hardware, and acquisition system are all showing normal readiness.

Resolve any obvious startup or accessory-recognition issue before testing another scan.

**Expected outcome:** No general readiness fault remains. If restoring readiness allows the scan to start normally, verify operation and stop.

### 4. Check Patient and Table Positioning
Verify:
- Patient position is appropriate
- Table is in the expected location
- Coils and accessories are properly positioned
- Cables are routed safely
- No object is obstructing table movement or setup

**Expected outcome:** Positioning and setup are correct. If correcting the setup allows scanning to proceed, confirm successful acquisition and stop.

### 5. Inspect Coil and Accessory Connections
Check the active coil and other normal external accessories for secure connection and visible damage.

If appropriate, reseat connections or compare with a known-good compatible accessory.

**Expected outcome:** Required acquisition accessories remain recognized and stable. If a faulty accessory is isolated, remove it from service and verify the scanner with a known-good component.

### 6. Review Normal Exam and Sequence Selections
Confirm the intended protocol or sequence has been selected appropriately and no obvious operator-entered parameter or workflow selection is preventing execution.

Do not alter protected or service-level configuration to force a sequence to run.

**Expected outcome:** The examination setup is valid. If correcting a normal workflow selection resolves the problem, complete scan verification and stop.

### 7. Check for Patient Motion or Communication Events
Determine whether the abort corresponds with:
- Patient movement
- Patient emergency request
- Communication loss
- Table movement
- Accessory disconnection
- Staff intentionally stopping the scan

**Expected outcome:** Any external reason for the abort is identified. If corrected and the scan subsequently completes normally, troubleshooting can stop.

### 8. Check Environmental and Cooling Status
Look for active temperature, cooling, ventilation, or equipment-room issues that might cause the system to inhibit or terminate scanning.

Do not continue scanning through an overtemperature or cooling-related condition.

**Expected outcome:** Environmental support is normal. If a facility issue is found, keep the MRI out of service until corrected.

### 9. Perform a Controlled Test Scan
After correcting an identified external cause, use an approved test object or appropriate nonpatient verification procedure.

Confirm:
- Scan begins normally
- Acquisition continues without aborting
- Images reconstruct as expected
- No recurring system fault is present

**Expected outcome:** A controlled scan completes successfully. Troubleshooting can stop.

### 10. Escalate Repeated or Unexplained Scan Aborts
If scan setup, patient positioning, external accessories, system readiness, and environment are correct but scanning continues to fail, stop troubleshooting.

**Expected outcome:** The system is removed from clinical service pending service evaluation.

## If the Problem Persists

External causes have been ruled out. Remaining categories may include RF, gradient, acquisition, control, cooling, timing, internal communication, or software/configuration problems requiring qualified MRI service.

The device should be:
- Removed from service
- Labeled **Out of Service**
- Sent for repair or service evaluation
- Evaluated using United Imaging documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not repeatedly attempt failed scans or enter unsupported service functions.

Knowing when to stop external troubleshooting is proper troubleshooting. Successful service must be followed by appropriate imaging and operational verification before return to clinical use.

## Clinical Use Tip

If a scan repeatedly aborts without an obvious patient-related reason, move the patient to a safe alternative plan rather than repeatedly restarting the examination.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

A scan abort should first be treated as a safety and workflow problem, then traced through positioning, accessories, readiness, and environment before internal failure is suspected. Verify a successful controlled scan and document the event clearly.

That is successful troubleshooting.
