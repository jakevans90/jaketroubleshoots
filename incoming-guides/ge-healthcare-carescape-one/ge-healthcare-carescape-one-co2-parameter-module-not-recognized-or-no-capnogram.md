---
schemaVersion: 1
title: "GE Healthcare CARESCAPE ONE Patient Monitor - CO2 Parameter Module Not Recognized or No Capnogram"
issueTitle: "CO2 Parameter Module Not Recognized or No Capnogram"
description: "Troubleshoots absent CO2 module recognition or capnogram caused by module seating, sampling accessories, blockage, moisture, connections, or configuration."
assetType: "Patient Monitor"
manufacturer: "GE Healthcare"
model: "CARESCAPE ONE"
slug: "ge-healthcare-carescape-one-co2-parameter-module-not-recognized-or-no-capnogram"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory staff reported the CARESCAPE ONE displayed the CO2 parameter but no capnogram was present."
  cause: "Clinical Engineering found the external sampling line was occluded with moisture."
  resolution: "The compromised sampling line was replaced with an approved compatible line, and stable capnogram, numeric CO2 response, and alarms were verified."
helpfulDetails:
  - "Whether the CO2 module was recognized."
  - "Presence or absence of capnogram."
  - "Exact displayed message."
  - "Sampling line condition."
  - "Moisture or blockage found."
  - "Known-good sampling line result."
  - "Known-good module result."
  - "Module seating and contact condition."
  - "CO2 test equipment results."
  - "Final waveform, numeric, and alarm status."
---
## What This Guide Helps With

Troubleshoots absent CO2 module recognition or capnogram caused by module seating, sampling accessories, blockage, moisture, connections, or configuration.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Ventilation Monitoring
If capnography is clinically required and unavailable, establish CO2 or ventilation monitoring using another verified device before troubleshooting.

Do not troubleshoot an unreliable capnography path while a patient depends on it for ventilation monitoring.

**Expected outcome:** Required patient monitoring continues while the CARESCAPE ONE CO2 problem is evaluated.

### 2. Confirm the Exact CO2 Complaint
Determine whether:
- The CO2 parameter module is not recognized.
- The module is recognized but no waveform appears.
- A waveform appears intermittently.
- Sampling appears blocked.
- Numeric CO2 is absent despite a waveform.
- The issue follows transport, module exchange, sampling line replacement, or contamination.

**Expected outcome:** The problem is separated into module-recognition versus gas-sampling or measurement failure.

### 3. Reseat the CO2 Parameter Module
With the device off patient dependence, remove and reinstall the CO2 parameter module using its normal external interface.

Inspect for incomplete seating or obvious mechanical obstruction.

**Expected outcome:** The module is recognized and initializes normally. If recognition returns and capnography functions correctly, complete final verification and stop troubleshooting.

### 4. Inspect the Module Interface
Inspect accessible contacts and mating surfaces for debris, moisture, cleaning residue, physical damage, or bent contacts.

Do not open the module or monitor enclosure.

**Expected outcome:** The external module interface is clean, dry, undamaged, and fully seated.

### 5. Inspect the Sampling Line and Patient Interface
For a sampling-based CO2 configuration, inspect the external sampling path for:
- Kinks.
- Occlusion.
- Moisture.
- Loose connections.
- Damaged tubing.
- Improperly connected airway adapter or sampling component.
- Contaminated disposable components.

Replace compromised consumables with approved compatible items.

**Expected outcome:** The sampling path is open and properly connected. If the capnogram returns, verify stability and stop troubleshooting.

### 6. Substitute Known-Good Sampling Accessories
Install a known-good compatible sampling line and associated disposable accessories.

Use only accessories appropriate to the installed CO2 technology.

**Expected outcome:** A stable capnogram appears if the original consumable was the cause. Remove the defective or obstructed accessory from service.

### 7. Compare With a Known-Good Compatible CO2 Module
If the module itself is not recognized, install a known-good compatible CO2 parameter module when available.

If the known-good module works, the original module should be removed from service. If neither module is recognized, investigate the CARESCAPE ONE interface or configuration.

**Expected outcome:** The failure is isolated to the CO2 module or the monitor interface.

### 8. Verify Accessible CO2 Configuration
Confirm the expected CO2 parameter is enabled and selected through approved user-accessible controls for the intended configuration.

Do not change restricted configuration or calibration data without approved service procedures.

**Expected outcome:** The CO2 monitoring configuration is appropriate. If an accessible configuration issue caused the missing display, correct it and verify operation.

### 9. Perform Functional Verification
Using an appropriate approved CO2 simulator, test gas, or manufacturer-supported method, verify:
- Module recognition.
- Capnogram display.
- Numeric CO2 response.
- Respiratory rate when applicable.
- CO2 alarm annunciation.

Use manufacturer criteria for any quantitative evaluation.

**Expected outcome:** CO2 monitoring operates consistently and alarms function correctly. Troubleshooting is complete.

### 10. Escalate Persistent CO2 Failure
If the module remains unrecognized or no capnogram is produced with known-good module and sampling accessories, stop external troubleshooting.

**Expected outcome:** The affected module or monitor is removed from service and escalated appropriately.

## If the Problem Persists

Common external causes have been ruled out. The remaining problem may involve the CO2 module, sampling pump, internal sensing system, module interface, communication path, software, or configuration.

The affected equipment should be:
- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved CO2 test equipment.
- Repaired, calibrated, or configured only by qualified personnel.

After service, verify CO2 waveform, numeric response, alarms, module recognition, and overall CARESCAPE ONE operation before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

When capnography is required for airway or ventilation monitoring, provide an alternate verified CO2 monitoring path before disconnecting modules or sampling lines.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->
## Final Thought

CO2 complaints must be separated into module recognition and gas-sampling problems before internal failure is assumed. Verify the external module interface and complete sampling path, maintain alternate ventilation monitoring, and escalate unresolved faults appropriately.

That is successful troubleshooting.
