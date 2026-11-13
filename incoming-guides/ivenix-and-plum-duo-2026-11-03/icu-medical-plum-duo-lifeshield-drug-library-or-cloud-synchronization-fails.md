---
schemaVersion: 1
title: "ICU Medical Plum Duo Infusion Pump - LifeShield Drug Library or Cloud Synchronization Fails"
issueTitle: "LifeShield Drug Library or Cloud Synchronization Fails"
description: "Troubleshoots synchronization failures involving connectivity, device assignment, date/time, network access, pending updates, or fleet-management configuration."
assetType: "Infusion Pump"
manufacturer: "ICU Medical"
model: "Plum Duo"
slug: "icu-medical-plum-duo-lifeshield-drug-library-or-cloud-synchronization-fails"
dateAdded: "2026-11-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Pharmacy reported that one Plum Duo remained on the previous drug-library version after the scheduled fleet deployment."
  cause: "Clinical Engineering found that the pump was not assigned to the intended deployment group in the authorized fleet-management system."
  resolution: "Corrected the approved device assignment, confirmed successful synchronization, and verified the expected drug-library version on the pump."
helpfulDetails:
  - "Exact synchronization message"
  - "Current drug-library version"
  - "Intended library version"
  - "Network connection indication"
  - "Location tested"
  - "Known-good pump comparison"
  - "Fleet assignment"
  - "Deployment status"
  - "Device date/time"
  - "Restart result"
  - "Final synchronization status"
---

## What This Guide Helps With

Troubleshoots synchronization failures involving connectivity, device assignment, date/time, network access, pending updates, or fleet-management configuration.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Safe Medication Delivery
Do not alter drug-library configuration on a pump being relied upon for active patient therapy. If current library availability or synchronization status creates uncertainty about safe programming, replace the pump with a verified device according to facility policy.

**Expected outcome:** Clinical therapy remains supported by a pump with an approved, verified configuration.

### 2. Confirm the Exact Synchronization Problem
Determine whether the issue involves downloading a drug library, uploading device data, cloud connectivity, synchronization status, or a specific pending deployment. Record all displayed status messages exactly.

**Expected outcome:** The failure is clearly defined rather than treated as a general network problem.

### 3. Verify the Pump Is Otherwise Operating Normally
Confirm normal startup, responsive controls, correct displayed date/time where user-visible, and absence of unrelated startup or system faults.

**Expected outcome:** The pump is stable enough for communication troubleshooting.

If the device is rebooting or otherwise unstable, troubleshoot that condition first and remove it from clinical use.

### 4. Check Network Availability
Verify that the expected hospital wireless or network environment is available in the location. Compare with another Plum Duo known to synchronize successfully in the same area when possible.

**Expected outcome:** A known-good device can access the required network environment.

If multiple pumps fail in the same area, escalate the network or infrastructure issue rather than replacing individual pumps.

### 5. Check Device Connectivity Status
Review permitted user-accessible network status indications without entering unauthorized service menus. Confirm the pump appears connected rather than offline or continuously attempting to associate.

**Expected outcome:** The device indicates normal network connectivity.

### 6. Compare Locations
Move the pump to a location where another verified Plum Duo has recently synchronized successfully, if operationally practical.

**Expected outcome:** The pump synchronizes in a known-good coverage area.

If synchronization succeeds elsewhere, investigate wireless coverage, network segmentation, or local infrastructure.

### 7. Verify Device Identity and Fleet Assignment
Using authorized fleet-management tools and approved procedures, verify the pump is correctly registered, assigned, and targeted for the intended library or synchronization group. Do not alter production configuration without appropriate authorization.

**Expected outcome:** The device is recognized by the management system and assigned to the intended deployment.

If correcting an authorized assignment restores synchronization, document the configuration change and verify completion.

### 8. Check Deployment Status
Determine whether the requested drug library or update is actually published, approved, and targeted to this pump. Compare the pump's displayed library version or status with another correctly updated unit when available.

**Expected outcome:** The pump is eligible for and correctly targeted by the pending deployment.

### 9. Restart and Reattempt Synchronization
If permitted by workflow and no patient is attached, perform a normal restart and allow sufficient time for standard network reconnection and approved synchronization processes.

**Expected outcome:** The pump reconnects and completes its normal synchronization workflow.

If successful, verify the expected library or synchronization status before concluding.

### 10. Perform Final Verification
Confirm the correct approved drug library or synchronization state is present, the pump starts normally, and no communication or configuration warnings remain.

**Expected outcome:** The pump displays the intended approved configuration and communicates normally.

## If the Problem Persists

If network availability, location, registration, targeting, deployment status, and normal restart have been verified, common external causes have been ruled out.

Possible remaining causes include device communication hardware, certificate or authentication issues, backend synchronization services, wireless infrastructure, fleet-management configuration, or other service-level problems.

The pump should be removed from service if its required drug library or connectivity configuration cannot be verified for safe clinical use. Label it **Out of Service** when appropriate and escalate to qualified Clinical Engineering, IT/network support, pharmacy informatics, ICU Medical support, or the authorized system administrator.

Any configuration changes should follow approved change-control procedures. Complete functional and configuration verification before return to service.

## Clinical Use Tip

Never assume a pump has received the current approved drug library solely because it is powered on and connected to Wi-Fi.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Drug-library troubleshooting should separate the pump, wireless network, fleet assignment, and backend deployment process before assuming a device failure. Maintain patient safety, protect configuration control, verify the final library state, and document all changes.

That is successful troubleshooting.
