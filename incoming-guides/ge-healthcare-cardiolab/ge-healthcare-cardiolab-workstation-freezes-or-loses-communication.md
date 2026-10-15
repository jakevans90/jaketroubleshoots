---
schemaVersion: 1
title: "GE Healthcare CardioLab Electrophysiology Recording System - Workstation Freezes or Loses Communication"
issueTitle: "Workstation Freezes or Loses Communication"
description: "CardioLab workstation becomes unresponsive or loses communication because of peripherals, network connections, acquisition interfaces, software, or infrastructure problems."
assetType: "Electrophysiology Recording System"
manufacturer: "GE Healthcare"
model: "CardioLab"
slug: "ge-healthcare-cardiolab-workstation-freezes-or-loses-communication"
dateAdded: "2026-10-15"
taxonomyMode: "reuse"
ccr:
  complaint: "EP staff reported that the CardioLab workstation lost communication with the acquisition hardware during room setup."
  cause: "Clinical Engineering found the external Ethernet connection at the workstation partially disconnected."
  resolution: "The cable was secured, communication and simulated signal acquisition remained stable during testing, and CardioLab was returned to service."
helpfulDetails:
  - "Time of freeze or communication loss"
  - "Application versus entire-workstation response"
  - "Exact displayed message"
  - "Peripheral status"
  - "Network link indicators"
  - "Acquisition-hardware status"
  - "Infrastructure issues observed"
  - "Whether the problem followed a recent change"
  - "Restart results"
  - "Recurrence during testing"
  - "Final communication status"
  - "Final device status"
---

## What This Guide Helps With

CardioLab workstation becomes unresponsive or loses communication because of peripherals, network connections, acquisition interfaces, software, or infrastructure problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Active Monitoring

Do not troubleshoot a frozen or communication-impaired CardioLab workstation while a patient depends on it as the only reliable monitoring or recording path.

Notify the clinical team and establish an approved alternate method before restarting, disconnecting, or manipulating the affected system.

**Expected outcome:** Patient monitoring and procedural continuity are maintained independently of the unstable workstation.

### 2. Confirm What Has Frozen or Disconnected

Determine whether the entire computer is unresponsive, only the CardioLab application is affected, displays are frozen while acquisition continues, or communication has been lost to specific acquisition or network components.

Record the time and any displayed message.

**Expected outcome:** The failure is narrowed to the workstation, application, acquisition link, or network path.

### 3. Check External Peripherals

Verify keyboard, mouse, displays, and other externally connected peripherals are functioning. A failed input device or display can appear to be a frozen workstation.

Inspect for disconnected or recently added USB devices.

**Expected outcome:** The apparent freeze is not caused by a failed external control or display.

If a peripheral is the cause and normal workstation operation is confirmed after replacement or reconnection, stop troubleshooting.

### 4. Inspect Communication Connections

Check accessible Ethernet and CardioLab acquisition-interface connections for looseness, damaged latches, strain, or disconnected cables.

Observe available network or device-link indicators without altering configuration.

**Expected outcome:** All required external communication paths are physically intact.

If reconnecting an approved external cable restores stable communication, verify the system and stop troubleshooting.

### 5. Check Network and Infrastructure Status

Determine whether other devices in the same room or network segment are experiencing communication problems.

Verify relevant network links and contact IT or integration support when facility network availability is questionable.

Do not change IP addresses, VLAN settings, domain settings, or firewall rules without authorization.

**Expected outcome:** The problem is identified as either CardioLab-local or part of a wider infrastructure issue.

If infrastructure restoration resolves CardioLab communication, verify stable operation and stop troubleshooting.

### 6. Preserve Information Before Restarting

When possible, document the displayed state, error text, recent actions, patient-study status, and approximate time of failure before restarting the workstation.

Follow local incident-preservation requirements if the freeze occurred during a serious clinical event.

**Expected outcome:** Useful troubleshooting and event information is preserved before system state is cleared.

### 7. Perform an Approved Orderly Restart

Once CardioLab is no longer supporting the patient, perform the approved restart procedure. Avoid repeated hard power cycling unless the system cannot be shut down normally and local procedures permit it.

Observe whether the workstation and acquisition hardware reconnect normally.

**Expected outcome:** The workstation restarts, CardioLab loads normally, and required communications remain stable.

If normal operation returns and remains stable, continue to final verification.

### 8. Verify Acquisition and Network Functions

Use an approved simulator or functional workflow to confirm signal acquisition, workstation responsiveness, communication with acquisition hardware, and any required network services.

Test for recurrence during a reasonable functional check.

**Expected outcome:** CardioLab remains responsive and maintains required communication.

If the system passes without recurrence, troubleshooting is complete.

### 9. Escalate Recurrent Freezing or Communication Loss

If the freeze recurs, communication drops repeatedly, or CardioLab cannot reconnect after external network and cable causes are ruled out, remove the system from service.

Do not perform unsupported operating-system modifications, software reinstalls, internal computer repair, or protected configuration changes.

**Expected outcome:** The unstable workstation is escalated for qualified software, hardware, or infrastructure evaluation.

## If the Problem Persists

External peripherals, network connections, acquisition interfaces, and basic infrastructure causes have been ruled out. Remaining possibilities may involve workstation hardware, operating system or CardioLab software, network services, acquisition hardware, storage, or managed configuration.

The CardioLab system should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved diagnostic tools.
- Repaired or configured only by qualified personnel.

After corrective work, verify workstation stability, signal acquisition, communication, and applicable data functions before return to service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Before restarting a frozen CardioLab workstation during an EP procedure, make sure another verified system is maintaining the patient information clinicians still need.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Separate an apparent workstation freeze from peripheral, network, and acquisition-link failures before assuming a computer problem. Preserve useful failure information, restart only when clinically safe, verify stability, and escalate recurrent problems appropriately.

That is successful troubleshooting.
