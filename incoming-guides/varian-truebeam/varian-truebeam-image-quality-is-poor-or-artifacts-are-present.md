---
schemaVersion: 1
title: "Varian TrueBeam Radiation Therapy System - Image Quality Is Poor or Artifacts Are Present"
issueTitle: "Image Quality Is Poor or Artifacts Are Present"
description: "TrueBeam imaging shows unexpected artifacts, reduced clarity, inconsistent appearance, or image quality that may affect positioning or clinical interpretation."
assetType: "Radiation Therapy System"
manufacturer: "Varian"
model: "TrueBeam"
slug: "varian-truebeam-image-quality-is-poor-or-artifacts-are-present"
dateAdded: "2026-09-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported a repeatable artifact on TrueBeam positioning images."
  cause: "Clinical Engineering found an external positioning accessory extending into the imaging field during acquisition."
  resolution: "Clinical Engineering repositioned the accessory and verified that repeat quality-control images were free of the reported artifact."
helpfulDetails:
  - "Description and location of artifact"
  - "Imaging mode affected"
  - "Whether artifact is repeatable"
  - "Patient or accessory positioning"
  - "Detector surface condition"
  - "Recent room or equipment changes"
  - "Controlled test-image result"
  - "Before-and-after images available"
  - "Medical Physics involvement"
  - "Final quality-control result"
  - "Final system status"
---
## What This Guide Helps With

TrueBeam imaging shows unexpected artifacts, reduced clarity, inconsistent appearance, or image quality that may affect positioning or clinical interpretation.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Suspend Questionable Imaging Use
If image quality could affect patient positioning, verification, or clinical decision-making, stop using the affected imaging function for treatment guidance until it is verified.

**Expected outcome:** Poor-quality imaging is not relied upon for patient treatment decisions.

### 2. Characterize the Image Problem
Determine whether the issue is noise, lines, bands, shading, distortion, clipping, missing image areas, motion artifact, inconsistent contrast, or another repeatable abnormality. Record whether the artifact occurs on every image or only specific workflows.

**Expected outcome:** The artifact is described in a reproducible way.

### 3. Review Patient and Accessory Positioning
Check for external objects, immobilization hardware, metallic items, cables, table attachments, or accessories within the imaging field that could create artifacts.

**Expected outcome:** No avoidable external object is contributing to image degradation.

### 4. Inspect Accessible Imaging Hardware
Check externally visible detector or imaging surfaces for contamination, physical obstruction, damage, or improper position. Clean only according to approved procedures.

**Expected outcome:** Imaging surfaces and accessible hardware are clean, intact, and correctly positioned.

### 5. Verify the Correct Imaging Workflow
Confirm that the intended imaging mode, protocol, and user-accessible settings are selected for the planned procedure. Compare with a known normal workflow when appropriate.

Do not alter treatment-planning or calibration parameters as a troubleshooting shortcut.

**Expected outcome:** The expected clinical imaging configuration is being used.

### 6. Check for Environmental or External Interference
Determine whether recent equipment additions, cable routing changes, room work, or other environmental changes correlate with the artifact.

**Expected outcome:** External environmental contributors are either identified or reasonably excluded.

### 7. Compare With a Controlled Test Image
Perform an approved phantom, quality-control, or other non-patient imaging check appropriate to the facility.

**Expected outcome:** The artifact either disappears, confirming an external/patient-related cause, or remains reproducible and requires further evaluation.

### 8. Repeat After Correcting Any External Cause
If an accessory, positioning condition, contamination, or other external factor is identified, correct it and repeat the approved verification image.

**Expected outcome:** Image quality returns to the facility's accepted clinical condition. If so, troubleshooting can stop.

### 9. Escalate Persistent or Unexplained Artifacts
If the artifact persists during controlled verification or image quality cannot be confidently accepted, remove the affected imaging function or system from clinical service.

**Expected outcome:** Unverified imaging is not used for patient positioning or treatment decisions.

## If the Problem Persists

External objects, positioning, imaging surfaces, workflow selection, and environmental contributors have been ruled out. Remaining causes may involve detector calibration, imaging electronics, geometry, acquisition software, image processing, or another internal subsystem.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or appropriate service evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired, calibrated, or configured only by qualified personnel

Return to service should include appropriate imaging quality-control verification and any required review by qualified Radiation Oncology or Medical Physics personnel.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

An image that appears usable at first glance may still be unacceptable for image-guided treatment if an unexplained artifact affects positioning accuracy.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Image-quality complaints should be reproduced and isolated systematically. Rule out positioning, accessories, contamination, workflow, and environmental causes before assuming detector failure, and require appropriate quality verification before clinical reuse.

That is successful troubleshooting.
