---
schemaVersion: 1
title: "Getinge Servo-n Ventilator - Edi/NAVA Signal Is Missing, Noisy, or Intermittent"
issueTitle: "Edi/NAVA Signal Is Missing, Noisy, or Intermittent"
description: "Troubleshoots unreliable Edi/NAVA signals caused by catheter position, connections, interference, accessory condition, configuration, or service-level communication faults."
assetType: "Ventilator"
manufacturer: "Getinge"
model: "Servo-n"
slug: "getinge-servo-n-edi-nava-signal-is-missing-noisy-or-intermittent"
dateAdded: "2026-11-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported intermittent loss of the Edi signal whenever the patient cable was moved."
  cause: "Clinical Engineering found an intermittent connection at the reusable Edi cable strain relief."
  resolution: "The damaged cable was replaced with an approved known-good cable, stable Edi signal operation was verified, and the ventilator was returned to service."
helpfulDetails:
  - "Missing, noisy, or intermittent signal"
  - "Associated message"
  - "Catheter and accessory type"
  - "Connector condition"
  - "Cable movement effect"
  - "Known-good cable or adapter result"
  - "Evidence of environmental interference"
  - "Configuration observed"
  - "Final signal verification"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots unreliable Edi/NAVA signals caused by catheter position, connections, interference, accessory condition, configuration, or service-level communication faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Reliable Ventilation
If NAVA or Edi-based support is unreliable during patient care, transition the patient to an appropriate verified ventilation mode or alternate ventilator according to the clinical plan.

Clinical personnel should manage catheter placement and patient-care decisions. Clinical Engineering should not troubleshoot an unreliable NAVA signal while the patient depends on it.

**Expected outcome:** The patient remains safely ventilated while technical troubleshooting proceeds.

### 2. Confirm the Exact Signal Problem
Determine whether the Edi signal is:
- Completely absent
- Present but noisy
- Intermittent
- Lost only during movement
- Lost after connecting a specific cable or accessory

Record any associated messages.

**Expected outcome:** The nature and reproducibility of the Edi/NAVA problem are established.

### 3. Inspect External Edi Connections
Inspect the accessible Edi/NAVA signal path from the patient-side accessory toward the ventilator.

Look for:
- Loose connectors
- Partially seated plugs
- Damaged cable insulation
- Bent or contaminated connector contacts
- Excessive cable strain
- Connections being pulled during patient movement

Reseat appropriate external connections.

**Expected outcome:** All Edi-related external connections are secure and undamaged.

### 4. Confirm Catheter and Accessory Compatibility
Verify that the connected Edi catheter, adapter, and cables are compatible with the Servo-n configuration.

Clinical staff should confirm appropriate catheter positioning using approved clinical methods.

**Expected outcome:** The correct compatible accessories are being used and the clinical placement has been verified.

### 5. Check for Movement and Electrical Interference
Observe whether noise appears when:
- The patient moves
- Cables are moved
- Other electrical devices are operated nearby
- Power cords or signal cables cross or run closely together

Reposition external cables where practical without compromising patient care.

**Expected outcome:** The signal remains stable despite normal cable movement and nearby equipment operation.

### 6. Inspect the Edi Cable and Adapter
Examine reusable cables and adapters for wear, damaged strain reliefs, contamination, or loose connections.

Gently manipulate the cable during bench testing to identify intermittent external faults without stressing connectors.

**Expected outcome:** Cable movement does not cause signal loss or excessive artifact.

### 7. Substitute Known-Good Compatible Accessories
When available and clinically appropriate, test with a known-good approved Edi cable, adapter, or other replaceable external accessory.

Replace one item at a time.

**Expected outcome:** If the Edi signal becomes stable with a known-good accessory, the defective external component is identified and removed from service. Troubleshooting can stop after verification.

### 8. Verify Normal Configuration
Confirm NAVA/Edi functionality is enabled and configured appropriately for the connected hardware using authorized normal controls.

Do not enter restricted service menus or alter undocumented settings.

**Expected outcome:** The ventilator configuration matches the installed Edi/NAVA hardware.

### 9. Perform Final Functional Verification
Verify stable Edi signal acquisition using the appropriate test setup or clinically approved verification process.

Confirm that signal loss does not recur with normal cable handling.

**Expected outcome:** The Edi signal is continuously detected and stable. Troubleshooting can stop.

## If the Problem Persists

External connections, accessories, cable condition, clinical catheter placement, interference, and normal configuration have been ruled out. The remaining problem may involve the Edi interface, internal communication, signal-processing hardware, or another service-level fault.

The Servo-n should be:
- Removed from NAVA-dependent service
- Labeled Out of Service when the fault affects intended use
- Sent for repair or bench evaluation
- Evaluated with appropriate Getinge documentation and approved test equipment
- Repaired or configured only by qualified personnel

Complete required functional verification before returning NAVA/Edi functionality to clinical service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A visible Edi waveform is not enough by itself; ensure the complete Edi/NAVA signal path remains stable before clinical dependence on NAVA resumes.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect ventilation first, then separate clinical placement issues from equipment, cable, accessory, and interference problems. Escalate when the external signal path is verified but reliable Edi acquisition cannot be restored.

That is successful troubleshooting.
