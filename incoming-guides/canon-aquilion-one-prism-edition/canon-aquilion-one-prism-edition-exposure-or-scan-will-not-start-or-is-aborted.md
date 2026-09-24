---
schemaVersion: 1
title: "Canon Aquilion ONE / PRISM Edition CT Scanner - Exposure or Scan Will Not Start or Is Aborted"
issueTitle: "Exposure or Scan Will Not Start or Is Aborted"
description: "Addresses scans that will not begin or abort because of readiness, positioning, protocol, interlock, connection, or infrastructure conditions."
assetType: "CT Scanner"
manufacturer: "Canon"
model: "Aquilion ONE / PRISM Edition"
slug: "canon-aquilion-one-prism-edition-exposure-or-scan-will-not-start-or-is-aborted"
dateAdded: "2026-09-24"
taxonomyMode: "reuse"
ccr:
  complaint: "CT staff reported a scheduled scan would prepare normally but would not begin exposure."
  cause: "Clinical Engineering found an external exam accessory required by the selected workflow was not connected correctly."
  resolution: "Corrected the accessory connection, performed an approved non-patient scan verification, and confirmed the system completed acquisition normally."
helpfulDetails:
  - "Exact abort or exposure message."
  - "Exam or protocol used."
  - "Whether scan never started or aborted mid-scan."
  - "Table and patient positioning."
  - "Emergency-stop status."
  - "Accessories involved."
  - "Known-good substitution results."
  - "Whether other protocols functioned."
  - "Functional verification results."
  - "Final device status."
---
## What This Guide Helps With

Addresses scans that will not begin or abort because of readiness, positioning, protocol, interlock, connection, or infrastructure conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Repeated Exposure Attempts
Do not repeatedly attempt exposures on a patient while the cause of a scan failure is unknown. If imaging is clinically urgent, transfer the patient to another verified scanner.

**Expected outcome:** Unnecessary radiation exposure and examination delay are minimized.

### 2. Confirm the Exact Failure
Determine whether the scan does not start at all or begins and then aborts. Record the protocol, exam stage, displayed message, and whether the condition occurs on every study or one specific exam.

**Expected outcome:** The failure mode is clearly defined.

### 3. Verify Scanner Ready Status
Confirm that the system has completed startup and indicates that the gantry, acquisition system, table, and other required subsystems are ready.

**Expected outcome:** No basic readiness condition is preventing scanning.

If normal ready status is restored and the scan process functions correctly during approved testing, proceed to verification.

### 4. Verify Patient and Table Positioning
Check that the patient table is positioned appropriately and that no external accessory, cable, tubing, support, or obstruction interferes with required movement or scanner operation.

**Expected outcome:** Positioning and external accessories do not prevent the examination.

### 5. Check Safety Interlocks and Emergency Controls
Inspect accessible safety and emergency-stop controls for an active condition.

Do not bypass any exposure or motion interlock.

**Expected outcome:** Safety systems are in their normal operating state.

### 6. Check Protocol and Exam Setup
Verify that the intended exam, patient selection, scan range, required workflow steps, and operator selections appear complete.

Do not alter restricted protocols or service-level parameters.

**Expected outcome:** No obvious workflow or selection error is preventing scan initiation.

If correcting the clinical setup resolves the issue, verify successful scan preparation and stop after functional confirmation.

### 7. Inspect External Connections and Accessories
Check accessible injector interfaces, ECG gating leads when applicable, workstation connections, and other external devices involved in the selected exam.

Use a known-good accessory or connection when appropriate and approved.

**Expected outcome:** External devices needed for the exam are connected and functioning.

### 8. Review the Pattern of Aborts
Determine whether failures occur only with a particular protocol, accessory, room condition, or workflow.

This helps distinguish a system-wide fault from an external or exam-specific problem.

**Expected outcome:** The failure is isolated to a reproducible condition or confirmed to affect general scanning.

### 9. Perform Approved Non-Patient Functional Verification
After correcting any external cause, perform an approved scan or system test without a patient as appropriate.

Confirm that the scan starts, completes, reconstructs, and returns the system to ready status.

**Expected outcome:** The CT system completes the test without aborting.

If achieved, troubleshooting is complete.

### 10. Escalate Persistent Exposure or Scan Failure
If scanning still will not begin or repeatedly aborts, remove the scanner from service. Do not troubleshoot internal X-ray generation, detector electronics, gantry control hardware, or restricted service functions without qualified service support.

**Expected outcome:** An unreliable scanner is not used clinically.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may include internal acquisition systems, X-ray generation, motion control, interlocks, synchronization, detector readiness, configuration, or infrastructure problems.

The CT scanner should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or qualified service evaluation.
- Evaluated using appropriate Canon service documentation and approved test equipment.
- Repaired, calibrated, or configured only by qualified personnel.

Complete required radiation, image-quality, and functional verification following service before return to clinical use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not repeatedly expose a patient in an attempt to determine whether an intermittent scan-abort condition has cleared.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Avoid unnecessary patient exposure, verify readiness and external workflow conditions first, and escalate repeated scan failures instead of assuming or bypassing an internal fault.

That is successful troubleshooting.
