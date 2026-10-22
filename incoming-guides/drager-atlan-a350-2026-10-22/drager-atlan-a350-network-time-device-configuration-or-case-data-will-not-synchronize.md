---
schemaVersion: 1
title: "Drager Atlan A350 Anesthesia Machine - Network Time, Device Configuration, or Case Data Will Not Synchronize"
issueTitle: "Network Time, Device Configuration, or Case Data Will Not Synchronize"
description: "Troubleshoot network connectivity, incorrect synchronized time, configuration distribution, case-data transfer, cabling, infrastructure, and external interface problems."
assetType: "Anesthesia Machine"
manufacturer: "Drager"
model: "Atlan A350"
slug: "drager-atlan-a350-network-time-device-configuration-or-case-data-will-not-synchronize"
dateAdded: "2026-10-22"
taxonomyMode: "reuse"
ccr:
  complaint: "Anesthesia staff reported that the Atlan A350 displayed the wrong network time and completed cases were not appearing in the expected downstream system."
  cause: "Clinical Engineering found the anesthesia machine connected to a network port that was not providing the required clinical network connectivity after a room connection change."
  resolution: "Coordinated restoration of the correct network connection, verified time synchronization, confirmed successful case-data transfer to the receiving system, and returned the machine to service."
helpfulDetails:
  - "Exact synchronization function affected."
  - "Displayed date and time."
  - "Network connection status."
  - "Network cable condition."
  - "Wall port or connection used."
  - "Results with a known-good cable."
  - "Whether other devices were affected."
  - "Recent network or room changes."
  - "Receiving application status."
  - "Configuration differences observed."
  - "Restart results."
  - "End-to-end data-transfer test result."
  - "Final device status."
---

## What This Guide Helps With

Troubleshoot network connectivity, incorrect synchronized time, configuration distribution, case-data transfer, cabling, infrastructure, and external interface problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Clinical Workflow

Do not interrupt an active anesthetic solely to troubleshoot network, time, configuration, or case-data synchronization unless the issue creates a separate patient-safety concern.

If the machine is otherwise clinically functional:

- Inform clinical staff of the integration problem.
- Preserve required documentation using the facility's approved alternate workflow.
- Avoid restarting or disconnecting the machine during an active case unless clinically appropriate.
- Address the communication fault when the device can be safely taken out of active patient use.

**Expected outcome:** Patient care and required clinical documentation continue safely while the synchronization issue is isolated.

### 2. Confirm What Is Actually Failing

Determine whether the reported problem involves:

- Network connection.
- Incorrect date or time.
- Failure to synchronize time.
- Device configuration not updating.
- Case data not transmitting.
- Patient or case information not appearing.
- Intermittent connectivity.
- A problem limited to one destination system.

Check whether the condition affects only one Atlan A350 or multiple devices.

**Expected outcome:** The failure is narrowed to time, configuration, network transport, case data, or a receiving-system problem.

If the reported function is currently working normally and repeated testing shows no fault, document the findings and stop troubleshooting.

### 3. Check Network Cable and Physical Connection

Inspect the accessible network connection.

Check for:

- Disconnected cable.
- Loose connector.
- Damaged latch.
- Bent or damaged external connector.
- Pinched cable.
- Improper wall-port connection.
- Recently moved or replaced equipment.

Reseat accessible network connections when safe.

**Expected outcome:** The physical network connection is secure and undamaged.

If reseating the cable restores synchronization and communication remains stable, proceed to final verification and stop troubleshooting.

### 4. Test With a Known-Good Network Cable

If the cable is suspect, substitute a known-good cable appropriate for the network environment.

Avoid changing multiple infrastructure components simultaneously.

**Expected outcome:** The device establishes normal network connectivity with the known-good cable.

If communication returns, replace the defective cable, document the cause, and complete final verification.

### 5. Verify the Network Port or Connection Path

Determine whether the connected wall jack, switch path, or approved network connection is operational.

Where facility policy permits:

- Confirm the expected port is being used.
- Check the connection using an approved known-good device or network test method.
- Coordinate with IT if port status, VLAN assignment, security policy, or switch configuration must be verified.

Do not move the anesthesia machine to an arbitrary network segment as a workaround.

**Expected outcome:** The connected network port provides the expected authorized connectivity.

If the infrastructure port is the cause, coordinate correction with IT and verify synchronization afterward.

### 6. Review Device Network Status Without Unauthorized Changes

Use normal user-accessible status screens to review available connection information and indications.

Look for:

- Connected versus disconnected status.
- Obvious addressing problems.
- Missing network connection.
- Communication status changes.
- Indicators showing a remote system is unavailable.

Record existing settings before any approved change.

Do not alter protected network parameters, addresses, certificates, security settings, or service configuration without authorization.

