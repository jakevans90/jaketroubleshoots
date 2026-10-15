---
schemaVersion: 1
title: "Boston Scientific OPAL HDx Electrophysiology Mapping System - Calibration or Quality-Control Test Fails"
issueTitle: "Calibration or Quality-Control Test Fails"
description: "Troubleshoots failed system checks or quality verification by checking setup, accessories, connections, environment, test equipment, and repeatability before escalation."
assetType: "Electrophysiology Mapping System"
manufacturer: "Boston Scientific"
model: "OPAL HDx"
slug: "boston-scientific-opal-hdx-calibration-or-quality-control-test-fails"
dateAdded: "2026-10-15"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the OPAL HDx quality-control check would not complete successfully before use."
  cause: "Clinical Engineering found a loose external test connection causing inconsistent verification results."
  resolution: "Clinical Engineering secured the connection, repeated the approved quality check successfully, confirmed repeatability, and returned the system to service."
helpfulDetails:
  - "Exact test performed"
  - "Exact failure message"
  - "Test stage that failed"
  - "External test setup"
  - "Cable and connector condition"
  - "Known-good accessories used"
  - "Test equipment used"
  - "Environmental factors observed"
  - "Repeat-test results"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots failed system checks or quality verification by checking setup, accessories, connections, environment, test equipment, and repeatability before escalation.

## Step-by-Step Troubleshooting

### 1. Remove the System From Clinical Dependence

Do not use a system for patient mapping when a required calibration, quality-control, or verification test has failed.

Move the procedure to verified equipment if continued mapping capability is required.

**Expected outcome:** No patient depends on equipment that has not passed required verification.

### 2. Identify the Exact Failed Test

Record:

- Name of the test
- Exact displayed result or message
- Stage at which it fails
- Whether it fails consistently
- Whether any system component was recently changed

Do not assume all failed system checks represent a calibration failure.

**Expected outcome:** The specific verification failure is clearly identified.

### 3. Verify Correct Test Setup

Confirm the test is being performed using the intended external connections, accessories, and approved test equipment.

Check that the test setup matches the applicable manufacturer or facility procedure.

**Expected outcome:** The test configuration is correct and repeatable.

### 4. Inspect External Test Connections

Check accessible connections involved in the test for:

- Loose connectors
- Damaged cables
- Bent contacts
- Contamination
- Incorrect connections
- Strain or intermittent movement

**Expected outcome:** Test connections are secure and intact. If correcting a connection produces a valid passing result, repeat the test to confirm before stopping troubleshooting.

### 5. Verify Accessories and Test Equipment

Confirm external accessories and test equipment being used are appropriate and in suitable condition.

If practical, substitute a known-good compatible accessory or test cable.

Do not adjust calibration values simply to obtain a passing result.

**Expected outcome:** A defective external accessory or test connection is either ruled out or identified.

### 6. Check Environmental Conditions

Look for environmental factors that may affect testing, including:

- Equipment movement
- Electromagnetic interference
- Unstable external power
- Improper cable routing
- Recently added nearby equipment

Correct obvious external conditions before repeating the test.

**Expected outcome:** The test environment is stable and appropriate.

### 7. Restart and Repeat Only Through Approved Procedures

If permitted, restart the system and repeat the failed test exactly as required by approved documentation.

Do not repeatedly recalibrate or change configuration without understanding why the test failed.

**Expected outcome:** The test passes consistently using the proper setup. If it does, troubleshooting can stop after final verification.

### 8. Compare With a Known-Good Setup

Where possible, compare the test setup, accessories, or external connections with a known-good OPAL HDx configuration.

Avoid changing multiple variables simultaneously.

**Expected outcome:** Any external difference contributing to the failure is identified.

### 9. Escalate a Repeatable Test Failure

If the calibration or quality-control test continues to fail with correct setup, known-good external accessories, and stable conditions, remove the system from service.

Do not bypass the test or record a passing result that was not achieved.

**Expected outcome:** The failed system is escalated for qualified evaluation.

## If the Problem Persists

Common external setup, accessory, connection, test-equipment, and environmental causes have been ruled out. The remaining problem may involve internal acquisition performance, system configuration, hardware communication, software, or another service-level condition.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

All required tests must pass before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A required verification test that will not pass is a reason to stop, not a reason to bypass the test and continue clinical use.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

A failed verification deserves a structured investigation beginning with setup and external connections. Never force a passing result or assume internal failure prematurely. Escalate persistent failures and document the actual test results and final disposition.

That is successful troubleshooting.
