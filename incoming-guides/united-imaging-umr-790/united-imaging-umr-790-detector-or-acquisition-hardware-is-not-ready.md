---
schemaVersion: 1
title: "United Imaging uMR 790 MRI System - Detector or Acquisition Hardware Is Not Ready"
issueTitle: "Detector or Acquisition Hardware Is Not Ready"
description: "Troubleshoots acquisition-readiness problems involving coils, external connections, patient setup, system initialization, accessory recognition, and communication before internal service is required."
assetType: "MRI System"
manufacturer: "United Imaging"
model: "uMR 790"
slug: "united-imaging-umr-790-detector-or-acquisition-hardware-is-not-ready"
dateAdded: "2026-09-25"
taxonomyMode: "reuse"
ccr:
  complaint: "MRI staff reported that the uMR 790 would not show the selected imaging coil as ready."
  cause: "Clinical Engineering found the coil connector was not fully seated at the accessible connection point."
  resolution: "The connection was reseated, the coil was consistently recognized, and an approved acquisition check completed normally."
helpfulDetails:
  - "Exact readiness message"
  - "Coil or accessory involved"
  - "Connector condition"
  - "Whether reseating changed the symptom"
  - "Known-good accessory results"
  - "Patient/exam setup"
  - "Whether the issue is intermittent"
  - "Physical damage or contamination"
  - "Results of test acquisition"
  - "Final system status"
---
## What This Guide Helps With

Troubleshoots acquisition-readiness problems involving coils, external connections, patient setup, system initialization, accessory recognition, and communication before internal service is required.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop the Examination
Do not continue scanning when acquisition hardware is unreliable or not ready. Remove the patient from dependence on the affected system and arrange an alternate imaging pathway if necessary.

**Expected outcome:** The patient is safe and troubleshooting can be performed without interrupting required care.

### 2. Confirm the Exact Readiness Condition
Identify what the operator sees:
- Acquisition system not ready
- Coil or accessory not recognized
- Scan preparation cannot complete
- Hardware readiness changes intermittently
- Problem occurs only with a particular setup

Record the displayed wording exactly when possible.

**Expected outcome:** The scope of the readiness problem is known. If the system returns to normal readiness and remains stable, proceed to final verification.

### 3. Verify Complete System Startup
Confirm the MRI system and workstation have completed normal startup and are not still initializing.

Check for other system faults that may prevent acquisition readiness.

**Expected outcome:** The system is fully initialized and otherwise ready. If completion of normal startup clears the condition, verify acquisition and stop.

### 4. Inspect the Selected RF Coil and Accessories
Check the coil or acquisition accessory being used for:
- Visible damage
- Loose connector
- Bent or contaminated connector interface
- Improper placement
- Cable strain
- Incorrect accessory selected for the intended examination

Do not use visibly damaged MRI coils or cables.

**Expected outcome:** The required accessory is intact, correctly positioned, and properly connected. If correcting the connection restores readiness, verify normal recognition and stop.

### 5. Reseat Approved External Connections
If the connection is designed for normal operator or Clinical Engineering handling, disconnect and reconnect it with the system in the appropriate safe state.

Do not access internal RF or acquisition assemblies.

**Expected outcome:** The accessory is consistently recognized after reconnection. If so, complete functional verification and stop.

### 6. Compare With a Known-Good Compatible Accessory
When appropriate and available, test with a known-good compatible coil or accessory approved for the system.

Do not substitute incompatible hardware simply to test the interface.

**Expected outcome:** If the known-good accessory is recognized normally, the original external accessory or cable becomes the likely problem. Remove the suspect accessory from service and stop after verification.

### 7. Check Patient Setup and Exam Selection
Verify the selected examination, coil configuration, patient orientation, and accessory setup match the intended scan workflow.

Do not make unsupported configuration changes to force hardware recognition.

**Expected outcome:** The hardware setup matches the examination requirements. If correcting the setup restores readiness, verify acquisition and stop.

### 8. Inspect the Environment and Connection Areas
Check for liquid contamination, mechanical damage, recently moved equipment, or unusual conditions around accessible acquisition connections.

**Expected outcome:** No environmental or physical condition is compromising hardware recognition. If contamination or damage is present, remove the affected component from service.

### 9. Perform a Controlled Acquisition Verification
After the readiness condition clears, use an approved test setup or site procedure to confirm:
- Hardware remains recognized
- Scan preparation completes
- Acquisition begins normally
- No readiness fault returns

**Expected outcome:** Acquisition hardware remains ready and stable. Troubleshooting can stop.

### 10. Escalate Persistent Acquisition Hardware Failure
If multiple compatible external accessories have been checked and the system still reports acquisition hardware unavailable, stop troubleshooting.

**Expected outcome:** The MRI system is removed from service for qualified evaluation.

## If the Problem Persists

External coils, connections, exam setup, and initialization conditions have been ruled out. Remaining causes may involve RF acquisition hardware, interface electronics, internal communication, configuration, or other service-level subsystems.

The device should be:
- Removed from service
- Labeled **Out of Service**
- Sent for repair or service evaluation
- Evaluated using United Imaging documentation and approved MRI test equipment
- Repaired or configured only by qualified personnel

Do not open RF electronics or perform internal acquisition-system troubleshooting beyond authorized service scope.

Knowing when to stop external troubleshooting is proper troubleshooting. Return to service only after acquisition readiness and appropriate imaging checks have been successfully completed.

## Clinical Use Tip

A damaged or intermittently recognized MRI coil should be removed from clinical use even if reconnecting it temporarily restores operation.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Acquisition-readiness faults should be approached from the outside inward: verify setup, coils, connectors, and system initialization before suspecting internal hardware. Remove unreliable components from service and document all verification performed.

That is successful troubleshooting.
