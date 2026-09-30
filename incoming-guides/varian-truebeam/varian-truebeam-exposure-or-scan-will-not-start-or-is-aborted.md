---
schemaVersion: 1
title: "Varian TrueBeam Radiation Therapy System - Exposure or Scan Will Not Start or Is Aborted"
issueTitle: "Exposure or Scan Will Not Start or Is Aborted"
description: "An imaging exposure, acquisition, scan, or related treatment workflow will not begin or stops unexpectedly after initiation."
assetType: "Radiation Therapy System"
manufacturer: "Varian"
model: "TrueBeam"
slug: "varian-truebeam-exposure-or-scan-will-not-start-or-is-aborted"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that imaging acquisition on the TrueBeam would not start and the workflow remained inhibited."
  cause: "Clinical Engineering found that an imaging component had not reached its required external operating position."
  resolution: "Clinical Engineering corrected the component position and verified successful imaging initiation and completion using an approved functional test."
helpfulDetails:
  - "Function that would not start"
  - "Whether failure occurred before or during acquisition"
  - "Exact displayed message"
  - "Interlock and emergency-stop status"
  - "Gantry, couch, and imaging-hardware positions"
  - "Accessory configuration"
  - "Workstation status"
  - "External connection condition"
  - "Results after correction"
  - "Final functional verification"
---
## What This Guide Helps With

An imaging exposure, acquisition, scan, or related treatment workflow will not begin or stops unexpectedly after initiation.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop the Clinical Workflow
If an exposure, acquisition, or treatment-related operation fails or aborts unexpectedly, do not repeatedly retry while the patient remains dependent on the system. Place the patient in a safe condition and notify the responsible Radiation Oncology team.

**Expected outcome:** Patient safety and treatment continuity are addressed before troubleshooting begins.

### 2. Determine Exactly What Failed
Identify whether the problem involves imaging acquisition, a treatment-related sequence, or another requested exposure/scan function. Record the message shown and whether the process failed before initiation or aborted after starting.

**Expected outcome:** The failed function and stage of failure are known.

### 3. Check System Readiness
Confirm that the TrueBeam has completed startup and that required imaging, positioning, workstation, and safety systems report ready.

**Expected outcome:** All required subsystems are available before another test is attempted.

### 4. Verify Room and Safety Conditions
Check accessible room interlocks, emergency-stop status, doors, and other externally observable safety conditions. Never bypass an interlock to initiate an exposure or treatment sequence.

**Expected outcome:** No external safety condition is inhibiting initiation.

### 5. Verify Patient and Equipment Positioning
Inspect the treatment couch, gantry area, imaging hardware, accessories, and immobilization devices for improper positioning or physical interference.

**Expected outcome:** Required components are positioned correctly and movement or acquisition paths are unobstructed.

### 6. Review User-Accessible Workflow Conditions
Confirm that the requested clinical workflow is properly prepared, required selections are complete, and no obvious user-accessible setting or pending acknowledgment is preventing initiation.

Do not change clinical treatment parameters simply to bypass an inhibit.

**Expected outcome:** The intended procedure is correctly prepared without unauthorized changes.

### 7. Check Supporting Hardware and Communications
Verify that required workstations, imaging components, input devices, and accessible network connections are responsive.

**Expected outcome:** Supporting systems required for the exposure or scan are available and communicating.

### 8. Repeat Only an Appropriate Controlled Test
After correcting an identified external condition, perform an approved non-patient functional verification or other facility-authorized test.

**Expected outcome:** The requested function starts and completes normally. If it does, troubleshooting can stop after required verification.

### 9. Escalate Repeated or Unexplained Aborts
Do not continue repeated exposure or treatment attempts when the system continues aborting or the reason is not clearly understood.

**Expected outcome:** A system with unresolved exposure or acquisition failure remains unavailable for clinical use.

## If the Problem Persists

External readiness conditions, room interlocks, positioning, workflow state, supporting hardware, and accessible communications have been ruled out. Remaining causes may involve internal control systems, imaging hardware, treatment-delivery interlocks, software, safety circuits, or other service-level conditions.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or appropriate service evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Before return to service, the affected acquisition or treatment-related function must pass all required functional, safety, imaging, and treatment-system checks.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Repeatedly clearing an unexplained abort and retrying is not an acceptable substitute for identifying why the system prevented or stopped the requested operation.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

An aborted or inhibited radiation-system workflow must be treated as a safety condition until the cause is understood. Verify external interlocks, positioning, readiness, and communications first, then escalate instead of bypassing or repeatedly retrying unexplained failures.

That is successful troubleshooting.
