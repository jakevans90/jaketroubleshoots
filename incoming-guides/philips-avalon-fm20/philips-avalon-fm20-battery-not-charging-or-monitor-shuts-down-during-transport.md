---
schemaVersion: 1
title: "Philips Avalon FM20 Fetal Monitor - Battery Not Charging or Monitor Shuts Down During Transport"
issueTitle: "Battery Not Charging or Monitor Shuts Down During Transport"
description: "Troubleshoots charging failure or transport shutdown caused by AC power, charging connection, battery condition, seating, or external power problems."
assetType: "Fetal Monitor"
manufacturer: "Philips"
model: "Avalon FM20"
slug: "philips-avalon-fm20-battery-not-charging-or-monitor-shuts-down-during-transport"
dateAdded: "2026-09-08"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the Avalon FM20 powered off shortly after being disconnected from AC power for transport."
  cause: "Clinical Engineering found that the installed battery would not sustain operation, while a known-good compatible battery operated normally."
  resolution: "Replaced the defective battery and verified charging, battery operation, AC-to-battery transition, and normal monitor function."
helpfulDetails:
  - "AC versus battery behavior"
  - "Outlet test result"
  - "Power-cord condition"
  - "Charging indication"
  - "Battery physical condition"
  - "Known-good battery result"
  - "Whether shutdown occurred immediately or after transport"
  - "Power-transition test result"
  - "Final functional verification"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots charging failure or transport shutdown caused by AC power, charging connection, battery condition, seating, or external power problems.

## Step-by-Step Troubleshooting
### 1. Protect the Patient Before Testing
Do not troubleshoot transport power while the monitor is the sole device providing required fetal or maternal monitoring. Transfer monitoring to another verified device before intentionally disconnecting AC power.

Expected outcome: Patient monitoring remains uninterrupted while battery performance is evaluated.

### 2. Confirm the Reported Power Problem
Determine whether the battery does not charge, shows an unexpected status indication, has very short runtime, or causes the monitor to shut down immediately or intermittently when AC power is removed.

Expected outcome: The charging and runtime complaint is clearly defined.

### 3. Verify the AC Power Source
Confirm the outlet or approved power source is functioning using an appropriate tester or known-good device. Inspect the power cord and plug for damage and confirm the monitor recognizes AC operation.

Expected outcome: A reliable AC source reaches the monitor.

### 4. Inspect the Power Cord and External Connections
Check the line cord, connector, strain relief, and accessible inlet area for cuts, looseness, contamination, heat damage, or intermittent connection.

Expected outcome: External power connections are secure and undamaged.

### 5. Observe Charging Status
With the monitor connected to verified AC power, observe the available battery and charging indicators. Allow sufficient time to determine whether the battery status changes normally without assuming a failed battery immediately.

Expected outcome: The monitor indicates that external power is present and the battery is charging as expected.

### 6. Inspect and Reseat the Battery if User-Accessible
If battery removal is permitted for Clinical Engineering under approved procedures, inspect it for swelling, leakage, cracked housing, damaged contacts, or contamination and reseat it securely. Do not use a physically damaged battery.

Expected outcome: The battery is correctly installed and free from visible defects.

### 7. Compare With a Known-Good Compatible Battery
When permitted, install a known-good compatible battery and repeat charging and transport-power checks.

Expected outcome: Normal operation with the known-good battery isolates the original battery as the likely cause. Replace the defective battery according to facility procedure.

### 8. Check for Intermittent Power Transfer
With the monitor off-patient and under controlled testing, verify that it remains operating when transferred between verified AC and battery power. Do not repeatedly cycle power on equipment being used clinically.

Expected outcome: Power transitions occur without restart or shutdown.

### 9. Perform Battery and Functional Verification
Use approved battery testing procedures or manufacturer-supported diagnostics available to qualified personnel. Verify appropriate charging behavior, battery operation, power transition, startup, alarms, and normal monitoring functions.

Expected outcome: The unit remains stable during expected transport operation. If successful, troubleshooting can stop.

### 10. Escalate Persistent Charging or Shutdown Problems
If a known-good battery will not charge or the monitor still shuts down during power transitions, remove it from service.

Expected outcome: A monitor with unreliable transport power is labeled Out of Service and sent for bench evaluation.

## If the Problem Persists
Outlet, power cord, battery seating, and the replaceable battery have been evaluated. Persistent failure may involve the charging system, power-management circuitry, battery interface, or another internal service-level problem.

Remove the monitor from service, label it Out of Service, and send it for repair or bench evaluation using appropriate Philips documentation and approved test equipment. Internal repair should be performed only by qualified personnel.

After repair, verify AC operation, battery charging, transport operation, power transitions, alarms, and complete monitor functionality before return to service. Knowing when external battery troubleshooting has reached its limit is proper troubleshooting.

## Clinical Use Tip
Confirm adequate battery operation before transport rather than discovering a power problem after the patient leaves an AC-powered care area.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought
Verify the external power path and battery before assuming an internal charging failure, protect monitoring continuity during testing, and document the final transport-power verification.

That is successful troubleshooting.
