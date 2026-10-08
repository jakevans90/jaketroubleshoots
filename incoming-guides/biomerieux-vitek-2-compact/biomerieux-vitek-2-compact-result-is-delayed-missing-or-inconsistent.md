---
schemaVersion: 1
title: "bioMerieux VITEK 2 Compact Microbiology Identification System - Result Is Delayed, Missing, or Inconsistent"
issueTitle: "Result Is Delayed, Missing, or Inconsistent"
description: "Use this guide when expected results are delayed, unavailable, inconsistent, or not appearing where laboratory staff expects them."
assetType: "Microbiology Identification System"
manufacturer: "bioMerieux"
model: "VITEK 2 Compact"
slug: "biomerieux-vitek-2-compact-result-is-delayed-missing-or-inconsistent"
dateAdded: "2026-10-08"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that completed results from the bioMerieux VITEK 2 Compact were visible on the analyzer but were missing from the LIS."
  cause: "Clinical Engineering found the analyzer had lost its external network connection while local test processing remained normal."
  resolution: "Restored the approved network connection, verified communication status, and laboratory staff confirmed successful transmission of an appropriate test result to the LIS."
helpfulDetails:
  - "Specimen or test affected"
  - "Whether the result existed on the analyzer"
  - "Analyzer test status"
  - "Relevant timestamps"
  - "Sample identifier status"
  - "Active analyzer messages"
  - "Number of affected results"
  - "Network and middleware status"
  - "Whether other analyzers were affected"
  - "Recent power or network changes"
  - "Repeat-test or QC outcome"
  - "End-to-end transmission result"
  - "Final system status"
---
## What This Guide Helps With

Use this guide when expected results are delayed, unavailable, inconsistent, or not appearing where laboratory staff expects them.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Decision-Making

Do not allow clinicians to rely on incomplete, missing, or questionable microbiology results.

Laboratory staff should identify affected specimens and use their approved alternate reporting or retesting workflow as necessary.

**Expected outcome:** Patient care continues without reliance on an unverified result.

### 2. Confirm What “Delayed, Missing, or Inconsistent” Means

Determine whether the result:

- Never appeared on the analyzer
- Appeared on the analyzer but not the LIS
- Is delayed compared with normal workflow
- Is associated with the wrong status
- Differs from an expected repeat or comparison
- Is only missing from a remote system

Identify the specific specimen or test and record timestamps when available.

**Expected outcome:** The location and nature of the result problem are clearly defined.

### 3. Verify the Test Actually Entered the Expected Workflow

Have laboratory staff confirm that the specimen, card, or test was correctly loaded, identified, and started.

Check whether the analyzer shows the test as:

- Pending
- In process
- Completed
- Failed
- Awaiting another action

**Expected outcome:** The actual analyzer state of the test is known.

### 4. Verify Sample and Consumable Identification

Check that sample identifiers, barcodes, racks, cards, and related consumables were recognized correctly.

Do not assume a missing electronic result if the test was never properly associated with the intended specimen.

**Expected outcome:** Sample-to-test association is verified.

### 5. Check Analyzer Status and Active Messages

Review normal operator-accessible status screens for current or recent messages that may explain delayed processing.

Look for related problems involving:

- Loading
- Transport
- Recognition
- Communication
- Fluid handling
- System initialization

Do not clear logs or delete records needed for investigation.

**Expected outcome:** Any equipment-side event associated with the delayed or missing result is identified.

### 6. Distinguish Analyzer Processing From LIS Transmission

If the result exists on the analyzer but is absent from the LIS, shift troubleshooting toward the communication path rather than the analytical process.

Verify external network connectivity, middleware availability, and result transmission status in collaboration with LIS or IT support.

**Expected outcome:** The issue is separated into analyzer processing or downstream communication.

### 7. Compare With Other Recent Tests

Determine whether:

- Only one specimen is affected
- Multiple recent results are delayed
- One test type is affected
- All results are affected
- Another instrument is experiencing similar delays

**Expected outcome:** The scope of the problem is established.

### 8. Check for External Workflow or Infrastructure Delays

Confirm whether recent changes occurred involving:

- LIS
- Middleware
- Network infrastructure
- Workstations
- User workflow
- Sample identification
- Equipment relocation
- Power interruptions

Do not modify protected configuration simply because results are delayed.

**Expected outcome:** External workflow or infrastructure causes are identified or ruled out.

### 9. Address Inconsistent Results Through Laboratory Verification

If the concern is that a result appears analytically inconsistent, laboratory personnel must determine whether repeat testing, QC, or another validated method is required.

Clinical Engineering should verify equipment operation but should not interpret microbiology results or decide clinical validity.

**Expected outcome:** Result validity is assessed through the laboratory's quality system while equipment performance is evaluated separately.

### 10. Perform Final End-to-End Verification

After correction, verify an appropriate test can:

- Be correctly identified
- Enter processing
- Complete normally
- Produce the expected analyzer status
- Transfer to the intended receiving system when applicable

Have laboratory staff confirm that result handling is normal.

**Expected outcome:** Result generation and reporting are functioning reliably from analyzer through final destination.

If the complete workflow is restored and laboratory verification is satisfactory, troubleshooting can stop.

## If the Problem Persists

If test setup, sample identification, analyzer status, processing state, communication path, recent system events, and external workflow have been checked, common external causes have been ruled out.

The remaining problem may involve internal processing control, database behavior, analyzer software, communication software, middleware, LIS configuration, or another service-level condition.

The device or affected result pathway should be:

- Removed from service if result integrity cannot be assured
- Labeled Out of Service when appropriate
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Preserve logs and affected-test details when escalation is required. Knowing when to stop external troubleshooting and involve manufacturer, LIS, or IT support is proper troubleshooting.

Complete laboratory validation and end-to-end result verification before return to routine use.

## Clinical Use Tip

When investigating a missing result, first determine whether the result was never generated or was generated but failed somewhere in the reporting path.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Follow the result from specimen identification through analyzer processing and final reporting before assuming an internal failure. Protect questionable results, preserve useful evidence, escalate appropriately, and document exactly where the workflow failed and how it was verified.

That is successful troubleshooting.
