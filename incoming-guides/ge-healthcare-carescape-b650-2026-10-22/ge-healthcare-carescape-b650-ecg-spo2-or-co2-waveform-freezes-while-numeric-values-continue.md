---
schemaVersion: 1
title: "GE Healthcare CARESCAPE B650 Patient Monitor - ECG, SpO2, or CO2 Waveform Freezes While Numeric Values Continue"
issueTitle: "ECG, SpO2, or CO2 Waveform Freezes While Numeric Values Continue"
description: "Troubleshoot a frozen ECG, SpO2, or CO2 waveform when numeric values continue, including accessories, display behavior, module connections, settings, and communication issues."
assetType: "Patient Monitor"
manufacturer: "GE Healthcare"
model: "CARESCAPE B650"
slug: "ge-healthcare-carescape-b650-ecg-spo2-or-co2-waveform-freezes-while-numeric-values-continue"
dateAdded: "2026-10-22"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the ECG waveform on the CARESCAPE B650 repeatedly froze while the displayed heart-rate value continued updating."
  cause: "Clinical Engineering found the ECG patient cable connection was intermittent and the waveform froze when the connector was disturbed."
  resolution: "Replaced the affected ECG cable with a verified compatible cable and confirmed stable ECG waveform, numeric response, and alarm operation using an approved simulator."
helpfulDetails:
  - "Parameter affected: ECG, SpO2, or CO2"
  - "Whether numeric values continued changing"
  - "Whether other waveforms remained normal"
  - "Patient cable, sensor, or sampling-line condition"
  - "Known-good accessory substitution results"
  - "Parameter-module status"
  - "Whether the symptom followed a specific module or accessory"
  - "Display and waveform configuration observed"
  - "Results before and after restart"
  - "Simulator or test-equipment results"
  - "Whether the fault was intermittent or continuous"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoot a frozen ECG, SpO2, or CO2 waveform when numeric values continue, including accessories, display behavior, module connections, settings, and communication issues.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Verify Monitoring Continuity

Do not troubleshoot an unreliable patient-monitoring function while a patient depends on it. If waveform information is clinically required, move monitoring to another verified monitor or provide an appropriate alternate monitoring method before continuing.

Confirm whether the waveform is actually frozen, intermittently updating, or simply absent. Determine which parameter is affected and whether alarms and numeric values continue changing.

Expected outcome: The patient is safely monitored by a reliable method, and the exact affected parameter and symptom are confirmed. If the reported condition cannot be reproduced and normal waveform operation is verified, troubleshooting can stop.

### 2. Confirm Whether the Problem Affects One Parameter or the Entire Display

Observe ECG, SpO2, CO2, and any other available waveforms. Compare waveform movement with numeric updates, alarm messages, and other screen elements such as the clock or menus.

If only one waveform is frozen, focus on that parameter's cable, sensor, module, and configuration. If several waveforms freeze together while the interface remains responsive, consider display processing or monitor communication rather than multiple simultaneous accessory failures.

Expected outcome: The issue is isolated to one parameter or identified as a broader monitor display problem. If normal waveform updates resume and remain stable, troubleshooting can stop.

### 3. Inspect the Patient Cable, Sensor, and Sampling Accessories

For the affected parameter, inspect externally accessible accessories for damage, contamination, loose connections, bent contacts, strain, or improper installation.

For ECG, inspect the patient cable and lead connections. For SpO2, inspect the sensor and extension cable if used. For CO2, inspect the sampling line, airway adapter, water trap, or other approved external sampling components applicable to the installed configuration.

Expected outcome: Accessories are securely connected, correctly installed, and free of obvious damage or blockage. If correcting an accessory connection restores a continuously updating waveform, troubleshooting can stop.

### 4. Reseat External Parameter Connections

Disconnect and reconnect the affected patient cable, sensor cable, sampling connection, or external module connection according to normal Clinical Engineering handling practices.

Do not force connectors or repeatedly reseat damaged components.

Expected outcome: The monitor recognizes the parameter and displays a continuously updating waveform. If the waveform remains stable during observation, troubleshooting can stop.

