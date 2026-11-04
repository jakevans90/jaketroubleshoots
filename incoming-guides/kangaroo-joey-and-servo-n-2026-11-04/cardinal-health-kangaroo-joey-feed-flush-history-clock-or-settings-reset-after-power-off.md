---
schemaVersion: 1
title: "Cardinal Health Kangaroo Joey Feeding Pump - Feed/Flush History, Clock, or Settings Reset After Power-Off"
issueTitle: "Feed/Flush History, Clock, or Settings Reset After Power-Off"
description: "Evaluates loss of stored history, clock information, or retained settings caused by shutdown method, configuration, depleted power, or service-level memory problems."
assetType: "Feeding Pump"
manufacturer: "Cardinal Health"
model: "Kangaroo Joey"
slug: "cardinal-health-kangaroo-joey-feed-flush-history-clock-or-settings-reset-after-power-off"
dateAdded: "2026-11-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the Kangaroo Joey clock and retained settings reset after the pump was powered off."
  cause: "Clinical Engineering found the pump's main battery was deeply discharged and the reset did not recur after normal charging and controlled power-cycle testing."
  resolution: "Restored the pump to a normal charged state, verified clock and setting retention through repeated normal startup, and returned the pump to service."
helpfulDetails:
  - "Information that reset"
  - "Values before shutdown"
  - "Values after restart"
  - "Type of shutdown"
  - "Whether the battery had fully discharged"
  - "AC and charging status"
  - "Unexpected restart behavior"
  - "Clock behavior"
  - "Settings observed"
  - "Repeatability of the reset"
  - "Final device status"
---

## What This Guide Helps With

Evaluates loss of stored history, clock information, or retained settings caused by shutdown method, configuration, depleted power, or service-level memory problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care Before Testing
If settings or historical information cannot be trusted, remove the affected pump from active patient use before attempting shutdown or restart testing.

Transfer feeding to another verified pump if continued therapy is required.

**Expected outcome:** Patient feeding is not affected by testing or uncertain retained information.

### 2. Identify Exactly What Resets
Determine whether the reported loss involves feeding history, flush history, time or date, programmed therapy information, user preferences, or multiple items.

Record the values before changing anything.

**Expected outcome:** The specific retained information that is being lost is identified.

### 3. Confirm Normal Shutdown Behavior
Ask whether the reset followed a normal power-off, complete battery depletion, prolonged storage, battery replacement, unexpected shutdown, or loss of AC power.

Reproduce only under controlled nonpatient conditions.

**Expected outcome:** The event associated with the reset is known.

### 4. Verify AC and Battery Condition
Connect the pump to a known-good AC source and confirm normal charging behavior.

If the primary battery is severely discharged or unreliable, resolve that condition before evaluating retention behavior.

**Expected outcome:** The pump has stable power for testing.

### 5. Review User-Accessible Settings
Confirm the relevant normal settings and clock information without entering restricted service menus or changing protected configuration.

Document the observed values.

**Expected outcome:** A baseline is established before the power cycle.

### 6. Perform a Controlled Power Cycle
With the pump disconnected from the patient, shut it down normally, wait briefly, and restart it.

Compare the retained values with the documented baseline.

**Expected outcome:** Information intended to persist through a normal shutdown remains intact.

If expected information is retained and the issue cannot be reproduced, document the test and continue observation as appropriate.

### 7. Distinguish Normal Clearing From Unexpected Loss
Determine whether the reported item is designed to clear during a normal workflow or whether it should remain stored according to approved documentation.

Do not assume every treatment value should persist indefinitely.

**Expected outcome:** Normal device behavior is separated from an actual retention failure.

### 8. Check for Unexpected Power Loss
Observe whether the pump restarts unexpectedly, loses power when disconnected from AC, or shows other evidence of an unreliable primary battery or power connection.

**Expected outcome:** A general power problem is ruled out before concluding there is a memory-related fault.

### 9. Repeat the Retention Check
If the reset is reproducible, repeat the test once under the same controlled conditions to confirm the failure.

Avoid unnecessary repeated cycling.

**Expected outcome:** A consistent retention problem is confirmed or ruled out.

### 10. Escalate Reproducible Data or Clock Loss
If information that should be retained repeatedly resets after a normal shutdown despite stable power, remove the pump from service for qualified evaluation.

**Expected outcome:** A pump with unreliable stored information is prevented from returning to clinical use without assessment.

## If the Problem Persists

Shutdown method, depleted battery, normal clearing behavior, and routine configuration issues have been ruled out. Remaining causes may involve internal timekeeping, memory retention, power-management circuitry, configuration integrity, or another service-level condition.

The device should be removed from service, labeled **Out of Service**, and evaluated using appropriate Cardinal Health service documentation and approved test equipment. Configuration or repair should be performed only by qualified personnel. Verify clock, retained settings, feeding functions, and applicable alarms before return to service.

Knowing when a data-retention problem requires escalation is proper troubleshooting.

## Clinical Use Tip

Do not rely on pump history as the sole clinical record when the device has demonstrated unexplained loss of stored information.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Define exactly what information is being lost, separate expected clearing behavior from a true retention fault, rule out power problems first, and escalate reproducible configuration or memory failures with clear documentation.

That is successful troubleshooting.
