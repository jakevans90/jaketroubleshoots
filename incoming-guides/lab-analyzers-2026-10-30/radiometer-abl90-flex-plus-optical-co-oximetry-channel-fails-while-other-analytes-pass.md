---
schemaVersion: 1
title: "Radiometer ABL90 FLEX PLUS Blood Gas Analyzer - Optical/Co-Oximetry Channel Fails While Other Analytes Pass"
issueTitle: "Optical/Co-Oximetry Channel Fails While Other Analytes Pass"
description: "Troubleshoots isolated optical or co-oximetry failures involving sample quality, consumables, optical contamination, configuration, or analyzer readiness."
assetType: "Blood Gas Analyzer"
manufacturer: "Radiometer"
model: "ABL90 FLEX PLUS"
slug: "radiometer-abl90-flex-plus-optical-co-oximetry-channel-fails-while-other-analytes-pass"
dateAdded: "2026-10-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that co-oximetry results were unavailable while blood-gas and electrolyte measurements continued to report."
  cause: "Clinical Engineering found the recently installed analytical consumable was not fully seated and the analyzer had not established normal optical-channel operation."
  resolution: "Correctly reseated the approved consumable, completed analyzer readiness checks and quality-control verification, confirmed all required parameters reported normally, and returned the unit to service."
helpfulDetails:
  - "Exact missing or flagged analytes"
  - "Exact analyzer message"
  - "Whether other channels passed"
  - "Sample condition and mixing"
  - "Consumable status and recent replacements"
  - "Whether the issue began after maintenance or power interruption"
  - "Accessible contamination observed"
  - "Quality-control results"
  - "Number of controlled tests performed"
  - "Results before and after correction"
  - "Final analyzer status"
---

## What This Guide Helps With

Troubleshoots isolated optical or co-oximetry failures involving sample quality, consumables, optical contamination, configuration, or analyzer readiness.

## Step-by-Step Troubleshooting

### 1. Protect Patient Testing and Confirm an Alternate Testing Path

Do not rely on incomplete analyzer results when the required co-oximetry parameters are unavailable or unreliable. Route affected patient testing to another verified analyzer or approved laboratory method.

Do not continue reporting unaffected parameters if laboratory policy requires the complete panel for the clinical decision.

**Expected outcome:** Required patient testing continues through a verified alternate method. If the clinical workflow is safely maintained, troubleshooting can proceed without delaying care.

### 2. Confirm the Exact Reported Failure

Determine which optical or co-oximetry results are missing, suppressed, flagged, or failing while other measurements remain available.

Confirm whether the issue occurs on every sample or only certain samples. Record the exact analyzer message or status rather than describing the condition only as a “co-ox failure.”

**Expected outcome:** The failure is confirmed as isolated to the optical/co-oximetry portion of testing. If the reported failure cannot be reproduced and a controlled test passes normally, troubleshooting can stop after verification.

### 3. Verify Analyzer Readiness

Confirm the ABL90 FLEX PLUS has completed startup and is in its normal ready state. Review visible analyzer status for consumable conditions, required maintenance, quality-control restrictions, or other conditions that could selectively limit results.

Do not bypass analyzer lockouts or alter restricted configuration.

**Expected outcome:** The analyzer is ready for testing with no active external condition intentionally disabling the optical measurement. If clearing a legitimate readiness condition restores the channel, troubleshooting can stop.

### 4. Evaluate Sample Quality

Review whether the affected samples contain visible air bubbles, clots, incomplete mixing, unusual sample volume, or other collection problems.

Compare performance using appropriate known-good quality-control or test material rather than repeatedly testing questionable patient specimens.

**Expected outcome:** The optical failure is reproduced with suitable test material rather than being limited to a compromised specimen. If proper sample preparation eliminates the issue, troubleshooting can stop.

### 5. Verify Consumable Installation and Status

Inspect accessible consumables associated with the current analytical setup. Confirm they are correctly installed, fully seated, recognized by the analyzer, and not visibly damaged or leaking.

If the issue began immediately after a consumable change, pay particular attention to installation, seating, packaging remnants, and analyzer recognition.

Do not remove or reinstall consumables repeatedly without an identified reason.

**Expected outcome:** Required consumables are installed correctly and recognized. If reseating or replacing an improperly installed approved consumable restores optical measurements, troubleshooting can stop after verification.

### 6. Inspect Accessible Optical and Sample Interfaces

Inspect only externally accessible areas associated with sample presentation and optical measurement for contamination, dried sample residue, condensation, or damage.

Use only manufacturer-approved cleaning procedures applicable to Clinical Engineering.

Do not open sealed optical assemblies or attempt to clean internal optics without authorized service instructions.

**Expected outcome:** Accessible interfaces are clean and free of contamination or damage. If approved cleaning restores the co-oximetry channel, troubleshooting can stop.

### 7. Review Recent Events or Changes

Determine whether the issue began after:

- Sensor-cassette replacement
- Other consumable replacement
- Cleaning
- Power interruption
- Analyzer relocation
- Configuration change
- Software or service activity

This helps distinguish an isolated measurement failure from a change-related condition.

**Expected outcome:** Any recent change is identified and verified for correct completion. If correcting an incomplete external installation or approved configuration issue restores operation, troubleshooting can stop.

### 8. Run Approved Quality-Control or Verification Material

Use appropriate approved material to determine whether the optical/co-oximetry channel can produce acceptable results while the other analyzer channels continue to operate normally.

Do not use patient samples as repeated troubleshooting material.

**Expected outcome:** The optical channel produces normal results using approved verification material. If the controlled test passes consistently, the issue may have been sample-specific and troubleshooting can stop after documentation.

### 9. Compare the Pattern Across Multiple Controlled Tests

If the optical channel continues to fail, determine whether the same parameters fail consistently and whether the failure is isolated from pH, blood gas, electrolyte, and other available measurements.

A consistent isolated failure after valid samples and consumables are confirmed supports escalation rather than continued external intervention.

**Expected outcome:** The failure pattern is clearly established. If the optical channel repeatedly fails while other analyzer functions remain normal, remove the analyzer from use for tests requiring those measurements and escalate.

### 10. Perform Final Functional Verification

After any corrective action, run the appropriate approved verification or quality-control material and confirm the optical/co-oximetry results are available along with the remaining analyzer parameters.

Confirm the analyzer returns to a normal ready state without channel-specific warnings.

**Expected outcome:** Optical/co-oximetry and other required measurements operate normally and repeatably. When this occurs, troubleshooting can stop and the analyzer may be returned to service according to facility policy.

## If the Problem Persists

If suitable samples, consumables, accessible contamination, analyzer readiness, and recent external changes have been ruled out, the issue may involve the internal optical measurement system, light source, detector path, internal sample interface, electronics, or service-level configuration.

The analyzer should be:

- Removed from service when the required co-oximetry measurements cannot be relied upon
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate Radiometer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not disassemble the optical system, attempt board-level repair, or bypass analytical restrictions.

Following repair, complete all applicable analyzer checks, quality-control verification, and facility-required return-to-service testing before clinical use.

Stopping after external and consumable causes are excluded is appropriate troubleshooting when an analytical channel remains unreliable.

## Clinical Use Tip

Do not assume a partial blood-gas panel is clinically interchangeable with the requested panel when co-oximetry measurements are missing.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

An isolated analytical-channel failure should be approached by protecting patient testing, confirming sample and consumable conditions, and verifying the failure with controlled material before suspecting internal optics. Escalate persistent analytical failures and document the complete verification path.

That is successful troubleshooting.
