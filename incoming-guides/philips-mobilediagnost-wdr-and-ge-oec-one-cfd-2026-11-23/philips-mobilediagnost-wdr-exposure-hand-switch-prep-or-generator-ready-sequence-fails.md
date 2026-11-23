---
schemaVersion: 1
title: "Philips MobileDiagnost wDR Mobile X-Ray System - Exposure Hand Switch, Prep, or Generator Ready Sequence Fails"
issueTitle: "Exposure Hand Switch, Prep, or Generator Ready Sequence Fails"
description: "Troubleshoots exposure-control, prep, ready, connection, interlock, detector, and generator-sequence problems before assuming an internal generator failure."
assetType: "Mobile X-Ray System"
manufacturer: "Philips"
model: "MobileDiagnost wDR"
slug: "philips-mobilediagnost-wdr-exposure-hand-switch-prep-or-generator-ready-sequence-fails"
dateAdded: "2026-11-23"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported that pressing the MobileDiagnost wDR exposure hand switch initiated prep intermittently but did not consistently proceed to exposure."
  cause: "Clinical Engineering found the external hand-switch connector was not fully seated."
  resolution: "Clinical Engineering reseated and secured the connection and verified repeated prep, ready, exposure, and image-acquisition sequences using approved testing."
helpfulDetails:
  - "Exact failed sequence stage"
  - "Console message or indicator"
  - "Hand-switch condition"
  - "Cable and strain-relief condition"
  - "Detector readiness"
  - "Safety-interlock status"
  - "Whether restart changed the symptom"
  - "Approved alternate-control comparison"
  - "Final exposure test result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots exposure-control, prep, ready, connection, interlock, detector, and generator-sequence problems before assuming an internal generator failure.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Unreliable Exposure Attempts
Do not repeatedly attempt exposures on a patient while the prep or exposure sequence is unreliable.

Move the examination to another verified system when timely imaging is required.

Expected outcome: The patient is not subjected to repeated failed or unintended exposure attempts.

### 2. Confirm the Exact Exposure Failure
Determine whether:
- Prep does not start
- Prep starts but ready is never reached
- Ready appears but exposure does not occur
- The hand switch is intermittent
- Exposure stops unexpectedly
- The detector or system reports not ready

Observe normal system messages and indicators.

Expected outcome: The failed stage of the exposure sequence is identified. If the sequence operates normally on repeated testing, perform final verification and stop troubleshooting.

### 3. Verify Normal System Startup and Readiness
Confirm that the unit has completed startup and is not displaying an unresolved fault or condition that inhibits exposure.

Verify that an appropriate examination and detector are selected through normal workflow.

Expected outcome: The system is in a normal condition where an exposure request should be accepted.

### 4. Inspect the Exposure Hand Switch
Check the hand switch and its accessible cable for:
- Cuts
- Crushing
- Bent strain relief
- Loose connection
- Sticky buttons
- Intermittent response when the cable is moved gently

Do not open or internally repair the switch unless authorized by service procedures.

Expected outcome: The hand switch is physically intact and responds consistently. If reseating an approved external connection restores reliable operation, verify repeated prep and exposure sequencing.

### 5. Verify Detector Readiness
Confirm that the selected detector is awake, connected, and ready for acquisition.

A detector communication or preparation failure can prevent the generator sequence from progressing normally.

Expected outcome: Detector status is normal and does not inhibit exposure. If restoring detector readiness resolves the sequence, verify acquisition and stop troubleshooting.

### 6. Check External Safety and Position Conditions
Verify that no emergency stop, collision condition, parking requirement, or other externally apparent safety state is preventing normal operation.

Do not bypass interlocks.

Expected outcome: No obvious safety interlock is blocking the exposure sequence.

### 7. Restart the System Using Normal Controls
When clinical workflow permits, shut down and restart the MobileDiagnost wDR normally.

Reassess the prep, ready, and exposure sequence without entering restricted service modes.

Expected outcome: The generator and exposure controls initialize normally. If the fault clears and remains absent during repeated testing, continue to final verification.

### 8. Compare With Another Approved Exposure Control When Applicable
If the system has another approved normal exposure-control method available, compare operation to help isolate a hand-switch-specific problem.

Do not substitute non-approved switches or bypass exposure controls.

Expected outcome: A second approved control helps determine whether the fault follows the hand switch or remains with the system.

### 9. Perform Functional Verification
Using approved test procedures, verify:
- Prep initiates
- Ready indication occurs
- Exposure request is accepted
- Exposure completes normally
- Detector captures the image
- No unexpected faults appear

Expected outcome: The complete exposure sequence operates repeatedly and predictably. Troubleshooting can stop.

### 10. Escalate an Unresolved Exposure Failure
If prep, ready, or exposure remains unreliable, remove the system from clinical use and refer it for qualified service.

Expected outcome: An unreliable radiation-producing system is not returned to patient use without proper evaluation.

## If the Problem Persists

Common external causes such as hand-switch condition, detector readiness, system startup, external interlocks, and basic workflow configuration have been ruled out.

The remaining problem may involve generator control, exposure-switch circuitry, internal interlocks, communication between system components, or another service-level fault.

The device should be:
- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Philips documentation and approved radiation test equipment
- Repaired or configured only by qualified personnel

Complete appropriate generator and exposure-sequence testing before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never repeatedly cycle prep or exposure on a patient when the system does not reliably indicate and complete the expected exposure sequence.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Radiation safety comes first. Identify the exact stage where the sequence stops and verify the hand switch, detector, system state, and external interlocks before assuming a generator problem. Escalate unresolved exposure faults and document the verified corrective action and final test result.

That is successful troubleshooting.
