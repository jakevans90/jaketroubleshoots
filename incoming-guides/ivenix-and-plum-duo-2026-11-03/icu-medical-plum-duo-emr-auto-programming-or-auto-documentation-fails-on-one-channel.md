---
schemaVersion: 1
title: "ICU Medical Plum Duo Infusion Pump - EMR Auto-Programming or Auto-Documentation Fails on One Channel"
issueTitle: "EMR Auto-Programming or Auto-Documentation Fails on One Channel"
description: "Troubleshoots channel-specific interoperability failures involving patient association, channel selection, network connectivity, middleware, order matching, or configuration."
assetType: "Infusion Pump"
manufacturer: "ICU Medical"
model: "Plum Duo"
slug: "icu-medical-plum-duo-emr-auto-programming-or-auto-documentation-fails-on-one-channel"
dateAdded: "2026-11-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that channel two would infuse normally but would not auto-document to the patient's EMR record."
  cause: "Clinical Engineering found channel two was associated with an outdated patient-device assignment in the authorized integration workflow."
  resolution: "Cleared the stale association through the approved workflow, reassigned the correct patient and channel, and verified successful auto-documentation to the EMR."
helpfulDetails:
  - "Affected channel"
  - "Auto-programming or auto-documentation failure"
  - "Patient-device association"
  - "Channel assignment"
  - "Pump network status"
  - "Location tested"
  - "Order status"
  - "Known-good pump comparison"
  - "Middleware or interface result"
  - "Restart/reassociation result"
  - "Final EMR verification"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots channel-specific interoperability failures involving patient association, channel selection, network connectivity, middleware, order matching, or configuration.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Safe Programming
Do not rely on failed auto-programming or auto-documentation to deliver or record therapy. Follow the facility's approved manual workflow or transfer to another verified device while interoperability is being evaluated.

**Expected outcome:** Therapy and documentation continue safely without depending on the failed interface.

### 2. Confirm Which Direction of Communication Failed
Determine whether the pump failed to receive programming from the EMR, failed to send infusion documentation back, or both. Confirm which channel is affected and whether the other channel communicates normally.

**Expected outcome:** The exact interoperability failure and affected channel are identified.

### 3. Confirm Patient and Device Association
Using authorized clinical workflow tools, verify that the correct patient, pump, and intended channel are associated. Check for an incorrect room, bed, device, or patient assignment.

**Expected outcome:** The EMR and pump are associated with the correct patient and channel.

If correcting the association restores communication, verify the complete workflow and stop troubleshooting.

### 4. Verify the Pump's Network Connection
Check permitted user-accessible connectivity indications. Compare the pump with another unit known to communicate successfully from the same location.

**Expected outcome:** The pump has normal network connectivity.

If neither pump communicates in the same area, investigate infrastructure rather than the individual Plum Duo.

### 5. Compare the Two Channels
Using a controlled test or approved interoperability workflow, determine whether one channel consistently succeeds while the other fails.

**Expected outcome:** Both channels support the expected integration workflow.

A repeatable one-channel failure should be documented carefully before escalation.

### 6. Verify the Order and Programming Workflow
Confirm the intended medication order is active, appropriate for the workflow, and matched to the correct patient and channel. Avoid modifying clinical orders solely to make a technical test succeed.

**Expected outcome:** A valid order is available for the intended interoperability process.

### 7. Check for Stale or Duplicate Associations
Review authorized system displays for old device assignments, duplicate channel associations, or prior patient links that could interfere with the current workflow.

**Expected outcome:** Only the correct current patient-device-channel relationship is active.

### 8. Restart Communication Through Approved Workflow
If permitted and the pump is not in patient use, perform a normal restart and re-establish the approved patient/device association.

**Expected outcome:** The pump reconnects and the intended channel resumes communication.

### 9. Compare With Another Pump
Where practical, use another verified Plum Duo with the same approved patient/test workflow and network location.

**Expected outcome:** The known-good device completes auto-programming and auto-documentation successfully.

If the known-good pump also fails, escalate the EMR, middleware, network, or interface path.

### 10. Verify the Complete Data Path
Coordinate with the appropriate integration or clinical informatics team to confirm whether the transaction reaches the interface engine or middleware and whether acknowledgment or documentation returns as expected. Clinical Engineering should verify device-side status without making unauthorized backend configuration changes.

**Expected outcome:** The point of failure is isolated to the pump, network, middleware, or EMR side.

### 11. Perform Final Verification
After correction, verify the intended channel receives the appropriate approved programming information and that completed infusion data appears at the correct patient record destination according to the site's validated workflow.

**Expected outcome:** Auto-programming and auto-documentation complete correctly for the affected channel.

## If the Problem Persists

If patient association, channel assignment, network connectivity, valid orders, known-good device comparison, and approved restart have been checked, common external causes have been ruled out.

Possible remaining categories include pump interoperability configuration, device software, channel-specific communication handling, middleware mapping, interface-engine configuration, network services, or EMR integration.

The pump should be removed from service if reliable interoperability is required for its intended clinical use and the failure cannot be safely bypassed by approved workflow. Label it **Out of Service** when appropriate and escalate to qualified Clinical Engineering, IT, clinical informatics, the EMR integration team, or ICU Medical support.

Any configuration changes must follow authorized change-control procedures. Complete functional and interoperability verification before return to service.

## Clinical Use Tip

Verify the complete path from the intended EMR order to the correct pump channel and back to the correct patient record.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Interoperability failures should be isolated systematically across patient association, channel assignment, pump connectivity, middleware, and EMR workflows. Maintain safe manual alternatives, avoid unauthorized configuration changes, verify the complete data path, and document the final correction clearly.

That is successful troubleshooting.
