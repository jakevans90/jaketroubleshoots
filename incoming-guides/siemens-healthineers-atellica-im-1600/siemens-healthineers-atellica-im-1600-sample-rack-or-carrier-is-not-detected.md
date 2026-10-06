---
schemaVersion: 1
title: "Siemens Healthineers Atellica IM 1600 Immunoassay Analyzer - Sample, Rack, or Carrier Is Not Detected"
issueTitle: "Sample, Rack, or Carrier Is Not Detected"
description: "Use this guide when samples, racks, or carriers are loaded but are not recognized, accepted, transported, or processed as expected."
assetType: "Immunoassay Analyzer"
manufacturer: "Siemens Healthineers"
model: "Atellica IM 1600"
slug: "siemens-healthineers-atellica-im-1600-sample-rack-or-carrier-is-not-detected"
dateAdded: "2026-10-06"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that samples loaded in one rack were not consistently detected by the Atellica IM 1600."
  cause: "Clinical Engineering found the rack damaged and confirmed that the detection problem followed the rack while a known-good rack operated normally."
  resolution: "The damaged rack was removed from use, a known-good rack was installed, and successful sample detection and transport were verified."
helpfulDetails:
  - "Samples, racks, or positions affected"
  - "Tube and label condition"
  - "Rack or carrier condition"
  - "Whether the failure followed the sample or accessory"
  - "Known-good substitution results"
  - "Barcode recognition status"
  - "Visible obstruction or contamination"
  - "Analyzer readiness state"
  - "Functional verification result"
  - "Final analyzer status"
---
## What This Guide Helps With

Use this guide when samples, racks, or carriers are loaded but are not recognized, accepted, transported, or processed as expected.

## Step-by-Step Troubleshooting

### 1. Protect Patient Testing and Confirm the Failure

Do not allow patient testing to depend on a sample-handling path that is intermittently or incorrectly detecting specimens.

Determine whether the problem affects:
- One sample
- One rack or carrier
- Multiple racks
- One loading position
- All sample transport
- Only certain tube types or identifiers

Record any displayed message and determine whether the sample is physically rejected, passes through without recognition, or is recognized incorrectly.

**Expected outcome:** The scope of the detection problem is clearly defined. If the problem is isolated to a single removable accessory or specimen and normal operation is restored with a known-good substitute, troubleshooting can stop after verification.

### 2. Inspect the Sample Container

Inspect the affected specimen for obvious external causes:
- Incorrectly seated tube
- Damaged or distorted tube
- Cap or closure interfering with positioning
- Label extending into an area used for detection
- Multiple overlapping labels
- Barcode label wrinkled or poorly positioned
- Tube leaning or binding in the rack

Do not manipulate the specimen in a way that compromises specimen integrity.

**Expected outcome:** The sample is correctly positioned and physically compatible with the normal workflow. If correcting positioning restores detection, the issue is resolved.

### 3. Inspect the Rack or Carrier

Remove the affected rack or carrier when safe and inspect it for:
- Cracks
- Warping
- Contamination
- Bent or damaged features
- Obstructions
- Improperly seated tubes
- Foreign material that could affect tracking or movement

Compare it with a known-good rack or carrier if available.

**Expected outcome:** The rack or carrier is physically intact and clean. If a known-good rack works normally while the original repeatedly fails, replace or remove the defective accessory and stop troubleshooting after confirmation.

### 4. Verify Correct Loading and Positioning

Confirm the rack, carrier, or sample is loaded in the correct orientation and fully positioned within the intended loading path.

Inspect accessible loading and transport areas for:
- Misaligned racks
- Items placed outside guides
- Foreign objects
- Labels or debris protruding into the pathway
- Obvious obstruction at entry points

Do not reach into moving mechanisms or defeat covers or interlocks.

**Expected outcome:** The loading pathway is unobstructed and the sample carrier is properly positioned. If correct loading restores detection, the issue is resolved.

### 5. Determine Whether the Failure Follows the Sample or Position

Using a suitable known-good specimen container or approved test material, determine whether the failure follows:
- The original tube
- The rack or carrier
- A specific loading position
- The analyzer regardless of sample or rack

Avoid using patient samples solely for troubleshooting when suitable laboratory controls or nonpatient test materials are available.

**Expected outcome:** The failure is narrowed to a sample, accessory, location, or analyzer-level condition. A problem isolated to a replaceable external item can be corrected and troubleshooting stopped after verification.

### 6. Check Barcode Recognition Separately

If physical sample presence is detected but identification fails, inspect the barcode and barcode-reading area separately.

Verify:
- Label is readable
- Barcode is not covered or damaged
- Label placement does not interfere with scanning
- Scanner window or externally accessible reader surface is clean
- The correct sample identification workflow is being used

**Expected outcome:** Samples are both physically detected and correctly identified. If the issue is barcode-specific, correct the labeling or reader obstruction and verify normal recognition.

### 7. Verify Analyzer Status and Sample-Handling Readiness

Confirm the analyzer is in a state that permits sample loading and processing. Check for active conditions that could prevent transport or detection, such as:
- Analyzer not ready
- Pending initialization
- Sample transport unavailable
- Waste or consumable condition preventing operation
- Active fault affecting sample movement

Do not alter restricted configuration or service settings.

**Expected outcome:** The analyzer is ready to accept samples. If clearing a valid external prerequisite restores detection, the issue is resolved.

### 8. Perform Functional Verification

Run an appropriate nonpatient sample or laboratory-approved material through the affected pathway.

Verify:
- Carrier acceptance
- Sample detection
- Identification
- Transport
- Processing initiation

**Expected outcome:** A known-good sample and carrier are repeatedly detected and processed normally. Troubleshooting can stop.

### 9. Escalate Persistent Detection Problems

If multiple known-good samples and carriers fail in the same position or throughout the analyzer, remove the affected system from routine use.

Do not attempt internal sensor alignment, internal transport repair, or restricted calibration unless specifically authorized.

**Expected outcome:** A persistent sample-detection problem is escalated for qualified service evaluation.

## If the Problem Persists

If known-good sample containers, racks, carrier positioning, loading technique, visible transport paths, and analyzer readiness have been verified, common external causes have been ruled out.

Remaining possibilities may involve an internal presence sensor, transport mechanism, reader, alignment condition, controller communication issue, or service-level configuration problem.

The analyzer should be:
- Removed from service if reliable sample identification or transport cannot be assured
- Labeled Out of Service
- Sent for repair or qualified service evaluation
- Evaluated using Siemens Healthineers documentation and approved test equipment
- Repaired or configured only by qualified personnel

Before returning the analyzer to service, verify reliable detection and processing using appropriate nonpatient material and complete required laboratory quality checks.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never rely on an analyzer that intermittently misses samples; undetected specimens can create clinically significant testing delays.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Sample-detection problems should be narrowed systematically from the tube and rack to positioning, identification, and analyzer transport. Reliable detection must be demonstrated before patient testing resumes, and persistent failures require service escalation.

That is successful troubleshooting.
