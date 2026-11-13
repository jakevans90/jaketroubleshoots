---
schemaVersion: 1
title: "Getinge Servo-n Ventilator - Nebulizer or Humidifier Integration Is Not Detected"
issueTitle: "Nebulizer or Humidifier Integration Is Not Detected"
description: "Troubleshoots missing nebulizer or humidifier integration caused by accessory compatibility, power, cables, mounting, configuration, or service-level communication faults."
assetType: "Ventilator"
manufacturer: "Getinge"
model: "Servo-n"
slug: "getinge-servo-n-nebulizer-or-humidifier-integration-is-not-detected"
dateAdded: "2026-11-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Respiratory Therapy reported that the Servo-n no longer detected the connected nebulizer interface during setup."
  cause: "Clinical Engineering found a damaged external nebulizer interface cable while a known-good cable restored communication."
  resolution: "The damaged cable was replaced, nebulizer detection and operation were verified, and the ventilator passed pre-use testing before return to service."
helpfulDetails:
  - "Nebulizer or humidifier involved"
  - "Accessory make and model"
  - "Detection versus power failure"
  - "Cable condition"
  - "Connector condition"
  - "Accessory power status"
  - "Known-good substitution result"
  - "Configuration observed"
  - "Circuit setup"
  - "Final integration test"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots missing nebulizer or humidifier integration caused by accessory compatibility, power, cables, mounting, configuration, or service-level communication faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Required Therapy
Do not interrupt required humidification or medication delivery solely to troubleshoot integration.

Provide an approved alternate method or move the patient to another verified setup before disconnecting an accessory that is necessary for current therapy.

**Expected outcome:** Required respiratory therapy continues independently while troubleshooting is performed.

### 2. Confirm Which Accessory Is Not Detected
Determine whether the problem involves:
- Nebulizer
- Humidifier
- Accessory communication only
- Accessory power
- Intermittent detection
- Detection after startup but not during operation

**Expected outcome:** The failure is clearly defined.

### 3. Verify Accessory Compatibility
Confirm the nebulizer, humidifier, interface module, cable, and mounting configuration are approved and compatible with the Servo-n setup.

Do not assume that physical connector compatibility means electronic integration is supported.

**Expected outcome:** The accessory configuration is appropriate for the ventilator.

### 4. Inspect Accessory Power
Verify the external accessory itself powers on normally when applicable.

Inspect its power supply, power cable, battery, or approved ventilator connection as appropriate.

**Expected outcome:** The accessory has reliable operating power.

### 5. Inspect Interface Cables and Connections
Check all external communication and power connections for:
- Loose plugs
- Damaged pins
- Bent contacts
- Contamination
- Broken cable insulation
- Damaged strain relief
- Improper routing

Reseat accessible connections.

**Expected outcome:** The accessory connection path is intact and securely connected.

### 6. Confirm Correct Physical Setup
Verify the accessory, breathing circuit, mounting position, adapters, and connection points match the intended setup.

For humidification systems, inspect for excessive condensate or accessory placement that could create a separate clinical problem even if electronic detection is restored.

**Expected outcome:** The accessory is physically installed correctly.

### 7. Test With Known-Good Compatible Components
When available, substitute a known-good interface cable, accessory, or approved power source one component at a time.

**Expected outcome:** If detection returns with one replacement component, the defective external item is identified and removed from service.

### 8. Verify Normal Configuration
Check accessible normal configuration options related to the accessory.

Do not alter undocumented settings or enter unauthorized service menus to force detection.

**Expected outcome:** The ventilator configuration is appropriate for the connected accessory.

### 9. Perform Final Functional Verification
Verify that the accessory is detected and functions correctly through the intended clinical workflow.

Confirm the ventilator continues to pass required pre-use and alarm checks.

**Expected outcome:** The accessory remains detected and operates reliably. Troubleshooting can stop.

## If the Problem Persists

Accessory compatibility, power, cables, positioning, and normal configuration have been ruled out. The remaining problem may involve an accessory interface, communication port, software compatibility issue, or internal service-level fault.

The affected equipment should be:
- Removed from integrated use
- Labeled Out of Service when the failed integration affects intended clinical use
- Sent for repair or bench evaluation
- Evaluated using appropriate Getinge and accessory-manufacturer documentation
- Repaired or configured only by qualified personnel

Verify both ventilator operation and accessory integration before return to clinical service.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

Loss of accessory detection should never result in unnoticed interruption of required humidification or aerosol therapy.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain therapy first, then verify accessory compatibility, power, cables, positioning, and configuration before suspecting an internal ventilator interface fault. Escalate unresolved integration failures and document the entire tested path.

That is successful troubleshooting.
