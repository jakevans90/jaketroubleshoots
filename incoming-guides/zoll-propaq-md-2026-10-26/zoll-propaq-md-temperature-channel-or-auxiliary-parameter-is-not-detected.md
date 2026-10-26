---
schemaVersion: 1
title: "ZOLL Propaq MD Defibrillator - Temperature Channel or Auxiliary Parameter Is Not Detected"
issueTitle: "Temperature Channel or Auxiliary Parameter Is Not Detected"
description: "Temperature or auxiliary parameter input is missing because of accessories, connectors, compatibility, configuration, patient connections, or parameter-module faults."
assetType: "Defibrillator"
manufacturer: "ZOLL"
model: "Propaq MD"
slug: "zoll-propaq-md-temperature-channel-or-auxiliary-parameter-is-not-detected"
dateAdded: "2026-10-26"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Propaq MD would not detect the connected temperature probe."
  cause: "Clinical Engineering found the reusable temperature interface cable failed to pass the signal while the probe and monitor channel tested normally with known-good accessories."
  resolution: "Replaced the defective interface cable, verified stable temperature detection with an approved test source, completed functional testing, and returned the unit to service."
helpfulDetails:
  - "Exact parameter affected"
  - "Whether the parameter was absent or intermittent"
  - "Sensor or probe type"
  - "Cable and adapter condition"
  - "Connector condition"
  - "Known-good accessory substitution results"
  - "Whether the fault followed the accessory"
  - "Configuration observed"
  - "Test-source results"
  - "Behavior after restart"
  - "Results before and after correction"
  - "Final device status"
---

## What This Guide Helps With

Temperature or auxiliary parameter input is missing because of accessories, connectors, compatibility, configuration, patient connections, or parameter-module faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Required Monitoring

If temperature or another auxiliary parameter is clinically required and the Propaq MD cannot provide it reliably, use another verified monitoring method before troubleshooting.

Do not repeatedly disconnect required patient monitoring while a patient depends on the measurement.

**Expected outcome:** Required monitoring continues through a dependable alternate method while the affected channel is evaluated.

### 2. Confirm Which Parameter Is Not Detected

Identify exactly what is missing and whether the device:

- Shows no parameter at all
- Recognizes the accessory but displays no value
- Displays an intermittent value
- Indicates an unsupported or disconnected accessory
- Loses the parameter when the cable is moved
- Fails only after startup, transport, or accessory exchange

**Expected outcome:** The affected channel and failure behavior are clearly established.

### 3. Verify the Parameter Is Expected on the Device Configuration

Confirm that the specific Propaq MD configuration is equipped and intended to support the reported temperature or auxiliary parameter.

Do not assume that every unit in a fleet has identical hardware or enabled options.

Compare with asset records, approved configuration information, or another known-good unit of the same configuration when available.

**Expected outcome:** The reported parameter is confirmed as supported on the affected device.

If the parameter is not part of the unit's approved configuration, document the finding rather than treating it as a hardware failure.

### 4. Inspect the Sensor, Probe, and Patient Cable

Inspect the complete external accessory chain for:

- Cracked sensor housings
- Cut or pinched cables
- Bent connector contacts
- Contamination
- Fluid intrusion
- Damaged strain relief
- Loose adapters
- Incompatible accessories

Follow the connection path from the patient-side sensor to the Propaq MD.

**Expected outcome:** All accessories are compatible, intact, clean, and connected correctly.

If a visibly damaged accessory is found, remove it from service and substitute a verified compatible accessory.

### 5. Reseat All Connections

Disconnect and reconnect the applicable sensor, adapter, or parameter cable using normal accessible connections.

Ensure connectors are fully seated without forcing them.

Intermittent or incomplete connector engagement can prevent parameter recognition even when the accessory appears connected.

**Expected outcome:** The parameter is detected immediately and remains present after reconnection.

