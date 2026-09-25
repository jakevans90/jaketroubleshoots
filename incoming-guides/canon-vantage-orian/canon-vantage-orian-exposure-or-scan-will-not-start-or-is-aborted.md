---
schemaVersion: 1
title: "Canon Vantage Orian MRI System - Exposure or Scan Will Not Start or Is Aborted"
issueTitle: "Exposure or Scan Will Not Start or Is Aborted"
description: "Addresses MRI scan sequences that will not begin or terminate unexpectedly because of readiness, setup, coil, patient, communication, or environmental conditions."
assetType: "MRI System"
manufacturer: "Canon"
model: "Vantage Orian"
slug: "canon-vantage-orian-exposure-or-scan-will-not-start-or-is-aborted"
dateAdded: "2026-09-25"
taxonomyMode: "reuse"
ccr:
  complaint: "MRI staff reported scans would not start and the system returned to a not-ready condition."
  cause: "Clinical Engineering found the selected imaging coil connection was not fully seated."
  resolution: "Secured the coil connection, confirmed normal hardware recognition, and completed an approved functional scan without recurrence."
helpfulDetails:
  - "Exact message displayed"
  - "Whether scan failed before or during acquisition"
  - "Protocol involved"
  - "Patient/table position"
  - "Coil used"
  - "Connector condition"
  - "Other exams or coils tested"
  - "Recent power or infrastructure event"
  - "Results after correction"
  - "Final scanner status"
---
## What This Guide Helps With
Addresses MRI scan sequences that will not begin or terminate unexpectedly because of readiness, setup, coil, patient, communication, or environmental conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Repeated Scan Attempts
If a scan repeatedly fails or aborts, do not continue retrying while a patient depends on unreliable operation. Assess the clinical situation and transfer the patient to another verified imaging workflow when necessary.

**Expected outcome:** Patient care is maintained without relying on an unstable scanner.

### 2. Confirm How the Scan Fails
Determine whether the scan never begins, starts and immediately aborts, stops partway through acquisition, or fails only with one exam or protocol.

Record displayed messages exactly and note when during the workflow the failure occurs.

**Expected outcome:** The failure point is clearly identified.

### 3. Verify Overall System Readiness
Confirm startup is complete, the scanner is not reporting another unresolved fault, and required subsystems indicate normal readiness.

**Expected outcome:** No general system condition prevents scanning.

### 4. Check Patient and Table Positioning
Verify the table is properly positioned, patient setup is complete, and no positioning issue, cable routing problem, or accessory obstruction is preventing the scan workflow.

**Expected outcome:** Patient positioning and table status are appropriate for the examination.

### 5. Inspect the Coil and Connections
Confirm the required imaging coil is correctly connected and physically intact. Check accessible connectors and cables for incomplete seating or visible damage.

**Expected outcome:** Required acquisition accessories are recognized and secure.

If correcting the coil connection restores scan operation, proceed to final verification.

### 6. Verify Routine Exam Settings
Review operator-visible patient orientation, exam selection, coil selection, and other routine settings involved in the attempted scan.

Do not alter protected service configuration or calibration values.

**Expected outcome:** The scan setup matches the intended examination and connected hardware.

### 7. Determine Whether the Failure Is Protocol-Specific
When clinically appropriate and without a patient dependent on the scanner, compare operation using another approved routine workflow or test setup.

Do not modify clinical protocols solely to bypass a persistent fault.

**Expected outcome:** The problem is identified as either specific to one workflow or present across scanning generally.

### 8. Check for Recent Environmental or Infrastructure Changes
Ask whether the problem followed a power event, HVAC issue, network interruption, software event, facility maintenance activity, or equipment change in or near the MRI environment.

**Expected outcome:** External environmental or infrastructure causes are either identified or reasonably excluded.

### 9. Perform a Controlled Functional Verification
After correcting any external cause, verify the system can initiate and complete an appropriate approved scan/test acquisition without aborting or displaying the original condition.

**Expected outcome:** The scan begins, proceeds, and completes normally with stable system readiness.

If achieved, troubleshooting can stop.

### 10. Escalate Repeated Scan Abortions
If scans continue to abort with known-good accessories and correct setup, remove the MRI from clinical service.

Do not investigate internal RF, gradient, power, control, or magnet-related hardware beyond authorized external checks.

**Expected outcome:** The scanner is referred for qualified service evaluation.

## If the Problem Persists

Common external readiness, positioning, coil, connection, protocol-selection, and environmental causes have been ruled out. The remaining issue may involve RF or gradient subsystems, scanner control, system software, safety interlocks, cooling, configuration, or other service-level functions.

The MRI system should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or system evaluation
- Evaluated using appropriate Canon service documentation and approved test equipment
- Repaired or configured only by qualified personnel

After repair, verify normal scan initiation and completion and perform appropriate image-quality and system checks before clinical return.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Repeatedly restarting an aborted examination can delay care without identifying the cause; move the patient to a reliable imaging pathway when scanner stability is uncertain.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Start by protecting the patient and identifying exactly where the MRI workflow fails. Rule out readiness, positioning, accessory, and configuration causes before escalating to internal subsystems, then verify a complete acquisition and document the event clearly.

That is successful troubleshooting.
