---
schemaVersion: 1
title: "United Imaging uMR 790 MRI System - Image Quality Is Poor or Artifacts Are Present"
issueTitle: "Image Quality Is Poor or Artifacts Are Present"
description: "Troubleshoots degraded MRI images and artifacts caused by patient motion, positioning, coils, external interference, accessories, protocol selection, or environmental factors."
assetType: "MRI System"
manufacturer: "United Imaging"
model: "uMR 790"
slug: "united-imaging-umr-790-image-quality-is-poor-or-artifacts-are-present"
dateAdded: "2026-09-25"
taxonomyMode: "reuse"
ccr:
  complaint: "MRI staff reported localized signal loss on uMR 790 studies performed with one specific imaging coil."
  cause: "Clinical Engineering reproduced the problem with the reported coil and obtained normal images using a known-good compatible coil."
  resolution: "The suspect coil was removed from service, normal image quality was verified with the known-good coil, and the MRI system was returned to use."
helpfulDetails:
  - "Description of artifact"
  - "Example images or study reference"
  - "Coil used"
  - "Patient position"
  - "Protocol or sequence"
  - "Known-good coil comparison"
  - "Phantom or QC result"
  - "Environmental changes"
  - "Whether artifact is reproducible"
  - "Final image-quality status"
---
## What This Guide Helps With

Troubleshoots degraded MRI images and artifacts caused by patient motion, positioning, coils, external interference, accessories, protocol selection, or environmental factors.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Avoid Unnecessary Repeat Scans
Do not repeatedly scan a patient while investigating unexplained image degradation.

Determine whether imaging can safely continue or whether the patient should be removed and the scanner evaluated using a nonpatient test method.

**Expected outcome:** Patient exposure to unnecessary repeat examinations and prolonged scan time is minimized.

### 2. Define the Image-Quality Problem
Determine whether the reported issue is:
- Motion artifact
- Signal loss
- Uneven signal
- Noise
- Distortion
- Repeating artifact
- Poor quality in one region
- Present only with one coil, protocol, or exam type

Review representative images if available.

**Expected outcome:** The artifact pattern and affected workflow are clearly identified.

### 3. Check Patient Motion and Positioning
Confirm:
- Patient remained still
- Region of interest was positioned appropriately
- Immobilization aids were used correctly when applicable
- No cable or accessory created discomfort or encouraged movement

**Expected outcome:** Patient setup is stable and repeatable. If correcting positioning eliminates the artifact, verify image quality and stop.

### 4. Inspect the RF Coil and Connections
Check the selected coil for:
- Correct placement
- Secure connections
- Visible damage
- Cable strain
- Contamination
- Inconsistent recognition

If appropriate, compare performance using a known-good compatible coil.

**Expected outcome:** The coil and connection are verified as suitable. If the artifact follows one external coil, remove that coil from service and stop after confirming normal images with a known-good component.

### 5. Remove Unnecessary External Items
Check for removable objects or accessories near the imaging region that could contribute to artifact or signal distortion.

Follow MRI safety requirements at all times.

**Expected outcome:** No avoidable external object is contributing to image degradation. If removing an item resolves the artifact, verify image quality and stop.

### 6. Verify Normal Protocol and Setup
Confirm that the intended exam protocol, coil selection, patient orientation, and normal user-selectable settings match the clinical examination.

Do not alter service-level calibration or protected configuration.

**Expected outcome:** Imaging setup is appropriate. If an incorrect normal setup was responsible, repeat an approved test and stop when quality is restored.

### 7. Determine Whether the Problem Is Reproducible
Use an approved MRI phantom or quality-control test method if available.

Determine whether the artifact:
- Appears without a patient
- Occurs with multiple coils
- Occurs only in one scan type
- Changes with patient positioning
- Is intermittent

**Expected outcome:** The issue is narrowed to patient/setup, accessory, or system-level behavior.

### 8. Check for Environmental or Facility Changes
Ask whether there has been:
- Construction
- New equipment nearby
- Electrical work
- Changes in adjacent rooms
- Recently introduced devices or accessories
- Changes to room doors or shielding-related conditions

Do not independently modify RF shielding or facility systems.

**Expected outcome:** No obvious environmental change is correlated with the artifact. If one is identified, coordinate appropriate facility or vendor evaluation.

### 9. Verify Image Quality After Correction
Repeat the approved test condition that originally showed the artifact.

Confirm images are consistent and acceptable using the site's normal quality process.

**Expected outcome:** The artifact is no longer present and image quality is stable. Troubleshooting can stop.

### 10. Escalate Persistent Image-Quality Problems
If positioning, patient motion, coils, protocol setup, and obvious environmental causes have been ruled out, remove the MRI system from routine clinical use until qualified evaluation occurs.

**Expected outcome:** The imaging system is prevented from producing potentially unreliable diagnostic images.

## If the Problem Persists

Remaining causes may involve internal RF, gradient, acquisition, calibration, shielding, magnet-related, reconstruction, or other service-level conditions.

The device should be:
- Removed from service
- Labeled **Out of Service**
- Sent for repair or service evaluation
- Evaluated using United Imaging documentation, approved phantoms, and qualified MRI test equipment
- Repaired or configured only by qualified personnel

Do not compensate for unexplained artifacts by repeatedly modifying clinical settings without identifying the cause.

Knowing when to stop external troubleshooting is proper troubleshooting. Return the system to service only after appropriate image-quality verification has passed.

## Clinical Use Tip

When an artifact appears unexpectedly, preserve representative images and document the exact coil, protocol, setup, and room conditions before changing anything.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Poor MRI image quality requires disciplined isolation of patient, accessory, setup, and environmental causes before internal system failure is assumed. Preserve evidence, verify the correction objectively, and escalate unexplained artifacts.

That is successful troubleshooting.
