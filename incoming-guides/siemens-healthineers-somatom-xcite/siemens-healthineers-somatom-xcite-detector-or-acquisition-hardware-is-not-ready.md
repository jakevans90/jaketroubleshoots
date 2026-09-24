---
schemaVersion: 1
title: "Siemens Healthineers SOMATOM X.cite CT Scanner - Detector or Acquisition Hardware Is Not Ready"
issueTitle: "Detector or Acquisition Hardware Is Not Ready"
description: "Use this guide when the scanner reports acquisition hardware unavailable, not ready, initializing, or otherwise prevents normal data acquisition."
assetType: "CT Scanner"
manufacturer: "Siemens Healthineers"
model: "SOMATOM X.cite"
slug: "siemens-healthineers-somatom-xcite-detector-or-acquisition-hardware-is-not-ready"
dateAdded: "2026-09-24"
taxonomyMode: "reuse"
ccr:
  complaint: "CT staff reported that the SOMATOM X.cite remained not ready for acquisition after patient setup."
  cause: "Clinical Engineering found the scanner had not completed normal initialization following a recent system restart."
  resolution: "The approved startup process was completed, a nonpatient acquisition and reconstruction were verified, and the scanner was returned to service."
helpfulDetails:
  - "Exact readiness or system message"
  - "Point in workflow where the issue occurred"
  - "Startup status"
  - "Relevant accessible connection condition"
  - "Whether the problem followed a restart or outage"
  - "Results of an approved restart"
  - "Nonpatient acquisition result"
  - "Reconstruction result"
  - "Persistent warnings"
  - "Final scanner status"
---
## What This Guide Helps With

Use this guide when the scanner reports acquisition hardware unavailable, not ready, initializing, or otherwise prevents normal data acquisition.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop the Examination
Do not continue an examination when the system reports that required acquisition hardware is not ready. Safely remove the patient when appropriate and use another scanner for urgent imaging.  
**Expected outcome:** No patient examination depends on unreliable acquisition hardware.

### 2. Confirm the Exact Readiness Condition
Record the exact displayed message and determine when it occurs: startup, patient setup, protocol selection, scan preparation, or immediately before acquisition.  
**Expected outcome:** The failure point and affected function are clearly documented.

### 3. Verify the Scanner Completed Normal Startup
Confirm that the operator workstation, gantry, and related system components have completed their normal initialization and that no broader startup condition remains active.  
**Expected outcome:** The scanner is otherwise operational and the problem is isolated to acquisition readiness.

### 4. Inspect Accessible External Connections and Accessories
Check accessible external connections for operator equipment and any relevant removable accessories. Look for loose cables, damaged connectors, or improperly seated components without opening gantry covers.  
**Expected outcome:** External connections are secure and free of visible damage.

### 5. Check System Status and Required Preparatory Conditions
Review the normal operator interface for system-status messages indicating that the scanner is waiting for initialization, calibration, temperature stabilization, or another permitted preparation step. Do not enter restricted service menus.  
**Expected outcome:** No unresolved external or normal operational condition is preventing readiness.

### 6. Perform an Approved Restart if Appropriate
If the system is stable and there is no evidence of overheating, electrical fault, or mechanical damage, perform the normal approved restart sequence once.  
**Expected outcome:** Acquisition hardware initializes successfully and the scanner reports ready. If it does, continue to functional verification and stop troubleshooting.

### 7. Perform a Nonpatient Acquisition Check
Use an approved nonpatient workflow or applicable quality-control procedure to confirm that the scanner can prepare for and complete an acquisition.  
**Expected outcome:** Acquisition begins and completes normally without recurring hardware-readiness messages.

### 8. Confirm Image Reconstruction and System Readiness
Verify that acquired data reconstructs normally and that no persistent system warning remains after the test.  
**Expected outcome:** The acquisition chain functions normally from scan preparation through image creation.

### 9. Escalate Persistent Acquisition Hardware Faults
If the scanner repeatedly reports that acquisition hardware is not ready or cannot complete the approved test, stop troubleshooting.  
**Expected outcome:** The unit remains out of clinical service pending qualified evaluation.

## If the Problem Persists

External connections, startup state, ordinary preparation conditions, and a normal restart have been evaluated. The remaining cause may involve detector electronics, acquisition-control hardware, gantry subsystems, synchronization, internal communications, or other service-level components.

The scanner should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or service evaluation
- Evaluated using current Siemens Healthineers service documentation and approved test equipment
- Repaired, calibrated, or configured only by qualified personnel

Complete required functional and image-quality verification before return to patient imaging. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not treat an acquisition-hardware readiness message as a harmless software delay when the scanner cannot reliably complete a test acquisition.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Confirm patient safety, complete startup, external connections, and normal preparation conditions before suspecting detector or acquisition hardware failure, then verify with an approved test or escalate for service.

That is successful troubleshooting.
