---
schemaVersion: 1
title: "Canon Ultimax-i Fluoroscopy / Interventional System - Detector or Acquisition Hardware Is Not Ready"
issueTitle: "Detector or Acquisition Hardware Is Not Ready"
description: "Troubleshoots detector or acquisition-not-ready conditions caused by startup state, connections, configuration, accessories, communication, or environmental conditions."
assetType: "Fluoroscopy / Interventional System"
manufacturer: "Canon"
model: "Ultimax-i"
slug: "canon-ultimax-i-detector-or-acquisition-hardware-is-not-ready"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the Canon Ultimax-i acquisition system remained not ready after room startup."
  cause: "Clinical Engineering found an accessible acquisition cable connection not fully seated."
  resolution: "Clinical Engineering secured the connection, restarted the system normally, and verified stable acquisition readiness with a nonclinical functional check."
helpfulDetails:
  - "Exact readiness message"
  - "Time failure occurred"
  - "Components showing not-ready status"
  - "Accessible cable condition"
  - "Accessory recognition"
  - "Visible detector damage"
  - "Restart result"
  - "Nonclinical test result"
  - "Final acquisition status"
---
## What This Guide Helps With

Troubleshoots detector or acquisition-not-ready conditions caused by startup state, connections, configuration, accessories, communication, or environmental conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Procedure
If detector or acquisition readiness becomes unreliable during a procedure, do not repeatedly attempt exposures while the patient depends on the system. Maintain clinical continuity using an approved alternate plan.

**Expected outcome:** Patient care does not depend on unreliable acquisition hardware.

### 2. Confirm the Exact Readiness Condition
Identify what the system reports as unavailable. Note any displayed message, status icon, affected detector or acquisition function, and whether the condition appeared at startup or during use.

**Expected outcome:** The affected acquisition function and timing of the failure are documented. If readiness returns and remains stable, continue to final verification.

### 3. Verify Complete System Startup
Confirm that the workstation, imaging system, displays, detector subsystem, and other externally observable components have finished startup. Allow normal initialization to finish before testing.

**Expected outcome:** The system has completed normal startup and is not simply waiting for initialization. If readiness appears normally, troubleshooting can stop after testing.

### 4. Inspect Accessible Detector and Acquisition Connections
Inspect accessible cables and connectors associated with acquisition hardware for looseness, damage, contamination, strain, or accidental disconnection.

Do not disconnect internal or high-voltage components.

**Expected outcome:** All approved external acquisition connections are secure and undamaged. If reseating an accessible connection restores readiness, verify stability and stop.

### 5. Verify Required Accessories and Configuration
Confirm that required external imaging accessories are present, correctly positioned, recognized, and appropriate for the intended examination. Check normal user-accessible acquisition selections for obvious mismatches.

Do not change restricted service configuration.

**Expected outcome:** Required accessories and normal acquisition selections are appropriate. If correcting the selection restores readiness, verify operation and stop.

### 6. Check for External Damage or Contamination
Inspect externally accessible detector surfaces, housings, connectors, and cables for impact damage, fluid contamination, bent hardware, or other visible abnormalities.

**Expected outcome:** No physical condition is found that would make continued use unsafe. Damaged hardware is removed from service rather than repeatedly tested.

### 7. Perform an Approved Restart if Appropriate
If the system is otherwise stable, use the normal shutdown and startup process to reinitialize the acquisition chain. Avoid repeated uncontrolled power cycling.

**Expected outcome:** Acquisition hardware initializes and reaches a stable ready state. If it does, continue with final verification.

### 8. Verify Acquisition Function Without a Patient
Using the facility's approved test method, confirm that the acquisition system becomes ready and completes a basic nonclinical imaging check. Verify that the ready condition remains stable.

**Expected outcome:** The detector and acquisition chain remain ready and function consistently. If successful, troubleshooting can stop.

## If the Problem Persists

Persistent acquisition-not-ready conditions after external connections, startup state, accessories, and basic configuration have been checked may involve detector electronics, acquisition subsystem communication, internal power, configuration, calibration status, or another service-level condition.

Remove the system from service if imaging readiness is unreliable. Label it **Out of Service** and arrange evaluation using Canon service documentation and approved test equipment. Do not perform unsupported detector disassembly or internal board-level troubleshooting.

Following repair, perform applicable acquisition, image-quality, calibration, and functional verification before clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Do not expose a patient simply to determine whether an intermittently unavailable detector has recovered; verify readiness using an approved nonclinical method first.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Detector readiness should be verified systematically through startup state, connections, accessories, and normal configuration before an internal fault is assumed. Protect the patient from repeated unnecessary attempts, escalate persistent failures, and document the final verification clearly.

That is successful troubleshooting.