### 5. Substitute a Known-Good Accessory When Appropriate

Use a compatible known-good ECG cable, SpO2 sensor/cable, CO2 sampling accessory, or other approved external component to separate an accessory problem from a monitor or module problem.

Do not substitute accessories whose compatibility has not been established.

Expected outcome: A known-good accessory either restores normal waveform operation or confirms that the symptom remains with the monitor/module. If substitution resolves the issue, replace or remove the defective accessory from service and troubleshooting can stop.

### 6. Check Parameter Module and Module-Rack Connections

If the affected measurement is provided through an external or removable parameter module, verify that the module is fully seated and recognized by the CARESCAPE B650.

Inspect accessible module connectors and mounting points for contamination, damage, or incomplete engagement. Do not disassemble the module or monitor.

Expected outcome: The installed module is securely connected and recognized without communication or module-status warnings. If reseating the module restores stable waveform operation, troubleshooting can stop after verification.

### 7. Verify Waveform Display and Parameter Settings

Confirm that the affected waveform is enabled and assigned to an active waveform area. Verify that display configuration, sweep behavior, waveform source selection, and parameter settings have not been inadvertently changed.

Avoid unauthorized configuration changes. Document any setting that must be corrected.

Expected outcome: The waveform is configured for active display and updates normally. If correcting a configuration issue restores proper operation, troubleshooting can stop.

### 8. Check for a Display-Only Freeze

Compare the monitor's numerical values, alarm indications, menus, clock, and other waveforms while the affected waveform appears frozen.

If the numeric value continues changing appropriately but the waveform remains visually stationary, document this distinction because it may indicate a display or data-presentation issue rather than complete loss of parameter acquisition.

Expected outcome: The technician determines whether acquisition is continuing while only waveform presentation is affected. If the display returns to normal operation and remains stable, troubleshooting can stop.

### 9. Restart the Monitor Under Controlled Conditions

Once the patient is no longer dependent on the affected monitor, perform a normal shutdown and restart using approved operating controls.

Do not interrupt power during startup or perform repeated uncontrolled power cycles.

Expected outcome: The CARESCAPE B650 completes startup normally and all connected parameters display continuously updating waveforms. If operation remains stable after restart, troubleshooting can stop.

### 10. Perform Functional Verification

Using appropriate approved simulators or test equipment, verify the affected parameter and observe the waveform for an adequate period to detect recurrence.

Confirm that numeric values change with the simulated input, the waveform tracks the input, and associated alarms and parameter indications function appropriately.

Expected outcome: Waveforms, numeric values, and applicable alarms respond consistently to known test inputs. If all functions are normal and the fault does not recur, the monitor may proceed through required return-to-service checks.

### 11. Remove From Service if the Waveform Still Freezes

If the waveform freezes again despite verified accessories, connections, module seating, configuration, and restart, do not return the monitor to clinical use based only on continuing numeric values.

Expected outcome: The unresolved monitor is removed from service, labeled Out of Service, and referred for bench evaluation or qualified service.

## If the Problem Persists

If the waveform continues freezing after external accessories, parameter connections, module seating, settings, and normal restart have been verified, common external causes have been ruled out.

Possible remaining categories include parameter-module communication, display processing, software behavior, internal data communication, or another service-level monitor fault. The equipment should be removed from service, labeled Out of Service, and sent for repair or bench evaluation.

Further evaluation should use appropriate GE Healthcare service documentation and approved test equipment. Internal repair, software servicing, or configuration changes should be performed only by qualified personnel.

After repair, complete applicable functional testing, alarm verification, parameter testing, and any required electrical-safety or return-to-service testing before releasing the monitor.

Knowing when to stop external troubleshooting and escalate an intermittent monitoring fault is proper troubleshooting.

## Clinical Use Tip

A changing numeric value does not make a frozen waveform acceptable when clinical decisions depend on waveform morphology or continuous visual monitoring.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Start by protecting the patient, then separate accessory, parameter, display, and monitor causes logically. Verify the failure with known inputs before assuming an internal fault, escalate persistent waveform freezes appropriately, and document exactly what was found and verified.

That is successful troubleshooting.
