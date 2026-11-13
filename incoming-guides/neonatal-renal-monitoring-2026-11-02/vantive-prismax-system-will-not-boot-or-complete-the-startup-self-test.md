---
schemaVersion: 1
title: "Vantive PrisMax Continuous Renal Replacement Therapy (CRRT) - System Will Not Boot or Complete the Startup Self-Test"
issueTitle: "System Will Not Boot or Complete the Startup Self-Test"
description: "PrisMax does not power on, restarts during startup, or cannot complete initialization because of power, connection, accessory, or service-level problems."
assetType: "Continuous Renal Replacement Therapy (CRRT)"
manufacturer: "Vantive"
model: "PrisMax"
slug: "vantive-prismax-system-will-not-boot-or-complete-the-startup-self-test"
dateAdded: "2026-11-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the PrisMax powered on but repeatedly stopped during the startup self-test and could not be prepared for therapy."
  cause: "Clinical Engineering found the AC power connection was loose at the equipment inlet, causing intermittent power during startup."
  resolution: "Clinical Engineering secured the power connection, inspected the cord and inlet, completed repeated successful startups and functional checks, and returned the unit to service."
helpfulDetails:
  - "Exact startup message or alarm"
  - "Point in the startup sequence where failure occurred"
  - "Whether the unit was on AC or battery"
  - "Outlet test result"
  - "Power-cord and inlet condition"
  - "Whether the device restarted or shut down"
  - "External accessories connected"
  - "Any obstruction or incorrectly positioned component found"
  - "Results of repeated startup testing"
  - "Final device status"
---

## What This Guide Helps With

PrisMax does not power on, restarts during startup, or cannot complete initialization because of power, connection, accessory, or service-level problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Therapy
Do not troubleshoot a PrisMax that is providing unreliable renal replacement therapy while a patient depends on it. If the unit cannot reliably boot or complete its startup checks, transfer therapy to another verified device according to the clinical plan.

Remove the affected unit from active patient use until its condition is understood.

**Expected outcome:** Patient therapy is maintained on a reliable system and the affected PrisMax is available for controlled troubleshooting.

### 2. Confirm the Exact Startup Failure
Ask clinical staff what occurred and reproduce the condition without a patient connected when appropriate. Determine whether the system:
- Shows no signs of power
- Powers on and immediately shuts down
- Repeatedly restarts
- Stops at a consistent point during startup
- Displays a specific message or alarm
- Completes some checks but not the full startup sequence

Record the exact displayed wording rather than paraphrasing it.

**Expected outcome:** The failure is repeatable or clearly characterized. If the system now starts normally and repeated controlled startups are successful, continue to final verification before returning it to service.

### 3. Verify the AC Power Source
Confirm that the power cord is fully seated and inspect it for cuts, crushed areas, damaged insulation, bent contacts, or signs of overheating.

Test the receptacle using approved electrical test equipment or a known-good appropriately rated device according to facility practice. Avoid switched, loose, or questionable outlets.

**Expected outcome:** A stable AC power source is confirmed. If correcting the outlet or power connection allows normal startup, the issue is resolved and troubleshooting can stop after final verification.

### 4. Inspect the External Power Connection
Inspect the device power inlet and accessible external connections for looseness, contamination, physical damage, or evidence of liquid intrusion.

Do not continue energizing the unit if there is burning odor, abnormal heat, visible electrical damage, or evidence of fluid inside the equipment.

**Expected outcome:** External power connections are intact and undamaged. Any electrical damage or liquid intrusion requires removal from service and escalation.

### 5. Disconnect Nonessential External Accessories
Remove nonessential externally connected accessories, communication cables, or peripherals that are not required for a basic startup test.

Restart the system in its simplest approved configuration.

**Expected outcome:** The PrisMax completes startup with unnecessary peripherals removed. If so, reconnect accessories individually to identify the external source of the problem.

### 6. Check for Mechanical Interference Before Startup
Inspect accessible doors, holders, scales, pump areas, clamps, and disposable-loading regions for an incorrectly positioned component, retained disposable material, foreign object, or obstruction that could interfere with initialization.

Do not bypass interlocks or force mechanical components into position.

**Expected outcome:** All externally accessible mechanisms are unobstructed and correctly positioned. Removing an obstruction allows the startup sequence to continue normally.

### 7. Perform a Controlled Restart
With stable AC power and external obstructions ruled out, shut the system down normally when possible and perform another controlled startup.

Observe whether the failure occurs at the same point and document any displayed message.

**Expected outcome:** The system completes its normal startup sequence without restarting, freezing, or reporting a persistent fault. If successful repeatedly, proceed to final verification.

### 8. Perform Final Functional Verification
Before return to service, verify that the device:
- Powers up consistently
- Completes its normal startup checks
- Accepts normal operator input
- Displays information correctly
- Produces expected audible and visual indications
- Shows no evidence of power interruption or abnormal restart behavior

Perform any manufacturer-required post-repair or return-to-service testing appropriate to the work performed.

**Expected outcome:** Startup and basic system functions are repeatable and reliable. The unit may be returned to service only after all required verification passes.

### 9. Escalate a Persistent Startup Failure
If the PrisMax repeatedly fails startup after AC power, external connections, accessories, and mechanical obstructions have been ruled out, stop external troubleshooting.

Do not attempt board-level troubleshooting, internal power-supply repair, or unauthorized service-menu changes.

**Expected outcome:** The unit is removed from clinical use and routed for qualified service evaluation.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve internal power distribution, battery circuitry, startup electronics, sensing systems, embedded software, internal communication, or another service-level fault.

The device should be:
- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

After repair, complete the required electrical-safety, startup, alarm, and functional verification before returning the PrisMax to clinical use.

Knowing when to stop external troubleshooting and escalate an unreliable CRRT system is proper troubleshooting.

## Clinical Use Tip

Never delay renal replacement therapy while troubleshooting a questionable PrisMax; move the patient to another verified system when continuity of therapy is required.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Patient safety comes first. Verify AC power, connections, external accessories, and accessible mechanical conditions before assuming an internal failure. Escalate persistent startup problems appropriately and document both the cause and final verification clearly.

That is successful troubleshooting.
