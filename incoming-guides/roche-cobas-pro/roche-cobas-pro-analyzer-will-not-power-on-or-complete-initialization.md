---
schemaVersion: 1
title: "Roche cobas pro Clinical Chemistry Analyzer - Analyzer Will Not Power On or Complete Initialization"
issueTitle: "Analyzer Will Not Power On or Complete Initialization"
description: "Troubleshoots no-power, incomplete startup, initialization hangs, and startup failures caused by external power, accessories, consumables, configuration, or environmental conditions."
assetType: "Clinical Chemistry Analyzer"
manufacturer: "Roche"
model: "cobas pro"
slug: "roche-cobas-pro-analyzer-will-not-power-on-or-complete-initialization"
dateAdded: "2026-10-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported the cobas pro powered on but repeatedly stopped before completing initialization."
  cause: "Clinical Engineering found an externally connected analyzer communication cable partially disconnected following nearby equipment movement."
  resolution: "Reseated and secured the connection, restarted the analyzer, verified successful initialization, and confirmed the system returned to ready status for laboratory QC."
helpfulDetails:
  - "Exact startup message or alarm"
  - "Stage where initialization stopped"
  - "Whether all modules powered on"
  - "Recent outage or power event"
  - "Facility power verification"
  - "Condition of external power and communication cables"
  - "Recent cleaning, maintenance, or relocation"
  - "Doors, covers, and removable components checked"
  - "Unusual heat, odor, leakage, or noise"
  - "Results before and after restart"
  - "Final analyzer status"
  - "QC or readiness verification performed"
---
## What This Guide Helps With

Troubleshoots no-power, incomplete startup, initialization hangs, and startup failures caused by external power, accessories, consumables, configuration, or environmental conditions.

## Step-by-Step Troubleshooting

### 1. Protect Patient Testing and Confirm the Reported Condition

Do not rely on an analyzer that cannot complete startup or initialization for patient testing. Redirect specimens to another verified analyzer or follow the laboratory downtime procedure.

Confirm whether the analyzer:
- Has no visible power
- Powers on but stops during initialization
- Displays a startup message or alarm
- Reboots unexpectedly
- Initializes some modules but not others

Record the exact displayed message and the point at which initialization stops.

**Expected outcome:** The exact failure mode is established and patient testing is safely redirected. If the analyzer subsequently initializes normally and passes required readiness checks, troubleshooting can stop after final verification.

### 2. Check External Power

Verify that the analyzer's normal facility power source is available and that no obvious upstream power interruption has occurred.

Inspect accessible:
- Power cords
- Plugs
- Approved power distribution equipment
- Facility receptacles
- External disconnects or breakers intended for normal operator or facility access

Look for loose connections, physical damage, heat, discoloration, or evidence of a recent outage.

Do not repeatedly reset a breaker that trips again.

**Expected outcome:** Stable facility power is present and external power connections are secure. If restoring a verified external power source allows normal initialization, the issue is resolved and troubleshooting can stop after verification.

### 3. Inspect the Analyzer for Unsafe Conditions

Before additional startup attempts, inspect for:
- Liquid leakage
- Chemical spills
- Unusual odor
- Smoke or overheating
- Damaged covers
- Loose external components
- Obstructed ventilation
- Evidence of fluid intrusion

If any unsafe condition is present, disconnect or isolate the equipment as appropriate and remove it from service.

**Expected outcome:** No unsafe physical or environmental condition is present before continued troubleshooting.

### 4. Verify Required External Modules and Connections

Confirm that externally connected modules, control computers, peripherals, and communications connections required for normal operation are powered and securely connected.

Inspect accessible cables for:
- Loose connectors
- Pinched or damaged sections
- Partially seated plugs
- Accidental disconnection during cleaning, relocation, or nearby work

Do not open internal electrical compartments.

**Expected outcome:** Required external modules and connections are present, powered, and secure. If reseating an accessible connection restores normal initialization, troubleshooting can stop after verification.

### 5. Check Covers, Doors, Consumables, and Accessible Positions

Verify that externally accessible covers and doors are fully closed and that required racks, reservoirs, consumables, or removable components are properly seated where applicable.

Look for anything left displaced after:
- Cleaning
- Consumable replacement
- Maintenance
- Spill response
- Analyzer relocation

Do not defeat interlocks.

**Expected outcome:** All externally accessible components required for initialization are correctly positioned.

### 6. Evaluate the Startup Sequence

Perform only the normal approved startup or restart process available to laboratory or Clinical Engineering personnel.

Observe:
- Whether the controller starts
- Whether all modules are recognized
- Whether initialization consistently stops at the same stage
- Any messages presented before the failure

Avoid repeated power cycling when the same fault immediately returns.

**Expected outcome:** The analyzer completes its normal startup sequence and reaches a ready state. If it does, proceed to final verification and stop troubleshooting.

### 7. Check Environmental Conditions

Verify that the analyzer area has:
- Normal room temperature
- Unobstructed airflow
- No obvious excessive heat
- No active water leak
- No recent electrical or construction activity affecting the installation
- Adequate clearance around external ventilation areas

**Expected outcome:** No environmental or infrastructure condition is preventing normal operation.

### 8. Perform Final Functional Verification

After the analyzer initializes successfully:
- Confirm all expected modules report ready
- Verify no unresolved startup alarms remain
- Confirm required consumables and reagents are recognized
- Verify normal specimen handling interfaces are available
- Perform laboratory-required control or readiness checks before patient use

**Expected outcome:** The analyzer is fully initialized and passes required operational checks. Troubleshooting is complete.

### 9. Escalate if Initialization Still Fails

If verified power, connections, external components, and environmental conditions are normal but initialization still fails, stop external troubleshooting.

Do not proceed into internal power supplies, control electronics, motors, boards, or unauthorized service functions.

**Expected outcome:** The analyzer remains unavailable and is escalated for qualified service evaluation.

## If the Problem Persists

Common external causes have been ruled out. The remaining problem may involve internal power distribution, module communication, motion hardware, sensors, control electronics, software, or another service-level condition.

The analyzer should be:
- Removed from service
- Labeled Out of Service
- Sent for repair or appropriate bench/on-site service evaluation
- Evaluated using Roche-approved documentation and approved test equipment
- Repaired or configured only by qualified personnel

Following repair, complete all required initialization, functional, calibration, QC, and laboratory return-to-service checks before patient testing resumes.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Redirect specimens before troubleshooting so delayed analyzer recovery does not create an avoidable patient-testing delay.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect patient testing first, verify power and external conditions before assuming an internal failure, confirm normal operation after correction, and escalate appropriately when startup cannot be safely restored. Clear CCR documentation preserves what was reported, found, and verified.

That is successful troubleshooting.
