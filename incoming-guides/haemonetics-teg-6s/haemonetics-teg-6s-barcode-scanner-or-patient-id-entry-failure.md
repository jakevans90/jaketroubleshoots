---
schemaVersion: 1
title: "Haemonetics TEG 6s Viscoelastic Hemostasis Analyzer - Barcode Scanner or Patient ID Entry Failure"
issueTitle: "Barcode Scanner or Patient ID Entry Failure"
description: "Addresses barcode reading, patient identification entry, label quality, scanner obstruction, touchscreen input, and workflow configuration problems."
assetType: "Viscoelastic Hemostasis Analyzer"
manufacturer: "Haemonetics"
model: "TEG 6s"
slug: "haemonetics-teg-6s-barcode-scanner-or-patient-id-entry-failure"
dateAdded: "2026-09-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that the TEG 6s barcode scanner would not read patient specimen labels."
  cause: "Clinical Engineering found dried residue on the scanner window, while manual patient ID entry remained functional."
  resolution: "Cleaned the scanner window using an approved method, verified repeated successful scans with known-good labels, and returned the analyzer to service."
helpfulDetails:
  - "Scanner response."
  - "Label condition."
  - "Barcode types affected."
  - "Known-good barcode result."
  - "Scanner window condition."
  - "Manual ID entry result."
  - "Touchscreen behavior."
  - "Recent configuration changes."
  - "Restart result."
  - "Final identification verification."
---
## What This Guide Helps With

Addresses barcode reading, patient identification entry, label quality, scanner obstruction, touchscreen input, and workflow configuration problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification Integrity

Do not proceed with patient testing if the analyzer cannot reliably associate results with the correct patient or specimen.

Use an approved alternate identification workflow or another verified analyzer as directed by laboratory policy.

**Expected outcome:** No result is generated under an uncertain or incorrect patient identity.

### 2. Confirm Whether Scanning or Manual Entry Is Affected

Determine whether:
- Barcode scanning fails.
- Manual patient ID entry fails.
- Both methods fail.
- Only certain barcode labels fail.
- The scanner activates but does not decode.
- The scanner does not respond at all.

**Expected outcome:** The problem is isolated to the scanner, label, user-entry interface, or broader software workflow.

### 3. Inspect the Barcode Label

Check the label for:
- Wrinkles.
- Smearing.
- Poor print quality.
- Damage.
- Curvature.
- Contamination.
- Incomplete barcode printing.

Use a known-good barcode for comparison.

**Expected outcome:** A known-good barcode reads normally. If so, the original label was the likely cause.

### 4. Clean and Inspect the Scanner Window

Inspect the accessible scanner surface for:
- Dust.
- Smudges.
- Dried material.
- Scratches.
- Obstruction.

Clean only with an approved method.

**Expected outcome:** The scanner window is clean and unobstructed. If scanning is restored, troubleshooting can stop after repeated verification.

### 5. Verify Scanning Position and Distance

Test the scanner using a known-good label at a normal orientation and practical working distance.

Avoid assuming a scanner failure based on one difficult label position.

**Expected outcome:** The scanner consistently reads a known-good barcode. If so, the device is functioning normally.

### 6. Test Manual Patient ID Entry

Use the normal data-entry screen to verify that characters can be entered, corrected, and accepted.

Do not create or save false patient records during troubleshooting.

**Expected outcome:** Manual data entry functions normally. If manual entry works but scanning does not, focus on the barcode path.

### 7. Verify Touchscreen Responsiveness

Check whether the touchscreen responds accurately across the areas needed for patient identification.

**Expected outcome:** Touchscreen inputs register normally without missed or unintended selections.

### 8. Verify Workflow and Configuration

Confirm that the analyzer is in the expected patient identification workflow and that no recent authorized configuration change has altered barcode or ID behavior.

Do not modify protected settings without authorization.

**Expected outcome:** Workflow configuration matches the facility's intended setup.

### 9. Restart and Reverify

If the scanner or entry interface appears frozen, perform a normal controlled restart when the analyzer is not in active testing.

Test:
- Known-good barcode.
- Manual ID entry.
- Navigation through the identification screen.

**Expected outcome:** Identification functions return to normal and remain stable.

### 10. Escalate Persistent Identification Failure

If scanning and/or manual entry remains unreliable, remove the analyzer from patient testing where positive identification is required.

**Expected outcome:** The device is routed for evaluation before an identification error can affect patient results.

## If the Problem Persists

External causes such as label quality, scanner contamination, scanning technique, touchscreen responsiveness, and basic workflow configuration have been ruled out. Remaining causes may involve the scanner hardware, touchscreen interface, software, configuration database, or another service-level function.

The device should be:
- Removed from service when reliable patient identification cannot be maintained.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Verify patient identification functionality before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never bypass positive patient identification merely to keep testing moving; a technically valid result assigned to the wrong patient is unsafe.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Scanner response.
- Label condition.
- Barcode types affected.
- Known-good barcode result.
- Scanner window condition.
- Manual ID entry result.
- Touchscreen behavior.
- Recent configuration changes.
- Restart result.
- Final identification verification.

## Final Thought

Patient identification is part of the measurement system. Verify labels and scanner conditions first, preserve identification integrity throughout troubleshooting, and escalate any unreliable input function before clinical use resumes.

That is successful troubleshooting.
