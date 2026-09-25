---
schemaVersion: 1
title: "United Imaging uMR 790 MRI System - Calibration or Quality-Control Test Fails"
issueTitle: "Calibration or Quality-Control Test Fails"
description: "Troubleshoots failed MRI calibration or quality-control testing caused by setup, phantom positioning, accessories, system readiness, environment, or repeatable equipment performance problems."
assetType: "MRI System"
manufacturer: "United Imaging"
model: "uMR 790"
slug: "united-imaging-umr-790-calibration-or-quality-control-test-fails"
dateAdded: "2026-09-25"
taxonomyMode: "reuse"
ccr:
  complaint: "MRI staff reported that the uMR 790 routine quality-control test failed during the scheduled performance check."
  cause: "Clinical Engineering found the QC phantom had been positioned incorrectly within the selected coil."
  resolution: "The phantom was repositioned according to the approved setup, the QC test was repeated successfully, and the passing result was documented."
helpfulDetails:
  - "Test that failed"
  - "Exact displayed message"
  - "Phantom condition"
  - "Phantom position"
  - "Coil used"
  - "External connection status"
  - "Environmental changes"
  - "Previous QC result"
  - "Repeat-test result"
  - "Final service status"
---
## What This Guide Helps With

Troubleshoots failed MRI calibration or quality-control testing caused by setup, phantom positioning, accessories, system readiness, environment, or repeatable equipment performance problems.

## Step-by-Step Troubleshooting

### 1. Remove Questionable Imaging Performance From Clinical Use
A failed calibration or quality-control test may indicate unreliable imaging performance.

If the failed test affects the ability to establish acceptable system performance, do not continue routine patient imaging until the failure is understood and resolved according to site policy.

**Expected outcome:** Potentially unreliable imaging is not used clinically while the failed test is investigated.

### 2. Confirm Which Test Failed
Document:
- Name or type of test
- Stage of the test where failure occurred
- Displayed message
- Whether the test previously passed
- Whether failure is repeatable

Do not invent or apply unofficial acceptance limits.

**Expected outcome:** The specific failed test and observed result are accurately identified.

### 3. Verify the Correct Test Setup
Confirm the approved phantom, coil, accessory, positioning method, and normal test workflow are correct.

Inspect the phantom and accessories for visible damage, leakage, deterioration, or improper setup.

**Expected outcome:** The test is configured according to the approved procedure. If correcting setup results in a passing test, document and stop.

### 4. Verify Phantom Positioning
Confirm the test object is positioned consistently and securely according to the site's approved QC method.

Incorrect placement can create a false failure.

**Expected outcome:** Phantom position is reproducible and appropriate. If repositioning restores an acceptable result, repeat the verification and stop.

### 5. Inspect Coil and External Connections
Check the coil and accessible acquisition connections used for QC.

Look for:
- Loose connections
- Cable damage
- Contamination
- Intermittent recognition
- Incorrect coil selection

**Expected outcome:** Acquisition accessories are correctly connected and stable. If correcting an external connection allows the test to pass, document the result and stop.

### 6. Confirm System Readiness and Environmental Stability
Verify the MRI system has completed startup and no temperature, cooling, facility-power, or other active condition is present.

Consider whether construction, electrical work, or equipment changes have recently occurred nearby.

**Expected outcome:** The scanner and environment are stable enough for valid testing.

### 7. Repeat the Test Once Under Controlled Conditions
After correcting any identified external cause, repeat the approved test using the same documented procedure.

Avoid repeated calibration attempts intended only to obtain a passing result.

**Expected outcome:** The test passes consistently. If it does, troubleshooting can stop after documentation.

### 8. Compare With a Known-Good Accessory When Appropriate
If the failed test uses a removable coil or accessory, repeat using a known-good compatible component if permitted.

**Expected outcome:** If the failure follows one accessory, remove that accessory from service. If the failure remains across known-good accessories, escalate the scanner.

### 9. Preserve Failed Results
Retain or document failed QC output as required by local procedure. Record what changed between the failed and successful attempts.

**Expected outcome:** Service personnel have a clear record of the failure and troubleshooting already performed.

### 10. Escalate a Repeatable QC Failure
If setup, positioning, accessories, system readiness, and environment are correct but the test continues to fail, stop external troubleshooting.

**Expected outcome:** The system remains out of service pending qualified evaluation.

## If the Problem Persists

Common setup and accessory causes have been ruled out. Remaining causes may involve calibration data, RF performance, gradients, magnet conditions, reconstruction, internal acquisition hardware, environmental interference, or other service-level categories.

The device should be:
- Removed from service
- Labeled **Out of Service**
- Sent for repair or service evaluation
- Evaluated using United Imaging documentation and approved MRI test equipment
- Repaired, adjusted, calibrated, or configured only by qualified personnel

Do not alter calibration values or protected configuration without authorization.

Knowing when to stop external troubleshooting is proper troubleshooting. Return the scanner to clinical service only after required calibration and QC verification successfully meet the applicable approved criteria.

## Clinical Use Tip

Do not dismiss a repeatable QC failure simply because routine images appear acceptable; objective performance testing exists to detect problems that may not be immediately obvious.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

QC troubleshooting should protect imaging reliability by first validating the test itself, then isolating accessories and environmental conditions before assuming an internal system defect. Repeatable failures deserve escalation and clear documentation.

That is successful troubleshooting.
