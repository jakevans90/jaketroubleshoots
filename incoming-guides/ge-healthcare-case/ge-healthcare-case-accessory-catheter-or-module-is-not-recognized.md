---
schemaVersion: 1
title: "GE Healthcare CASE Stress Test System - Accessory, Catheter, or Module Is Not Recognized"
issueTitle: "Accessory, Catheter, or Module Is Not Recognized"
description: "A connected CASE accessory or module is unavailable, unidentified, or fails to initialize despite being physically connected."
assetType: "Stress Test System"
manufacturer: "GE Healthcare"
model: "CASE"
slug: "ge-healthcare-case-accessory-catheter-or-module-is-not-recognized"
dateAdded: "2026-10-19"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that a connected CASE acquisition accessory was not recognized during system setup."
  cause: "Clinical Engineering found the external interface cable was damaged and communication returned with a known-good cable."
  resolution: "Replaced the damaged cable and verified the accessory was consistently recognized and functional after system restart."
helpfulDetails:
  - "Exact accessory or module"
  - "Recognition message or status"
  - "Connector condition"
  - "Accessory power status"
  - "Compatibility confirmed"
  - "Known-good accessory result"
  - "Known-good cable result"
  - "Results on another compatible system"
  - "Restart result"
  - "Final device status"
---

## What This Guide Helps With
A connected CASE accessory or module is unavailable, unidentified, or fails to initialize despite being physically connected.

## Step-by-Step Troubleshooting
### 1. Protect the Patient and Clarify the Accessory
Do not continue a stress study if the unrecognized accessory or module is necessary for safe monitoring or exercise control. Move the patient to an appropriate alternate setup before troubleshooting.

CASE does not normally use invasive catheters as a primary stress-test accessory, so identify exactly what staff mean by “catheter” before proceeding.

**Expected outcome:** The affected component and its clinical importance are clearly identified.

### 2. Confirm the Recognition Failure
Determine whether the component is completely absent, appears intermittently, is shown but unavailable, or stopped being recognized after a connection, restart, or equipment change.

**Expected outcome:** The failure mode is documented and reproducible.

### 3. Verify Physical Connection
Inspect accessible connectors and cables at the accessory, module, and CASE interface. Confirm the connection is fully seated and there are no visibly bent contacts, contamination, damaged housings, or strained cables.

**Expected outcome:** The accessory is physically connected correctly. If reseating restores recognition, proceed to final verification.

### 4. Verify Accessory Power
If the component has its own power source or external supply, confirm it is energized normally and inspect the external power connections.

**Expected outcome:** The accessory has appropriate external power and shows normal readiness.

### 5. Confirm Compatibility
Verify that the accessory or module is intended for the installed CASE configuration. Compare it with a known working component or approved manufacturer documentation.

Do not force an incompatible connector or modify an accessory to make it fit.

**Expected outcome:** The connected component is compatible with the system.

### 6. Substitute a Known-Good Accessory or Cable
When available, connect a verified compatible known-good accessory or communication cable to the same interface.

**Expected outcome:** If the known-good component is recognized, the original accessory or cable is isolated as the likely cause and should be removed from service.

### 7. Try the Suspect Accessory on an Approved Known-Good Setup
If practical and permitted, test the suspect component on another compatible system.

**Expected outcome:** A component that fails on multiple known-good interfaces is confirmed as the likely faulty accessory rather than a CASE workstation issue.

### 8. Perform a Controlled Restart
With the system out of clinical use, restart the accessory and CASE workstation in the normal supported manner.

Do not enter unauthorized service menus or change protected hardware configuration.

**Expected outcome:** The component initializes and remains recognized after restart.

### 9. Verify Full Accessory Function
Recognition alone is not sufficient. Confirm the accessory or module performs its intended function and maintains communication during an appropriate functional test.

**Expected outcome:** The component is recognized consistently and functions normally. The issue is resolved and troubleshooting can stop.

## If the Problem Persists
External connections, accessory power, compatibility, known-good substitutions, and normal restart have been evaluated. A persistent recognition failure may involve the CASE interface, module electronics, communication hardware, drivers or software, protected configuration, or another service-level issue.

Remove the affected system or accessory from service, label it **Out of Service**, and conduct bench evaluation using appropriate manufacturer documentation and approved test equipment. Repairs or configuration changes should be performed only by qualified personnel.

Complete functional testing of the affected interface before return to service.

## Clinical Use Tip
A peripheral that is recognized only intermittently should not be trusted for a stress study; verify stable communication before the patient begins exercise.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Recognition problems are best isolated by confirming the exact component, then checking connection, power, compatibility, and known-good substitutions. Avoid unsupported configuration changes and escalate when a stable external cause cannot be found.

That is successful troubleshooting.
