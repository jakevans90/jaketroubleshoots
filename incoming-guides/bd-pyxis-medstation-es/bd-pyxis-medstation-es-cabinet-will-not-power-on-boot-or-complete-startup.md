---
schemaVersion: 1
title: "BD Pyxis MedStation ES Medication Dispensing Cabinet - Cabinet Will Not Power On, Boot, or Complete Startup"
issueTitle: "Cabinet Will Not Power On, Boot, or Complete Startup"
description: "Cabinet is dead, stalls during startup, repeatedly restarts, or does not reach normal operation due to power, connection, peripheral, or system-level problems."
assetType: "Medication Dispensing Cabinet"
manufacturer: "BD"
model: "Pyxis MedStation ES"
slug: "bd-pyxis-medstation-es-cabinet-will-not-power-on-boot-or-complete-startup"
dateAdded: "2026-09-09"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported the Pyxis MedStation ES would not complete startup after a power interruption."
  cause: "Clinical Engineering found the cabinet had facility power but the external UPS output had not recovered correctly."
  resolution: "Restored the approved UPS power path, restarted the cabinet normally, and verified stable startup, login availability, secured drawers, and network connection."
helpfulDetails:
  - "Exact startup symptom or displayed message."
  - "Whether cabinet was completely dead or partially booted."
  - "AC receptacle test result."
  - "UPS status."
  - "Recent outage or relocation."
  - "External cable condition."
  - "Network link status."
  - "Whether nearby cabinets were affected."
  - "Point where startup stopped."
  - "Results after controlled restart."
  - "Final cabinet status."
---

## What This Guide Helps With

Cabinet is dead, stalls during startup, repeatedly restarts, or does not reach normal operation due to power, connection, peripheral, or system-level problems.

## Step-by-Step Troubleshooting

### 1. Protect Medication Access and Patient Care

Confirm clinical staff have an approved alternate method for medication access before troubleshooting. Do not continue troubleshooting a cabinet that is actively required for medication administration.

If the cabinet is cycling power, producing unusual heat or odor, or shows visible electrical damage, disconnect it from service and escalate immediately.

**Expected outcome:** Medication access is maintained through an alternate workflow and the cabinet can be evaluated without affecting patient care.

If patient care continuity is established and the cabinet later returns to reliable operation after the checks below, troubleshooting can stop after final verification.

### 2. Confirm the Exact Startup Condition

Determine whether the cabinet:

- Has no lights, fans, or display activity.
- Begins startup but freezes.
- Restarts repeatedly.
- Reaches a login or application screen but never becomes fully operational.
- Failed after a power interruption, relocation, maintenance event, or network outage.

Observe any displayed message without repeatedly power-cycling the cabinet.

**Expected outcome:** The failure is clearly identified as no-power, interrupted boot, restart, or incomplete application startup.

### 3. Verify Facility Power

Inspect the AC power cord and plug for damage, looseness, or accidental disconnection. Confirm the cord is fully seated at accessible connections.

Verify the receptacle has power using an approved tester or known-good method appropriate for Clinical Engineering.

If the cabinet is connected through an approved UPS or power-conditioning device, verify that device is powered and not indicating an obvious fault.

**Expected outcome:** Stable facility power is present and the cabinet power connection is secure.

If normal operation returns after restoring a loose or interrupted AC connection, perform final functional verification and stop troubleshooting.

### 4. Inspect External Power Components

Inspect accessible power cords, UPS connections, power strips if institutionally approved, and external switches for:

- Damage.
- Loose connections.
- Signs of overheating.
- Tripped or switched-off conditions.
- Evidence the cabinet was recently moved or unplugged.

Do not bypass protective devices or substitute unapproved power accessories.

**Expected outcome:** All external power components appear intact and correctly connected.

### 5. Perform One Controlled Restart When Appropriate

If there is no evidence of electrical damage and facility procedures permit it, perform a normal controlled restart using the approved cabinet power process.

Avoid repeated forced shutdowns because they can complicate software or database recovery.

Observe whether startup progresses consistently and note where it stops.

**Expected outcome:** The cabinet completes startup and reaches its normal operational state without freezing or restarting.

If startup completes normally and remains stable, proceed to final verification and stop troubleshooting.

### 6. Isolate External Peripherals When Safely Permitted

Inspect accessible external peripherals such as:

- Barcode scanner.
- Badge reader.
- Printer.
- External keyboard or pointing device if installed.
- Network cable.
- Other externally connected accessories.

Look for damaged connectors, pinched cables, liquid contamination, or a peripheral that appears physically compromised. Disconnecting peripherals should only be performed when allowed by local procedures and without altering secured medication-control functions.

**Expected outcome:** No external peripheral or cable is visibly causing the startup problem.

### 7. Check Network Status Separately From Power-Up

If the cabinet boots but cannot finish becoming operational, verify the network cable is connected and inspect available external link indicators where applicable.

Confirm whether other Pyxis stations or networked devices in the same area are also affected. Coordinate with IT or pharmacy system support when a broader outage is suspected.

Do not change network addressing or security configuration without authorization.

**Expected outcome:** The problem is identified as either cabinet-local or part of a network/server condition.

### 8. Verify Stable Operation

After the cabinet starts successfully:

- Confirm the display remains active.
- Confirm login functionality is available.
- Confirm drawers remain secured.
- Confirm expected network status is restored.
- Confirm no repeating restart or fault condition occurs during observation.

Do not perform medication transactions unless authorized and appropriate for testing.

**Expected outcome:** The cabinet remains stable and presents normal operational functions without recurrence.

If these checks pass, troubleshooting is complete.

### 9. Escalate an Unresolved Startup Failure

If stable power is present and the cabinet still will not boot, freezes, or repeatedly restarts, stop external troubleshooting.

Potential service-level causes may include internal power distribution, storage, operating system, application software, controller, or server-dependent conditions. Do not assume a specific failed component without further approved diagnostics.

**Expected outcome:** An unresolved cabinet is removed from clinical dependency and routed for appropriate service evaluation.

## If the Problem Persists

Common external power, connection, peripheral, and basic network causes have been ruled out.

The cabinet should be:

- Removed from service when medication security or availability cannot be assured.
- Labeled **Out of Service**.
- Sent for repair or appropriate bench/on-site technical evaluation.
- Evaluated using current manufacturer documentation and approved test equipment.
- Repaired, restored, or configured only by qualified personnel.

Return to service only after successful startup, stable operation, medication-security functions, communications, and applicable operational checks have been verified.

Knowing when to stop external troubleshooting rather than repeatedly forcing restarts is proper troubleshooting.

## Clinical Use Tip

Ensure pharmacy and nursing have an approved alternate medication-access process before removing a dispensing cabinet from service.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect medication access first, verify basic power and external conditions before assuming an internal failure, stop when deeper service is required, and document both the cause and final operational verification clearly.

That is successful troubleshooting.
