---
schemaVersion: 1
title: "Mindray Resona I9 Ultrasound System - Exposure or Scan Will Not Start or Is Aborted"
issueTitle: "Exposure or Scan Will Not Start or Is Aborted"
description: "Use when live ultrasound imaging, acquisition, or a selected study function will not begin or unexpectedly stops."
assetType: "Ultrasound System"
manufacturer: "Mindray"
model: "Resona I9"
slug: "mindray-resona-i9-exposure-or-scan-will-not-start-or-is-aborted"
dateAdded: "2026-10-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported live imaging on the Resona I9 would not start when using the selected transducer."
  cause: "Clinical Engineering found the system remained in a frozen imaging state after the previous examination."
  resolution: "Clinical Engineering restored live imaging using normal controls, verified repeated freeze and unfreeze operation and stable acquisition, and returned the system to service."
helpfulDetails:
  - "Exact acquisition function affected"
  - "Probe in use"
  - "Whether the probe was recognized"
  - "System state when failure occurred"
  - "Exact displayed message"
  - "Known-good probe result"
  - "Accessories connected"
  - "Whether restart changed the condition"
  - "Whether failure is intermittent"
  - "Final functional test result"
  - "Final device status"
---
## What This Guide Helps With

Use when live ultrasound imaging, acquisition, or a selected study function will not begin or unexpectedly stops.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Continuity of Care
Do not continue relying on the system if imaging repeatedly stops or acquisition is unreliable. Use another verified ultrasound system if the examination is clinically necessary.

**Expected outcome:** The patient is examined using reliable equipment while troubleshooting proceeds.

### 2. Clarify What “Scan Will Not Start” Means
Determine whether live B-mode imaging is unavailable, the image remains frozen, a specific imaging mode will not activate, acquisition stops after beginning, or a study-specific function is affected. Ultrasound does not use ionizing-radiation exposure, so document the actual acquisition behavior.

**Expected outcome:** The exact unavailable imaging or acquisition function is identified.

### 3. Verify Transducer Recognition
Confirm the selected compatible transducer is recognized and properly connected. Inspect its external cable, connector, housing, and acoustic surface for visible damage.

**Expected outcome:** The transducer is recognized and suitable for continued testing.

### 4. Check Basic Imaging State
Verify the system is not left in freeze, review, measurement, playback, or another mode that prevents the expected live imaging behavior. Return to normal live imaging using standard controls.

**Expected outcome:** Live imaging starts normally. If it remains stable, proceed to final verification.

### 5. Verify Examination and Probe Selection
Confirm the intended probe and appropriate examination configuration are selected through normal clinical controls. Do not alter protected presets or service-level configuration as a troubleshooting shortcut.

**Expected outcome:** The system is configured for a valid acquisition using the connected probe.

### 6. Test a Known-Good Compatible Probe
If the problem may be probe-related, use a compatible known-good transducer when available.

**Expected outcome:** The known-good probe produces stable live imaging. If the problem follows the original probe, remove that probe from service and stop system troubleshooting after verifying normal system performance.

### 7. Check External Accessories and Connections
Inspect externally connected accessories or peripherals relevant to the failed function. Confirm connectors are seated and cables are undamaged. Disconnect only nonessential accessories when appropriate and permitted.

**Expected outcome:** No external accessory is preventing or interrupting normal acquisition.

### 8. Perform a Controlled Restart
If the problem remains and the system is not supporting active patient care, complete a normal shutdown and restart. Observe whether the issue returns.

**Expected outcome:** Live acquisition initializes and remains available. If the fault does not recur, complete final verification.

### 9. Reproduce the Reported Workflow
Use an appropriate test setup to reproduce the reported action without involving a patient. Verify the scan can start, remain active, freeze/unfreeze normally, and complete the required acquisition sequence.

**Expected outcome:** The reported function operates repeatedly without interruption. If successful, troubleshooting can stop.

## If the Problem Persists

External probe, connection, operating-state, accessory, and basic software-state causes have been ruled out. A persistent failure may involve acquisition electronics, software, configuration, probe-interface hardware, or another internal service-level problem.

Remove the system from service, label it **Out of Service**, and send it for repair or bench evaluation. Use appropriate Mindray service documentation and approved test equipment. Internal repair or protected configuration changes should be completed only by qualified personnel.

Before return to service, verify stable live imaging and the specific acquisition function originally reported as failing.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

If acquisition repeatedly stops during a diagnostic examination, move the patient to a verified system rather than attempting repeated resets during care.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect the patient, identify the actual ultrasound acquisition failure, verify probes, connections, controls, and operating state first, escalate persistent internal faults, and document both the cause and final functional verification.

That is successful troubleshooting.
