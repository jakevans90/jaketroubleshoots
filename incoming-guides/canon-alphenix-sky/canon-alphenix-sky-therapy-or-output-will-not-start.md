---
schemaVersion: 1
title: "Canon Alphenix Sky+ Angiography System - Therapy or Output Will Not Start"
issueTitle: "Therapy or Output Will Not Start"
description: "Troubleshoot commanded system output that will not initiate because of readiness, controls, accessories, interlocks, configuration, or system communication problems."
assetType: "Angiography System"
manufacturer: "Canon"
model: "Alphenix Sky+"
slug: "canon-alphenix-sky-therapy-or-output-will-not-start"
dateAdded: "2026-10-14"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Canon Alphenix Sky+ would not initiate the requested imaging output when commanded."
  cause: "Clinical Engineering found the external foot control connection partially seated and confirmed normal control recognition after reseating it."
  resolution: "Clinical Engineering secured the connection, verified reliable activation with a non-patient functional check, and returned the system to service."
helpfulDetails:
  - "Function or output that would not start"
  - "Exact warning or inhibit message"
  - "System readiness status"
  - "External control condition"
  - "Relevant accessory recognition"
  - "Interlock or positioning status"
  - "Known-good substitution results"
  - "Functional test results"
  - "Final system status"
---
## What This Guide Helps With
Troubleshoot commanded system output that will not initiate because of readiness, controls, accessories, interlocks, configuration, or system communication problems.

## Step-by-Step Troubleshooting
### 1. Protect the Patient and Stop the Procedure if Needed
If required imaging or system output cannot be initiated reliably, do not continue an invasive procedure unless the clinical team has established a safe alternative plan.

**Expected outcome:** Patient care is not dependent on an angiography system that cannot reliably produce the required output.

### 2. Confirm the Exact Output Failure
Determine which commanded function will not start, whether the request is ignored or inhibited, and whether the system displays a readiness message, warning, or other status indication.

**Expected outcome:** The failure is defined as a specific output/readiness problem rather than a general system complaint.

### 3. Verify Overall System Readiness
Confirm that the system has completed startup and is not displaying an unresolved fault or unavailable subsystem. Verify that required system components appear online.

**Expected outcome:** The system reaches the normal state required before initiating output.

### 4. Inspect External Controls and Connections
Inspect accessible hand controls, foot controls, switches, cables, connectors, and operator interfaces associated with the requested function. Check for obvious damage or loose connections.

**Expected outcome:** External command devices are connected, undamaged, and responsive.

### 5. Check Safety Interlocks and Positioning
Verify that applicable table, gantry, detector, room safety, collision-prevention, or other normal safety conditions are satisfied. Never bypass a safety interlock to obtain output.

**Expected outcome:** No legitimate external safety condition is intentionally inhibiting operation.

### 6. Verify Accessories and Required Modules
Confirm that required approved accessories or modules are attached and recognized where the requested function depends on them.

**Expected outcome:** All required external components are present and recognized.

### 7. Verify Accessible Operating Selections
Check normal user-accessible mode and function selections to confirm that the requested operation is enabled and appropriate for the current setup. Do not alter restricted service configuration.

**Expected outcome:** The requested function is correctly selected and available.

### 8. Test With Known-Good External Controls When Appropriate
If an approved interchangeable external control or accessory is available, substitute it to determine whether the failure follows the accessory.

**Expected outcome:** A known-good substitute restores normal activation if the external control was defective.

### 9. Perform Functional Verification
After correcting an external cause, verify the requested output using an appropriate non-patient functional test and any required safety checks before clinical use.

**Expected outcome:** Output starts reliably when commanded and terminates normally. Troubleshooting can stop.

### 10. Escalate an Unresolved Output Failure
If output remains inhibited despite correct readiness, connections, accessories, positioning, and controls, remove the system from service.

**Expected outcome:** Unreliable output is not used clinically and the system is referred for qualified service.

## If the Problem Persists
Common external controls, readiness conditions, accessories, positioning, and safety interlocks have been ruled out. Remaining possibilities include internal control circuitry, generator or imaging-output systems, system communication, configuration, or another protected service-level condition.

Remove the system from service, label it **Out of Service**, and arrange evaluation using Canon service documentation and approved test equipment. Do not bypass safety systems or perform unauthorized internal adjustments.

Return to service only after the commanded function, applicable safety systems, and required system performance have been verified. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
Never bypass an interlock or repeat output attempts around an unexplained inhibit during an invasive procedure.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought
Verify system readiness, external controls, accessories, and legitimate safety interlocks before assuming an internal output failure, and never bypass safety mechanisms to force operation.

That is successful troubleshooting.
