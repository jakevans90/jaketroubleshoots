---
schemaVersion: 1
title: "Samsung Healthcare GM85 Fit Mobile X-Ray System - Exposure or Scan Will Not Start or Is Aborted"
issueTitle: "Exposure or Scan Will Not Start or Is Aborted"
description: "Addresses exposures that will not initiate or abort because of readiness, detector, control, interlock, connection, power, or acquisition conditions."
assetType: "Mobile X-Ray System"
manufacturer: "Samsung Healthcare"
model: "GM85 Fit"
slug: "samsung-healthcare-gm85-fit-exposure-or-scan-will-not-start-or-is-aborted"
dateAdded: "2026-09-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology staff reported that the GM85 Fit reached the bedside but would not initiate an exposure."
  cause: "Clinical Engineering found the external exposure hand-switch connector partially disengaged."
  resolution: "Clinical Engineering securely reconnected the exposure control, completed approved nonpatient exposure testing, and verified reliable operation before return to service."
helpfulDetails:
  - "Exact message or symptom"
  - "Whether preparation reached ready status"
  - "Detector readiness"
  - "Exposure-control condition"
  - "Battery and AC status"
  - "Recent collision, drop, or fluid exposure"
  - "Whether the exposure never started or aborted"
  - "Results of approved nonpatient testing"
  - "Repeatability after correction"
  - "Final device status"
---
## What This Guide Helps With

Addresses exposures that will not initiate or abort because of readiness, detector, control, interlock, connection, power, or acquisition conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Prevent Unnecessary Exposure
Do not repeatedly attempt patient exposures while troubleshooting. If clinically necessary imaging cannot be completed promptly, move the examination to another verified system.

Expected outcome: No unnecessary radiation exposure occurs while the failure is investigated.

### 2. Confirm the Exact Failure
Determine whether the system never reaches ready status, the exposure control does nothing, an exposure starts and aborts, or the system returns a message.

Record the exact displayed message and circumstances.

Expected outcome: The failure is reproducible and clearly categorized. If the condition cannot be reproduced, continue checking for intermittent external causes before returning to service.

### 3. Confirm System and Detector Readiness
Verify the console shows the system and intended detector in the expected ready state.

Resolve detector-not-ready conditions before troubleshooting exposure generation itself.

Expected outcome: Detector and acquisition systems are available. If correcting detector readiness restores exposures, complete functional verification and stop troubleshooting.

### 4. Check Exposure Controls and Connections
Inspect the hand switch, exposure control, cable, connector, and accessible strain relief for damage, looseness, sticking, or contamination.

Confirm the control is connected as intended. Do not bypass or jumper exposure-control circuits.

Expected outcome: The exposure control is intact, connected, and responds normally. If reseating a loose approved connection restores operation, verify and stop.

### 5. Verify System Position and Operating State
Confirm the system is not in transport, shutdown, charging-only, error, or another operating state that prevents exposure.

Verify any normal operator-accessible preparation steps are complete without changing protected configuration.

Expected outcome: The system enters the expected acquisition-ready state.

### 6. Verify Power and Battery Condition
Confirm sufficient battery state and stable system power. If the unit behaves differently while connected to a verified AC source, document the difference.

Expected outcome: Exposure operation is not being prevented by an inadequate system power condition. If restoring the proper power state corrects the issue, complete final verification.

### 7. Inspect for External Damage or Recent Events
Ask whether the unit was dropped, collided with equipment, exposed to fluid, abruptly powered down, or moved immediately before the problem occurred.

Inspect accessible exterior areas for signs of impact.

Expected outcome: No external event suggests unsafe internal damage. If significant impact or liquid intrusion is identified, remove the system from service.

### 8. Perform an Approved Nonpatient Exposure Test
Using facility-approved procedures, an appropriate test object, and required radiation-safety precautions, perform a controlled functional exposure test.

Do not use a patient to confirm whether an intermittent system problem remains.

Expected outcome: The exposure initiates, completes without aborting, and produces the expected acquisition result. If so, troubleshooting can stop after final verification.

### 9. Confirm Repeatability
Where appropriate, repeat the approved functional test sufficiently to establish that the problem is not intermittent.

Expected outcome: Exposure initiation and completion remain reliable. Intermittent exposure operation requires removal from service even if one test succeeds.

## If the Problem Persists

If detector readiness, exposure controls, external connections, system state, and power condition have been verified, common external causes have been ruled out.

Possible remaining categories include generator control, exposure-switch circuitry, acquisition synchronization, internal communication, software, power electronics, or safety-interlock faults.

The system should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate Samsung Healthcare documentation and approved X-ray test equipment.
- Repaired or configured only by qualified personnel.

Complete required radiation-output, acquisition, image-quality, and safety verification before clinical return.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Never use repeated patient exposures to determine whether an intermittent exposure fault has cleared.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Exposure troubleshooting must minimize radiation risk, verify readiness and external controls before assuming generator failure, prove reliable operation using appropriate nonpatient testing, and escalate any persistent or intermittent condition.

That is successful troubleshooting.
