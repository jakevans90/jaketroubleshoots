---
schemaVersion: 1
title: "ICU Medical Plum Duo Infusion Pump - Battery Will Not Charge or Support the Specified Backup Runtime"
issueTitle: "Battery Will Not Charge or Support the Specified Backup Runtime"
description: "Troubleshoots battery complaints caused by AC power, charging connection, battery state, excessive load, storage condition, or battery-related hardware faults."
assetType: "Infusion Pump"
manufacturer: "ICU Medical"
model: "Plum Duo"
slug: "icu-medical-plum-duo-battery-will-not-charge-or-support-the-specified-backup-runtime"
dateAdded: "2026-11-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that the Plum Duo displayed a low battery shortly after being disconnected from AC for transport."
  cause: "Clinical Engineering verified that the installed battery failed the applicable manufacturer battery-performance test after a full approved charge."
  resolution: "Replaced the battery using the approved service process and verified charging, AC-to-battery transition, and battery performance before returning the pump to service."
helpfulDetails:
  - "Battery complaint"
  - "Charging indication"
  - "AC outlet tested"
  - "Power cord condition"
  - "Battery detection status"
  - "Battery service history"
  - "Approved charge duration"
  - "Battery test result"
  - "AC-to-battery transition result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots battery complaints caused by AC power, charging connection, battery state, excessive load, storage condition, or battery-related hardware faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient From Unexpected Power Loss
Do not leave a patient dependent on a pump with questionable battery operation when loss of AC power or transport could interrupt therapy. Transfer the infusion to another verified pump when necessary.

**Expected outcome:** Patient therapy remains supported by reliable power.

### 2. Confirm the Battery Complaint
Determine whether the battery will not charge, is not detected, discharges rapidly, shuts the pump down unexpectedly, or fails an approved runtime test. Record battery indications and any exact messages.

**Expected outcome:** The specific battery failure is confirmed.

### 3. Verify the AC Source
Connect the pump to a known-good hospital-grade outlet or approved test source. Verify the outlet supplies power and that the pump recognizes external AC.

**Expected outcome:** The pump receives stable AC power.

If the original outlet or connection was faulty and charging resumes normally, verify battery operation before closing the work order.

### 4. Inspect the Power Cord and External Connection
Inspect accessible power cord components and the pump's external power connection for damage, looseness, contamination, or intermittent engagement.

**Expected outcome:** The AC connection is secure and undamaged.

Visible damage or overheating requires removal from service.

### 5. Observe Charging Indications
With the pump connected to stable AC, observe whether the normal charging indication appears. Allow charging according to approved manufacturer procedures before evaluating runtime.

**Expected outcome:** The pump recognizes the battery and indicates normal charging behavior.

### 6. Restart the Pump
With no patient connected, perform a normal restart and recheck battery detection and charging status.

**Expected outcome:** Battery status remains recognized and stable after restart.

### 7. Perform an Approved Battery Test
After appropriate charging, perform the manufacturer's approved battery performance or runtime verification using the specified test conditions. Do not invent a runtime threshold; use current applicable service documentation.

**Expected outcome:** Battery performance meets the applicable manufacturer requirement.

If the battery passes the approved test, document the result and return the device to service if all other checks pass.

### 8. Check Battery Age or Service History
Review available maintenance history for previous battery replacements, repeated battery complaints, or storage periods that may explain reduced capacity.

**Expected outcome:** Battery history is consistent with observed performance or identifies a likely maintenance-related cause.

### 9. Verify Operation During AC-to-Battery Transition
Under controlled non-patient conditions, verify the pump remains operational during normal transfer from AC to battery and back to AC.

**Expected outcome:** The pump maintains operation and correctly recognizes each power source.

### 10. Complete Final Functional Verification
Verify startup, charging, battery operation, power-source transition, alarms, and both infusion channels as required by departmental procedures.

**Expected outcome:** The pump provides reliable power operation and passes applicable battery requirements.

## If the Problem Persists

If the AC source, power connection, normal charging period, restart, and approved battery test have been verified but the battery remains undetected or fails performance requirements, common external causes have been ruled out.

Possible remaining categories include battery deterioration, battery connection, charging circuitry, power-management hardware, or another internal service-level fault.

The pump should be removed from service, labeled **Out of Service**, and evaluated using appropriate manufacturer documentation and approved test equipment. Battery replacement, internal repair, or power-system servicing should be performed only by qualified personnel.

Complete all required electrical, battery, alarm, and functional testing before return to service.

## Clinical Use Tip

Verify battery readiness before transport whenever the infusion could become dependent on battery power.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Battery complaints should first be separated from AC-source and connection problems. Verify charging and performance using approved procedures, remove unreliable batteries from service, and document the measured result rather than relying only on the displayed battery icon.

That is successful troubleshooting.
