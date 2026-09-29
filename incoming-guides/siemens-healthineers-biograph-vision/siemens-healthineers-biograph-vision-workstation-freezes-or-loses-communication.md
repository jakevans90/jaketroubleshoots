---
schemaVersion: 1
title: "Siemens Healthineers Biograph Vision PET / CT System - Workstation Freezes or Loses Communication"
issueTitle: "Workstation Freezes or Loses Communication"
description: "Use this guide when the operator workstation becomes unresponsive or loses communication with scanner components because of external connections, network conditions, or software-state issues."
assetType: "PET / CT System"
manufacturer: "Siemens Healthineers"
model: "Biograph Vision"
slug: "siemens-healthineers-biograph-vision-workstation-freezes-or-loses-communication"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Biograph Vision workstation lost communication with the scanner during setup."
  cause: "Clinical Engineering found an accessible Ethernet connection at the workstation partially seated."
  resolution: "Clinical Engineering secured the connection, restarted the workstation normally, verified stable scanner communication and workflow operation, and returned the system to service."
helpfulDetails:
  - "Freeze versus communication-loss symptom"
  - "Exact displayed message"
  - "Keyboard and mouse response"
  - "Monitor status"
  - "External network connection condition"
  - "Other systems affected"
  - "Recent network work"
  - "Restart result"
  - "Recurrence after restart"
  - "Final communication status"
---
## What This Guide Helps With

Use this guide when the operator workstation becomes unresponsive or loses communication with scanner components because of external connections, network conditions, or software-state issues.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Dependence on an Unresponsive Workstation

If the workstation freezes during patient positioning or acquisition, do not assume the scanner is safely controllable.

Maintain patient safety, stop further examination activity, and use appropriate approved system controls to place the patient in a safe condition.

**Expected outcome:** The patient is safe and no active procedure relies on an unresponsive workstation.

### 2. Define the Failure

Determine whether:

- The mouse or keyboard is unresponsive.
- The display is frozen but the system remains active.
- Communication with the scanner is lost.
- Only one application is unresponsive.
- The problem occurs during a particular workflow.
- The workstation restarts unexpectedly.

Record any message displayed.

**Expected outcome:** The failure is distinguished as local workstation, application, or scanner-communication related.

### 3. Check Display and Input Devices

Inspect the workstation's accessible external components:

- Monitor power.
- Video connection.
- Keyboard.
- Mouse.
- Approved USB connections.
- External power connections.

A blank display can be mistaken for a frozen computer.

**Expected outcome:** Display and input hardware are powered, connected, and functional.

If an external peripheral connection correction restores normal control, verify operation and stop.

### 4. Inspect Accessible Network and Communication Connections

Check accessible Ethernet and system communication connections for:

- Loose connectors.
- Disconnected cables.
- Visible cable damage.
- Recently disturbed patching.
- Abnormal port indicators when normally visible.

Do not move the scanner to another network port or VLAN without authorization.

**Expected outcome:** Accessible communication connections are intact and correctly connected.

If reseating an approved external connection restores stable communication, verify operation and stop.

### 5. Determine Whether the Problem Is Local or Infrastructure-Wide

Check whether other connected imaging or clinical systems are experiencing similar communication issues.

If multiple systems are affected, coordinate with the appropriate network or infrastructure team rather than altering the scanner configuration.

**Expected outcome:** A local scanner problem is distinguished from a broader infrastructure problem.

### 6. Allow an Application to Recover if Appropriate

If the workstation is temporarily busy rather than completely nonresponsive, avoid repeated clicking or forced power removal.

Observe whether normal operation returns within the expected local workflow.

**Expected outcome:** The application either recovers normally or remains clearly unresponsive.

If it recovers and communication remains stable during verification, troubleshooting may stop.

### 7. Perform a Controlled Restart if Required

If the system is not performing an active patient acquisition and approved normal controls permit it, perform one controlled workstation or system restart according to facility and manufacturer-approved practice.

Do not use hard power removal unless specifically required by an approved procedure.

**Expected outcome:** The workstation restarts normally and reconnects to required scanner subsystems.

If normal operation and communication are restored and remain stable, proceed to verification.

### 8. Verify Scanner Communication

Confirm after recovery that the workstation correctly communicates with required scanner components and can:

- Display system status.
- Access normal operator functions.
- Recognize scanner readiness.
- Complete an approved non-patient test workflow if required.

**Expected outcome:** Communication remains stable without repeat disconnects.

### 9. Perform Final Functional Verification

Verify:

- Stable workstation response.
- Keyboard and mouse operation.
- Scanner status communication.
- Study workflow access.
- Acquisition control availability.
- No recurring freeze or communication loss.

**Expected outcome:** The workstation and scanner communicate reliably through required functions.

If all checks pass, troubleshooting is complete.

### 10. Escalate Recurring Freezes or Communication Loss

If the workstation repeatedly freezes, crashes, or loses scanner communication after connections and infrastructure conditions are verified, stop external troubleshooting.

**Expected outcome:** The affected system is removed from clinical use and escalated for qualified service.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve workstation hardware, operating-system or application faults, internal scanner networking, system controllers, protected network configuration, data corruption, or other service-level conditions.

The device should be:

- Removed from service when reliable control cannot be assured.
- Labeled **Out of Service**.
- Sent for repair or qualified system evaluation.
- Evaluated using appropriate Siemens Healthineers documentation and approved diagnostic tools.
- Repaired or configured only by qualified personnel.

Do not modify protected network settings, reinstall system software, or enter unauthorized service utilities.

Required scanner and workstation functionality must be verified before return to clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A workstation that intermittently reconnects after freezing should not be considered reliable until communication remains stable through an appropriate functional test.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient first, separate a simple peripheral or network connection issue from a true system fault, verify sustained communication after correction, and escalate recurrent workstation instability.

That is successful troubleshooting.
