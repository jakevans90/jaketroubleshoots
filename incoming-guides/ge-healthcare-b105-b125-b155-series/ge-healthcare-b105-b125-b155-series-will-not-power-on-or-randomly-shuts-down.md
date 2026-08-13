---
schemaVersion: 1
title: "GE Healthcare B105 / B125 / B155 Series Patient Monitor - Will Not Power On or Randomly Shuts Down"
issueTitle: "Will Not Power On or Randomly Shuts Down"
description: "Troubleshoots no-power, unexpected shutdown, unstable AC operation, battery-related shutdown, loose power connections, and other externally verifiable causes."
assetType: "Patient Monitor"
manufacturer: "GE Healthcare"
model: "B105 / B125 / B155 Series"
slug: "ge-healthcare-b105-b125-b155-series-will-not-power-on-or-randomly-shuts-down"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the B125 patient monitor shut down intermittently during use."
  cause: "Clinical Engineering found the external AC power cord connection was loose and power was interrupted when the cord was moved."
  resolution: "Replaced the damaged power cord, verified stable AC and battery operation, tested normal movement and alarms, and returned the monitor to service."
helpfulDetails:
  - "Whether the monitor was on AC or battery"
  - "Whether shutdown occurred during transport"
  - "Outlet tested"
  - "Power cord condition"
  - "Battery recognition and condition"
  - "Known-good battery or cord comparison"
  - "Whether the unit rebooted or completely lost power"
  - "Damage, heat, odor, or contamination"
  - "Results before and after correction"
  - "Final functional and alarm test results"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots no-power, unexpected shutdown, unstable AC operation, battery-related shutdown, loose power connections, and other externally verifiable causes.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Monitoring
If the monitor is currently being used on a patient and cannot remain powered reliably, transfer monitoring to another verified patient monitor before troubleshooting.

Do not continue troubleshooting a monitor that may shut down while a patient depends on it.

**Expected outcome:** The patient has continuous monitoring from a reliable device and the affected monitor is available for safe evaluation.

If reliable monitoring has been restored on another device, continue troubleshooting the affected monitor off-patient.

### 2. Confirm the Exact Power Complaint
Determine whether the monitor:
- Does not power on at all
- Starts and immediately shuts down
- Shuts down only on battery
- Shuts down only when moved
- Reboots intermittently
- Loses power when the power cord or connector is disturbed

Ask whether the condition occurs consistently or intermittently.

**Expected outcome:** The failure pattern is clearly identified so AC, battery, connection, or internal causes can be separated.

If the reported issue cannot be reproduced, inspect for intermittent external causes before returning the monitor to service.

### 3. Inspect for Damage or Unsafe Conditions
Inspect the monitor, power cord, AC inlet, mounting arrangement, and accessible connectors for:
- Cracked housings
- Bent or damaged connectors
- Liquid contamination
- Burn marks
- Unusual heat or odor
- Loose components
- Evidence of impact or transport damage

Do not energize equipment with evidence of electrical or liquid damage until appropriately evaluated.

**Expected outcome:** No visible condition is present that makes further powered troubleshooting unsafe.

If damage, overheating, odor, or contamination is found, remove the monitor from service and stop troubleshooting.

### 4. Verify the AC Power Source
Confirm the monitor is connected to an appropriate powered outlet. Test the outlet using an approved method or compare operation at a known-good receptacle.

Avoid assuming the monitor is faulty because another device was previously connected to the same outlet.

**Expected outcome:** A verified AC source is available.

If the monitor operates normally from a known-good outlet, correct or report the facility power issue and troubleshooting can stop after functional verification.

### 5. Inspect and Reseat the Power Connection
Inspect the AC power cord and external power connections. Verify that connections are fully seated and are not easily disturbed.

If permitted by facility practice, substitute a compatible known-good power cord.

Gently observe whether normal handling of the cord or monitor causes power interruption. Do not manipulate damaged electrical connections while energized.

**Expected outcome:** The monitor remains powered with secure external power connections.

If replacing or reseating an external power cord corrects the problem, complete functional verification and troubleshooting can stop.

### 6. Compare AC and Battery Operation
With the monitor off-patient, compare behavior while connected to AC power and while operating from battery as applicable.

Observe whether:
- The monitor powers reliably on AC
- Battery status is recognized
- Shutdown occurs only after AC is removed
- Shutdown occurs despite verified AC power
- The monitor reboots when moved between power sources

**Expected outcome:** The monitor operates normally during the intended transition between available power sources.

If failure occurs only on battery, continue with battery-focused evaluation rather than assuming a general power-system failure.

### 7. Evaluate the Battery Externally
Check battery status indications and inspect accessible battery areas for poor seating, damage, swelling, contamination, or abnormal heat.

If the design permits battery removal by Clinical Engineering, reseat the battery according to approved procedures. A compatible known-good battery may be used for comparison when available.

Do not use a swollen, leaking, excessively hot, or physically damaged battery.

**Expected outcome:** A properly seated, serviceable battery is recognized and supports stable operation.

If a known-good battery resolves the shutdown condition, replace the failed battery through the approved process and proceed to final verification.

### 8. Check for Movement-Related Shutdown
If shutdown occurs during transport, repositioning, or cable movement, reproduce the condition carefully off-patient.

Check whether the symptom corresponds with:
- Power cord movement
- Battery seating
- Docking or mounting movement
- External connector movement
- Physical vibration

Do not repeatedly stress damaged connectors.

**Expected outcome:** Normal movement does not interrupt power.

If an external loose connection is identified and safely corrected, verify stable operation and troubleshooting can stop.

### 9. Perform Final Functional Verification
After correction, operate the monitor through representative normal conditions. Verify:
- Reliable startup
- Stable AC operation
- Appropriate battery recognition
- Stable operation during normal movement
- Normal display and controls
- Normal alarm functionality
- No unexpected reboot or shutdown

Perform any required electrical safety or return-to-service testing according to facility policy and approved manufacturer documentation.

**Expected outcome:** The monitor remains stable and performs normally under expected operating conditions.

If all checks pass, document the repair and return the monitor to service.

### 10. Escalate an Unresolved Power Failure
If the monitor still will not power on, continues rebooting, or shuts down despite verified AC power, known-good external connections, and an acceptable battery, stop external troubleshooting.

Do not proceed into unapproved internal power-supply, board-level, or component repair.

**Expected outcome:** An unresolved or unsafe monitor is removed from clinical availability and routed for qualified service.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may include an internal power subsystem, battery charging circuitry, internal connection, thermal condition, power-management function, or another service-level fault.

The monitor should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired or configured only by qualified personnel

After repair, complete appropriate functional, alarm, power-source, battery, and electrical safety verification before return to clinical use.

Knowing when to stop external troubleshooting and escalate an unreliable patient monitor is proper troubleshooting.

## Clinical Use Tip

Never leave a patient connected to a monitor that has demonstrated unexplained shutdowns, even if it powers back on normally afterward.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**




## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient first, verify external power and battery conditions before assuming internal failure, reproduce intermittent faults safely, and escalate any monitor that cannot provide dependable operation. Clear CCR documentation should describe exactly what was reported, found, corrected, and verified.

That is successful troubleshooting.
