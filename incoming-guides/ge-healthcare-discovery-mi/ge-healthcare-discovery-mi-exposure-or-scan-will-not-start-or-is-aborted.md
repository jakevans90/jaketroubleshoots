---
schemaVersion: 1
title: "GE Healthcare Discovery MI PET / CT System - Exposure or Scan Will Not Start or Is Aborted"
issueTitle: "Exposure or Scan Will Not Start or Is Aborted"
description: "Troubleshoots scans that will not begin or abort unexpectedly because of readiness, interlocks, patient setup, acquisition settings, connections, or infrastructure."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "Discovery MI"
slug: "ge-healthcare-discovery-mi-exposure-or-scan-will-not-start-or-is-aborted"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "PET / CT staff reported that the Discovery MI would prepare the examination but the scan would not begin."
  cause: "Clinical Engineering found the external scan-control connection loose at the operator area."
  resolution: "Clinical Engineering secured the connection, verified normal system readiness, completed an approved functional acquisition, and returned the scanner to service after required checks passed."
helpfulDetails:
  - "Exact message or abort indication"
  - "Stage at which scan stopped"
  - "PET or CT portion affected"
  - "Protocol being used"
  - "Patient/table position"
  - "Emergency-stop status"
  - "Exposure-control condition"
  - "External cable condition"
  - "Results after restart"
  - "Functional acquisition result"
  - "Final scanner status"
---
## What This Guide Helps With
Troubleshoots scans that will not begin or abort unexpectedly because of readiness, interlocks, patient setup, acquisition settings, connections, or infrastructure.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Repeated Scan Attempts

Do not repeatedly attempt CT exposure or PET / CT acquisition while the reason for an aborted or inhibited scan is unknown.

Safely pause the examination, maintain patient communication, and move the patient to an alternate verified system if timely continuation cannot be assured.

**Expected outcome:** The patient is protected from unnecessary repeat attempts and the scanner is available for controlled troubleshooting.

### 2. Confirm When the Scan Fails

Determine whether the scan:

- Never becomes enabled
- Starts and immediately aborts
- Stops during table movement
- Stops during CT acquisition
- Stops during PET acquisition
- Fails only with a specific protocol

Record any displayed message and the point in the workflow where the failure occurs.

**Expected outcome:** The exact failure point is known.

### 3. Verify Overall System Readiness

Confirm that the system has completed startup and that required PET and CT subsystems indicate ready.

Check for unresolved:

- Hardware-not-ready conditions
- Interlock conditions
- Motion faults
- Cooling warnings
- Communication faults
- Workstation errors

**Expected outcome:** The scanner is fully initialized and no general readiness condition is blocking acquisition.

### 4. Check Patient Positioning and Travel Path

Verify that the patient, table, cables, monitoring equipment, injector tubing, positioning aids, and other accessories are arranged so they cannot interfere with table or gantry operation.

Make sure no object is contacting the gantry or obstructing travel.

**Expected outcome:** The patient setup permits safe, unobstructed positioning and acquisition.

### 5. Verify Safety and Exposure Controls

Check accessible emergency-stop, exposure-control, and normal safety-interlock status.

Do not bypass or defeat an interlock to make an exposure proceed.

Inspect external exposure-control hardware and accessible cables for damage or loose connections where applicable.

**Expected outcome:** Safety controls are in their normal operating state and accessible exposure-control components are intact.

### 6. Review Study and Protocol Setup

Confirm that the selected protocol and patient examination are complete and appropriate for the intended scan.

Check operator-accessible items such as:

- Correct examination selected
- Required acquisition steps completed
- Necessary positioning entered
- Required accessories recognized
- No obvious incomplete field or workflow step

Do not modify restricted protocol or service parameters unless authorized.

**Expected outcome:** The examination is correctly prepared and no incomplete setup is preventing acquisition.

### 7. Determine Whether the Failure Is Protocol-Specific

When safe and clinically appropriate, compare the behavior using an approved test workflow or another known-good standard configuration.

Do not expose a patient solely for troubleshooting.

**Expected outcome:** The technician can determine whether the fault affects the entire acquisition system or only a particular workflow.

If an operator-level setup issue is identified and corrected, proceed to final verification.

### 8. Perform an Approved Controlled Restart

If no unsafe condition exists and external checks are normal, perform an approved normal restart according to department and manufacturer procedures.

Avoid repeated restart attempts if the same abort recurs.

**Expected outcome:** The scanner initializes normally and acquisition readiness is restored.

### 9. Perform Final Functional Verification

Complete an approved nonclinical or quality-control verification as appropriate.

Confirm:

- Scan initiation is enabled
- Acquisition begins normally
- Table motion occurs correctly
- The acquisition completes without unexpected abort
- Data are available for reconstruction
- No unresolved warning remains

**Expected outcome:** The system completes a representative acquisition normally.

If required functional and safety testing passes, troubleshooting can stop and the scanner may be returned to service.

## If the Problem Persists

If readiness, patient setup, safety controls, external exposure controls, protocol setup, connections, and approved restart procedures are normal but scanning still fails or aborts, the cause may involve internal acquisition electronics, safety interlocks, motion synchronization, generator or exposure systems, detector communication, PET acquisition hardware, workstation communication, or another service-level condition.

The system should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or formal system evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not bypass exposure interlocks or repeatedly generate exposures to reproduce a persistent fault.

After repair, perform all required radiation, acquisition, image-quality, functional, and safety verification before return to clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Avoid unnecessary repeat CT exposure while investigating scan aborts; move the patient to another verified imaging system when reliable acquisition cannot be promptly confirmed.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

A failed or aborted scan should be approached by protecting the patient, identifying exactly where the workflow stops, and checking readiness, positioning, interlocks, controls, and study setup before assuming internal acquisition failure. Verify the correction without unnecessary patient exposure and document the result clearly.

That is successful troubleshooting.
