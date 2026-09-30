---
schemaVersion: 1
title: "Varian TrueBeam Radiation Therapy System - Workstation Freezes or Loses Communication"
issueTitle: "Workstation Freezes or Loses Communication"
description: "A TrueBeam workstation becomes unresponsive, freezes, disconnects, or loses communication with another required system component."
assetType: "Radiation Therapy System"
manufacturer: "Varian"
model: "TrueBeam"
slug: "varian-truebeam-workstation-freezes-or-loses-communication"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that the TrueBeam workstation became unresponsive and stopped communicating with the treatment system."
  cause: "Clinical Engineering found an accessible network cable connection partially unseated at the workstation."
  resolution: "Clinical Engineering secured the connection, restarted the workstation using the approved process, and verified stable communication and normal workflow operation."
helpfulDetails:
  - "Workstation affected"
  - "Application or function affected"
  - "Freeze versus communication-loss symptoms"
  - "Display and peripheral response"
  - "External network cable condition"
  - "Other systems affected"
  - "Infrastructure outage status"
  - "Restart result"
  - "Communication verification"
  - "Recurrence after restart"
  - "Final system status"
---
## What This Guide Helps With

A TrueBeam workstation becomes unresponsive, freezes, disconnects, or loses communication with another required system component.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop the Workflow
Do not continue a treatment or imaging workflow when a required workstation is frozen or communications are unreliable. Place the patient in a safe condition and coordinate with Radiation Oncology.

**Expected outcome:** Patient treatment does not depend on an unstable workstation or communication path.

### 2. Identify the Affected Workstation and Function
Determine which workstation or console is affected and whether the issue is a complete freeze, delayed response, application failure, display problem, or communication loss.

**Expected outcome:** The affected system and failure mode are clearly identified.

### 3. Check Basic Power and Display Operation
Verify workstation power, monitor power, accessible power connections, and display input status. Check whether keyboard or mouse response indicates the computer itself remains operational.

**Expected outcome:** A simple display or peripheral issue is distinguished from a true workstation failure.

### 4. Inspect Accessible Network and Data Connections
Check externally accessible network and communication cables for loose connectors, visible damage, or recent relocation.

**Expected outcome:** Required external data connections are secure.

### 5. Determine Whether the Problem Is Local or System-Wide
Check whether other TrueBeam-related workstations or hospital systems can communicate normally. Determine whether a broader network or infrastructure outage has been reported.

**Expected outcome:** The problem is narrowed to the local workstation, the TrueBeam environment, or shared infrastructure.

### 6. Check Supporting Applications
If the workstation remains responsive, verify whether the required application is running normally and whether other user-accessible system functions respond.

Do not terminate restricted processes or alter service configuration.

**Expected outcome:** The problem is isolated to the application or to the entire workstation.

### 7. Perform an Approved Restart
If the patient is safe and policy permits, perform the normal approved restart of the affected workstation or application. Avoid repeated forced shutdowns.

**Expected outcome:** The workstation restarts and communication is restored. If it remains stable, proceed to verification.

### 8. Verify Complete Communication
Confirm communication through the full required path rather than relying only on a normal-looking screen. Verify that expected system status, data exchange, and workflow functions are restored.

**Expected outcome:** The workstation communicates normally with required systems. Troubleshooting can stop after successful verification.

### 9. Escalate Recurrent Freezes or Communication Loss
If the workstation freezes again, communication repeatedly drops, or required data cannot be trusted, remove the affected workflow from service.

**Expected outcome:** Unreliable workstation operation is not used for patient treatment.

## If the Problem Persists

External power, peripherals, accessible network connections, application status, and obvious infrastructure problems have been ruled out. Remaining causes may involve workstation hardware, operating system or application software, network infrastructure, internal system communications, or configuration.

The device should be:

- Removed from service when the affected workstation is required for safe treatment
- Labeled Out of Service
- Sent for repair or appropriate service/IT evaluation
- Evaluated using appropriate manufacturer documentation and approved diagnostic tools
- Repaired or configured only by qualified personnel

Return to service requires stable workstation operation and verification of all required communications and clinical workflow functions.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A workstation that reconnects briefly but repeatedly loses communication should be considered unreliable until the complete treatment workflow remains stable.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Workstation problems can interrupt critical radiation-treatment workflows even when other system hardware appears normal. Verify power, peripherals, connections, and infrastructure first, then escalate recurring instability rather than relying on a temporary recovery.

That is successful troubleshooting.
