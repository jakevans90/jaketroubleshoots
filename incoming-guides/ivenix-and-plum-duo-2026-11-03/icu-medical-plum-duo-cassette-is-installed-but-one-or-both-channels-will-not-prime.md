---
schemaVersion: 1
title: "ICU Medical Plum Duo Infusion Pump - Cassette Is Installed but One or Both Channels Will Not Prime"
issueTitle: "Cassette Is Installed but One or Both Channels Will Not Prime"
description: "Troubleshoots priming failures caused by cassette installation, tubing, clamps, fluid source, door engagement, channel selection, or pump-detection problems."
assetType: "Infusion Pump"
manufacturer: "ICU Medical"
model: "Plum Duo"
slug: "icu-medical-plum-duo-cassette-is-installed-but-one-or-both-channels-will-not-prime"
dateAdded: "2026-11-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the cassette installed normally but channel two would not complete priming."
  cause: "Clinical Engineering found the administration set tubing kinked immediately above the cassette, preventing normal fluid movement."
  resolution: "Replaced the affected set, confirmed both channels primed normally, and completed functional verification before returning the pump to service."
helpfulDetails:
  - "Affected channel"
  - "Exact displayed message"
  - "Administration set condition"
  - "Cassette seating condition"
  - "Clamp positions"
  - "Tubing kinks or restrictions"
  - "Fluid source used"
  - "Known-good cassette result"
  - "Results on each channel"
  - "Door/latch behavior"
  - "Final priming result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots priming failures caused by cassette installation, tubing, clamps, fluid source, door engagement, channel selection, or pump-detection problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Therapy
Do not troubleshoot a pump that is actively providing unreliable therapy to a patient. Transfer the infusion to another verified pump when interruption or inaccurate delivery could affect patient care. Preserve the administration set and cassette if practical so the reported condition can be reproduced safely on the bench.

**Expected outcome:** Patient therapy continues on verified equipment and the affected Plum Duo is available for controlled troubleshooting.

If therapy is safely restored using another device, continue troubleshooting the removed pump.

### 2. Confirm Which Channel Will Not Prime
Determine whether the problem affects the first channel, second channel, or both. Reproduce the reported condition using an appropriate test setup rather than a patient-connected line. Record any displayed message exactly as shown.

**Expected outcome:** The affected channel and exact failure condition are confirmed.

If the channel primes normally and repeated attempts do not reproduce the problem, inspect the original disposable and document the finding before return to service.

### 3. Inspect the Administration Set and Cassette
Examine the cassette and associated tubing for deformation, contamination, cracked components, improperly seated tubing, closed clamps, severe kinks, or visible damage. Verify that the set is appropriate for the device and has not been previously damaged during installation.

**Expected outcome:** The cassette and tubing are intact, correctly assembled, and unobstructed.

If replacing a visibly defective disposable with an approved known-good set restores priming, the issue is resolved and troubleshooting can stop after functional verification.

### 4. Verify Fluid Source and Line Configuration
Confirm that the test fluid source contains adequate fluid, tubing is routed normally, clamps are open where required, and the line is not pinched by a pole clamp, tubing organizer, cassette door, or other accessory. Verify that source positioning is reasonable for the setup.

**Expected outcome:** Fluid can move freely from the source through the external tubing path.

If correcting a clamp, kink, or source-position problem restores priming, troubleshooting can stop after repeating the prime successfully.

### 5. Remove and Reinstall the Cassette
Remove the cassette, inspect the cassette interface for debris or obvious obstruction, and reinstall it carefully without forcing the mechanism. Verify that the cassette sits fully and evenly in its intended position and that the door or latch closes normally.

**Expected outcome:** The cassette is fully seated and recognized without excessive force or abnormal resistance.

If proper reseating restores priming on both channels, the issue is resolved.

### 6. Compare With a Known-Good Set
Install a new or verified known-good compatible administration set using the same test configuration. Do not reuse a questionable cassette when determining whether the pump or disposable is responsible.

**Expected outcome:** The known-good cassette primes normally on both channels.

If the known-good set works consistently, remove the defective disposable from use and document the disposable-related cause.

### 7. Compare the Two Channels
Using the same known-good setup, test each channel independently. Determine whether the failure follows the disposable or remains associated with one channel of the pump.

**Expected outcome:** Both channels respond consistently with the same verified setup.

If only one channel continues to fail while the other works with the identical cassette setup, remove the pump from service for further evaluation.

### 8. Restart the Pump and Retest
With no patient attached, perform a normal power cycle. Allow the pump to complete startup, then repeat cassette installation and priming using the known-good set.

**Expected outcome:** The pump completes startup and both channels prime normally.

If a normal restart restores reliable operation and repeated tests pass, complete final verification before return to service.

### 9. Perform Final Functional Verification
Verify normal startup, cassette recognition, door engagement, priming, channel selection, alarm operation, and basic infusion function using appropriate approved test equipment and procedures.

**Expected outcome:** Both channels prime and operate consistently without abnormal alarms or interruptions.

If all required checks pass, return the device to service according to departmental policy.

## If the Problem Persists

If one or both channels still will not prime after cassette seating, tubing, clamps, fluid source, known-good disposables, and normal startup have been verified, common external causes have been ruled out.

The remaining cause may involve the cassette-detection mechanism, pumping mechanism, channel sensing, configuration, or another service-level condition. Do not perform unauthorized internal adjustments or board-level troubleshooting.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate ICU Medical documentation and approved test equipment
- Repaired or configured only by qualified personnel
- Subjected to complete return-to-service testing before clinical use

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Move the patient to another verified infusion pump before troubleshooting any channel that cannot reliably prime or establish fluid delivery.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Safe troubleshooting starts by protecting the patient, then ruling out disposable, tubing, positioning, and cassette-installation problems before assuming an internal failure. Verify the correction, escalate unresolved channel-specific failures, and document the complaint, cause, and resolution clearly.

That is successful troubleshooting.
