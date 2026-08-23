---
schemaVersion: 1
title: "Philips Zenition Series C-Arm - Fluoroscopy Footswitch or Hand Switch Not Working"
issueTitle: "Fluoroscopy Footswitch or Hand Switch Not Working"
description: "Addresses nonresponsive exposure controls caused by loose connections, damaged accessories, contamination, cable problems, control selection, or system readiness."
assetType: "C-Arm"
manufacturer: "Philips"
model: "Zenition Series"
slug: "philips-zenition-series-fluoroscopy-footswitch-or-hand-switch-not-working"
dateAdded: "2026-08-22"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the Philips Zenition Series footswitch would not activate fluoroscopy, although the hand switch still worked."
  cause: "Clinical Engineering found damage to the footswitch cable near the strain relief."
  resolution: "The damaged footswitch was removed from service, replaced with an approved known-good footswitch, and reliable fluoroscopy activation and release were verified."
helpfulDetails:
  - "Whether the footswitch, hand switch, or both failed."
  - "System X-ray readiness."
  - "Cable and strain-relief condition."
  - "Connector condition."
  - "Evidence of fluid intrusion."
  - "Results with each exposure control."
  - "Known-good substitution result."
  - "Whether the problem was intermittent or complete."
  - "Results after restart."
  - "Final activation and release verification."
---
## What This Guide Helps With

Addresses nonresponsive exposure controls caused by loose connections, damaged accessories, contamination, cable problems, control selection, or system readiness.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Reliance on the Failed Control

Do not continue a procedure using an unreliable exposure switch. If imaging is required, use another verified exposure control only if its operation is confirmed and facility workflow permits, or exchange the C-arm.

Determine whether the footswitch, hand switch, or both are affected.

**Expected outcome:** The patient is not dependent on an unreliable exposure control, and the affected control is identified.

### 2. Confirm the System Is Otherwise Ready for X-Ray

Verify that the Zenition Series has completed startup and shows normal imaging readiness. Confirm there is no broader X-ray inhibit, detector-not-ready condition, or system communication failure.

**Expected outcome:** The system is ready for imaging and the complaint is isolated to the exposure control.

If all controls fail and the system itself is not X-ray ready, troubleshoot the broader exposure-inhibit condition instead.

### 3. Inspect the Footswitch or Hand Switch

Check the accessory housing, switch surfaces, cable, strain relief, and connector for damage, contamination, cuts, crushed sections, bent pins, or evidence of fluid intrusion. Inspect cable routing for pinching under wheels or equipment.

Do not use a damaged or fluid-contaminated exposure control.

**Expected outcome:** The accessory is physically intact and safe for further testing.

If damage or fluid intrusion is found, remove the accessory from service and replace it with an approved known-good unit before continuing.

### 4. Verify the External Connection

Confirm that the footswitch or hand switch is connected to the correct accessible port and is fully seated. If necessary, power the system down appropriately before disconnecting and reseating the accessory.

Do not force keyed connectors.

**Expected outcome:** The exposure-control connection is secure and correctly installed.

If reseating the connector restores operation, proceed to final functional verification.

### 5. Compare Footswitch and Hand-Switch Operation

When both controls are available, test them independently according to approved radiation-safety practices. Observe whether one control activates imaging while the other does not.

**Expected outcome:** The problem is isolated to one accessory or shown to affect the system globally.

If one switch operates correctly and the other does not, keep the failed switch out of service and continue with a known-good replacement.

### 6. Substitute a Known-Good Compatible Control

If an approved compatible footswitch or hand switch is available, connect the known-good accessory using normal procedures and retest.

**Expected outcome:** The known-good control operates normally if the original exposure accessory is faulty.

If the known-good control works, replace or route the original accessory for repair and stop troubleshooting after final verification.

### 7. Check User-Accessible Control and Workflow Conditions

Verify that the system is in the intended imaging mode and that no user-accessible workflow state is preventing the selected control from operating. Compare the configuration with a known-good Zenition system when appropriate.

Do not change restricted configuration or service settings.

**Expected outcome:** Normal user-accessible settings support operation of the selected exposure control.

### 8. Restart the System Once if Needed

If the accessory and its connection appear normal but the control remains unresponsive, perform a controlled shutdown and restart using normal procedures. Retest after the system reaches full readiness.

**Expected outcome:** The control either resumes normal operation or the failure remains consistent for escalation.

### 9. Perform Final Functional Verification

Verify the repaired or replacement exposure control activates imaging predictably, releases correctly, and does not produce intermittent operation. Confirm imaging terminates when the switch is released and that normal system status is maintained.

Use approved test objects and radiation-safety procedures.

**Expected outcome:** The exposure control operates reliably through repeated functional checks.

If successful, troubleshooting can stop and the equipment may be returned to service.

### 10. Escalate Persistent Control Failure

If known-good exposure controls also fail despite normal system readiness and secure external connections, stop external troubleshooting.

**Expected outcome:** A likely system-side control or communication problem is recognized and the equipment is withheld from clinical use.

## If the Problem Persists

Common external accessory, connector, cable, readiness, and workflow causes have been ruled out. The remaining issue may involve the system-side control interface, internal communication circuitry, configuration, or another service-level condition.

The system should be:

- Removed from service when dependable exposure control cannot be assured.
- Labeled Out of Service.
- Sent for repair or qualified bench/service evaluation.
- Evaluated using approved Philips documentation and test equipment.
- Repaired or configured only by qualified personnel.

Do not bypass an exposure-control circuit or attempt internal board-level repair. Complete functional and applicable radiation-safety verification before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A switch that works intermittently is not acceptable for clinical use; replace the accessory or exchange the C-arm before continuing the procedure.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Exposure controls are safety-critical. Isolate the complaint to the accessory or system, verify connectors and known-good substitutions before assuming internal failure, and remove unreliable controls from service with clear CCR documentation.

That is successful troubleshooting.

