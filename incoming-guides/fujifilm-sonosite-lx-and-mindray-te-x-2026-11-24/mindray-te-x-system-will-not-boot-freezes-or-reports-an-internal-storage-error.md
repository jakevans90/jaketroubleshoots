---
schemaVersion: 1
title: "Mindray TE X Ultrasound System - System Will Not Boot, Freezes, or Reports an Internal Storage Error"
issueTitle: "System Will Not Boot, Freezes, or Reports an Internal Storage Error"
description: "Troubleshoots startup, freezing, or storage-related symptoms after external power, connected accessories, peripherals, and normal restart conditions are checked."
assetType: "Ultrasound System"
manufacturer: "Mindray"
model: "TE X"
slug: "mindray-te-x-system-will-not-boot-freezes-or-reports-an-internal-storage-error"
dateAdded: "2026-11-24"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the TE X repeatedly froze during startup and would not reach the normal imaging screen."
  cause: "Clinical Engineering found a connected external USB device was associated with the startup freeze."
  resolution: "Clinical Engineering removed the external USB device and verified repeated normal startup, stable imaging controls, test image acquisition, and normal shutdown."
helpfulDetails:
  - "Exact startup or storage message"
  - "Point where startup stops"
  - "AC and battery behavior"
  - "External devices connected"
  - "Result with peripherals removed"
  - "Response to controlled restart"
  - "Whether patient data remained accessible"
  - "Test acquisition and storage result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots startup, freezing, or storage-related symptoms after external power, connected accessories, peripherals, and normal restart conditions are checked.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Clinical Continuity
Remove the TE X from active use if it cannot boot reliably, freezes during imaging, or cannot safely store examination data. Move the patient to another verified ultrasound system.

Expected outcome: Clinical care no longer depends on the unstable system.

### 2. Record the Exact Failure
Document whether the system is completely unresponsive, stops at a particular startup stage, repeatedly restarts, freezes after login, or displays a storage-related message. Record the exact displayed text without interpreting it.

Expected outcome: The failure is accurately documented for comparison and escalation.

### 3. Verify External Power
Confirm the outlet, AC cord, and accessible power connections are secure and functional. Determine whether behavior differs on AC versus available battery power without repeatedly cycling a failing system.

Expected outcome: Stable external power is confirmed as the source.

### 4. Disconnect Nonessential External Accessories
With the system powered down appropriately, disconnect nonessential USB devices, printers, external displays, removable media, or other externally attached accessories that are not required for startup.

Expected outcome: The TE X starts normally if an external accessory was interfering. If so, reconnect accessories individually to identify the cause.

### 5. Perform One Controlled Restart
After confirming power and removing nonessential accessories, perform a normal shutdown/startup or approved power-cycle sequence.

Expected outcome: The system completes startup and remains responsive. Avoid repeated cycling if the same failure immediately returns.

### 6. Check Available Storage Through Normal Controls
If the system boots, use normal user-accessible functions to determine whether examination storage appears available and whether the reported condition clears. Do not delete patient data or reformat storage as a troubleshooting shortcut.

Expected outcome: Storage functions are available without errors and existing data remains accessible as appropriate.

### 7. Test a Basic Nonclinical Workflow
Without relying on the system for patient care, verify that menus respond, an approved test image can be acquired, and basic navigation remains stable.

Expected outcome: The system remains responsive and does not freeze during basic operation.

### 8. Reconnect External Accessories Individually
If the TE X operates normally after accessories were removed, reconnect approved external devices one at a time and observe behavior.

Expected outcome: The offending external accessory is identified, or all accessories reconnect without recurrence.

### 9. Perform Final Functional Verification
Confirm reliable startup, stable control response, image acquisition, examination storage where appropriate, and normal shutdown.

Expected outcome: The full basic workflow completes without freezing or storage errors. Otherwise, keep the system out of service.

## If the Problem Persists

External power, attached peripherals, and a controlled restart have been checked. Persistent boot, freezing, or internal-storage symptoms may involve system software, operating storage, internal hardware, data corruption, or another service-level condition.

Remove the TE X from service, label it **Out of Service**, and send it for repair or bench evaluation. Preserve patient data and system information according to institutional policy. Do not reformat storage, reinstall software, open internal assemblies, or perform unauthorized recovery procedures.

Qualified personnel should use appropriate Mindray documentation and approved service tools. Complete startup, image acquisition, data-storage, and functional verification before return to service.

## Clinical Use Tip

A system that freezes or cannot reliably save examinations should not be used merely because live imaging still appears available.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect patient workflow, document the precise failure, eliminate external power and peripheral causes before assuming internal storage failure, and stop when recovery would require service-level procedures.

That is successful troubleshooting.
