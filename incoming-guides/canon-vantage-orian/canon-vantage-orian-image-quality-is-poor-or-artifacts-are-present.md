---
schemaVersion: 1
title: "Canon Vantage Orian MRI System - Image Quality Is Poor or Artifacts Are Present"
issueTitle: "Image Quality Is Poor or Artifacts Are Present"
description: "Addresses degraded MRI images and artifacts caused by positioning, motion, coils, accessories, external interference, setup, or environmental conditions."
assetType: "MRI System"
manufacturer: "Canon"
model: "Vantage Orian"
slug: "canon-vantage-orian-image-quality-is-poor-or-artifacts-are-present"
dateAdded: "2026-09-25"
taxonomyMode: "reuse"
ccr:
  complaint: "MRI staff reported localized signal loss on examinations performed with one imaging coil."
  cause: "Clinical Engineering reproduced the problem with that coil and obtained normal images using a known-good compatible coil."
  resolution: "Removed the affected coil from service and verified acceptable image quality with the known-good coil using the approved test workflow."
helpfulDetails:
  - "Description of artifact"
  - "Anatomy or exam involved"
  - "Coil used"
  - "Patient motion observed"
  - "Coil placement"
  - "Known-good coil comparison"
  - "External equipment recently added"
  - "Protocol or orientation used"
  - "QC or phantom result"
  - "Final image-quality status"
---
## What This Guide Helps With
Addresses degraded MRI images and artifacts caused by positioning, motion, coils, accessories, external interference, setup, or environmental conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Confirm Clinical Usability
If images are unreliable for diagnosis, do not continue using the scanner as though image quality is acceptable. Coordinate an alternate imaging pathway if necessary.

**Expected outcome:** Clinical decisions are not based on known unreliable images.

### 2. Characterize the Image Problem
Determine whether the complaint involves noise, shading, signal loss, ghosting, distortion, banding, unusual bright or dark areas, or another visible artifact.

Determine whether it affects every study, one coil, one exam type, or one patient.

**Expected outcome:** The artifact pattern and affected workflows are clearly identified without prematurely assigning a cause.

### 3. Verify Patient Positioning and Motion Factors
Review patient positioning, immobilization, comfort, and the likelihood of voluntary or involuntary movement during the examination.

**Expected outcome:** Positioning is appropriate and obvious motion-related causes are corrected when possible.

If image quality becomes normal after correcting patient positioning or motion, troubleshooting can stop after verification.

### 4. Inspect the Coil and Coil Placement
Check the selected MRI coil for visible damage and confirm it is positioned correctly for the intended anatomy.

Verify coil elements, cables, and accessories are not compressed, sharply bent, trapped, or improperly arranged.

**Expected outcome:** The coil is intact, correctly positioned, and properly connected.

### 5. Compare With a Known-Good Coil or Setup
When appropriate, repeat an approved test using another compatible known-good coil or established test setup.

**Expected outcome:** The comparison shows whether the image-quality problem follows a specific coil/accessory or remains with the scanner.

If the problem follows one coil, remove that coil from service.

### 6. Check External Items in the Scan Environment
Look for newly introduced equipment, cables, accessories, powered devices, or other changes in or near the MRI environment that could contribute to interference or image degradation.

Follow MRI safety rules when removing or relocating equipment.

**Expected outcome:** No obvious external interference source remains.

### 7. Verify Routine Scan Setup
Check operator-visible protocol selection, coil selection, patient orientation, field positioning, and other routine exam parameters for accidental mismatch.

Do not alter restricted calibration or service settings.

**Expected outcome:** The examination is configured correctly for the intended acquisition.

### 8. Determine Whether the Problem Is Reproducible
Using an approved quality-control phantom or established test process when available, determine whether the reported artifact can be reproduced independent of the original patient.

**Expected outcome:** The problem is identified as patient/setup-specific or scanner/accessory-related.

### 9. Perform Final Image-Quality Verification
After correcting an external cause, verify that an approved test or quality-control acquisition produces expected image quality without the reported artifact.

**Expected outcome:** Image quality is restored and the original artifact is no longer present.

If achieved, troubleshooting can stop.

### 10. Escalate Persistent Image-Quality Problems
If the artifact remains across known-good coils, appropriate test setups, and multiple approved acquisitions, remove the scanner from service or restrict use according to facility policy until qualified evaluation is completed.

Do not adjust internal RF, gradient, shim, magnet, or calibration parameters outside authorized procedures.

**Expected outcome:** Persistent quality problems are escalated without unauthorized internal adjustment.

## If the Problem Persists

Common patient-positioning, motion, coil, accessory, scan-setup, and external-interference causes have been ruled out. The remaining issue may involve RF performance, gradient performance, magnet homogeneity, calibration, system configuration, shielding integrity, or another service-level condition.

The MRI system should be:

- Removed from service when image quality cannot be relied upon
- Labeled Out of Service
- Sent for qualified evaluation
- Evaluated using appropriate Canon documentation and approved MRI quality-assurance test equipment
- Repaired, calibrated, or configured only by qualified personnel

Complete appropriate image-quality and system verification before return to clinical use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

When evaluating an artifact, determine whether it follows the patient, the coil, the protocol, or the scanner before assuming a hardware failure.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Image artifacts should be approached methodically by separating patient, coil, setup, environmental, and scanner causes. Verify the correction with an appropriate image-quality check, escalate persistent problems, and document findings without assuming an internal failure too early.

That is successful troubleshooting.
