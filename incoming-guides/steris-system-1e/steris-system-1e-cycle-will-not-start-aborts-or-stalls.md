---
schemaVersion: 1
title: "STERIS SYSTEM 1E Endoscope Reprocessor (AER) - Cycle Will Not Start, Aborts, or Stalls"
issueTitle: "Cycle Will Not Start, Aborts, or Stalls"
description: "Troubleshoots cycles that will not begin, stop unexpectedly, or remain in one phase because of loading, utility, consumable, door, or external conditions."
assetType: "Endoscope Reprocessor (AER)"
manufacturer: "STERIS"
model: "SYSTEM 1E"
slug: "steris-system-1e-cycle-will-not-start-aborts-or-stalls"
dateAdded: "2026-09-21"
taxonomyMode: "reuse"
ccr:
  complaint: "Sterile Processing reported the SYSTEM 1E cycle would not start and repeatedly returned to a not-ready condition."
  cause: "Clinical Engineering found the processing load positioned so that the door could not achieve proper closure."
  resolution: "Corrected the load position, verified proper door closure, and completed a full functional cycle without alarms before returning the unit to service."
helpfulDetails:
  - "Exact phase where the cycle stopped"
  - "Displayed message or alarm"
  - "Load type"
  - "Accessory and connector condition"
  - "Consumable status"
  - "Door and latch condition"
  - "Water and drain availability"
  - "Whether failure repeats unloaded or with another approved setup"
  - "Results of verification cycle"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots cycles that will not begin, stop unexpectedly, or remain in one phase because of loading, utility, consumable, door, or external conditions.

## Step-by-Step Troubleshooting
### 1. Protect the Load and Maintain Reprocessing Continuity
Treat any cycle that did not complete normally as unsuccessful unless facility and manufacturer procedures explicitly establish otherwise. Do not release affected devices for patient use. Transfer processing to another validated system if needed.

**Expected outcome:** Potentially incompletely processed devices remain segregated and clinical workflow continues safely. Troubleshoot the affected SYSTEM 1E without relying on it for patient-ready devices.

### 2. Confirm Where the Cycle Fails
Ask whether the cycle never starts, aborts immediately, stops during filling, processing, draining, or another phase, or appears frozen. Record displayed messages and determine whether the same condition occurs with repeated attempts.

**Expected outcome:** The failure point is identified. If the cycle subsequently completes normally, investigate the original cause and perform another controlled verification before stopping.

### 3. Inspect the Unit and Processing Area
Check for leakage, water on the floor, unusual noise, odor, overheating, loose accessories, damaged external components, or an improperly seated load. Stop immediately if a safety hazard is present.

**Expected outcome:** No physical hazard exists. If leakage, overheating, or damage is found, remove the equipment from service rather than continuing cycle attempts.

### 4. Verify the Door Is Fully Closed and Ready
Inspect accessible door, seal, latch, and load-area surfaces for obstruction, debris, or improperly positioned items. Confirm nothing in the load interferes with closure or locking.

**Expected outcome:** The door closes normally and the system recognizes the required safe condition. If correcting an obstruction allows the cycle to start and complete, verify operation and troubleshooting can stop.

### 5. Verify the Load and Accessories Are Properly Positioned
Confirm the load, processing tray, connectors, tubing, adapters, and other required accessories are installed and routed correctly according to approved processing practice. Look for pinched, disconnected, or visibly damaged external components.

**Expected outcome:** The load and all required external accessories are correctly installed. If correcting setup restores a complete cycle, stop after final verification.

### 6. Verify Required Consumables
Confirm required chemistry or other cycle consumables are present, correctly installed, within permitted use conditions, and not visibly damaged. Do not bypass consumable recognition or substitute unapproved materials.

**Expected outcome:** Required consumables are available and accepted by the system. If replacement of an exhausted or incorrectly installed consumable restores normal operation, verify a complete cycle and stop.

### 7. Check Facility Utilities
Verify required water, drain, electrical power, and other facility services are available. Look for closed accessible valves, kinked external hoses, blocked visible drains, or evidence of a building utility problem.

**Expected outcome:** External utilities are available and unrestricted. If correcting a utility problem allows the cycle to complete normally, troubleshooting can stop after verification.

### 8. Observe a Controlled Test Cycle
With the unit safe to operate and using an approved test setup, initiate a cycle and observe whether it progresses normally. Note exactly where any delay or abort occurs. Do not repeatedly run failed cycles without determining why.

**Expected outcome:** The cycle proceeds through its expected phases without unexplained interruption. If successful, perform final verification and document the correction.

### 9. Perform Final Functional Verification
Confirm normal cycle initiation, progression, completion indication, drainage, door release, and cycle documentation as applicable. Verify no abnormal alarms or leakage occurred.

**Expected outcome:** A complete cycle finishes normally and the unit is ready for service. Troubleshooting can stop.

### 10. Escalate Repeated Cycle Failure
If load setup, consumables, door condition, and facility utilities are correct but the unit repeatedly aborts or stalls, stop external troubleshooting.

**Expected outcome:** The system is removed from service and referred for qualified evaluation rather than repeatedly processing questionable loads.

## If the Problem Persists
Common external causes involving load setup, accessories, consumables, door closure, power, water, and drain conditions have been ruled out. The unresolved condition may involve internal valves, pumps, sensors, controls, process monitoring, software, or other service-level components.

Remove the SYSTEM 1E from service, label it **Out of Service**, and send it for repair or bench evaluation. Use appropriate manufacturer documentation and approved test equipment. Repairs, calibration, and configuration changes must be performed only by qualified personnel.

Return-to-service testing should demonstrate reliable cycle initiation, progression, completion, utilities, alarms, and required process functions.

Knowing when to stop external troubleshooting is part of proper troubleshooting.

## Clinical Use Tip
A cycle that stops before validated completion should not be treated as successfully processed simply because the device appears clean.

## Work Order Documentation (CCR Method)
<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)
<!-- Helpful details come from front matter. -->

## Final Thought
Protect questionable loads, identify the exact failure phase, rule out setup and infrastructure problems first, verify a complete cycle after correction, and escalate unresolved process failures with clear documentation.

That is successful troubleshooting.
