---
schemaVersion: 1
title: "Carestream DRX-Rise Mobile X-Ray System - Image Has Dead Pixels, Bands, Lag, or Calibration Nonuniformity"
issueTitle: "Image Has Dead Pixels, Bands, Lag, or Calibration Nonuniformity"
description: "Troubleshoot image artifacts caused by detector condition, contamination, processing, positioning, calibration state, wireless transfer, or detector-specific faults."
assetType: "Mobile X-Ray System"
manufacturer: "Carestream"
model: "DRX-Rise"
slug: "carestream-drx-rise-image-has-dead-pixels-bands-lag-or-calibration-nonuniformity"
dateAdded: "2026-11-18"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported a repeatable dark band across images acquired with one DRX-Rise detector."
  cause: "Clinical Engineering found the artifact followed the same detector during a known-good detector comparison and remained after approved calibration."
  resolution: "Removed the affected detector from service, provided a verified replacement detector, and documented the failed image-quality testing for repair evaluation."
helpfulDetails:
  - "Artifact appearance and orientation"
  - "Whether artifact is fixed or intermittent"
  - "Detector identification"
  - "Detector physical condition"
  - "Recent impact or fluid exposure"
  - "Known-good detector comparison"
  - "Calibration status"
  - "Test phantom used"
  - "Console versus PACS appearance"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoot image artifacts caused by detector condition, contamination, processing, positioning, calibration state, wireless transfer, or detector-specific faults.

## Step-by-Step Troubleshooting

### 1. Protect Diagnostic Image Quality
Do not continue clinical imaging with artifacts that could obscure anatomy or simulate pathology. Move examinations to another verified detector or system when necessary.  
Expected outcome: Patient diagnosis does not depend on compromised image quality.

### 2. Confirm the Artifact Pattern
Determine whether the image shows fixed dead pixels, horizontal or vertical bands, ghosting/lag, nonuniform shading, intermittent dropout, or an artifact only in certain examinations.  
Expected outcome: The artifact is clearly characterized and reproducible if possible.

### 3. Inspect the Detector Externally
Check the detector surface and protective cover for contamination, fluid, debris, cracks, impact damage, warping, or attached objects that could produce artifacts.  
Expected outcome: Detector is clean, intact, and free of external artifact sources.

### 4. Check Acquisition Conditions
Verify the detector is positioned normally and not partially shielded by rails, cables, holders, accessories, or unintended objects.  
Expected outcome: The detector has an unobstructed and appropriate acquisition setup.

### 5. Determine Whether the Artifact Follows the Detector
If another compatible detector is available, acquire an approved test image under comparable conditions.  
Expected outcome: The comparison shows whether the artifact follows one detector or remains with the DRX-Rise system.

### 6. Review Recent Detector Events
Ask whether the detector was recently dropped, exposed to fluid, stored improperly, deeply discharged, or used immediately after an unusual high-exposure sequence.  
Expected outcome: A relevant external event is identified or reasonably excluded.

### 7. Verify Approved Calibration Status
Determine whether the system indicates that a normal detector calibration or correction procedure is due or incomplete. Perform only authorized calibration procedures using approved methods.  
Expected outcome: Detector calibration completes normally and subsequent test images are uniform.

### 8. Repeat a Controlled Image-Quality Test
Using approved imaging phantoms or test methods, acquire images under consistent conditions and compare artifact location and severity.  
Expected outcome: Image is free of clinically significant fixed artifacts. If the problem is no longer present and verification passes, troubleshooting can stop.

### 9. Check Image Display Versus Acquired Data
If practical, compare the image on the acquisition console with the received image at another approved viewing destination.  
Expected outcome: The problem is isolated to acquisition, processing, transfer, or display rather than assumed to be detector damage.

### 10. Escalate Persistent Image Artifacts
If fixed pixels, banding, lag, or nonuniformity remain after external checks and approved calibration, remove the affected detector or system from clinical use.  
Expected outcome: Unreliable image-quality equipment is withheld until service evaluation is completed.

## If the Problem Persists

Common external and calibration-related causes have been ruled out. Remaining categories include detector electronics, detector correction data, image-processing software, communication hardware, acquisition system hardware, or service-level calibration issues.

Remove the affected equipment from service, label it **Out of Service**, and send it for repair or bench evaluation. Use appropriate Carestream documentation, approved image-quality phantoms, and test equipment.

Return to service should include successful detector calibration where applicable and documented image-quality verification.

Knowing when persistent artifacts require detector or system escalation is proper troubleshooting.

## Clinical Use Tip

Treat repeatable image artifacts as a patient-safety concern when they could hide anatomy or resemble clinical findings.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Image quality directly affects diagnosis, so verify simple detector and acquisition causes first, use approved calibration and comparison tests, and remove persistent artifact sources from service.

That is successful troubleshooting.
