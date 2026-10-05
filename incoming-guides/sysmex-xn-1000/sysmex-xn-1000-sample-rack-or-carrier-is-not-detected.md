---
schemaVersion: 1
title: "Sysmex XN-1000 Hematology Analyzer - Sample, Rack, or Carrier Is Not Detected"
issueTitle: "Sample, Rack, or Carrier Is Not Detected"
description: "Samples or racks are not recognized because of positioning, barcode, carrier, loading, obstruction, sensor-path, or workflow-related external conditions."
assetType: "Hematology Analyzer"
manufacturer: "Sysmex"
model: "XN-1000"
slug: "sysmex-xn-1000-sample-rack-or-carrier-is-not-detected"
dateAdded: "2026-10-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that one rack repeatedly passed the loading area without its samples being recognized."
  cause: "Clinical Engineering found several sample barcodes on the rack wrinkled and positioned outside the normal readable orientation."
  resolution: "The samples were relabeled and reloaded, after which all samples were detected correctly and the rack completed processing normally."
helpfulDetails:
  - "Whether one or all racks are affected"
  - "Sample tube type and physical condition"
  - "Barcode condition and orientation"
  - "Rack or carrier condition"
  - "Known-good rack comparison"
  - "Loading position tested"
  - "Any visible debris or obstruction"
  - "Whether the rack moves normally"
  - "Results before and after correction"
  - "Final analyzer status"
---
## What This Guide Helps With

Samples or racks are not recognized because of positioning, barcode, carrier, loading, obstruction, sensor-path, or workflow-related external conditions.

## Step-by-Step Troubleshooting

### 1. Protect Patient Testing and Confirm the Failure
Redirect testing to another verified analyzer or approved backup process if the detection problem is delaying patient results. Determine whether the problem affects one sample, one rack, multiple racks, or all samples.

**Expected outcome:** The scope of the detection problem is defined without compromising patient testing. If only one sample or rack is affected, focus troubleshooting there.

### 2. Inspect the Sample and Rack
Check the affected tube, rack, and carrier for cracks, deformation, contamination, improper seating, foreign material, or incompatible physical condition. Verify the tube is fully seated and positioned consistently with other successfully processed samples.

**Expected outcome:** The sample and rack are physically intact and correctly positioned. Repositioning or replacing a damaged external item should restore detection.

### 3. Check Barcode Condition and Orientation
Inspect the sample barcode for wrinkles, smearing, poor print quality, excessive curvature, obstruction, or incorrect orientation. Compare it with a sample that the analyzer reads correctly.

**Expected outcome:** The barcode is clean, legible, and positioned for reliable reading. If correcting or replacing the label restores detection, troubleshooting can stop after verification.

### 4. Try a Known-Good Sample or Rack
Use an approved known-good rack or properly prepared test sample to determine whether the problem follows the original sample/rack or remains with the analyzer position.

**Expected outcome:** A known-good item is detected normally. If so, the problem is isolated to the original sample, label, or rack rather than the analyzer.

### 5. Inspect the Loading and Transport Path
With the analyzer in an appropriate safe state, visually inspect accessible sample loading and transport areas for misplaced tubes, debris, dried material, labels, or other obvious obstructions. Do not reach into moving mechanisms.

**Expected outcome:** The accessible transport path is clear. Removal of an external obstruction restores normal detection.

### 6. Verify Rack Placement and Loading Technique
Confirm racks are loaded completely and aligned correctly in the intended loading location. Check that no external accessory or neighboring rack is interfering with movement or presentation.

**Expected outcome:** Racks enter the analyzer path normally and are detected consistently.

### 7. Compare Detection Across Positions
If practical, test more than one rack and loading position to identify whether the failure is isolated to a single rack, carrier, loading area, or the entire analyzer.

**Expected outcome:** The failure pattern is narrowed to an external rack/sample issue or a repeatable analyzer-side detection problem.

### 8. Perform an Approved Restart if Appropriate
If the analyzer is otherwise stable and the detection failure persists across known-good racks, perform an approved restart after ensuring samples are safely removed or managed.

**Expected outcome:** Normal rack and sample detection returns after restart. If it does, verify several samples before stopping troubleshooting.

### 9. Perform Final Functional Verification
Run appropriate nonpatient or approved verification samples through the affected loading path. Confirm racks advance normally, barcodes are recognized, and samples are associated correctly.

**Expected outcome:** Multiple samples and racks are detected without recurrence. Troubleshooting can stop.

### 10. Escalate Persistent Detection Failure
If known-good samples and racks repeatedly fail in the same analyzer position or transport path, stop external troubleshooting.

**Expected outcome:** The analyzer is removed from service or the affected workflow is disabled as appropriate and qualified service evaluation is initiated.

## If the Problem Persists

Common sample, barcode, rack, positioning, obstruction, and loading causes have been ruled out. The remaining problem may involve an internal sensor, transport mechanism, reader assembly, alignment, controller, or service-level configuration condition.

Remove the analyzer from service if reliable sample identification or transport cannot be assured, label it **Out of Service**, and arrange repair or service evaluation. Use appropriate Sysmex documentation and approved test equipment. Internal alignment, sensor replacement, or mechanism repair should be completed only by qualified personnel.

After service, verify reliable rack transport, sample detection, barcode association, and analyzer performance before return to clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not manually bypass unreliable sample identification; positive patient-sample identification must remain intact throughout the testing process.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Reliable sample identification is a patient-safety requirement. Start with tubes, labels, racks, and positioning before suspecting internal detection hardware, verify the complete sample path after correction, and document the findings clearly.

That is successful troubleshooting.
