---
schemaVersion: 1
title: "Siemens Healthineers Biograph Vision PET / CT System - System Will Not Power On or Complete Startup"
issueTitle: "System Will Not Power On or Complete Startup"
description: "Use this guide when the system is unresponsive, partially powered, or unable to complete normal startup due to power, connection, control, or environmental causes."
assetType: "PET / CT System"
manufacturer: "Siemens Healthineers"
model: "Biograph Vision"
slug: "siemens-healthineers-biograph-vision-system-will-not-power-on-or-complete-startup"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Biograph Vision operator workstation powered on, but the scanner would not complete startup."
  cause: "Clinical Engineering found an accessible system safety stop activated with no continuing unsafe condition present."
  resolution: "Clinical Engineering restored the safety control, completed a normal startup, verified scanner readiness and basic system operation, and returned the unit to service."
helpfulDetails:
  - "Exact point where startup stopped"
  - "Exact displayed alarm or message"
  - "Whether gantry, table, workstation, and displays powered"
  - "Facility power status"
  - "Emergency-stop status"
  - "Recent outage or maintenance activity"
  - "External cable condition"
  - "Room temperature or HVAC concerns"
  - "Result of controlled restart"
  - "Final scanner status"
---
## What This Guide Helps With

Use this guide when the system is unresponsive, partially powered, or unable to complete normal startup due to power, connection, control, or environmental causes.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Continuity of Care

Do not troubleshoot the Biograph Vision while a patient depends on the system for an active examination. Safely remove the patient from the table if possible and transfer the study to another verified imaging system when clinically necessary.

If there is smoke, unusual odor, visible electrical damage, fluid intrusion, abnormal heat, or repeated breaker operation, stop immediately and remove the system from service.

**Expected outcome:** The patient is safe, no examination depends on the affected system, and the equipment is safe to approach.

If an obvious hazardous condition is present, troubleshooting is complete; remove the system from service and escalate.

### 2. Confirm the Exact Startup Failure

Determine what clinical staff observed and where startup stops. Verify whether:

- The entire system appears unpowered.
- The operator workstation powers but the scanner does not.
- The gantry or table initializes but another subsystem does not.
- Startup stalls at a consistent point.
- An alarm or message appears.
- The failure followed a power outage, shutdown, maintenance activity, or room utility interruption.

Record the exact displayed message rather than paraphrasing it.

**Expected outcome:** The failed stage of startup and affected subsystem are clearly identified.

If the system completes normal startup during verification and repeated basic operation is normal, proceed to final verification and stop troubleshooting.

### 3. Verify Facility Power

Check accessible facility power sources associated with the PET / CT installation. Confirm that:

- Required room power is available.
- No accessible disconnect has been inadvertently turned off.
- No associated breaker or power distribution indicator is visibly abnormal.
- Other room equipment does not suggest a wider electrical outage.

Do not repeatedly reset a breaker that trips again. A repeated trip requires facilities or qualified service evaluation.

**Expected outcome:** Facility electrical power supplying the system appears available and stable.

If restoring an inadvertently disabled approved power source results in normal startup, verify full system operation and stop troubleshooting.

### 4. Inspect External Power and Control Connections

Inspect accessible external power and control connections without opening covers or cabinets. Look for:

- Loose or partially seated connectors.
- Damaged power cords or accessible cables.
- Pinched, crushed, or pulled cabling.
- Disconnected workstation or peripheral power.
- Damage caused by recent room movement or service activity.

Do not reconnect unidentified internal or high-voltage connections.

**Expected outcome:** Accessible system power and control connections are intact, secure, and undamaged.

If correcting an obvious external connection restores startup, perform final functional verification and stop.

### 5. Check Emergency-Off and Safety Controls

Verify that accessible emergency-stop or emergency-off controls associated with the system are not activated. Inspect their physical state before resetting anything.

Only restore a safety control when the reason for its activation is understood and no unsafe condition remains.

**Expected outcome:** Safety controls are in the appropriate normal operating condition.

If an inadvertently activated safety control is confirmed as the cause and normal startup returns after safe restoration, verify operation and stop.

### 6. Check Workstation and Peripheral Startup

Determine whether the operator workstation, displays, input devices, and required external peripherals are receiving power and starting normally.

Inspect:

- Display power and signal state.
- Keyboard and mouse connections.
- Accessible network connections.
- External power strips or approved UPS equipment, if part of the installed configuration.
- Whether a peripheral failure is preventing normal system interaction rather than preventing scanner power itself.

**Expected outcome:** Operator controls and required external peripherals are available and responsive.

If a loose external peripheral or power connection is corrected and startup completes normally, verify the system and stop.

### 7. Evaluate Room and Utility Conditions

Confirm that the imaging room and equipment spaces do not have obvious environmental or infrastructure problems such as:

- Excessive room temperature.
- Blocked ventilation.
- Water intrusion.
- Loss of required cooling.
- Recent electrical or HVAC outage.
- Active facility alarms.

Do not bypass environmental protections to force startup.

**Expected outcome:** No external room or utility condition is preventing normal startup.

If an environmental problem is corrected by the responsible department and the system starts normally afterward, complete functional verification and stop.

### 8. Attempt One Controlled Normal Restart if Appropriate

If no hazard is present and manufacturer-approved normal shutdown/startup controls remain available, perform one controlled restart according to the facility's approved operating process.

Avoid repeated power cycling. Repeated unsuccessful startup attempts can complicate fault diagnosis and may stress system components.

**Expected outcome:** The Biograph Vision completes its normal startup sequence without recurring faults.

If startup completes and the system remains stable, proceed to final verification and stop troubleshooting.

### 9. Perform Final Functional Verification

Before releasing the system, confirm that:

- Startup completes normally.
- Operator controls respond.
- Gantry and table status are normal.
- Required imaging subsystems report ready.
- No unresolved safety or system fault remains.
- Basic communication functions required for clinical use are available.

Perform any required return-to-service checks consistent with facility policy and manufacturer documentation.

**Expected outcome:** The system reaches a stable ready state and passes required return-to-service verification.

If all checks pass, troubleshooting is complete.

### 10. Escalate an Unresolved Startup Failure

If the system still will not power on or complete startup after external power, controls, connections, environment, and normal restart conditions have been verified, stop external troubleshooting.

**Expected outcome:** The unresolved system is removed from clinical use and routed for qualified service evaluation.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve internal power distribution, system controllers, subsystem communication, cooling infrastructure, startup configuration, or another service-level condition.

The device should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or qualified bench/system evaluation.
- Evaluated using appropriate Siemens Healthineers documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Do not bypass safety circuits, repeatedly reset protective devices, open high-voltage assemblies, or perform unauthorized internal troubleshooting.

After corrective service, complete appropriate functional, safety, and imaging-related return-to-service testing before clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Do not leave a patient positioned on an unavailable PET / CT system while troubleshooting startup; move the patient to a safe location and arrange alternate imaging as needed.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient first, verify facility power and accessible external causes before assuming an internal failure, stop when safe troubleshooting limits are reached, and document both the cause and final verification clearly.

That is successful troubleshooting.
