---
schemaVersion: 1
title: "ICU Medical Plum Duo Infusion Pump - Proximal Occlusion Alarm Persists With an Open, Patent Line"
issueTitle: "Proximal Occlusion Alarm Persists With an Open, Patent Line"
description: "Troubleshoots persistent proximal occlusion alarms caused by source restrictions, clamps, kinks, cassette loading, tubing, containers, or sensing problems."
assetType: "Infusion Pump"
manufacturer: "ICU Medical"
model: "Plum Duo"
slug: "icu-medical-plum-duo-proximal-occlusion-alarm-persists-with-an-open-patent-line"
dateAdded: "2026-11-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported repeated proximal occlusion alarms on channel one despite an apparently open line."
  cause: "Clinical Engineering found the upstream tubing partially compressed beneath the cassette door during installation."
  resolution: "Reinstalled the administration set correctly, verified unrestricted tubing, and confirmed normal infusion and alarm behavior on both channels."
helpfulDetails:
  - "Exact alarm message"
  - "Affected channel"
  - "Fluid source condition"
  - "Clamp positions"
  - "Tubing restrictions"
  - "Cassette condition"
  - "Known-good set result"
  - "Alternate source result"
  - "Channel comparison"
  - "Restart result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots persistent proximal occlusion alarms caused by source restrictions, clamps, kinks, cassette loading, tubing, containers, or sensing problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Therapy
If an occlusion alarm repeatedly interrupts a clinically necessary infusion, transfer therapy to another verified pump when appropriate. Do not repeatedly restart therapy without identifying the cause of the alarm.

**Expected outcome:** Patient therapy continues without relying on a pump producing unexplained occlusion alarms.

### 2. Confirm the Exact Alarm
Identify the affected channel and record the exact proximal occlusion message. Reproduce the problem using a controlled test setup rather than a patient-connected line.

**Expected outcome:** The alarm is confirmed under controlled conditions.

### 3. Check the Fluid Source
Inspect the source container for empty or nearly empty volume, closed venting where applicable, collapsed container conditions, improperly inserted spike, or other upstream restrictions.

**Expected outcome:** Fluid can leave the source normally.

If correcting the source restores operation, troubleshooting can stop after repeating the test.

### 4. Inspect All Upstream Clamps and Tubing
Trace the line from the fluid source to the cassette. Verify clamps are open where required and tubing is not kinked, compressed, twisted, trapped under equipment, or bent sharply.

**Expected outcome:** The entire proximal fluid path is visibly unrestricted.

### 5. Inspect Cassette Installation
Remove and reinstall the cassette according to approved handling practices. Inspect for deformation, contamination, or tubing caught improperly in the cassette interface or door.

**Expected outcome:** The cassette seats completely and the tubing path remains unrestricted.

If reseating eliminates the alarm, repeat testing to verify reliability.

### 6. Test With a Known-Good Disposable
Replace the administration set and cassette with a verified compatible known-good set. Use the same fluid source and test conditions.

**Expected outcome:** The known-good set runs without a proximal occlusion alarm.

If the alarm disappears, remove the original disposable from use and document the cause.

### 7. Substitute the Fluid Source
If the alarm continues, use a different appropriate test fluid container to eliminate a source-container or spike-related restriction.

**Expected outcome:** The pump infuses normally from the substitute source.

### 8. Compare Channels
Use the same known-good set and source to compare both channels.

**Expected outcome:** Both channels operate without false proximal occlusion alarms.

If the alarm remains isolated to one channel while the other operates normally under identical conditions, remove the pump from service.

### 9. Restart and Retest
Perform a normal power cycle with no patient connected, allow startup to complete, and repeat the test.

**Expected outcome:** The affected channel operates without a recurring false occlusion alarm.

### 10. Complete Functional Verification
Verify both channels, alarm operation, cassette recognition, and basic flow using approved procedures and test equipment.

**Expected outcome:** The pump delivers consistently and responds appropriately to actual test conditions.

## If the Problem Persists

If the source, clamps, tubing, cassette, disposable, and channel comparison have been verified, a persistent proximal occlusion alarm may reflect a sensing, pressure-detection, mechanical, calibration, or service-level problem.

The pump should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Tested using appropriate manufacturer procedures and approved equipment
- Calibrated or repaired only by qualified personnel
- Fully verified before return to service

Do not alter pressure-related configuration or calibration without authorized documentation and equipment.

## Clinical Use Tip

Treat an unexplained occlusion alarm as potentially real until the entire upstream fluid path has been physically traced and verified.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Occlusion troubleshooting should begin with the complete external fluid path before pressure sensing is suspected. Verify source, tubing, clamps, cassette installation, and disposables, then escalate a repeatable channel-specific failure appropriately.

That is successful troubleshooting.
