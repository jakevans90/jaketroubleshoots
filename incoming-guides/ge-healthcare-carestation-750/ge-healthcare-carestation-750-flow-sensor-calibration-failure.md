---
schemaVersion: 1
title: "GE Healthcare Carestation 750 Anesthesia Machine - Flow Sensor Calibration Failure"
issueTitle: "Flow Sensor Calibration Failure"
description: "Flow calibration fails because of sensor contamination, moisture, improper installation, breathing-system leaks, connections, or an unresolved measurement fault."
assetType: "Anesthesia Machine"
manufacturer: "GE Healthcare"
model: "Carestation 750"
slug: "ge-healthcare-carestation-750-flow-sensor-calibration-failure"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Anesthesia staff reported that the Carestation 750 repeatedly failed flow sensor calibration during system checkout."
  cause: "Clinical Engineering found moisture on an accessible flow-sensing component that was interfering with calibration."
  resolution: "The affected component was addressed according to approved handling requirements, calibration passed, and ventilation measurements were verified during final checkout."
helpfulDetails:
  - "Exact calibration message"
  - "Whether the failure repeats"
  - "Flow-sensor condition"
  - "Moisture or contamination observed"
  - "Sensor orientation and seating"
  - "Circuit leak status"
  - "Breathing-system configuration"
  - "Known-good substitution result"
  - "Calibration result after correction"
  - "Volume-verification result"
  - "Final device status"
---

## What This Guide Helps With
Flow calibration fails because of sensor contamination, moisture, improper installation, breathing-system leaks, connections, or an unresolved measurement fault.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Remove the Machine From Active Use
Do not troubleshoot questionable flow measurement while the Carestation 750 is being relied on for patient ventilation or respiratory-volume monitoring.

Move clinical care to another verified anesthesia machine if necessary.

**Expected outcome:** The machine is available for controlled testing without patient dependence.

### 2. Confirm the Calibration Failure
Repeat the approved calibration or checkout sequence and document the exact point at which it fails.

Record any associated message rather than assuming the flow sensor itself is defective.

**Expected outcome:** The calibration failure is reproducible. If calibration completes normally on repeat testing and subsequent checkout passes, troubleshooting can stop.

### 3. Inspect the Breathing Circuit and Connections
Check for disconnected hoses, open ports, loose fittings, damaged tubing, or incorrectly installed accessories that could interfere with calibration.

**Expected outcome:** The breathing circuit is complete and securely connected. If correcting an external leak allows calibration to pass, the issue is resolved.

### 4. Inspect Accessible Flow-Sensing Components
Following approved handling practices, inspect user-removable or Clinical Engineering-accessible flow-sensing components for:

- Moisture
- Visible contamination
- Damage
- Incorrect orientation
- Incomplete seating
- Loose connections

Do not probe or mechanically alter sensitive sensing elements.

**Expected outcome:** Flow-sensing components are clean, dry, intact, correctly oriented, and fully seated.

### 5. Allow Wet Components to Be Corrected Appropriately
If moisture is present in approved reusable components, address it according to manufacturer instructions. Replace disposable components when contamination or damage is present.

Do not use unapproved cleaning or drying techniques.

**Expected outcome:** No moisture or contamination remains that could interfere with measurement. If calibration then succeeds, troubleshooting can stop after verification.

### 6. Reseat the Flow-Sensing Assembly
Remove and reinstall only components intended to be routinely removable, checking mating surfaces and accessible connectors for damage or obstruction.

**Expected outcome:** The sensor assembly is securely installed and recognized. Successful calibration after reseating confirms the issue was installation related.

### 7. Verify Breathing-System Assembly
Check that externally removable breathing-system parts and consumables are properly installed.

A leak or incorrect assembly elsewhere in the system can produce a calibration failure even when the sensor appears normal.

**Expected outcome:** The breathing system is correctly assembled with no obvious external leak source.

### 8. Substitute a Known-Good Compatible Component When Appropriate
If the flow-sensing component is routinely replaceable and an approved compatible known-good component is available, substitute it and repeat calibration.

**Expected outcome:** If calibration succeeds with the known-good component, replace the original component. If calibration continues to fail, escalate rather than repeatedly replacing parts.

### 9. Repeat Checkout and Verify Volume Measurement
After calibration succeeds, test ventilation using an appropriate test lung or analyzer.

Verify stable inspired and expired volume measurement and complete the required checkout.

**Expected outcome:** Calibration, volume measurement, and checkout operate normally. Troubleshooting can stop.

### 10. Escalate Repeated Calibration Failure
If calibration continues to fail after external leaks, installation, moisture, contamination, and replaceable components have been ruled out, stop external troubleshooting.

**Expected outcome:** The Carestation 750 remains out of service pending service-level evaluation.

## If the Problem Persists
Common external causes have been ruled out. Remaining possibilities may involve internal signal processing, sensor interfaces, pneumatic measurement paths, internal connections, or other service-level faults.

The Carestation 750 should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired or configured only by qualified personnel

Successful calibration alone should be followed by functional ventilation and checkout verification before return to service.

Knowing when repeated calibration failure requires escalation is proper troubleshooting.

## Clinical Use Tip
Do not return an anesthesia machine to service when flow-derived volume measurements cannot be verified as reliable.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
A calibration failure does not automatically indicate an internal sensor defect. Verify the breathing system, moisture, contamination, seating, and external components first, then confirm measurement accuracy before return to clinical service and clearly document what was found.

That is successful troubleshooting.
