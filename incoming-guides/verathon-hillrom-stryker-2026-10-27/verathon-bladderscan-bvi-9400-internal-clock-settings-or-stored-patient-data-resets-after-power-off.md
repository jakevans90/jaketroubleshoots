---
schemaVersion: 1
title: "Verathon BladderScan BVI 9400 Bladder Scanner - Internal Clock, Settings, or Stored Patient Data Resets After Power-Off"
issueTitle: "Internal Clock, Settings, or Stored Patient Data Resets After Power-Off"
description: "Troubleshoots time, settings, or stored-data loss after shutdown by checking power state, shutdown method, configuration, storage behavior, and repeatability."
assetType: "Bladder Scanner"
manufacturer: "Verathon"
model: "BladderScan BVI 9400"
slug: "verathon-bladderscan-bvi-9400-internal-clock-settings-or-stored-patient-data-resets-after-power-off"
dateAdded: "2026-10-27"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the BladderScan BVI 9400 date and time returned to incorrect values after the scanner was powered off."
  cause: "Clinical Engineering confirmed that the clock reset after repeated normal power cycles even though external charging and shutdown operation were normal."
  resolution: "Clinical Engineering removed the scanner from service, labeled it for bench evaluation, and documented the repeatable clock-retention failure for qualified service repair and post-repair verification."
helpfulDetails:
  - "Exact information that reset"
  - "Date and time before and after shutdown"
  - "Settings before and after shutdown"
  - "Whether stored records were affected"
  - "Normal versus unexpected shutdown"
  - "Charging and external power status"
  - "Whether the problem occurs after every power cycle"
  - "Results using an appropriate test record"
  - "Unexpected restart behavior"
  - "Configuration observed"
  - "Number of successful or failed retention tests"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots time, settings, or stored-data loss after shutdown by checking power state, shutdown method, configuration, storage behavior, and repeatability.

## Step-by-Step Troubleshooting
### 1. Protect Patient Data and Clinical Workflow

If stored patient information disappears or timestamps become unreliable, do not depend on the scanner as the sole record of clinical results until the behavior is understood.

Use the facility's approved alternate documentation process and protect existing stored records from unnecessary deletion or overwrite.

**Expected outcome:** Patient care records and workflow are protected while the scanner is evaluated. If data integrity cannot be assured, remove the unit from clinical use.

### 2. Confirm Exactly What Resets

Determine whether the reported problem involves:

- Date and time
- User-accessible settings
- Stored patient examinations
- All three
- Only specific settings
- Only a prolonged power-off period
- Every shutdown

Record the values before powering the device off so they can be compared afterward.

**Expected outcome:** The specific information being lost and the conditions causing the reset are clearly identified.

### 3. Verify Normal Startup and General Operation

Power the scanner on and verify that it starts normally without unexpected restart loops, warnings, display problems, or other abnormal behavior.

Check whether the current date, time, settings, and stored records are already correct before starting the controlled test.

**Expected outcome:** The scanner boots normally and provides a stable baseline for testing. If startup itself is abnormal, remove the unit from service and evaluate the broader power/startup complaint.

### 4. Check Charging and External Power Condition

Verify the scanner's approved charging or power arrangement is connected and functioning as expected. Inspect accessible power connectors, cradle contacts, charger connections, and cables for damage or contamination.

Allow the device to operate using its normal approved power arrangement before repeating the shutdown test.

**Expected outcome:** The scanner receives stable external power and shows no obvious charging or connection abnormality. If correcting an external power connection resolves the reset behavior, verify another power cycle and troubleshooting can stop.

### 5. Verify the Shutdown Method

Use the normal operator shutdown procedure rather than abruptly removing power, disconnecting a charger during an active process, or otherwise forcing the device off.

Observe whether the scanner completes its shutdown normally.

**Expected outcome:** The unit shuts down through its intended normal workflow. If the reset occurred only after an improper shutdown and normal shutdown preserves settings and data, document the finding and troubleshooting can stop.

