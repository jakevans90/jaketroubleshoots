---
schemaVersion: 1
title: "Philips IntelliVue MX850 Patient Monitor - CO2 Module Not Recognized or No Capnogram"
issueTitle: "CO2 Module Not Recognized or No Capnogram"
description: "Troubleshoots missing CO2 module recognition or capnogram caused by module seating, sampling accessories, airway connections, blockage, moisture, configuration, or communication problems."
assetType: "Patient Monitor"
manufacturer: "Philips"
model: "IntelliVue MX850"
slug: "philips-intellivue-mx850-co2-module-not-recognized-or-no-capnogram"
dateAdded: "2026-08-14"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported the MX850 displayed no capnogram even though the CO2 module appeared connected."
  cause: "Clinical Engineering found the disposable sampling line was obstructed with moisture."
  resolution: "Clinical Engineering replaced the approved sampling line and verified a stable capnogram, CO2 numeric display, and alarm operation before return to service."
helpfulDetails:
  - "Whether the module was recognized"
  - "Exact displayed message"
  - "Sampling line or adapter type"
  - "Moisture or blockage observed"
  - "Module seating and connector condition"
  - "Known-good accessory results"
  - "Known-good module results"
  - "Capnogram behavior"
  - "Alarm verification"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots missing CO2 module recognition or capnogram caused by module seating, sampling accessories, airway connections, blockage, moisture, configuration, or communication problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Required Ventilation Monitoring

If capnography is clinically required and the MX850 cannot provide a reliable CO2 waveform or value, use another verified monitoring method before troubleshooting.

**Expected outcome:** Required ventilation monitoring remains available.

### 2. Confirm the Exact CO2 Complaint

Determine whether:

- The CO2 module is not recognized
- The module is recognized but no capnogram appears
- Numeric values are absent
- The waveform is intermittent
- The problem began after changing sampling accessories
- A specific displayed message is present

**Expected outcome:** The problem is separated into module recognition versus gas-sampling failure.

### 3. Inspect and Reseat the CO2 Module

If a removable CO2 module is used, confirm it is fully seated in the appropriate measurement interface.

Inspect accessible connectors and housing for damage or contamination.

**Expected outcome:** The module is recognized normally. If recognition is restored, continue to sampling-path verification.

### 4. Inspect the Sampling Line or Airway Adapter

For the installed CO2 technology, inspect accessible sampling accessories for:

- Loose connections
- Kinks
- Blockage
- Moisture
- Cracks
- Incorrect assembly
- Contamination

Replace disposable sampling components when indicated rather than attempting to clear contaminated patient-use components.

**Expected outcome:** The sampling or optical path is open, correctly assembled, and securely connected.

### 5. Check the Patient Interface

Verify that the airway adapter, cannula, or sampling connection is positioned correctly for the intended clinical use.

Patient disconnection or poor placement can produce no waveform even when the monitor is functioning normally.

**Expected outcome:** Exhaled gas can reach the CO2 measurement path and a capnogram appears.

### 6. Substitute Known-Good External Accessories

Use approved compatible known-good sampling components, adapter, or connection accessories as appropriate.

**Expected outcome:** A normal capnogram with known-good accessories identifies an external sampling component as the cause.

### 7. Compare with a Known-Good Module When Available

If module recognition remains in question, install a compatible known-good CO2 module in the same approved interface.

Alternatively, test the suspect module on another compatible monitor when facility procedures permit.

**Expected outcome:** The failure follows either the module or the monitor/interface path.

### 8. Check Configuration and Measurement Availability

Confirm the appropriate CO2 measurement channel is available in the current configuration and that no recent equipment exchange or approved configuration change preceded the complaint.

Do not enter restricted service menus.

**Expected outcome:** No obvious configuration issue prevents CO2 measurement.

### 9. Perform Functional Verification

Using appropriate approved test equipment or a controlled test source, verify:

- Module recognition
- Stable capnogram
- CO2 numeric display
- No intermittent dropout
- Relevant alarms
- Stable operation with normal external cable or module handling

**Expected outcome:** CO2 monitoring is stable and reliable. Troubleshooting can stop.

### 10. Escalate Persistent CO2 Failure

If known-good sampling accessories and a known-good module or interface comparison do not resolve the problem, stop external troubleshooting.

**Expected outcome:** The affected module or monitor is removed from clinical service for service-level evaluation.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities include the CO2 module, module communication path, sampling pump or internal gas path for applicable technology, configuration, or other service-level electronics.

The affected equipment should be:

- Removed from service when reliable capnography is required
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate Philips documentation and approved test equipment
- Repaired or configured only by qualified personnel

Perform full CO2 and alarm verification before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Loss of a capnogram can represent either equipment failure or loss of the patient sampling connection; verify the complete monitoring path promptly.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Separate recognition faults from sampling-path problems, inspect the external gas path before assuming module failure, verify the complete measurement and alarm function, and escalate unresolved faults appropriately.

That is successful troubleshooting.
