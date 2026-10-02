---
schemaVersion: 1
title: "Roche cobas pro Clinical Chemistry Analyzer - Sample, Rack, or Carrier Is Not Detected"
issueTitle: "Sample, Rack, or Carrier Is Not Detected"
description: "Troubleshoots missing sample, rack, or carrier detection caused by positioning, identification, loading, obstruction, contamination, or external transport-path conditions."
assetType: "Clinical Chemistry Analyzer"
manufacturer: "Roche"
model: "cobas pro"
slug: "roche-cobas-pro-sample-rack-or-carrier-is-not-detected"
dateAdded: "2026-10-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported one sample rack repeatedly entered the cobas pro but was not recognized."
  cause: "Clinical Engineering found the affected rack visibly damaged and not seating correctly in the loading path."
  resolution: "Replaced the rack with a verified compatible rack, confirmed normal detection and transport, and returned the analyzer for laboratory verification."
helpfulDetails:
  - "Samples or racks affected"
  - "Whether the failure follows one rack"
  - "Tube and label condition"
  - "Rack orientation"
  - "Loading position involved"
  - "Visible obstruction or contamination"
  - "Known-good rack test"
  - "Detection behavior before and after correction"
  - "Any displayed message"
  - "Final sample-tracking status"
---
## What This Guide Helps With

Troubleshoots missing sample, rack, or carrier detection caused by positioning, identification, loading, obstruction, contamination, or external transport-path conditions.

## Step-by-Step Troubleshooting

### 1. Protect Patient Testing and Confirm the Failure

Do not repeatedly process a specimen when sample identity or carrier tracking is uncertain. Remove affected specimens from the active workflow and follow laboratory procedures for maintaining positive sample identification.

Confirm whether the problem affects:
- One sample
- One rack or carrier
- Several racks
- All sample loading
- A specific loading position

Record any displayed message and whether the analyzer physically accepts the carrier but fails to recognize it.

**Expected outcome:** The affected sample-handling scope is clearly identified without risking specimen misidentification.

### 2. Verify the Correct Rack, Carrier, and Sample Placement

Confirm that the rack or carrier being used is appropriate for the analyzer workflow and is loaded in the correct orientation.

Check that:
- Tubes are fully seated
- Nothing protrudes or interferes with movement
- Rack identification features are unobstructed
- The carrier is not visibly bent, cracked, or damaged
- The sample is positioned according to the laboratory's approved workflow

**Expected outcome:** The sample and carrier are correctly positioned and mechanically compatible. If correcting placement restores detection, troubleshooting can stop after verification.

### 3. Inspect the Sample and Rack Identification Area

Check sample labels and rack identification surfaces for:
- Wrinkles
- Peeling labels
- Excessive overlap
- Smudging
- Condensation
- Contamination
- Damaged identifiers

Ensure labels do not interfere with tube seating or movement.

**Expected outcome:** Identification surfaces are clean, intact, readable, and appropriately positioned.

### 4. Inspect the Accessible Loading Path

With the analyzer in a safe state, inspect externally accessible loading and transport areas for:
- Misloaded racks
- Foreign material
- Caps or debris
- Spilled specimen material
- Obvious mechanical obstruction
- Carriers positioned outside their normal track

Do not reach into moving mechanisms or bypass guards or interlocks.

**Expected outcome:** No visible obstruction prevents rack entry, movement, or sensing.

### 5. Try a Known-Good Rack or Carrier

If laboratory procedure permits, transfer an appropriate nonpatient test setup or known-good specimen container to a known-good compatible rack or carrier.

Observe whether the analyzer detects it normally.

**Expected outcome:** A known-good carrier is detected normally. If replacing a damaged or contaminated rack resolves the issue, troubleshooting can stop after final verification.

### 6. Determine Whether the Problem Follows the Sample or the Position

Compare:
- The affected sample in another approved carrier
- A known-good sample or carrier in the affected loading location

Do not compromise specimen identity while performing comparisons.

**Expected outcome:** The fault is isolated to the sample/label, carrier, or analyzer loading path rather than being assumed to be an internal failure.

### 7. Check Accessible Sensors and Reading Areas for Contamination

Inspect only externally accessible areas associated with sample or rack detection. Follow approved cleaning procedures for visible contamination.

Do not open protected covers or adjust sensor alignment.

**Expected outcome:** Accessible detection areas are clean and unobstructed. If cleaning restores consistent detection, proceed to final verification.

### 8. Verify Normal Transport and Detection

Run an approved test carrier or laboratory-defined verification sequence and observe:
- Carrier acceptance
- Correct movement
- Correct identification
- No repeated detection alarm
- Correct sample position recognition

**Expected outcome:** Sample and carrier detection operate normally throughout the expected handling path. Troubleshooting is complete.

### 9. Escalate Repeated Detection Failures

If known-good samples and carriers are not reliably detected after external conditions are ruled out, stop troubleshooting.

Persistent failures may involve transport sensing, identification hardware, positioning mechanisms, or analyzer control systems that require qualified service.

**Expected outcome:** Unreliable sample tracking is removed from clinical use and escalated.

## If the Problem Persists

Common external causes such as incorrect loading, damaged carriers, labels, contamination, and visible obstruction have been ruled out. The remaining issue may involve internal sensors, reader hardware, carrier transport mechanisms, alignment, communications, or service-level configuration.

The analyzer should be:
- Removed from service when reliable specimen identification or tracking cannot be assured
- Labeled Out of Service
- Sent for repair or appropriate service evaluation
- Evaluated using Roche-approved documentation and approved test equipment
- Repaired or configured only by qualified personnel

Complete required functional and laboratory verification before returning the analyzer to patient testing.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Never continue testing when the analyzer cannot reliably associate a specimen with the correct rack position and patient order.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Protect specimen identity first, then work from sample placement and rack condition toward the analyzer transport path. Verify reliable detection before returning the system to use, and escalate rather than accepting intermittent sample tracking.

That is successful troubleshooting.
