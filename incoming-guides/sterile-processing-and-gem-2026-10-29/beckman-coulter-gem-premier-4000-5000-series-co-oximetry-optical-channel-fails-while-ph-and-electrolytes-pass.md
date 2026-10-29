---
schemaVersion: 1
title: "Beckman Coulter GEM Premier 4000 / 5000 Series Blood Gas Analyzer - Co-Oximetry Optical Channel Fails While pH and Electrolytes Pass"
issueTitle: "Co-Oximetry Optical Channel Fails While pH and Electrolytes Pass"
description: "Troubleshoots isolated co-oximetry failures when other measurements remain functional, focusing on sample quality, GEM PAK condition, configuration, and external causes."
assetType: "Blood Gas Analyzer"
manufacturer: "Beckman Coulter"
model: "GEM Premier 4000 / 5000 Series"
slug: "beckman-coulter-gem-premier-4000-5000-series-co-oximetry-optical-channel-fails-while-ph-and-electrolytes-pass"
dateAdded: "2026-10-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory reported that co-oximetry analytes were unavailable while pH and electrolyte testing continued to pass."
  cause: "Clinical Engineering found the installed GEM PAK was not operating correctly for the co-oximetry measurement function while the remaining channels continued to verify normally."
  resolution: "GEM PAK was replaced using the approved process, required QC passed for co-oximetry and other measurements, and the analyzer was returned to service."
helpfulDetails:
  - "Exact missing or flagged co-oximetry analytes"
  - "Whether pH, blood gases, and electrolytes passed"
  - "Patient sample versus QC behavior"
  - "GEM PAK identification and status"
  - "GEM PAK seating or visible condition"
  - "Recent GEM PAK replacement"
  - "Analyzer messages or indicators"
  - "Recent configuration or software changes"
  - "Results before and after corrective action"
  - "QC verification results"
  - "Final analyzer status"
---

## What This Guide Helps With
Troubleshoots isolated co-oximetry failures when other measurements remain functional, focusing on sample quality, GEM PAK condition, configuration, and external causes.

## Step-by-Step Troubleshooting

### 1. Protect Patient Testing and Confirm Alternate Testing Is Available

Do not rely on the analyzer for co-oximetry results while the optical channel is failing or producing questionable measurements. Direct specimens requiring affected analytes to another verified analyzer according to laboratory workflow.

Identify whether pH, blood gases, and electrolytes remain available and whether the problem is limited specifically to co-oximetry measurements.

**Expected outcome:** Patient testing continues through a verified method, and the failure is confirmed as isolated to the co-oximetry portion of the analyzer.

If alternate testing is established and the exact affected measurements are known, continue troubleshooting.

### 2. Confirm the Exact Reported Failure

Review the analyzer display, result screen, QC status, and available event information. Determine whether co-oximetry analytes are:

- Missing entirely
- Suppressed or flagged
- Failing quality checks
- Intermittently available
- Failing only on patient samples
- Failing on both patient and control material

Do not assume an optical hardware failure solely because other analytes pass.

**Expected outcome:** The failure pattern is clearly documented and reproducible.

If the analyzer now produces acceptable co-oximetry results and required checks pass, troubleshooting can stop after final verification.

### 3. Inspect the Sample and Collection Path

Verify that the sample presented for testing is appropriate for the requested analysis and has been handled according to laboratory procedure. Inspect for obvious issues such as inadequate sample volume, clotting, bubbles, contamination, or abnormal sample presentation that could interfere with analysis.

Compare the behavior using appropriate control material or another suitable specimen when permitted by laboratory procedure.

**Expected outcome:** The failure is not attributable to an obvious specimen or collection problem.

If correcting the specimen-related issue restores valid co-oximetry results and required QC passes, troubleshooting can stop.

### 4. Check GEM PAK Status and Installation

Review the installed GEM PAK status from the normal operator interface. Confirm that it is properly installed and that the analyzer does not indicate a cartridge-related condition affecting the requested measurements.

