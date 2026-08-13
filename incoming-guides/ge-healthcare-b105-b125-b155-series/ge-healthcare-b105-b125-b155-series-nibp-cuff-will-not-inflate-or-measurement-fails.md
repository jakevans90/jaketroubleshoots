---
schemaVersion: 1
title: "GE Healthcare B105 / B125 / B155 Series Patient Monitor - NIBP Cuff Will Not Inflate or Measurement Fails"
issueTitle: "NIBP Cuff Will Not Inflate or Measurement Fails"
description: "Troubleshoots failed NIBP cycles, no cuff inflation, leaks, damaged hoses, cuff problems, connection issues, and externally verifiable measurement failures."
assetType: "Patient Monitor"
manufacturer: "GE Healthcare"
model: "B105 / B125 / B155 Series"
slug: "ge-healthcare-b105-b125-b155-series-nibp-cuff-will-not-inflate-or-measurement-fails"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that the B155 monitor began inflating the NIBP cuff but repeatedly failed to complete measurements."
  cause: "Clinical Engineering found a leak in the external NIBP hose and confirmed normal operation with a known-good hose."
  resolution: "Replaced the damaged hose, verified repeated successful NIBP cycles with approved test equipment, checked deflation and alarms, and returned the monitor to service."
helpfulDetails:
  - "Exact NIBP message"
  - "Whether inflation started"
  - "Cuff condition"
  - "Hose condition"
  - "Kinks or loose fittings"
  - "Cuff application"
  - "Known-good cuff result"
  - "Known-good hose result"
  - "Leak-test result"
  - "Controlled NIBP test result"
  - "Results before and after correction"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots failed NIBP cycles, no cuff inflation, leaks, damaged hoses, cuff problems, connection issues, and externally verifiable measurement failures.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Provide an Alternate Blood Pressure Method
If blood pressure measurement is clinically required and NIBP is unavailable or unreliable, ensure an alternate verified blood pressure method is available before troubleshooting.

Do not repeatedly cycle a malfunctioning cuff on a patient while diagnosing equipment.

**Expected outcome:** Clinical care continues without dependence on the affected NIBP function.

### 2. Confirm the Exact NIBP Complaint
Determine whether:
- The cuff does not inflate
- Inflation begins but stops
- The cuff inflates and measurement fails
- Measurements are intermittent
- Pressure does not release normally
- The problem occurs with one cuff or hose only
- The monitor displays a specific message

**Expected outcome:** The NIBP failure is clearly characterized.

### 3. Inspect the Cuff and Hose
Inspect the NIBP cuff, tubing, connectors, and hose for:
- Tears
- Cracks
- Loose fittings
- Pinched tubing
- Kinks
- Damaged connectors
- Separation at hose fittings
- Contamination or obstruction

**Expected outcome:** The external pneumatic path is unobstructed, intact, and securely connected.

If correcting a kink or loose fitting restores normal measurements, proceed to final verification.

### 4. Verify Cuff Selection and Application
Coordinate with clinical staff to confirm the cuff is appropriate for the intended patient and is applied correctly.

A poorly positioned or inappropriate cuff can contribute to failed or unreliable measurements even when the monitor functions normally.

**Expected outcome:** A suitable cuff is correctly applied without obstruction of the tubing.

If proper cuff application corrects the issue, verify repeated successful measurements and troubleshooting can stop.

### 5. Reseat the NIBP Hose Connection
Disconnect and reconnect the external NIBP hose at accessible connection points.

Inspect the monitor-side connector for obvious physical damage or looseness.

Do not force incompatible fittings.

**Expected outcome:** The hose is fully seated and forms a secure pneumatic connection.

If reseating restores consistent inflation and measurement, proceed to final verification.

### 6. Substitute Known-Good NIBP Accessories
Use a compatible known-good cuff and hose.

Substitute one component at a time when practical to determine whether the failure follows the cuff or tubing.

**Expected outcome:** The known-good cuff and hose inflate and complete measurements normally.

If the original cuff or hose causes the failure, replace the defective accessory.

### 7. Perform an Off-Patient NIBP Test
Use approved NIBP test equipment or a suitable simulator according to facility procedures.

Observe whether:
- Inflation starts
- Pressure is maintained appropriately during the test
- The measurement cycle completes
- Deflation occurs normally
- Repeated cycles behave consistently

Do not infer calibration accuracy from a simple inflation test.

**Expected outcome:** The monitor completes a controlled NIBP test consistently.

### 8. Check for an External Leak
Using approved test methods, determine whether an externally connected hose or cuff assembly leaks.

Do not disassemble the monitor's internal pneumatic system as part of routine external troubleshooting.

**Expected outcome:** The external pneumatic circuit maintains pressure as expected for the approved test.

If an external leak is identified, replace the affected accessory and retest.

### 9. Perform Final Functional Verification
After correction, verify:
- Consistent cuff inflation
- Successful measurement completion
- Normal deflation
- No obvious pneumatic leakage
- Stable connector engagement
- Appropriate NIBP alarm behavior where applicable

Perform any required performance verification with approved NIBP test equipment.

**Expected outcome:** NIBP operation is repeatable and appropriate for clinical use.

If all checks pass, document and return the monitor to service.

### 10. Escalate Persistent NIBP Failure
If the monitor cannot inflate or complete measurements using known-good accessories and approved test equipment, stop external troubleshooting.

Do not proceed into internal pump, valve, transducer, pneumatic assembly, or board-level repair unless specifically authorized and trained.

**Expected outcome:** The monitor is removed from service and routed for qualified repair.

## If the Problem Persists

External cuff, hose, fittings, application, and controlled test conditions have been ruled out. Remaining causes may involve internal pneumatic components, pressure measurement circuitry, calibration, configuration, or another service-level fault.

The monitor should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved NIBP test equipment
- Repaired, calibrated, or configured only by qualified personnel

After repair, complete the required NIBP performance verification and confirm overall monitor and alarm operation before return to clinical use.

Knowing when a pneumatic failure requires service-level evaluation is proper troubleshooting.

## Clinical Use Tip

Avoid repeated unsuccessful cuff cycles on a patient; move to an alternate verified blood pressure method while Clinical Engineering evaluates the monitor.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**




## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain an alternate blood pressure method, inspect the complete external pneumatic path before assuming an internal failure, and distinguish simple inflation from verified NIBP performance. Escalate unresolved pneumatic problems and document the confirmed cause and testing.

That is successful troubleshooting.
