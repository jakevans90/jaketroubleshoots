---
schemaVersion: 1
title: "Advanced Sterilization Products (ASP) STERRAD NX Sterilizer - Cassette Is Rejected, Will Not Index, or Reports No Cycles Remaining"
issueTitle: "Cassette Is Rejected, Will Not Index, or Reports No Cycles Remaining"
description: "Troubleshoot cassette rejection, indexing problems, recognition failures, or cycle-availability messages caused by cassette condition, installation, consumables, or system readiness."
assetType: "Sterilizer"
manufacturer: "Advanced Sterilization Products (ASP)"
model: "STERRAD NX"
slug: "advanced-sterilization-products-asp-sterrad-nx-cassette-is-rejected-will-not-index-or-reports-no-cycles-remaining"
dateAdded: "2026-11-17"
taxonomyMode: "reuse"
ccr:
  complaint: "Sterile Processing reported that the STERRAD NX repeatedly rejected the installed sterilant cassette and would not proceed to cycle setup."
  cause: "Clinical Engineering found the installed cassette was not recognized, while a known-good approved cassette was accepted and indexed normally."
  resolution: "Removed the suspect cassette from use, installed a known-good cassette, verified normal cassette recognition and cycle setup, and returned the sterilizer to service after required checks."
helpfulDetails:
  - "Exact cassette-related message"
  - "Cassette condition"
  - "Cassette status or remaining-use indication"
  - "Whether cassette was newly installed"
  - "Results with a known-good cassette"
  - "Cassette-loading-area condition"
  - "Whether indexing occurred"
  - "Restart results"
  - "Final functional verification"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoot cassette rejection, indexing problems, recognition failures, or cycle-availability messages caused by cassette condition, installation, consumables, or system readiness.

## Step-by-Step Troubleshooting

### 1. Protect Sterile Processing Workflow

Do not rely on a STERRAD NX that cannot reliably recognize or advance the sterilant cassette. Redirect loads to another validated sterilization process or verified sterilizer according to facility procedures.

Do not repeatedly attempt processing of instruments while cassette status is uncertain.

**Expected outcome:** Required instrument processing continues using verified equipment while the affected sterilizer is evaluated.

### 2. Confirm the Exact Cassette Complaint

Record the displayed message and determine whether the cassette:

- Is rejected immediately
- Is accepted but will not index
- Indicates no usable cycles remain
- Becomes unavailable during cycle setup
- Was functioning normally before the current event

Do not assume the cassette or sterilizer has failed based only on a general report such as "cassette problem."

**Expected outcome:** The failure point and displayed condition are clearly identified.

### 3. Inspect the Cassette Externally

Using appropriate PPE and facility procedures for handling the sterilant cassette, inspect it for:

- Physical damage
- Leakage or contamination
- Distortion
- Improper storage or handling
- Obvious signs that it should not be used

Do not attempt to open, modify, refill, or repair the cassette.

**Expected outcome:** The cassette is intact and suitable for installation. If damaged or leaking, remove it from use and stop troubleshooting with that cassette.

### 4. Verify Correct Cassette Installation

Remove and reinstall the cassette only according to approved operating procedures. Confirm it is fully seated in the intended orientation and that nothing externally obstructs its insertion or movement.

Do not force the cassette or cassette mechanism.

**Expected outcome:** The cassette installs normally without binding or excessive force.

### 5. Check Cassette Status and Consumable Availability

Verify that the installed cassette is appropriate for the STERRAD NX and has remaining usable capacity according to the system indication and facility inventory controls.

If the system correctly identifies an exhausted cassette, replace it with an approved cassette.

**Expected outcome:** A usable cassette is installed and recognized with available processing capacity. If normal operation returns, troubleshooting can stop after verification.

### 6. Test With a Known-Good Approved Cassette

When permitted by facility procedures, substitute another properly stored, undamaged, approved cassette.

Do not repeatedly sacrifice consumables if multiple known-good cassettes are rejected.

**Expected outcome:** A known-good cassette is recognized and indexes normally. If it does, remove the original cassette from use and document the finding.

### 7. Inspect the Accessible Cassette Loading Area

With the sterilizer idle and safe to inspect, check the externally accessible cassette-loading area for:

- Packaging debris
- Obvious obstruction
- Damage
- Contamination
- Misalignment visible without disassembly

Do not reach into inaccessible mechanisms or defeat covers or interlocks.

**Expected outcome:** The loading path is clean and unobstructed with no obvious external damage.

### 8. Restart Only When Appropriate

If no cycle is active and facility procedures permit, perform a normal shutdown and restart to determine whether the cassette recognition interface recovers.

Do not use repeated power cycling to bypass a persistent cassette fault.

**Expected outcome:** The sterilizer starts normally and recognizes an approved cassette. If cassette handling remains reliable through setup, troubleshooting can stop.

### 9. Perform Final Functional Verification

Before returning the sterilizer to service, verify:

- Normal startup
- Cassette recognition
- Normal cassette status indication
- Successful cycle setup
- No recurring cassette-related message
- Any facility-required functional or quality checks

**Expected outcome:** Cassette operation is repeatable and the sterilizer is suitable for return to service.

### 10. Escalate Persistent Cassette-System Problems

If multiple known-good cassettes are rejected, the cassette will not index, or the mechanism shows abnormal operation, stop external troubleshooting.

**Expected outcome:** The sterilizer is removed from clinical processing pending qualified service evaluation.

## If the Problem Persists

Common external causes such as cassette condition, installation, consumable availability, and accessible obstruction have been ruled out. The remaining problem may involve the cassette transport, recognition system, controls, sensors, or another service-level condition.

The sterilizer should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench/service evaluation
- Evaluated using appropriate ASP documentation and approved test equipment
- Repaired or configured only by qualified personnel

After repair, complete the manufacturer-appropriate functional verification and facility-required sterilization quality checks before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not release instruments for patient use from a processing cycle when sterilant availability or cassette delivery is uncertain.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the processing workflow first, verify the cassette and installation before assuming an internal mechanism failure, and escalate persistent cassette-handling faults with clear CCR documentation.

That is successful troubleshooting.