### 6. Establish a Controlled Baseline

Record the following before the test:

- Displayed date and time
- Relevant user-accessible settings
- Number or identity of appropriate stored test records
- Current power condition

If permitted, create an appropriate nonpatient test record for verification rather than using identifiable clinical data unnecessarily.

**Expected outcome:** A clear before-and-after comparison is available.

### 7. Perform a Controlled Power-Off Test

Power the scanner off normally. After an appropriate controlled interval, power it back on and compare the date, time, settings, and stored test information with the baseline.

Do not repeatedly cycle power excessively in an attempt to force a failure.

**Expected outcome:** The scanner retains expected settings, clock information, and stored data through a normal power cycle. If retention is correct and repeated testing is satisfactory, troubleshooting can stop.

### 8. Determine Whether the Problem Is Data-Specific or System-Wide

If stored information is affected, determine whether:

- Only one record is missing
- New test records disappear after shutdown
- Older records remain
- Settings reset while records remain
- Clock information resets independently

This distinction helps determine whether the problem is a record-management issue, configuration issue, or broader retention problem.

**Expected outcome:** The symptom is narrowed to a specific retention category without assuming an internal component failure.

### 9. Review User-Accessible Date, Time, and Configuration Settings

Verify the scanner's accessible clock and configuration values. Compare them with facility requirements or a known-good BVI 9400 when appropriate.

Make only authorized changes and record any configuration corrected.

Do not access restricted service menus or alter undocumented parameters.

**Expected outcome:** Accessible configuration is correct and remains retained after a normal power cycle. If an authorized settings correction resolves the issue, perform another complete power-cycle test and troubleshooting can stop.

### 10. Verify Battery-Supported Operation if Applicable

Observe whether the scanner remains stable during normal battery operation and transition between approved charging/power conditions.

A device that unexpectedly loses power or restarts may present as a settings-retention problem when the underlying symptom is actually unstable power.

Do not open the battery compartment or replace internal energy-storage components unless specifically authorized by approved service documentation.

**Expected outcome:** The scanner remains powered and stable during normal approved use. Unexpected shutdowns or resets require removal from service and qualified evaluation.

### 11. Perform Final Retention Verification

After any correction:

1. Confirm the correct clock and settings.
2. Save an appropriate test record if required.
3. Shut down normally.
4. Restart the scanner.
5. Verify the clock, configuration, and test record remain correct.
6. Repeat as necessary to establish reliable operation.

**Expected outcome:** Information remains correctly retained across repeated normal power cycles. If retention is consistent, the scanner may be returned to service according to facility procedure and troubleshooting can stop.

### 12. Escalate Persistent Retention Failures

If the clock, configuration, or stored data continues to reset after external power, charging, shutdown procedure, configuration, and controlled power-cycle behavior have been verified, do not proceed with internal memory, battery, or circuit-level repair without appropriate service documentation.

**Expected outcome:** The device is removed from service and routed for qualified bench or manufacturer-level evaluation.

## If the Problem Persists
Common external and workflow causes have been ruled out. Remaining possibilities may involve internal backup power, nonvolatile storage, software, configuration retention, power-management circuitry, or another service-level issue.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

After repair, verify clock retention, configuration retention, stored-record integrity, normal shutdown, restart, and overall scanner function before returning the device to clinical use.

Knowing when to stop external troubleshooting instead of pursuing unauthorized internal memory or power repairs is proper troubleshooting.

## Clinical Use Tip
When timestamps or stored records are unreliable, ensure the clinical result is documented through an approved alternate method before the scanner is removed from service.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Protect patient information first and use controlled before-and-after testing to determine exactly what is being lost. Verify power, shutdown procedure, settings, and retention behavior before assuming an internal fault, then escalate persistent data-integrity problems with complete documentation.

That is successful troubleshooting.
