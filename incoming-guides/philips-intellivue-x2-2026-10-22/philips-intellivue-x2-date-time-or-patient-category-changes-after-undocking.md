---
schemaVersion: 1
title: "Philips IntelliVue X2 Patient Monitor - Date, Time, or Patient Category Changes After Undocking"
issueTitle: "Date, Time, or Patient Category Changes After Undocking"
description: "Troubleshoots unexpected date, time, or patient-category changes after undocking caused by synchronization, configuration, workflow, docking, or system-association problems."
assetType: "Patient Monitor"
manufacturer: "Philips"
model: "IntelliVue X2"
slug: "philips-intellivue-x2-date-time-or-patient-category-changes-after-undocking"
dateAdded: "2026-10-22"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the IntelliVue X2 displayed the correct time while docked but changed to an incorrect time after being undocked for transport."
  cause: "Clinical Engineering confirmed that the time discrepancy consistently followed the X2 during independent operation while other monitoring devices displayed the correct facility time."
  resolution: "The X2 was removed from service for qualified bench evaluation after repeated undock/redock testing confirmed a device-specific time synchronization problem."
helpfulDetails:
  - "Exact field that changed"
  - "Value while docked"
  - "Value after undocking"
  - "Value after redocking"
  - "Patient identity status"
  - "Patient category observed"
  - "Host monitor information"
  - "Other monitors affected or unaffected"
  - "Docking location"
  - "Known-good dock comparison"
  - "Network or synchronization observations"
  - "Final undock/redock test result"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots unexpected date, time, or patient-category changes after undocking caused by synchronization, configuration, workflow, docking, or system-association problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient Before Making Changes

If an unexpected patient category or time change could affect monitoring behavior, alarm interpretation, documentation, or patient identification, do not make unverified corrections while the X2 is actively relied upon for patient care.

Provide alternate verified monitoring if necessary before troubleshooting.

**Expected outcome:** Patient monitoring remains reliable while the configuration discrepancy is investigated.

### 2. Confirm Exactly What Changes

Document the information shown while the X2 is docked and immediately after undocking.

Determine whether the change involves:

- Date
- Clock time
- Time zone presentation
- Patient category
- Patient demographics
- More than one of these items

Determine whether the value returns to normal after redocking.

**Expected outcome:** The specific field and the exact point at which it changes are identified. If repeated undocking does not reproduce the issue and all displayed information remains correct, document the test and troubleshooting can stop.

### 3. Verify the Current Patient Identity

Confirm that the X2 remains associated with the intended patient before and after undocking.

A change in patient assignment or admission state may appear to be a category or configuration problem.

Do not alter demographics or patient category merely to match an expected screen without first confirming the patient.

**Expected outcome:** The correct patient remains associated with the X2. If an authorized correction of an identified patient-assignment error resolves the problem, verify operation and troubleshooting can stop.

### 4. Compare Docked and Undocked Values Directly

Record the displayed date, time, and patient category while docked.

Undock the X2 using the normal transport workflow and compare those same fields without changing settings.

Then redock it and observe whether they change again.

**Expected outcome:** The displayed information remains consistent through the dock/undock cycle. If the discrepancy reliably follows the operating state, continue troubleshooting rather than treating it as a random user-setting change.

### 5. Check the Docking Interface

Inspect accessible docking contacts and connectors for:

- Incomplete engagement
- Contamination
- Physical damage
- Loose fit
- Evidence of fluid intrusion

Confirm the X2 is fully recognized when docked and transitions normally to independent transport operation when removed.

**Expected outcome:** Docking and undocking occur cleanly without intermittent recognition. If correcting an external docking issue eliminates the information change, repeat the test and troubleshooting can stop.

### 6. Determine Whether the X2 or Host Is Supplying the Unexpected Information

Compare the X2 with the host or receiving monitor before undocking.

If available, compare both with another verified monitoring system or the facility's authoritative time source.

For patient category, verify the intended category through the approved clinical workflow rather than assuming either display is correct.

**Expected outcome:** It is clear whether the unexpected information appears to originate with the X2, the host monitoring system, or the broader environment.

### 7. Check for a Workflow-Related Category Change

Determine whether the transport process involved:

- Admission or discharge
- Moving the patient to another monitoring location
- Reassociation with another host
- Selecting a new patient
- A category change entered during transport preparation

Review only normal user-accessible information and involve clinical staff if patient workflow actions need clarification.

**Expected outcome:** No legitimate patient workflow explains the unexpected category change. If an identified workflow action caused the change and normal values are restored through the approved workflow, verify and troubleshooting can stop.

### 8. Check Time Synchronization and Infrastructure Clues

If date or time changes after undocking, determine whether other connected monitors show the same incorrect time.

Look for patterns such as:

- One X2 affected
- One host or location affected
- Multiple monitors affected
- Correct time while connected but incorrect time when independent
- Incorrect time corrected after reconnection

Do not manually alter network time sources or protected configuration as a troubleshooting shortcut.

**Expected outcome:** The issue is isolated to the X2, its host, or a broader synchronization/configuration problem. If an external infrastructure issue is confirmed, escalate to the responsible support group.

### 9. Compare With a Known-Good Compatible Docking Location

With the X2 removed from patient use, test it with another approved compatible docking location if available.

Compare whether the same date, time, or category change occurs when the unit is docked and undocked there.

**Expected outcome:** The comparison shows whether the behavior follows the X2 or the original host/docking location. If the problem is isolated to an external location and corrected, complete final verification and troubleshooting can stop.

### 10. Avoid Unsupported Configuration Changes

If the observed values appear to be configuration-dependent, record the behavior and current settings visible through the normal clinical interface.

Do not enter unauthorized service modes, change network configuration, modify protected defaults, or force synchronization settings without appropriate documentation and authorization.

**Expected outcome:** Configuration evidence is preserved without introducing additional variables. Unresolved configuration behavior is escalated appropriately.

### 11. Perform Final Undock/Redock Verification

After any correction, perform a controlled test and confirm:

- Correct date and time while docked
- Correct date and time after undocking
- Correct patient category
- Correct patient identity
- Stable monitoring during transport mode
- Correct values after redocking
- Normal association with the receiving monitoring system

**Expected outcome:** Date, time, patient category, and patient identity remain correct through the complete transport cycle. If so, troubleshooting is complete.

## If the Problem Persists

If patient identity, workflow, docking, host behavior, time synchronization clues, and known-good comparisons have been checked but information continues to change after undocking, common external causes have been ruled out.

Possible remaining categories include a device configuration issue, synchronization problem, host-monitor configuration mismatch, software/service condition, internal timekeeping problem, or broader monitoring infrastructure issue.

The X2 should be:

- Removed from service when the incorrect information could affect safe monitoring or documentation
- Labeled Out of Service
- Sent for repair or bench evaluation when the fault follows the X2
- Escalated to the appropriate monitoring, network, or configuration support team when the issue is system-wide
- Evaluated using appropriate Philips documentation and approved test equipment
- Repaired or configured only by qualified personnel

Complete a full undock/redock functional verification before returning the X2 to clinical use.

Knowing when to stop changing settings and escalate a reproducible synchronization or configuration problem is proper troubleshooting.

## Clinical Use Tip

Before beginning transport, verify patient identity and category on the X2; after undocking, confirm they remain correct before relying on alarm and trend information.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Unexpected changes in time or patient category can affect documentation, patient association, and monitoring workflow. Verify the patient first, reproduce the issue without changing protected settings, separate device behavior from host or infrastructure behavior, and escalate when external causes are exhausted. Document exactly what changed and how the final condition was verified.

That is successful troubleshooting.
