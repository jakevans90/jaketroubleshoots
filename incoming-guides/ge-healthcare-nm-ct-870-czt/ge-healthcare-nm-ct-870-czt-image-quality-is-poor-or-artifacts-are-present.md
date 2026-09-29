---
schemaVersion: 1
title: "GE Healthcare NM/CT 870 CZT PET / CT System - Image Quality Is Poor or Artifacts Are Present"
issueTitle: "Image Quality Is Poor or Artifacts Are Present"
description: "Images show unexpected artifacts, distortion, noise, nonuniformity, or degraded quality caused by positioning, motion, accessories, contamination, setup, or system performance."
assetType: "PET / CT System"
manufacturer: "GE Healthcare"
model: "NM/CT 870 CZT"
slug: "ge-healthcare-nm-ct-870-czt-image-quality-is-poor-or-artifacts-are-present"
dateAdded: "2026-09-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Imaging staff reported a recurring artifact on NM/CT 870 CZT studies that was not present on previous examinations."
  cause: "Clinical Engineering found an external positioning item had been left within the imaging field during the affected studies."
  resolution: "Clinical Engineering removed the item, completed the appropriate image-quality check, verified normal images, and returned the system to service."
helpfulDetails:
  - "Description and location of artifact"
  - "CT, nuclear medicine, or fused images affected"
  - "Whether artifact follows a detector or protocol"
  - "Patient motion observed"
  - "Accessories in imaging field"
  - "Protocol and reconstruction used"
  - "Phantom or QC test result"
  - "Environmental changes"
  - "Scanner versus PACS appearance"
  - "Final image-quality status"
---
## What This Guide Helps With

Images show unexpected artifacts, distortion, noise, nonuniformity, or degraded quality caused by positioning, motion, accessories, contamination, setup, or system performance.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Avoid Unnecessary Repeat Imaging

Do not repeatedly rescan a patient while the source of an image-quality problem is unknown. If images are not clinically reliable, stop using the affected acquisition mode until the system is evaluated.

**Expected outcome:** Additional unnecessary exposure or unusable imaging is avoided.

### 2. Define the Artifact Precisely

Review the affected images with qualified imaging staff and determine whether the problem affects nuclear medicine images, CT images, fused images, or all modalities.

Document whether the artifact is fixed in position, patient-dependent, intermittent, protocol-specific, or present across multiple studies.

**Expected outcome:** The artifact is characterized well enough to guide troubleshooting rather than being described only as “poor image quality.”

### 3. Check Patient Motion and Positioning

Review whether patient movement, incorrect centering, positioning aids, arms, clothing, external objects, or other patient-related factors could explain the appearance.

**Expected outcome:** Patient positioning and motion are either identified as the cause or reasonably excluded.

### 4. Inspect Accessories and Imaging Path

Check pads, straps, immobilization devices, detector surfaces, table accessories, cables, and removable items within or near the imaging field.

Look for contamination, misplaced objects, fluid, debris, or damaged accessories.

**Expected outcome:** Nothing external is unintentionally contributing to the image artifact. If removal or repositioning corrects the problem, verify with appropriate testing and troubleshooting can stop.

### 5. Verify Protocol and Acquisition Setup

Confirm the intended protocol, acquisition mode, reconstruction selection, patient orientation, study information, and other normal operator-visible settings.

Compare with a known-good protocol or prior successful study when appropriate. Do not alter protected configuration to chase an artifact.

**Expected outcome:** The examination setup matches the intended clinical application.

### 6. Determine Whether the Problem Follows a Particular Detector or Acquisition Mode

Using approved test methods, determine whether the artifact appears consistently with a particular detector position, CT acquisition, nuclear medicine acquisition, or reconstruction path.

Do not perform internal detector adjustments.

**Expected outcome:** The problem is localized to a workflow, modality, or detector-related condition without invasive troubleshooting.

### 7. Perform Required Quality-Control Checks

Run the appropriate manufacturer- and site-approved image-quality or quality-control test using the designated phantom or test object.

Do not substitute informal visual judgment for required QC when assessing system performance.

**Expected outcome:** The system either passes required QC or provides objective evidence that additional service is required.

### 8. Check for Environmental or External Interference

Inspect for recent room changes, construction, unusual vibration, HVAC problems, equipment moved near the scanner, or other environmental changes that correlate with the artifact.

**Expected outcome:** No identifiable external environmental change is degrading imaging performance.

### 9. Verify Image Display and Transfer Path

Compare images on the acquisition workstation and destination viewing system when appropriate.

A display, processing, transfer, or hanging-protocol issue can resemble acquisition degradation.

**Expected outcome:** The artifact is confirmed to originate in the appropriate portion of the imaging chain. If images are correct at the scanner but altered downstream, escalate the downstream system instead of the scanner.

### 10. Escalate Persistent Image-Quality Problems

If positioning, accessories, protocol, display, environment, and approved QC checks do not resolve the problem, remove the affected system or acquisition mode from service as appropriate.

Do not perform internal detector alignment, detector module replacement, CT calibration adjustment, or reconstruction-system repair without authorized service procedures.

**Expected outcome:** Clinically unreliable imaging is prevented from returning to use until qualified service and QC are complete.

## If the Problem Persists

Common external causes including patient motion, positioning, accessories, contamination, protocol selection, environment, and downstream display have been ruled out. Remaining categories may include detector performance, CT acquisition hardware, calibration, alignment, reconstruction software, internal communication, or other service-level conditions.

The device should be:

- Removed from service when image quality cannot be trusted.
- Labeled Out of Service.
- Sent for repair or system evaluation.
- Evaluated using appropriate GE Healthcare documentation, approved phantoms, and test equipment.
- Repaired, calibrated, or configured only by qualified personnel.

Required image-quality and quality-control tests must pass before return to clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Confirm whether an artifact is present at the acquisition workstation before assuming the scanner caused an appearance seen only on a downstream viewer.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Protect patients from unnecessary repeat imaging, characterize artifacts before troubleshooting, eliminate positioning and external causes first, verify correction objectively, and escalate whenever image quality cannot be trusted.

That is successful troubleshooting.
