---
schemaVersion: 1
title: "Medtronic 5392 External Pacemaker - Self-Test Fails or Error 0004 Appears at Startup"
issueTitle: "Self-Test Fails or Error 0004 Appears at Startup"
description: "Startup self-test failure or Error 0004, including battery, cable, control, connection, and device-condition causes that can be externally verified."
assetType: "External Pacemaker"
manufacturer: "Medtronic"
model: "5392"
slug: "medtronic-5392-self-test-fails-or-error-0004-appears-at-startup"
dateAdded: "2026-11-12"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Medtronic 5392 displayed Error 0004 and would not complete its startup self-test."
  cause: "Clinical Engineering reproduced the startup failure after verifying battery installation and disconnecting external patient cables."
  resolution: "Device was removed from service and sent for qualified bench evaluation after the self-test failure persisted with known-good batteries and external causes were ruled out."
helpfulDetails:
  - "Exact startup message or Error 0004"
  - "Whether the failure occurs every startup"
  - "Battery type and condition"
  - "Results with known-good batteries"
  - "Accessories connected during the failure"
  - "Condition of battery contacts and receptacles"
  - "Visible impact or fluid damage"
  - "Display and alarm behavior"
  - "Results of repeated power cycles"
  - "Final device status"
---

## What This Guide Helps With

Startup self-test failure or Error 0004, including battery, cable, control, connection, and device-condition causes that can be externally verified.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Pacing Support

Do not troubleshoot the Medtronic 5392 while a pacing-dependent patient relies on the affected device. Transfer pacing support to another verified external pacemaker or other clinically appropriate method before testing.

If the unit cannot complete its startup self-test, behaves unpredictably, or cannot provide dependable pacing, remove it from clinical use.

**Expected outcome:** Patient pacing support is maintained independently of the suspect pacemaker, allowing safe troubleshooting.

### 2. Confirm the Exact Startup Condition

Power the pacemaker on away from the patient and observe the complete startup sequence. Record whether the self-test stops consistently, whether Error 0004 appears every time, and whether any other abnormal display, audible, or control behavior accompanies it.

Do not assign a specific internal meaning to the error unless confirmed by approved Medtronic service documentation.

**Expected outcome:** The reported failure is reproduced and accurately documented. If startup completes normally on repeated tests, continue verification before returning the unit to service.

### 3. Inspect the Pacemaker Externally

Inspect the enclosure, battery compartment, battery contacts visible without disassembly, connector receptacles, controls, display, and labeling for contamination, corrosion, fluid intrusion, cracking, deformation, or impact damage.

Remove the device from service immediately if physical damage or fluid intrusion could affect safe operation.

**Expected outcome:** No external damage or contamination capable of interfering with startup is present.

### 4. Verify Battery Condition and Installation

Remove and reinstall the approved batteries using correct orientation. Confirm that the batteries are within serviceable condition and that the compartment closes securely.

When appropriate, repeat the startup test using known-good approved batteries.

**Expected outcome:** The pacemaker starts normally with properly installed known-good batteries. If the self-test passes consistently, continue final verification and troubleshooting can stop after successful testing.

### 5. Isolate External Patient Cables and Accessories

Disconnect patient cables and unnecessary accessories before repeating startup. Inspect connected accessories for contamination, damaged pins, bent contacts, or abnormal mechanical loading of the receptacles.

If startup succeeds with an accessory removed, inspect or substitute that accessory before reconnecting it.

**Expected outcome:** The pacemaker completes startup with no defective external accessory influencing the self-test.

### 6. Check Controls for Binding or Abnormal Input

Verify that accessible keys and control dials are not stuck, partially depressed, contaminated, or mechanically damaged. Operate them gently through their normal range without forcing them.

**Expected outcome:** Controls move normally and do not appear to interfere with startup.

### 7. Repeat Startup With a Controlled Bench Configuration

With known-good batteries installed and external accessories disconnected, perform several normal power cycles according to approved service practices.

Do not enter unauthorized service modes or alter protected configuration settings.

**Expected outcome:** Startup and self-test complete consistently without Error 0004. If so, proceed to functional verification and troubleshooting can stop after verification.

### 8. Perform Final Functional Verification

Before return to service, connect the pacemaker to appropriate approved test equipment and verify required pacing, sensing, controls, indicators, and alarms according to manufacturer procedures and facility policy.

**Expected outcome:** All required functions operate normally and consistently. The unit may be returned to service only after successful verification.

### 9. Escalate an Unresolved Self-Test Failure

If Error 0004 or the failed self-test persists despite known-good batteries, isolated accessories, and satisfactory external inspection, stop external troubleshooting.

**Expected outcome:** The device remains out of clinical service and is referred for qualified bench evaluation.

## If the Problem Persists

Common external causes have been ruled out. A persistent startup failure may involve an internal power, control, self-test, display, connector, or other service-level condition that cannot be safely diagnosed through routine external troubleshooting.

The device should be:

- Removed from service and labeled **Out of Service**
- Sent for repair or qualified bench evaluation
- Evaluated using appropriate Medtronic documentation and approved test equipment
- Repaired or configured only by qualified personnel
- Subjected to complete return-to-service functional testing before clinical use

Knowing when to stop external troubleshooting rather than assuming a specific internal component has failed is proper troubleshooting.

## Clinical Use Tip

Maintain verified alternate pacing support before removing or testing any external pacemaker used on a pacing-dependent patient.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient first, verify batteries and external accessories before assuming internal failure, document the reproduced condition clearly, and escalate persistent self-test faults for qualified evaluation.

That is successful troubleshooting.