If reseating the connection restores reliable operation and repeated testing remains normal, troubleshooting can stop after final verification.

### 6. Substitute a Known-Good Sensor or Probe

Use a known-good compatible temperature probe or other applicable accessory.

Change only one component at a time where possible.

**Expected outcome:** The parameter is detected and displays normally with the known-good accessory.

If substitution resolves the issue, remove the defective accessory from service and document the finding.

### 7. Substitute the Patient or Interface Cable

If the measurement uses a separate patient cable, adapter, or interface cable, substitute a known-good compatible one.

A cable can appear physically intact while failing electrically.

**Expected outcome:** The parameter is recognized consistently with the known-good cable or adapter.

If the issue follows the cable, replace the defective accessory and complete final verification.

### 8. Test the Suspect Accessory on Another Compatible Device

When available, connect the suspect sensor or cable to another compatible verified Propaq MD or approved test setup.

This helps determine whether the fault follows the accessory.

**Expected outcome:** The accessory either functions normally on the second system or reproduces the failure.

If the failure follows the accessory, remove that accessory from service. If the accessory works normally elsewhere, continue evaluating the original device.

### 9. Inspect the Device Connector

Visually inspect the applicable external parameter connector on the Propaq MD.

Look for:

- Bent contacts
- Foreign material
- Corrosion
- Loose connector housing
- Physical damage
- Evidence of forced insertion

Do not insert tools into contacts or attempt internal connector repair during external troubleshooting.

**Expected outcome:** The connector is clean, undamaged, and mechanically secure.

Visible connector damage requires removal from service and escalation.

### 10. Check User-Accessible Parameter Configuration

Verify that the parameter display or measurement has not been intentionally disabled, hidden, or changed through normal approved configuration.

Do not enter restricted service menus or make unauthorized configuration changes.

Compare settings with a known-good unit when appropriate.

**Expected outcome:** The supported parameter is enabled and available through the normal approved configuration.

If correcting an authorized user-accessible setting restores the measurement, proceed to final verification.

### 11. Verify Measurement With an Approved Test Source

Use an appropriate approved simulator or test source when available for the affected parameter.

This separates patient-side sensor conditions from the Propaq MD measurement channel.

**Expected outcome:** The device recognizes the test input and displays the expected parameter response according to approved test criteria.

If the unit performs correctly with the approved test source, the device channel is likely functional and the external accessory chain should be re-evaluated.

### 12. Perform Final Functional Verification

After correction, verify:

- Parameter detection is immediate
- The displayed value remains stable
- Cable movement does not cause dropout
- The parameter remains present after restart if applicable
- Other monitoring functions remain normal
- No connector damage is present

Complete required return-to-service testing.

**Expected outcome:** The temperature or auxiliary parameter remains reliably detected and the original complaint is resolved.

If all verification passes, troubleshooting can stop.

### 13. Escalate Persistent Channel Failure

If a known-good accessory and approved test source are not detected despite proper configuration and an undamaged external connector, remove the device from service.

**Expected outcome:** A suspected internal measurement-channel fault is routed for qualified evaluation rather than further external troubleshooting.

## If the Problem Persists

Common external causes such as accessory failure, incompatible probes, damaged cables, incomplete connections, configuration, and external connector condition have been ruled out.

The remaining problem may involve the parameter input circuitry, internal connector assembly, configuration data, or other service-level hardware.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Following repair, verify the affected parameter using an approved test source and complete all applicable defibrillator return-to-service checks.

Knowing when external accessory isolation is complete and internal evaluation is required is proper troubleshooting.

## Clinical Use Tip

If the missing parameter is clinically necessary, establish an alternate verified monitoring method before disconnecting or substituting accessories.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Start with continuity of monitoring, verify that the parameter is actually supported, isolate probes, cables, connectors, and configuration before assuming an internal channel failure, and escalate only after external causes have been systematically ruled out.

That is successful troubleshooting.
