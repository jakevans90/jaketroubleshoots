---
schemaVersion: 1
title: "GE Healthcare NM/CT 870 CZT PET / CT System - Workstation Freezes or Loses Communication"
issueTitle: "Workstation Freezes or Loses Communication"
description: "The operator workstation freezes, becomes unresponsive, or loses communication with acquisition hardware because of connections, software state, network, or subsystem availability."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "NM/CT 870 CZT"
slug: "ge-healthcare-nm-ct-870-czt-workstation-freezes-or-loses-communication"
dateAdded: "2026-09-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported the NM/CT 870 CZT workstation became unresponsive and lost communication with the acquisition system."
  cause: "Clinical Engineering found an accessible external communication cable was partially disconnected at the workstation."
  resolution: "Clinical Engineering secured the connection, performed an approved restart, verified stable workstation and acquisition communication, and returned the system to service."
helpfulDetails:
  - "Frozen application or entire workstation"
  - "Mouse and keyboard response"
  - "Exact communication message"
  - "Acquisition subsystem status"
  - "Workstation power state"
  - "External cable condition"
  - "Network link indication"
  - "Other network resources affected"
  - "Restart result"
  - "Final communication status"
---
## What This Guide Helps With

The operator workstation freezes, becomes unresponsive, or loses communication with acquisition hardware because of connections, software state, network, or subsystem availability.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop the Examination

If the workstation becomes unreliable during a patient examination, do not continue scanning or positioning through an unresponsive interface. Safely end the study and remove or transfer the patient as clinically appropriate.

**Expected outcome:** The patient is no longer dependent on an unreliable control interface.

### 2. Determine Whether the Problem Is a Freeze or Communication Loss

Check whether the mouse and keyboard respond, whether the display updates, and whether the application is frozen while the operating system remains responsive.

Determine whether acquisition hardware is still visible or whether the workstation specifically reports loss of communication.

**Expected outcome:** The fault is categorized as workstation unresponsiveness, application failure, or subsystem communication loss.

### 3. Check Workstation Power and External Connections

Inspect accessible workstation power, monitor connections, keyboard, mouse, and authorized communication or network cables.

Look for looseness, damage, or an inadvertently disconnected cable.

**Expected outcome:** External workstation connections are secure and normal. If correction restores stable operation, complete functional verification and troubleshooting can stop.

### 4. Verify Other System Components Remain Powered

Check normal status indicators for the gantry, detectors, CT subsystem, acquisition computers, and other required system components.

A workstation may report communication failure because the remote subsystem has lost power or failed startup.

**Expected outcome:** Required remote subsystems remain powered and initialized.

### 5. Check the Network or System Communication Path

When within Clinical Engineering scope, verify link indicators, accessible switch connections, approved network cabling, and relevant physical network path.

Do not change VLANs, addresses, firewall rules, or protected system configuration without authorization.

**Expected outcome:** The external communication path is intact or an infrastructure issue is identified for escalation.

### 6. Identify the Scope of the Communication Failure

Determine whether the workstation cannot communicate only with the scanner hardware, or whether it also cannot reach PACS, worklist, or other network resources.

This helps distinguish local acquisition communication from a broader network problem.

**Expected outcome:** The failure is localized to system-internal communication or broader network connectivity.

### 7. Perform a Controlled Application or System Restart

If patient care is no longer dependent on the system and there is no evidence of hardware damage or unstable power, use the approved shutdown/restart process.

Avoid forced power cycling unless specifically authorized.

**Expected outcome:** The workstation and connected acquisition components initialize normally and maintain communication.

### 8. Verify Input Devices and Display Response

Confirm the keyboard, mouse, touchscreen if applicable, and display behave normally after restart.

Use known-good approved external input peripherals where appropriate to rule out a simple accessory failure.

**Expected outcome:** Operator controls are responsive and stable.

### 9. Perform Functional Communication Verification

Verify the workstation can communicate with required acquisition hardware and complete an appropriate nonpatient system test.

If network functions are also required, verify the relevant approved communication path.

**Expected outcome:** Workstation control and system communication remain stable. The issue is resolved and troubleshooting can stop.

### 10. Escalate Recurrent Freezes or Communication Loss

If the workstation repeatedly freezes, disconnects, restarts unexpectedly, or loses acquisition communication despite normal external connections, remove the system from service.

Do not perform unsupported operating-system changes, software installation, internal computer repair, or protected configuration changes.

**Expected outcome:** A recurrent control-system or communication problem is escalated before it can affect another patient study.

## If the Problem Persists

Common external workstation, peripheral, cable, power, and network-path causes have been ruled out. Remaining categories may include workstation hardware, acquisition computers, system software, internal network components, storage, interface services, or protected configuration.

The device should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or controlled system evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved diagnostic tools.
- Repaired, restored, or configured only by qualified personnel.

Verify workstation stability, acquisition communication, required network functions, and system operation before return to clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not use an intermittently responsive workstation to control patient positioning or acquisition simply because the screen begins responding again.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

An unreliable workstation is a system-control problem, so protect the patient first, verify simple connections and communication paths, confirm stable operation after correction, and escalate recurring failures rather than relying on temporary recovery.

That is successful troubleshooting.
