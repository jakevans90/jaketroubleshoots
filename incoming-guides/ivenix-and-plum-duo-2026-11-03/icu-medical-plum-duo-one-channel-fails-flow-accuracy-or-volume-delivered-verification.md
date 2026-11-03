---
schemaVersion: 1
title: "ICU Medical Plum Duo Infusion Pump - One Channel Fails Flow-Accuracy or Volume-Delivered Verification"
issueTitle: "One Channel Fails Flow-Accuracy or Volume-Delivered Verification"
description: "Troubleshoots a channel-specific delivery discrepancy by verifying test setup, disposables, fluid path, measurement equipment, configuration, and repeatability."
assetType: "Infusion Pump"
manufacturer: "ICU Medical"
model: "Plum Duo"
slug: "icu-medical-plum-duo-one-channel-fails-flow-accuracy-or-volume-delivered-verification"
dateAdded: "2026-11-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Preventive testing found channel two delivering outside the applicable flow-accuracy acceptance criteria while channel one passed."
  cause: "Clinical Engineering found the initial test cassette was deformed and produced inconsistent flow measurements."
  resolution: "Replaced the cassette with a known-good administration set, repeated testing on both channels, and verified delivery within the applicable manufacturer requirements."
helpfulDetails:
  - "Affected channel"
  - "Programmed test condition"
  - "Measured result"
  - "Test equipment used"
  - "Analyzer calibration status"
  - "Disposable condition"
  - "Known-good set result"
  - "Channel comparison"
  - "Repeatability"
  - "Applicable acceptance criteria source"
  - "Final verification result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots a channel-specific delivery discrepancy by verifying test setup, disposables, fluid path, measurement equipment, configuration, and repeatability.

## Step-by-Step Troubleshooting

### 1. Remove the Pump From Patient Use
A channel that may be delivering inaccurately must not be used for patient therapy. Transfer any active infusion to another verified pump and label the suspect device appropriately during evaluation.

**Expected outcome:** No patient depends on the channel under investigation.

### 2. Confirm the Reported Accuracy Failure
Review the original test method, programmed values, measured volume, affected channel, disposable used, and test equipment. Repeat the verification using an approved test procedure.

**Expected outcome:** The accuracy failure is either reproduced or shown to have resulted from the original setup.

### 3. Verify the Analyzer or Measurement Setup
Confirm the flow analyzer, gravimetric setup, collection device, tubing arrangement, and other test equipment are appropriate, correctly configured, and within current verification or calibration requirements.

**Expected outcome:** The measurement system is suitable for determining pump performance.

If correcting the test setup brings results within the applicable manufacturer criteria, troubleshooting can stop after repeat verification.

### 4. Inspect the Administration Set
Check the cassette and tubing for kinks, stretching, deformation, trapped air, partially closed clamps, leaks, or unusual resistance.

**Expected outcome:** The disposable fluid path is intact and unrestricted.

### 5. Use a Known-Good Disposable
Repeat testing with a new or verified compatible administration set.

**Expected outcome:** The measured result is repeatable with a known-good disposable.

If the original disposable caused the discrepancy and the replacement passes, document the disposable-related cause.

### 6. Verify Fluid Source and Test Conditions
Confirm adequate source fluid, stable positioning, appropriate tubing routing, and consistent test conditions between channels. Avoid introducing unnecessary variables when comparing results.

**Expected outcome:** Both channels are tested under equivalent conditions.

### 7. Compare Both Channels
Using the same verified test equipment, fluid source, and disposable setup, test each channel independently.

**Expected outcome:** Both channels meet the applicable manufacturer performance requirements.

If one channel repeatedly fails while the other passes under identical conditions, remove the pump from service.

### 8. Repeat the Test
Repeat the failed channel verification to determine whether the result is consistent or intermittent. Do not average an obvious failure into an acceptable result.

**Expected outcome:** Results are stable and repeatable.

An intermittent out-of-tolerance condition is still a failure requiring further evaluation.

### 9. Check for External Mechanical Interference
Verify tubing is not being compressed by the door, stand, clamp, analyzer fixture, or other equipment. Confirm the cassette is fully seated.

**Expected outcome:** No external mechanical condition is altering fluid delivery.

### 10. Complete Final Verification
If the channel subsequently passes, perform the required complete flow and safety verification according to approved service procedures before return to clinical use.

**Expected outcome:** Both channels meet applicable performance requirements consistently.

## If the Problem Persists

If the test equipment, disposable, fluid source, tubing, cassette seating, and repeat measurements have been verified and one channel continues to fail accuracy or delivered-volume testing, common external causes have been ruled out.

Possible remaining categories include pumping-mechanism wear, channel calibration, internal mechanical condition, sensing, or another service-level fault.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for bench repair or evaluation
- Evaluated under approved ICU Medical service procedures
- Calibrated or repaired only by qualified personnel using approved test equipment
- Subjected to full return-to-service performance testing

Do not attempt informal calibration adjustments or compensate by altering programmed values.

## Clinical Use Tip

A channel that fails delivery verification should be treated as unreliable even when the second channel passes.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Accuracy failures require disciplined verification of the measurement setup and disposable before an internal pump problem is assumed. A repeatable channel-specific failure warrants removal from service, qualified repair, and complete performance verification.

That is successful troubleshooting.
