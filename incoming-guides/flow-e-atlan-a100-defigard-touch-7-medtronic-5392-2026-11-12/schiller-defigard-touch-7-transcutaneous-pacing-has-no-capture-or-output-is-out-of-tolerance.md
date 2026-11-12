---
schemaVersion: 1
title: "Schiller DEFIGARD Touch 7 Defibrillator - Transcutaneous Pacing Has No Capture or Output Is Out of Tolerance"
issueTitle: "Transcutaneous Pacing Has No Capture or Output Is Out of Tolerance"
description: "Troubleshoots pacing problems involving pad contact, cable recognition, ECG sensing, user settings, patient factors, or pacing-output verification."
assetType: "Defibrillator"
manufacturer: "Schiller"
model: "DEFIGARD Touch 7"
slug: "schiller-defigard-touch-7-transcutaneous-pacing-has-no-capture-or-output-is-out-of-tolerance"
dateAdded: "2026-11-12"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that transcutaneous pacing from the DEFIGARD Touch 7 did not appear to produce capture."
  cause: "Clinical Engineering verified normal pacing output on an approved analyzer and found that the equipment fault could not be reproduced with known-good therapy accessories."
  resolution: "Completed pacing and ECG functional verification, documented normal device output, and returned the unit to service after successful testing."
helpfulDetails:
  - "Whether pacing mode was entered."
  - "Therapy accessory recognition."
  - "ECG quality."
  - "Pacing mode used."
  - "Rate and output settings observed."
  - "Known-good cable or pad result."
  - "Analyzer measurements."
  - "Whether the complaint was reproduced."
  - "Final device status."
---

## What This Guide Helps With

Troubleshoots pacing problems involving pad contact, cable recognition, ECG sensing, user settings, patient factors, or pacing-output verification.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Pacing Capability

If transcutaneous pacing is clinically required and the DEFIGARD Touch 7 is not producing effective therapy, immediately provide another verified pacing-capable device or alternate treatment as directed by the clinical team.

Do not troubleshoot uncertain pacing output while the patient depends on the unit.

**Expected outcome:** Required pacing support continues using reliable equipment.

### 2. Distinguish No Capture From No Pacing Output

Clinical noncapture does not automatically indicate equipment failure.

Determine whether the device:

- Does not enter pacing mode.
- Does not recognize therapy pads.
- Shows pacing markers but no clinical capture.
- Produces no apparent pacing output.
- Fails output verification on test equipment.

**Expected outcome:** The symptom is separated into a device-output problem, accessory problem, or patient-capture concern.

### 3. Inspect Therapy Pads and Placement

For a patient-related report, clinical staff should verify pad condition and placement according to their approved clinical procedure.

For bench troubleshooting, inspect pads, adapters, and therapy cables for damage and secure connection.

**Expected outcome:** Approved therapy accessories are correctly connected and recognized.

### 4. Substitute Known-Good Therapy Accessories

Use approved known-good pads and therapy cables for bench evaluation.

**Expected outcome:** The device recognizes the replacement accessory and pacing behavior becomes stable if the original accessory was defective.

### 5. Verify ECG Signal Quality

Demand pacing depends on reliable ECG sensing.

Check for:

- Lead-off conditions.
- Excessive ECG artifact.
- Poor electrode contact.
- Unstable heart-rate detection.

Use an approved simulator during bench testing.

**Expected outcome:** The device receives a stable ECG signal suitable for pacing evaluation.

### 6. Verify User-Accessible Pacing Controls

Confirm that the appropriate pacing mode, rate, and output controls respond normally during an approved bench test.

Do not use service-level calibration adjustments unless authorized.

**Expected outcome:** Pacing controls respond predictably and the device generates pacing indications as expected.

### 7. Verify Output With an Approved Analyzer

Connect the defibrillator to an approved defibrillator/pacer analyzer using the manufacturer-appropriate test setup.

Measure pacing output according to approved manufacturer and facility procedures.

**Expected outcome:** Pacing output meets the applicable specified requirement. If output passes, the device fault is not reproduced and troubleshooting can stop after documenting the result.

### 8. Verify Demand/Fixed Pacing Behavior as Applicable

Using a simulator and analyzer, verify the pacing mode involved in the original complaint and any additional pacing functions required by the return-to-service procedure.

**Expected outcome:** Pacing output and sensing behavior are reliable and repeatable.

## If the Problem Persists

Known-good therapy accessories, ECG sensing, normal controls, and analyzer testing have been completed. If pacing output remains absent, erratic, or outside the applicable manufacturer specification, an internal therapy-control or output fault may exist.

The device should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate manufacturer documentation and approved defibrillator/pacer test equipment.
- Repaired or calibrated only by qualified personnel.

Do not adjust internal pacing circuitry without authorized procedures. Complete required pacing, defibrillation, monitoring, alarm, and electrical-safety testing before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Clinical noncapture can occur even when pacing output is normal, so separate patient response from device output using approved test equipment.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Separate patient capture from electrical pacing output before diagnosing a device failure. Verify the complete therapy and ECG sensing paths with approved analyzers, and remove the defibrillator from service whenever pacing output cannot be confirmed.

That is successful troubleshooting.
