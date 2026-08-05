---
schemaVersion: 1
title: "Masimo Rad-97 Pulse Oximeter - Software Freeze, Boot Loop, Or Startup Failure"
issueTitle: "Software Freeze, Boot Loop, Or Startup Failure"
description: "Startup or software failures caused by unstable power, depleted battery, attached accessories, corrupted configuration, incomplete updates, or internal system faults."
assetType: "Pulse Oximeter"
manufacturer: "Masimo"
model: "Rad-97"
slug: "masimo-rad-97-software-freeze-boot-loop-or-startup-failure"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Rad-97 repeatedly restarted and would not progress beyond the startup screen."
  cause: "Clinical Engineering found an unapproved USB device connected to the monitor and verified that startup completed normally after it was removed."
  resolution: "Removed the unapproved accessory, completed repeated startup and extended functional testing, verified monitoring and alarms, and returned the device to service."
helpfulDetails:
  - "Last visible startup screen or message"
  - "Restart or freeze pattern"
  - "AC and battery behavior"
  - "Power supply and outlet tested"
  - "Physical damage, heat, odor, or fluid exposure"
  - "Connected accessories"
  - "Recent software or configuration changes"
  - "Results after accessory removal"
  - "Extended stability test results"
  - "Final device status"
---

## What This Guide Helps With

Startup or software failures caused by unstable power, depleted battery, attached accessories, corrupted configuration, incomplete updates, or internal system faults.

## Step-by-Step Troubleshooting

### 1. Remove the Device From Patient Use

Do not troubleshoot a frozen, restarting, or non-starting monitor while a patient depends on it. Transfer monitoring to another verified device immediately.

Expected outcome: Patient monitoring continues on reliable equipment.

### 2. Confirm the Startup Failure

Determine whether the Rad-97 freezes during operation, remains on a startup screen, repeatedly restarts, shuts down during boot, or does not progress beyond initial indicators.

Record the last visible screen, message, tone, and indicator behavior.

Expected outcome: The failure stage is identified.

### 3. Inspect for Damage, Heat, Odor, or Fluid Intrusion

Check the enclosure, vents, connectors, power supply, and battery area for impact damage, abnormal heat, odor, swelling, residue, or fluid exposure.

Do not power the device again if unsafe physical conditions are present.

Expected outcome: The device is either safe for limited external testing or immediately removed from service.

### 4. Verify the External Power Source

Inspect the approved power supply and connections. Test on a verified outlet and confirm that the power connector remains secure.

Avoid repeated power cycling if the device becomes hot or emits unusual sounds or odor.

Expected outcome: Stable external power is available and the device begins a normal startup.

### 5. Allow Battery Charging

If the battery is deeply depleted, connect the approved power supply and allow sufficient charging according to facility and manufacturer guidance before retesting.

Expected outcome: The monitor starts normally after adequate charging. If stable, continue to final verification.

### 6. Disconnect Nonessential Accessories

Remove sensors, patient cables, USB devices, network cables, adapters, and other nonessential external accessories.

Attempt startup with only approved power connected.

Expected outcome: The Rad-97 starts normally in a basic configuration. Reconnect accessories individually to identify an external cause.

### 7. Perform a Controlled Restart

Use the normal power control and shutdown process when responsive.

Do not repeatedly interrupt startup or use undocumented reset methods.

Expected outcome: The monitor completes startup and remains responsive.

### 8. Observe Startup Self-Checks

Watch for consistent progress through the startup sequence, normal display operation, audible indications, and absence of repeated rebooting.

Expected outcome: Startup completes without errors or looping.

### 9. Verify Configuration and Software History

Determine whether the problem began after an authorized software update, profile change, network change, or accessory connection.

Do not reinstall software, downgrade versions, or access restricted service functions without approved procedures.

Expected outcome: A recent authorized change is identified for escalation or rollback by qualified personnel.

### 10. Perform Extended Functional Testing

After successful startup, verify display, controls, sensor detection, pleth waveform, numerical readings, alarms, charging, battery operation, network status, and stability over time.

Expected outcome: The Rad-97 remains stable through repeated normal operation.

### 11. Escalate Recurring Software or Startup Failure

Any device that repeats a boot loop, freezes again, or cannot complete startup must remain out of service.

Expected outcome: The unit is labeled Out of Service and sent for qualified bench evaluation.

## If the Problem Persists

External causes involving power, depleted battery, connected accessories, environmental damage, and temporary software state have been ruled out.

The remaining cause may involve internal storage, processor function, software corruption, battery management, power distribution, configuration, or another service-level condition. Remove the device from service, label it Out of Service, and send it for evaluation using current manufacturer documentation and approved test equipment.

Only qualified personnel should perform software recovery, authorized configuration restoration, or internal repair. Complete all monitoring, alarm, electrical safety, battery, and communication tests before return to service.

## Clinical Use Tip

A monitor that restarts or freezes even once during testing should not return to clinical use until the cause is understood and stability is verified.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Remove unstable equipment from patient use, verify power and external accessories before assuming software or hardware failure, avoid undocumented recovery methods, and escalate recurring startup problems.

That is successful troubleshooting.
