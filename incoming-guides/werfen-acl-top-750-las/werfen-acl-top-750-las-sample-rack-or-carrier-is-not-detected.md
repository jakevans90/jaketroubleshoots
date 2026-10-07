---
schemaVersion: 1
title: "Werfen ACL TOP 750 LAS Coagulation Analyzer - Sample, Rack, or Carrier Is Not Detected"
issueTitle: "Sample, Rack, or Carrier Is Not Detected"
description: "Troubleshoots sample, rack, or carrier detection failures caused by positioning, identification, loading, contamination, obstruction, or external accessory problems."
assetType: "Coagulation Analyzer"
manufacturer: "Werfen"
model: "ACL TOP 750 LAS"
slug: "werfen-acl-top-750-las-sample-rack-or-carrier-is-not-detected"
dateAdded: "2026-10-07"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that one sample rack was repeatedly not detected by the ACL TOP 750 LAS."
  cause: "Clinical Engineering found the affected rack was physically damaged and did not seat normally in the loading position."
  resolution: "Clinical Engineering removed the damaged rack from use, verified proper detection with a known-good rack, and confirmed normal sample loading before return to service."
helpfulDetails:
  - "Sample or rack involved"
  - "Whether one or all positions were affected"
  - "Exact analyzer message"
  - "Tube condition"
  - "Label condition"
  - "Carrier condition"
  - "Known-good substitutions performed"
  - "Loading position tested"
  - "Visible contamination or obstruction"
  - "Detection results after correction"
  - "Final analyzer status"
---
## What This Guide Helps With

Troubleshoots sample, rack, or carrier detection failures caused by positioning, identification, loading, contamination, obstruction, or external accessory problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Testing and Confirm the Failure

Do not continue relying on a sample-loading pathway that cannot reliably detect specimens. Redirect urgent testing to another verified analyzer if needed.

Determine whether the issue affects:
- One sample
- One rack or carrier
- Multiple racks
- One loading position
- All sample loading

Record the exact analyzer message and whether the problem is intermittent or repeatable.

**Expected outcome:** The scope of the detection failure is known. If the issue is limited to one sample or carrier and a properly prepared replacement is detected normally, troubleshooting can stop after verification.

### 2. Inspect the Sample Container

Verify the specimen container is appropriate for the laboratory workflow and is not:
- Cracked
- Grossly contaminated externally
- Improperly capped for the intended process
- Mispositioned in the rack
- Physically incompatible with the carrier being used

Do not modify or force a specimen container to make it fit.

**Expected outcome:** The sample container is intact, properly positioned, and appropriate for the loading system.

### 3. Inspect the Rack or Carrier

Check the rack or carrier externally for:
- Damage
- Warping
- Broken or missing features
- Contamination
- Debris
- Improper sample seating

Compare it with a known-good rack or carrier if available.

**Expected outcome:** The rack or carrier is clean, undamaged, and loaded correctly. If a known-good carrier is detected normally, remove the suspect carrier from use and troubleshooting can stop after confirming repeatability.

### 4. Verify Loading Position and Orientation

Reload the sample, rack, or carrier using the normal laboratory loading orientation.

Ensure it is fully seated and not being held out of position by:
- Adjacent tubes
- Labels
- Caps
- Debris
- Foreign objects

Do not push against powered motion mechanisms.

**Expected outcome:** The sample or carrier seats normally and is recognized. If recognition is restored, troubleshooting can stop after confirming normal processing.

### 5. Check Labels and Identification

Inspect sample labels for:
- Poor placement
- Wrinkles
- Excessive overlap
- Damage
- Obstruction of readable identification
- Labels interfering mechanically with seating

If the analyzer identifies samples by barcode, compare the affected tube with a known-good labeled specimen.

**Expected outcome:** Identification is readable and does not interfere with positioning. If correcting the label resolves detection, troubleshooting can stop.

### 6. Inspect Accessible Loading Areas

With the analyzer in a safe condition, inspect externally accessible sample-loading paths for:
- Debris
- Broken tube fragments
- Dried contamination
- Misplaced consumables
- Obvious obstruction

Clean only accessible areas using approved laboratory or manufacturer cleaning practices.

**Expected outcome:** No visible obstruction prevents loading or detection.

### 7. Perform a Known-Good Comparison

Use a known-good sample container and known-good rack or carrier appropriate for testing.

Determine whether:
- The known-good combination works
- Only one rack fails
- Only one sample position fails
- All loading attempts fail

This separates an accessory problem from an analyzer-side detection problem.

**Expected outcome:** The fault is isolated to the specimen, carrier, loading position, or analyzer. If a defective external component is identified and replacement restores normal operation, troubleshooting can stop.

### 8. Verify Normal Processing

After correcting the cause, confirm the analyzer:
- Detects the sample
- Associates the correct identification
- Accepts the rack or carrier
- Moves the specimen through the normal workflow without repeat detection errors

**Expected outcome:** Samples are consistently recognized and processed normally. Troubleshooting can stop.

## If the Problem Persists

If proper sample preparation, labeling, rack condition, carrier positioning, and accessible loading areas have been verified but detection still fails, common external causes have been ruled out.

The remaining cause may involve a sample-presence sensor, barcode subsystem, transport mechanism, position sensor, alignment issue, controller, or other service-level fault.

The analyzer should be:
- Removed from service if reliable sample identification or transport cannot be assured
- Labeled Out of Service as appropriate
- Sent for repair or bench evaluation
- Evaluated using current Werfen documentation and approved test equipment
- Repaired or adjusted only by qualified personnel

Do not defeat sample sensors or force racks through the loading mechanism.

Return the analyzer to service only after reliable detection and normal processing have been demonstrated.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never process patient samples through a loading path that cannot consistently confirm the correct specimen and carrier.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect specimen integrity, verify sample preparation and external loading components before assuming an internal detection problem, and escalate when reliable sample recognition cannot be restored.

That is successful troubleshooting.
