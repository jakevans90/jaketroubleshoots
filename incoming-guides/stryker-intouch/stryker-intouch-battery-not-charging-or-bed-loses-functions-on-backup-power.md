---
schemaVersion: 1
title: "Stryker InTouch Hospital Bed - Battery Not Charging or Bed Loses Functions on Backup Power"
issueTitle: "Battery Not Charging or Bed Loses Functions on Backup Power"
description: "Troubleshooting charging failure, short backup operation, or lost bed functions caused by AC power, connections, battery condition, settings, or excessive load."
assetType: "Hospital Bed"
manufacturer: "Stryker"
model: "InTouch"
slug: "stryker-intouch-battery-not-charging-or-bed-loses-functions-on-backup-power"
dateAdded: "2026-07-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that the InTouch bed displayed a low battery and lost powered functions immediately after AC power was disconnected."
  cause: "Clinical Engineering found that the battery connection was not fully seated after a recent battery replacement."
  resolution: "Clinical Engineering secured the battery connection, confirmed normal charging indication, tested intended functions on backup power, and completed final functional verification."
helpfulDetails:
  - "AC and battery indicator behavior."
  - "Outlet tested and result."
  - "Power-cord and plug condition."
  - "Length of time connected to AC power."
  - "Functions available or unavailable on battery."
  - "Immediate shutdown or gradual discharge behavior."
  - "Accessible battery condition and connection status."
  - "Known-good battery or approved test result."
  - "Electrical safety test result when applicable."
  - "Final AC and backup-power status."
---

## What This Guide Helps With

Troubleshooting charging failure, short backup operation, or lost bed functions caused by AC power, connections, battery condition, settings, or excessive load.

## Step-by-Step Troubleshooting

### 1. Ensure Patient Safety and Continuity of Care

Do not rely on an InTouch bed with uncertain backup power during transport, emergency movement, or care that requires powered positioning.

Notify clinical staff. Connect the bed to verified AC power when safe. Move the patient to another verified bed if essential positioning, braking, transport, or safety functions cannot be maintained.

**Expected outcome:** Patient care continues without dependence on an unreliable battery system.

### 2. Confirm the Exact Battery-Related Condition

Determine whether:

The bed does not indicate charging while connected to AC power.

The battery indicator remains low after extended connection to AC.

The bed loses all functions when unplugged.

Only selected functions are unavailable on battery.

Backup operation is unusually brief.

The problem occurs after storage, transport, or prolonged disconnection.

Record the indicator behavior before disconnecting or reconnecting power.

**Expected outcome:** The reported condition is reproduced and distinguished from normal differences between AC-powered and battery-powered operation.

### 3. Verify the AC Power Source

Confirm that the bed is connected directly to an appropriate hospital-grade outlet.

Check the outlet using an approved receptacle tester or verified powered device according to facility policy. Avoid unapproved extension cords or adapters. Confirm that the outlet is not controlled by a wall switch or interrupted circuit.

**Expected outcome:** The outlet provides stable power. If restoring outlet power initiates normal charging, continue charging and verify backup operation before stopping.

### 4. Inspect the Power Cord and Plug

Unplug the bed before closely inspecting the power cord.

Check for:

Cuts, crushing, exposed conductors, or damaged insulation.

Bent, loose, discolored, or heat-damaged plug blades.

Evidence of fluid exposure.

Strain or damage where the cord enters the bed.

Improper wrapping or routing that may have stressed the cable.

Remove the bed from service immediately if electrical damage, overheating, arcing, or exposed conductors are present.

**Expected outcome:** The power cord and plug are safe and intact, or the bed is removed from service for repair.

### 5. Confirm AC Power Recognition

Reconnect the bed to a verified outlet and observe the AC and charging indicators.

Allow time for the bed to recognize external power. Confirm that the power cord is fully inserted into any detachable external connection.

**Expected outcome:** The bed recognizes AC power and indicates charging. If it does not, continue troubleshooting without assuming battery failure.

### 6. Inspect Accessible Battery Connections

With the bed removed from clinical use and handled according to approved procedures, inspect only externally accessible battery connections or compartments.

Look for:

Loose accessible connectors.

Corrosion or contamination.

Swelling, cracking, leakage, unusual heat, or odor.

Damaged retention hardware.

Evidence that the battery was recently replaced but not fully connected.

Do not open sealed battery assemblies or perform unauthorized internal disassembly.

**Expected outcome:** Accessible connections are secure and the battery shows no physical hazard. A swollen, leaking, hot, or damaged battery requires immediate removal from service.

### 7. Allow an Appropriate Charging Period

If the bed has been stored or deeply discharged, leave it connected to verified AC power for an appropriate charging period based on approved service documentation.

Do not judge battery condition from only a brief connection to AC power.

**Expected outcome:** The battery status improves and the bed remains functional during a controlled backup-power test. If charging and backup operation are restored, proceed to final verification.

### 8. Test Backup Operation Without a Patient

Remove the bed from patient use before testing battery operation.

Disconnect AC power and verify the functions intended to remain available on backup power. Operate only enough motions to assess performance and avoid unnecessarily discharging the battery.

Observe for:

Immediate shutdown.

Rapid battery-indicator drop.

Weak, slow, or interrupted motion.

Loss of controls or indicators.

Unexpected alarms or resets.

**Expected outcome:** Intended backup functions operate consistently without immediate shutdown or abnormal behavior.

### 9. Compare With a Known-Good Battery When Authorized

When approved by facility procedure and manufacturer documentation, compare performance using a compatible known-good battery or approved battery test method.

Do not substitute batteries with uncertain condition, chemistry, rating, or compatibility.

**Expected outcome:** The test distinguishes a degraded battery from a charging-system or power-distribution problem. Replace only with the correct approved battery.

### 10. Perform Return-to-Service Verification

After correction, reconnect the bed to AC power and confirm:

AC power is recognized.

Charging indication is present.

The battery supports intended backup functions.

Controls and powered motions operate normally.

No electrical damage, odor, heat, or abnormal alarms are present.

Complete required electrical safety and functional testing following battery or power-system repair.

**Expected outcome:** The bed charges normally and performs reliably on both AC and intended backup power. Troubleshooting can stop.

## If the Problem Persists

External power, outlet condition, cord integrity, accessible connections, charging time, and basic battery condition have been evaluated. The remaining cause may involve a depleted battery, charging circuit, power-supply assembly, internal wiring, control system, or approved configuration.

Remove the bed from service, label it Out of Service, and send it for bench evaluation using appropriate Stryker documentation and approved battery and electrical test equipment. Repairs should be completed only by qualified personnel. Verify AC operation, charging, backup operation, and applicable electrical safety requirements before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Do not begin patient transport with a questionable battery, even when the bed operates normally while connected to AC power.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain patient support, verify the outlet and external power path first, evaluate the battery without assuming an internal charging failure, and document the final AC and backup-power performance.

That is successful troubleshooting.