**Expected outcome:** The device shows a network state consistent with the known facility configuration.

If an approved correction restores communication, proceed to functional verification.

### 7. Determine Whether the Problem Is Device-Specific or Infrastructure-Wide

Compare the affected Atlan A350 with another similar functioning device or another endpoint on the same supported workflow when available.

Ask:

- Are other anesthesia machines synchronizing normally?
- Are multiple devices showing the wrong time?
- Are case records from other rooms transmitting?
- Did the problem begin after network maintenance or an outage?
- Is the receiving clinical system available?

**Expected outcome:** The fault is isolated to the machine, local connection, network infrastructure, or receiving application.

If multiple devices are affected, escalate the infrastructure issue rather than performing unnecessary service on each anesthesia machine.

### 8. Verify Time Synchronization Behavior

If the reported issue is incorrect time:

- Compare the displayed time with the facility's authoritative clinical time source.
- Determine whether only the time is wrong or network communication is also unavailable.
- Check whether the discrepancy returns after normal operation or restart.
- Verify whether other networked devices are affected.

Do not manually compensate for persistent synchronization failure unless permitted by approved policy and configuration procedures.

**Expected outcome:** The Atlan A350 displays the correct facility time and remains synchronized.

If correct time synchronization returns after restoring network connectivity, the issue is resolved.

### 9. Verify Case Data and Receiving-System Availability

If network connectivity appears normal but case data does not transfer, determine where the data flow stops.

Verify:

- A case or record is created normally at the anesthesia machine.
- The expected receiving application or integration system is operational.
- Other devices can communicate with the same destination.
- The issue is not limited to one patient, case, room, or interface endpoint.

Protect patient information during testing and use approved test records where required.

**Expected outcome:** Case data traverses the expected workflow or the failure is isolated to a specific downstream system.

If the Atlan A350 sends data normally and the receiving system remains unable to process it, escalate to the appropriate IT, integration, or application support group.

### 10. Review Approved Configuration Consistency

If the problem involves configuration synchronization, compare approved user-visible configuration with a known-good equivalent device when appropriate.

Check for:

- Unexpected local configuration differences.
- Recent device replacement.
- Recent software or network changes.
- Incorrect room or workflow association where visible and authorized.
- Configuration that did not update after a central change.

Do not copy protected settings or make unauthorized service-level configuration changes.

**Expected outcome:** Approved device configuration is consistent with the intended clinical environment.

If an authorized configuration correction restores synchronization, document the change and verify all affected functions.

### 11. Use a Controlled Restart Only When Clinically Safe

If the machine is off-patient and approved workflow allows it, perform a normal controlled shutdown and restart.

Do not remove power abruptly to resolve a communications problem.

After restart, observe whether:

- Network connectivity returns.
- Time synchronizes.
- Configuration updates.
- Case-data communication resumes.

**Expected outcome:** The system completes startup normally and all required network functions reconnect.

If synchronization returns and remains stable, proceed to final verification.

### 12. Perform Final End-to-End Verification

Before closing the work order, verify the affected function from source to destination.

As applicable:

- Confirm network connectivity.
- Confirm correct device time.
- Confirm configuration state.
- Send or observe an approved test transaction.
- Verify the intended receiving system receives the data.
- Confirm no unrelated clinical functions were disturbed.

**Expected outcome:** The complete communication path functions normally and consistently.

If the end-to-end path is verified, troubleshooting can stop.

## If the Problem Persists

If power, physical cabling, network connection, local port, user-accessible configuration, device restart, receiving-system availability, and basic infrastructure checks have been completed, the remaining problem may involve:

- Network infrastructure.
- VLAN or routing configuration.
- Firewall or access-control policy.
- Time-server availability.
- Interface or integration middleware.
- Server-side configuration.
- Device software or protected configuration.
- Authentication or certificate-related services.
- An internal network-interface or service-level device problem.

The device should be removed from clinical service if the synchronization failure affects safe operation, alarm management, required documentation, or the facility's ability to use the equipment safely. When removal is required, label it **Out of Service** and send it for appropriate evaluation.

Service-level device issues should be:

- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Coordinated with IT, networking, clinical applications, or integration support where appropriate.
- Repaired or configured only by qualified personnel.

After correction, verify the complete end-to-end path rather than relying only on a connected-network indication.

Knowing when the problem has moved beyond the anesthesia machine and into infrastructure or application support is proper troubleshooting.

## Clinical Use Tip

When case-data synchronization fails, verify the entire path to the receiving clinical system and ensure staff have an approved alternate documentation workflow.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Networked anesthesia-system problems require the same disciplined approach as hardware faults: protect clinical workflow, verify the physical connection first, isolate device versus infrastructure causes, avoid unauthorized configuration changes, and confirm the complete data path before closing the work order.

That is successful troubleshooting.
