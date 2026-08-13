---
schemaVersion: 1
title: "GE Healthcare Carestation 750 Anesthesia Machine - Gas Module Not Recognized or Gas Measurement Unavailable"
issueTitle: "Gas Module Not Recognized or Gas Measurement Unavailable"
description: "Gas measurement is missing because of module seating, sampling components, power, moisture, configuration, connections, or a service-level module fault."
assetType: "Anesthesia Machine"
manufacturer: "GE Healthcare"
model: "Carestation 750"
slug: "ge-healthcare-carestation-750-gas-module-not-recognized-or-gas-measurement-unavailable"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Anesthesia staff reported that the Carestation 750 gas module was present but respiratory gas measurements were unavailable."
  cause: "Clinical Engineering found the sampling line obstructed by moisture."
  resolution: "The sampling line was replaced, gas measurements returned and remained stable, and the machine passed final checkout."
helpfulDetails:
  - "Module recognition status"
  - "Missing parameters"
  - "Sampling-line condition"
  - "Water-trap condition"
  - "Whether measurements are intermittent"
  - "Module seating"
  - "Startup behavior"
  - "Known-good module result"
  - "Known-good sample line result"
  - "Final gas-measurement verification"
  - "Final checkout result"
  - "Final device status"
---

## What This Guide Helps With
Gas measurement is missing because of module seating, sampling components, power, moisture, configuration, connections, or a service-level module fault.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Provide Alternate Monitoring
If required anesthetic-gas, CO2, or respiratory-gas monitoring is unavailable during patient care, provide appropriate alternate monitoring and follow clinical policy.

Do not troubleshoot the gas module while the patient depends on its measurements.

**Expected outcome:** Required patient monitoring continues independently of the affected gas module.

### 2. Confirm the Exact Failure
Determine whether the Carestation 750:

- Does not recognize the gas module
- Recognizes it but shows no gas values
- Shows intermittent measurements
- Reports sampling unavailable
- Loses only one measured parameter

Record the displayed status and whether the issue occurs at startup or during operation.

**Expected outcome:** The failure mode is clearly identified and reproducible.

### 3. Verify Machine Power and Normal Startup
Confirm the anesthesia machine is operating on stable AC power and has completed normal startup as far as possible.

Power-cycle the system only when clinically safe and consistent with approved procedures.

**Expected outcome:** The machine starts normally and the gas measurement problem is reassessed. If normal module recognition returns and remains stable through checkout, troubleshooting can stop.

### 4. Inspect and Reseat the Gas Module
If the module is intended to be removable by trained technical personnel, inspect it for incomplete insertion or visible physical damage.

Remove and reinstall it according to approved handling procedures, ensuring it is fully seated.

**Expected outcome:** The module is fully seated and recognized. If gas values return and remain stable, proceed to final verification.

### 5. Inspect Sampling Tubing and Patient-Side Accessories
Check the sample line, airway adapter, filters, and related accessories for:

- Disconnection
- Occlusion
- Kinking
- Cracking
- Moisture
- Incorrect installation

Replace questionable disposable components with compatible known-good items.

**Expected outcome:** The sampling path is open, dry, intact, and correctly connected. If gas measurement returns, the external sampling problem is resolved.

### 6. Check the Water Trap or Moisture-Management Components
Inspect accessible moisture-management components for fullness, contamination, incorrect installation, or damage.

Service or replace them only according to approved procedures.

**Expected outcome:** The moisture-management pathway is properly installed and not obstructing sampling. Restored gas measurement after correction resolves the issue.

### 7. Verify Module and System Configuration
Confirm the installed gas module is compatible with the Carestation 750 configuration and that no obvious user-accessible configuration setting has disabled the expected measurement display.

Do not alter restricted configuration settings.

**Expected outcome:** The module and system configuration are appropriate. If correcting an approved configuration setting restores measurement, verify operation and stop troubleshooting.

### 8. Compare With a Known-Good Module When Approved
If the module is field-swappable and a compatible known-good module is available, perform a controlled substitution.

Do not swap modules if manufacturer procedures prohibit it or if calibration/service requirements cannot be met.

**Expected outcome:** If the known-good module is recognized and measures normally, the original module should be removed for evaluation. If the failure remains, the problem may be system-side.

### 9. Verify Gas Measurements
Once recognition is restored, verify appropriate gas values using a controlled test setup.

Confirm sampling, waveform response where applicable, alarms, and stability before return to service.

**Expected outcome:** Gas measurements are available and stable and required checkout functions pass. Troubleshooting can stop.

### 10. Escalate Persistent Module or Measurement Failure
If the module remains unrecognized or gas measurements remain unavailable after seating, sampling, moisture, and approved substitution checks, stop troubleshooting.

**Expected outcome:** The machine or affected module is removed from service and routed for qualified evaluation.

## If the Problem Persists
Common external causes have been ruled out. Remaining categories may include module electronics, internal communications, system interfaces, sampling pump or pneumatic components, configuration data, or another service-level failure.

The affected Carestation 750 or gas module should be:

- Removed from service as appropriate
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired or configured only by qualified personnel

Required gas measurements and communication should be verified before return to clinical use.

Knowing when missing gas monitoring requires alternate monitoring and service escalation is proper troubleshooting.

## Clinical Use Tip
If gas monitoring required for the case is unavailable, establish verified alternate monitoring before investigating the anesthesia machine.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Missing gas measurements can originate outside the module itself. Verify seating, sampling, moisture handling, accessories, and permitted configuration first, then confirm measurement performance before deciding the failure requires module or system repair.

That is successful troubleshooting.
