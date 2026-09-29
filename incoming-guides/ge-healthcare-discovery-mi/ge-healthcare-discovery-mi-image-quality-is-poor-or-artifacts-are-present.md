---
schemaVersion: 1
title: "GE Healthcare Discovery MI PET / CT System - Image Quality Is Poor or Artifacts Are Present"
issueTitle: "Image Quality Is Poor or Artifacts Are Present"
description: "Troubleshoots PET or CT image artifacts and degraded quality caused by positioning, motion, accessories, contamination, protocol selection, calibration, or environmental factors."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "Discovery MI"
slug: "ge-healthcare-discovery-mi-image-quality-is-poor-or-artifacts-are-present"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Imaging staff reported a repeatable artifact on Discovery MI CT images that was not present on prior studies."
  cause: "Clinical Engineering found a removable positioning accessory with metallic material left within the imaging field during the affected examinations."
  resolution: "Clinical Engineering removed the accessory, completed approved image-quality verification, confirmed the artifact was no longer present, and returned the scanner to service."
helpfulDetails:
  - "PET, CT, or fused images affected"
  - "Artifact appearance and location"
  - "Patients or protocols affected"
  - "Patient movement"
  - "Positioning details"
  - "Accessories in the scan field"
  - "Recent configuration changes"
  - "QC status"
  - "Test phantom result"
  - "Final image-quality result"
---
## What This Guide Helps With
Troubleshoots PET or CT image artifacts and degraded quality caused by positioning, motion, accessories, contamination, protocol selection, calibration, or environmental factors.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Unnecessary Repeat Imaging

Do not repeat CT exposures or PET acquisitions solely to investigate an unexplained image-quality problem without first checking obvious external causes.

If diagnostic image quality cannot be assured, stop clinical use of the affected acquisition path and move the patient to another verified system when necessary.

**Expected outcome:** The patient is not subjected to unnecessary repeat imaging and questionable images are not relied upon clinically.

### 2. Characterize the Image Problem

Determine whether the issue affects:

- CT images
- PET images
- Fused PET / CT images
- One examination or multiple patients
- One protocol or all protocols
- A specific anatomical region
- All reconstructed series

Review when the artifact first appeared and whether it is repeatable.

**Expected outcome:** The artifact is categorized well enough to guide external troubleshooting.

### 3. Check Patient Motion and Positioning

Review the study for motion, mispositioning, or inconsistent positioning between acquisitions.

Check whether:

- The patient moved
- Arms or body position changed
- Respiratory motion may have affected alignment
- The patient was uncomfortable or unable to remain still
- Positioning devices shifted

**Expected outcome:** Patient movement and positioning are either identified as the likely cause or reasonably ruled out.

If positioning or motion explains the issue and a repeat study is clinically authorized, correct the setup before reacquisition.

### 4. Inspect External Objects and Accessories

Check the scan field and patient setup for objects that can introduce artifacts, including:

- Monitoring leads
- Cables
- Metallic objects
- Positioning aids
- Clothing hardware
- External devices
- Accessories inadvertently left in the imaging field

Also inspect approved scanner accessories for damage or incorrect placement.

**Expected outcome:** No avoidable external object or damaged accessory is affecting image quality.

### 5. Confirm Correct Protocol and Reconstruction Selection

Verify that the intended clinical protocol, acquisition mode, reconstruction selection, and operator-accessible image settings were used.

Compare with a known-good examination or approved department configuration when appropriate.

Do not alter service calibration or restricted reconstruction parameters.

**Expected outcome:** The imaging workflow uses the intended approved configuration.

### 6. Determine Whether the Problem Is Patient-Specific or System-Wide

Review recent studies or approved test images to determine whether the artifact occurs:

- Only with one patient
- Only with one protocol
- Only with one accessory
- Across multiple unrelated examinations

Avoid using patient exposures solely as a troubleshooting test.

**Expected outcome:** The issue is narrowed to a patient/workflow cause or a reproducible equipment-related condition.

### 7. Inspect the Accessible Imaging Area

Inspect accessible surfaces and components around the patient opening and table for:

- Foreign material
- Fluid contamination
- Damaged covers
- Loose accessories
- Objects in the imaging path
- Visible physical damage

Do not open detector or gantry covers.

**Expected outcome:** Accessible imaging surfaces and the scan path are clean, intact, and unobstructed.

### 8. Review Calibration and Quality-Control Status

Determine whether required calibration or quality-control procedures are current and whether any recent QC test showed abnormal results.

If an approved operator-level or Clinical Engineering QC procedure is appropriate, perform it using designated phantoms and test equipment.

**Expected outcome:** Quality-control results are acceptable and do not reproduce the image-quality problem.

If QC passes and the external cause has been corrected, proceed to final verification.

### 9. Verify Image Quality Before Return to Service

Use approved test procedures to verify the affected modality.

Confirm:

- No reproducible unexplained artifact remains
- Images reconstruct normally
- PET / CT registration is appropriate when applicable
- No new fault appears
- Required QC criteria are met

**Expected outcome:** Image quality is acceptable according to applicable department and manufacturer requirements.

If required image-quality testing passes, troubleshooting can stop and the scanner may be returned to service.

## If the Problem Persists

If patient motion, positioning, external objects, accessories, protocol selection, accessible contamination, and approved quality-control checks have been ruled out but artifacts persist, the cause may involve detector performance, calibration, acquisition electronics, reconstruction, motion correction, PET / CT registration, mechanical alignment, or another service-level condition.

The system should be:

- Removed from service when image reliability is uncertain
- Labeled Out of Service
- Sent for repair or formal system evaluation
- Evaluated using appropriate GE Healthcare documentation, phantoms, and approved test equipment
- Calibrated, repaired, or configured only by qualified personnel

Do not compensate for unexplained system artifacts by changing clinical settings without determining the cause.

Following service, complete required image-quality and calibration testing before return to clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Compare questionable PET / CT images with positioning, motion, accessories, and recent QC results before repeating a patient scan or assuming detector failure.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Poor image quality should be investigated systematically before internal failure is assumed. Protect the patient from unnecessary repeat imaging, verify positioning, motion, accessories, protocol selection, and QC status, and escalate when a reproducible artifact remains unexplained.

That is successful troubleshooting.
