---
schemaVersion: 1
title: "Smiths Medical Medfusion 3500 Infusion Pump - Infusion Stops Unexpectedly or Pump Reboots During Delivery"
issueTitle: "Infusion Stops Unexpectedly or Pump Reboots During Delivery"
description: "Troubleshoots unexpected infusion interruption or reboot caused by power, battery, connections, loading, environmental conditions, or device malfunction."
assetType: "Infusion Pump"
manufacturer: "Smiths Medical"
model: "Medfusion 3500"
slug: "smiths-medical-medfusion-3500-infusion-stops-unexpectedly-or-pump-reboots-during-delivery"
dateAdded: "2026-09-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that the Medfusion 3500 rebooted unexpectedly while delivering an infusion."
  cause: "Clinical Engineering found an intermittent AC power connection at the external power cord that reproduced with normal handling."
  resolution: "The defective external power component was replaced with an approved replacement, continuous operation and power-transition testing were completed successfully, and the pump was returned to service."
helpfulDetails:
  - "Whether pump stopped, shut down, or rebooted"
  - "Any displayed message"
  - "AC or battery operation when event occurred"
  - "Outlet tested"
  - "Power cord and connector condition"
  - "Battery indication"
  - "Whether programming was retained"
  - "Known-good syringe setup result"
  - "Movement-related behavior"
  - "Functional test results"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots unexpected infusion interruption or reboot caused by power, battery, connections, loading, environmental conditions, or device malfunction.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Restore Therapy
Treat an unexpected pump stop or reboot as an unreliable therapy-delivery condition. Transfer the infusion to another verified pump immediately when interruption could affect the patient.

**Expected outcome:** Required therapy continues safely without dependence on the affected pump.

### 2. Confirm What Actually Occurred
Determine whether the pump powered off, rebooted, stopped infusion while remaining powered, alarmed before stopping, lost programming, or restarted after movement or connection to AC power. Record any displayed message.

**Expected outcome:** The event is accurately characterized instead of being treated as a generic shutdown.

### 3. Inspect AC Power
Check the power cord, external power supply components if applicable, plug, strain relief, and receptacle for looseness or damage. Verify the outlet using an appropriate method.

**Expected outcome:** Reliable external power is available and connections remain secure.

### 4. Check Battery Operation
With the pump safely on the bench, observe battery status and determine whether the event occurs on battery, AC power, or during transition between power sources. Do not rely solely on an icon if the reported problem suggests battery instability.

**Expected outcome:** The pump remains powered appropriately through normal permitted power-source transitions.

### 5. Inspect for Physical or Liquid Damage
Examine the housing and accessible connectors for impact damage, loose components, liquid intrusion, residue, overheating, odor, or other abnormal conditions.

**Expected outcome:** No physical condition requiring immediate removal from service is present.

### 6. Verify Syringe and Fluid-Path Setup
Confirm that the reported stop was not caused by an actual occlusion, syringe-loading condition, plunger problem, or another legitimate infusion alarm.

**Expected outcome:** A normal therapy-related alarm or external setup problem is either identified or ruled out.

### 7. Reproduce the Event With a Known-Good Setup
Using a known-good syringe and controlled bench setup, operate the pump while observing power and infusion status. Do not repeatedly stress a pump exhibiting heat, odor, electrical damage, or other unsafe behavior.

**Expected outcome:** The pump operates continuously without rebooting or stopping, or the failure is reproduced under controlled conditions.

### 8. Check for Movement-Related Interruption
Without abusing connectors or the housing, observe whether normal handling or movement causes power interruption. Inspect accessible power connections for intermittent contact.

**Expected outcome:** Normal movement does not cause a shutdown, reboot, or power-source interruption.

### 9. Perform Functional and Power Verification
Using approved test equipment and procedures, verify basic infusion performance, power operation, battery behavior as applicable, startup, and alarms following the reported event.

**Expected outcome:** The pump remains stable and passes applicable return-to-service checks. If so, troubleshooting can stop.

### 10. Escalate Any Unexplained Reboot or Stop
If the pump reboots, powers off, loses programming, or stops infusion unexpectedly without a verified external cause, remove it from service even if the problem is intermittent.

**Expected outcome:** An intermittently unreliable therapy-delivery device is prevented from returning to patient care.

## If the Problem Persists

External AC power, battery operation, connectors, syringe setup, fluid-path conditions, and obvious physical damage have been evaluated. Remaining possibilities include power-management circuitry, battery-related service conditions, software, internal connections, drive control, or another service-level fault.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel

After corrective action, perform complete applicable power, battery, infusion, alarm, and safety verification before clinical return. Knowing not to return an intermittently rebooting infusion pump to service is proper troubleshooting.

## Clinical Use Tip

An unexplained reboot during infusion should be treated as a significant reliability failure even when the pump powers back up normally afterward.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Whether pump stopped, shut down, or rebooted
- Any displayed message
- AC or battery operation when event occurred
- Outlet tested
- Power cord and connector condition
- Battery indication
- Whether programming was retained
- Known-good syringe setup result
- Movement-related behavior
- Functional test results
- Final device status

## Final Thought

Unexpected interruption demands careful separation of external power, battery, setup, and true device failure. Verify the simple causes first, but escalate any unexplained recurrence before the pump returns to patient care.

That is successful troubleshooting.
