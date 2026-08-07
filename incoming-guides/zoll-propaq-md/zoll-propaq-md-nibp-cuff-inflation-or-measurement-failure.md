---
schemaVersion: 1
title: "ZOLL Propaq MD Defibrillator - NIBP Cuff Inflation or Measurement Failure"
issueTitle: "NIBP Cuff Inflation or Measurement Failure"
description: "NIBP measurement will not start, cuff will not inflate correctly, or readings fail because of cuff, tubing, connections, positioning, or pneumatic problems."
assetType: "Defibrillator"
manufacturer: "ZOLL"
model: "Propaq MD"
slug: "zoll-propaq-md-nibp-cuff-inflation-or-measurement-failure"
dateAdded: "2026-08-07"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Propaq MD cuff inflated but repeatedly failed to complete an NIBP measurement."
  cause: "Clinical Engineering found a leaking NIBP hose that prevented the pneumatic system from maintaining pressure."
  resolution: "The damaged hose was replaced and repeated NIBP simulator measurements completed normally during final verification."
helpfulDetails:
  - "Inflation behavior"
  - "Whether measurement started or aborted"
  - "Cuff size and condition"
  - "Hose condition"
  - "Connector condition"
  - "Known-good cuff or hose substitution"
  - "Patient versus simulator result"
  - "Leak observed"
  - "Deflation behavior"
  - "Repeated test results"
  - "Final device status"
---

## What This Guide Helps With

NIBP measurement will not start, cuff will not inflate correctly, or readings fail because of cuff, tubing, connections, positioning, or pneumatic problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Provide Alternate Blood Pressure Monitoring
If blood pressure measurement is clinically necessary, use another verified method or monitor while the Propaq MD NIBP function is evaluated.

Do not repeatedly cycle an unreliable cuff on a patient solely for troubleshooting.

**Expected outcome:** Clinically necessary blood pressure monitoring continues independently of the affected NIBP system.

### 2. Confirm the Reported NIBP Condition
Determine whether the problem is:

- Cuff does not inflate
- Cuff inflates but measurement aborts
- Cuff remains inflated
- Measurement takes unusually long
- Repeated measurement failure
- Reading appears inconsistent
- Problem occurs with one cuff or all cuffs

Reproduce the condition with an appropriate NIBP simulator when available.

**Expected outcome:** The specific failure mode is confirmed.

### 3. Inspect the Cuff
Check the cuff for:

- Tears
- Worn hook-and-loop material
- Damaged bladder
- Kinked material
- Incorrect size for the intended application
- Loose hose connection
- Contamination affecting the connection

**Expected outcome:** The cuff is physically intact and appropriate for testing. If replacing a damaged cuff restores proper operation, verify measurements and stop troubleshooting.

### 4. Inspect NIBP Tubing
Examine the hose for:

- Kinks
- Cracks
- Pinholes
- Compression damage
- Loose fittings
- Damaged connectors
- Obstructions

Trace the entire external pneumatic path.

**Expected outcome:** The hose is open, intact, and securely connected.

### 5. Reseat the Pneumatic Connections
Disconnect and reconnect the cuff hose at the cuff and device as applicable.

Verify that connectors seat fully and are not partially engaged.

**Expected outcome:** The pneumatic circuit is securely connected. If inflation and measurement return to normal, complete final verification and troubleshooting can stop.

### 6. Verify Cuff Placement and Test Conditions
For clinical complaints, confirm that the cuff was applied correctly and that excessive patient motion, incorrect cuff size, or poor positioning was not contributing to failed measurements.

For bench testing, use a validated NIBP simulator according to departmental procedure.

**Expected outcome:** The test setup eliminates patient-positioning and movement variables.

### 7. Substitute Known-Good Cuff and Hose
Test with a known-good compatible cuff and hose.

Substitute external components before suspecting the device pneumatic system.

**Expected outcome:** If the unit measures normally with known-good accessories, the faulty cuff or hose is identified and can be replaced. Troubleshooting can stop after verification.

### 8. Observe Inflation and Deflation Behavior
During controlled testing, observe whether the device:

- Begins inflation
- Builds pressure smoothly
- Maintains the pneumatic circuit
- Deflates appropriately after measurement
- Completes a measurement without abnormal interruption

Do not open the device or bypass pneumatic safety functions.

**Expected outcome:** Inflation, measurement, and deflation occur consistently without leakage or abnormal behavior.

### 9. Perform Final Functional Verification
Using approved NIBP test equipment:

- Run repeated measurements
- Verify stable inflation and deflation
- Confirm no external leaks
- Confirm displayed results are consistent with the test setup
- Confirm alarms or error indications clear appropriately

**Expected outcome:** NIBP operation is repeatable and reliable. Troubleshooting can stop.

### 10. Escalate Persistent NIBP Failure
If the problem remains with verified tubing, cuff, connections, and NIBP simulator, remove the unit from service.

**Expected outcome:** An unresolved pneumatic, sensing, configuration, or internal NIBP problem is sent for qualified evaluation.

## If the Problem Persists

Once external cuff, hose, connector, placement, movement, and known-good substitution issues have been ruled out, the remaining cause may involve an internal pneumatic assembly, pressure sensing, control circuitry, configuration, or another service-level condition.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Following repair, perform applicable NIBP performance, alarm, monitoring, defibrillator, and electrical safety testing before clinical release.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Use another verified blood pressure method rather than repeatedly cycling a malfunctioning NIBP cuff on a patient.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain alternate blood pressure monitoring, rule out cuffs, hoses, connectors, positioning, and test conditions first, verify performance with appropriate equipment, escalate unresolved pneumatic failures, and clearly document the findings and final test results.

That is successful troubleshooting.
