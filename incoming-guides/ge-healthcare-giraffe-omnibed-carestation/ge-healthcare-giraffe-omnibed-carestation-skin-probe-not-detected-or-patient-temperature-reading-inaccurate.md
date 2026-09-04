---
schemaVersion: 1
title: "GE Healthcare Giraffe OmniBed Carestation Infant Incubator - Skin Probe Not Detected or Patient Temperature Reading Inaccurate"
issueTitle: "Skin Probe Not Detected or Patient Temperature Reading Inaccurate"
description: "Troubleshoots missing or inaccurate patient-temperature readings caused by probe connection, placement, cable damage, incompatible accessories, or sensing problems."
assetType: "Infant Incubator"
manufacturer: "GE Healthcare"
model: "Giraffe OmniBed Carestation"
slug: "ge-healthcare-giraffe-omnibed-carestation-skin-probe-not-detected-or-patient-temperature-reading-inaccurate"
dateAdded: "2026-09-04"
taxonomyMode: "reuse"
ccr:
  complaint: "NICU staff reported that the patient skin temperature intermittently disappeared from the OmniBed display."
  cause: "Clinical Engineering found a damaged skin-probe cable that opened intermittently when handled."
  resolution: "Replaced the probe with an approved compatible probe, verified a stable temperature reading and normal response, and completed functional testing."
helpfulDetails:
  - "Displayed skin temperature"
  - "Operating mode"
  - "Probe recognition status"
  - "Probe and cable condition"
  - "Connector condition"
  - "Probe placement observed"
  - "Known-good probe result"
  - "Whether cable movement affected reading"
  - "Test simulator or verification result"
  - "Alarm response"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots missing or inaccurate patient-temperature readings caused by probe connection, placement, cable damage, incompatible accessories, or sensing problems.

## Step-by-Step Troubleshooting

### 1. Protect the Infant Before Testing the Probe

If the OmniBed is using skin temperature as part of active thermal control, do not manipulate or substitute the probe while the infant depends on that control mode without clinical coordination.

Move to another verified thermal-support method or have clinical staff establish an appropriate safe operating condition first.

**Expected outcome:** Probe troubleshooting can proceed without compromising temperature control.

### 2. Confirm the Exact Probe Complaint

Determine whether the issue is:

- No skin temperature displayed
- Probe not recognized
- Intermittent reading
- Reading obviously inconsistent with the infant's clinical temperature
- Reading changes when the cable is moved
- One probe works while another does not

Record the operating mode and displayed temperature.

**Expected outcome:** The reported symptom is clearly reproduced or characterized.

### 3. Inspect the Skin Probe and Cable

Inspect the entire accessible probe assembly for:

- Cuts
- Crushed insulation
- Bent or damaged connector contacts
- Fluid contamination
- Loose strain relief
- Evidence of repeated pulling or pinching

Do not use a visibly damaged patient-temperature probe.

**Expected outcome:** The probe and cable are physically intact. A damaged accessory is removed from use.

### 4. Verify the Probe Connection

Disconnect and reconnect the skin probe according to normal equipment handling practices, ensuring the connector is fully seated and correctly aligned.

Inspect the receptacle externally for contamination or obvious damage.

**Expected outcome:** A secure connection restores and maintains the patient-temperature reading. If it does, troubleshooting can stop after verification.

### 5. Verify Correct Probe Placement

If the problem is inaccurate temperature rather than detection, have appropriate clinical personnel confirm that the probe is correctly attached to the patient and positioned according to clinical procedure.

A properly functioning sensor can provide a misleading value if it is detached, poorly secured, insulated incorrectly, or influenced by an external heat source.

**Expected outcome:** Probe placement is appropriate and the reading becomes clinically reasonable.

### 6. Substitute a Known-Good Compatible Probe

With the patient protected and using only an approved compatible accessory, connect a known-good probe.

Do not substitute an unapproved temperature sensor merely because the connector fits.

**Expected outcome:** If the known-good probe works normally, the original probe is the likely cause. Replace the defective probe and troubleshooting can stop after verification.

### 7. Compare the Reading Appropriately

If inaccuracy remains suspected, compare the displayed skin temperature using the applicable approved test method or simulator rather than relying only on a casual comparison with another clinical thermometer.

Follow current service documentation for test setup and interpretation.

**Expected outcome:** The skin-temperature channel accurately reports the approved test input.

### 8. Check for Intermittent Connector Behavior

Without stressing the connector, observe whether normal handling of the cable causes the reading to disappear or change abruptly.

If more than one known-good probe produces intermittent readings at the same equipment connector, remove the device from service.

**Expected outcome:** The connection remains stable during normal handling.

### 9. Perform Final Functional Verification

After correcting a probe or connection issue, verify stable temperature display and the applicable alarm and thermal-control functions using approved procedures before return to service.

**Expected outcome:** The patient-temperature channel operates reliably and passes required testing. Troubleshooting can stop.

## If the Problem Persists

If probe condition, connection, placement, and known-good substitution have been verified, the problem may involve the probe receptacle, temperature-input circuitry, calibration, wiring, processor, or thermal-control system.

The OmniBed should be:

- Removed from service when skin-temperature control cannot be trusted
- Labeled Out of Service
- Sent for repair or bench evaluation
- Tested using current GE Healthcare documentation and approved simulation or temperature test equipment
- Repaired or calibrated only by qualified personnel

Complete temperature-input, alarm, and applicable thermal-control testing before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A connected skin probe is not necessarily a correctly positioned skin probe; confirm placement before treating a questionable value as an equipment failure.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Displayed skin temperature
- Operating mode
- Probe recognition status
- Probe and cable condition
- Connector condition
- Probe placement observed
- Known-good probe result
- Whether cable movement affected reading
- Test simulator or verification result
- Alarm response
- Final device status

## Final Thought

Start with the probe, connector, and placement before assuming a problem inside the OmniBed. Patient-temperature inputs directly influence thermal-control decisions, so any channel that cannot be verified must be taken out of clinical use and properly escalated.

That is successful troubleshooting.
