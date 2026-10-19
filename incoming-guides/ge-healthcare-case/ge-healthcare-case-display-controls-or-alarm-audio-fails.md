---
schemaVersion: 1
title: "GE Healthcare CASE Stress Test System - Display, Controls, or Alarm Audio Fails"
issueTitle: "Display, Controls, or Alarm Audio Fails"
description: "Display, input controls, or configured audible indications fail or become unreliable, limiting safe operation of the CASE stress-test system."
assetType: "Stress Test System"
manufacturer: "GE Healthcare"
model: "CASE"
slug: "ge-healthcare-case-display-controls-or-alarm-audio-fails"
dateAdded: "2026-10-19"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the CASE display intermittently went blank although the workstation remained powered."
  cause: "Clinical Engineering found the external video cable was loose at the display connection."
  resolution: "Secured the video cable and verified continuous display operation and normal CASE control response during functional testing."
helpfulDetails:
  - "Failed display, control, or audio function"
  - "Display power indicator"
  - "Video and power cable condition"
  - "Keyboard or mouse response"
  - "Known-good substitution results"
  - "Audio or mute setting observed"
  - "Whether failure occurred only in CASE"
  - "Restart result"
  - "Final functional-test result"
  - "Final device status"
---

## What This Guide Helps With
Display, input controls, or configured audible indications fail or become unreliable, limiting safe operation of the CASE stress-test system.

## Step-by-Step Troubleshooting
### 1. Protect the Patient
Do not continue a stress study if loss of the display or controls prevents reliable ECG monitoring, exercise control, or response to patient status. Stop the study safely and provide alternate monitoring as necessary.

**Expected outcome:** The patient is no longer dependent on an interface that cannot be reliably seen, heard, or controlled.

### 2. Identify the Failed Function
Determine whether the complaint involves the monitor, touchscreen if present, keyboard, mouse, another control interface, speaker, or an audible indication. Confirm whether the failure is constant or intermittent.

**Expected outcome:** The issue is isolated to a specific user-interface function.

### 3. Check Display Power and Connections
Confirm the display is powered, its indicator is normal, and accessible power and video cables are fully seated. Verify brightness or normal user controls have not been unintentionally changed.

**Expected outcome:** Display power and external connections are correct. If correcting a loose connection restores the image, proceed to final verification.

### 4. Check External Input Devices
Inspect keyboard, mouse, touchscreen interface cables, and other accessible controls for loose connections, damage, contamination, or stuck controls. Reconnect removable devices with the system safely out of clinical use.

**Expected outcome:** Required control devices respond reliably.

### 5. Substitute Known-Good External Devices
When appropriate, test with a compatible known-good monitor, keyboard, mouse, or cable to separate the workstation from the external device.

**Expected outcome:** If the known-good external device functions normally, the original accessory is isolated and should be removed from service.

### 6. Verify Audio Path and User-Accessible Volume
For an audio complaint, confirm the expected function actually generates an audible indication in the installed CASE configuration. Check user-accessible volume or mute controls where applicable and verify external speakers are connected if the system uses them.

Do not defeat or silence required clinical alerts.

**Expected outcome:** Configured audible indications are clearly heard when intentionally tested.

### 7. Check for Application Versus Hardware Failure
Determine whether controls work elsewhere in the operating environment or whether the failure is confined to the CASE application. Note whether the pointer moves, keyboard responds, and display remains active.

**Expected outcome:** The problem is narrowed to an external interface device, workstation, or CASE application.

### 8. Perform One Controlled Restart
With the system removed from active clinical use, restart the CASE workstation normally.

**Expected outcome:** Display, controls, and configured audio initialize normally and remain responsive.

### 9. Perform Final Functional Verification
Verify the display is readable, required input controls operate consistently, configured audible functions are present, and the CASE application can be safely operated through a representative workflow.

**Expected outcome:** All required interface functions operate normally. The issue is resolved and troubleshooting can stop.

## If the Problem Persists
External display connections, input devices, user-accessible settings, known-good substitutions, and normal restart have been checked. A persistent problem may involve workstation hardware, display electronics, audio hardware, drivers, application software, or another service-level condition.

Remove the system from service, label it **Out of Service**, and perform bench evaluation using appropriate manufacturer documentation and approved test equipment. Repairs should be performed only by qualified personnel.

Verify all essential user-interface and audible functions before return to service.

## Clinical Use Tip
If clinicians cannot reliably see the ECG or control the exercise test, the CASE system should not be used even if ECG acquisition itself continues.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
A working acquisition system is not clinically usable if essential information cannot be displayed or controlled reliably. Check external interface components first, verify complete operation after correction, and escalate persistent failures appropriately.

That is successful troubleshooting.
