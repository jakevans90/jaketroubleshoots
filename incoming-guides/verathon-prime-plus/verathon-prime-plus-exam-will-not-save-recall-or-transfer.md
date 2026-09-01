---
schemaVersion: 1
title: "Verathon Prime Plus Bladder Scanner - Exam Will Not Save, Recall, or Transfer"
issueTitle: "Exam Will Not Save, Recall, or Transfer"
description: "Helps isolate workflow, storage, patient-selection, connectivity, configuration, and external communication causes affecting exam saving, recall, or transfer."
assetType: "Bladder Scanner"
manufacturer: "Verathon"
model: "Prime Plus"
slug: "verathon-prime-plus-exam-will-not-save-recall-or-transfer"
dateAdded: "2026-09-01"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that Prime Plus exams were completing normally but would not transfer to the expected destination."
  cause: "Clinical Engineering found the external network connection was loose and the scanner did not have a stable communication path."
  resolution: "Clinical Engineering reseated the network connection, verified successful saving and transfer of an approved test exam, and returned the scanner to service."
helpfulDetails:
  - "Whether save, recall, transfer, or multiple functions failed"
  - "Exact displayed message"
  - "Whether scanning itself worked normally"
  - "Patient or exam workflow observed"
  - "Network or docking connection condition"
  - "Communication status"
  - "Whether other devices were affected"
  - "Destination or interface availability"
  - "Test exam results"
  - "Final device status"
---
## What This Guide Helps With

Helps isolate workflow, storage, patient-selection, connectivity, configuration, and external communication causes affecting exam saving, recall, or transfer.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Preserve Clinical Information
Do not delay necessary patient assessment while troubleshooting data handling. If the scanner can measure correctly but cannot save or transfer results, ensure clinically necessary findings are documented through an approved alternate process.

Avoid deleting existing exams or changing system configuration during initial troubleshooting.

**Expected outcome:** Patient care continues safely and important examination results are preserved through an approved workflow.

### 2. Confirm the Exact Failure
Determine whether the complaint involves:
- Exam will not save
- Previously saved exam cannot be recalled
- Exam appears saved but cannot be transferred
- Only certain exams are affected
- Transfer fails consistently or intermittently

Record any displayed message exactly as shown without interpreting or inventing an error meaning.

**Expected outcome:** The affected part of the data workflow is clearly identified.

### 3. Verify Basic Scanner Operation
Confirm the Prime Plus:
- Starts normally
- Accepts normal user input
- Performs a representative scan
- Displays the resulting examination data normally

**Expected outcome:** Core scanning functions operate correctly. If the scanner is generally unstable, remove it from service and troubleshoot the broader system problem first.

### 4. Verify Patient and Exam Workflow
Confirm the correct patient or exam context is selected and that required operator-accessible fields are completed according to facility workflow.

Do not change protected system configuration or create test patient records in a production system unless allowed by facility procedure.

**Expected outcome:** The exam is associated with the intended record and can be saved normally. If correcting an incomplete or incorrect workflow restores saving, troubleshooting can stop after verification.

### 5. Check Available Storage and Existing Exam Behavior
Using normal operator-accessible functions, determine whether other recent exams can be saved and recalled.

Avoid deleting stored clinical data unless authorized.

**Expected outcome:** Exam storage and recall operate consistently. If only one record is affected, document the isolated event and verify normal operation with an approved test record.

### 6. Verify External Communication Connections
If transfer is affected, inspect applicable accessible communication connections such as:
- Network cable
- Docking connection
- Approved communication accessory
- Wireless connection status, if used

Reseat external connections where appropriate.

**Expected outcome:** The external communication path is physically connected and stable. If reseating restores transfer, confirm repeated successful transfer before stopping.

### 7. Verify Network or Communication Availability
When the device depends on facility network services, determine whether other devices on the same workflow are also affected.

Coordinate with IT or the appropriate infrastructure team when a network, interface, server, or destination system problem is suspected.

Do not change IP settings, security settings, or protected network configuration without authorization.

**Expected outcome:** The required infrastructure is available and the scanner has normal communication. If an infrastructure outage explains the complaint, document the cause and coordinate restoration rather than performing unnecessary device repair.

### 8. Verify Authorized Configuration
Review only operator-accessible or authorized configuration needed to confirm that the intended destination or transfer method is selected.

Do not enter restricted service menus or make undocumented configuration changes.

**Expected outcome:** The approved transfer destination and normal workflow are selected. If an authorized configuration correction restores operation, document the exact change and verify transfer.

### 9. Perform Final Functional Verification
Using an approved test workflow, confirm:
- A representative exam can be created
- The exam saves
- It can be recalled
- Transfer completes when applicable
- The receiving destination receives the expected information

**Expected outcome:** The full intended exam workflow succeeds from acquisition through storage, recall, and transfer. Troubleshooting can stop.

## If the Problem Persists

Common workflow, external connection, infrastructure availability, and authorized configuration causes have been ruled out. The remaining issue may involve internal storage, application software, database functions, interface configuration, networking services, or another service-level problem.

The device should be:
- Removed from service if reliable exam retention is required for intended use
- Labeled Out of Service when appropriate
- Sent for repair or bench evaluation when a device-level problem is suspected
- Evaluated using appropriate Verathon documentation and approved test equipment
- Repaired or configured only by qualified personnel

Coordinate with IT or interface support when evidence points to hospital network or destination-system infrastructure.

Complete an end-to-end return-to-service workflow test before restoring clinical use.

## Clinical Use Tip

When electronic transfer is unavailable, ensure bladder-scan results are documented through the approved alternate clinical record process.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter; optional explanatory prose may follow. -->



## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Separate a scanning problem from a data-workflow problem, then verify the exam path logically from patient selection through storage and external communication. Avoid unnecessary configuration changes, involve infrastructure support when appropriate, and document the verified cause and outcome.

That is successful troubleshooting.
