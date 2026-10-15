---
schemaVersion: 1
title: "GE Healthcare CardioLab Electrophysiology Recording System - Gantry, Table, or Positioning Motion Is Unavailable"
issueTitle: "Gantry, Table, or Positioning Motion Is Unavailable"
description: "Associated EP-lab table or positioning motion is unavailable while using CardioLab because of interlocks, external controls, connections, or integrated-system communication."
assetType: "Electrophysiology Recording System"
manufacturer: "GE Healthcare"
model: "CardioLab"
slug: "ge-healthcare-cardiolab-gantry-table-or-positioning-motion-is-unavailable"
dateAdded: "2026-10-15"
taxonomyMode: "reuse"
ccr:
  complaint: "EP staff reported that table positioning was unavailable during setup for a CardioLab procedure."
  cause: "Clinical Engineering found the external table hand-control connector partially disengaged."
  resolution: "The connector was reseated, table movement and stopping functions were verified through the approved controls, and the equipment was returned to service."
helpfulDetails:
  - "Exact movement unavailable"
  - "Control station or pedal used"
  - "Emergency-stop condition"
  - "Obstructions found"
  - "External cable condition"
  - "Whether other motion directions worked"
  - "Associated imaging or table-system status"
  - "Control comparison results"
  - "Communication indicators"
  - "Results before and after correction"
  - "Final motion verification"
  - "Final device status"
---

## What This Guide Helps With

Associated EP-lab table or positioning motion is unavailable while using CardioLab because of interlocks, external controls, connections, or integrated-system communication.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Unintended Movement

Do not troubleshoot positioning equipment while a patient depends on unstable or unreliable motion control. Notify the clinical team, secure the patient appropriately, and prevent unintended table or accessory movement.

Determine whether CardioLab itself is affected or whether the reported motion problem belongs to an integrated imaging or procedure-table system.

**Expected outcome:** The patient is protected from unintended motion and the affected subsystem is correctly identified.

If the motion problem is unrelated to CardioLab, route the issue to the responsible equipment service pathway.

### 2. Confirm the Exact Motion Complaint

Ask which motion is unavailable, which control was used, whether any movement remains available, and whether the condition began after repositioning equipment or connecting accessories.

Observe the issue without commanding unnecessary movement around the patient.

**Expected outcome:** The failed motion and responsible control path are clearly identified.

If the reported issue was caused by use of the wrong control station and normal movement is confirmed, troubleshooting can stop.

### 3. Check External Emergency Stops and Motion Inhibits

Inspect accessible emergency-stop controls, collision stops, pedals, hand controls, and other externally visible motion-inhibit conditions associated with the table or imaging system.

Do not reset an emergency or safety interlock until the reason for its activation is understood and it is safe to do so.

**Expected outcome:** No external safety control is unintentionally preventing movement.

If a safely correctable external inhibit is cleared and motion returns normally, verify all required movement and stop troubleshooting.

### 4. Inspect External Control and Interface Connections

Check accessible table-control, pedal, hand-control, network, and interface cables for loose plugs, damaged connectors, pinching, or strain.

For CardioLab-integrated environments, confirm that any external interface used for procedural synchronization or system communication remains connected.

**Expected outcome:** Required external controls and communications are securely connected and physically intact.

If reconnecting an approved external control restores motion, verify safe operation and stop troubleshooting.

### 5. Check Positioning and Collision Conditions

Look for equipment, cables, patient-support accessories, stools, carts, or other objects that may obstruct movement or trigger a collision-protection condition.

Verify that cables have enough slack for intended motion and are not caught on surrounding equipment.

**Expected outcome:** The movement path is clear and no external obstruction prevents positioning.

If removing an obstruction restores safe motion, perform a controlled verification and stop troubleshooting.

### 6. Verify Associated System Readiness

Check whether the integrated imaging or table-control system reports that it is ready for motion. Confirm that required components have completed startup and have not lost communication.

Do not enter restricted service menus or bypass motion interlocks.

**Expected outcome:** Associated positioning equipment is powered, ready, and not reporting an unresolved safety condition.

If normal motion returns after restoring external readiness or communication, verify operation and stop troubleshooting.

### 7. Compare Available Control Points

When permitted, determine whether the affected motion fails from one control only or from all approved controls. A motion that works from one control but not another may indicate an external hand control, pedal, or control-station problem rather than a drive-system failure.

**Expected outcome:** The problem is isolated to a specific external control or confirmed across the positioning system.

If a replaceable external control is identified and a known-good approved substitute restores normal function, complete verification and stop troubleshooting.

### 8. Perform Final Functional Verification

With the equipment clear of the patient or under an approved controlled test condition, verify required motion directions, stopping behavior, external controls, and communication with the surrounding EP-lab workflow.

Do not return equipment to service if movement is intermittent, uncontrolled, or inconsistent.

**Expected outcome:** Positioning motion operates predictably and all required safety functions remain intact.

If all applicable tests pass, troubleshooting is complete.

### 9. Escalate Unresolved Motion Problems

If motion remains unavailable after external controls, connections, obstructions, system readiness, and communication have been checked, remove the affected positioning equipment from service as appropriate.

Do not bypass safety interlocks or attempt internal motor, drive, controller, or board-level repair.

**Expected outcome:** Unsafe or unavailable motion is escalated for qualified evaluation.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve the associated table or imaging system, motion-control electronics, interlocks, managed integration, internal drive hardware, or another service-level condition rather than CardioLab itself.

The affected equipment should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation as appropriate.
- Evaluated using applicable manufacturer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Return to service only after controlled positioning and safety-function verification. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Prevent unintended patient or equipment movement and identify which integrated EP-lab subsystem actually owns the failed motion before beginning corrective work.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Start by protecting the patient and identifying whether CardioLab or another integrated EP-lab system owns the motion function. Rule out external controls, obstructions, connections, and readiness conditions before escalating an unresolved motion problem.

That is successful troubleshooting.
