---
schemaVersion: 1
title: "Karl Storz IMAGE1 S Rubina Endoscopic / OR Camera System - Power LED Rubina Light Source Will Not Ignite or Communicate"
issueTitle: "Power LED Rubina Light Source Will Not Ignite or Communicate"
description: "Helps isolate light-source ignition or communication failures caused by power, connections, light cables, controller communication, or external equipment problems."
assetType: "Endoscopic / OR Camera System"
manufacturer: "Karl Storz"
model: "IMAGE1 S Rubina"
slug: "karl-storz-image1-s-rubina-power-led-rubina-light-source-will-not-ignite-or-communicate"
dateAdded: "2026-11-16"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that the Rubina light source powered on but would not communicate with the IMAGE1 S system."
  cause: "Clinical Engineering found an external communication cable was not fully seated at the light-source connection."
  resolution: "The connection was reseated, communication and stable illumination were verified, and the system was returned to service."
helpfulDetails:
  - "Whether the light source powered on"
  - "Whether illumination was produced"
  - "Communication status"
  - "Outlet or power source checked"
  - "Power-cord condition"
  - "Light-cable condition"
  - "Communication cables inspected"
  - "Known-good substitutions"
  - "Any displayed message"
  - "Final light-source status"
---

## What This Guide Helps With

Helps isolate light-source ignition or communication failures caused by power, connections, light cables, controller communication, or external equipment problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Provide Alternate Illumination

Do not continue a procedure when the required endoscopic illumination is unavailable or unstable. Provide a verified alternate light source and imaging path before troubleshooting.

Never look directly into a connected active light output.

**Expected outcome:** Safe visualization is maintained independently of the affected light source.

### 2. Confirm the Exact Light-Source Failure

Determine whether the light source is completely unpowered, powered but not producing illumination, or producing light while communication with IMAGE1 S is unavailable.

Observe normal status indicators and record any displayed message.

**Expected outcome:** The problem is separated into power, illumination, or communication failure.

If normal illumination and communication return and remain stable, troubleshooting can stop after verification.

### 3. Verify AC Power and External Power Connections

Confirm the light source is connected to known-good AC power. Inspect the power cord and external power distribution for damage or looseness.

If appropriate, test the outlet using approved equipment or compare with another verified outlet.

**Expected outcome:** Reliable AC power is present and the light source powers normally.

If restoring power resolves the issue, perform final functional verification.

### 4. Verify Normal Startup

Restart the light source using normal controls if clinically appropriate and allow the system to complete startup.

Observe whether the light source remains powered without resetting.

**Expected outcome:** The unit completes normal startup and remains stable.

If normal restart restores illumination and communication, proceed to final verification.

### 5. Inspect Light Cable and Accessible Connections

Inspect the light cable for damage, contamination, poor seating, excessive bending, or damaged connector features.

Reconnect the cable securely without forcing it.

**Expected outcome:** The light cable is securely connected and illumination is available through the intended optical path.

If correcting the connection restores normal light output, troubleshooting can stop after verification.

### 6. Inspect Communication Connections

Check accessible communication or system interconnect cables between the light source and IMAGE1 S components.

Inspect for loose connectors, damaged cables, incorrect ports, or incomplete seating.

**Expected outcome:** The external communication path is secure and the light source is recognized by the system.

If communication is restored, proceed to final verification.

### 7. Compare With Known-Good Compatible Components

When available, substitute a verified compatible light cable or external communication cable one component at a time.

If another compatible light source is available, compare system behavior without altering undocumented settings.

**Expected outcome:** The test isolates whether the fault follows an external cable or the light-source assembly.

If a defective external component is identified, remove it from service and replace it.

### 8. Perform Final Functional Verification

Verify normal startup, stable illumination, communication with the IMAGE1 S system, and appropriate operation during standard and required Rubina visualization modes.

**Expected outcome:** Illumination is stable and light-source communication remains normal throughout testing.

If all checks pass, the equipment may be returned to service.

## If the Problem Persists

External power, light cable, communication connections, startup, and known-good substitutions have been checked.

Remove the affected light source from service, label it **Out of Service**, and send it for repair or bench evaluation. Persistent failure may involve internal light-generation circuitry, communication electronics, power conversion, firmware, or other service-level faults.

Evaluate with appropriate Karl Storz documentation and approved test equipment. Do not perform internal board-level troubleshooting or unauthorized repair.

Complete functional and applicable electrical-safety testing before return to service.

## Clinical Use Tip

Confirm both illumination and camera-system communication before a case that depends on Rubina visualization modes.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Loss of illumination requires immediate clinical backup. Verify power, cables, and communication before assuming an internal light-source failure, stop when external checks are exhausted, and document the final verified condition clearly.

That is successful troubleshooting.