Inspect accessible areas for improper seating, contamination, leakage, damage, or evidence that the GEM PAK has been disturbed.

Do not open or disassemble the GEM PAK.

**Expected outcome:** The GEM PAK is properly installed, appears intact, and is recognized normally by the analyzer.

If reseating or replacing the GEM PAK according to approved laboratory/manufacturer procedure restores normal operation and QC passes, troubleshooting can stop.

### 5. Compare Patient Testing With QC or Known-Good Material

Run the appropriate approved verification or quality-control process available to Clinical Engineering in coordination with laboratory personnel.

Determine whether the co-oximetry failure occurs consistently while the analyzer's other measurement channels remain acceptable.

**Expected outcome:** The testing establishes whether the problem follows the optical measurement function rather than a specific patient sample.

If co-oximetry passes with appropriate verification material and subsequent patient testing is normal, document the result and troubleshooting can stop.

### 6. Verify Analyzer Configuration and Requested Test Availability

Using authorized normal configuration screens, verify that the expected co-oximetry measurements remain enabled and available for the installed configuration.

Check for recent configuration changes, software updates, GEM PAK changes, or laboratory workflow changes that correspond with the start of the problem.

Do not enter restricted service menus or alter calibration/service parameters without appropriate authorization and documentation.

**Expected outcome:** Co-oximetry is correctly configured and no unintended configuration change explains the failure.

If correcting an authorized configuration issue restores the measurements and all required verification passes, troubleshooting can stop.

### 7. Inspect Accessible Optical/Sample Areas Without Disassembly

Inspect only externally accessible areas specified for routine cleaning or inspection. Look for visible contamination, residue, fluid intrusion, or damage that could interfere with the analyzer's measurement path.

Use only approved cleaning methods and materials.

**Expected outcome:** Accessible areas are clean, dry, undamaged, and free from conditions that could interfere with testing.

If approved cleaning corrects the failure and QC/functional testing passes, troubleshooting can stop.

### 8. Restart and Recheck the Analyzer

If laboratory workflow permits, complete a normal controlled restart and allow the analyzer to complete its startup checks.

Do not repeatedly reboot an analyzer that reports persistent hardware, temperature, optical, or GEM PAK faults.

**Expected outcome:** The analyzer completes startup normally and either restores the co-oximetry measurements or reproduces the isolated failure consistently.

If normal function returns, complete QC or other required verification before returning the affected measurements to clinical use.

### 9. Perform Final Functional Verification

Before return to service, confirm that:

- Co-oximetry measurements are available
- Required QC or verification passes
- Previously unaffected measurements remain functional
- No new analyzer alarms or faults are present
- Laboratory staff confirm normal workflow

**Expected outcome:** All required measurements and verification checks operate normally.

If these conditions are met, troubleshooting is complete.

## If the Problem Persists

If pH, blood gas, and electrolyte functions remain acceptable but the co-oximetry channel continues to fail after sample, GEM PAK, configuration, accessible-cleaning, and verification checks, common external causes have been ruled out.

The remaining possibilities may involve the optical measurement system, internal temperature control, internal signal processing, analyzer configuration, or another service-level condition.

The analyzer should be:

- Removed from service for affected testing
- Labeled **Out of Service** if reliable clinical use cannot be assured
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not proceed into optical assemblies, internal electronics, or board-level troubleshooting unless specifically authorized and trained.

After repair, complete the manufacturer-appropriate functional checks and laboratory-required QC before return to service.

Knowing when to stop external troubleshooting and escalate an isolated measurement-system failure is proper troubleshooting.

## Clinical Use Tip

A functioning pH or electrolyte channel does not establish that co-oximetry results are reliable; route affected tests to another verified analyzer until verification passes.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- rendered from front matter -->

## Final Thought

Protect patient testing first, verify that the failure is truly isolated, and rule out samples, consumables, configuration, and accessible external conditions before assuming an internal optical failure. Escalate persistent failures appropriately and document both the cause and final verification clearly.

That is successful troubleshooting.
