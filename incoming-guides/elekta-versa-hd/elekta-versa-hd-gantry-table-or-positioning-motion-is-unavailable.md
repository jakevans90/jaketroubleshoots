---
schemaVersion: 1
title: "Elekta Versa HD Radiation Therapy System - Gantry, Table, or Positioning Motion Is Unavailable"
issueTitle: "Gantry, Table, or Positioning Motion Is Unavailable"
description: "Gantry, treatment table, or other positioning motion is unavailable because of interlocks, controls, obstructions, positioning conditions, or external communication problems."
assetType: "Radiation Therapy System"
manufacturer: "Elekta"
model: "Versa HD"
slug: "elekta-versa-hd-gantry-table-or-positioning-motion-is-unavailable"
dateAdded: "2026-10-01"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that treatment table motion on the Elekta Versa HD was unavailable during patient setup."
  cause: "Clinical Engineering found an external positioning control connection was not fully seated."
  resolution: "Clinical Engineering secured the connection, verified repeatable table motion and normal stopping behavior, and completed functional checks before return to service."
helpfulDetails:
  - "Motion or axis affected"
  - "Whether all or only one control location failed"
  - "Exact displayed message"
  - "Emergency-stop status"
  - "Obstructions found"
  - "Accessory or patient-support configuration"
  - "Control or pendant condition"
  - "Abnormal sound or vibration"
  - "Functions tested after correction"
  - "Final device status"
---
## What This Guide Helps With

Gantry, treatment table, or other positioning motion is unavailable because of interlocks, controls, obstructions, positioning conditions, or external communication problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Unintended Motion

Stop treatment activity and ensure the patient is safely supported. Do not troubleshoot unreliable positioning equipment while a patient depends on it.

If necessary, follow departmental procedures for safe patient removal before technical troubleshooting.

**Expected outcome:** The patient is safe and no unexpected equipment movement can occur during troubleshooting.

### 2. Confirm Which Motion Is Unavailable

Determine whether the problem affects the gantry, treatment table, a specific axis, multiple axes, or all positioning motion.

Note whether the motion command is ignored, starts and stops, is inhibited, or produces a displayed message.

**Expected outcome:** The affected motion and exact failure behavior are clearly identified.

### 3. Inspect for Physical Obstructions

Check the treatment area for accessories, immobilization devices, cables, patient-support equipment, room items, or other objects that could interfere with movement.

Do not force movement past resistance.

**Expected outcome:** The intended travel path is clear and no external obstruction is preventing motion.

### 4. Check Emergency and Safety Controls

Verify that accessible emergency-stop controls and other operator safety controls are in their intended state.

Do not bypass collision protection, interlocks, or safety systems.

**Expected outcome:** Motion is not being inhibited by an externally activated safety control.

### 5. Verify Positioning Controls

Inspect the applicable hand controls, pendant, console controls, or other normal positioning interfaces for damage, stuck controls, loose connections, or abnormal indicators.

If an approved equivalent control method is available, compare operation using that method.

**Expected outcome:** A functional control produces the expected positioning command. If one external control is defective while another works normally, isolate the defective control from use.

### 6. Verify Required System State

Confirm that the Versa HD is in the appropriate operational state for the requested motion and that no visible interlock, mode restriction, or workflow condition is preventing movement.

Do not alter protected configuration or service settings.

**Expected outcome:** The system is in a state where the requested movement should normally be permitted.

### 7. Check Accessories and Table Attachments

Inspect attached treatment accessories, indexing hardware, patient supports, immobilization devices, and external cabling for improper installation or interference.

Remove or reposition only items that can safely be addressed without affecting patient setup or calibration.

**Expected outcome:** No accessory or external attachment is mechanically or logically inhibiting movement.

### 8. Compare Motion Functions

With the system out of clinical use, test other normal positioning functions to determine whether the problem is isolated or system-wide.

Observe for abnormal sound, vibration, hesitation, or inconsistent movement.

**Expected outcome:** Normal motion is smooth and repeatable. Any abnormal motion requires removal from service even if movement remains possible.

### 9. Perform Final Functional Verification

If normal motion is restored after correcting an external condition, verify the affected movement through its normal operational range appropriate for routine service testing and confirm that controls stop motion normally.

**Expected outcome:** The positioning function operates consistently without abnormal indications. Troubleshooting can stop after required return-to-service checks are completed.

### 10. Escalate Persistent Motion Failure

If motion remains unavailable or unreliable after external controls, obstructions, accessories, interlocks, and operating state are checked, stop troubleshooting.

**Expected outcome:** The system is removed from service for qualified evaluation rather than operated with unreliable positioning.

## If the Problem Persists

External positioning causes have been ruled out. The remaining problem may involve motion control electronics, drives, position feedback, internal safety circuits, collision detection, system communications, or service-level configuration.

The Versa HD should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench/service evaluation.
- Evaluated using appropriate Elekta documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Do not bypass motion interlocks or perform internal drive or controller repair without authorized procedures. Required positioning, safety, and treatment-system checks must be completed before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Any positioning function that moves unpredictably, hesitates, or fails to stop normally should be treated as unsafe even if the system can still complete some movements.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Patient protection comes first around high-mass positioning systems. Verify obstructions, controls, accessories, safety conditions, and operating state before assuming an internal motion-system failure, then escalate when movement remains unreliable.

That is successful troubleshooting.
