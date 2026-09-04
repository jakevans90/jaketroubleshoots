---
schemaVersion: 1
title: "Smiths Medical Medfusion 3500 Infusion Pump - Syringe Not Recognized or Incorrect Syringe Size Detected"
issueTitle: "Syringe Not Recognized or Incorrect Syringe Size Detected"
description: "Troubleshoots syringe recognition or size-detection problems caused by syringe selection, loading, positioning, compatibility, or external mechanical conditions."
assetType: "Infusion Pump"
manufacturer: "Smiths Medical"
model: "Medfusion 3500"
slug: "smiths-medical-medfusion-3500-syringe-not-recognized-or-incorrect-syringe-size-detected"
dateAdded: "2026-09-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Medfusion 3500 identified the installed syringe as the wrong size and would not proceed normally."
  cause: "Clinical Engineering found that the syringe was not fully seated in the retaining mechanism, preventing consistent syringe detection."
  resolution: "The syringe was reloaded correctly, repeated recognition tests were successful, and pump operation was verified before return to service."
helpfulDetails:
  - "Syringe manufacturer, type, and size"
  - "Exact displayed message"
  - "Whether recognition failed continuously or intermittently"
  - "Condition of syringe flange and barrel"
  - "Syringe position when failure occurred"
  - "Known-good syringe tested"
  - "Other syringe sizes tested"
  - "Condition of external retaining components"
  - "Results before and after correction"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots syringe recognition or size-detection problems caused by syringe selection, loading, positioning, compatibility, or external mechanical conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Therapy
Do not troubleshoot a Medfusion 3500 that is delivering critical therapy while the patient depends on it. Transfer therapy to another verified pump when interruption could affect patient safety. Remove the affected pump from active clinical use before manipulating the syringe or loading mechanism.

**Expected outcome:** Patient therapy continues safely on appropriate equipment and the reported pump is available for controlled evaluation.

### 2. Confirm the Exact Recognition Problem
Determine whether the pump fails to recognize the syringe entirely, identifies the wrong syringe size, intermittently changes the detected size, or prevents programming because the loaded syringe does not match the expected selection. Record any displayed message without assuming its cause.

**Expected outcome:** The exact failure condition is reproduced or clearly documented.

### 3. Inspect the Syringe
Remove the syringe and inspect it for deformation, damaged flanges, unusual dimensions, incorrect assembly, contamination, or other physical conditions that could interfere with proper loading. Verify that the syringe type being evaluated is appropriate for use with the pump according to current approved documentation.

**Expected outcome:** A compatible, undamaged syringe is available for testing.

### 4. Reload the Syringe Correctly
Install the syringe carefully, making sure the barrel, flange, and plunger are seated squarely in the intended external retaining features. Confirm that no tubing, labels, tape, or other material prevents the syringe from seating completely.

**Expected outcome:** The syringe sits securely and the pump consistently detects the expected syringe configuration. If recognition is correct, troubleshooting can stop after functional verification.

### 5. Inspect the Syringe Retaining Components
Examine accessible syringe-retaining and detection areas for debris, dried medication, physical damage, sticking movement, or obstruction. Do not force any component or disassemble the pump.

**Expected outcome:** Accessible mechanisms are clean, unobstructed, and move normally without looseness or binding.

### 6. Test With a Known-Good Syringe
Using an approved known-good syringe of the expected type and size, repeat the loading and recognition test. Compare the response with the originally reported syringe.

**Expected outcome:** The known-good syringe is recognized correctly. If so, the original syringe or loading condition was the likely external cause and troubleshooting can stop after documenting the result.

### 7. Compare Multiple Approved Syringe Sizes if Appropriate
If the reported problem involves incorrect size detection, evaluate more than one compatible syringe size as appropriate to determine whether the error follows one syringe or occurs across multiple syringes.

**Expected outcome:** Each tested syringe is identified consistently. Repeated incorrect identification across known-good syringes indicates the pump requires further service evaluation.

### 8. Verify Programming and Syringe Selection
Confirm that the pump's displayed syringe information and intended programming correspond to the physically installed syringe. Do not override a mismatch or make unauthorized configuration changes simply to permit operation.

**Expected outcome:** Physical syringe installation and displayed pump information agree.

### 9. Perform Final Functional Verification
Using appropriate bench-testing practices, verify reliable syringe recognition through repeated unload-and-reload cycles and confirm that normal programming can proceed without intermittent detection changes.

**Expected outcome:** Syringe recognition remains stable during repeated testing. If stable, the pump may proceed through required return-to-service testing.

### 10. Escalate Persistent Recognition Errors
If known-good compatible syringes are repeatedly not recognized, are incorrectly identified, or recognition changes with minor movement, remove the pump from service for manufacturer-directed evaluation.

**Expected outcome:** An unreliable pump is prevented from returning to clinical use until properly evaluated and verified.

## If the Problem Persists

Common external causes such as syringe condition, compatibility, loading, positioning, and obstruction have been ruled out. The remaining cause may involve the syringe detection mechanism, mechanical alignment, configuration, or another service-level condition.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

After corrective action, complete all applicable functional, safety, and performance verification before returning the pump to clinical use. Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Never bypass or ignore a syringe identification mismatch to begin patient therapy; move the therapy to a verified pump if recognition cannot be confirmed.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Syringe manufacturer, type, and size
- Exact displayed message
- Whether recognition failed continuously or intermittently
- Condition of syringe flange and barrel
- Syringe position when failure occurred
- Known-good syringe tested
- Other syringe sizes tested
- Condition of external retaining components
- Results before and after correction
- Final device status

## Final Thought

Protect the patient first, then verify syringe compatibility, physical condition, loading, and detection before assuming an internal failure. Escalate persistent recognition problems and clearly document what was found and verified.

That is successful troubleshooting.
