---
schemaVersion: 1
title: "Canon Aquilion ONE / PRISM Edition CT Scanner - Detector or Acquisition Hardware Is Not Ready"
issueTitle: "Detector or Acquisition Hardware Is Not Ready"
description: "Addresses detector or acquisition-not-ready conditions caused by startup state, external connections, environment, configuration, or subsystem communication problems."
assetType: "CT Scanner"
manufacturer: "Canon"
model: "Aquilion ONE / PRISM Edition"
slug: "canon-aquilion-one-prism-edition-detector-or-acquisition-hardware-is-not-ready"
dateAdded: "2026-09-24"
taxonomyMode: "reuse"
ccr:
  complaint: "CT staff reported the scanner remained in an acquisition-not-ready state after startup."
  cause: "Clinical Engineering found the condition began after an interrupted startup and no external connection or environmental fault was present."
  resolution: "Performed an approved controlled restart, confirmed acquisition hardware returned to ready status, and completed non-patient functional verification before return to service."
helpfulDetails:
  - "Exact readiness message."
  - "Time in startup sequence when fault appeared."
  - "Whether prior scans were successful."
  - "Recent power or software event."
  - "Accessible connection condition."
  - "Equipment-room temperature or HVAC issue."
  - "Restart results."
  - "QC or functional check results."
  - "Whether fault returned."
  - "Final scanner status."
---
## What This Guide Helps With

Addresses detector or acquisition-not-ready conditions caused by startup state, external connections, environment, configuration, or subsystem communication problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Delay Unreliable Imaging
Do not begin or continue diagnostic scanning when detector or acquisition readiness is uncertain. Move urgent studies to another verified scanner when clinically necessary.

**Expected outcome:** No patient examination depends on unreliable acquisition hardware.

### 2. Confirm the Exact Not-Ready Condition
Determine what staff observed and when it occurred. Record the exact displayed message, indicator, affected protocol, and whether the condition began at startup or after previous successful scans.

**Expected outcome:** The fault is clearly characterized without assuming a detector failure.

### 3. Confirm Complete System Startup
Verify the CT system and operator workstation have completed normal startup and that no subsystem is still initializing.

**Expected outcome:** The scanner has reached the point where acquisition hardware should normally report ready.

If the not-ready condition clears after normal initialization, verify scan readiness and stop.

### 4. Check External Connections and Accessible Hardware
Inspect accessible workstation, acquisition-related, interface, and peripheral connections for looseness or visible damage.

Do not open gantry or detector assemblies.

**Expected outcome:** External connections are intact and secure.

If correcting an approved accessible connection restores ready status, continue to final verification.

### 5. Check Environmental Conditions
Inspect the scanner and equipment-room environment for excessive temperature, blocked ventilation, moisture, unusual odor, or recent HVAC interruption.

**Expected outcome:** Environmental conditions are appropriate for CT operation.

If an environmental condition caused the fault, restore the room to an acceptable operating state and verify stable readiness before use.

### 6. Review Recent Changes
Determine whether the condition began after a software restart, power interruption, service activity, hardware replacement, configuration change, or network/infrastructure event.

Do not modify service configuration based only on suspicion.

**Expected outcome:** Any relevant recent event is identified for troubleshooting or escalation.

### 7. Perform an Approved Controlled Restart
If no unsafe condition exists and approved procedures permit it, perform a normal controlled restart of the system.

Avoid repeated restart cycles when the same not-ready condition immediately returns.

**Expected outcome:** The acquisition system initializes and remains ready.

If it does, proceed to verification.

### 8. Verify Readiness Using Approved System Checks
Use normal operator indications and approved quality or readiness checks to confirm that the acquisition system is available.

Do not perform patient imaging solely to test an unresolved fault.

**Expected outcome:** Detector/acquisition readiness is confirmed without recurring errors.

### 9. Perform Final Functional Verification
Run the appropriate approved non-patient functional or quality-control verification and confirm expected image acquisition, system communication, and ready indications.

**Expected outcome:** Acquisition completes normally and the scanner remains ready.

If achieved, troubleshooting is complete.

### 10. Escalate Persistent Not-Ready Conditions
If acquisition hardware remains unavailable, stop external troubleshooting. Do not attempt detector replacement, internal gantry access, board-level troubleshooting, or restricted calibration procedures.

**Expected outcome:** The unresolved CT system is removed from clinical service and escalated appropriately.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may include detector electronics, acquisition electronics, internal communication paths, internal power, environmental controls, calibration dependencies, or service-level configuration.

The CT scanner should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or qualified service evaluation.
- Evaluated using appropriate Canon documentation and approved CT test equipment.
- Repaired, calibrated, or configured only by qualified personnel.

Required quality-control and image-performance testing must be completed before return to clinical service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not perform diagnostic imaging when the system cannot positively establish acquisition readiness, even if some scanner functions remain available.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Verify startup, external connections, environment, and recent changes before assuming acquisition hardware has failed, and require proper QC before returning the scanner to service.

That is successful troubleshooting.
