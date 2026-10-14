---
schemaVersion: 1
title: "Canon Alphenix Sky+ Angiography System - System Will Not Power On or Complete Startup"
issueTitle: "System Will Not Power On or Complete Startup"
description: "Troubleshoot startup failure, incomplete initialization, power loss, external power problems, emergency-stop conditions, disconnected components, or system communication problems."
assetType: "Angiography System"
manufacturer: "Canon"
model: "Alphenix Sky+"
slug: "canon-alphenix-sky-system-will-not-power-on-or-complete-startup"
dateAdded: "2026-10-14"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Canon Alphenix Sky+ stopped during startup and would not reach the ready condition."
  cause: "Clinical Engineering found an accessible external system interconnect cable partially disconnected."
  resolution: "Clinical Engineering secured the connection, restarted the system, verified normal startup and basic system operation, and returned the unit to service."
helpfulDetails:
  - "Exact startup message or indication"
  - "Components that powered on or remained off"
  - "Facility power status"
  - "Emergency-stop or shutdown-control status"
  - "Condition of external cables and connections"
  - "Whether restart changed the condition"
  - "Any unusual sound, heat, odor, or visible damage"
  - "Results of final functional verification"
  - "Final device status"
---
## What This Guide Helps With
Troubleshoot startup failure, incomplete initialization, power loss, external power problems, emergency-stop conditions, disconnected components, or system communication problems.

## Step-by-Step Troubleshooting
### 1. Protect the Patient and Maintain Continuity of Care
Do not troubleshoot an unavailable or unreliable angiography system while it is needed for an active procedure. If a patient is involved, coordinate with clinical staff and move care to an appropriate alternative system or workflow before troubleshooting.

**Expected outcome:** The patient is no longer dependent on the affected system and troubleshooting can proceed safely.

### 2. Confirm the Exact Startup Failure
Determine whether the entire system is unpowered, some components power on, startup stops at a particular stage, or an error message appears. Record the exact message and which consoles, displays, generators, tables, or related components appear operational.

**Expected outcome:** The failure is narrowed to a complete power loss, partial-system problem, or startup/communication failure.

### 3. Verify Facility Power
Confirm that the system's normal facility power source is available. Check accessible disconnects, approved power controls, and room power indicators for an abnormal condition. Do not reset breakers or facility electrical protection unless authorized by site procedure.

**Expected outcome:** Required facility power is available. If restoring an approved external power condition returns the system to normal startup, troubleshooting can stop after functional verification.

### 4. Inspect External Power and Communication Connections
Inspect accessible power cords, interconnect cables, console connections, display connections, and external system cables for looseness, physical damage, strain, or accidental disconnection.

**Expected outcome:** All accessible connections are secure and undamaged. Correcting a loose external connection restores normal startup if it was the cause.

### 5. Check Emergency and Safety Controls
Verify that accessible emergency-stop or shutdown controls have not been activated and that no room safety condition is intentionally preventing operation. Do not bypass or defeat a safety interlock.

**Expected outcome:** No external safety control is preventing startup. If an unintentionally activated control is safely restored and startup completes normally, troubleshooting can stop.

### 6. Check Connected System Components
Verify that required external consoles, monitors, operator controls, table interfaces, imaging components, and approved peripherals are connected and powered as applicable. Look for one subsystem that remains offline while the rest of the system starts.

**Expected outcome:** Required system components are present and available for initialization.

### 7. Perform an Approved Restart
If patient care is protected and no hardware damage, smoke, odor, overheating, or electrical abnormality is present, perform a normal shutdown and restart using approved operating controls.

**Expected outcome:** The system completes startup without repeating the reported failure. If it does, proceed to final verification and stop troubleshooting.

### 8. Perform Final Functional Verification
Confirm that the system reaches its normal ready condition and that operator controls, displays, table functions, communications, and required imaging readiness indicators behave normally. Complete any required return-to-service testing applicable to the work performed.

**Expected outcome:** The angiography system starts reliably and passes applicable functional checks.

### 9. Escalate an Unresolved Startup Failure
If startup repeatedly fails, a subsystem remains unavailable, or normal operation cannot be verified, stop external troubleshooting.

**Expected outcome:** The system remains removed from clinical use and is referred for qualified service evaluation.

## If the Problem Persists
Common external power, connection, safety-control, peripheral, and restart causes have been ruled out. The remaining problem may involve internal power distribution, system control, subsystem communication, software, configuration, or other service-level conditions.

Remove the system from service, label it **Out of Service**, and arrange repair or bench/service evaluation as appropriate. Evaluation should use current manufacturer documentation and approved diagnostic or test equipment. Internal repair, configuration changes, or service-level adjustments should be performed only by qualified personnel.

Return the system to service only after the fault is corrected and required functional, safety, and imaging-system verification is successfully completed. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
Do not begin or continue an invasive procedure on an angiography system that cannot reliably complete startup and demonstrate normal system readiness.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought
Protect the patient first, verify power and external system conditions before assuming an internal failure, escalate persistent startup problems appropriately, and document both the cause and final verification clearly.

That is successful troubleshooting.
