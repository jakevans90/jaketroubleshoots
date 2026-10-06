---
schemaVersion: 1
title: "Abbott Alinity hq Hematology Analyzer - Sample, Rack, or Carrier Is Not Detected"
issueTitle: "Sample, Rack, or Carrier Is Not Detected"
description: "Addresses missed sample, rack, or carrier detection caused by positioning, identification, loading, obstruction, accessory condition, or external sensor-path issues."
assetType: "Hematology Analyzer"
manufacturer: "Abbott"
model: "Alinity hq"
slug: "abbott-alinity-hq-sample-rack-or-carrier-is-not-detected"
dateAdded: "2026-10-06"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that the Abbott Alinity hq intermittently failed to detect samples loaded in one rack."
  cause: "Clinical Engineering found the affected rack damaged and confirmed a known-good rack was detected normally."
  resolution: "Clinical Engineering removed the damaged rack from service, verified normal sample detection with a known-good rack, and returned the analyzer for laboratory quality verification."
helpfulDetails:
  - "Whether one or all samples were affected"
  - "Tube type and condition"
  - "Barcode condition"
  - "Rack or carrier identification"
  - "Positions affected"
  - "Visible debris or obstruction"
  - "Known-good rack comparison"
  - "Known-good sample comparison"
  - "Displayed message"
  - "Transport behavior"
  - "Final detection result"
---
## What This Guide Helps With

Addresses missed sample, rack, or carrier detection caused by positioning, identification, loading, obstruction, accessory condition, or external sensor-path issues.

## Step-by-Step Troubleshooting

### 1. Protect Specimen Workflow
Do not continue repeatedly loading patient specimens into an unreliable transport or detection path. Route testing through an alternate validated workflow if necessary.

Identify whether the problem affects one specimen, one rack or carrier, or all loaded samples.

**Expected outcome:** Patient specimens remain controlled and the scope of the detection problem is established.

### 2. Confirm the Exact Failure
Determine whether the analyzer fails to recognize the sample entirely, detects the carrier but not the tube, rejects one position, fails intermittently, or stops transport.

Document any displayed message or indicator.

**Expected outcome:** The failure is reproducible and clearly defined. If the issue cannot be reproduced and normal detection is verified repeatedly, troubleshooting can stop.

### 3. Inspect Sample and Tube Positioning
Verify the sample tube is properly seated, upright where required, and appropriate for the laboratory's validated Alinity hq workflow.

Check for damaged tubes, loose caps, excessive labels, peeling labels, or label placement that could interfere with handling or identification.

**Expected outcome:** The sample is correctly positioned and physically suitable for transport and detection. If correcting tube placement resolves detection, verify with another sample and stop.

### 4. Inspect the Rack or Carrier
Examine the affected rack or carrier for cracks, contamination, deformation, worn identification features, foreign material, or improper loading.

Compare it with a known-good rack or carrier when available.

**Expected outcome:** The carrier is intact and properly loaded. If a known-good carrier works normally while the original does not, remove the defective accessory from use and stop.

### 5. Check the Loading and Transport Area
Inspect accessible sample-loading and transport surfaces for dried material, debris, misplaced tubes, label fragments, or other obstructions.

Clean only accessible areas using approved procedures. Do not reach into moving mechanisms.

**Expected outcome:** The sample path is clear and accessible surfaces are clean. If removing an external obstruction restores detection, verify normal transport and stop.

### 6. Verify Barcode and Identification Conditions
If detection appears related to sample identification, inspect barcode quality, orientation, wrinkles, contrast, and placement.

Try a known-good properly labeled specimen or laboratory-approved test item to distinguish a sample-label problem from an analyzer problem.

**Expected outcome:** A known-good identification item is recognized normally. If only the original label fails, correct the specimen-identification issue and stop.

### 7. Compare Multiple Positions and Carriers
Test another known-good rack or carrier and, if practical, another sample position. Determine whether the failure follows the specimen, follows the carrier, or remains at the analyzer.

Do not use patient specimens for unnecessary repeated testing.

**Expected outcome:** The affected element is isolated. If replacing an external carrier or correcting loading resolves the condition, verify normal operation and stop.

### 8. Verify Analyzer Readiness and Settings
Confirm the analyzer is in the correct operating state to accept specimens and that no visible control, paused workflow, or laboratory-approved setting is preventing sample processing.

Do not modify restricted configuration merely to force detection.

**Expected outcome:** The analyzer is configured and ready for normal specimen loading. If restoring the correct operating state resolves detection, troubleshooting can stop.

### 9. Perform Final Functional Verification
Run a known-good laboratory-approved sample or control through the normal loading path and confirm that detection, identification, transport, and processing begin normally.

**Expected outcome:** Sample and carrier detection function consistently. The issue is resolved and troubleshooting can stop.

## If the Problem Persists

External positioning, tube condition, barcode condition, rack or carrier condition, accessible obstructions, and operating state have been ruled out. The remaining cause may involve an internal transport sensor, reader, mechanism, alignment issue, control system, or configuration requiring service evaluation.

The analyzer should be:

- Removed from service if specimen handling is unreliable
- Labeled Out of Service
- Sent for repair or bench/service evaluation
- Evaluated using appropriate Abbott documentation and approved test equipment
- Repaired or configured only by qualified personnel

Return the analyzer to clinical use only after transport and detection functions operate reliably and required laboratory quality verification is completed.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not keep reloading irreplaceable patient specimens into a carrier path that is intermittently failing to detect or transport samples.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect the specimen, then separate tube, label, carrier, loading, and analyzer causes before assuming an internal transport failure. Reliable repeat detection should be demonstrated before the analyzer is returned to routine testing.

That is successful troubleshooting.
