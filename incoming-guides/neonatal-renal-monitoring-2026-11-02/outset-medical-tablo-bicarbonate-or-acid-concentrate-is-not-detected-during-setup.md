---
schemaVersion: 1
title: "Outset Medical Tablo Hemodialysis (HD) Machine - Bicarbonate or Acid Concentrate Is Not Detected During Setup"
issueTitle: "Bicarbonate or Acid Concentrate Is Not Detected During Setup"
description: "Use this guide when Tablo does not recognize bicarbonate or acid concentrate during setup despite apparently correct supplies and connections."
assetType: "Hemodialysis (HD) Machine"
manufacturer: "Outset Medical"
model: "Tablo"
slug: "outset-medical-tablo-bicarbonate-or-acid-concentrate-is-not-detected-during-setup"
dateAdded: "2026-11-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Tablo would not detect the acid concentrate during treatment setup."
  cause: "Clinical Engineering found the external acid concentrate connection incompletely seated, preventing reliable recognition during setup."
  resolution: "The connection was reseated, setup was repeated successfully, concentrate recognition remained stable, and the machine completed functional verification before return to service."
helpfulDetails:
  - "Exact setup message displayed"
  - "Whether acid, bicarbonate, or both were affected"
  - "Concentrate type and condition"
  - "External tubing and connector condition"
  - "Presence of residue, crystallization, or moisture"
  - "Known-good concentrate substitution results"
  - "Whether the failure was repeatable"
  - "Setup stage where detection failed"
  - "Results after reseating or replacement"
  - "Final setup and functional verification status"
---

## What This Guide Helps With

Use this guide when Tablo does not recognize bicarbonate or acid concentrate during setup despite apparently correct supplies and connections.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Dialysis Continuity

Do not troubleshoot concentrate-detection problems while a patient depends on the affected Tablo for treatment. If treatment has not started, keep the machine out of clinical use until setup completes correctly. If a problem develops during treatment, follow the facility's clinical process for safely discontinuing or transferring therapy before technical troubleshooting.

Inspect for concentrate leakage, unusual odor, damaged tubing, wet connectors, or other conditions that could create a chemical or electrical hazard.

**Expected outcome:** The patient is supported by an appropriate alternate plan, and the Tablo can be evaluated without interrupting required therapy. If safe operation and correct concentrate recognition are restored and verified, troubleshooting can stop.

### 2. Confirm Which Concentrate Is Not Being Detected

Reproduce the reported condition through the normal setup workflow without bypassing prompts. Determine whether the problem involves:

- Acid concentrate
- Bicarbonate source
- Both concentrate sources
- A specific container, connection, or setup attempt
- Intermittent recognition rather than complete failure

Record the exact on-screen message or setup stage where progress stops.

**Expected outcome:** The failure is narrowed to a specific concentrate source or a broader setup-recognition problem. If the issue cannot be reproduced and repeated setup completes normally, document the test results and troubleshooting can stop.

### 3. Verify the Correct Concentrate and Consumables

Confirm that the concentrate and associated disposable supplies are the correct type for the intended Tablo setup and treatment configuration. Check labels, packaging, expiration status when applicable, and obvious signs of contamination, crystallization, leakage, damage, or improper storage.

Do not substitute an unapproved chemical or concentrate formulation merely to test recognition.

**Expected outcome:** Correct, intact, appropriate concentrate supplies are being used. If replacing an obviously incorrect or compromised supply restores recognition, complete setup verification and troubleshooting can stop.

### 4. Inspect the Concentrate Connections

Inspect the accessible acid and bicarbonate connections for:

- Incomplete seating
- Loose fittings
- Kinked tubing
- Pinched tubing
- Wet or contaminated connection surfaces
- Crystallized residue
- Damaged connectors
- Misrouted tubing

Disconnect and reconnect only as permitted by normal Clinical Engineering handling and manufacturer documentation.

**Expected outcome:** All concentrate connections are clean, correctly routed, and fully seated. If reseating the connection restores detection and setup proceeds normally, troubleshooting can stop after verification.

### 5. Check for Air, Flow Restriction, or Supply Depletion

Inspect the accessible concentrate path for conditions that could prevent the machine from sensing or drawing concentrate, including an empty or nearly empty source, blocked tubing, collapsed tubing, closed clamps where applicable, or excessive air in the accessible supply path.

Do not open internal fluid circuits or bypass sensors.

**Expected outcome:** The external concentrate supply path is unobstructed and capable of supplying fluid to the machine. If correcting an external restriction restores detection, complete setup verification and troubleshooting can stop.

### 6. Substitute a Known-Good Concentrate Supply When Appropriate

If permitted by facility procedure, repeat setup using a known-good, correctly prepared concentrate supply and compatible external consumables.

Change one item at a time so the cause can be identified.

**Expected outcome:** A known-good supply is detected normally. If the original concentrate or associated external consumable is identified as the cause, replace it, repeat setup, and troubleshooting can stop after successful verification.

### 7. Inspect Accessible Detection and Connection Areas

Examine accessible areas associated with the concentrate connections for residue, dried concentrate, moisture, debris, damage, or anything preventing correct mechanical engagement.

Clean only according to approved procedures. Do not insert tools into sensor openings or defeat detection mechanisms.

**Expected outcome:** Accessible detection and connection areas are clean, dry, undamaged, and unobstructed. If cleaning an approved accessible area restores recognition, repeat setup and verify normal operation before stopping.

### 8. Restart the Setup Under Controlled Conditions

If the external supply and connections are correct, safely cancel or restart the setup process as allowed by manufacturer procedures. Confirm that the system correctly recognizes each required concentrate source during a fresh setup sequence.

Do not repeatedly power-cycle a machine that shows abnormal heat, odor, leakage, electrical problems, or persistent startup faults.

**Expected outcome:** Tablo recognizes the required concentrate supplies and progresses normally through setup. If recognition remains unreliable, remove the device from service.

### 9. Perform Final Functional Verification

After correction, complete the normal setup process without bypassing warnings or prompts. Confirm that concentrate recognition remains stable and that the machine completes all required preparation checks before considering it available for clinical use.

**Expected outcome:** Setup completes normally with both concentrate sources correctly recognized and no recurring alarms or setup interruptions. Troubleshooting can stop.

## If the Problem Persists

If correct concentrate supplies, external tubing, connectors, seating, routing, and known-good substitutions have been verified, common external causes have been ruled out.

The remaining problem may involve an internal concentrate-detection circuit, fluid-delivery component, sensor, calibration condition, internal tubing path, software state, or service-level configuration issue. Do not bypass concentrate detection or proceed with treatment when the machine cannot reliably verify the required concentrate source.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated using appropriate Outset Medical documentation and approved test equipment
- Repaired, calibrated, or configured only by qualified personnel

Any corrective work affecting dialysate preparation or fluid delivery must be followed by appropriate manufacturer-required functional and safety verification before return to clinical use.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Never place a Tablo into patient use when required concentrate recognition is intermittent or incomplete, even if setup succeeds after repeated attempts.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Concentrate-recognition problems should be approached by protecting the patient, verifying the correct supplies and external fluid path, and proving simple causes before suspecting internal sensing or fluid-delivery failures. Reliable verification and clear CCR documentation are essential before return to service.

That is successful troubleshooting.
