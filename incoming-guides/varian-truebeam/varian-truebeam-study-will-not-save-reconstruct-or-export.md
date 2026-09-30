---
schemaVersion: 1
title: "Varian TrueBeam Radiation Therapy System - Study Will Not Save, Reconstruct, or Export"
issueTitle: "Study Will Not Save, Reconstruct, or Export"
description: "Imaging or study data will not save, reconstruct, complete processing, or export to the required clinical destination."
assetType: "Radiation Therapy System"
manufacturer: "Varian"
model: "TrueBeam"
slug: "varian-truebeam-study-will-not-save-reconstruct-or-export"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported that TrueBeam imaging studies completed locally but would not export to the configured destination."
  cause: "Clinical Engineering found the destination clinical system unavailable due to a network-side service interruption."
  resolution: "Clinical Engineering coordinated restoration with IT and verified successful export and receipt of an approved test study before returning the workflow to service."
helpfulDetails:
  - "Save, reconstruction, or export function affected"
  - "Exact displayed message"
  - "Single study versus all studies"
  - "Workstation responsiveness"
  - "Network connection status"
  - "Destination-system status"
  - "Storage or processing message"
  - "Restart performed"
  - "Test dataset used"
  - "Confirmation at receiving destination"
  - "Final system status"
---
## What This Guide Helps With

Imaging or study data will not save, reconstruct, complete processing, or export to the required clinical destination.

## Step-by-Step Troubleshooting

### 1. Protect Patient Data and Clinical Continuity
Do not delete, overwrite, or repeatedly recreate clinically important data while troubleshooting. Confirm the patient is safe and notify Radiation Oncology if the failed study affects treatment decisions or workflow.

**Expected outcome:** Patient care continues safely and potentially recoverable clinical data is preserved.

### 2. Identify Which Function Failed
Determine whether the problem is saving, reconstruction, local processing, export, or transfer to another system. Record the exact message and the last successfully completed step.

**Expected outcome:** The failed portion of the data workflow is clearly identified.

### 3. Confirm the Workstation Is Responsive
Check whether the associated workstation and application respond normally or whether the system is frozen, unusually slow, or reporting other faults.

**Expected outcome:** A workstation-performance issue is distinguished from a study-specific failure.

### 4. Check Whether the Problem Is Study-Specific
Determine whether the issue affects only one study or all new studies. Do not alter or delete patient records simply to test the system.

Use approved test data when available.

**Expected outcome:** The problem is narrowed to one dataset or the overall processing workflow.

### 5. Verify Required Network Connectivity for Export
If export is affected, inspect accessible network connections and confirm that the intended destination is online and reachable through approved methods.

**Expected outcome:** A basic network or destination outage is either identified or ruled out.

### 6. Verify the Intended Export Destination
Confirm that the correct configured clinical destination is selected and available. Do not modify restricted DICOM, storage, or network settings without authorization.

**Expected outcome:** The expected destination is correctly selected and active.

### 7. Check for Obvious Storage or System Messages
Review user-accessible notifications for storage, processing, communication, or application conditions. Do not manually remove protected system files or patient data to free space.

**Expected outcome:** Any obvious user-visible storage or processing condition is identified without compromising data integrity.

### 8. Perform an Approved Restart if Needed
If the workstation or application appears stalled and the patient is no longer dependent on it, follow the approved restart process. Preserve data according to facility and manufacturer procedures.

**Expected outcome:** Processing resumes normally after restart or the failure remains reproducible.

### 9. Perform a Controlled Save, Reconstruction, or Export Test
Use approved test data to verify the affected function and confirm completion at the intended endpoint when applicable.

**Expected outcome:** The study processes successfully through the full required workflow. If it does, troubleshooting can stop.

### 10. Escalate Persistent Data-Handling Failures
If studies repeatedly fail to save, reconstruct, or export, if data integrity is uncertain, or if storage cannot be verified, discontinue the affected workflow.

**Expected outcome:** Unreliable data handling is prevented from affecting patient treatment.

## If the Problem Persists

External network connectivity, destination availability, workstation responsiveness, and basic workflow selection have been ruled out. Remaining causes may involve application software, storage systems, reconstruction services, databases, internal communications, DICOM services, or other service-level infrastructure.

The device or affected workflow should be:

- Removed from service when safe clinical data handling cannot be assured
- Labeled Out of Service when the system cannot safely support treatment
- Sent for repair or appropriate Varian/IT/PACS evaluation
- Evaluated using appropriate manufacturer documentation and approved diagnostic tools
- Repaired or configured only by qualified personnel

Return to service requires successful saving, processing, reconstruction, and transfer testing for the functions affected, with data integrity confirmed.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never delete a failed or incomplete clinical study simply to clear the workflow until the care team confirms that the data is no longer required.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Data-processing failures require protection of both the patient and the clinical record. Preserve existing data, verify the workstation, network, and destination before assuming an internal failure, and escalate whenever study integrity or reliable completion cannot be confirmed.

That is successful troubleshooting.
