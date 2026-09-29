---
schemaVersion: 1
title: "GE Healthcare NM/CT 870 CZT PET / CT System - Exposure or Scan Will Not Start or Is Aborted"
issueTitle: "Exposure or Scan Will Not Start or Is Aborted"
description: "An acquisition will not begin or stops unexpectedly because of readiness, interlocks, positioning, protocol, communication, or external system conditions."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "NM/CT 870 CZT"
slug: "ge-healthcare-nm-ct-870-czt-exposure-or-scan-will-not-start-or-is-aborted"
dateAdded: "2026-09-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported the NM/CT 870 CZT study would not begin and returned to a not-ready condition when acquisition was initiated."
  cause: "Clinical Engineering found a positioning accessory preventing the system from reaching the required acquisition position."
  resolution: "Clinical Engineering corrected the accessory placement, completed a nonclinical test acquisition, verified normal scan completion, and returned the system to service."
helpfulDetails:
  - "Exact abort or readiness message"
  - "Nuclear medicine or CT acquisition affected"
  - "Protocol selected"
  - "Stage where acquisition stopped"
  - "Table and detector position"
  - "Interlock status"
  - "External accessories in use"
  - "Communication status"
  - "Nonclinical test result"
  - "Final system status"
---
## What This Guide Helps With

An acquisition will not begin or stops unexpectedly because of readiness, interlocks, positioning, protocol, communication, or external system conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Repeated Attempts

Do not repeatedly initiate CT exposure or nuclear imaging acquisition while the cause of an abort is unknown. Safely end the attempted study and remove or transfer the patient when continued operation cannot be assured.

**Expected outcome:** The patient is not subjected to unnecessary repeated acquisition attempts or unreliable imaging.

### 2. Confirm Which Acquisition Fails

Determine whether the problem affects nuclear medicine acquisition, CT acquisition, combined workflow, or all study types.

Record the exact message, stage of the scan, protocol selected, and whether the scan never starts or begins and then aborts.

**Expected outcome:** The failure is narrowed to a specific acquisition stage. If a valid acquisition now completes normally, verify the system and troubleshooting can stop.

### 3. Verify System Readiness

Check normal operator-visible status for detector readiness, CT readiness, table and gantry readiness, workstation communication, and required system initialization.

**Expected outcome:** All components required by the selected workflow indicate ready.

### 4. Check Patient Positioning and Interlocks

Verify patient positioning, table location, detector position, gantry position, accessories, and physical clearances.

Confirm no emergency-stop, collision detection, or other accessible safety interlock is active.

**Expected outcome:** The system is physically positioned to permit the intended acquisition and no safety condition is blocking operation.

### 5. Verify Protocol and Study Setup

Confirm the correct patient, examination, acquisition protocol, and required study information are selected.

Do not change clinical parameters merely to bypass an error. Compare with a known valid setup when appropriate.

**Expected outcome:** The study setup is complete and internally consistent for the intended procedure.

### 6. Inspect Required External Accessories and Connections

Check accessible cables, acquisition controls, patient-related accessories, gating or monitoring connections when used, and other externally connected equipment required by the selected examination.

Use a known-good compatible accessory when appropriate and authorized.

**Expected outcome:** Required external accessories and controls are connected and functioning. If substitution restores reliable scanning, remove the defective accessory from service and troubleshooting can stop after verification.

### 7. Check for Communication Interruptions

Review normal status indicators for workstation, acquisition, gantry, detector, and CT subsystem communication.

Inspect authorized external network or system connections if communication loss coincides with the abort.

**Expected outcome:** Required system components maintain communication through scan initiation.

### 8. Perform a Controlled Nonclinical Test

Once external causes are corrected, perform an appropriate nonpatient test or approved quality-control acquisition.

Do not use a patient as the test load for an unresolved scanning problem.

**Expected outcome:** The scan initiates, continues, and completes normally without unexpected abort. If successful and required checks pass, troubleshooting can stop.

### 9. Evaluate Reproducibility

If the problem occurred only once, confirm that the system remains stable through repeated appropriate test operation rather than assuming a transient recovery proves reliability.

**Expected outcome:** Acquisition is consistently repeatable and system readiness remains normal.

### 10. Escalate Repeated Scan Failure

If the scan repeatedly fails despite normal readiness, positioning, accessories, study setup, and external communication, remove the system from service.

Do not bypass exposure controls, interlocks, or internal acquisition safeguards.

**Expected outcome:** Persistent scan or exposure failure is escalated for qualified service rather than worked around clinically.

## If the Problem Persists

Common external causes involving readiness, patient positioning, interlocks, study setup, accessories, controls, and communication have been ruled out. Remaining categories may include CT generation or acquisition hardware, detector electronics, synchronization, internal communication, system software, or protected configuration.

The device should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or system evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Complete appropriate acquisition, radiation-system, detector, and quality-control verification before return to clinical service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not repeatedly expose or rescan a patient simply to determine whether an intermittent acquisition fault has cleared.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Prevent unnecessary patient exposure, confirm readiness and physical conditions first, verify correction with a controlled test rather than a patient, and escalate repeated scan failures instead of bypassing safeguards.

That is successful troubleshooting.
