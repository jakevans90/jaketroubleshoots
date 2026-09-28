---
schemaVersion: 1
title: "Siemens Healthineers Biograph Vision PET / CT System - Image Quality Is Poor or Artifacts Are Present"
issueTitle: "Image Quality Is Poor or Artifacts Are Present"
description: "Use this guide when PET or CT images show artifacts, unexpected noise, distortion, misregistration, or inconsistent quality caused by positioning, accessories, motion, or system conditions."
assetType: "PET / CT System"
manufacturer: "Siemens Healthineers"
model: "Biograph Vision"
slug: "siemens-healthineers-biograph-vision-image-quality-is-poor-or-artifacts-are-present"
dateAdded: "2026-09-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported a recurring artifact visible on CT images acquired with the Biograph Vision."
  cause: "Clinical Engineering found a positioning accessory containing dense material had been left within the scan field."
  resolution: "Clinical Engineering removed the accessory, repeated an approved test acquisition, verified the artifact was absent, and returned the system to service."
helpfulDetails:
  - "PET, CT, or fused images affected"
  - "Artifact appearance and location"
  - "Studies or protocols affected"
  - "Patient-motion observations"
  - "Accessories present"
  - "Recent service or environmental change"
  - "Whether artifact moves with patient position"
  - "QC result"
  - "Test-object result"
  - "Final image-quality status"
---
## What This Guide Helps With

Use this guide when PET or CT images show artifacts, unexpected noise, distortion, misregistration, or inconsistent quality caused by positioning, accessories, motion, or system conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Avoid Unnecessary Repeat Imaging

Do not repeatedly rescan a patient solely to investigate unexplained image-quality problems, particularly when additional CT exposure would result.

Use existing images, approved phantoms, and non-patient test methods whenever possible.

**Expected outcome:** Patient safety and radiation exposure remain controlled while troubleshooting proceeds.

### 2. Characterize the Artifact

Determine:

- Whether the artifact is on PET, CT, or fused images.
- Whether it occurs in every study or only one patient.
- Whether it appears in the same image location.
- Whether it changes with positioning.
- Whether it began suddenly.
- Whether there was recent calibration, service, room work, or accessory change.

Retain representative images when permitted by facility policy.

**Expected outcome:** The artifact pattern and conditions are clearly defined.

If the artifact is confirmed to be patient-specific and system quality checks remain normal, no equipment repair may be required.

### 3. Check Patient Motion and Positioning

Review whether the patient moved during acquisition and whether positioning was stable.

Check:

- Head or body support.
- Patient comfort.
- Immobilization accessories.
- Table position.
- Whether motion occurred between PET and CT portions of the examination.

**Expected outcome:** Positioning and motion-related causes are either identified or reasonably excluded.

If motion explains the artifact and equipment performance is normal, troubleshooting can stop after documentation.

### 4. Inspect External Accessories and Objects in the Scan Field

Look for external objects that may affect images, including:

- Positioning aids.
- Cables.
- Monitoring equipment.
- Jewelry or clothing components.
- Blankets containing unexpected material.
- Patient-support accessories.
- Objects accidentally left on the table.

**Expected outcome:** No unnecessary external object is affecting the imaging field.

If removing an external object eliminates the artifact during approved verification, troubleshooting is complete.

### 5. Verify Table and Patient Alignment

Check that patient positioning, centering, and accessory placement are appropriate for the intended examination.

Do not change calibration or geometry parameters to compensate for incorrect positioning.

**Expected outcome:** Patient and table positioning are mechanically appropriate and reproducible.

If positioning correction resolves the issue, verify image quality and stop.

### 6. Compare Multiple Studies or Approved Test Images

Determine whether the same artifact appears:

- Across different patients.
- Across different protocols.
- In the same physical image region.
- Only on PET.
- Only on CT.
- Only after fusion or reconstruction.

Use approved non-patient test objects when available.

**Expected outcome:** The artifact is localized to a patient-specific, acquisition-specific, reconstruction-specific, or system-wide pattern.

### 7. Check Environmental and External Conditions

Inspect for recent environmental changes that could affect system performance, such as:

- Room temperature issues.
- Cooling interruptions.
- Nearby construction or service activity.
- Equipment newly positioned near the system.
- Recent facility power events.

Do not assume a detector defect until environmental causes are excluded.

**Expected outcome:** No obvious external environmental change explains the image-quality problem.

### 8. Perform Approved Quality Checks

Run only the normal quality-control or performance checks that Clinical Engineering is authorized and trained to perform using appropriate test equipment.

Do not alter calibration constants simply because an image artifact is present.

**Expected outcome:** Approved quality checks either pass or provide reproducible evidence of a system-level issue.

If QC passes and the artifact is traced to a corrected external cause, verify final image quality and stop.

### 9. Perform Final Image Verification

After correction, obtain an approved test acquisition and verify:

- Artifact is absent.
- Image quality is stable.
- PET and CT image alignment is acceptable for the tested workflow.
- No new image-quality issue appears.
- Required QC passes.

**Expected outcome:** Image quality is restored and stable.

If verification passes, troubleshooting is complete.

### 10. Escalate Persistent Image Artifacts

If artifacts persist after positioning, accessories, motion, environment, and approved QC have been addressed, stop external troubleshooting.

**Expected outcome:** The system is removed from affected clinical use and escalated for qualified service evaluation.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may involve detector performance, calibration, acquisition electronics, geometry, reconstruction software, PET/CT registration, internal synchronization, or other service-level conditions.

The device should be:

- Removed from service when image quality cannot be trusted.
- Labeled **Out of Service** or otherwise restricted according to facility policy.
- Sent for repair or qualified system evaluation.
- Evaluated using appropriate Siemens Healthineers documentation, phantoms, and approved test equipment.
- Calibrated, repaired, or configured only by qualified personnel.

Do not compensate for unexplained artifacts by changing protected calibration values.

Required imaging and quality-control testing must pass before clinical return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Preserve representative artifact images when permitted; the pattern can be valuable to qualified service personnel and may prevent unnecessary repeat patient scans.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Start with positioning, motion, accessories, and environment before assuming detector failure, protect patients from unnecessary repeat imaging, and require objective image-quality verification before return to service.

That is successful troubleshooting.
