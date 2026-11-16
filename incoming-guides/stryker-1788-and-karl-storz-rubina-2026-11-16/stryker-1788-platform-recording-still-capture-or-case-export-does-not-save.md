---
schemaVersion: 1
title: "Stryker 1788 Platform Endoscopic / OR Camera System - Recording, Still Capture, or Case Export Does Not Save"
issueTitle: "Recording, Still Capture, or Case Export Does Not Save"
description: "Capture or export failures caused by storage availability, connections, destination media, workflow settings, network paths, or integration problems."
assetType: "Endoscopic / OR Camera System"
manufacturer: "Stryker"
model: "1788 Platform"
slug: "stryker-1788-platform-recording-still-capture-or-case-export-does-not-save"
dateAdded: "2026-11-16"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that still images captured on the Stryker 1788 appeared to save but were not reaching the expected case-export destination."
  cause: "Clinical Engineering verified local capture was functional and found the external export destination was unavailable."
  resolution: "Coordinated restoration of the external destination and verified successful test capture, export, and retrieval through the complete workflow."
helpfulDetails:
  - "Still capture or video recording affected"
  - "Local save versus external export result"
  - "Intended destination"
  - "External media recognition"
  - "Storage status observed"
  - "Network or integration status"
  - "Test-file retrieval result"
  - "Whether another room or workflow works"
  - "Support groups involved"
  - "Final export verification"
---

## What This Guide Helps With

Capture or export failures caused by storage availability, connections, destination media, workflow settings, network paths, or integration problems.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow and Preserve Required Documentation

If images or video must be retained for the current procedure, notify the clinical team when capture or export is unreliable. Use the facility-approved alternate documentation method rather than repeatedly testing the failed workflow during patient care.

**Expected outcome:** Required clinical documentation can continue through an approved reliable method.

### 2. Confirm the Exact Failure

Determine whether the problem affects:

- Still-image capture
- Video recording
- Local saving
- Export to removable media
- Network or integration export
- All capture functions

Determine whether the system indicates that capture occurred even though the file cannot later be found.

**Expected outcome:** The affected part of the workflow is clearly identified.

### 3. Verify Camera System Stability

Confirm the 1788 system remains powered, displays normal video, and does not restart or freeze during capture attempts.

**Expected outcome:** The camera platform remains stable while capture is requested.

### 4. Confirm the Intended Save Destination

Identify where the clinical team expects the files to be stored or exported.

Verify the selected destination using normal controls and confirm that the workflow has not been unintentionally changed.

**Expected outcome:** The intended save destination is selected and available.

### 5. Check External Storage or Connected Media

If removable or external media is part of the approved workflow, verify that it is:

- Correctly connected
- Recognized by the system
- Not physically damaged
- Appropriate for the intended workflow
- Not obviously unavailable because of a full or inaccessible condition

Do not connect unapproved media.

**Expected outcome:** Approved external storage is recognized and accessible.

### 6. Test a Simple Capture

Using a nonclinical test setup, perform one still capture or short approved test recording and verify whether it can be located at the intended destination.

**Expected outcome:** The test file saves and can be retrieved. If so, the basic capture function is working.

### 7. Separate Local Capture From Export

When possible, determine whether the system can save locally but fails only when transferring the file to another system or destination.

**Expected outcome:** The issue is isolated to capture, storage, or export rather than treated as one undifferentiated failure.

### 8. Verify External Connections and Network Path

For an export workflow involving external equipment or network infrastructure, inspect accessible external connections and verify the associated destination system is available.

Coordinate with IT, PACS, OR integration, or the appropriate support group when the problem is outside the camera platform.

Do not make unauthorized network changes.

**Expected outcome:** The external destination and required path are available.

### 9. Compare With a Known-Working Workflow

When practical, compare the affected setup with another verified 1788 configuration or known-working OR workflow.

Note differences in connected equipment, destination selection, external media, or infrastructure.

**Expected outcome:** A configuration or infrastructure difference is identified or ruled out.

### 10. Perform Final Functional Verification

Verify the actual workflow used clinically:

- Capture a test image or recording
- Confirm it is saved
- Retrieve the file
- Export it when required
- Confirm it arrives at the intended destination
- Verify the system remains stable

**Expected outcome:** The complete capture-and-export workflow succeeds. Troubleshooting can stop and the system may be returned to service.

## If the Problem Persists

If save destination, approved storage media, system stability, local capture, external connections, and destination infrastructure have been verified, the remaining cause may involve storage management, application configuration, network services, integration infrastructure, software, or another service-level condition.

The affected system should be:

- Removed from service when required clinical capture cannot be reliably performed and no approved alternative exists
- Labeled Out of Service when appropriate
- Sent for repair or bench evaluation when the fault is within the device
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Configured or repaired only by qualified personnel

Coordinate with the appropriate IT or integration team when the fault has been isolated outside the camera platform. Verify the complete save and export workflow before return to service.

Knowing when the failure belongs to the device versus the connected infrastructure is proper troubleshooting.

## Clinical Use Tip

Successful image capture is not fully verified until the saved file can be retrieved from the destination expected by the clinical team.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Treat capture, storage, and export as separate parts of the workflow. Verify each stage before assuming a camera-system failure, involve infrastructure support when appropriate, and document the final end-to-end result.

That is successful troubleshooting.
