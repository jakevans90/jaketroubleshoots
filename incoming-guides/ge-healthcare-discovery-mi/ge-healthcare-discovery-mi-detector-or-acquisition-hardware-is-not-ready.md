---
schemaVersion: 1
title: "GE Healthcare Discovery MI PET / CT System - Detector or Acquisition Hardware Is Not Ready"
issueTitle: "Detector or Acquisition Hardware Is Not Ready"
description: "Troubleshoots PET or CT acquisition readiness problems caused by incomplete startup, connections, accessories, environmental conditions, configuration, or subsystem communication."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "Discovery MI"
slug: "ge-healthcare-discovery-mi-detector-or-acquisition-hardware-is-not-ready"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the Discovery MI displayed an acquisition-not-ready condition and would not begin the planned study."
  cause: "Clinical Engineering found an accessible acquisition workstation connection partially disconnected after equipment had been moved."
  resolution: "Clinical Engineering secured the connection, restarted the affected system components normally, verified acquisition readiness, and confirmed successful functional testing before return to service."
helpfulDetails:
  - "Exact displayed message"
  - "PET, CT, or both affected"
  - "Startup status"
  - "Recent power interruption"
  - "External cable condition"
  - "Accessories connected"
  - "Environmental condition"
  - "Results after restart"
  - "Test acquisition result"
  - "Final subsystem status"
---
## What This Guide Helps With
Troubleshoots PET or CT acquisition readiness problems caused by incomplete startup, connections, accessories, environmental conditions, configuration, or subsystem communication.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Clinical Acquisition

Do not continue a patient examination when the scanner reports that required detector or acquisition hardware is not ready.

Safely pause the study and establish an alternate imaging plan if the system cannot promptly return to a verified ready state.

**Expected outcome:** No patient is depending on unreliable acquisition hardware.

### 2. Identify Which Acquisition Function Is Not Ready

Determine whether the reported condition involves:

- PET acquisition
- CT acquisition
- Both modalities
- A specific external accessory or interface
- The acquisition workstation
- A general system-not-ready condition

Record the exact displayed message and when it appears.

**Expected outcome:** The affected acquisition path is clearly identified.

### 3. Confirm Complete System Startup

Verify that the Discovery MI has fully initialized.

Check whether any subsystem still shows:

- Starting
- Initializing
- Offline
- Not ready
- Communication unavailable
- Faulted status

Allow normal initialization to complete before attempting additional studies.

**Expected outcome:** Required PET / CT subsystems reach their normal ready state.

If normal initialization completes and acquisition becomes available, proceed to functional verification.

### 4. Check External Connections and Accessories

Inspect accessible acquisition-related connections and approved accessories for:

- Loose connectors
- Damaged cables
- Recently disconnected equipment
- Incorrectly seated accessories
- External devices that are powered off
- Connections disturbed during cleaning or service activity

Do not access detector assemblies or internal gantry electronics.

**Expected outcome:** Accessible acquisition connections and required external accessories are secure and functional.

### 5. Verify Examination Setup and Configuration

Review the selected examination and acquisition setup.

Confirm that required study parameters, patient information, acquisition mode, and approved accessory selections are complete and appropriate.

Do not change service calibration data or restricted configuration values.

**Expected outcome:** The selected study is properly configured and is not being blocked by an incomplete operator-level setup.

### 6. Check Environmental and Support Conditions

Look for room or system conditions that may prevent detector readiness, including:

- Abnormal room temperature
- Cooling alarms
- Recent power interruption
- Support-system alarms
- Facility maintenance
- Network or communication outage affecting system components

**Expected outcome:** Required environmental and support conditions are normal.

### 7. Perform an Approved Restart if Appropriate

If external checks are normal and no hazardous condition exists, use an approved normal restart procedure according to local policy and manufacturer guidance.

Do not repeatedly restart a scanner that consistently returns to the same acquisition fault.

**Expected outcome:** The system reinitializes and the PET and CT acquisition subsystems reach normal ready status.

If the affected subsystem returns to ready and remains stable, proceed to final verification.

### 8. Verify Acquisition Readiness Without Patient Dependence

Use the appropriate approved system checks, test workflow, or quality-control process to confirm that the affected acquisition path is functioning.

Verify that:

- Required hardware reports ready
- No unresolved warning remains
- Acquisition can be initiated appropriately
- Data are received by the workstation
- The system remains stable

**Expected outcome:** Acquisition hardware is ready and produces a normal test result.

If required verification passes, troubleshooting can stop and the scanner may be returned to service.

## If the Problem Persists

If startup, accessible connections, study configuration, environmental conditions, and approved restart procedures have been verified but detector or acquisition hardware remains unavailable, the cause may involve internal detector electronics, acquisition hardware, communication links, timing or synchronization functions, power distribution, cooling, or service-level configuration.

The system should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or formal system evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired, calibrated, or configured only by qualified personnel

Do not attempt detector disassembly or internal electronics troubleshooting without authorized service procedures.

Following repair, complete manufacturer-required acquisition, calibration, image-quality, and safety verification before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Do not begin or continue a PET / CT examination unless all required acquisition subsystems indicate normal readiness before the patient is committed to the scan.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

An acquisition-not-ready condition does not automatically mean a detector failure. Protect the patient, identify the affected modality, verify startup, connections, setup, environment, and communication first, then escalate when the problem remains beyond safe external troubleshooting.

That is successful troubleshooting.
