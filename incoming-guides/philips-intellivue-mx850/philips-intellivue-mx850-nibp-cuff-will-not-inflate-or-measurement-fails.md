---
schemaVersion: 1
title: "Philips IntelliVue MX850 Patient Monitor - NIBP Cuff Will Not Inflate or Measurement Fails"
issueTitle: "NIBP Cuff Will Not Inflate or Measurement Fails"
description: "Troubleshoots failed NIBP measurements caused by cuff selection, hose leaks, loose connections, patient movement, positioning, external obstruction, or measurement-system faults."
assetType: "Patient Monitor"
manufacturer: "Philips"
model: "IntelliVue MX850"
slug: "philips-intellivue-mx850-nibp-cuff-will-not-inflate-or-measurement-fails"
dateAdded: "2026-08-14"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported the Philips IntelliVue MX850 NIBP cuff would inflate but repeatedly failed to complete a measurement."
  cause: "Clinical Engineering found a leaking NIBP hose connection that prevented the system from maintaining pressure."
  resolution: "Clinical Engineering replaced the approved NIBP hose and verified successful measurements and proper inflation and deflation using approved test equipment."
helpfulDetails:
  - "Exact failure behavior"
  - "Exact displayed message"
  - "Cuff size and condition"
  - "Hose and connector condition"
  - "Whether inflation occurred"
  - "Known-good cuff results"
  - "Known-good hose results"
  - "Patient movement or positioning concerns"
  - "Analyzer or simulator results"
  - "Final functional status"
---

## What This Guide Helps With

Troubleshoots failed NIBP measurements caused by cuff selection, hose leaks, loose connections, patient movement, positioning, external obstruction, or measurement-system faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Blood Pressure Assessment

If blood pressure information is clinically required and the MX850 cannot obtain a reliable NIBP measurement, use another verified blood pressure method before troubleshooting.

**Expected outcome:** Clinically required blood pressure assessment continues.

### 2. Confirm the Exact NIBP Failure

Determine whether the cuff:

- Does not inflate
- Inflates but immediately deflates
- Repeatedly retries
- Inflates but produces no result
- Produces intermittent failures
- Works on some patients but not others

Record any displayed message exactly.

**Expected outcome:** The failure is characterized before parts are changed.

### 3. Inspect Cuff Size and Application

Verify the cuff is appropriate for the patient and is:

- Positioned correctly
- Wrapped securely
- Not twisted
- Not excessively loose
- Not placed over thick clothing
- Not obstructed by bedding or other equipment

**Expected outcome:** The cuff is correctly applied. If a measurement succeeds consistently after correction, proceed to verification.

### 4. Inspect the Cuff

Inspect the cuff and bladder for:

- Tears
- Loose tubing
- Damaged fittings
- Obvious air leakage
- Contamination
- Deformation

**Expected outcome:** The cuff retains inflation normally and has no obvious external leak.

### 5. Inspect the NIBP Hose

Check the entire external hose for:

- Kinks
- Compression under equipment
- Cracks
- Loose fittings
- Damaged connectors
- Leakage
- Obstruction

Ensure each connection is fully seated.

**Expected outcome:** The hose provides an unobstructed, sealed air path.

### 6. Substitute Known-Good External Components

Use a compatible known-good cuff and hose.

Change one component at a time when practical.

**Expected outcome:** If NIBP operates normally with a known-good cuff or hose, remove the failed accessory from service and proceed to verification.

### 7. Check Patient and Environmental Conditions

Measurement can fail because of:

- Patient movement
- Tremor
- Improper limb positioning
- Cuff movement
- External compression of the cuff or hose

Repeat the measurement only when clinically appropriate and the patient is suitably positioned.

**Expected outcome:** A reliable measurement is obtained under stable conditions.

### 8. Test with Approved NIBP Test Equipment

When the problem persists away from patient use, connect appropriate approved NIBP simulation or analyzer equipment using the correct setup.

Do not attempt internal pneumatic adjustments.

**Expected outcome:** The monitor initiates, inflates, measures, and deflates appropriately. If it passes testing, the original issue was likely external or application-related.

### 9. Perform Final Functional Verification

Verify:

- Successful inflation and deflation
- Stable pressure measurement with approved test equipment
- No obvious external leakage
- Correct display of the completed measurement
- Relevant alarm or status indication where applicable

**Expected outcome:** NIBP operation is reliable. Troubleshooting can stop.

### 10. Escalate Persistent Pneumatic or Measurement Failure

If the MX850 still cannot complete NIBP measurements with known-good cuff, hose, and approved test equipment, stop troubleshooting.

**Expected outcome:** The affected NIBP system is removed from clinical use and referred for service evaluation.

## If the Problem Persists

Common external causes have been ruled out. The remaining issue may involve internal pneumatic components, the pressure measurement system, valves, pump operation, module electronics, or another service-level problem.

The affected equipment should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate Philips documentation and approved NIBP test equipment
- Repaired or configured only by qualified personnel

Complete appropriate NIBP accuracy, leakage, functional, and alarm verification before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

If repeated NIBP attempts fail, avoid unnecessary repeated cuff cycling on the patient; switch to another verified blood pressure method while troubleshooting.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain blood pressure assessment, inspect cuff application and the entire external pneumatic path first, verify performance with approved test equipment, and escalate rather than attempting internal pneumatic repair at the bedside.

That is successful troubleshooting.
