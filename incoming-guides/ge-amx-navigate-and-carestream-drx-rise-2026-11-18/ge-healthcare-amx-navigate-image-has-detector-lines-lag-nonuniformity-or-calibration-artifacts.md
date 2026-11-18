---
schemaVersion: 1
title: "GE Healthcare AMX Navigate Mobile X-Ray System - Image Has Detector Lines, Lag, Nonuniformity, or Calibration Artifacts"
issueTitle: "Image Has Detector Lines, Lag, Nonuniformity, or Calibration Artifacts"
description: "Acquired images show lines, residual images, uneven response, fixed artifacts, or other detector-related image-quality abnormalities."
assetType: "Mobile X-Ray System"
manufacturer: "GE Healthcare"
model: "AMX Navigate"
slug: "ge-healthcare-amx-navigate-image-has-detector-lines-lag-nonuniformity-or-calibration-artifacts"
dateAdded: "2026-11-18"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported a fixed vertical line appeared in the same location on images acquired with one AMX Navigate detector."
  cause: "Clinical Engineering reproduced the artifact on a non-patient test image and confirmed it followed the detector when compared with a known-good detector."
  resolution: "Removed the affected detector from service for repair and verified artifact-free imaging on the AMX Navigate using the known-good detector."
helpfulDetails:
  - "Artifact type"
  - "Whether artifact is fixed or intermittent"
  - "Detector identification"
  - "Physical damage"
  - "Surface contamination"
  - "Detector battery state"
  - "Detector orientation test"
  - "Known-good detector comparison"
  - "Calibration performed"
  - "Test-image result"
  - "Final detector status"
  - "Final system status"
---

## What This Guide Helps With

Acquired images show lines, residual images, uneven response, fixed artifacts, or other detector-related image-quality abnormalities.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Unnecessary Repeat Exposure
Do not repeatedly expose a patient to determine whether an image artifact is reproducible. Move to an alternate verified detector or system when clinically necessary.

Expected outcome: Image-quality troubleshooting does not create unnecessary patient dose.

### 2. Characterize the Artifact
Determine whether the artifact is:
- A fixed line
- Multiple lines
- Residual or lag image
- Uniformity variation
- A localized defect
- Edge-related
- Intermittent
- Present on every image

Record whether the artifact remains in the same detector location.

Expected outcome: The artifact pattern is clearly described.

### 3. Inspect the Detector Surface
Check the detector and any protective cover for:
- Debris
- Fluid
- Tape residue
- Cracks
- Impact damage
- Objects lying on or beneath the detector

Expected outcome: No external material is creating an image artifact.

### 4. Verify Detector Positioning
Confirm the detector is correctly positioned and not being flexed, compressed, or improperly supported during testing.

Expected outcome: Mechanical positioning is not contributing to the image abnormality.

### 5. Verify Detector Communication and Battery Condition
Confirm the detector is stably connected and has adequate battery power.

Expected outcome: Communication or low-power instability is not contributing to the problem.

### 6. Acquire an Approved Test Image
Using appropriate test material and no patient, obtain an image under controlled conditions.

Expected outcome: The artifact is either reproduced or ruled out without involving a patient.

### 7. Rotate or Reposition the Detector
Change detector orientation relative to the test object while maintaining an appropriate controlled setup.

- If the artifact moves with the detector, suspect the detector or detector calibration.
- If the artifact remains fixed relative to the object or geometry, investigate the imaging setup or another system component.

Expected outcome: The test helps localize the artifact source.

### 8. Compare With a Known-Good Detector
Use a compatible known-good detector on the same AMX Navigate.

Expected outcome: If the artifact disappears, the original detector is isolated as the likely source. If it remains, evaluate the system or acquisition path.

### 9. Perform Approved Calibration or Quality-Control Functions
If normal Clinical Engineering responsibility includes approved detector calibration or quality-control procedures, perform only those documented procedures using the proper conditions and test equipment.

Do not improvise calibration steps or alter protected service parameters.

Expected outcome: The detector completes the approved procedure and subsequent test images are uniform.

### 10. Verify Image Quality After Correction
Acquire a controlled non-patient test image and confirm that lines, lag, or nonuniformity are no longer present.

Expected outcome: Image quality is acceptable and repeatable. Troubleshooting can stop.

### 11. Escalate Persistent Image Artifacts
If the artifact follows a detector, remains after approved calibration, or cannot be isolated through external testing, remove the affected detector or system from service.

Expected outcome: Equipment producing unreliable diagnostic images is not returned to patient use.

## If the Problem Persists

Common external and acquisition causes have been ruled out. Remaining possibilities may involve detector electronics, detector calibration, internal image-processing functions, generator consistency, software, or another service-level imaging component.

The affected equipment should be:
- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved imaging test equipment
- Repaired or calibrated only by qualified personnel

Return-to-service testing should confirm acceptable image quality over appropriate controlled test conditions.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Use a test object rather than a patient when determining whether an image artifact follows the detector.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Image artifacts should be isolated methodically without creating unnecessary repeat exposures. Confirm the detector, positioning, environment, and known-good comparison before assuming an internal imaging-system failure.

That is successful troubleshooting.
