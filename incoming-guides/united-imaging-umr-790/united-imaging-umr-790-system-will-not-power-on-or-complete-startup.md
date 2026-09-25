---
schemaVersion: 1
title: "United Imaging uMR 790 MRI System - System Will Not Power On or Complete Startup"
issueTitle: "System Will Not Power On or Complete Startup"
description: "Troubleshoots startup failure, incomplete boot, loss of console power, external power issues, shutdown states, and connected equipment preventing normal system readiness."
assetType: "MRI System"
manufacturer: "United Imaging"
model: "uMR 790"
slug: "united-imaging-umr-790-system-will-not-power-on-or-complete-startup"
dateAdded: "2026-09-25"
taxonomyMode: "reuse"
ccr:
  complaint: "MRI staff reported that the United Imaging uMR 790 would not complete startup after a facility power interruption."
  cause: "Clinical Engineering found an approved external system power condition had not returned to its normal operating state following the interruption."
  resolution: "The authorized external power condition was restored, the MRI system completed startup normally, and system readiness was verified before return to service."
helpfulDetails:
  - "Exact point where startup stops"
  - "Any displayed fault message"
  - "Recent outage or electrical work"
  - "Console and display power status"
  - "Emergency-stop or shutdown status"
  - "External power indicators"
  - "Cable and peripheral condition"
  - "Abnormal noise, odor, heat, or moisture"
  - "Results after approved restart"
  - "Final system-ready status"
---
## What This Guide Helps With

Troubleshoots startup failure, incomplete boot, loss of console power, external power issues, shutdown states, and connected equipment preventing normal system readiness.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Confirm System Status
Do not troubleshoot the MRI system while a patient depends on it for an active examination. Safely remove the patient from the scanner area as appropriate and maintain continuity of care using an alternate imaging plan if needed.

Confirm whether the reported condition is:
- No visible system power
- Console or workstation not starting
- Startup stopping at a particular stage
- System powering on but never reaching a ready state
- Repeated shutdown or restart

Note any displayed message without attempting unsupported resets or service-level configuration changes.

**Expected outcome:** The patient is safe and the exact startup symptom is identified. If the system subsequently reaches its normal ready state and remains stable, troubleshooting can stop after functional verification.

### 2. Verify Facility Power and External Power Conditions
Check accessible power indicators, approved disconnect positions, equipment-room power conditions, and any external power distribution associated with the MRI system.

Determine whether:
- A recent outage, generator transfer, electrical work, or emergency shutdown occurred
- Other connected MRI equipment has also lost power
- An approved disconnect appears to have been operated
- Any facility circuit or infrastructure problem has been reported

Do not operate electrical disconnects or infrastructure controls outside Clinical Engineering authorization.

**Expected outcome:** Required external power sources are available and no obvious facility-power interruption is present. If restoring an authorized external power condition returns the system to normal operation, verify startup and stop troubleshooting.

### 3. Check Emergency and Shutdown Conditions
Inspect accessible emergency-stop or shutdown controls for evidence they were activated. Verify the system has not been intentionally placed in a shutdown condition by clinical, facilities, or service personnel.

Do not reset emergency controls until it is confirmed that the original reason for activation has been addressed and reset is permitted.

**Expected outcome:** No unresolved emergency or shutdown condition prevents startup. If an authorized reset restores normal startup, complete functional verification and stop.

### 4. Inspect Accessible Power and Communication Connections
Inspect external workstation, display, console, peripheral, and approved equipment-room connections for:
- Loose plugs
- Partially seated cables
- Damaged connectors
- Accidental disconnection
- Visible cable damage

Do not enter restricted equipment cabinets or disturb high-voltage, magnet, RF, gradient, or internal power assemblies.

**Expected outcome:** Accessible connections are secure and undamaged. If reseating an approved external connection restores normal startup, verify stability and stop.

### 5. Check Console and Workstation Startup
Determine whether the operator workstation and associated displays are receiving power and completing their normal boot sequence.

If an approved normal restart is permitted by site procedure, perform only the standard restart process. Do not repeatedly power-cycle a system that freezes, shuts down unexpectedly, or displays a persistent fault.

**Expected outcome:** The workstation reaches the normal application environment and communicates with the MRI system. If normal readiness returns, verify operation and stop.

### 6. Check Peripheral Devices That May Affect Startup
Inspect externally connected devices such as monitors, input devices, network-connected peripherals, or approved accessories for obvious faults or abnormal states.

Disconnect or substitute peripherals only when they are designed for normal external connection and doing so is permitted.

**Expected outcome:** No external peripheral is preventing normal startup. If removing or replacing a faulty external peripheral restores startup, verify the complete system and stop.

### 7. Verify Environmental Conditions
Check the scanner, console, and equipment areas for:
- Excessive heat
- Blocked ventilation
- Water or condensation
- Unusual odor
- Abnormal noise
- Evidence of recent facility work

Do not continue powering equipment showing signs of overheating, liquid intrusion, smoke, or electrical damage.

**Expected outcome:** The environment is suitable for operation with no obvious safety hazard. If an environmental problem is found, remove the system from service until corrected.

### 8. Perform Final Functional Verification
Once normal startup is restored, allow the system to complete its standard initialization and confirm:
- Console operation
- System-ready indication
- Table and positioning availability
- Acquisition readiness
- Normal communication with required peripherals
- No persistent fault or abnormal shutdown

Perform any required return-to-service checks using approved procedures.

**Expected outcome:** The United Imaging uMR 790 reaches normal operating readiness without recurring faults. Troubleshooting can stop.

### 9. Escalate an Unresolved Startup Failure
If power is available, external connections are correct, emergency conditions are cleared, and the system still fails to start or initialize, stop external troubleshooting.

**Expected outcome:** The system remains out of clinical service and is escalated for qualified MRI service evaluation.

## If the Problem Persists

Common external causes have been ruled out. Remaining causes may involve internal power distribution, startup control, system communication, computing hardware, cooling dependencies, configuration, or other service-level MRI subsystems.

The device should be:
- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench/service evaluation as appropriate
- Evaluated using United Imaging documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not access internal power, RF, gradient, magnet, or other restricted assemblies without proper authorization and training.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting. After service, complete appropriate startup, operational, safety, and return-to-service verification before clinical use.

## Clinical Use Tip

After any abnormal MRI shutdown or startup failure, confirm the entire imaging system reaches a stable ready state before bringing another patient into the examination workflow.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient first, verify external power and shutdown conditions before assuming internal failure, and escalate unresolved startup problems appropriately. Clear CCR documentation should capture the reported symptom, verified cause, corrective action, and final system status.

That is successful troubleshooting.
