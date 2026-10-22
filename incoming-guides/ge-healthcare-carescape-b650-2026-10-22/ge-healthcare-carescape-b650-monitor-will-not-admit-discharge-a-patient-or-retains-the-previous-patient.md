---
schemaVersion: 1
title: "GE Healthcare CARESCAPE B650 Patient Monitor - Monitor Will Not Admit/Discharge a Patient or Retains the Previous Patient"
issueTitle: "Monitor Will Not Admit/Discharge a Patient or Retains the Previous Patient"
description: "Troubleshoot patient admit/discharge failures, retained demographics, workflow configuration, network connectivity, and communication problems that can leave the wrong patient associated with the monitor."
assetType: "Patient Monitor"
manufacturer: "GE Healthcare"
model: "CARESCAPE B650"
slug: "ge-healthcare-carescape-b650-monitor-will-not-admit-discharge-a-patient-or-retains-the-previous-patient"
dateAdded: "2026-10-22"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the CARESCAPE B650 continued displaying the previous patient's demographics and would not retain a new patient admission."
  cause: "Clinical Engineering found the monitor's network cable was not fully seated, preventing normal synchronization with the monitoring system."
  resolution: "Reseated the network connection and verified successful discharge of the prior patient, admission of the correct patient, and matching patient information at the bedside and central monitoring system."
helpfulDetails:
  - "Exact admit or discharge symptom"
  - "Previous patient information retained"
  - "Whether demographics clear temporarily"
  - "Bed and location shown on the monitor"
  - "Network connection and link status"
  - "Whether other monitors are affected"
  - "Central-station patient information"
  - "Whether the issue follows one bed or one monitor"
  - "Results before and after restart"
  - "Results after network correction"
  - "Admit/discharge verification results"
  - "Bedside-to-central synchronization result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoot patient admit/discharge failures, retained demographics, workflow configuration, network connectivity, and communication problems that can leave the wrong patient associated with the monitor.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification and Clinical Data Integrity

Do not continue routine monitoring under incorrect patient demographics when data could be stored, transmitted, or associated with the wrong patient record.

Confirm the patient's identity using approved clinical workflow. If necessary, use another verified monitor or follow the facility's downtime or unidentified-patient process until correct association can be established.

Expected outcome: No new clinical data is knowingly assigned to the wrong patient while troubleshooting proceeds.

### 2. Confirm the Exact Admit/Discharge Failure

Determine whether the CARESCAPE B650 will not admit a new patient, will not discharge the current patient, retains previous demographics after discharge, reloads an old patient after restart, or receives incorrect patient information from another system.

Record the displayed patient information and any related message exactly as shown.

Expected outcome: The failure is clearly identified as an admit, discharge, retention, or external patient-association problem. If the current patient information is correct and the problem cannot be reproduced, troubleshooting can stop after workflow verification.

### 3. Verify the Monitor's Current Patient Information

Review the patient name, identifier, bed, unit, or other available demographic fields through normal clinical workflow.

Confirm whether the retained information exists only on the bedside monitor or is also visible at the central station or downstream clinical system.

Expected outcome: The technician determines where the incorrect patient association is present. If the incorrect data exists only at one endpoint, troubleshooting can be focused appropriately.

### 4. Attempt the Normal Discharge Workflow

Using the standard authorized clinical workflow, attempt to discharge the previous patient.

Observe whether the monitor clears the demographics, rejects the discharge, appears to clear them temporarily, or immediately repopulates the same information.

Expected outcome: The previous patient's information clears and remains cleared. If successful, proceed with a test admission or approved workflow verification and troubleshooting can stop when correct operation is confirmed.

### 5. Check for Pending or Incomplete User Actions

Verify that required fields, confirmations, or workflow selections have been completed. Ensure the monitor is not awaiting a final confirmation or presenting a status that has been overlooked.

Do not create fictitious patient information merely to force the workflow.

Expected outcome: The admit/discharge operation completes without an unresolved local workflow step. If correcting the workflow resolves the problem, troubleshooting can stop.

### 6. Verify Bed and Location Configuration

Confirm that the monitor is associated with the intended clinical location, bed, or care area and that staff are not attempting to admit a patient through a workflow intended for another location.

