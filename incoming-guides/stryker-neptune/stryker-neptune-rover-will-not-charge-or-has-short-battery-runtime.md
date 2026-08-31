---
schemaVersion: 1
title: "Stryker Neptune Surgical Fluid Management System - Rover Will Not Charge or Has Short Battery Runtime"
issueTitle: "Rover Will Not Charge or Has Short Battery Runtime"
description: "Use when the Neptune battery does not appear to charge, loses charge unusually quickly, or cannot reliably support normal mobile operation."
assetType: "Surgical Fluid Management System"
manufacturer: "Stryker"
model: "Neptune"
slug: "stryker-neptune-rover-will-not-charge-or-has-short-battery-runtime"
dateAdded: "2026-08-31"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that the Neptune battery discharged quickly and the rover would not remain powered during transport."
  cause: "Clinical Engineering found the unit had been connected to a receptacle that was not supplying AC power, and the battery had not been charging."
  resolution: "Connected the rover to a verified powered receptacle, confirmed normal charging and subsequent battery operation, and returned the unit to service after functional verification."
helpfulDetails:
  - "Battery status at arrival"
  - "AC or battery operating condition"
  - "Outlet verification result"
  - "Power cord condition"
  - "AC/charging indicator behavior"
  - "Whether the unit shut down when unplugged"
  - "Charging response"
  - "Controlled battery test result"
  - "Any recent storage or heavy mobile use"
  - "Final device status"
---
## What This Guide Helps With

Use when the Neptune battery does not appear to charge, loses charge unusually quickly, or cannot reliably support normal mobile operation.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow

Do not rely on a Neptune with uncertain battery runtime when loss of power could interrupt suction or another required clinical function.

Use AC power or another verified device as appropriate while evaluating the rover.

**Expected outcome:** Clinical care is not dependent on an unreliable battery.

### 2. Confirm the Battery Complaint

Determine whether the battery:

- Does not indicate charging
- Charges only intermittently
- Appears charged but discharges quickly
- Causes shutdown when AC power is removed

Record the battery indicator condition before testing.

**Expected outcome:** The battery problem is clearly characterized.

### 3. Verify the AC Power Source

Connect the Neptune to a known-good properly grounded receptacle.

If needed, verify the receptacle using approved electrical test methods or compare with another known-good load.

**Expected outcome:** Reliable AC power is available to the Neptune. If charging begins normally after changing outlets, troubleshoot the original facility outlet separately and verify the rover.

### 4. Inspect the Power Cord and Connection

Inspect the accessible power cord, plug, strain relief, and equipment connection for:

- Cuts
- Fraying
- Bent or damaged blades
- Loose fit
- Discoloration
- Heat damage
- Fluid contamination

Remove the unit from service immediately if unsafe electrical damage is found.

**Expected outcome:** The AC connection is secure and free of visible damage.

### 5. Confirm the Unit Recognizes AC Power

With the Neptune connected to known-good AC, verify that the normal external AC or charging indication is present.

Reseat a detachable approved power cord when applicable.

**Expected outcome:** The rover recognizes AC input and indicates the expected charging state. If it does not recognize verified AC power, escalation may be required.

### 6. Allow Normal Charging and Reassess Status

Leave the unit connected to AC under normal charging conditions and observe whether battery status progresses appropriately.

Do not assume battery failure based on a single low-charge indication immediately after extended use.

**Expected outcome:** Battery status improves while connected to verified AC power.

### 7. Evaluate Battery Runtime Functionally

After an appropriate charge period, disconnect AC power in a controlled nonclinical environment and observe whether the Neptune remains powered normally.

Do not perform runtime testing while the unit is needed for patient care.

**Expected outcome:** The rover remains operational on battery without immediate low-battery behavior or unexpected shutdown.

### 8. Check for Environmental or Usage Factors

Determine whether the reported short runtime followed extended mobile use, prolonged storage without charging, repeated incomplete charging, or unusually frequent transport.

Confirm ventilation openings are unobstructed and the unit is not being stored in an inappropriate environment.

**Expected outcome:** No external usage or environmental condition explains the shortened runtime.

### 9. Perform Final Power Verification

Verify stable operation on AC and controlled transition to battery operation. Confirm that power indicators behave consistently and that the unit does not reset during the transition.

**Expected outcome:** AC operation, charging indication, and battery operation are stable. Troubleshooting can stop if performance is normal.

### 10. Escalate Persistent Charging or Runtime Problems

If verified AC power reaches the unit but charging remains abnormal, runtime is consistently poor, or the Neptune shuts down unexpectedly on battery, stop troubleshooting.

**Expected outcome:** The rover is removed from service for battery, charging-system, or power-system evaluation.

## If the Problem Persists

Common external causes such as a failed outlet, damaged cord, loose power connection, insufficient charging opportunity, and environmental factors have been ruled out.

The remaining issue may involve the battery, charging circuitry, internal power distribution, battery monitoring, internal connections, or another service-level condition.

The device should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate Stryker documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Following battery or charging repair, perform appropriate electrical safety and functional testing before returning the rover to clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not send a Neptune into a procedure on battery power when its runtime has not been verified after a charging complaint.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter; optional explanatory prose may follow. -->



## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Verify the power source, cord, charging indication, and controlled battery operation before condemning the battery. A rover with unreliable battery performance should be removed from service, evaluated appropriately, and documented with clear before-and-after results.

That is successful troubleshooting.
