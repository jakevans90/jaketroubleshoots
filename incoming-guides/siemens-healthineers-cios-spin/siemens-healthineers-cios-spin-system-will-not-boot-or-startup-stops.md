---
schemaVersion: 1
title: "Siemens Healthineers Cios Spin C-Arm - System Will Not Boot or Startup Stops"
issueTitle: "System Will Not Boot or Startup Stops"
description: "Addresses no-power conditions, incomplete startup, frozen boot sequences, power-source problems, disconnected components, and other externally verifiable startup causes."
assetType: "C-Arm"
manufacturer: "Siemens Healthineers"
model: "Cios Spin"
slug: "siemens-healthineers-cios-spin-system-will-not-boot-or-startup-stops"
dateAdded: "2026-08-26"
taxonomyMode: "reuse"
ccr:
  complaint: "Surgical staff reported the Cios Spin stopped during startup and would not reach the normal operating screen."
  cause: "Clinical Engineering found the system connected to a faulty facility receptacle that did not provide reliable AC power."
  resolution: "The C-arm was connected to a verified receptacle, started normally on repeated checks, and passed basic operational and imaging verification."
helpfulDetails:
  - "Exact point where startup stopped."
  - "Any displayed message."
  - "Whether the system had been recently moved."
  - "AC receptacle tested."
  - "Power cord condition."
  - "Emergency-control status."
  - "External connections inspected."
  - "Accessories disconnected during testing."
  - "Results of controlled restart."
  - "Whether the failure repeated."
  - "Final functional test results."
  - "Final device status."
---

## What This Guide Helps With
Addresses no-power conditions, incomplete startup, frozen boot sequences, power-source problems, disconnected components, and other externally verifiable startup causes.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Continuity of Care
Do not troubleshoot a Cios Spin that is required for an active procedure if its operation is unreliable. If the system cannot boot or remains stuck during startup, notify the clinical team and move the procedure to another verified imaging system when necessary.

Check for smoke, unusual odor, abnormal heat, fluid intrusion, visible damage, or evidence of electrical damage before touching or energizing the system. If any are present, disconnect the system from use and stop troubleshooting.

**Expected outcome:** The patient is not dependent on the affected system, and the C-arm is safe to evaluate.

### 2. Confirm the Exact Startup Complaint
Ask clinical staff what occurred immediately before the failure and determine whether the system:
- Shows no signs of power.
- Begins startup and shuts back down.
- Stops at a startup screen.
- Displays a message or warning.
- Boots intermittently.
- Experienced the problem after transport, relocation, power interruption, or accessory connection.

Record any displayed message exactly rather than interpreting it from memory.

**Expected outcome:** The failure is reproducible or clearly characterized enough to guide further checks.

### 3. Verify Facility AC Power
Confirm that the system power cord is fully inserted and undamaged. Inspect the plug, cord, strain relief, and accessible power connections for damage.

Verify the wall receptacle using an appropriate approved method or known-good equipment. Avoid extension cords, unauthorized adapters, overloaded power strips, or questionable temporary power sources.

If the Cios Spin was moved between rooms, compare operation at a known-good approved receptacle when appropriate.

**Expected outcome:** Stable facility AC power is available to the system. If restoring proper AC power corrects startup, troubleshooting can stop after functional verification.

### 4. Inspect System Power Connections
Inspect externally accessible connections between the C-arm, workstation, monitor cart, or other associated system components required for normal startup.

Look for:
- Partially seated connectors.
- Loose locking hardware.
- Pinched or stretched cables.
- Connectors disturbed during transport.
- Visible contamination or bent connector shells.

Reseat only user-accessible or service-approved external connections with power removed when appropriate.

**Expected outcome:** All required external system connections are intact and securely seated. If the unit now starts normally, continue to final verification.

### 5. Check Power Controls and Emergency-Off Conditions
Verify that the normal power control is functioning mechanically and is not stuck or damaged.

Inspect accessible emergency-stop or emergency-off controls and confirm none are unintentionally engaged. Do not defeat or bypass a safety interlock or emergency circuit.

**Expected outcome:** No externally accessible power or emergency control is preventing startup.

### 6. Remove Nonessential External Accessories
Disconnect nonessential external USB devices, removable media, peripherals, or accessories that are not required for basic startup, provided doing so is permitted and does not alter required configuration.

Restart the system using the normal approved startup sequence.

Do not repeatedly hard-cycle the system if it continues stopping at the same stage.

**Expected outcome:** The system starts normally without an external peripheral interfering. If so, reconnect accessories individually to identify the external cause.

### 7. Observe the Startup Sequence
Power the system normally and observe:
- Which components energize.
- Whether displays illuminate.
- Whether the workstation progresses through startup.
- Whether the system stops at the same point each time.
- Any warning indicators or messages.
- Whether a component repeatedly restarts.

Do not enter restricted service modes or change configuration values solely to force startup.

**Expected outcome:** Startup completes normally, or a consistent failure point is identified for escalation.

### 8. Perform a Controlled Restart When Appropriate
If the system has frozen but does not show evidence of electrical or mechanical damage, perform one controlled shutdown and restart using normal approved controls.

Allow the system to complete its normal shutdown and startup processes. Avoid repeated forced power interruptions.

**Expected outcome:** The system completes startup without freezing or restarting. If normal operation returns and remains stable, proceed to final verification.

### 9. Perform Final Functional Verification
Once startup completes, verify normal basic operation before returning the system to clinical use.

Confirm:
- Displays and controls initialize normally.
- No unresolved startup warnings remain.
- Required system components communicate.
- C-arm movement and basic controls respond normally.
- Imaging availability is normal using approved test methods.
- No unusual noise, odor, heat, or intermittent shutdown occurs.

**Expected outcome:** The Cios Spin completes startup repeatedly and passes appropriate functional checks. Troubleshooting can stop and the device may be returned to service according to facility procedure.

### 10. Escalate if Startup Remains Abnormal
Remove the system from service if it remains unable to boot, repeatedly freezes, shuts down unexpectedly, loses communication with required components, or cannot complete required functional verification.

Do not proceed into power supplies, internal computer hardware, control boards, high-voltage circuits, or other internal assemblies without appropriate manufacturer documentation, authorization, and training.

**Expected outcome:** An unresolved or unreliable system is prevented from returning to clinical use and is routed for qualified service.

## If the Problem Persists
If facility power, external connections, controls, peripherals, and controlled restart have been ruled out, the remaining cause may involve internal power distribution, embedded computing hardware, software initialization, system communications, configuration, or another service-level subsystem.

The Cios Spin should be:
- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench/service evaluation.
- Evaluated using appropriate Siemens Healthineers documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

After corrective work, complete applicable electrical safety, startup, communication, mechanical, imaging, and functional verification before clinical return.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip
If startup reliability is uncertain, move the procedure to another verified imaging system rather than attempting repeated restarts during patient care.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**


## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Protect the patient first, verify power and external causes before assuming an internal failure, confirm normal operation after correction, escalate unreliable equipment appropriately, and document the complaint, verified cause, and resolution clearly.

That is successful troubleshooting.
