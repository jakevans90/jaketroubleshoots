---
schemaVersion: 1
title: "Olympus ESG-410 Electrosurgical Unit (ESU) - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "A study-management complaint is assigned to the ESG-410 even though saving, reconstruction, and diagnostic study export normally belong to imaging or documentation systems."
assetType: "Electrosurgical Unit (ESU)"
manufacturer: "Olympus"
model: "ESG-410"
slug: "olympus-esg-410-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-09-17"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that a procedural study would not export and the ticket was entered against the Olympus ESG-410."
  cause: "Clinical Engineering confirmed normal ESG-410 operation and found that the study was being generated and exported by a separate documentation workstation."
  resolution: "Verified the ESU was functional, corrected the equipment association on the work order, and referred the study-export failure to the appropriate workstation and network support workflow."
helpfulDetails:
  - "Device that created the study"
  - "Whether acquisition completed"
  - "Save, reconstruction, or export stage affected"
  - "Exact displayed message"
  - "Local storage status"
  - "Network connection status"
  - "Destination system"
  - "Other systems affected"
  - "ESG-410 local operational status"
  - "Final study-transfer result"
---

## What This Guide Helps With
A study-management complaint is assigned to the ESG-410 even though saving, reconstruction, and diagnostic study export normally belong to imaging or documentation systems.

## Step-by-Step Troubleshooting
### 1. Preserve Patient Care and Required Data

If a clinical imaging or procedure system cannot save required study data, follow the department's approved downtime and data-preservation workflow. Avoid repeated actions that could overwrite or lose unsaved patient information.

**Expected outcome:** Clinical care and available patient data are protected while the failure is investigated.

### 2. Identify the Equipment That Owns the Study

Determine which workstation, imaging system, recording platform, endoscopy processor, or documentation system created the study.

The Olympus ESG-410 is an electrosurgical generator and does not normally perform diagnostic image reconstruction or study export.

**Expected outcome:** The actual study-producing device is identified.

### 3. Determine Which Stage Fails

Clarify whether acquisition completes but saving fails, reconstruction never finishes, local storage is unavailable, export fails, or the destination never receives the study.

**Expected outcome:** The failure is isolated to a specific stage of the study workflow.

### 4. Verify ESG-410 Operation Separately

If the ESU is implicated because it is part of the same procedure setup, verify normal ESG-410 startup, controls, and accessory operation independently.

**Expected outcome:** The electrosurgical generator is either confirmed normal or a separate ESU-specific issue is identified.

### 5. Check the Actual Workstation's External Conditions

Inspect accessible power, network cables, removable media when applicable, docking connections, and peripheral connections on the system responsible for saving or exporting the study.

Do not disconnect storage devices or restart systems containing unsaved data unless the appropriate workflow permits it.

**Expected outcome:** Obvious external connection or power problems are corrected without risking patient data.

### 6. Check Available Storage and System Status

Using normal user-accessible status information on the actual study system, determine whether storage is full, the destination is unavailable, or the application reports a save or processing problem.

Do not delete patient data or alter database settings as a troubleshooting shortcut.

**Expected outcome:** A visible storage, processing, or destination problem is identified or ruled out.

### 7. Determine Whether the Problem Is Local or Network-Wide

Check whether the affected system can save locally and whether other systems can send information to the same destination.

This helps separate local workstation issues from server, PACS, interface, or network failures.

**Expected outcome:** The fault domain is narrowed to the originating device or shared infrastructure.

### 8. Verify a Complete Save or Export After Correction

After the responsible system is corrected, perform an approved test or clinical workflow verification confirming that the study saves, processes, and reaches the intended destination.

Do not consider a transfer successful solely because the sending system reports that it started.

**Expected outcome:** The complete study workflow finishes and the destination confirms receipt when applicable.

## If the Problem Persists
Study saving, reconstruction, and export are not normal standalone functions of the Olympus ESG-410. Persistent failures should be investigated on the actual imaging, documentation, recording, storage, or network system responsible for the study.

If that equipment cannot reliably preserve or process required clinical data, remove it from service when appropriate and label it **Out of Service**. Evaluate it using the correct manufacturer documentation and approved diagnostic tools. Storage, database, network, or PACS infrastructure problems should be escalated to the appropriate Clinical Engineering, imaging, integration, or IT team.

Do not modify the ESG-410 internally to address a study-processing function it does not provide.

## Clinical Use Tip
Protect unsaved patient data first; avoid unnecessary restarts or disconnections until the system responsible for the study has been identified.

## Work Order Documentation (CCR Method)
<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)
<!-- Helpful details come from front matter. -->

## Final Thought
Protect patient data, identify the system responsible for the study, verify external conditions before assuming internal failure, and escalate storage or network problems to the correct technical team with clear documentation.

That is successful troubleshooting.
