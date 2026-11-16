---
schemaVersion: 1
title: "Karl Storz IMAGE1 S Rubina Endoscopic / OR Camera System - IMAGE1 S Controller Will Not Boot or a CONNECT Module Remains Offline"
issueTitle: "IMAGE1 S Controller Will Not Boot or a CONNECT Module Remains Offline"
description: "Helps isolate startup or module-offline problems caused by AC power, interconnects, module seating, external cables, startup sequence, or system-level faults."
assetType: "Endoscopic / OR Camera System"
manufacturer: "Karl Storz"
model: "IMAGE1 S Rubina"
slug: "karl-storz-image1-s-rubina-image1-s-controller-will-not-boot-or-a-connect-module-remains-offline"
dateAdded: "2026-11-16"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that the IMAGE1 S controller powered on but one CONNECT module remained offline after startup."
  cause: "Clinical Engineering found an external interconnect cable was loose at the affected module."
  resolution: "The cable was reseated, the system was restarted, and stable module communication, camera recognition, and live video were verified."
helpfulDetails:
  - "Whether the controller powered on"
  - "Startup stage reached"
  - "Whether resets occurred"
  - "CONNECT module affected"
  - "AC power checked"
  - "Module power indicators"
  - "Interconnect cable condition"
  - "External accessories isolated"
  - "Known-good cables or modules tested"
  - "Final startup and communication status"
---

## What This Guide Helps With

Helps isolate startup or module-offline problems caused by AC power, interconnects, module seating, external cables, startup sequence, or system-level faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Provide Alternate Visualization

Do not troubleshoot a controller that will not boot or has required modules offline while a patient depends on the system.

Move the case to a verified alternate camera system or provide another approved visualization method.

**Expected outcome:** Patient care does not depend on the affected controller.

### 2. Confirm the Exact Startup Failure

Determine whether the controller is completely unpowered, begins startup but never completes it, repeatedly restarts, or boots while a CONNECT module remains offline.

Record normal indicator behavior and any displayed fault message.

**Expected outcome:** The failure is clearly classified as power, startup, restart, or module communication related.

If the system completes startup normally and all required modules remain online, troubleshooting can stop after verification.

### 3. Verify AC Power

Confirm the controller and associated modules are connected to known-good AC power.

Inspect power cords, power strips approved for the installation, and external connections for damage or looseness.

**Expected outcome:** Stable AC power is available to each required system component.

If restoring power resolves the startup problem, proceed to final verification.

### 4. Check External Module Power Status

Verify each connected module shows expected normal power indications.

Confirm modules have not been unintentionally switched off or disconnected from external power.

**Expected outcome:** All required modules receive power and remain energized.

If a module returns online after correcting its power connection, verify complete system operation.

### 5. Inspect System Interconnect Cables

Power down when appropriate and inspect accessible controller-to-module cables for damage, incorrect connections, loose locking mechanisms, or incomplete seating.

Reconnect each cable securely without forcing it.

**Expected outcome:** Interconnect cables are fully seated and module communication is restored.

If the CONNECT module returns online and remains stable, proceed to final verification.

### 6. Perform a Controlled Restart

Using normal controls, power the system down and restart it in the approved normal operating sequence.

Do not repeatedly cycle power if the controller resets continuously or shows signs of electrical distress.

**Expected outcome:** The controller completes startup once and all required modules become available.

If startup completes normally and remains stable, continue to final verification.

### 7. Isolate External Accessories

If the system still will not complete startup, disconnect nonessential external accessories only when safe and permitted, then retry normal startup.

Do not disconnect internal wiring or open modules.

**Expected outcome:** The test identifies whether an external accessory or connection is preventing normal operation.

If removing one external accessory restores startup, keep that accessory out of service and verify the remaining system.

### 8. Compare Known-Good External Cables or Modules

When available and approved, substitute a verified compatible external interconnect cable or module one component at a time.

**Expected outcome:** The comparison identifies whether the offline condition follows an external cable or module.

If a specific external component is isolated, remove it from service.

### 9. Perform Final Functional Verification

Restart the complete intended configuration and verify the controller boots normally, all required CONNECT modules remain online, the camera head is recognized, live video is stable, and required visualization modes are available.

**Expected outcome:** The complete system starts normally and remains stable without module dropouts or resets.

If all checks pass, the system may be returned to service.

## If the Problem Persists

AC power, module power, interconnect cables, startup sequence, external accessories, and available substitutions have been checked.

Remove the system from service, label it **Out of Service**, and send it for repair or bench evaluation. Persistent boot or module-offline problems may involve internal power supplies, processor functions, communication hardware, firmware, or system configuration.

Evaluate using appropriate Karl Storz service documentation and approved test equipment. Internal repair, module configuration, or service-level software actions should be performed only by qualified personnel.

Do not return the system to clinical use until the complete intended configuration boots successfully and remains stable.

## Clinical Use Tip

Verify the entire IMAGE1 S system configuration before a case; a controller that boots is not ready for use if a required CONNECT module remains offline.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Start controller and module troubleshooting with power and external communication paths before assuming an internal system failure. Protect clinical continuity, stop when safe external checks are exhausted, escalate appropriately, and document the final verified configuration.

That is successful troubleshooting.
