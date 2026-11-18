---
schemaVersion: 1
title: "GE Healthcare AMX Navigate Mobile X-Ray System - Exposure Is Inhibited or Prep/Expose Switch Does Not Complete the Sequence"
issueTitle: "Exposure Is Inhibited or Prep/Expose Switch Does Not Complete the Sequence"
description: "The system will not prepare or expose, exposure is inhibited, or the exposure control does not complete the expected sequence."
assetType: "Mobile X-Ray System"
manufacturer: "GE Healthcare"
model: "AMX Navigate"
slug: "ge-healthcare-amx-navigate-exposure-is-inhibited-or-prep-expose-switch-does-not-complete-the-sequence"
dateAdded: "2026-11-18"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported the AMX Navigate would enter prep but would not complete an exposure when the hand switch was pressed."
  cause: "Clinical Engineering found damage at the exposure-switch cable that caused intermittent operation."
  resolution: "Replaced the approved exposure control, verified reliable prep and expose operation using a controlled non-patient test, and returned the unit to service."
helpfulDetails:
  - "Exact inhibit or status message"
  - "Whether prep occurred"
  - "Whether exposure occurred"
  - "Hand-switch condition"
  - "Cable and connector condition"
  - "Detector availability"
  - "Battery state"
  - "Emergency-stop status"
  - "Known-good switch result"
  - "Functional exposure-test result"
  - "Final device status"
---

## What This Guide Helps With

The system will not prepare or expose, exposure is inhibited, or the exposure control does not complete the expected sequence.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Prevent Unintended Exposure
Do not repeatedly operate the exposure control around a patient while determining why the sequence is failing. Use a controlled test environment and follow facility radiation-safety procedures.

Expected outcome: Troubleshooting can proceed without unnecessary radiation exposure.

### 2. Confirm the Exact Sequence Failure
Determine whether:
- Prep does not begin
- Prep occurs but exposure does not occur
- The switch feels mechanically abnormal
- The system displays an inhibit
- The sequence fails only in one operating mode
- The problem is intermittent

Record any displayed status or inhibit message exactly.

Expected outcome: The failure point in the prep/expose sequence is established.

### 3. Verify Normal System Readiness
Confirm the AMX Navigate completes normal startup, has adequate battery charge, and is not reporting another condition that intentionally prevents exposure.

Expected outcome: The system reaches its normal ready state.

### 4. Verify the Detector Is Available
Confirm the selected detector is connected, recognized, ready, and appropriately selected for the examination. A detector communication problem may prevent normal exposure workflow.

Expected outcome: The intended detector is available for acquisition.

### 5. Verify Examination and Acquisition Setup
Confirm a valid examination or approved test workflow has been selected and that required acquisition selections are complete. Do not alter protected configuration parameters simply to bypass an inhibit.

Expected outcome: The system has the required normal workflow information to permit exposure.

### 6. Inspect the Prep/Expose Control
Inspect the hand switch or exposure control and its accessible cable for:
- Cracks
- Pinching
- Cuts
- Loose connector seating
- Bent or damaged connector areas
- Sticking buttons
- Abnormal tactile response

Expected outcome: The switch and cable are physically intact and securely connected.

### 7. Reseat Accessible Connections
With the system in a safe state, reseat the normal external exposure-control connection where permitted.

Expected outcome: The exposure control is securely connected. If the sequence is restored, continue to final verification.

### 8. Substitute a Known-Good Approved Exposure Control
If a compatible known-good hand switch or exposure control is available, substitute it without opening the system.

Expected outcome: If the known-good control restores operation, the original control or cable is isolated as the likely cause.

### 9. Check for Other Safety Inhibits
Verify that emergency-stop, collision, detector, generator-readiness, or other normal system status conditions are not preventing operation. Do not bypass a safety interlock.

Expected outcome: No active safety condition is blocking the sequence.

### 10. Perform an Approved Functional Exposure Test
Using facility-approved radiation-safety procedures, a suitable test object, and no patient, verify the prep and exposure sequence.

Expected outcome: Prep initiates correctly and the exposure completes normally. If successful, troubleshooting can stop.

### 11. Escalate an Unresolved Exposure Inhibit
If prep/expose remains unreliable after the switch, detector, workflow, system readiness, and accessible connections have been checked, remove the system from clinical use.

Expected outcome: A unit with unreliable exposure control is not used on patients.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve exposure-control circuitry, generator readiness, safety-interlock logic, internal wiring, detector communication, system configuration, or other service-level faults.

The system should be:
- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare service documentation and approved X-ray test equipment
- Repaired or configured only by qualified personnel

Return-to-service testing should verify normal prep, exposure initiation, exposure termination, image acquisition, and applicable radiation-safety functions.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never bypass an exposure inhibit or safety interlock to obtain an image; identify why the system is preventing exposure.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Exposure problems require disciplined troubleshooting because the system may be intentionally inhibiting radiation for a valid reason. Verify external controls, detector readiness, workflow, and safety conditions before escalating to generator or internal-system evaluation.

That is successful troubleshooting.
