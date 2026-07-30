---
schemaVersion: 1
title: "Mortara ELI Series Electrocardiograph (EKG) Machine - Software Freeze, Boot Loop, Or Startup Failure"
issueTitle: "Software Freeze, Boot Loop, Or Startup Failure"
description: "Troubleshooting frozen controls, repeated restarting, incomplete startup, or failed boot caused by power, accessories, media, battery, or software conditions."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "Mortara"
model: "ELI Series"
slug: "mortara-eli-series-software-freeze-boot-loop-or-startup-failure"
dateAdded: "2026-07-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Mortara ELI Series EKG machine repeatedly froze at startup and could not be used for ECG acquisition."
  cause: "Clinical Engineering found an incompatible USB device connected during startup; the EKG machine started normally after the media was removed."
  resolution: "Removed the USB device from use, completed repeated startup tests and a simulator ECG acquisition, and returned the unit to service."
helpfulDetails:
  - "Exact freeze or restart point."
  - "Displayed message."
  - "AC and battery behavior."
  - "Outlet test result."
  - "Accessories connected."
  - "Removable media present."
  - "Storage status."
  - "Function that triggers the freeze."
  - "Number of successful restarts."
  - "Simulator ECG result."
  - "Final device status."
---

## What This Guide Helps With

Troubleshooting frozen controls, repeated restarting, incomplete startup, or failed boot caused by power, accessories, media, battery, or software conditions.

## Step-by-Step Troubleshooting

### 1. Ensure Patient Safety and Continuity of Care

Do not troubleshoot a frozen, restarting, or unreliable EKG machine while it is being used for a patient.

Notify clinical staff and use another verified EKG machine for any required ECG. Do not rely on locally stored ECGs until their save status is confirmed.

**Expected outcome:** Patient care continues without depending on an unstable device.

### 2. Confirm the Exact Failure Pattern

Determine whether the device:

- Does not power on.

- Stops at a startup screen.

- Repeatedly restarts.

- Starts but freezes during use.

- Freezes only during printing, transmission, retrieval, or export.

- Displays an error before restarting.

- Developed the issue after a software update, power interruption, accessory connection, or fluid exposure.

Record the last normal screen and any displayed message.

**Expected outcome:** The issue is categorized as power failure, boot interruption, application freeze, or function-specific lockup.

### 3. Check for Signs Requiring Immediate Removal From Service

Inspect for:

- Burning odor.

- Unusual heat.

- Fluid intrusion.

- Cracked housing.

- Damaged power inlet.

- Arcing or discoloration.

- Repeated clicking or abnormal noise.

Do not continue powering the unit if any of these conditions are present.

**Expected outcome:** Unsafe electrical or physical conditions are identified before further testing.

### 4. Verify AC Power

Inspect the power cord and inlet for damage. Confirm the plug is fully inserted.

Test the outlet using an approved outlet tester or connect the EKG machine to a known-good approved receptacle. Avoid power strips unless specifically approved.

**Expected outcome:** The device receives stable AC power and begins charging or starting normally. If power correction resolves the problem, proceed to final verification and stop.

### 5. Check Battery Behavior

Observe whether the device starts differently on AC power and battery power.

Do not repeatedly cycle a severely depleted battery. Allow charging according to the approved workflow. Remove the unit from service if it shuts down unexpectedly or cannot maintain operation long enough to complete an ECG.

**Expected outcome:** The failure is identified as AC-related, battery-related, or independent of the power source.

### 6. Disconnect External Accessories

With the device powered down, disconnect nonessential external accessories, including:

- USB storage.

- Barcode scanner.

- Network cable.

- External keyboard or pointing device.

- Optional accessory modules not needed for startup.

- Leave only the approved power connection and required acquisition hardware.

**Expected outcome:** The device starts without a faulty or incompatible accessory interfering with startup.

### 7. Remove Removable Media

Remove any USB storage or other removable media before restart.

A corrupted or incompatible device can delay or interrupt startup or cause the application to freeze during file access.

**Expected outcome:** The EKG machine starts normally without removable media. If so, test the media separately and do not reconnect it until verified.

### 8. Perform a Controlled Power Reset

If the normal controls respond, perform a normal shutdown.

If the device is completely frozen, remove it from clinical use and follow the approved method for powering it off. Disconnect AC power and external accessories. Allow the unit to fully power down before reconnecting AC and restarting.

Do not repeatedly hard-cycle the device.

**Expected outcome:** The device completes startup and reaches its normal operating screen without restarting or freezing.

### 9. Observe Startup Closely

During restart, note:

- Whether the display illuminates.

- Any startup tones.

- Progress indicators.

- The exact point where startup stops.

- Whether the device restarts at the same point.

- Whether controls respond.

- Whether date and time are retained.

**Expected outcome:** A repeatable failure point is documented for escalation or the device starts normally.

### 10. Test Core Functions Individually

After a successful startup, test one function at a time:

- Patient entry.

- Acquisition module recognition.

- Simulator ECG acquisition.

- Saving.

- Printing.

Record retrieval.

Network transmission.

USB export, when applicable.

**Expected outcome:** The specific function causing the freeze is isolated without subjecting a patient to unreliable operation.

### 11. Verify Available Storage

Review normal storage and pending-transmission status.

A full record queue or inaccessible stored record may contribute to freezing during saving or retrieval. Preserve required ECGs before any authorized cleanup.

**Expected outcome:** The device has usable storage and can save and retrieve a test record normally.

### 12. Perform Final Reliability Verification

Using an ECG simulator:

- Start the device from a powered-off state.

Confirm normal startup.

Acquire and save a test ECG.

Print or transmit it.

Operate the device long enough to verify it remains responsive.

Restart it again and confirm consistent startup.

**Expected outcome:** The EKG machine starts and functions reliably through repeated controlled testing. Troubleshooting can stop.

### 13. Escalate Any Recurring Instability

Remove the device from service if it:

- Freezes again.

- Repeats a boot loop.

- Cannot complete startup.

- Loses stored records.

- Shuts down unexpectedly.

- Requires repeated forced restarts.

- Fails only during a specific clinical function.

**Expected outcome:** An unstable EKG machine is prevented from returning to patient use.

## If the Problem Persists

External causes involving AC power, battery behavior, accessories, removable media, storage status, and temporary software state have been ruled out. The remaining issue may involve internal power regulation, storage hardware, operating software, corrupted configuration, display electronics, or another service-level failure.

The device should be:

- Removed from service.

- Labeled Out of Service.

- Sent for repair or bench evaluation.

- Evaluated using appropriate Mortara documentation and approved test equipment.

- Repaired, restored, or configured only by qualified personnel.

Preserve available logs and patient records. Do not install unapproved software or attempt unauthorized recovery procedures.

After repair, complete electrical safety testing when required and verify startup, ECG acquisition, saving, printing, retrieval, and transmission before return to service.

Knowing when to stop after recurring instability is proper troubleshooting.

## Clinical Use Tip

A device that restarts successfully once is not proven reliable; complete an ECG acquisition and repeat-start verification before return to service.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Patient care comes first when software behavior is unreliable. Rule out power, accessories, media, and storage before assuming an internal fault, but do not return a device that freezes or restarts unpredictably. Verify reliable operation and document the complete sequence.

That is successful troubleshooting.
