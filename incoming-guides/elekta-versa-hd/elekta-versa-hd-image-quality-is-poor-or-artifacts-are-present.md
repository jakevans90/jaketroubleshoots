---
schemaVersion: 1
title: "Elekta Versa HD Radiation Therapy System - Image Quality Is Poor or Artifacts Are Present"
issueTitle: "Image Quality Is Poor or Artifacts Are Present"
description: "Acquired images are degraded, inconsistent, or contain artifacts caused by positioning, accessories, contamination, setup, calibration state, or acquisition-path problems."
assetType: "Radiation Therapy System"
manufacturer: "Elekta"
model: "Versa HD"
slug: "elekta-versa-hd-image-quality-is-poor-or-artifacts-are-present"
dateAdded: "2026-10-01"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiation Oncology reported a repeatable artifact on Versa HD verification images that affected image interpretation."
  cause: "Clinical Engineering found an external positioning accessory unintentionally within the imaging field."
  resolution: "Clinical Engineering repositioned the accessory, repeated the approved QC acquisition, and verified that the artifact was no longer present before return to service."
helpfulDetails:
  - "Artifact appearance and location"
  - "Workflows affected"
  - "Whether issue is repeatable"
  - "Accessories present"
  - "Detector position and condition"
  - "QC test image results"
  - "Display or workstation used"
  - "Recent room or equipment changes"
  - "Results before and after correction"
  - "Final image-quality status"
---
## What This Guide Helps With

Acquired images are degraded, inconsistent, or contain artifacts caused by positioning, accessories, contamination, setup, calibration state, or acquisition-path problems.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Decision-Making

Do not use images of questionable quality for patient positioning, verification, or treatment decisions.

If clinically necessary, use an alternate verified method according to departmental procedures.

**Expected outcome:** No patient treatment decision relies on an image known to be unreliable.

### 2. Confirm the Image-Quality Complaint

Review the affected image and determine whether the issue is noise, banding, streaking, distortion, missing areas, repeated patterns, poor contrast, or another visible abnormality.

Determine whether the issue affects every image or only certain workflows.

**Expected outcome:** The artifact is clearly characterized and its reproducibility is understood.

### 3. Check Patient and Accessory Positioning

Confirm that patient supports, immobilization devices, treatment accessories, cables, clothing items, or other objects are not unexpectedly within the imaging field.

**Expected outcome:** No avoidable external object or setup condition is causing the artifact.

### 4. Inspect Accessible Detector Surfaces and Components

Inspect accessible detector covers and imaging surfaces for contamination, damage, foreign material, or obvious obstruction.

Clean only according to approved procedures.

**Expected outcome:** Accessible imaging surfaces are clean and physically intact.

### 5. Verify Detector and Equipment Position

Confirm that imaging hardware is fully deployed or positioned as required and that no obvious misalignment or mechanical interference is present.

**Expected outcome:** Imaging components are correctly positioned for acquisition.

### 6. Verify Acquisition Setup

Confirm that the intended imaging workflow and appropriate clinical acquisition selection are being used.

Compare the issue with another appropriate approved acquisition setup when possible, without changing parameters merely to mask the problem.

**Expected outcome:** Poor image quality is not the result of an incorrect workflow or unintended selection.

### 7. Compare With an Approved Test Object or QC Image

Acquire an approved quality-control image or use an appropriate test object to determine whether the artifact persists without the patient.

**Expected outcome:** If the artifact disappears, investigate patient setup or external objects. If it remains, the issue is likely within the imaging path or system environment.

### 8. Check Environment and External Interference

Look for recent equipment changes, nearby electronic devices, cable routing changes, construction, power events, or other environmental changes that coincide with the complaint.

**Expected outcome:** No external environmental change explains the image degradation.

### 9. Verify Image Display Path

Compare the image on an appropriate local display or workstation when available to distinguish acquisition artifacts from display or transfer issues.

**Expected outcome:** The artifact can be localized to acquisition or display/communication rather than assumed to originate from the detector.

### 10. Perform Final Image Verification

After correction of an external cause, repeat an approved QC image and confirm normal image appearance and consistency.

**Expected outcome:** The image meets the department's approved acceptance criteria. Troubleshooting can stop after required verification is complete.

### 11. Escalate Persistent Image-Quality Problems

If artifacts remain after setup, accessories, detector condition, positioning, workflow, environment, and display path are checked, stop troubleshooting.

**Expected outcome:** The imaging function is withheld from clinical use until qualified evaluation is completed.

## If the Problem Persists

External causes have been ruled out. Remaining possibilities may include detector performance, calibration, imaging electronics, synchronization, internal communication, reconstruction, or other service-level imaging problems.

The Versa HD should be:

- Removed from affected clinical imaging use.
- Labeled Out of Service when image integrity cannot be assured.
- Sent for qualified repair or service evaluation.
- Evaluated using appropriate Elekta documentation and approved imaging test equipment.
- Repaired, calibrated, or configured only by qualified personnel.

Required image-quality and treatment-system checks must be completed before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

An image that looks usable is not necessarily suitable for treatment guidance; verify questionable image quality with approved QC methods before clinical use.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Treat questionable image quality as a patient-safety issue. Rule out positioning, accessories, contamination, workflow, environment, and display-path causes before assuming an internal imaging failure, and verify the correction objectively.

That is successful troubleshooting.
