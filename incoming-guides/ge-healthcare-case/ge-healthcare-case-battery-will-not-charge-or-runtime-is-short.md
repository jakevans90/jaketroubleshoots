---
schemaVersion: 1
title: "GE Healthcare CASE Stress Test System - Battery Will Not Charge or Runtime Is Short"
issueTitle: "Battery Will Not Charge or Runtime Is Short"
description: "A battery-backed CASE component, workstation accessory, or associated UPS does not charge or provides unexpectedly short backup runtime."
assetType: "Stress Test System"
manufacturer: "GE Healthcare"
model: "CASE"
slug: "ge-healthcare-case-battery-will-not-charge-or-runtime-is-short"
dateAdded: "2026-10-19"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the backup power unit supporting the CASE workstation would not maintain power during a brief AC interruption."
  cause: "Clinical Engineering verified normal AC input but found the backup battery failed the approved battery test."
  resolution: "Replaced the approved battery component and verified normal charging and successful backup-power operation before return to service."
helpfulDetails:
  - "Exact battery-backed component"
  - "AC power status"
  - "Charging indicators"
  - "Battery or UPS fault indications"
  - "Physical battery condition"
  - "Charge history if known"
  - "Approved battery-test result"
  - "Known-good substitution result"
  - "AC and backup-power verification"
  - "Final device status"
---

## What This Guide Helps With
A battery-backed CASE component, workstation accessory, or associated UPS does not charge or provides unexpectedly short backup runtime.

## Step-by-Step Troubleshooting
### 1. Determine Which Battery Is Involved
Identify the exact battery-backed component. CASE installations may vary, and a stationary workstation may rely primarily on AC power while another system component or UPS provides battery backup.

Do not assume the CASE workstation contains a user-serviceable battery merely because staff report a “battery problem.”

**Expected outcome:** The battery complaint is tied to a specific component or approved backup-power device.

### 2. Protect the Patient and Clinical Workflow
Do not start or continue a stress study if loss of AC power could cause the affected system to shut down unexpectedly and required backup power is unavailable.

**Expected outcome:** The system is not being relied upon beyond its verified power capability.

### 3. Verify AC Input to the Charging Device
Confirm the affected component or UPS is connected to a known-good approved AC source. Inspect the power cord and accessible connections for damage or looseness.

**Expected outcome:** Reliable AC power reaches the charging equipment. If charging resumes after correcting the AC connection, monitor operation and continue to verification.

### 4. Check Charging and Battery Indicators
Observe available charging, battery, or fault indicators and record their state. Compare the observed indications with approved documentation for the specific battery-backed component.

Do not invent interpretations for unfamiliar indicators.

**Expected outcome:** The charging state is understood from supported documentation.

### 5. Allow an Appropriate Charging Opportunity
If the battery was recently depleted or disconnected from AC, allow it to charge according to the applicable manufacturer's instructions before judging runtime.

**Expected outcome:** The battery reaches its normal indicated charged state. If it cannot, proceed with further isolation.

### 6. Inspect Accessible Battery-Related Connections
Where user-accessible and manufacturer-approved, inspect external battery packs, charging leads, or UPS connections for loose connectors, damage, contamination, or swelling.

Do not open sealed battery packs or continue using any battery showing heat, swelling, leakage, odor, or physical damage.

**Expected outcome:** No unsafe battery condition is present and accessible connections are secure.

### 7. Perform an Approved Runtime or Battery Test
Use the manufacturer's supported battery test, UPS self-test, or approved load evaluation when applicable. Do not create an improvised load test on a patient-care system.

**Expected outcome:** The battery or backup device meets applicable manufacturer performance requirements.

### 8. Substitute a Known-Good Approved Battery or UPS if Applicable
If the component uses an approved field-replaceable battery or external UPS and local policy permits substitution, test with a verified compatible replacement.

**Expected outcome:** Normal charging or runtime with the known-good component isolates the original battery or backup unit as the cause.

### 9. Verify System Operation on Intended Power Sources
After correction, confirm the CASE system and required peripherals operate normally from AC and that any intended battery backup functions correctly.

**Expected outcome:** Power remains stable for the intended configuration. The issue is resolved and troubleshooting can stop.

## If the Problem Persists
AC input, accessible charging connections, battery condition, supported testing, and approved substitutions have been evaluated. The remaining issue may involve a failed battery, charger, UPS, internal power electronics, or configuration requiring service.

Remove the affected battery-backed component from service and label it **Out of Service**. Batteries showing swelling, leakage, excessive heat, or other unsafe conditions require immediate isolation according to facility battery-safety procedures.

Evaluate the equipment using appropriate manufacturer documentation and approved test equipment. Perform applicable return-to-service testing after battery or power-system repair.

## Clinical Use Tip
Do not assume backup power is available simply because the CASE workstation is presently operating on AC; verify any required battery-backed component before the stress study.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
First identify exactly which component contains or depends on the battery. Verify AC supply and external charging conditions before replacing components, remove unsafe batteries immediately, and document the actual battery or backup-power test result.

That is successful troubleshooting.
