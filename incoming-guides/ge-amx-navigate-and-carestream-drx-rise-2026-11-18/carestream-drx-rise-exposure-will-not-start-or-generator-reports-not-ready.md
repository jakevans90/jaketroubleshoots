---
schemaVersion: 1
title: "Carestream DRX-Rise Mobile X-Ray System - Exposure Will Not Start or Generator Reports Not Ready"
issueTitle: "Exposure Will Not Start or Generator Reports Not Ready"
description: "Troubleshoot exposure inhibition, generator-not-ready conditions, detector readiness, exposure controls, interlocks, power, and acquisition setup."
assetType: "Mobile X-Ray System"
manufacturer: "Carestream"
model: "DRX-Rise"
slug: "carestream-drx-rise-exposure-will-not-start-or-generator-reports-not-ready"
dateAdded: "2026-11-18"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported that the DRX-Rise displayed a not-ready condition and would not begin exposure."
  cause: "Clinical Engineering found the wireless detector was powered off and therefore unavailable for acquisition."
  resolution: "Powered and reconnected the detector, confirmed normal ready status, and verified a successful controlled test acquisition."
helpfulDetails:
  - "Exact generator or readiness message"
  - "Stage where exposure stops"
  - "Detector status"
  - "Selected examination"
  - "Exposure-switch condition"
  - "Emergency-stop or interlock state"
  - "Approved substitutions performed"
  - "Whether prep is reached"
  - "Test acquisition result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoot exposure inhibition, generator-not-ready conditions, detector readiness, exposure controls, interlocks, power, and acquisition setup.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Prevent Repeated Unnecessary Exposure Attempts
Stop repeated exposure attempts until the cause is identified. If imaging is clinically urgent, transfer the examination to another verified imaging system.  
Expected outcome: Patient care continues without unnecessary or uncertain radiation exposure.

### 2. Confirm the Reported Exposure Sequence
Determine whether the failure occurs during preparation, ready indication, exposure command, or image acquisition. Record the exact displayed message or status.  
Expected outcome: The specific point in the exposure sequence is identified.

### 3. Verify Normal System Power and Startup
Confirm the DRX-Rise is fully powered and has completed normal startup without unresolved warnings or inhibited conditions.  
Expected outcome: System reaches the normal acquisition-ready state. If restarting through the normal approved workflow clears a temporary condition and the problem does not recur, continue to final verification.

### 4. Confirm Detector Readiness
Verify the intended detector is powered, connected, selected, and available for acquisition. A detector that is offline or not ready may prevent the imaging sequence from completing.  
Expected outcome: Detector displays a normal ready condition.

### 5. Check Examination and Acquisition Setup
Verify a valid examination is selected and required acquisition fields or workflow steps are complete. Do not change clinical technique or configuration merely to bypass an inhibit.  
Expected outcome: The system is properly prepared for a normal authorized exposure.

### 6. Inspect the Exposure Switch and External Cable
Check the hand switch or other normal exposure control for visible damage, contamination, cable strain, loose accessible connection, or intermittent operation.  
Expected outcome: Exposure control is physically intact and responds consistently.

### 7. Check Safety and Motion Interlocks
Verify emergency-stop, collision, parking, or other accessible system conditions are not preventing readiness. Do not bypass any safety interlock.  
Expected outcome: No active safety condition is blocking exposure.

### 8. Test With Approved Nonpatient Conditions
Using appropriate radiation-safety controls and approved test methods, determine whether the system reaches prep/ready and completes a permitted test exposure.  
Expected outcome: System transitions through the exposure sequence normally. If it does, troubleshooting can stop after confirming image acquisition.

### 9. Compare External Accessories When Appropriate
If a removable compatible exposure switch or detector is suspected, use a known-good approved substitute when available. Change only one item at a time.  
Expected outcome: Comparison isolates the problem without bypassing safety features.

### 10. Escalate Persistent Exposure Inhibition
If the generator remains not ready or exposure cannot be initiated after external and workflow checks, remove the system from clinical service.  
Expected outcome: An unreliable X-ray generator is not used on patients.

## If the Problem Persists

Common external causes and normal acquisition conditions have been ruled out. Remaining possibilities include generator hardware, exposure-control circuitry, safety interlocks, detector communication, software, configuration, or other service-level faults.

Remove the DRX-Rise from service, label it **Out of Service**, and send it for repair or bench evaluation. Evaluate the system using appropriate Carestream documentation, radiation-safety procedures, and approved test equipment.

After repair, complete appropriate functional and generator performance verification before returning the system to patient use.

Knowing when to stop rather than bypass an exposure inhibit is proper troubleshooting.

## Clinical Use Tip

Never bypass a readiness or safety inhibit to obtain an X-ray exposure.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Limit unnecessary exposure attempts, verify workflow and detector readiness before suspecting the generator, never bypass safety interlocks, and document both the failure and final verification.

That is successful troubleshooting.
