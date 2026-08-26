---
schemaVersion: 1
title: "Siemens Healthineers Cios Spin C-Arm - Fluoroscopy Footswitch or Hand Switch Not Working"
issueTitle: "Fluoroscopy Footswitch or Hand Switch Not Working"
description: "Addresses failed exposure-control activation caused by loose connections, damaged cables, control selection, contamination, physical damage, or system readiness conditions."
assetType: "C-Arm"
manufacturer: "Siemens Healthineers"
model: "Cios Spin"
slug: "siemens-healthineers-cios-spin-fluoroscopy-footswitch-or-hand-switch-not-working"
dateAdded: "2026-08-26"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported the Cios Spin footswitch intermittently failed to start fluoroscopy."
  cause: "Clinical Engineering found visible damage at the footswitch cable strain relief and confirmed normal operation with a compatible known-good control."
  resolution: "The damaged footswitch was replaced, activation and release were verified through repeated functional testing, and the C-arm was returned to service."
helpfulDetails:
  - "Footswitch or hand switch affected."
  - "Specific pedal or button affected."
  - "Physical condition."
  - "Connector condition."
  - "Cable routing."
  - "Known-good control results."
  - "Imaging-ready status."
  - "Any inhibit message."
  - "Restart results."
  - "Activation and release verification."
  - "Final device status."
---

## What This Guide Helps With
Addresses failed exposure-control activation caused by loose connections, damaged cables, control selection, contamination, physical damage, or system readiness conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Prevent Uncontrolled Imaging
If an exposure control does not function reliably during a procedure, stop depending on that control. Provide another approved exposure method or verified imaging system if clinically required.

If a switch sticks, activates intermittently, or could cause unintended radiation, immediately remove it from use.

**Expected outcome:** No patient or staff member is exposed to unreliable or unintended radiation activation.

### 2. Confirm Which Control and Function Are Affected
Determine whether the problem involves:
- Footswitch only.
- Hand switch only.
- One pedal or button.
- Fluoroscopy only.
- Other exposure functions.
- Both footswitch and hand switch.

Confirm whether the system otherwise indicates X-ray ready.

**Expected outcome:** The problem is isolated to a specific control, function, or broader imaging issue.

### 3. Inspect the Control Externally
Examine the footswitch or hand switch for:
- Cracks.
- Liquid contamination.
- Debris.
- Damaged housing.
- Sticking controls.
- Frayed or crushed cable.
- Damaged strain relief.
- Bent or damaged connector hardware.

Do not open the switch housing unless specifically authorized by applicable service documentation.

**Expected outcome:** The control is physically intact and suitable for further testing. Damaged or contaminated controls are removed from service.

### 4. Verify the Connector Is Fully Seated
Trace the control cable to its system connection and verify it is correctly inserted and secured.

Look for a connector disturbed by transport, cable tension, equipment movement, or cleaning.

Disconnect and reconnect only accessible connectors using the appropriate powered-down condition when required.

**Expected outcome:** The system recognizes a securely connected exposure control. If operation returns, continue to verification.

### 5. Check Cable Routing and Position
Verify the switch cable is not:
- Trapped under a wheel.
- Stretched by C-arm movement.
- Pinched by equipment.
- Wrapped tightly around the cart.
- Subjected to repeated bending at the strain relief.

Reposition the cable to remove mechanical stress.

**Expected outcome:** The control operates without cable-position-dependent interruption.

### 6. Compare With Another Approved Exposure Control
If available, test the alternate approved exposure control.

Examples include comparing the footswitch response with the hand switch or using an approved known-good compatible control.

Do not substitute an unapproved accessory.

**Expected outcome:** If the alternate control works normally, the original external switch or cable is strongly isolated as the cause. Troubleshooting may stop after replacement and verification.

### 7. Verify System Readiness and Mode
If neither control works, confirm the Cios Spin is fully initialized, the detector is ready, no exposure-inhibit condition is active, and the selected workflow permits imaging.

A system-level inhibit can appear to be a failed switch.

**Expected outcome:** The system is ready to accept an exposure command.

### 8. Perform a Controlled Restart if Needed
If controls are intact and connected but appear unrecognized after a software or communication interruption, perform one controlled restart.

Recheck recognition after normal initialization.

**Expected outcome:** Exposure controls are recognized and respond normally after restart.

### 9. Verify Activation and Release
Using approved radiation-safety practices and a suitable test object, verify:
- The intended control initiates fluoroscopy or exposure.
- Activation occurs only when commanded.
- Exposure terminates immediately when the control is released.
- Each intended pedal or button performs its expected function.
- No intermittent response occurs when the cable is positioned normally.

**Expected outcome:** The exposure control operates consistently and safely. Troubleshooting can stop.

### 10. Escalate Unresolved Control Problems
If known-good external controls also fail or exposure-control recognition remains unreliable, remove the C-arm from service.

Do not bypass the switch, short connector contacts, or defeat radiation-control circuitry.

**Expected outcome:** An unreliable radiation-control system is prevented from clinical use.

## If the Problem Persists
After accessible connectors, control condition, cable routing, known-good substitutions, system readiness, and restart have been ruled out, the cause may involve internal exposure-control interfaces, communication hardware, safety circuitry, configuration, or another service-level condition.

The Cios Spin should be:
- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench/service evaluation.
- Evaluated with Siemens Healthineers documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Complete exposure-control, radiation-safety, and imaging verification before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
A sticking or intermittent exposure switch is a radiation-safety issue and should be removed from use immediately rather than worked around.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**


## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Treat exposure controls as safety-critical components, eliminate simple connection and accessory causes first, verify both activation and release, and escalate any unresolved or intermittent behavior.

That is successful troubleshooting.
