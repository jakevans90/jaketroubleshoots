---
schemaVersion: 1
title: "Varian TrueBeam Radiation Therapy System - Detector or Acquisition Hardware Is Not Ready"
issueTitle: "Detector or Acquisition Hardware Is Not Ready"
description: "Imaging detector or acquisition hardware does not become ready, is unavailable, or prevents required treatment imaging from proceeding."
assetType: "Radiation Therapy System"
manufacturer: "Varian"
model: "TrueBeam"
slug: "varian-truebeam-detector-or-acquisition-hardware-is-not-ready"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that the TrueBeam imaging system remained not ready and imaging acquisition could not begin."
  cause: "Clinical Engineering found an accessible acquisition workstation cable connection loose at the external interface."
  resolution: "Clinical Engineering secured the connection, restarted the affected workflow, and verified imaging-system readiness and successful functional imaging verification."
helpfulDetails:
  - "Imaging function affected"
  - "Exact readiness message"
  - "Point in workflow where failure occurred"
  - "Detector or imaging-hardware position"
  - "External cable condition"
  - "Workstation status"
  - "System startup status"
  - "Known-good comparison results"
  - "Restart results"
  - "Imaging verification results"
  - "Final device status"
---
## What This Guide Helps With

Imaging detector or acquisition hardware does not become ready, is unavailable, or prevents required treatment imaging from proceeding.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Suspend the Imaging Workflow
Do not proceed with treatment when required imaging or acquisition hardware cannot be relied upon. Move the patient to a safe condition and coordinate with Radiation Oncology before continuing.

**Expected outcome:** No treatment proceeds without the imaging capability required by the clinical workflow.

### 2. Identify the Affected Imaging Component
Determine which imaging or acquisition function is reported unavailable and whether the problem occurs during initialization, positioning, image acquisition, or readiness confirmation. Record all displayed messages.

**Expected outcome:** The affected imaging function and failure point are clearly identified.

### 3. Check External Positioning and Clearance
Inspect externally visible imaging components for correct deployed or parked position as applicable. Verify that accessories, immobilization equipment, cables, or other objects are not blocking movement or positioning.

**Expected outcome:** Imaging hardware has appropriate clearance and no external obstruction is present.

### 4. Inspect Accessible Connections
Check accessible external cables, workstation connections, and supporting communication connections for looseness or visible damage. Do not disconnect internal or restricted-service connections.

**Expected outcome:** Accessible imaging-system connections are secure and intact.

### 5. Verify Supporting Workstations
Confirm that the imaging-related workstation, display, and associated software interface have completed startup and are responsive.

**Expected outcome:** Supporting acquisition systems are powered and operating normally.

### 6. Check System Readiness and Workflow State
Verify that the overall TrueBeam system has completed initialization and is in an appropriate state for imaging. Confirm that no unresolved safety condition, incomplete startup process, or positioning state is preventing readiness.

**Expected outcome:** The system is correctly prepared for acquisition.

### 7. Perform an Approved Restart if Appropriate
If external checks are normal and facility procedures allow, perform the approved restart of the affected user-accessible subsystem or system. Avoid repeated restart attempts if the same failure returns.

**Expected outcome:** Acquisition hardware initializes and reports ready. If so, continue to functional verification.

### 8. Verify Imaging Function
With no patient depending on an unreliable system, perform the appropriate facility-approved imaging verification or quality-control check.

**Expected outcome:** Imaging hardware becomes ready and successfully completes the required verification. Troubleshooting can stop if results are acceptable.

### 9. Remove From Service if Readiness Cannot Be Confirmed
If the detector or acquisition system remains unavailable, intermittently drops out, or fails verification, stop external troubleshooting.

**Expected outcome:** The system is withheld from treatment workflows requiring the affected imaging capability.

## If the Problem Persists

External positioning, connections, system state, supporting workstation operation, and basic workflow conditions have been ruled out. The remaining problem may involve imaging electronics, detector hardware, motion/position feedback, communications, calibration data, software, or another internal service-level subsystem.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or appropriate service evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Any imaging subsystem involved in patient positioning or treatment verification must pass required functional and quality checks before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not bypass required image-guidance steps simply because the treatment-delivery portion of the system appears operational.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Required imaging is part of safe radiation-treatment delivery. Rule out positioning, external connections, workstation status, and workflow conditions first, then escalate persistent readiness failures rather than assuming a specific internal component has failed.

That is successful troubleshooting.
