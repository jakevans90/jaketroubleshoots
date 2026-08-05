---
schemaVersion: 1
title: "Medtronic Capnostream 35 Capnography Monitor - Startup Failure, Boot Loop, or Software Freeze"
issueTitle: "Startup Failure, Boot Loop, or Software Freeze"
description: "Troubleshoots failure to start, repeated restarting, frozen screens, or software lockups caused by power, battery, accessories, environment, or internal faults."
assetType: "Capnography Monitor"
manufacturer: "Medtronic"
model: "Capnostream 35"
slug: "medtronic-capnostream-35-startup-failure-boot-loop-or-software-freeze"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that the Capnostream 35 repeatedly restarted and would not remain on the monitoring screen."
  cause: "Clinical Engineering found that the boot loop occurred only while a damaged USB device was connected to the monitor."
  resolution: "The damaged USB device was removed, and repeated startup, extended operation, controls, capnography, alarms, and battery function were verified."
helpfulDetails:
  - "Stage where startup stopped"
  - "Exact message or screen displayed"
  - "Restart frequency"
  - "Indicator and sound behavior"
  - "Evidence of heat, liquid, odor, or damage"
  - "Outlet and power-supply test results"
  - "AC versus battery behavior"
  - "Connected accessories"
  - "Extended functional-test results"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots failure to start, repeated restarting, frozen screens, or software lockups caused by power, battery, accessories, environment, or internal faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Remove the Device From Use

Do not continue using a monitor that will not start, repeatedly reboots, or freezes. Transfer the patient to another verified monitor and maintain required respiratory and oxygenation surveillance.

Disconnect the suspect monitor from the patient before troubleshooting.

**Expected outcome:** The patient remains continuously monitored by reliable equipment.

### 2. Observe and Document the Failure

Determine whether the device is completely dead, stops at a logo, restarts repeatedly, reaches the main screen and freezes, shuts down unexpectedly, or freezes only during a specific function.

Record visible messages, indicator behavior, sounds, and the stage where startup stops.

**Expected outcome:** The startup or software failure is clearly characterized.

### 3. Inspect for Damage, Heat, Liquid, or Odor

Examine the monitor, power supply, connectors, and battery area externally for impact damage, liquid intrusion, excessive heat, swelling, discoloration, or unusual odor.

Immediately disconnect power and remove the device from service if any unsafe condition is found.

**Expected outcome:** No obvious physical or electrical hazard is present before further testing.

### 4. Verify the AC Power Source

Test the wall outlet with an approved method and inspect the power cord and external power supply for damage, looseness, or contamination. Connect the monitor directly to a verified outlet rather than an untested power strip.

**Expected outcome:** The monitor receives stable AC power. If it starts and remains stable, troubleshooting can stop after full functional verification.

### 5. Compare AC and Battery Operation

Observe whether the monitor starts on AC power, battery power, both, or neither. Check battery and charging indicators.

Do not continue testing a swollen, hot, damaged, or leaking battery.

**Expected outcome:** The problem is isolated to AC input, battery operation, or the monitor itself.

### 6. Disconnect Nonessential Accessories

Remove USB devices, network cables, external communication accessories, and nonessential patient accessories. Leave only the approved power source connected for startup testing.

A damaged peripheral may cause the software to hang or reboot.

**Expected outcome:** The monitor starts normally after an external device is removed. If stable, identify the accessory and stop troubleshooting after verification.

### 7. Perform One Controlled Power Reset

Use the normal shutdown process when possible. If the unit is frozen and the approved operator process allows a forced shutdown, power it off once, disconnect external power, allow it to fully shut down, then restart on verified AC power.

Do not repeatedly force shutdowns or cycle power through a boot loop.

**Expected outcome:** The monitor completes startup and remains responsive. If it does, continue to extended testing.

### 8. Check Environmental Conditions

Confirm that the monitor is not exposed to blocked ventilation, direct heat, excessive cold, condensation, or contamination. Move it to an appropriate dry test environment and allow it to stabilize before retrying.

**Expected outcome:** Normal startup occurs in an appropriate environment. If so, correct the environmental cause and complete functional verification.

### 9. Perform Extended Functional Verification

If startup succeeds, test touchscreen and physical controls, CO2 monitoring with a known-good FilterLine and approved source, SpO2 if equipped and applicable, alarms, battery charging, trend storage, and restart behavior.

Observe long enough to determine whether the freeze returns.

**Expected outcome:** The monitor remains responsive and completes all critical functions. If fully reliable, return-to-service testing can be completed.

### 10. Remove From Service for Recurrent or Persistent Failure

If the monitor remains in a boot loop, freezes again, fails startup, or shuts down unexpectedly, remove it from service and label it **Out of Service**.

Do not attempt operating-system reinstallation, firmware loading, internal battery disconnection, board replacement, or service-menu recovery without approved manufacturer procedures.

**Expected outcome:** An unstable monitor is prevented from returning to clinical use and is escalated for bench evaluation.

## If the Problem Persists

Power-source, accessory, environmental, and normal restart causes have been ruled out. Remaining possibilities include software corruption, failed internal storage, battery or power-management failure, display or control-system problems, internal connection failure, or main electronics malfunction.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired, restored, or configured only by qualified personnel

Following repair, verify repeated startup, extended operation, battery and AC transitions, touchscreen and controls, CO2 waveform and values, alarms, stored data, communications, and electrical safety when applicable before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A monitor that restarts or freezes intermittently is unsafe even if it operates normally after a single reboot.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient, verify power and remove external accessories before assuming an internal software or electronics failure. A device that repeatedly freezes or restarts must be escalated, thoroughly tested after repair, and documented with clear observations and final verification.

That is successful troubleshooting.
