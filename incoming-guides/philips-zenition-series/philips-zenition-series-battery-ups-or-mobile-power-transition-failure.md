---
schemaVersion: 1
title: "Philips Zenition Series C-Arm - Battery, UPS, or Mobile Power Transition Failure"
issueTitle: "Battery, UPS, or Mobile Power Transition Failure"
description: "Addresses abnormal mobile-power behavior caused by AC supply, charging conditions, power connections, battery condition, UPS status, or transition-related faults."
assetType: "C-Arm"
manufacturer: "Philips"
model: "Zenition Series"
slug: "philips-zenition-series-battery-ups-or-mobile-power-transition-failure"
dateAdded: "2026-08-22"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that the Philips Zenition Series shut down when disconnected from AC power for transport."
  cause: "Clinical Engineering found that the system had not been charging because its external AC connector was not fully seated."
  resolution: "The connector was secured, normal charging status was confirmed, and stable AC-to-mobile-power transition and system operation were verified before return to service."
helpfulDetails:
  - "Exact battery or UPS complaint."
  - "Whether shutdown occurs when AC is removed."
  - "AC receptacle verification."
  - "Power-cord and connector condition."
  - "Charging indication."
  - "Battery or UPS status shown to the user."
  - "Whether the unit was recently stored or transported."
  - "External accessories connected."
  - "Behavior during AC-to-mobile and mobile-to-AC transitions."
  - "Unexpected restart or shutdown behavior."
  - "Results after appropriate charging."
  - "Final transition and functional status."
---
## What This Guide Helps With

Addresses abnormal mobile-power behavior caused by AC supply, charging conditions, power connections, battery condition, UPS status, or transition-related faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Avoid Unplanned Power Loss

Do not rely on a Zenition Series system with unstable mobile power during an active procedure. Connect to a verified AC source when safe, or exchange the system for another verified C-arm if dependable operation cannot be assured.

Determine whether the complaint is failure to charge, shutdown when unplugged, unexpected restart during transition, short mobile runtime, or UPS-related warning behavior.

**Expected outcome:** Clinical imaging is not dependent on unreliable battery or UPS operation, and the reported power condition is clearly defined.

### 2. Inspect for Electrical Damage

Inspect power cords, plugs, connectors, accessible charging connections, and system exterior for damage, overheating, liquid intrusion, discoloration, unusual odor, or loose components.

Do not continue powering equipment that shows evidence of electrical damage.

**Expected outcome:** No external electrical condition requires immediate removal from service.

If damage, heat, odor, or liquid intrusion is present, remove the system from service and escalate.

### 3. Verify the Facility AC Source

Connect the unit to its intended verified AC receptacle. Confirm the receptacle provides power using an approved method and that no switched outlet, failed power strip, or damaged facility connection is involved.

**Expected outcome:** Stable facility AC power is available to the system.

If correcting the AC source restores normal charging and operation, continue to final verification.

### 4. Verify External Power Connections

Confirm all applicable external power cords and connectors are fully seated and undamaged. Check for connectors that may have loosened during transport.

**Expected outcome:** The system receives uninterrupted AC power through intact external connections.

If securing a connection restores normal charging or power transition, proceed to final verification.

### 5. Observe Normal Charging or Power Status Indications

With the system connected to verified AC power, observe normal user-accessible battery, charging, or UPS indications. Allow the system to reach a stable state before interpreting status.

Do not infer battery health solely from a single momentary indication.

**Expected outcome:** The system recognizes AC input and indicates the expected charging or powered state.

### 6. Confirm the Complaint Under Controlled Conditions

With no patient relying on the equipment, reproduce the reported transition only if normal operating procedures permit. Observe what happens when moving between the verified AC-powered and intended mobile-power states.

Stop immediately if the system shuts down unexpectedly, repeatedly restarts, or produces unsafe behavior.

**Expected outcome:** The transition occurs normally or the failure is safely reproduced and documented.

### 7. Check for External Loads or Accessories

Disconnect nonessential externally powered accessories when safe and retest. Ensure no unsupported device is drawing power from the system or connected in a way that alters normal power operation.

**Expected outcome:** Nonessential external equipment is ruled out as a contributor to the power-transition complaint.

### 8. Allow Appropriate Recharge Before Retesting Runtime

If the system has recently been stored, transported, or left disconnected from AC, allow it to charge according to the approved manufacturer workflow before judging runtime.

Do not invent or substitute an arbitrary charging interval.

**Expected outcome:** Battery or UPS performance is evaluated only after the system has had an appropriate opportunity to charge.

### 9. Compare With Known-Good Operation

When available, compare user-accessible power indications and transition behavior with another equivalent Zenition system. Do not swap internal batteries or UPS components unless specifically permitted by approved service procedures.

**Expected outcome:** The reported behavior is confirmed as abnormal rather than a normal operating characteristic.

### 10. Perform Final Functional Verification

Verify stable operation on AC, expected transition to the intended mobile-power state, return to AC operation, charging indication, startup stability, and normal system functions following the transition.

Perform only the runtime or battery testing required by approved Philips or facility procedures.

**Expected outcome:** Power remains stable throughout permitted transitions without unexpected shutdown, restart, or loss of system function.

If all tests pass, troubleshooting can stop and the device may be returned to service.

### 11. Escalate Persistent Battery or UPS Failure

If the unit will not charge, shuts down during a normal transition, repeatedly restarts, or cannot provide dependable mobile power after external AC and connection issues are ruled out, stop troubleshooting.

**Expected outcome:** The device is withheld from clinical use requiring mobile-power capability until evaluated by qualified service personnel.

## If the Problem Persists

Common external AC supply, cable, connector, accessory, and charging-condition causes have been ruled out. The remaining problem may involve the battery subsystem, UPS, charging circuitry, power-management subsystem, configuration, or another internal service-level condition.

The Philips Zenition Series should be:

- Removed from service when dependable power cannot be assured.
- Labeled Out of Service.
- Sent for repair or qualified bench/service evaluation.
- Evaluated using approved Philips documentation and appropriate test equipment.
- Repaired, configured, or have internal power components replaced only by qualified personnel.

Do not open battery or UPS assemblies or attempt board-level power repair. Following corrective action, complete required electrical-safety, charging, transition, runtime, startup, and functional return-to-service testing.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not begin a procedure that depends on mobile operation unless the C-arm's required power state and transition behavior have been verified.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Mobile-power problems should be evaluated with patient safety first and stable AC power confirmed before suspecting internal batteries or charging systems. Verify external connections and controlled transitions, then escalate unreliable power performance with complete CCR documentation.

That is successful troubleshooting.

