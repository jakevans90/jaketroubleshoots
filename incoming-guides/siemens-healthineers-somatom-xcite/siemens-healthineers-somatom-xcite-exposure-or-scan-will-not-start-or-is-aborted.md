---
schemaVersion: 1
title: "Siemens Healthineers SOMATOM X.cite CT Scanner - Exposure or Scan Will Not Start or Is Aborted"
issueTitle: "Exposure or Scan Will Not Start or Is Aborted"
description: "Use this guide when a prepared CT examination will not begin, terminates unexpectedly, or repeatedly aborts before normal acquisition is completed."
assetType: "CT Scanner"
manufacturer: "Siemens Healthineers"
model: "SOMATOM X.cite"
slug: "siemens-healthineers-somatom-xcite-exposure-or-scan-will-not-start-or-is-aborted"
dateAdded: "2026-09-24"
taxonomyMode: "reuse"
ccr:
  complaint: "CT staff reported that scans on the SOMATOM X.cite would prepare normally but would not start."
  cause: "Clinical Engineering found an unresolved positioning condition preventing the system from reaching scan-ready status."
  resolution: "The positioning condition was corrected, a nonpatient test scan completed normally, and scanner readiness was verified before return to service."
helpfulDetails:
  - "Exact point where the scan stopped"
  - "Displayed warning or message"
  - "Selected protocol"
  - "Table and positioning status"
  - "Emergency or safety-control status"
  - "Whether all protocols were affected"
  - "Results with a nonpatient test"
  - "Results after approved restart"
  - "Any abnormal sound, odor, or heat"
  - "Final scanner status"
---
## What This Guide Helps With

Use this guide when a prepared CT examination will not begin, terminates unexpectedly, or repeatedly aborts before normal acquisition is completed.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Discontinue Unreliable Scanning
Stop repeated attempts if the scanner cannot reliably initiate or complete acquisition. Remove the patient when clinically appropriate and arrange alternate imaging if needed.  
**Expected outcome:** The patient is not subjected to repeated unsuccessful scan attempts or unnecessary exposure.

### 2. Confirm the Exact Failure Point
Determine whether the scan fails during preparation, immediately before exposure, at exposure initiation, or during acquisition. Record all displayed messages and operator observations.  
**Expected outcome:** The failure is tied to a specific stage of the scan sequence.

### 3. Verify System Ready Status
Confirm the scanner has completed startup and that the operator interface reports the system ready for the intended examination. Check for unresolved warnings or interlocks.  
**Expected outcome:** No general system-readiness condition is preventing acquisition.

### 4. Check Patient Positioning and Table Conditions
Verify that the patient table and positioning setup are within the intended examination workflow and that no obstruction, collision condition, or positioning fault is present.  
**Expected outcome:** Patient positioning and table status do not prevent scan initiation.

### 5. Verify Protocol and Operator Selections
Confirm that the intended examination and protocol are selected correctly and that all required normal workflow entries have been completed. Do not alter protected configuration parameters.  
**Expected outcome:** No incomplete or incorrect operator selection is blocking the scan.

### 6. Check Accessible Interlocks and Room Conditions
Verify accessible emergency controls, room conditions, and other normal safety interlocks. Confirm that no visible door, positioning, or system-state condition is preventing exposure.  
**Expected outcome:** External safety conditions permit scanning.

### 7. Perform an Approved Nonpatient Test
If safe and permitted, reproduce the condition using an approved phantom or nonpatient test workflow rather than repeatedly exposing a patient.  
**Expected outcome:** The scanner completes the test acquisition normally. If it does, investigate the original workflow conditions and stop troubleshooting once reliable function is verified.

### 8. Perform One Approved Restart if Appropriate
If no hardware safety concern is present, complete the normal system restart process and repeat the approved nonpatient test.  
**Expected outcome:** Scan initiation and completion return to normal without unexpected aborts.

### 9. Escalate Repeated Scan Aborts
If scans still fail or abort, especially if the event is repeatable under controlled nonpatient testing, remove the system from service.  
**Expected outcome:** Further exposure attempts cease and qualified service evaluation is initiated.

## If the Problem Persists

External workflow, positioning, accessible safety conditions, system readiness, and normal restart have been checked. Remaining causes may involve acquisition control, high-voltage or X-ray generation systems, synchronization, internal safety interlocks, gantry electronics, or service-level software.

The scanner should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or appropriate service evaluation
- Evaluated using Siemens Healthineers documentation and approved test equipment
- Repaired or configured only by qualified personnel

Required functional, radiation-output, and image-quality verification should be completed as applicable before clinical return. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Use a nonpatient test workflow whenever practical instead of repeatedly attempting failed acquisitions on a patient.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Avoid repeated patient attempts, identify exactly where the acquisition sequence stops, verify external conditions and workflow first, and escalate persistent scan-abort conditions for qualified service.

That is successful troubleshooting.
