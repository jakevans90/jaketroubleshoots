---
schemaVersion: 1
title: "Fujifilm Sonosite Sonosite LX Ultrasound System - Measurement Package, Annotation, or Calculation Will Not Save"
issueTitle: "Measurement Package, Annotation, or Calculation Will Not Save"
description: "Troubleshoots measurements, annotations, or calculations that disappear or cannot save because of workflow, exam state, storage, configuration, or software issues."
assetType: "Ultrasound System"
manufacturer: "Fujifilm Sonosite"
model: "Sonosite LX"
slug: "fujifilm-sonosite-sonosite-lx-measurement-package-annotation-or-calculation-will-not-save"
dateAdded: "2026-11-24"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that measurements entered on the Sonosite LX disappeared after leaving the image."
  cause: "Clinical Engineering reproduced the issue and found that the examination was being performed under an incorrect measurement package for the intended workflow."
  resolution: "The correct exam package was selected and measurement entry, saving, and subsequent review were successfully verified."
helpfulDetails:
  - "Function affected"
  - "Exam type selected"
  - "When entered information disappears"
  - "Whether images save normally"
  - "Measurement package used"
  - "Storage messages"
  - "Restart results"
  - "Test-study results"
  - "Persistence after reopening"
  - "Final system status"
---

## What This Guide Helps With

Troubleshoots measurements, annotations, or calculations that disappear or cannot save because of workflow, exam state, storage, configuration, or software issues.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Documentation
If measurements or calculations cannot be reliably retained, clinicians should document required clinical information through an approved alternate method until the system is verified.

Expected outcome: Required patient information is not lost because of troubleshooting.

### 2. Confirm the Exact Failure
Determine whether the problem affects measurements, annotations, calculations, or all saved exam information. Establish whether data disappears immediately, after changing images, or after closing the study.

Expected outcome: The failure is reproducible and tied to a specific workflow point.

### 3. Verify the Correct Patient/Exam Context
Confirm that an appropriate exam is active and the user is working within the intended patient or test study.

Expected outcome: Data is being entered within a valid active examination.

### 4. Check Basic Image Saving
Acquire an appropriate test image and verify whether the image itself can be stored.

Expected outcome: Basic storage works normally, or the problem is identified as a broader storage issue.

### 5. Verify the Measurement or Calculation Workflow
Repeat the operation using the normal clinical sequence and confirm all required selections or completion actions are performed before leaving the screen.

Expected outcome: The result is accepted and retained when the normal workflow is completed.

### 6. Check the Selected Exam Package
Confirm that the appropriate exam type, measurement package, or calculation set is selected through normal user-accessible controls.

Expected outcome: Required measurement and calculation functions correspond to the intended examination.

### 7. Review Storage Availability
Using normal system menus, verify that storage is available and not reporting an error. Do not delete clinical studies without authorization.

Expected outcome: Adequate accessible storage is available for the test workflow.

### 8. Perform a Controlled Restart
With no active patient examination dependent on the system, shut down and restart normally, then repeat the test using a nonclinical or authorized test study.

Expected outcome: Measurements, annotations, and calculations save normally after restart.

### 9. Perform Final Workflow Verification
Create a representative test measurement or annotation, save the image/study as appropriate, reopen or review it, and confirm the information remains present.

Expected outcome: Required data persists through the completed workflow. Troubleshooting can stop.

## If the Problem Persists

Exam context, workflow, package selection, storage availability, and temporary software state have been checked. Remaining causes may involve application software, database integrity, storage, user configuration, software options, or another service-level condition.

If clinically required data cannot be reliably retained, remove the system from that workflow and label it **Out of Service** when appropriate. Send it for qualified evaluation using Fujifilm Sonosite documentation and approved service methods. Do not perform unauthorized database repair or software modification.

After corrective action, verify the complete measurement/save/review workflow before return to service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never assume an on-screen measurement has been retained; verify persistence before the examination is closed when documentation is clinically required.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Saving problems require verification of the entire workflow, not just the button pressed. Confirm exam context, storage, and persistence before assuming software failure, and escalate when clinical documentation cannot be trusted.

That is successful troubleshooting.
