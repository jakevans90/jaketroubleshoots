---
schemaVersion: 1
title: "Drager Evita XL Ventilator - Internal Battery Will Not Charge or Hold the Ventilator During AC Loss"
issueTitle: "Internal Battery Will Not Charge or Hold the Ventilator During AC Loss"
description: "Troubleshoot battery charging or backup-power failures caused by AC supply, connections, charging conditions, battery condition, or service-level power-system problems."
assetType: "Ventilator"
manufacturer: "Drager"
model: "Evita XL"
slug: "drager-evita-xl-internal-battery-will-not-charge-or-hold-the-ventilator-during-ac-loss"
dateAdded: "2026-11-06"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the Evita XL shut down when AC power was removed during a pre-use check."
  cause: "Clinical Engineering verified normal AC power and found that the installed battery could not support the approved backup-power test."
  resolution: "The battery was replaced under approved procedures, charging and AC-loss switchover passed, and the ventilator completed functional verification."
helpfulDetails:
  - "Battery status indication"
  - "AC recognition status"
  - "Outlet test result"
  - "Power cord condition"
  - "Battery physical condition"
  - "Charging behavior"
  - "AC-loss switchover result"
  - "Known-good battery substitution"
  - "Final battery test result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoot battery charging or backup-power failures caused by AC supply, connections, charging conditions, battery condition, or service-level power-system problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Avoid an Unverified Power Transfer

Do not intentionally remove AC power from a ventilator supporting a patient when battery operation is uncertain.

Move the patient to another verified ventilator before testing backup-power performance.

**Expected outcome:** The patient is safely ventilated by an independent verified source and the Evita XL can be tested without clinical risk.

### 2. Confirm the Reported Battery Problem

Determine whether the battery fails to charge, is not recognized, shows abnormal status, immediately loses power after AC removal, or provides unexpectedly short backup operation.

Document the battery indication before changing anything.

**Expected outcome:** The specific charging or switchover failure is identified and reproducible.

### 3. Verify AC Power at the Source

Check the power cord, plug, outlet, and any approved intermediate power connection. Test the outlet using an appropriate method and confirm the ventilator recognizes AC power.

**Expected outcome:** Reliable AC power is present and the ventilator indicates external power appropriately. If restoring AC power begins normal charging and subsequent battery testing passes, troubleshooting can stop.

### 4. Inspect Accessible Power and Battery Connections

Inspect accessible battery or power connections permitted during normal maintenance. Look for loose connections, damaged housings, corrosion, swelling, contamination, or other visible defects.

Do not open or repair battery packs.

**Expected outcome:** Battery-related external connections are secure and there is no physical battery damage. Any swollen, leaking, overheated, or physically damaged battery requires immediate removal from service.

### 5. Allow an Appropriate Charging Opportunity

If the ventilator has recently been stored or disconnected from AC, place it on verified AC power and allow charging in accordance with facility and manufacturer procedures.

Do not judge battery condition from a brief charging interval alone.

**Expected outcome:** Battery status progresses normally toward a charged state. If charging resumes and the subsequent backup test passes, troubleshooting can stop.

### 6. Perform a Controlled AC-Loss Test

With the ventilator off the patient and connected to a test lung, verify stable operation on AC. Then perform the approved power-switchover test while monitoring ventilation, display, alarms, and battery status.

**Expected outcome:** The ventilator transfers to battery operation without an unexpected shutdown or loss of ventilation. If successful, continue to battery-performance verification.

### 7. Evaluate Battery Performance

Use the appropriate approved procedure to assess whether the battery can support the expected verification test.

Do not invent or apply an arbitrary runtime requirement; use the current manufacturer documentation and facility criteria for the installed battery configuration.

**Expected outcome:** The battery meets the applicable performance criteria. If it does, troubleshooting can stop following final documentation.

### 8. Substitute an Approved Known-Good Battery When Appropriate

If the battery is externally serviceable by Clinical Engineering under approved procedures, install a known-good approved battery and repeat charging and switchover testing.

**Expected outcome:** Normal operation with a known-good battery identifies the original battery as defective. Replace it according to approved procedures and complete return-to-service testing.

### 9. Escalate a Persistent Charging or Switchover Failure

If known-good AC power and an approved known-good battery do not resolve the problem, stop external troubleshooting.

The fault may involve internal charging circuitry, power distribution, battery monitoring, or another service-level power component.

**Expected outcome:** The ventilator is removed from service and routed for qualified repair.

## If the Problem Persists

External AC supply, power cord condition, battery connection, charging opportunity, and battery condition have been evaluated.

Remove the Evita XL from service, label it **Out of Service**, and send it for repair or bench evaluation using appropriate Drager documentation and approved electrical test equipment. Internal charging or power-distribution repair should be performed only by qualified personnel.

After repair, verify AC operation, battery charging, AC-to-battery switchover, ventilation continuity, power alarms, and all required return-to-service functions.

## Clinical Use Tip

Never test battery backup by unplugging a ventilator that is supporting a patient unless continuity of ventilation is already independently protected.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Verify safe alternate ventilation first, confirm the external AC source and battery condition, test switchover only under controlled conditions, and escalate power-system faults that remain after a known-good battery is evaluated.

That is successful troubleshooting.
