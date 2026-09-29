---
schemaVersion: 1
title: "Samsung Healthcare GM85 Fit Mobile X-Ray System - Detector or Acquisition Hardware Is Not Ready"
issueTitle: "Detector or Acquisition Hardware Is Not Ready"
description: "Addresses detector-not-ready or acquisition problems caused by detector power, charging, pairing, connections, positioning, or communication conditions."
assetType: "Mobile X-Ray System"
manufacturer: "Samsung Healthcare"
model: "GM85 Fit"
slug: "samsung-healthcare-gm85-fit-detector-or-acquisition-hardware-is-not-ready"
dateAdded: "2026-09-29"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology staff reported that the GM85 Fit detector remained unavailable and the system would not become ready for acquisition."
  cause: "Clinical Engineering found the detector battery discharged and the detector was not fully seated in its charging location."
  resolution: "Clinical Engineering correctly seated and charged the detector, confirmed stable recognition and acquisition readiness, and completed functional verification."
helpfulDetails:
  - "Exact detector status or message"
  - "Detector identifier"
  - "Detector charge indication"
  - "Physical condition"
  - "Wired or wireless operation"
  - "Docking or charging condition"
  - "Known-good detector result"
  - "Locations where communication was tested"
  - "Acquisition verification result"
  - "Final detector status"
---
## What This Guide Helps With

Addresses detector-not-ready or acquisition problems caused by detector power, charging, pairing, connections, positioning, or communication conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Imaging Availability
Do not delay necessary imaging while troubleshooting unreliable acquisition hardware. Use another verified detector or mobile X-ray system if clinically required.

Do not make repeated patient exposures while attempting to prove whether the detector is functioning.

Expected outcome: Patient imaging continuity is maintained without unnecessary exposure. Troubleshooting proceeds without a patient depending on the affected system.

### 2. Confirm the Reported Condition
Determine whether the detector is not detected, appears offline, does not reach ready status, disconnects intermittently, or fails only during acquisition.

Record any displayed message exactly as shown.

Expected outcome: The failure condition is clearly defined and reproducible. If detector readiness is restored before further action, continue with controlled verification.

### 3. Inspect Detector Condition
Inspect the detector externally for cracks, impact damage, loose covers, contamination, fluid exposure, or damaged connector areas.

Do not use a detector showing physical damage that could affect electrical safety, image integrity, or internal components.

Expected outcome: The detector is externally intact. Visible impact or liquid damage requires removal from service.

### 4. Verify Detector Power and Charge State
Confirm the detector is powered as intended and has adequate charge. If charging or docking is used, verify proper seating and normal external charging indications.

Compare operation after adequate charging when battery depletion is suspected.

Expected outcome: The detector has sufficient power and reaches its normal available state. If charging resolves the problem, verify acquisition functionality and stop troubleshooting.

### 5. Check Detector Selection and Association
Confirm the intended detector is selected or associated with the system using normal operator-accessible controls.

If multiple detectors are used in the department, confirm staff have not selected or brought the wrong detector to the system.

Do not enter restricted service configuration menus.

Expected outcome: The correct detector is selected and recognized. If correcting detector selection restores readiness, complete functional verification.

### 6. Check Wireless and Environmental Conditions
If detector communication is wireless, confirm the detector is within the expected operating area and that obvious environmental or infrastructure changes have not occurred.

Compare behavior near the system versus farther away. Avoid changing network infrastructure without coordination.

Expected outcome: Detector communication remains stable under normal operating conditions. If location or external interference is clearly responsible, document and escalate infrastructure concerns as appropriate.

### 7. Inspect Accessible Detector Connections
Where a wired connection, charger, docking location, or external accessory is involved, inspect the connection for bent contacts, contamination, loose seating, or damage.

Use only approved cleaning methods and accessories.

Expected outcome: Accessible detector interfaces are clean, intact, and securely connected. If correcting an external connection restores readiness, stop after verification.

### 8. Compare With a Known-Good Detector When Approved
If another compatible, approved detector is available and department procedures permit substitution, test the system with the known-good detector.

Do not change system configuration beyond normal supported detector selection.

Expected outcome: A known-good detector either operates normally, isolating the issue to the original detector, or shows the same problem, suggesting a system or communication issue.

### 9. Perform Final Acquisition Verification
Use the approved facility or manufacturer method for nonpatient operational verification. Confirm the detector reaches ready status, remains connected, and produces a usable image without communication interruption.

Expected outcome: Detector status and acquisition remain stable. If so, the system may be returned to service.

## If the Problem Persists

If detector power, condition, charge state, selection, accessible connections, and approved substitutions have been checked, common external causes have been ruled out.

Possible remaining categories include detector electronics, wireless hardware, acquisition subsystem communication, internal interface hardware, software configuration, or infrastructure faults.

The affected device or detector should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate Samsung Healthcare documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Do not clinically use a detector that connects intermittently or produces unreliable acquisition status. Complete acquisition and image-quality verification before return to service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Confirm detector readiness before positioning a patient so a communication problem does not lead to unnecessary repositioning or repeat exposure.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Detector troubleshooting should rule out charge, selection, connection, and environmental causes before assuming internal hardware failure while avoiding unnecessary patient exposure and documenting the final verified condition.

That is successful troubleshooting.
