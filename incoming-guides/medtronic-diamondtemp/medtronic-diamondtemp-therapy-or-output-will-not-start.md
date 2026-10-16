---
schemaVersion: 1
title: "Medtronic DiamondTemp Cardiac Ablation Generator - Therapy or Output Will Not Start"
issueTitle: "Therapy or Output Will Not Start"
description: "Use this guide when the generator powers normally but commanded therapy or RF output does not begin or immediately stops."
assetType: "Cardiac Ablation Generator"
manufacturer: "Medtronic"
model: "DiamondTemp"
slug: "medtronic-diamondtemp-therapy-or-output-will-not-start"
dateAdded: "2026-10-16"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the DiamondTemp generator powered normally but RF therapy would not initiate."
  cause: "Clinical Engineering found the external therapy-control connection was not fully seated."
  resolution: "Clinical Engineering reseated the connection and verified normal activation and output using the approved functional test procedure."
helpfulDetails:
  - "Whether therapy never started or stopped immediately"
  - "Exact displayed message"
  - "Generator readiness state"
  - "Catheter and accessory recognition"
  - "External control condition"
  - "Cable and connector inspection"
  - "Known-good substitution result"
  - "Approved output-test result"
  - "Results before and after correction"
  - "Final device status"
---

## What This Guide Helps With

Use this guide when the generator powers normally but commanded therapy or RF output does not begin or immediately stops.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Procedural Safety
Do not repeatedly attempt therapy when the generator will not produce reliable output. Notify the clinical team and use an approved alternate therapy system if treatment must continue.

**Expected outcome:** The patient is not dependent on an unreliable generator and repeated uncontrolled therapy attempts are avoided.

### 2. Confirm the Exact Output Failure
Determine whether therapy never starts, begins and immediately stops, fails only with one accessory, or is intentionally inhibited by a displayed condition. Record the exact displayed message or indicator.

**Expected outcome:** The failure mode is clearly identified.

### 3. Confirm Normal System Readiness
Verify the generator has completed startup and is not showing an unresolved alarm, fault, or non-ready state. Do not bypass an inhibit or defeat a safety interlock.

**Expected outcome:** The generator indicates that prerequisite conditions are satisfied, or an unresolved condition identifies the next troubleshooting area.

### 4. Check Required External Connections
Inspect the applicable catheter connection, patient cables, accessory interfaces, and any required external therapy-control connections. Confirm they are correctly seated and undamaged.

**Expected outcome:** All required external components are connected and recognized. If correcting a connection restores therapy readiness, proceed to verification.

### 5. Verify Accessory Compatibility and Recognition
Confirm the connected catheter and accessories are approved for the intended system configuration and recognized by the generator.

**Expected outcome:** The system recognizes all required therapy components. An incompatible or unrecognized component is replaced with an approved one.

### 6. Inspect Therapy Activation Controls
Check accessible therapy activation controls, including external controls when part of the approved setup, for physical damage, connection problems, or failure to register normal operation.

**Expected outcome:** The activation control functions consistently. If a known-good approved control restores operation, remove the defective accessory from service.

### 7. Review User-Accessible Therapy Setup
Confirm intended parameters and selections are entered correctly and that no normal procedural prerequisite has been omitted. Do not change clinical therapy parameters merely to force output.

**Expected outcome:** The system is correctly configured for the intended procedure without bypassing safeguards.

### 8. Substitute Known-Good External Components
When clinically appropriate and the system is not connected to a patient for therapy, use approved known-good cables, controls, or compatible accessories to isolate an external component.

**Expected outcome:** Therapy readiness is restored with a known-good component, identifying the suspect accessory.

### 9. Perform Approved Output Verification
Use manufacturer-approved procedures and appropriate test equipment or load where authorized. Do not use a patient as the functional test.

**Expected outcome:** The generator produces controlled output as expected under the approved test condition. The issue is resolved and troubleshooting can stop after required verification.

### 10. Escalate Persistent Output Failure
If all required external components are recognized, setup is correct, and approved output testing still fails, discontinue further external troubleshooting.

**Expected outcome:** The generator is removed from service for qualified repair or manufacturer evaluation.

## If the Problem Persists

External connections, therapy controls, compatible accessories, and normal setup have been ruled out. Remaining causes may include an internal output-stage problem, safety-interlock condition, internal sensing fault, software issue, configuration problem, or other service-level failure.

Remove the generator from service, label it **Out of Service**, and send it for repair or bench evaluation using appropriate manufacturer documentation and approved test equipment. Do not bypass output inhibits or safety protections. Internal repair should be performed only by qualified personnel.

After service, perform all required output, safety, alarm, and functional verification before clinical use. Knowing when not to force therapy is proper troubleshooting.

## Clinical Use Tip

Never bypass an output inhibit or repeatedly trigger RF therapy simply to determine whether a generator will eventually start.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Keep the patient safe, verify readiness and all external therapy prerequisites before suspecting an internal output fault, never defeat safety inhibits, verify output properly after correction, and document exactly what restored operation.

That is successful troubleshooting.
