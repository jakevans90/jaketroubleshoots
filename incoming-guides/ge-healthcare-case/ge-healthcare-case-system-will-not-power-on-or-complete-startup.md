---
schemaVersion: 1
title: "GE Healthcare CASE Stress Test System - System Will Not Power On or Complete Startup"
issueTitle: "System Will Not Power On or Complete Startup"
description: "CASE workstation does not power on, displays no normal startup activity, or fails to reach the operational application after power-up."
assetType: "Stress Test System"
manufacturer: "GE Healthcare"
model: "CASE"
slug: "ge-healthcare-case-system-will-not-power-on-or-complete-startup"
dateAdded: "2026-10-19"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the GE Healthcare CASE workstation would not power on for a scheduled stress study."
  cause: "Clinical Engineering found the workstation power connection loose at the approved power distribution unit."
  resolution: "Reseated the power connection, restarted the system, and verified normal CASE startup and ECG acquisition before returning the system to service."
helpfulDetails:
  - "Whether the workstation had any power indicators"
  - "Display status"
  - "Outlet or power-distribution equipment tested"
  - "Condition of power cord and connectors"
  - "Any startup message observed"
  - "External devices disconnected during testing"
  - "Results of controlled restart"
  - "ECG acquisition status after startup"
  - "Exercise-device communication status"
  - "Final device status"
---

## What This Guide Helps With
CASE workstation does not power on, displays no normal startup activity, or fails to reach the operational application after power-up.

## Step-by-Step Troubleshooting
### 1. Protect the Patient and Preserve Continuity of Care
Do not troubleshoot a CASE system during an active stress study if loss of ECG monitoring, exercise control, or emergency response capability could affect patient safety. Stop or transfer the study according to clinical protocol and provide alternate monitoring as required.

**Expected outcome:** No patient depends on the affected system while troubleshooting is performed. If alternate equipment is required, move the patient before continuing.

### 2. Confirm the Exact Startup Failure
Ask staff what occurred when the system was powered on. Determine whether there is no power at all, the workstation powers up without a display, startup stops before the CASE application loads, or a peripheral fails while the workstation remains operational. Observe the condition directly when possible.

**Expected outcome:** The failure is narrowed to power, workstation startup, display, application startup, or an attached peripheral. If the system starts normally and the reported condition cannot be reproduced, perform functional verification and stop troubleshooting.

### 3. Verify Facility Power
Confirm the system power cord is fully seated and connected to the intended receptacle or approved power distribution equipment. Inspect the cord and plug for damage. Verify the receptacle with an appropriate tester or known-good device when permitted by facility procedure.

Avoid bypassing approved grounding or power-distribution arrangements.

**Expected outcome:** Reliable AC power is confirmed at the system. If restoring a loose connection or correcting the external power source restores normal startup, verify operation and stop troubleshooting.

### 4. Inspect External Power Components
Check accessible power strips, isolation equipment, UPS units, switches, and peripheral power connections that are part of the installed CASE configuration. Confirm required switches are on and no external protection device has obviously tripped.

Do not repeatedly reset a device that trips again.

**Expected outcome:** All external power components required by the installation are energized normally. If an external power component is the cause and correcting it restores operation, continue to final verification.

### 5. Check Workstation and Display Power Separately
Observe workstation power indicators, fans, audible startup activity, and display indicators. Verify the monitor is powered and its video cable is secure. If the computer appears to start but the display remains blank, test the display path with an approved known-good monitor or cable when practical.

**Expected outcome:** Workstation and display status can be distinguished. If the issue is limited to an external display connection and normal display operation is restored, troubleshooting can stop after verification.

### 6. Disconnect Nonessential External Accessories
With the system safely shut down, disconnect nonessential external USB devices or other removable accessories that may interfere with startup, while preserving required installed components. Restart using the normal supported procedure.

Do not alter internal hardware or service-level configuration.

**Expected outcome:** The system completes startup with the minimum required external configuration. If one removable accessory prevents startup, remove it from use and verify the CASE system remains functional.

### 7. Perform a Controlled Restart
If the workstation has power but startup or application loading is incomplete, perform one controlled shutdown and restart using normal operating controls. Record any visible messages exactly as displayed.

Avoid repeated power cycling if abnormal odor, heat, electrical noise, or hardware damage is present.

**Expected outcome:** CASE reaches its normal operational state without repeated startup failure. If it does, proceed to final verification and stop troubleshooting.

### 8. Complete Functional Verification
Confirm the workstation, display, CASE application, ECG acquisition interface, configured exercise equipment, and other required peripherals initialize and communicate as expected. Verify the system is ready to acquire a test record before returning it to clinical use.

**Expected outcome:** The complete configured stress-test system starts normally and required functions are available. The issue is resolved and troubleshooting can stop.

## If the Problem Persists
Common external power, connection, display, and accessory causes have been ruled out. The remaining problem may involve workstation hardware, operating-system startup, application software, internal power circuitry, configuration, or another service-level condition.

Remove the CASE system from service, label it **Out of Service**, and send it for repair or bench evaluation. Evaluate it using appropriate GE Healthcare documentation and approved test equipment. Internal repairs or configuration changes should be performed only by qualified personnel.

Knowing when to stop external troubleshooting instead of repeatedly restarting an unreliable diagnostic system is proper troubleshooting. Complete appropriate functional and electrical safety testing before return to service when applicable.

## Clinical Use Tip
Do not begin an exercise stress study until ECG acquisition, exercise-device communication, and required emergency-response functions have been verified.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Protect the patient first, verify external power and connections before assuming an internal failure, and confirm the complete stress-test system operates correctly after correction. Escalate persistent startup problems and document the complaint, cause, and verified resolution clearly.

That is successful troubleshooting.
