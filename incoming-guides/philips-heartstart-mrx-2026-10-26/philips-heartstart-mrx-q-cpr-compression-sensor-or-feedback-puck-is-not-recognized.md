---
schemaVersion: 1
title: "Philips HeartStart MRx Defibrillator - Q-CPR Compression Sensor or Feedback Puck Is Not Recognized"
issueTitle: "Q-CPR Compression Sensor or Feedback Puck Is Not Recognized"
description: "Troubleshoot missing Q-CPR accessory recognition caused by connections, cable damage, accessory condition, configuration, or incompatible external components."
assetType: "Defibrillator"
manufacturer: "Philips"
model: "HeartStart MRx"
slug: "philips-heartstart-mrx-q-cpr-compression-sensor-or-feedback-puck-is-not-recognized"
dateAdded: "2026-10-26"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the HeartStart MRx would not recognize the Q-CPR compression feedback accessory."
  cause: "Clinical Engineering found damage at the Q-CPR accessory cable strain relief and confirmed normal recognition with a known-good accessory."
  resolution: "Replaced the defective Q-CPR accessory, verified stable recognition and feedback operation, and completed required functional testing before return to service."
helpfulDetails:
  - "Whether the accessory was completely absent or intermittent"
  - "Accessory physical condition"
  - "Connector condition"
  - "Cable and strain-relief condition"
  - "Whether movement affected recognition"
  - "Known-good accessory results"
  - "Comparison-device results"
  - "Configuration observed"
  - "Feedback function after correction"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoot missing Q-CPR accessory recognition caused by connections, cable damage, accessory condition, configuration, or incompatible external components.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Continue CPR

Never interrupt CPR or delay defibrillation while troubleshooting a compression-feedback accessory.

If Q-CPR feedback is unavailable during an active resuscitation, continue CPR according to the clinical team's established process and use another verified feedback method if required.

Troubleshoot the accessory only when doing so will not interfere with patient care.

**Expected outcome:** Resuscitation continues without dependence on an unreliable feedback accessory.

### 2. Confirm the Exact Recognition Problem

Determine whether the compression sensor or feedback puck:

- Is not detected at all
- Connects intermittently
- Is detected but provides no feedback
- Loses recognition when moved
- Fails only with one particular accessory

Confirm that the complaint specifically involves Q-CPR recognition rather than the MRx display or another unrelated function.

**Expected outcome:** The problem is reproducible and narrowed to accessory recognition or feedback operation.

### 3. Verify Basic MRx Operation

Confirm that the defibrillator powers normally and that its monitoring, display, controls, and other applicable functions are operating normally.

If the unit has broader instability, freezes, restarts, or shows multiple accessory failures, remove it from service.

**Expected outcome:** The MRx operates normally except for the Q-CPR accessory complaint.

### 4. Inspect the Compression Sensor or Feedback Puck

Examine the accessory for:

- Cracks
- Deformation
- Liquid contamination
- Damaged housings
- Loose cable entry points
- Bent or contaminated contacts
- Evidence of impact or crushing

Do not continue using a visibly damaged CPR feedback accessory.

**Expected outcome:** The accessory is physically intact. If damage is found, replace the accessory and verify recognition before stopping troubleshooting.

### 5. Inspect and Reseat All External Connections

Disconnect and reconnect the Q-CPR accessory using the normal external connection points.

Inspect connectors for contamination, damage, incomplete seating, or mechanical looseness.

Do not force connectors or use improvised adapters.

**Expected outcome:** Connections seat securely and the accessory is recognized consistently. If reseating corrects the problem and repeated connection remains reliable, troubleshooting can stop after functional verification.

### 6. Inspect the Accessory Cable

Follow the external cable from the accessory to the device and look for:

- Cuts
- Pinching
- Sharp bends
- Stretched sections
- Damaged strain relief
- Intermittent operation during normal cable positioning

Do not aggressively flex a questionable cable in a way that could worsen damage.

**Expected outcome:** The cable remains electrically and mechanically stable during normal handling. If a damaged cable or accessory assembly is replaced and recognition returns, the issue is resolved.

### 7. Confirm the Correct Accessory and Configuration

Verify that the connected CPR feedback accessory is intended for the HeartStart MRx configuration in use.

Confirm the device is configured to support the installed Q-CPR functionality where applicable, without entering unauthorized service menus or altering protected settings.

**Expected outcome:** The correct accessory is connected to an appropriately configured MRx. If an incorrect accessory caused the complaint, use the approved component and verify operation.

### 8. Substitute a Known-Good Accessory

When available, connect a compatible known-good Q-CPR accessory.

This is one of the most useful ways to distinguish an accessory problem from a device-side recognition problem.

**Expected outcome:** The known-good accessory is immediately and consistently recognized. If so, remove the original accessory from service and troubleshooting can stop after final verification.

### 9. Compare the Suspect Accessory on Another Compatible System

If organizational resources and procedures allow, test the questionable accessory with another compatible, verified system.

Do not disrupt clinical readiness of another defibrillator solely for troubleshooting.

**Expected outcome:** The comparison identifies whether the failure follows the accessory or remains with the original MRx.

### 10. Verify Feedback Function With Approved Test Methods

After recognition is restored, verify the Q-CPR feedback pathway using approved test equipment or manufacturer-supported functional procedures.

Confirm that the accessory remains recognized and feedback responds consistently throughout the test.

**Expected outcome:** The accessory is detected and feedback operates consistently. The issue is resolved and troubleshooting can stop.

### 11. Escalate Persistent Recognition Failures

If multiple compatible known-good accessories fail to be recognized by the same MRx, or recognition remains intermittent after external connections and configuration have been checked, stop troubleshooting.

**Expected outcome:** The MRx is removed from service when Q-CPR functionality is required and sent for qualified bench evaluation.

## If the Problem Persists

Common accessory, cable, connection, compatibility, and external configuration causes have been ruled out. Remaining possibilities may involve the device-side accessory interface, internal communication, software/configuration, or another service-level condition.

The device should be:

- Removed from service when Q-CPR functionality is required
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Philips documentation and approved test equipment
- Repaired or configured only by qualified personnel

Complete required defibrillator and accessory functional testing before return to service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Compression feedback is an aid, not a reason to interrupt CPR; continue resuscitation using the clinical team's established process if the feedback accessory fails.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Patient care and uninterrupted CPR come first. Work from the accessory and connections inward, use known-good substitutions to isolate the fault, verify feedback before return to service, and escalate device-side failures rather than assuming an internal component.

That is successful troubleshooting.
