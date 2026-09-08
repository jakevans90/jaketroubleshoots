---
schemaVersion: 1
title: "Nova Biomedical StatStrip Blood Glucose Meter - Date and Time Incorrect or Reverts After Power Loss"
issueTitle: "Date and Time Incorrect or Reverts After Power Loss"
description: "Incorrect or resetting time caused by synchronization problems, power loss, configuration, docking issues, or a service-level clock-retention problem."
assetType: "Blood Glucose Meter"
manufacturer: "Nova Biomedical"
model: "StatStrip"
slug: "nova-biomedical-statstrip-date-and-time-incorrect-or-reverts-after-power-loss"
dateAdded: "2026-09-08"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that the StatStrip displayed the wrong date and time after being removed from the dock."
  cause: "Clinical Engineering found the meter had not synchronized correctly while using a malfunctioning docking station."
  resolution: "The meter was synchronized on a known-good dock, date and time retention were verified through restart testing, and the meter was returned to service."
helpfulDetails:
  - "Incorrect date and time observed"
  - "Correct reference time"
  - "Battery status"
  - "Recent power-loss history"
  - "Dock used"
  - "Synchronization status"
  - "Comparison-meter time"
  - "Configuration observed"
  - "Restart results"
  - "Final timestamp verification"
---

## What This Guide Helps With
Incorrect or resetting time caused by synchronization problems, power loss, configuration, docking issues, or a service-level clock-retention problem.

## Step-by-Step Troubleshooting

### 1. Protect Result Traceability

If the meter displays substantially incorrect date or time, do not rely on it for patient testing until result timestamps can be trusted.

Provide another verified meter if testing is required.

**Expected outcome:** Patient results are not generated with unreliable timestamps.

### 2. Confirm the Failure Pattern

Determine whether the time is merely offset, progressively drifting, or resetting after battery depletion, shutdown, charging, or docking.

Record the displayed date and time.

**Expected outcome:** The problem pattern is clearly defined.

### 3. Compare With the Correct Facility Time

Verify the current time using an approved facility reference.

Check whether the meter differs by minutes, hours, date, or time zone.

**Expected outcome:** The magnitude and type of time error are known.

### 4. Check Meter Power Status

Inspect battery condition, charging behavior, and whether the meter recently experienced complete power loss.

A power-related event may help explain when the clock changed.

**Expected outcome:** Obvious power instability is ruled out or identified.

### 5. Verify Docking and Synchronization

Place the meter on a known-good compatible dock according to normal workflow and confirm that it is detected.

If time is centrally synchronized, allow the approved synchronization process to occur.

**Expected outcome:** The meter communicates with the docking or management system and receives current information when designed to do so.

### 6. Compare With Another Meter

Check the date and time on another StatStrip using the same dock or management environment.

**Expected outcome:** The comparison helps determine whether the issue is meter-specific or system-wide.

If multiple meters show the same incorrect time, investigate the central configuration or infrastructure.

### 7. Verify Authorized Time Configuration

Review only accessible and approved configuration settings related to time or system synchronization.

Do not make unsupported service-level configuration changes.

**Expected outcome:** Time configuration agrees with the facility's intended setup.

### 8. Recheck After Power Cycling

After synchronization and with adequate power, restart the meter normally and verify whether date and time are retained.

Do not repeatedly power-cycle a meter being used clinically.

**Expected outcome:** Correct time remains stable after a normal restart.

### 9. Perform a Retention Check

After the meter has been disconnected from the dock and operated normally, recheck date and time.

If appropriate, repeat after a normal shutdown and restart.

**Expected outcome:** The correct clock setting is retained consistently.

If successful, troubleshooting can stop.

### 10. Escalate a Meter That Cannot Retain Time

If date or time repeatedly resets despite correct synchronization and stable power, remove the meter from service.

**Expected outcome:** Patient results are not generated with unreliable timestamps.

## If the Problem Persists

External synchronization, dock, configuration, and obvious power causes have been ruled out. Remaining possibilities include internal clock-retention failure, internal power-retention issues, software problems, or central system configuration faults.

The meter should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation if the problem is meter-specific.
- Evaluated using appropriate Nova Biomedical documentation and approved test equipment.
- Repaired or configured only by qualified personnel.
- Verified for correct clock retention and result timestamps before return to service.

Accurate timestamps are part of safe result traceability, and knowing when to escalate is proper troubleshooting.

## Clinical Use Tip

Incorrect meter time can make a clinically valid glucose result appear in the wrong sequence within the patient record.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Treat accurate time as part of result integrity, check synchronization and power before assuming an internal clock failure, and remove the meter from service when reliable timestamps cannot be maintained.

That is successful troubleshooting.
