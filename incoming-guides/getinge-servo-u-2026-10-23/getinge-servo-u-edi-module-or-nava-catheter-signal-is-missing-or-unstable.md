---
schemaVersion: 1
title: "Getinge Servo-u Ventilator - Edi Module or NAVA Catheter Signal Is Missing or Unstable"
issueTitle: "Edi Module or NAVA Catheter Signal Is Missing or Unstable"
description: "Helps isolate missing or unstable Edi/NAVA signals caused by catheter placement, connections, accessories, setup, or external signal interference."
assetType: "Ventilator"
manufacturer: "Getinge"
model: "Servo-u"
slug: "getinge-servo-u-edi-module-or-nava-catheter-signal-is-missing-or-unstable"
dateAdded: "2026-10-23"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Servo-u intermittently lost the Edi signal and NAVA could not be reliably maintained."
  cause: "Clinical Engineering found the external Edi connection was not fully seated and the signal dropped when the cable was moved."
  resolution: "Reseated and secured the Edi connection, verified a stable signal during external handling, completed functional checks, and returned the ventilator to service."
helpfulDetails:
  - "Exact Edi/NAVA symptom displayed"
  - "Whether Edi was absent or intermittent"
  - "Ventilation mode in use when reported"
  - "Edi module recognition status"
  - "Catheter connection condition"
  - "Clinical confirmation of catheter positioning"
  - "Cable and connector condition"
  - "Known-good accessory substitution results"
  - "Whether movement affected the signal"
  - "Environmental or interference observations"
  - "Results before and after correction"
  - "Final device status"
---

## What This Guide Helps With

Helps isolate missing or unstable Edi/NAVA signals caused by catheter placement, connections, accessories, setup, or external signal interference.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Ventilation
If the patient depends on NAVA or Edi-based monitoring, do not troubleshoot an unreliable signal while therapy depends on it. Transition the patient to an appropriate verified ventilation mode or another ventilator as clinically directed before technical troubleshooting.

Confirm that ventilation remains stable and appropriate while Clinical Engineering evaluates the Edi system.

**Expected outcome:** The patient has uninterrupted respiratory support independent of the questionable Edi/NAVA signal.

If safe ventilation has been established, continue troubleshooting.

### 2. Confirm the Exact Reported Condition
Determine whether the reported problem is:

- No Edi waveform or value
- Intermittent Edi signal
- Edi signal that disappears with movement
- NAVA unavailable because the Edi signal is not usable
- Edi module or associated accessory not recognized
- Signal present but obviously unstable or inconsistent

Record whether the problem began after catheter insertion, patient repositioning, transport, accessory exchange, cleaning, or ventilator restart.

**Expected outcome:** The failure is clearly defined and can be reproduced or verified.

If the signal is now stable and the original condition cannot be reproduced, perform final verification before returning the device to service.

### 3. Inspect the Edi Module and External Connections
Inspect the Edi-related module, cable, connector, and ventilator interface for:

- Loose or partially seated connections
- Bent, damaged, contaminated, or wet connector surfaces
- Cable strain
- Cracked housings
- Evidence of fluid intrusion
- Improperly connected accessories

Disconnect and reconnect accessible external connections according to normal approved handling practices.

**Expected outcome:** All Edi system connections are clean, undamaged, and securely seated.

If reseating an external connection restores a stable signal, verify operation and stop troubleshooting.

### 4. Verify the Correct NAVA Catheter and Patient Connection
Confirm that the catheter and associated connection components are appropriate for the intended NAVA/Edi setup and have not been substituted with an incompatible accessory.

Clinical personnel should verify catheter placement and patient-related positioning using the approved clinical procedure. Clinical Engineering should not reposition an invasive patient catheter unless specifically trained and authorized to perform that clinical task.

**Expected outcome:** The correct catheter is connected and clinical staff confirm that patient placement is acceptable.

If correcting the catheter connection or clinical positioning restores a stable Edi signal, troubleshooting can stop after verification.

### 5. Check for Movement-Related or Intermittent Connections
While the device is off the patient or otherwise safely isolated from dependent clinical use, gently inspect accessible cables and connectors for intermittent behavior.

Do not aggressively flex or manipulate a catheter or patient-connected component.

Look for signal changes associated with:

- Connector movement
- Cable positioning
- Module movement
- Bed or ventilator repositioning

**Expected outcome:** The signal remains stable during normal external handling.

If the failure consistently follows an external cable or connector and disappears with a known-good replacement, replace the defective accessory and proceed to final verification.

### 6. Compare With a Known-Good Compatible Accessory
When available and permitted, substitute a known-good compatible external Edi cable, module accessory, or other replaceable connection component.

Do not substitute patient-specific or invasive components unless clinically appropriate and managed by authorized staff.

**Expected outcome:** A known-good external component either restores normal Edi operation or confirms that the issue is not limited to that accessory.

If a known-good external accessory corrects the problem, remove the defective accessory from service and stop troubleshooting after functional verification.

### 7. Review Ventilator Setup and Edi/NAVA Availability
Verify that the ventilator is configured for the intended clinical setup and that the Edi/NAVA functionality expected by the department is available.

Do not enter restricted service menus or change protected configuration settings without authorization and manufacturer documentation.

Check for obvious incorrect setup selections or a mode/configuration state that prevents Edi information from being displayed or used.

**Expected outcome:** The ventilator is appropriately configured for Edi/NAVA use without unauthorized configuration changes.

If correcting an approved setup selection restores operation, confirm stable signal performance and stop troubleshooting.

### 8. Check for Environmental or Electrical Interference
Evaluate whether the instability occurs only when other equipment is connected or operating nearby.

Inspect for:

- Damaged power cords or grounding connections
- Multiple devices sharing questionable power strips or adapters
- Strong electrical interference associated with nearby equipment
- Cable routing alongside high-energy equipment or power cables

Do not defeat protective grounding or alter facility electrical systems.

**Expected outcome:** The Edi signal remains stable in a normal clinical electrical environment.

If relocating an interfering external cable or removing a confirmed external interference source restores reliable operation, verify the full clinical setup and stop troubleshooting.

### 9. Perform Final Functional Verification
After any correction, verify the Servo-u using an appropriate approved test setup before patient use.

Confirm:

- Edi module recognition
- Stable Edi signal when connected to an appropriate test or clinical setup
- No recurring connection-related faults
- Normal ventilator operation
- No new alarms or abnormal behavior introduced during troubleshooting

**Expected outcome:** The Edi/NAVA system operates consistently and the ventilator passes required return-to-service checks.

If all checks pass, the device may be returned to service according to facility policy.

### 10. Escalate an Unresolved Edi/NAVA Failure
If the Edi signal remains missing or unstable after external accessories, connections, clinical placement, setup, and environmental causes have been ruled out, stop external troubleshooting.

Do not perform board-level repair or unauthorized internal diagnostics.

**Expected outcome:** The ventilator is removed from clinical use and routed for qualified service evaluation.

## If the Problem Persists

Common external causes have been ruled out. The remaining problem may involve the Edi interface, module electronics, ventilator communication, protected configuration, software, or another internal service-level condition.

The device should be:

- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate Getinge service documentation and approved test equipment
- Repaired or configured only by qualified personnel

Any Edi/NAVA repair must be followed by appropriate functional and return-to-service testing before patient use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not allow a patient to remain dependent on NAVA when the Edi signal is unreliable; establish stable alternate ventilation before troubleshooting.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient first, then isolate the Edi signal path logically from the patient connection outward. Verify accessories and setup before assuming an internal Servo-u failure, escalate appropriately, and document the actual cause and verification clearly.

That is successful troubleshooting.
