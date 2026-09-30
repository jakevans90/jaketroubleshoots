---
schemaVersion: 1
title: "Canon Ultimax-i Fluoroscopy / Interventional System - Exposure or Scan Will Not Start or Is Aborted"
issueTitle: "Exposure or Scan Will Not Start or Is Aborted"
description: "Troubleshoots exposures that will not initiate or terminate unexpectedly because of readiness, controls, interlocks, accessories, settings, or communication."
assetType: "Fluoroscopy / Interventional System"
manufacturer: "Canon"
model: "Ultimax-i"
slug: "canon-ultimax-i-exposure-or-scan-will-not-start-or-is-aborted"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that fluoroscopic exposure on the Canon Ultimax-i would not initiate from the foot control."
  cause: "Clinical Engineering found the external footswitch connector partially disconnected."
  resolution: "Clinical Engineering reseated the footswitch connection and verified reliable exposure initiation and completion using an approved nonclinical test setup."
helpfulDetails:
  - "Exact failure point"
  - "Imaging mode affected"
  - "Displayed message"
  - "Detector readiness"
  - "Exposure-control condition"
  - "Safety or positioning status"
  - "Settings observed"
  - "Whether restart changed behavior"
  - "Nonclinical exposure test result"
  - "Final system status"
---
## What This Guide Helps With

Troubleshoots exposures that will not initiate or terminate unexpectedly because of readiness, controls, interlocks, accessories, settings, or communication.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Before Repeating Exposure Attempts
Do not repeatedly attempt exposures simply to see whether the problem clears. If imaging is required for an ongoing procedure and the Ultimax-i is unreliable, move to an approved alternate imaging plan.

**Expected outcome:** Unnecessary radiation exposure is avoided and clinical continuity is maintained.

### 2. Confirm the Exact Failure
Determine whether exposure never starts, begins and immediately aborts, stops during acquisition, or fails only in a particular imaging mode. Record any displayed message and the point in the workflow where the failure occurs.

**Expected outcome:** The failure is reproducible and clearly defined. If normal imaging resumes, proceed to final verification before returning to use.

### 3. Verify System Readiness
Confirm that the system has completed startup and that the acquisition hardware, detector, positioning components, and workstation show normal readiness.

**Expected outcome:** No upstream not-ready condition is preventing exposure. If resolving a readiness issue restores imaging, stop after verification.

### 4. Check External Exposure Controls
Inspect accessible hand switches, footswitches, control-panel buttons, and external cables used to initiate fluoroscopy or acquisition. Look for damage, contamination, loose connections, or a control that does not respond normally.

Use a known-good approved accessory when available and appropriate.

**Expected outcome:** The external exposure control operates normally. If substitution identifies a defective accessory, replace or remove it from service and verify operation.

### 5. Check Safety Interlocks and Positioning Conditions
Verify that no active emergency stop, collision condition, positioning issue, or other externally apparent safety state is inhibiting exposure. Confirm that required positioning is complete and stable.

Never bypass an interlock.

**Expected outcome:** The system is in a normal condition permitting exposure. If correcting the external condition restores imaging, proceed to verification.

### 6. Review Normal Examination Selections
Check that the intended examination, imaging mode, detector selection, and other operator-accessible settings are appropriate and complete.

Do not alter restricted service or calibration parameters.

**Expected outcome:** The selected imaging workflow is internally consistent and ready to run. If correcting an obvious selection error resolves the issue, verify and stop.

### 7. Check for Communication or Workstation Symptoms
Determine whether the exposure problem occurs alongside frozen controls, delayed responses, detector-not-ready status, communication warnings, or other workstation abnormalities.

If the system software is unstable, perform only an approved normal restart when clinically safe.

**Expected outcome:** The workstation and acquisition system respond normally. If restart restores stable operation, continue to final testing.

### 8. Perform a Nonclinical Functional Test
Using an approved test setup, verify that an exposure or acquisition can be initiated and completed without abnormal termination. Confirm that the system returns to ready status afterward.

**Expected outcome:** Imaging starts, completes, and returns to ready status consistently. If successful, troubleshooting can stop.

## If the Problem Persists

If exposure remains unavailable or repeatedly aborts after readiness, external controls, safety conditions, settings, and communication have been checked, the remaining cause may involve internal generation, acquisition control, detector communication, timing, safety circuitry, configuration, or another service-level condition.

Remove the system from service, label it **Out of Service**, and arrange qualified evaluation using Canon documentation and approved test equipment. Do not bypass exposure interlocks or attempt internal high-voltage troubleshooting.

After repair, complete applicable exposure, image-quality, safety, and functional testing before return to clinical service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Avoid repeated patient exposures during troubleshooting; use approved test objects and nonclinical verification whenever radiation must be generated.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Exposure failures require deliberate troubleshooting that avoids unnecessary radiation. Verify readiness, external controls, safety conditions, settings, and communication before suspecting internal generation or acquisition faults, then escalate unresolved problems and document the final test.

That is successful troubleshooting.
