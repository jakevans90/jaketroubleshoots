---
schemaVersion: 1
title: "Philips IntelliVue MX750 Patient Monitor - CO2 Module Not Recognized or No Capnogram"
issueTitle: "CO2 Module Not Recognized or No Capnogram"
description: "Troubleshoots missing CO2 module recognition or capnogram caused by module seating, sampling accessories, airway connections, blockage, moisture, or configuration."
assetType: "Patient Monitor"
manufacturer: "Philips"
model: "IntelliVue MX750"
slug: "philips-intellivue-mx750-co2-module-not-recognized-or-no-capnogram"
dateAdded: "2026-08-14"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the IntelliVue MX750 recognized the CO2 module but displayed no capnogram."
  cause: "Clinical Engineering found the sidestream sampling line obstructed by moisture."
  resolution: "Clinical Engineering replaced the affected sampling line and verified a stable capnogram, CO2 measurement, respiratory-rate display, and alarm response."
helpfulDetails:
  - "Whether the module was recognized"
  - "Whether any capnogram was present"
  - "Sampling-line condition"
  - "Moisture or blockage observed"
  - "Airway adapter condition"
  - "Known-good accessory result"
  - "Known-good module comparison"
  - "Measurement source observed"
  - "Functional test result"
  - "Final alarm and monitoring status"
---

## What This Guide Helps With
Troubleshoots missing CO2 module recognition or capnogram caused by module seating, sampling accessories, airway connections, blockage, moisture, or configuration.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Required Ventilation Monitoring
If capnography is clinically required and the MX750 cannot provide a reliable CO2 waveform or measurement, establish another verified method before troubleshooting.

**Expected outcome:** Required ventilation monitoring continues without depending on the affected CO2 channel.

### 2. Confirm Whether the Problem Is Recognition or Sampling
Determine whether the CO2 module is completely absent from the monitor, recognized but showing no waveform, or producing an intermittent or poor-quality capnogram.

**Expected outcome:** The problem is narrowed to module recognition, sampling-path performance, or patient connection.

### 3. Inspect and Reseat the CO2 Module
If an external measurement module is used, inspect it for proper seating, contamination, connector damage, or incomplete insertion. Remove and reinstall it securely while the device is not being relied upon clinically.

**Expected outcome:** The module is recognized and remains available. If recognition returns consistently, proceed with functional verification.

### 4. Inspect Sampling Accessories
For sidestream configurations, inspect the sampling line, airway adapter, water-management components, and connections for kinks, blockage, liquid contamination, loose fittings, or visible damage. For other approved configurations, inspect the corresponding external airway accessories.

**Expected outcome:** The sampling path is open, dry as required, and securely connected. If replacing a blocked or contaminated disposable restores the capnogram, continue to final verification.

### 5. Verify the Patient Connection
Check that the airway adapter or sampling connection is placed correctly in the breathing circuit and that connections are not loose or bypassing exhaled gas.

**Expected outcome:** Exhaled gas reaches the CO2 measurement path and a waveform is obtained.

### 6. Substitute Known-Good Compatible Accessories
Use known-good approved sampling components or airway accessories to determine whether the failure follows a disposable or cable.

**Expected outcome:** A normal capnogram appears with known-good accessories. If so, remove the defective accessory from use.

### 7. Compare With a Known-Good Compatible CO2 Module
When available, test a known-good compatible CO2 module on the same MX750 or test the suspect module on another verified compatible system.

**Expected outcome:** The failure follows either the module or the monitor interface, allowing the affected component to be isolated.

### 8. Verify Measurement Source and Configuration
Confirm that the intended CO2 source is selected and recognized and that no recent configuration or equipment change coincided with the complaint. Avoid unauthorized service-menu changes.

**Expected outcome:** The intended CO2 source is available and properly configured for the clinical setup.

### 9. Perform Functional Verification
Use an appropriate capnography test method or simulator according to facility practice. Verify module recognition, waveform generation, numeric CO2 display, respiratory-rate reporting where applicable, and alarms.

**Expected outcome:** CO2 monitoring performs reliably. If so, troubleshooting is complete.

### 10. Escalate Persistent CO2 Failure
If the module, sampling path, accessories, patient connection, known-good substitutions, and configuration checks do not resolve the issue, stop external troubleshooting.

**Expected outcome:** The affected module or monitor is removed from service for qualified evaluation.

## If the Problem Persists
Common external CO2 causes have been ruled out. The remaining issue may involve a module pump or sensing subsystem, module electronics, monitor interface, internal communication, configuration, or another service-level problem.

The affected equipment should be:
- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Philips documentation and approved test equipment
- Repaired or configured only by qualified personnel

Following repair, verify module recognition, capnogram generation, numeric values, respiratory-rate reporting if applicable, and alarms before return to service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
Loss of a capnogram during ventilation or sedation should be treated as a clinical monitoring interruption until the patient and airway are independently verified.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Separate recognition problems from gas-sampling problems, inspect the complete external CO2 path before assuming module failure, and escalate persistent capnography issues when dependable monitoring cannot be restored.

That is successful troubleshooting.
