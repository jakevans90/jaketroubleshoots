---
schemaVersion: 1
title: "GE Healthcare CardioLab Electrophysiology Recording System - System Will Not Power On or Complete Startup"
issueTitle: "System Will Not Power On or Complete Startup"
description: "CardioLab will not power on, boot normally, or reach an operational state because of power, peripheral, connection, or workstation startup problems."
assetType: "Electrophysiology Recording System"
manufacturer: "GE Healthcare"
model: "CardioLab"
slug: "ge-healthcare-cardiolab-system-will-not-power-on-or-complete-startup"
dateAdded: "2026-10-15"
taxonomyMode: "reuse"
ccr:
  complaint: "EP staff reported that the CardioLab workstation would not complete startup before a scheduled procedure."
  cause: "Clinical Engineering found a loose external power connection supplying the affected workstation."
  resolution: "The power connection was secured, CardioLab completed startup normally, acquisition functions were verified, and the system was returned to service."
helpfulDetails:
  - "Exact point where startup stopped"
  - "Components with or without power indicators"
  - "Outlet or power-source test results"
  - "Condition of power cords and UPS equipment"
  - "Displayed startup message"
  - "Network link status"
  - "External peripherals connected"
  - "Whether the issue followed a power interruption"
  - "Results after restart"
  - "Final functional test results"
  - "Final device status"
---

## What This Guide Helps With

CardioLab will not power on, boot normally, or reach an operational state because of power, peripheral, connection, or workstation startup problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Procedure Continuity

Do not troubleshoot an unreliable CardioLab system while a patient depends on it for active electrophysiology monitoring or recording. If a procedure is underway, notify the clinical team and establish an approved alternate monitoring or recording method before proceeding.

Confirm whether the reported problem involves the entire CardioLab system, one workstation, a display, an acquisition component, or an associated peripheral.

**Expected outcome:** The patient is supported by an appropriate alternate workflow and the affected portion of CardioLab is clearly identified.

If clinical operation has been safely restored using another system, continue troubleshooting only on equipment that is no longer supporting the patient.

### 2. Verify Facility Power and External Power Connections

Confirm the workstation, displays, acquisition hardware, isolation equipment, and any associated equipment rack are connected to their intended power sources. Inspect power cords, plugs, power strips, UPS equipment, and accessible breakers or switches for obvious damage or an OFF condition.

Verify the receptacle using an approved method when facility power is in question. Do not repeatedly reset a breaker that trips again.

**Expected outcome:** Required components receive stable facility power without damaged cords, tripped protection devices, or intermittent connections.

If restoring an external power connection allows normal startup, verify full system operation and stop troubleshooting.

### 3. Check Component Power States

Observe which CardioLab components show power indicators, fan activity, display backlighting, or other normal startup signs. Determine whether the failure affects all equipment or only one device in the system.

Ensure required monitors and externally accessible equipment switches are powered on.

**Expected outcome:** All required system components enter their normal startup sequence.

If only a display or peripheral was powered off and normal CardioLab operation returns after correction, verify functionality and stop troubleshooting.

### 4. Inspect External Cables and Peripheral Connections

Inspect accessible power, network, video, keyboard, mouse, acquisition-interface, and other external cables for looseness, damaged connectors, strain, or accidental disconnection.

Reseat only connections that are intended for routine external service access and can be safely disconnected with the system out of clinical use.

**Expected outcome:** External connections are secure and undamaged, and required peripherals are detected during startup.

If reseating a loose external connection restores normal startup, complete functional verification and stop troubleshooting.

### 5. Remove Nonessential External Peripherals When Appropriate

If the workstation begins startup but hangs before reaching the normal operating environment, disconnect recently added or nonessential USB devices or peripherals when permitted by local procedures.

Do not disconnect required clinical interfaces without first understanding their function.

**Expected outcome:** The workstation completes startup without interference from an external peripheral.

If removing a nonessential peripheral restores normal operation, identify and correct the accessory issue before return to service.

### 6. Observe the Startup Sequence and Record the Failure Point

Restart the affected equipment only when clinically safe and consistent with approved procedures. Observe whether the failure occurs before the operating system starts, during workstation login, during CardioLab software loading, or while connecting to acquisition hardware or network services.

Record displayed messages exactly without interpreting them as a specific internal failure unless confirmed by approved documentation.

**Expected outcome:** CardioLab completes startup and reaches its normal ready state, or a repeatable failure point is documented.

If startup completes normally and remains stable, continue to final verification.

### 7. Verify Network and Required System Communication

If CardioLab starts but does not become fully operational, verify external Ethernet connections, link indicators, approved network connectivity, and communication to associated CardioLab components.

Do not change IP addresses, VLAN assignments, firewall settings, or other managed network configuration without authorization.

**Expected outcome:** Required CardioLab components communicate normally after startup.

If restoring an external network connection resolves the issue, verify stable operation and stop troubleshooting.

### 8. Perform Final Functional Verification

Confirm the workstation remains powered, displays remain active, acquisition hardware is recognized, expected controls respond, and the system reaches its normal ready condition.

Where applicable, perform approved operational or return-to-service testing before releasing the system.

**Expected outcome:** CardioLab starts reliably and all required recording-system functions are available.

If the system completes verification without recurrence, troubleshooting is complete.

### 9. Escalate an Unresolved Startup Failure

If the system remains dead, repeatedly hangs, restarts, or cannot reach its normal operating state after external causes are ruled out, stop external troubleshooting.

Do not proceed into internal power supplies, computer hardware, circuit boards, or restricted service configuration without appropriate authorization and documentation.

**Expected outcome:** An unresolved system is removed from clinical use and routed for qualified service.

## If the Problem Persists

Common external power, connection, peripheral, and basic communication causes have been ruled out. Remaining possibilities may include workstation hardware, internal power distribution, software corruption, acquisition-system communication, managed network configuration, or another service-level condition.

The CardioLab system should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

After corrective work, complete applicable functional, electrical-safety, communication, and recording verification before return to clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Before troubleshooting CardioLab during an EP case, ensure the clinical team has another verified method to maintain required patient monitoring and procedural information.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient first, then work from facility power and external connections toward communication and software-level causes. Verify normal operation before assuming internal failure, escalate appropriately, and document the complaint, cause, and verified resolution clearly.

That is successful troubleshooting.
