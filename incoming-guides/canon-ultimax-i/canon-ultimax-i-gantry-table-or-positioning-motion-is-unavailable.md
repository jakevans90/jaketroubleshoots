---
schemaVersion: 1
title: "Canon Ultimax-i Fluoroscopy / Interventional System - Gantry, Table, or Positioning Motion Is Unavailable"
issueTitle: "Gantry, Table, or Positioning Motion Is Unavailable"
description: "Troubleshoots unavailable or inhibited positioning caused by obstructions, controls, interlocks, positioning limits, connections, or system readiness."
assetType: "Fluoroscopy / Interventional System"
manufacturer: "Canon"
model: "Ultimax-i"
slug: "canon-ultimax-i-gantry-table-or-positioning-motion-is-unavailable"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that table positioning on the Canon Ultimax-i was unavailable during room setup."
  cause: "Clinical Engineering found an equipment cable routed into the table travel area and interfering with movement."
  resolution: "Clinical Engineering rerouted the cable, confirmed the travel path was clear, and verified smooth table movement using normal controls."
helpfulDetails:
  - "Specific motion affected"
  - "Direction or position where motion stops"
  - "Emergency-stop status"
  - "Objects or cables in travel path"
  - "Control station tested"
  - "External control and cable condition"
  - "Abnormal noise or binding"
  - "Whether motion was intermittent"
  - "Final positioning test result"
---
## What This Guide Helps With

Troubleshoots unavailable or inhibited positioning caused by obstructions, controls, interlocks, positioning limits, connections, or system readiness.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Before Testing Motion
Stop attempted movement if the patient, staff, lines, accessories, or procedural equipment could be trapped, pulled, struck, or displaced. If the system cannot be positioned reliably during a procedure, transition to an alternate safe workflow.

Never troubleshoot unpredictable movement while a patient depends on the system.

**Expected outcome:** The patient and surrounding equipment are protected from unintended motion. Continue only when movement can be tested safely.

### 2. Confirm Which Motion Is Affected
Determine whether the problem affects the table, imaging assembly, specific directional movement, or all positioning functions. Confirm whether movement is completely unavailable, intermittent, limited, or stops at a particular position.

**Expected outcome:** The affected motion function and exact symptom are identified. If the system operates normally during testing, verify all required motion functions and stop.

### 3. Inspect for Physical Obstructions
Check around and beneath the table and imaging system for stools, cables, foot controls, carts, patient lines, drapes, accessories, or other objects interfering with travel.

Do not force movement against resistance.

**Expected outcome:** The full intended travel path is clear. If removal of an obstruction restores motion, verify safe operation and stop.

### 4. Check Emergency Stops and Safety Conditions
Verify that emergency-stop controls and accessible motion-safety controls are in their normal states. Confirm that no obvious collision, safety, or positioning condition is preventing movement.

Only reset a safety control after determining why it was activated.

**Expected outcome:** No active external safety condition is inhibiting movement. If motion returns after resolving the condition, perform functional verification.

### 5. Verify Controls and Operating State
Confirm that the system has completed startup and is in an operating state that permits positioning. Test the appropriate operator-accessible positioning controls and note whether one control station works while another does not.

**Expected outcome:** Motion commands are accepted from functioning controls. If a single external control was the problem and normal motion is restored, troubleshooting can stop after verification.

### 6. Inspect Accessible Control Connections
Inspect accessible footswitches, hand controls, pendants, and associated external cables or connectors when relevant. Look for damage, pinching, contamination, looseness, or accidental disconnection.

Use an approved known-good accessory only when compatibility is established.

**Expected outcome:** External positioning controls and cables are intact and connected. If a known-good compatible control restores operation, identify the defective accessory and stop after testing.

### 7. Check Position and Travel Conditions
Determine whether the system is already at a normal travel boundary or in a position where a different movement must occur before the requested movement becomes available.

Do not override software or mechanical limits.

**Expected outcome:** The requested motion is being attempted within normal accessible positioning conditions. If repositioning within normal controls restores motion, verify repeatability and stop.

### 8. Perform Final Motion Verification
Without a patient, exercise the affected positioning function through an appropriate safe range using normal controls. Verify smooth response, predictable stopping, and absence of abnormal noise, binding, or repeated interruption.

**Expected outcome:** Positioning operates smoothly and consistently. If successful, troubleshooting can stop.

## If the Problem Persists

If positioning remains unavailable after external controls, obstructions, safety conditions, connections, and operating state have been verified, the problem may involve internal motion control, drive components, position sensing, safety circuitry, configuration, or subsystem communication.

Remove the system from service when required positioning cannot be relied upon. Label it **Out of Service** and arrange service evaluation using Canon documentation and approved test equipment. Internal motion-system adjustments or repairs should be performed only by qualified personnel.

Before return to service, verify required movement functions, safety stops, positioning response, and overall system operation.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Secure patient lines, catheters, tubes, and procedural accessories before any table or imaging-system movement.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Positioning problems should be approached from the outside in: protect the patient, clear the travel path, verify safety controls and accessories, and confirm normal operation before assuming an internal motion failure. Escalate unreliable movement and document the complete findings.

That is successful troubleshooting.
