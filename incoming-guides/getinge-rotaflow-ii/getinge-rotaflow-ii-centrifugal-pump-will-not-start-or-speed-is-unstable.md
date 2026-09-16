---
schemaVersion: 1
title: "Getinge ROTAFLOW II Extracorporeal Membrane Oxygenation (ECMO) System - Centrifugal Pump Will Not Start or Speed Is Unstable"
issueTitle: "Centrifugal Pump Will Not Start or Speed Is Unstable"
description: "Troubleshoots pump startup failure, unstable speed, pump-head installation, drive connection, control, power, and circuit-related external causes."
assetType: "Extracorporeal Membrane Oxygenation (ECMO) System"
manufacturer: "Getinge"
model: "ROTAFLOW II"
slug: "getinge-rotaflow-ii-centrifugal-pump-will-not-start-or-speed-is-unstable"
dateAdded: "2026-09-16"
taxonomyMode: "reuse"
ccr:
  complaint: "ECMO staff reported the ROTAFLOW II pump would start but the pump speed was unstable during setup."
  cause: "Clinical Engineering found the pump head was not fully seated in the drive interface."
  resolution: "Correctly seated the compatible pump head, verified stable pump startup and commanded speed on a test setup, completed functional checks, and returned the system to service."
helpfulDetails:
  - "Whether pump failed to start or varied after startup"
  - "Displayed alarm or message"
  - "AC or battery operation"
  - "Pump-head condition and installation"
  - "Drive-interface condition"
  - "Cable and connector inspection"
  - "Known-good pump-head test result"
  - "Abnormal sound or vibration"
  - "Commanded versus observed speed behavior"
  - "Final functional test results"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots pump startup failure, unstable speed, pump-head installation, drive connection, control, power, and circuit-related external causes.

## Step-by-Step Troubleshooting
### 1. Protect the Patient and Maintain ECMO Flow
Never troubleshoot unstable or unavailable ECMO pumping while a patient depends on that pump. Activate the established ECMO contingency process and maintain extracorporeal support using clinically approved backup equipment.

Clinical personnel must manage clamps, circuit transfers, pump-head changes, and patient-connected tubing.

**Expected outcome:** Continuous patient support is maintained while the questionable drive system is safely isolated for evaluation.

### 2. Confirm the Exact Pump Behavior
Determine whether the pump:
- Will not begin rotating
- Starts and immediately stops
- Runs but cannot maintain the selected speed
- Surges or varies unexpectedly
- Produces abnormal noise or vibration
- Generates a displayed alarm or warning

Record the displayed speed and circumstances when the problem occurs.

**Expected outcome:** The pump malfunction is clearly characterized and reproducible on a non-patient test setup.

### 3. Verify Console Power and Basic Operation
Confirm the console has stable AC power or an adequate approved battery source and has completed startup normally.

A console with unstable power can create apparent pump-drive problems.

**Expected outcome:** The console remains powered and stable. If correcting the power source restores consistent pump operation, proceed to final verification.

### 4. Inspect the Pump Head and Drive Interface
With the system safely out of patient use, inspect the pump head installation and accessible drive interface. Verify:
- Pump head is the appropriate compatible component
- It is fully seated in the drive
- No obvious obstruction or foreign material is present
- Housing is not cracked or deformed
- The drive interface is clean and undamaged

Do not force a pump head into the drive.

**Expected outcome:** The pump head is properly installed and mechanically secure. If reseating it restores normal operation, continue to functional verification.

### 5. Inspect the Circuit for External Mechanical Causes
On an appropriate test setup, check for external conditions that could affect rotation or apparent flow, such as:
- Kinked tubing
- Improper tubing routing
- Excessive tension on the pump head
- Pump-head or tubing deformation
- Circuit positioning that loads the pump assembly

Patient-connected circuit manipulation belongs to the clinical ECMO team.

**Expected outcome:** The circuit and pump head are positioned without external mechanical restriction.

### 6. Use a Known-Good Compatible Pump Head When Appropriate
If available and permitted by facility procedure, test the drive with a known-good compatible pump head in a non-patient setup.

Do not substitute disposable circuit components on an active ECMO patient solely for equipment troubleshooting.

**Expected outcome:** Stable operation with the known-good component indicates the original pump-head or setup should be evaluated or replaced according to clinical and manufacturer procedures.

### 7. Inspect Drive and Console Connections
Verify all accessible drive-unit connections are fully seated and undamaged. Inspect cables and connectors for:
- Bent contacts
- Pinching
- Cuts
- Strain
- Fluid contamination
- Loose engagement

**Expected outcome:** Drive connections are intact and secure. Correcting a loose connection restores stable operation when the connection was the cause.

### 8. Verify Speed Control Operation
On a safe test setup, adjust the speed control through an appropriate operating range and observe whether the displayed value responds smoothly and whether pump operation follows the commanded change.

Do not enter unauthorized calibration or service menus.

**Expected outcome:** Commanded pump speed changes smoothly and remains stable. Erratic control behavior requires service evaluation.

### 9. Perform Final Functional Verification
Verify the pump drive:
- Starts consistently
- Responds predictably to normal controls
- Holds commanded speed
- Has no abnormal noise or vibration
- Produces appropriate flow behavior on the approved test setup
- Generates required alarms or indications during applicable tests

**Expected outcome:** Pump-drive performance is stable and repeatable. Troubleshooting can stop after all required return-to-service tests pass.

### 10. Escalate Persistent Pump Instability
If pump rotation remains unavailable or unstable with proper installation, stable power, secure connections, and a known-good compatible setup, remove the equipment from service.

**Expected outcome:** Suspected drive, control, internal power, or electronic faults are evaluated by qualified service personnel rather than pursued through unsafe external troubleshooting.

## If the Problem Persists
External power, pump-head seating, circuit positioning, drive connections, and basic control causes have been ruled out. Remaining possibilities include an internal drive mechanism, motor-control system, feedback system, internal electronics, or other service-level failure.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate Getinge documentation and approved test equipment
- Repaired or configured only by qualified personnel

Following service, verify stable speed control, pump operation, alarms, monitoring, and other required safety functions before return to clinical use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
Any unexplained loss or instability of ECMO pump speed warrants immediate clinical backup action; never use repeated restarts as a substitute for reliable extracorporeal support.

## Work Order Documentation (CCR Method)
<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)
<!-- Helpful details come from front matter. -->

## Final Thought
Maintain patient circulation first, eliminate power, connection, installation, and pump-head causes methodically, verify stable operation before release, and escalate any unexplained pump instability.

That is successful troubleshooting.
