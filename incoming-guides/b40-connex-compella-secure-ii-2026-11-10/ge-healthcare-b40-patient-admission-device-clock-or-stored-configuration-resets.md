---
schemaVersion: 1
title: "GE Healthcare B40 Patient Monitor - Patient Admission, Device Clock, or Stored Configuration Resets"
issueTitle: "Patient Admission, Device Clock, or Stored Configuration Resets"
description: "Troubleshoot patient admission, clock, or configuration resets caused by workflow, power interruptions, synchronization, or settings retention problems."
assetType: "Patient Monitor"
manufacturer: "GE Healthcare"
model: "B40"
slug: "ge-healthcare-b40-patient-admission-device-clock-or-stored-configuration-resets"
dateAdded: "2026-11-10"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the B40 displayed the incorrect date and time after being restarted."
  cause: "Clinical Engineering found that the device clock had been set incorrectly and remained at the incorrect time after normal startup."
  resolution: "Corrected the clock through the authorized configuration procedure and verified accurate time retention after a controlled shutdown and restart."
helpfulDetails:
  - "Specific information that resets"
  - "Original and changed values"
  - "Failure timing"
  - "Shutdown and startup conditions"
  - "AC and battery status"
  - "Device clock comparison"
  - "Expected retention behavior"
  - "Software and configuration information"
  - "Network synchronization status"
  - "Known-good monitor comparison"
  - "Final retention and alarm verification"
---

## What This Guide Helps With

Troubleshoot patient admission, clock, or configuration resets caused by workflow, power interruptions, synchronization, or settings retention problems.

## Step-by-Step Troubleshooting

### 1. Ensure Patient Safety and Monitoring Continuity
- Determine whether the reset affects patient identification, alarm limits, monitoring configuration, or clinical documentation.
- If patient association or essential monitoring settings cannot be trusted, arrange another verified monitor.
- Notify clinical staff of any potential patient data or alarm configuration discrepancy.
- Do not conduct reset or power-cycle testing while the patient depends on the affected monitor.

Expected outcome: Patient monitoring, alarm settings, and identification remain reliable through a verified alternate device.

### 2. Identify Exactly What Resets
- Determine whether the problem involves patient admission information, the displayed date and time, stored settings, or multiple items.
- Record the original and changed values.
- Ask whether the reset occurs after shutdown, AC disconnection, battery depletion, or network reconnection.
- Determine whether the behavior is repeatable.

Expected outcome: The affected information and conditions causing the reset are identified.

### 3. Verify Normal Patient Discharge and Admission Behavior
- Review the approved clinical workflow for patient discharge and admission.
- Determine whether the reported loss of patient information followed an intentional discharge or new admission.
- Confirm whether the installed configuration retains or clears specific information during those operations.
- Do not treat expected workflow behavior as a hardware fault.

Expected outcome: Normal patient workflow behavior is distinguished from unexpected information loss.

### 4. Inspect AC Power and Battery Status
- Verify that the monitor receives stable AC power.
- Inspect the external power cord and connector.
- Check displayed battery status and charging indications.
- Review whether unexpected shutdowns or battery depletion occurred before the reset.

Expected outcome: No external power condition explains the loss of information.

### 5. Verify the Device Clock
- Record the displayed date and time.
- Compare them with an approved facility time reference.
- Determine whether the monitor receives time information from an external system, if supported and configured.
- Check whether the clock changes after normal startup or network reconnection.
- Do not alter protected time synchronization settings without authorization.

Expected outcome: The clock behavior and any supported synchronization source are understood.

### 6. Review Authorized Configuration Retention
- Identify which settings are expected to persist across shutdowns.
- Distinguish patient-specific settings from authorized default configurations.
- Review accessible configuration information without changing restricted settings.
- Compare with a functioning B40 of the same software and configuration when available.

Expected outcome: Expected configuration retention is established for the installed monitor.

### 7. Perform a Controlled Retention Test
- Remove the monitor from patient use.
- Record the approved test settings and current clock information.
- Use only authorized, nonclinical test information.
- Perform a normal shutdown and restart according to manufacturer procedures.
- Compare retained values with the documented baseline.

Expected outcome: Required information persists or resets only as specified by the manufacturer.

### 8. Evaluate Network or External System Influence
- If the monitor uses an approved network or integration connection, determine whether the reset coincides with synchronization or patient assignment changes.
- Coordinate with clinical IT or the integration team.
- Verify whether an external system is providing time, patient association, or configuration information.
- Do not disconnect protected network services or change interface settings without approval.

Expected outcome: External synchronization and integration effects are identified or ruled out.

### 9. Compare With a Known-Good Monitor
- Use a B40 with matching software and approved configuration.
- Perform the same nonclinical retention test.
- Compare startup, clock, and settings behavior.
- Record any differences without copying restricted configuration information.

Expected outcome: The comparison helps determine whether the problem is device-specific or associated with the configured workflow.

### 10. Complete Final Retention and Functional Verification
- Verify clock accuracy and expected retention after the approved test sequence.
- Confirm that required default settings are correct.
- Verify patient admission workflow using approved nonclinical test information.
- Test monitoring and applicable alarms.
- Confirm correct network association where required.

Expected outcome: The monitor retains required information and operates according to its approved configuration. If all verification passes, document the correction and stop troubleshooting.

## If the Problem Persists

Normal admission workflow, external power, battery status, clock synchronization, and accessible configuration have been evaluated. Remaining possibilities include internal settings retention faults, backup power components, software corruption, nonvolatile storage problems, or integration configuration issues.

Remove the B40 from service, label it Out of Service, and arrange repair or bench evaluation. Qualified personnel should use manufacturer documentation and approved diagnostic equipment. Any internal repair, software restoration, or protected configuration change must be performed only by qualified personnel.

Before returning the monitor to service, verify clock behavior, required configuration retention, patient admission workflow, monitoring functions, and applicable alarms. Recognizing when external troubleshooting is complete is proper troubleshooting.

## Clinical Use Tip

After a configuration or admission reset, verify patient identity and alarm limits before clinical use. A monitor may display valid measurements while retaining an incorrect patient association or alarm configuration.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Unexpected resets can affect patient identification, alarm configuration, and clinical records even when measurements appear normal. Protect patient safety, verify expected workflow and power behavior, evaluate synchronization and retention, and escalate persistent faults. Clear CCR documentation and final functional verification complete the troubleshooting process.

That is successful troubleshooting.
