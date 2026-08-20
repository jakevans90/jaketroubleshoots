---
schemaVersion: 1
title: "GE Healthcare OEC Elite C-Arm - Battery, UPS, or Mobile Power Transition Failure"
issueTitle: "Battery, UPS, or Mobile Power Transition Failure"
description: "Troubleshoots loss of power during mobile transition caused by AC supply, charging, battery condition, connections, or external power-system problems."
assetType: "C-Arm"
manufacturer: "GE Healthcare"
model: "OEC Elite"
slug: "ge-healthcare-oec-elite-battery-ups-or-mobile-power-transition-failure"
dateAdded: "2026-08-20"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the OEC Elite workstation shut down immediately when AC power was disconnected for transport."
  cause: "Clinical Engineering found an accessible UPS power connection was not fully seated."
  resolution: "The connection was secured and controlled AC-to-mobile and mobile-to-AC transition testing confirmed uninterrupted operation."
helpfulDetails:
  - "Behavior when AC was disconnected"
  - "AC operation status"
  - "Charging indication"
  - "Power-cord condition"
  - "UPS or battery indication"
  - "External power connections"
  - "Accessories connected"
  - "Approximate observed runtime"
  - "AC-to-mobile test result"
  - "Mobile-to-AC test result"
  - "Unusual heat, odor, or damage"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots loss of power during mobile transition caused by AC supply, charging, battery condition, connections, or external power-system problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Imaging Availability
If the OEC Elite loses power or becomes unstable when disconnected from AC during a procedure, connect to a verified power source when safe or provide another imaging system. Do not rely on uncertain battery or UPS operation for patient care.

**Expected outcome:** Clinical imaging continues using a stable power source.

### 2. Confirm the Exact Power-Transition Complaint
Determine whether the system shuts down immediately when unplugged, lasts only briefly, fails to transfer back to AC, does not charge, or shows intermittent power loss while being moved.

**Expected outcome:** The failure is characterized as charging, runtime, transfer, or general power instability.

### 3. Verify AC Power Operation
Connect the system to a verified facility outlet and confirm normal startup and operation. Inspect the power cord and plug for damage, overheating, or strain.

**Expected outcome:** The system operates normally from AC. If it does not, troubleshoot the broader power problem before evaluating battery transition.

### 4. Verify Charging Indication
With the unit connected to AC, observe available user-level battery or charging indications. Allow sufficient normal charging opportunity according to facility and manufacturer practices before evaluating runtime.

**Expected outcome:** The system recognizes AC input and indicates expected charging behavior.

### 5. Inspect External Power Connections
Check accessible power connections associated with the workstation, monitor cart, UPS, and mobile power path. Look for loose connectors, damaged cables, or partially seated plugs.

**Expected outcome:** All accessible mobile-power connections are secure and undamaged.

### 6. Check for Power-Related Accessories or Loads
Confirm that optional external equipment is not incorrectly connected to or overloading a mobile power source. Remove nonessential accessories when safe and repeat the transition test.

**Expected outcome:** The system transitions normally with its required configuration.

### 7. Test AC-to-Mobile Transition Without a Patient
After confirming the system is adequately charged and stable on AC, perform an approved non-patient transition test by disconnecting facility power as permitted by service procedures.

**Expected outcome:** Required components remain powered and operational through the transition. If they do, proceed to return-to-AC testing.

### 8. Test Mobile-to-AC Transition
Reconnect the system to verified facility power and observe whether AC operation and charging resume normally.

**Expected outcome:** The system returns to external power without interruption or abnormal behavior.

### 9. Evaluate Repeatability
Repeat only the approved functional transition checks necessary to establish reliability. Do not repeatedly deep-discharge the system merely to reproduce the complaint.

**Expected outcome:** Mobile power transition is stable and repeatable. Troubleshooting can stop after required final verification.

### 10. Escalate Short Runtime or Failed Transition
If the system cannot maintain power, unexpectedly shuts down, fails to charge, produces unusual heat or odor, or behaves inconsistently during transition, discontinue mobile operation.

**Expected outcome:** An unreliable power system is removed from clinical use pending qualified service evaluation.

## If the Problem Persists
External AC supply, charging status, power connections, accessories, and controlled transition behavior have been checked. Remaining possibilities may involve battery degradation, UPS components, charging circuitry, internal power distribution, power-control electronics, or another service-level fault.

Remove the OEC Elite from service, label it **Out of Service**, and send it for repair or bench evaluation. Use appropriate GE Healthcare documentation and approved electrical-safety and battery test equipment. Batteries or UPS components should be tested, repaired, or replaced only by qualified personnel using approved parts and procedures.

Before return to service, verify stable AC operation, charging, required mobile runtime behavior, transition in both directions, and applicable electrical-safety and functional tests. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
A mobile imaging system that unexpectedly shuts down when unplugged should remain on verified AC power only long enough to safely remove it from clinical dependency.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Maintain stable power for patient care, verify AC input, charging, connections, and controlled transition behavior before assuming battery failure, and never return a system with intermittent mobile power to service. Escalate appropriately and document both the cause and final transition verification.

That is successful troubleshooting.
