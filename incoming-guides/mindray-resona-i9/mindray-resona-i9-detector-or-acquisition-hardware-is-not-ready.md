---
schemaVersion: 1
title: "Mindray Resona I9 Ultrasound System - Detector or Acquisition Hardware Is Not Ready"
issueTitle: "Detector or Acquisition Hardware Is Not Ready"
description: "Use when a transducer is not recognized, acquisition is unavailable, or the system cannot establish a usable live imaging path."
assetType: "Ultrasound System"
manufacturer: "Mindray"
model: "Resona I9"
slug: "mindray-resona-i9-detector-or-acquisition-hardware-is-not-ready"
dateAdded: "2026-10-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported the Resona I9 would not recognize the transducer required for an examination."
  cause: "Clinical Engineering found the reported transducer was not fully seated in its external connector."
  resolution: "Clinical Engineering reconnected the transducer correctly, verified consistent recognition and stable live imaging, and returned the system to service."
helpfulDetails:
  - "Probe type involved"
  - "Whether one or all probes are affected"
  - "Exact displayed message"
  - "Probe cable and housing condition"
  - "Connector condition"
  - "Known-good probe results"
  - "Connections tested"
  - "Whether recognition is intermittent"
  - "Live imaging result"
  - "Results after restart"
  - "Final device and probe status"
---
## What This Guide Helps With

Use when a transducer is not recognized, acquisition is unavailable, or the system cannot establish a usable live imaging path.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Diagnostic Capability
Do not continue a diagnostic examination if the required transducer or acquisition path is unreliable. Move the patient to another verified ultrasound system when necessary.

**Expected outcome:** Diagnostic imaging continues on reliable equipment while the affected system is evaluated.

### 2. Confirm the Exact Acquisition Problem
Determine whether no probe is recognized, one specific probe is unavailable, all probes are unavailable, live imaging does not begin, or acquisition becomes unavailable intermittently. Record any displayed message.

**Expected outcome:** The fault is narrowed to a particular probe, connector, operating condition, or system-wide acquisition problem.

### 3. Inspect the Selected Transducer
Remove the probe from patient use and inspect the accessible cable, strain relief, connector, housing, and acoustic surface for contamination, cuts, exposed conductors, cracks, impact damage, or other abnormalities. Follow infection-control requirements while handling probes.

**Expected outcome:** The probe has no visible condition that would make continued use unsafe. Damaged probes are removed from service rather than further tested clinically.

### 4. Verify Probe Connection
Confirm the transducer connector is correctly seated and secured using the normal connection method. Do not force a connector or manipulate damaged contacts.

**Expected outcome:** The transducer is fully connected and recognized by the system. If recognition returns and remains stable, continue to functional verification.

### 5. Test Another Compatible Known-Good Probe
When available and permitted, connect a compatible known-good probe and check whether it is recognized and can produce live imaging.

**Expected outcome:** A known-good probe operates normally. If only the original probe fails, isolate that probe from service and stop system troubleshooting after verifying the ultrasound system with the known-good probe.

### 6. Compare Available Probe Connections
If appropriate for the installed configuration, determine whether the problem follows the probe or remains associated with a particular accessible connection. Do not repeatedly connect questionable equipment or access internal connectors.

**Expected outcome:** The problem is isolated to an external probe/accessory or shown to affect the system more broadly.

### 7. Verify Imaging Selection and Controls
Confirm an appropriate recognized transducer and examination configuration are selected and the system is not simply frozen, paused, or left in a state that prevents live imaging. Avoid changing protected configuration or service settings.

**Expected outcome:** Normal live acquisition becomes available through standard operator controls.

### 8. Perform a Controlled Restart if Appropriate
If probes and connections appear normal but acquisition hardware remains unavailable, perform a normal system shutdown and restart when patient care is not dependent on the unit.

**Expected outcome:** The acquisition path initializes normally after restart. If it does, verify continued stable operation before returning the unit to service.

### 9. Perform Final Functional Verification
Using a compatible verified probe, confirm recognition, stable live imaging, normal control response, and consistent acquisition without connection-related interruption.

**Expected outcome:** The Resona I9 provides stable live imaging from the tested probe. If successful, troubleshooting can stop.

## If the Problem Persists

External probe condition, connection, probe selection, and known-good substitution have been evaluated. A persistent problem may involve the acquisition electronics, probe interface, software, configuration, or another internal service-level condition.

Remove the affected equipment from service. If the problem is isolated to a transducer, label that transducer **Out of Service** while retaining the ultrasound system only if its remaining configuration is verified safe and clinically appropriate. If acquisition is broadly unreliable, remove the entire system from service.

Send the affected equipment for repair or bench evaluation using appropriate Mindray documentation and approved test equipment. Internal repair or configuration should be performed only by qualified personnel.

Complete applicable probe safety checks and functional imaging verification before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A transducer with visible cable, connector, housing, or acoustic-surface damage should be removed from patient use even if it still produces an image.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect diagnostic reliability, inspect the probe and connection before assuming an acquisition failure, use known-good substitution to isolate the problem, verify stable imaging, escalate internal faults appropriately, and document the result clearly.

That is successful troubleshooting.
