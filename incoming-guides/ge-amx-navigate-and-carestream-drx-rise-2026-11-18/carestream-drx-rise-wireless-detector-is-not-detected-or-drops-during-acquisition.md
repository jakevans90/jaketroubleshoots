---
schemaVersion: 1
title: "Carestream DRX-Rise Mobile X-Ray System - Wireless Detector Is Not Detected or Drops During Acquisition"
issueTitle: "Wireless Detector Is Not Detected or Drops During Acquisition"
description: "Troubleshoot detector recognition, intermittent wireless connection, acquisition dropout, detector power, positioning, pairing, and local wireless communication problems."
assetType: "Mobile X-Ray System"
manufacturer: "Carestream"
model: "DRX-Rise"
slug: "carestream-drx-rise-wireless-detector-is-not-detected-or-drops-during-acquisition"
dateAdded: "2026-11-18"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported that the DRX-Rise wireless detector repeatedly disconnected before image acquisition."
  cause: "Clinical Engineering found the detector battery was not fully seated, causing intermittent detector power and communication loss."
  resolution: "Reseated the detector battery, inspected the contacts, and verified repeated detector recognition and successful test acquisitions without dropout."
helpfulDetails:
  - "Exact communication message"
  - "Detector identification"
  - "Detector battery status"
  - "Whether connection loss occurs during movement or acquisition"
  - "Physical condition of detector and battery"
  - "Detector selected by the system"
  - "Known-good detector comparison"
  - "Locations where dropout occurred"
  - "Results of repeated test acquisitions"
  - "Final detector and system status"
---

## What This Guide Helps With

Troubleshoot detector recognition, intermittent wireless connection, acquisition dropout, detector power, positioning, pairing, and local wireless communication problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Imaging Continuity
Do not continue troubleshooting while a patient is positioned for an examination that depends on the unreliable detector. Move the examination to another verified detector or imaging system when necessary.  
Expected outcome: Patient care continues without depending on an intermittently connected detector. Stop troubleshooting clinically if an alternate verified system is required.

### 2. Confirm the Exact Detector Failure
Determine whether the detector is never recognized, disconnects only during positioning, drops during exposure preparation, or reconnects intermittently. Record any displayed communication message without assuming the detector itself has failed.  
Expected outcome: The failure pattern is clearly reproduced or documented.

### 3. Verify Detector Power and Charge State
Inspect the detector for normal power indication and adequate charge. Confirm the battery is properly installed if removable and that battery contacts and accessible detector surfaces show no contamination, damage, or deformation.  
Expected outcome: Detector powers normally and remains powered. If restoring detector power resolves recognition, verify operation and stop.

### 4. Inspect the Detector and External Interfaces
Check the detector enclosure, accessible connectors, battery interface, protective cover, and any docking or charging contacts for physical damage or contamination. Do not use a detector with impact damage, liquid intrusion, cracked housing, or damaged connectors.  
Expected outcome: Detector is physically intact and external interfaces are clean and secure.

### 5. Check Detector Selection and System Status
Verify the intended detector is selected or available to the DRX-Rise system and that another detector is not unintentionally active. Avoid unauthorized pairing, network, or service configuration changes.  
Expected outcome: The correct detector is shown as available and selected for acquisition. If incorrect selection caused the issue, correct it, verify acquisition, and stop.

### 6. Evaluate Position and Wireless Environment
Test the detector near the mobile system in a normal acquisition position. Look for shielding, unusual distance, placement behind dense structures, or local RF/environmental conditions that correlate with disconnects.  
Expected outcome: Detector remains connected in a normal working position. If repositioning eliminates the problem consistently, document the environmental cause and stop after verification.

### 7. Perform a Known-Good Comparison
When available and approved for the system, test a known-good compatible detector or test the reported detector on another appropriate system. Change only one variable at a time.  
Expected outcome: The comparison isolates the problem to the detector, mobile system, or local environment.

### 8. Verify Acquisition Stability
Using appropriate test conditions and without exposing a patient, confirm the detector remains connected through detector selection, preparation, permitted test acquisition, image receipt, and post-acquisition processing.  
Expected outcome: Detector remains continuously recognized and the image transfers normally. If successful repeatedly, troubleshooting can stop.

### 9. Escalate an Unresolved Connection Problem
If detector communication remains intermittent after external causes, power, selection, positioning, and known-good comparisons are checked, remove the affected detector or system from clinical use as appropriate.  
Expected outcome: Unreliable imaging equipment is prevented from returning to patient use until bench evaluation or authorized service is completed.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities include detector hardware, wireless communication hardware, system configuration, software, or infrastructure-level problems.

Remove the affected equipment from service, label it **Out of Service**, and send it for repair or bench evaluation. Evaluate it using appropriate Carestream documentation and approved test equipment. Repair, pairing changes, calibration, or configuration changes should be completed only by qualified personnel.

Before return to service, verify reliable detector recognition, stable acquisition, image transfer, and any required image-quality functions.

Knowing when to stop external troubleshooting and escalate an intermittent detector problem is proper troubleshooting.

## Clinical Use Tip

Do not acquire patient images with a detector that has demonstrated intermittent communication until stable operation has been verified.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient first, verify detector power and external conditions before assuming an internal failure, confirm stable acquisition after correction, escalate intermittent problems appropriately, and document the complaint, cause, and resolution clearly.

That is successful troubleshooting.
