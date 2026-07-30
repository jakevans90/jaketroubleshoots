---
schemaVersion: 1
title: "Mortara ELI Series Electrocardiograph (EKG) Machine - ECG Interpretation Or Analysis Not Generated"
issueTitle: "ECG Interpretation Or Analysis Not Generated"
description: "Troubleshooting missing automated ECG interpretation caused by signal quality, lead placement, patient data, acquisition mode, configuration, or software availability."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "Mortara"
model: "ELI Series"
slug: "mortara-eli-series-ecg-interpretation-or-analysis-not-generated"
dateAdded: "2026-07-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Mortara ELI Series machine printed ECG tracings without the expected automated interpretation."
  cause: "Clinical Engineering found that the selected department report format excluded interpretation text even though analysis was present in the stored record."
  resolution: "Restored the approved report format, verified interpretation output with a simulator ECG, and returned the unit to service."
helpfulDetails:
  - "Whether measurements were generated."
  - "Acquisition mode selected."
  - "Lead-off or artifact indications."
  - "Patient demographics entered."
  - "Analysis configuration observed."
  - "Report format selected."
  - "Simulator ECG result."
  - "Local versus printed result."
  - "Exported or transmitted result."
  - "Comparison device findings."
  - "Final device status."
---

## What This Guide Helps With

Troubleshooting missing automated ECG interpretation caused by signal quality, lead placement, patient data, acquisition mode, configuration, or software availability.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Clinical Decision-Making

Automated ECG interpretation is an aid and does not replace clinician review.

Do not delay urgent clinical assessment while troubleshooting missing analysis. Ensure the ECG tracing is provided to qualified clinical staff for interpretation.

**Expected outcome:** Clinical decisions do not depend solely on the device-generated analysis.

### 2. Confirm the Exact Reported Condition

Determine whether:

- No interpretation text is generated.

- Measurements appear but interpretation does not.

- Interpretation is generated for some patients but not others.

- Analysis is missing only from printed, exported, or transmitted reports.

- The device displays an analysis-disabled message.

- The tracing is incomplete or marked with lead-off or poor-quality warnings.

**Expected outcome:** The issue is identified as acquisition quality, patient-data, configuration, licensing, output-format, or software behavior.

### 3. Verify a Complete Diagnostic ECG Was Acquired

Confirm that the workflow produced the intended diagnostic resting ECG rather than:

- Rhythm-only recording.

- Preview screen.

- Incomplete acquisition.

- Monitoring display.

- Manual printout.

- A record with missing required leads.

**Expected outcome:** A complete diagnostic acquisition is available for analysis.

### 4. Check Lead Placement and Electrode Contact

Using an ECG simulator or appropriately prepared test setup, verify all required leads are present and stable.

Inspect:

- Electrode expiration and storage condition.

- Skin preparation.

- Lead placement.

- Lead-wire connection.

- Patient cable condition.

- Lead-off indications.

- Excessive motion or muscle artifact.

**Expected outcome:** The acquired ECG contains stable, complete signals suitable for analysis. If analysis appears after correcting signal quality, troubleshooting can stop.

### 5. Review Signal Quality

Examine the tracing for:

- Flat or missing leads.

- Excessive baseline wander.

- Tremor artifact.

- Electrical interference.

- Clipped or saturated signals.

- Reversed or misplaced leads.

- Continuous lead-off conditions.

Repeat the acquisition on an ECG simulator to separate patient-related signal quality from device behavior.

**Expected outcome:** A clean simulator ECG produces expected measurements and analysis when the feature is available.

### 6. Verify Required Patient Demographics

Check whether the analysis workflow requires patient information such as age, sex, or other demographics.

Enter approved test demographics and repeat the simulator acquisition. Do not fabricate demographics for an actual patient.

**Expected outcome:** Required patient fields are completed and the device can apply the intended analysis workflow.

### 7. Verify Analysis Is Enabled

Review only normal authorized settings to confirm that automated measurements or interpretation have not been disabled for:

- The current user.

- The department profile.

- The selected report type.

- The acquisition mode.

- The device configuration.

Compare with a working ELI Series device in the same department.

**Expected outcome:** Analysis is enabled under the approved configuration.

### 8. Check Report and Display Selection

Confirm that interpretation text is configured to appear on the selected output.

The analysis may exist in the stored record but be excluded from a particular print format, PDF template, or transmitted report.

**Expected outcome:** The selected report format includes the required measurements or interpretation.

### 9. Restart the Device

Confirm all patient records are saved.

Perform a normal shutdown and restart, then acquire a new simulator ECG using approved test data.

**Expected outcome:** The analysis function initializes and generates the expected output.

### 10. Compare Local, Printed, and Transmitted Results

Review the same test ECG:

- On the device.

- In the stored record.

- On the printed report.

- In the exported file.

- At the receiving ECG management system.

**Expected outcome:** The interpretation is present consistently, or the problem is isolated to a specific output path.

### 11. Perform Final Functional Verification

Using an ECG simulator:

Confirm all required leads.

Acquire a clean diagnostic ECG.

Verify measurements.

Verify interpretation text when configured and licensed.

Print or transmit the report.

Confirm the expected content is present.

**Expected outcome:** The device generates and outputs the expected analysis. Troubleshooting can stop.

### 12. Escalate Unresolved Analysis Failure

Remove the device from service or clearly restrict its use if the configured clinical workflow requires automated analysis and the function remains unavailable or inconsistent.

Do not claim the device is clinically accurate based solely on the presence of interpretation text.

**Expected outcome:** A device with an unresolved analysis function is not returned without appropriate review and authorization.

## If the Problem Persists

Common causes involving acquisition mode, incomplete leads, artifact, patient demographics, analysis enablement, and report selection have been ruled out. The remaining issue may involve software licensing, configuration corruption, analysis software, report-template configuration, or a system integration problem.

The device should be:

- Removed from service when automated analysis is required by the approved workflow.

- Labeled Out of Service or restricted according to facility policy.

- Sent for repair or bench evaluation.

- Evaluated using appropriate Mortara documentation and approved ECG simulation equipment.

- Repaired or configured only by qualified personnel.

After correction, verify clean simulated ECG acquisition, measurements, interpretation generation, and output on all required report pathways.

Knowing when to stop prevents Clinical Engineering from substituting technical troubleshooting for clinical interpretation.

## Clinical Use Tip

Automated interpretation must always be reviewed by qualified clinical personnel, even when the EKG machine is functioning normally.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Keep clinical interpretation with qualified caregivers while checking acquisition quality, complete leads, patient data, configuration, and report selection before assuming software failure. Verify the full output pathway and document the exact cause and test result.

That is successful troubleshooting.
