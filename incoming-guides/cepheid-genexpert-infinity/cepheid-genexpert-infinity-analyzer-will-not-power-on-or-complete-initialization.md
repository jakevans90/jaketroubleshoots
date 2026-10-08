---
schemaVersion: 1
title: "Cepheid GeneXpert Infinity Molecular Diagnostic System - Analyzer Will Not Power On or Complete Initialization"
issueTitle: "Analyzer Will Not Power On or Complete Initialization"
description: "Troubleshoot loss of power, incomplete startup, initialization failures, workstation problems, external connections, environmental conditions, and other noninvasive causes."
assetType: "Molecular Diagnostic System"
manufacturer: "Cepheid"
model: "GeneXpert Infinity"
slug: "cepheid-genexpert-infinity-analyzer-will-not-power-on-or-complete-initialization"
dateAdded: "2026-10-08"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that the GeneXpert Infinity powered partially but would not complete initialization."
  cause: "Clinical Engineering found the system workstation power connection loose at the approved external power source."
  resolution: "Clinical Engineering secured the connection, restarted the system, verified successful initialization and normal ready status, and released it for laboratory quality verification."
helpfulDetails:
  - "Exact startup message or observed stopping point"
  - "Whether the system was completely dead or partially powered"
  - "Workstation and display status"
  - "Facility outlet or approved power-source test result"
  - "UPS or power-distribution status"
  - "External cable condition"
  - "Recent power, IT, network, or relocation activity"
  - "Unusual heat, odor, noise, or damage"
  - "Results before and after restart"
  - "Final system status"
---
## What This Guide Helps With

Troubleshoot loss of power, incomplete startup, initialization failures, workstation problems, external connections, environmental conditions, and other noninvasive causes.

## Step-by-Step Troubleshooting

### 1. Protect Testing Continuity and Patient Care
Determine whether patient specimens are currently loaded, processing, or awaiting testing. Coordinate with laboratory staff before cycling power or interrupting the system. If testing cannot continue reliably, redirect time-sensitive specimens to another validated testing method or analyzer according to laboratory procedure.

Do not troubleshoot an unreliable diagnostic system while patient results depend on it operating correctly.

**Expected outcome:** Active testing is protected or transferred, and the system can be evaluated without risking specimens or delaying critical results. If continuity is established, continue troubleshooting.

### 2. Confirm the Exact Startup Failure
Ask laboratory staff what occurred and observe the system state. Determine whether the system is completely dead, powers partially, reaches the workstation but not the analyzer, stops during initialization, or displays a specific message.

Record the exact displayed message rather than paraphrasing it.

**Expected outcome:** The failure is narrowed to loss of incoming power, workstation startup, analyzer startup, or incomplete initialization. If the system now initializes normally, troubleshooting can stop after verification.

### 3. Verify Facility Power
Inspect the power connection and confirm applicable plugs are fully seated and undamaged. Verify the receptacle or approved power source is functioning using an appropriate method. Check for evidence of a tripped facility circuit, disconnected UPS, or other external power interruption.

Do not repeatedly reset a circuit that trips again.

**Expected outcome:** Stable facility power is available to the system. If restoring an external power source allows normal initialization, proceed to final functional verification.

### 4. Inspect External Power Components
Inspect accessible power cords, approved power distribution equipment, UPS connections, and external switches for looseness, damage, heat, discoloration, or signs of liquid exposure.

Verify required external components are switched on and operating.

**Expected outcome:** External power components are intact and correctly connected. Damaged electrical components require removal from service rather than continued operation.

### 5. Verify Workstation and System Components Start
Observe whether the workstation, display, and GeneXpert Infinity system components start normally. A workstation that remains off or a display with no signal may create the appearance that the entire system failed.

Check external display and workstation connections without opening equipment enclosures.

**Expected outcome:** The workstation and analyzer components reach their normal startup states. If reseating an external connection restores operation, verify the complete system before returning it to use.

### 6. Check External Communication Connections
Inspect accessible Ethernet and other required system communication cables. Confirm connectors are seated and that no recent IT, switch, network, or workstation changes coincide with the startup problem.

Avoid changing network configuration simply to test a theory.

**Expected outcome:** Required external communication paths are physically connected and unchanged from the validated configuration.

### 7. Check the Operating Environment
Verify that ventilation openings are unobstructed and the system has not been exposed to excessive heat, moisture, cleaning fluid, or recent relocation. Look for unusual odor, abnormal fan behavior, or physical damage.

**Expected outcome:** The environment is suitable for operation with no visible condition that would prevent startup. Abnormal heat, odor, or electrical damage requires immediate removal from service.

### 8. Perform an Approved Restart When Appropriate
If no active testing is at risk and laboratory workflow permits it, perform a normal system shutdown and restart using the established site or manufacturer-approved process.

Do not repeatedly power-cycle a system that consistently fails at the same point.

**Expected outcome:** The system completes initialization and reaches its normal ready state. If it does, verify normal operation and stop troubleshooting.

### 9. Verify Functional Readiness
Confirm with laboratory personnel that the system recognizes its available components and reaches the expected operational state. Verify that no persistent startup or communication messages remain.

Any required laboratory quality checks must be completed according to laboratory policy before patient testing resumes.

**Expected outcome:** The complete system initializes normally and is acceptable for clinical operation.

### 10. Escalate an Unresolved Initialization Failure
If verified power, connections, workstation operation, network connections, and environmental conditions are normal but initialization still fails, stop external troubleshooting.

**Expected outcome:** The equipment remains out of clinical service pending qualified evaluation rather than being repeatedly restarted or partially used.

## If the Problem Persists

Common external power, connection, workstation, communication, and environmental causes have been ruled out. The remaining problem may involve an internal power subsystem, automation component, module, controller, software service, configuration, or another service-level condition.

The GeneXpert Infinity should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or appropriate bench/service evaluation
- Evaluated using current manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not open assemblies or attempt board-level troubleshooting unless specifically authorized and trained to do so. Following repair, complete applicable functional verification and laboratory-required quality processes before return to patient testing.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Confirm an alternate validated testing pathway is available before interrupting an analyzer handling time-sensitive molecular diagnostic specimens.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect patient testing first, then verify power and external dependencies before assuming an internal failure. A successful repair includes functional verification, appropriate escalation when needed, and clear CCR documentation.

That is successful troubleshooting.
