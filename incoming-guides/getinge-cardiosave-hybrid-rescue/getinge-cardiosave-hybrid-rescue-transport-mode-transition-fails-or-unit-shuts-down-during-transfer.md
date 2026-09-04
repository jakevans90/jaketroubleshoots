---
schemaVersion: 1
title: "Getinge Cardiosave Hybrid / Rescue Intra-Aortic Balloon Pump - Transport Mode Transition Fails or Unit Shuts Down During Transfer"
issueTitle: "Transport Mode Transition Fails or Unit Shuts Down During Transfer"
description: "Troubleshoots transport transition or shutdown problems involving AC power, battery condition, connections, accessories, docking, or movement-related interruptions."
assetType: "Intra-Aortic Balloon Pump"
manufacturer: "Getinge"
model: "Cardiosave Hybrid / Rescue"
slug: "getinge-cardiosave-hybrid-rescue-transport-mode-transition-fails-or-unit-shuts-down-during-transfer"
dateAdded: "2026-09-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Cardiosave shut down when disconnected from AC power for transport."
  cause: "Clinical Engineering found an external battery connection was not fully engaged."
  resolution: "Clinical Engineering reseated the battery connection, verified repeated AC-to-battery transitions and stable operation during controlled testing, and returned the unit to service after required checks."
helpfulDetails:
  - "Point at which shutdown occurred"
  - "AC power status"
  - "Battery indication"
  - "Charging behavior"
  - "Power cord condition"
  - "Battery and docking connection condition"
  - "Whether movement reproduced the failure"
  - "AC-to-battery test results"
  - "Any reboot or loss of pumping"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots transport transition or shutdown problems involving AC power, battery condition, connections, accessories, docking, or movement-related interruptions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Before Moving the IABP

Unexpected shutdown during transport can interrupt life-sustaining counterpulsation. If transport operation is unreliable, do not continue moving a dependent patient until a verified support plan is established.

Use another verified IABP or clinically appropriate alternative when necessary.

**Expected outcome:** The patient is not transported with unreliable circulatory support.

### 2. Confirm How the Failure Occurs

Determine whether shutdown occurs when AC power is disconnected, during docking or undocking, when entering the transport configuration, during movement, or after a period on battery.

Record battery indicators and displayed messages.

**Expected outcome:** The transition point associated with the failure is identified.

### 3. Verify AC Power and Charging Before Transport

Connect the Cardiosave to a known-good hospital-grade AC source and confirm normal power indication and charging behavior.

Inspect the power cord and plug for damage.

**Expected outcome:** AC operation is stable and the battery indicates normal charging. If a loose external power connection caused the issue, correct it, verify operation, and stop troubleshooting.

### 4. Check Battery Status

Review the available battery status indications. A battery showing poor charge acceptance, unexpectedly low capacity, or abnormal status should not be trusted for patient transport.

Do not assume displayed charge percentage alone proves adequate battery performance.

**Expected outcome:** Battery status is appropriate for controlled testing. Abnormal battery behavior requires removal from transport use.

### 5. Inspect External Battery and Power Connections

Check accessible battery seating, external power interfaces, connectors, docking points, and latches applicable to the Hybrid / Rescue configuration for incomplete engagement or physical damage.

**Expected outcome:** All accessible power-related interfaces are secure and undamaged. If reseating an external connection restores reliable transitions, verify repeatedly and stop troubleshooting.

### 6. Check for Movement-Related Intermittency

With the device off-patient, perform controlled movement while monitoring power status. Inspect whether cord strain, docking movement, vibration, or repositioning causes power interruption.

**Expected outcome:** Power remains stable during normal controlled movement. A movement-sensitive failure requires corrective action before clinical transport.

### 7. Test AC-to-Battery Transition Off-Patient

Using approved procedures, operate the Cardiosave under a controlled test load and transition from AC to battery operation.

Do not perform this test for the first time while the device is supporting a patient.

**Expected outcome:** The unit continues operating without rebooting or interrupting required functions. If transition is stable after correcting an external connection, troubleshooting can stop.

### 8. Verify Battery Operation Under Controlled Conditions

Assess whether battery operation remains stable for the approved functional test period using manufacturer procedures. Do not invent or impose an unsupported runtime threshold.

**Expected outcome:** The unit remains powered and functional throughout the required test. Unexpected shutdown indicates further service is required.

### 9. Perform Final Transport-Readiness Verification

Verify power transition, battery operation, controls, display, alarms, pump function, and all applicable transport-related checks before return to service.

**Expected outcome:** Multiple transitions are stable and no shutdown occurs. Troubleshooting can stop.

### 10. Escalate Any Unexplained Shutdown

If the Cardiosave shuts down, resets, or loses pumping during controlled testing after external power and battery connections are verified, remove it from service.

**Expected outcome:** A potentially serious internal power problem is escalated appropriately.

## If the Problem Persists

External AC supply, battery seating, docking interfaces, connectors, and movement-related causes have been ruled out. Remaining possibilities include battery deterioration, internal power-management problems, charging-system faults, power-distribution issues, or other service-level conditions.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate Getinge documentation and approved test equipment
- Repaired or battery components replaced only by qualified personnel

Complete required battery, power-transition, pump-operation, alarm, and electrical safety testing before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never begin a patient transfer on an IABP with unresolved battery or power-transition concerns; verify transport operation before leaving the controlled care area.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Point at which shutdown occurred
- AC power status
- Battery indication
- Charging behavior
- Power cord condition
- Battery and docking connection condition
- Whether movement reproduced the failure
- AC-to-battery test results
- Any reboot or loss of pumping
- Final device status

## Final Thought

Transport failures deserve a conservative response because loss of IABP power can immediately affect patient support. Verify AC power, batteries, external interfaces, and controlled transitions before suspecting internal failure, and remove any intermittently shutting-down unit from service.

That is successful troubleshooting.