Do not alter permanent location configuration without authorization.

Expected outcome: The monitor's displayed location and expected clinical placement are consistent. If a documented configuration mismatch is corrected by authorized personnel and patient association works normally afterward, troubleshooting can stop.

### 7. Check Network Connectivity

Verify that the CARESCAPE B650 has normal network connectivity based on its installed configuration.

Inspect accessible network cabling, docking connections, link indicators, and other external network components. Compare behavior with nearby functioning monitors when useful.

Expected outcome: The monitor has stable network connectivity and no obvious external network connection problem. If restoring a disconnected network path allows patient admit/discharge functions to synchronize correctly, troubleshooting can stop after verification.

### 8. Determine Whether the Problem Is Local or System-Wide

Check whether other monitors in the same care area are experiencing similar admission, discharge, or patient-association problems.

If multiple devices are affected simultaneously, avoid repeatedly modifying individual monitors. Escalate toward the central monitoring, network, interface, or clinical-system infrastructure.

Expected outcome: The fault is identified as isolated to the CARESCAPE B650 or affecting a wider monitoring environment. If the broader system is restored and the monitor synchronizes correctly, troubleshooting can stop.

### 9. Compare With the Central Station or Patient-Management Source

Where applicable, verify whether the central monitoring system or connected patient-management source shows the correct current patient and bed assignment.

A bedside monitor that repeatedly receives old demographics may be reflecting information supplied by another system rather than locally storing it incorrectly.

Expected outcome: Patient information is consistent across the expected monitoring path, or the location where incorrect data originates is identified for escalation.

### 10. Restart the Monitor Only When Clinically Appropriate

After the patient is safely monitored by another method, perform a normal shutdown and restart if permitted by the clinical workflow.

Do not use repeated reboots as a substitute for identifying whether an external system is repopulating the previous patient.

Expected outcome: After restart, the monitor displays the appropriate unadmitted state or current patient information and remains synchronized. If the issue is resolved and correct patient association is verified end-to-end, troubleshooting can stop.

### 11. Test the Admit/Discharge Workflow Safely

Using an approved test workflow or facility-approved nonclinical method, verify that the monitor can clear patient information and accept the next patient association without retaining prior demographics.

Do not use real patient identifiers solely for testing unless authorized and clinically appropriate.

Expected outcome: The CARESCAPE B650 correctly transitions between patient states and does not retain or restore inappropriate prior-patient information.

### 12. Remove From Service or Escalate if Patient Association Remains Unreliable

If the monitor repeatedly retains previous patient data, cannot complete admission/discharge, or receives inconsistent demographics despite verified workflow and network connectivity, stop local troubleshooting.

Expected outcome: The monitor is removed from service when the problem appears device-specific, or the issue is escalated immediately to the appropriate monitoring, interface, network, or clinical-application support team when infrastructure is implicated.

## If the Problem Persists

If local workflow, bed/location configuration, accessible network connections, restart, and comparison with the central monitoring environment do not resolve the problem, common external bedside causes have been ruled out.

Remaining categories may include monitor configuration, central monitoring, patient-association services, network communication, interface processing, ADT workflow, or another service-level software problem. Do not assume the CARESCAPE B650 itself is defective if multiple monitors or systems show the same condition.

For a device-specific unresolved fault, remove the monitor from service, label it Out of Service, and send it for bench evaluation using appropriate GE Healthcare documentation and approved test methods. Infrastructure or integration problems should be escalated to the responsible qualified team.

After correction, verify the complete patient-association path, including discharge of the previous patient, admission of the correct patient, synchronization with applicable central systems, and absence of retained prior demographics before returning the monitor to service.

Knowing when to stop changing the bedside monitor and escalate a system-level patient-association problem is proper troubleshooting.

## Clinical Use Tip

Always confirm the patient identity at both the bedside monitor and the receiving central or clinical system before considering an admit/discharge problem resolved.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Patient-association problems require both technical troubleshooting and data-integrity awareness. Verify local workflow and connectivity first, confirm the complete monitoring path before blaming the monitor, escalate system-level faults appropriately, and document the final patient-association verification clearly.

That is successful troubleshooting.
