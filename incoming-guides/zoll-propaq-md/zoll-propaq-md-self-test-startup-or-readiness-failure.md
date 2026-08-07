---
schemaVersion: 1
title: "ZOLL Propaq MD Defibrillator - Self-Test, Startup, or Readiness Failure"
issueTitle: "Self-Test, Startup, or Readiness Failure"
description: "Device fails startup, self-test, or readiness checks because of power, battery, accessories, configuration, environmental conditions, or an internal service-level problem."
assetType: "Defibrillator"
manufacturer: "ZOLL"
model: "Propaq MD"
slug: "zoll-propaq-md-self-test-startup-or-readiness-failure"
dateAdded: "2026-08-07"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Propaq MD intermittently failed to complete startup and did not consistently indicate ready status."
  cause: "Clinical Engineering found that the installed battery intermittently lost connection and confirmed normal startup with a known-good compatible battery."
  resolution: "The suspect battery was removed from service and replaced, and repeated startup, readiness, monitoring, pacing, and defibrillator functional tests passed."
helpfulDetails:
  - "Exact startup or readiness message"
  - "Point in startup where failure occurred"
  - "Battery condition"
  - "Known-good battery result"
  - "AC versus battery behavior"
  - "Outlet tested"
  - "Power cord condition"
  - "Accessories connected during failure"
  - "Physical damage or contamination"
  - "Number of successful repeated startups"
  - "Final functional test results"
  - "Final device status"
---

## What This Guide Helps With

Device fails startup, self-test, or readiness checks because of power, battery, accessories, configuration, environmental conditions, or an internal service-level problem.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Replace the Defibrillator
A Propaq MD that does not complete startup or indicates it is not ready should not be relied upon for emergency use.

Replace it immediately with another verified defibrillator before technical troubleshooting.

**Expected outcome:** Emergency monitoring, pacing, and defibrillation capability remain available.

### 2. Document the Exact Failure
Record exactly what occurs during startup or readiness checking, including:

- Blank display
- Startup stops before completion
- Unexpected restart
- Self-test failure indication
- Readiness indicator abnormal
- Audible or visual warning
- Failure only on battery or only on external power

Do not invent or paraphrase displayed error information when documenting the work order.

**Expected outcome:** The exact failure state is captured for reproducible troubleshooting and escalation.

### 3. Inspect the Unit Externally
Check for:

- Impact damage
- Cracked housing
- Liquid contamination
- Damaged connectors
- Loose battery
- Damaged power connection
- Excessive heat
- Unusual odor
- Evidence of fluid ingress

Do not power a unit with evidence of significant liquid intrusion, burning, or severe physical damage.

**Expected outcome:** The device has no obvious external condition requiring immediate removal from service without further testing.

### 4. Verify Battery Condition and Seating
Remove and reinstall the battery correctly.

Inspect for physical damage, contamination, or abnormal heat.

If available, test with a known-good compatible battery.

**Expected outcome:** The device has a verified, properly seated battery. If startup succeeds consistently with a known-good battery, replace the defective battery and complete full functional verification.

### 5. Verify External Power
Connect a known-good approved external power source to a verified outlet.

Inspect accessible power cords and connectors.

Observe whether startup behavior differs between external power and battery operation.

**Expected outcome:** Basic power availability is ruled in or out as the cause.

### 6. Disconnect Nonessential External Accessories
With the device removed from clinical use, disconnect nonessential external patient accessories and communication cables before repeating startup.

Do not disconnect components required by the manufacturer's normal startup procedure.

**Expected outcome:** A damaged external accessory or connection no longer interferes with startup. If the unit starts normally, reconnect accessories individually to identify the external cause.

### 7. Repeat Startup Under Controlled Conditions
Perform a normal power cycle using standard controls.

Observe the sequence without repeatedly cycling the unit excessively.

Record any displayed message or point at which startup stops.

**Expected outcome:** The device completes normal startup and reaches a ready state. If it does so repeatedly after correcting an external cause, proceed to comprehensive functional verification.

### 8. Evaluate Readiness With Known-Good Accessories
Reconnect verified compatible monitoring and therapy accessories required for intended service.

Check whether the readiness condition changes with a specific cable or accessory attached.

**Expected outcome:** External accessories do not create a readiness failure.

### 9. Check Environmental and Basic Configuration Factors
Confirm the device is being tested in a suitable environment and that no obvious user-accessible setting or incomplete workflow is being mistaken for a readiness failure.

Do not reset the device, erase configuration, install software, or alter protected service settings without manufacturer-approved procedures and authorization.

**Expected outcome:** Environmental and normal operational factors are ruled out.

### 10. Perform Complete Functional Verification
If startup and readiness return to normal, verify the functions appropriate to the Propaq MD's intended use, including as applicable:

- Battery and external power operation
- ECG monitoring
- NIBP
- SpO2
- EtCO2
- Alarm operation
- External pacing
- Defibrillator charging and discharge with an analyzer
- Communication functions
- Readiness indication

**Expected outcome:** The unit completes startup consistently and all required clinical functions pass testing. Troubleshooting can stop.

### 11. Escalate Any Persistent Startup or Readiness Failure
If the Propaq MD repeatedly fails startup, self-test, or readiness checks after power, battery, accessories, and external conditions are ruled out, stop troubleshooting.

**Expected outcome:** The device remains out of service for qualified diagnostic evaluation.

## If the Problem Persists

Once battery condition, external power, accessories, connectors, environmental conditions, and normal operational factors have been ruled out, the remaining cause may involve internal power management, system software, stored configuration, self-test circuitry, monitoring or therapy subsystems, or another service-level condition.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not bypass readiness checks or return the device to service simply because it appears to operate after an intermittent failure.

Following repair, perform complete manufacturer-appropriate return-to-service testing of all applicable monitoring, therapy, alarm, battery, and electrical safety functions.

Knowing when to stop after a failed readiness check is proper troubleshooting.

## Clinical Use Tip

A defibrillator with an unresolved startup, self-test, or readiness failure should be replaced immediately rather than kept available as a backup.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Treat a readiness failure as a safety issue, establish alternate defibrillation capability first, verify power, battery, accessories, and external conditions before assuming internal failure, escalate recurring self-test problems, and document complete return-to-service verification.

That is successful troubleshooting.
