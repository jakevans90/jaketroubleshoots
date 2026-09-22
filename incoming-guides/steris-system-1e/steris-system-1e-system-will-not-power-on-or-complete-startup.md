---
schemaVersion: 1
title: "STERIS SYSTEM 1E Endoscope Reprocessor (AER) - System Will Not Power On or Complete Startup"
issueTitle: "System Will Not Power On or Complete Startup"
description: "Troubleshoots loss of power, incomplete startup, failed initialization, external power problems, connection issues, and conditions preventing the SYSTEM 1E from becoming ready."
assetType: "Endoscope Reprocessor (AER)"
manufacturer: "STERIS"
model: "SYSTEM 1E"
slug: "steris-system-1e-system-will-not-power-on-or-complete-startup"
dateAdded: "2026-09-21"
taxonomyMode: "reuse"
ccr:
  complaint: "Sterile Processing reported the STERIS SYSTEM 1E would not complete startup and remained unavailable for processing."
  cause: "Clinical Engineering found the unit connected to a facility receptacle that was not supplying power."
  resolution: "Restored connection to a verified powered receptacle, confirmed repeated normal startup, and completed functional verification before returning the unit to service."
helpfulDetails:
  - "Whether the unit was completely dead or stopped during startup"
  - "Exact displayed message or alarm"
  - "Indicator light status"
  - "Facility outlet test result"
  - "Condition of cord and plug"
  - "Recent power interruption or relocation"
  - "Utility availability"
  - "Point where startup stopped"
  - "Results of controlled restart"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots loss of power, incomplete startup, failed initialization, external power problems, connection issues, and conditions preventing the SYSTEM 1E from becoming ready.

## Step-by-Step Troubleshooting
### 1. Protect Patient Care and Reprocessing Workflow
Do not rely on a SYSTEM 1E that cannot complete startup for processing devices needed for patient care. Move reprocessing to another validated unit or approved workflow according to facility policy. Do not consider any interrupted or questionable load processed.

**Expected outcome:** Clinical operations continue using an approved alternative while the affected unit is evaluated. If another verified unit restores workflow, continue troubleshooting the SYSTEM 1E offline.

### 2. Confirm the Exact Reported Condition
Ask staff whether the unit is completely dead, powers on briefly, stops during initialization, freezes at a startup screen, restarts repeatedly, or displays a specific message. Determine whether the problem followed a power interruption, cleaning, relocation, service activity, or utility event.

**Expected outcome:** The failure is reproduced or clearly characterized. If the unit now completes startup normally, perform additional startup cycles and functional verification before returning it to service.

### 3. Inspect for Immediate Safety Concerns
Check for liquid around the unit, unusual odor, overheating, damaged cords, damaged plugs, loose panels, visible leakage, or signs of electrical damage. Do not energize equipment with obvious electrical or water-related hazards.

**Expected outcome:** No unsafe physical condition is present. If damage, leakage, overheating, or electrical hazard is found, remove the unit from service and stop troubleshooting.

### 4. Verify Facility Power
Confirm that the unit is connected to its intended power source. Inspect the plug and accessible cord for damage or looseness. Verify the receptacle using an approved tester or known-good device when permitted by facility procedure. Check for a tripped facility breaker or switched receptacle only within Clinical Engineering's authorized scope.

**Expected outcome:** Stable facility power is available at the equipment connection. If restoring the power source allows normal startup, verify repeated operation and troubleshooting can stop.

### 5. Check Accessible Power Controls and Connections
Verify that accessible power switches, emergency shutoffs, disconnects, or related external controls are in their normal operating position. Confirm accessible external connectors have not been disturbed.

**Expected outcome:** Required external controls and connections are correctly positioned. If correcting an external connection restores startup, repeat startup and confirm normal readiness before stopping.

### 6. Perform a Controlled Power Cycle
If the equipment is safe to operate and no load is being processed, shut the unit down using the normal method when possible. Allow shutdown to complete, then restore power and observe the full startup sequence. Do not repeatedly cycle power if the unit continually resets or shows signs of hardware instability.

**Expected outcome:** The SYSTEM 1E completes initialization and reaches its normal ready state. If it does, perform functional verification and troubleshooting can stop.

### 7. Check Utility Availability Affecting Initialization
Confirm required facility utilities serving the reprocessor are available and that accessible supply valves have not been closed. A unit may energize but remain unavailable if required water, drain, or other infrastructure conditions are not satisfied.

**Expected outcome:** Required facility utilities are available and no obvious external utility issue is preventing readiness. If restoring a utility allows startup to complete, verify normal operation and stop.

### 8. Review Observable Messages and Indicators
Record any startup message, alarm text, indicator status, or point in the startup sequence where progress stops. Do not clear configuration, enter unauthorized service modes, or repeatedly acknowledge unexplained faults simply to place the unit into service.

**Expected outcome:** Any remaining startup failure is documented accurately enough for service escalation. If the message clears after correction of an identified external cause and the unit starts normally, continue to final verification.

### 9. Perform Final Functional Verification
After a correction, restart the unit again and confirm normal display operation, controls, utility readiness, door operation, and absence of abnormal alarms or leakage. Conduct any required return-to-service testing according to facility and manufacturer procedures.

**Expected outcome:** The SYSTEM 1E starts consistently and is ready for normal processing without abnormal indications. Troubleshooting can stop.

### 10. Escalate an Unresolved Startup Failure
If reliable facility power, accessible connections, controls, and utilities are verified but startup still fails, stop external troubleshooting. Do not perform board-level repair or unauthorized internal adjustments.

**Expected outcome:** The unit is removed from clinical use and routed for qualified service evaluation.

## If the Problem Persists
Common external power, connection, control, and utility causes have been ruled out. The remaining problem may involve internal power distribution, startup electronics, sensors, software, safety interlocks, or another service-level condition.

Remove the SYSTEM 1E from service, label it **Out of Service**, and send it for repair or bench evaluation. Evaluation should use appropriate STERIS service documentation and approved test equipment. Internal repairs, configuration changes, or calibration should be performed only by qualified personnel.

Before return to service, verify startup, controls, safety functions, utilities, processing readiness, and any required performance or electrical safety tests.

Stopping after safe external troubleshooting has been exhausted is proper troubleshooting.

## Clinical Use Tip
Never release or reuse a load from a reprocessor that lost power or failed startup before a validated processing cycle was completed.

## Work Order Documentation (CCR Method)
<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)
<!-- Helpful details come from front matter. -->

## Final Thought
Protect the processing workflow first, verify power and external conditions before assuming an internal failure, confirm the correction through repeated functional checks, escalate appropriately, and document the event clearly.

That is successful troubleshooting.
