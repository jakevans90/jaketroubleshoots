---
schemaVersion: 1
title: "GE Healthcare Carestation 750 Anesthesia Machine - System Checkout or Leak Test Failure"
issueTitle: "System Checkout or Leak Test Failure"
description: "Checkout or leak testing fails due to circuit connections, breathing-system assembly, accessories, seals, gas supplies, or other external causes."
assetType: "Anesthesia Machine"
manufacturer: "GE Healthcare"
model: "Carestation 750"
slug: "ge-healthcare-carestation-750-system-checkout-or-leak-test-failure"
dateAdded: "2026-08-13"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that the Carestation 750 repeatedly failed the system checkout during leak testing."
  cause: "Clinical Engineering found a loose patient breathing-circuit connection that created an external circuit leak."
  resolution: "The connection was properly seated, the complete system checkout was repeated successfully, and the machine passed final functional verification."
helpfulDetails:
  - "Exact checkout step or displayed message"
  - "Whether the failure is repeatable"
  - "AC power status"
  - "Pipeline and cylinder status"
  - "Breathing-circuit condition"
  - "Reservoir-bag condition"
  - "Consumables and accessories installed"
  - "Known-good circuit substitution results"
  - "Leak-test result before and after correction"
  - "Final checkout status"
  - "Final device disposition"
---

## What This Guide Helps With
Checkout or leak testing fails due to circuit connections, breathing-system assembly, accessories, seals, gas supplies, or other external causes.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Anesthesia Capability
Do not troubleshoot a failed checkout or leak condition while a patient depends on the anesthesia machine. If the issue occurs during clinical use, transition the patient to an appropriate verified anesthesia or ventilation method according to facility procedure.

Remove the Carestation 750 from clinical use until the source of the failure is identified and required testing is successfully completed.

**Expected outcome:** The patient is supported independently of the affected machine and the unit is available for controlled troubleshooting.

### 2. Confirm the Exact Checkout Failure
Repeat only the appropriate operator-accessible checkout or leak test and record where the sequence fails and any displayed message.

Determine whether the failure consistently occurs at the same stage or appeared only once.

**Expected outcome:** The reported failure is reproduced and the affected portion of checkout is identified. If checkout completes normally and repeated verification is successful, troubleshooting can stop.

### 3. Verify Basic Power and Gas Availability
Confirm the machine is properly connected to AC power and operating normally. Check external oxygen, air, and other configured pipeline connections for proper attachment.

Inspect hoses for loose fittings, visible damage, severe kinks, or incorrect connections. If cylinders are part of the configured backup supply, confirm they are properly installed and available.

**Expected outcome:** Required power and gas sources are connected and no obvious supply issue is present. Correcting a loose or unavailable external supply that allows checkout to pass resolves the problem.

### 4. Inspect the Patient Breathing Circuit
Check the breathing circuit from the machine connection through the patient connection. Look for:

- Loose or partially seated hoses
- Cracked tubing
- Open sampling or auxiliary ports
- Missing caps
- Incorrect circuit assembly
- Damaged connectors
- Unintended open branches

Reseat all accessible connections.

**Expected outcome:** The breathing circuit is complete, intact, and securely connected. If correcting the circuit allows the leak test and checkout to pass, troubleshooting can stop.

### 5. Inspect the Breathing System Assembly and Consumables
Verify externally removable breathing-system components are properly installed and fully seated. Inspect accessible seals, canister connections, bags, filters, water traps, and other installed consumables for incorrect installation or visible damage.

Do not disassemble internal pneumatic assemblies beyond normal approved user-removable components.

**Expected outcome:** All breathing-system components and consumables are properly installed without visible defects. A corrected assembly that restores successful checkout resolves the issue.

### 6. Check the Reservoir Bag and Adjustable Components
Confirm the reservoir bag is intact and correctly attached. Check that externally adjustable breathing-system controls are positioned appropriately for the checkout being performed.

Inspect for sticking, obvious contamination, or a loose connection without attempting internal repair.

**Expected outcome:** The bag and accessible breathing-system controls are intact and positioned appropriately. If correction results in a successful test, troubleshooting can stop.

### 7. Check Installed Accessories and Sampling Connections
Inspect gas-sampling tubing, airway adapters, filters, humidification accessories, and any other components that open into or interact with the breathing circuit.

Temporarily replace a questionable disposable accessory with a compatible known-good item when appropriate.

**Expected outcome:** Accessories are intact, compatible, and not creating an unintended leak or obstruction. Successful checkout after replacing an accessory confirms the external cause.

### 8. Perform a Controlled Known-Good Circuit Comparison
If the leak remains, install a compatible known-good breathing circuit and required disposable components.

Repeat the checkout or leak test without changing unrelated configuration.

**Expected outcome:** If the test passes with the known-good circuit, the removed circuit or accessory set is the likely cause and can be replaced. If the failure remains, continue troubleshooting.

### 9. Repeat Complete Checkout
After any correction, restore the machine to its intended clinical configuration and perform the complete required checkout.

Verify ventilation, gas delivery, monitoring, alarms, and leak testing as applicable before return to service.

**Expected outcome:** The Carestation 750 completes checkout without the original failure. If it does, troubleshooting is complete.

### 10. Escalate an Unresolved Checkout Failure
If checkout or leak testing continues to fail after external circuits, connections, supplies, consumables, and accessible assemblies have been verified, stop external troubleshooting.

**Expected outcome:** The machine remains unavailable for clinical use and is routed for qualified service evaluation.

## If the Problem Persists
Common external causes have been ruled out. The remaining problem may involve an internal pneumatic leak, valve or flow-control problem, sensor issue, breathing-system interface, configuration problem, or another service-level condition.

The Carestation 750 should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired or configured only by qualified personnel

After repair, complete the required functional, leak, alarm, ventilation, gas-delivery, and return-to-service testing before clinical use.

Knowing when to stop external troubleshooting and escalate a persistent checkout failure is proper troubleshooting.

## Clinical Use Tip
Never place an anesthesia machine into service after bypassing or accepting an unresolved checkout or leak-test failure.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Protect the patient first, then work from external circuits, gas supplies, connections, accessories, and assembly toward more involved causes. Verify successful checkout before assuming an internal failure or returning the machine to service, and document the complaint, confirmed cause, corrective action, and final test result clearly.

That is successful troubleshooting.
