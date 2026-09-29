---
schemaVersion: 1
title: "GE Healthcare NM/CT 870 CZT PET / CT System - Detector or Acquisition Hardware Is Not Ready"
issueTitle: "Detector or Acquisition Hardware Is Not Ready"
description: "Detector or acquisition hardware remains unavailable because of startup state, connections, accessory configuration, communication, temperature, or environmental conditions."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "NM/CT 870 CZT"
slug: "ge-healthcare-nm-ct-870-czt-detector-or-acquisition-hardware-is-not-ready"
dateAdded: "2026-09-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported the NM/CT 870 CZT acquisition system remained not ready after patient setup."
  cause: "Clinical Engineering found an accessible external system communication connector was not fully seated."
  resolution: "Clinical Engineering secured the connection, restarted the system through the approved process, verified detector readiness and required functional checks, and returned the system to service."
helpfulDetails:
  - "Exact not-ready message"
  - "Detector or subsystem affected"
  - "Startup versus mid-study occurrence"
  - "External connection condition"
  - "Detector and gantry positioning"
  - "Environmental condition"
  - "Communication status"
  - "Restart result"
  - "Quality-control result"
  - "Final acquisition readiness"
---
## What This Guide Helps With

Detector or acquisition hardware remains unavailable because of startup state, connections, accessory configuration, communication, temperature, or environmental conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Clinical Acquisition

Do not continue an examination when the detector or acquisition system is reporting an unreliable or not-ready condition. Safely remove or transfer the patient as appropriate before troubleshooting.

**Expected outcome:** No patient depends on acquisition hardware whose readiness cannot be confirmed.

### 2. Confirm the Exact Not-Ready Condition

Record the exact displayed message and determine whether the condition involves the CZT detector system, CT acquisition hardware, one detector position, the entire acquisition chain, or another subsystem.

Ask whether the condition began during startup, positioning, calibration, or an active study.

**Expected outcome:** The affected acquisition function and timing of the fault are identified. If readiness returns and remains stable, verify operation and troubleshooting can stop.

### 3. Verify Overall System Startup Is Complete

Confirm the workstation, gantry, acquisition computers, detectors, and related system components have completed normal initialization.

Do not assume detector failure when the detector is waiting on another subsystem.

**Expected outcome:** All prerequisite system components indicate their normal ready state.

### 4. Inspect External Detector and Accessory Conditions

Inspect accessible detector surfaces, positioning areas, external cables, connectors, covers, and accessories for obvious damage, obstruction, contamination, or improper seating.

Do not disconnect or manipulate internal detector connections.

**Expected outcome:** No external physical condition is preventing detector readiness. If correcting an approved external connection restores readiness, verify operation and troubleshooting can stop.

### 5. Verify Positioning and Mechanical State

Confirm detector heads, gantry components, table, and positioning accessories are in a valid operating position and that no collision or safety condition is active.

**Expected outcome:** Mechanical positioning permits normal acquisition readiness.

### 6. Check Environment and Ventilation

Verify room temperature and ventilation appear normal, air pathways are not blocked, and there is no evidence of recent HVAC failure, excessive heat, water intrusion, or contamination.

Acquisition electronics may intentionally remain unavailable when environmental conditions are unsuitable.

**Expected outcome:** No external environmental condition is preventing system readiness.

### 7. Check Communication Status

Review normal operator-visible system status for loss of communication between acquisition hardware and the workstation.

Inspect accessible network or system communication cables where Clinical Engineering is authorized to do so.

**Expected outcome:** External communication paths are intact and required subsystems are visible to the system.

### 8. Perform One Controlled Restart if Appropriate

If there are no indications of overheating, electrical damage, or repeated hardware faults, perform an approved controlled restart.

Avoid repeated restart attempts if the same acquisition subsystem fails every time.

**Expected outcome:** Detector and acquisition hardware complete initialization and reach a stable ready state. If so, proceed to functional verification and troubleshooting can stop afterward.

### 9. Perform Appropriate Readiness and Quality Verification

Before clinical use, complete the applicable system readiness check, acquisition test, or quality-control process required by site and manufacturer procedures.

Do not return the system to service solely because the error disappeared.

**Expected outcome:** Acquisition hardware remains ready and passes required verification. The issue is resolved and troubleshooting can stop.

### 10. Escalate Persistent Hardware Not-Ready Conditions

If external connections, positioning, environment, initialization, and communication are normal but the hardware remains unavailable, remove the system from service.

Do not attempt CZT detector module repair, internal acquisition electronics repair, internal cabling repair, or restricted service configuration without appropriate authorization.

**Expected outcome:** A persistent acquisition-system problem is referred for qualified evaluation before further patient use.

## If the Problem Persists

External readiness, positioning, communication, connection, and environmental causes have been ruled out. Remaining categories may include detector electronics, acquisition computers, internal communication, power distribution, temperature monitoring, detector positioning feedback, or service-level configuration.

The device should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or system evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Required detector, CT, acquisition, and quality-control verification should be completed after repair before clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A detector that intermittently reports ready is not suitable for patient imaging until stable readiness and required quality checks are demonstrated.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Treat acquisition readiness as a patient-safety requirement, verify external dependencies before assuming detector failure, confirm performance with required testing, and escalate persistent hardware conditions appropriately.

That is successful troubleshooting.
