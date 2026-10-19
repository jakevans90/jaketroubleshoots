---
schemaVersion: 1
title: "GE Healthcare CASE Stress Test System - Therapy or Output Will Not Start"
issueTitle: "Therapy or Output Will Not Start"
description: "A commanded stress-test output or connected exercise function does not begin, respond, or operate as expected from the CASE system."
assetType: "Stress Test System"
manufacturer: "GE Healthcare"
model: "CASE"
slug: "ge-healthcare-case-therapy-or-output-will-not-start"
dateAdded: "2026-10-19"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the treadmill would not start when commanded from the GE Healthcare CASE system."
  cause: "Clinical Engineering found the external communication cable between CASE and the treadmill was not fully seated."
  resolution: "Secured the communication cable and verified normal treadmill start, control response, and stop operation without a patient present."
helpfulDetails:
  - "Exact output or peripheral affected"
  - "Peripheral power status"
  - "Communication cable condition"
  - "Ready or safety-control status"
  - "Device selected in CASE"
  - "Independent peripheral test result"
  - "Restart results"
  - "Control response after correction"
  - "Final device status"
---

## What This Guide Helps With
A commanded stress-test output or connected exercise function does not begin, respond, or operate as expected from the CASE system.

## Step-by-Step Troubleshooting
### 1. Protect the Patient Before Testing Exercise Functions
Do not troubleshoot a treadmill, ergometer, or other exercise-control problem while a patient is depending on the affected equipment. Stop exercise safely and assist the patient according to clinical protocol.

CASE is a diagnostic stress-test system rather than a therapeutic device; first determine what staff mean by “therapy or output.”

**Expected outcome:** The patient is safe and the reported output function is clearly identified.

### 2. Identify the Exact Output That Will Not Start
Determine whether staff are referring to a connected treadmill, ergometer, printer, acquisition function, or another configured peripheral. Confirm the expected action and what actually occurs.

**Expected outcome:** The problem is narrowed to one specific CASE-controlled or CASE-associated output.

### 3. Verify the Peripheral Has Power
Check the affected external device for normal power indications and inspect its accessible power cord and approved facility power source.

**Expected outcome:** The connected peripheral is powered and ready. If restoring peripheral power corrects the problem, verify operation and stop troubleshooting.

### 4. Inspect Communication and Control Connections
Check accessible cables between CASE and the affected exercise or output device. Verify connectors are secure, undamaged, and connected to the correct interfaces.

**Expected outcome:** External control and communication connections are intact. If reseating a loose connection restores normal operation, proceed to final verification.

### 5. Check Peripheral Readiness and Safety Conditions
Verify the connected device is in its normal ready state and that obvious external stop controls, interlocks, or safety controls are not preventing operation. Do not bypass safety switches or interlocks.

**Expected outcome:** The peripheral reports or demonstrates a safe ready condition.

### 6. Confirm the Correct Device Is Selected
Review user-accessible CASE settings to verify the intended exercise or output device is selected for the test configuration. Do not change protected installation or service parameters without authorization.

**Expected outcome:** CASE is configured to use the intended connected peripheral.

### 7. Test the Peripheral Independently When Appropriate
Using its normal approved controls and with no patient attached, determine whether the external device operates independently of CASE when that test is supported.

**Expected outcome:** If the peripheral fails independently, the problem is isolated outside the CASE workstation. Remove the affected peripheral from service and stop troubleshooting CASE.

### 8. Restart the Communication Path
With the system safely out of clinical use, perform a controlled restart of CASE and the affected external device using normal procedures.

**Expected outcome:** Communication is re-established and the intended output responds normally.

### 9. Perform Final Functional Verification
Without a patient on the equipment, verify the CASE system can communicate with and appropriately command the configured exercise or output device through the expected workflow. Verify emergency stop and safety functions remain available as applicable.

**Expected outcome:** The output starts and responds consistently. The issue is resolved and troubleshooting can stop.

## If the Problem Persists
Power, cabling, peripheral readiness, user-accessible configuration, and basic independent operation have been checked. The remaining issue may involve CASE communication hardware, peripheral control electronics, interface configuration, software, or service-level settings.

Remove the affected system or peripheral from service and label it **Out of Service**. Perform bench evaluation using appropriate manufacturer documentation and approved test equipment. Do not bypass safety controls or modify undocumented configuration to restore operation.

Verify the complete CASE-to-peripheral control path before return to service.

## Clinical Use Tip
Always verify treadmill or ergometer communication and stop controls before placing a patient on the exercise equipment.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
First define the failed output, then separate the CASE workstation from the connected peripheral using power, connection, readiness, and independent-operation checks. Never bypass safety functions, and verify the complete control path before clinical use.

That is successful troubleshooting.
