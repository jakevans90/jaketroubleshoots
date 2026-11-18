---
schemaVersion: 1
title: "GE Healthcare AMX Navigate Mobile X-Ray System - Detector Will Not Connect, Charge, or Register to the System"
issueTitle: "Detector Will Not Connect, Charge, or Register to the System"
description: "A compatible digital detector is unavailable, fails registration, will not communicate, or does not charge as expected."
assetType: "Mobile X-Ray System"
manufacturer: "GE Healthcare"
model: "AMX Navigate"
slug: "ge-healthcare-amx-navigate-detector-will-not-connect-charge-or-register-to-the-system"
dateAdded: "2026-11-18"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported the AMX Navigate would not recognize the detector and the detector remained unavailable for imaging."
  cause: "Clinical Engineering found the detector was not fully seated in its charging/interface position and the accessible contacts were contaminated."
  resolution: "Cleaned the accessible contacts, reseated the detector, confirmed normal recognition and charging indication, and completed a successful non-patient functional acquisition test."
helpfulDetails:
  - "Detector asset or identification number"
  - "Exact status message"
  - "Detector battery condition"
  - "Charging indication"
  - "Physical damage"
  - "Charging-contact condition"
  - "Whether the detector powers on"
  - "Known-good detector result"
  - "Comparison-system result"
  - "Connection stability"
  - "Final acquisition result"
  - "Final device status"
---

## What This Guide Helps With

A compatible digital detector is unavailable, fails registration, will not communicate, or does not charge as expected.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care Before Troubleshooting
Do not delay an urgent examination while repeatedly troubleshooting an unavailable detector. Move clinical imaging to another verified detector or imaging system when necessary.

Expected outcome: Patient imaging can continue safely while the affected detector or system is evaluated.

### 2. Confirm the Exact Detector Complaint
Determine whether the detector:
- Is not recognized
- Is recognized but unavailable for acquisition
- Connects intermittently
- Does not charge
- Appears discharged
- Is assigned to another system
- Loses connection after initially registering

Record any displayed detector-status message exactly.

Expected outcome: The communication, registration, or charging problem is clearly defined.

### 3. Verify Detector Identity and Compatibility
Confirm the detector being used is the intended detector for the AMX Navigate configuration. Check labeling, asset identification, and local detector-assignment records where applicable.

Expected outcome: The detector is confirmed to belong to or be approved for the system being tested.

### 4. Inspect the Detector Externally
Inspect for:
- Cracks
- Impact damage
- Bent or damaged connection areas
- Contamination
- Fluid intrusion
- Damaged battery or battery interface, when applicable
- Damaged charging contacts or connectors

Remove a detector with significant physical damage from clinical use.

Expected outcome: The detector has no obvious condition that would make further operation unsafe.

### 5. Verify Detector Power and Battery Condition
Confirm the detector can power normally and has adequate battery charge for communication testing. Reseat an externally removable battery when appropriate and permitted.

Expected outcome: The detector powers normally with adequate energy available.

### 6. Inspect Charging Interfaces
Inspect the detector charging location, dock, contacts, or associated accessible cabling for contamination, bent contacts, incomplete seating, or obvious physical damage.

Expected outcome: The detector seats correctly and the charging interface is clean and mechanically intact.

### 7. Re-establish the Normal Detector Connection
Use the normal approved workflow to reconnect or select the detector without entering unauthorized service menus or changing network parameters.

Expected outcome: The AMX Navigate identifies the intended detector and reports it available for acquisition. If successful, proceed to final verification.

### 8. Test With a Known-Good Compatible Detector
If available, connect a known-good compatible detector to the same system.

- If the known-good detector works, the original detector or its battery/charging path is suspect.
- If neither detector works, investigate the AMX Navigate communication/configuration side.

Expected outcome: Substitution isolates the problem to the detector or system side.

### 9. Test the Suspect Detector on an Approved Comparison System
When facility workflow and detector configuration permit, test the suspect detector using another compatible system or approved charging location.

Expected outcome: The comparison establishes whether the detector failure follows the detector.

### 10. Perform Final Acquisition Verification
After restoring communication, verify the detector remains connected and completes an approved test acquisition using facility procedures. Do not expose a patient merely to test the equipment.

Expected outcome: The detector remains available and acquisition completes normally. Troubleshooting can stop.

### 11. Escalate Persistent Detector Problems
If the detector will not register, connect, charge, or remain connected after external checks and known-good substitution, remove the affected detector or system from service as appropriate.

Expected outcome: Unreliable detector operation is not returned to clinical use.

## If the Problem Persists

External charging, seating, identity, battery, and connection causes have been ruled out. Remaining possibilities may involve detector electronics, wireless communication hardware, system configuration, charging electronics, internal battery condition, or service-level pairing/registration.

The affected equipment should be:
- Removed from service
- Labeled Out of Service
- Sent for repair or bench evaluation
- Evaluated using appropriate GE Healthcare documentation and approved test equipment
- Repaired or configured only by qualified personnel

After repair, verify detector recognition, stable connection, charging where applicable, and successful image acquisition before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Confirm detector availability before positioning the patient so an unavailable detector does not create unnecessary delay or repeat positioning.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Confirm detector identity, physical condition, battery status, charging interfaces, and known-good substitutions before assuming an internal detector or system failure. Return the equipment only after stable recognition and acquisition have been verified.

That is successful troubleshooting.
