---
schemaVersion: 1
title: "Smiths Medical Medfusion 3500 Infusion Pump - Drug Library Missing, Outdated, or Will Not Load"
issueTitle: "Drug Library Missing, Outdated, or Will Not Load"
description: "Troubleshoots missing or unavailable drug-library content caused by configuration, communication, deployment, version, or server-related problems."
assetType: "Infusion Pump"
manufacturer: "Smiths Medical"
model: "Medfusion 3500"
slug: "smiths-medical-medfusion-3500-drug-library-missing-outdated-or-will-not-load"
dateAdded: "2026-09-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that a Medfusion 3500 did not display the expected current drug library for their care area."
  cause: "Clinical Engineering found the pump had not received the current authorized library deployment assigned to that device group."
  resolution: "The approved library was deployed through the authorized system process, the correct configuration was verified after restart, and the pump was returned to service."
helpfulDetails:
  - "Expected drug-library version or identifier"
  - "Library or profile actually displayed"
  - "Clinical area assignment"
  - "Device identifier"
  - "Comparison pump used"
  - "Network status"
  - "Deployment status"
  - "Whether other pumps were affected"
  - "Result after restart"
  - "Final verified configuration"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots missing or unavailable drug-library content caused by configuration, communication, deployment, version, or server-related problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Therapy
Do not alter drug-library configuration on a pump actively supporting a patient. If the required safety library is unavailable for the intended therapy, follow facility policy and provide an appropriately configured replacement pump.

**Expected outcome:** Patient therapy uses equipment with the required verified configuration.

### 2. Confirm the Exact Library Problem
Determine whether the library is completely missing, appears outdated, fails to load after deployment, contains an unexpected version, or is unavailable only within a particular profile or care area.

**Expected outcome:** The specific configuration discrepancy is documented.

### 3. Verify Device Identification and Assignment
Confirm the pump's identity and intended clinical assignment according to facility records. Make sure the unit has not been moved from another area with a different approved configuration.

**Expected outcome:** The device is being compared with the correct expected library and profile.

### 4. Compare With a Known-Good Pump
Check another properly functioning Medfusion 3500 assigned to the same clinical environment. Compare visible library or configuration information available through normal authorized interfaces.

**Expected outcome:** The expected library state and version can be distinguished from a pump-specific problem.

### 5. Check Power and Normal Startup
Restart the pump only when it is safely removed from clinical use. Observe whether the drug library becomes available after a normal startup and whether any configuration or communication messages appear.

**Expected outcome:** The pump completes startup normally and either loads the expected library or provides a reproducible failure condition.

### 6. Verify Network Availability if Library Distribution Uses the Network
Confirm that the pump has the expected network connection and that the relevant infrastructure is available. Determine whether other similar pumps are experiencing the same problem before assuming a device failure.

**Expected outcome:** Network-dependent library distribution has an available communication path.

### 7. Verify the Authorized Deployment Status
Using the facility's approved management process, determine whether the library was actually assigned, distributed, and accepted for this device or device group. Do not manually create or alter clinical drug data outside the approved governance process.

**Expected outcome:** The pump's expected deployment state is confirmed.

### 8. Check for Broader System Impact
Determine whether the problem affects one pump, multiple pumps in one area, or the entire fleet. Coordinate with pharmacy, medication-safety, IT, or the responsible system administrator as appropriate.

**Expected outcome:** A device-specific problem is separated from a server, deployment, or enterprise configuration issue.

### 9. Verify the Correct Library After Correction
After an authorized deployment or connectivity correction, confirm that the expected approved library or profile is displayed and remains available after a normal restart.

**Expected outcome:** The intended approved configuration is present and stable. If confirmed, troubleshooting can stop after documentation.

### 10. Escalate Unresolved Configuration Failure
If the pump cannot obtain or retain its required drug library despite verified infrastructure and authorized deployment, remove it from clinical use requiring that library and escalate to qualified service or system administration.

**Expected outcome:** A misconfigured pump is prevented from unintended clinical deployment.

## If the Problem Persists

Common causes involving device assignment, startup, network availability, deployment status, and system-wide configuration have been evaluated. The remaining problem may involve device configuration, software, server communication, database assignment, or another service-level condition.

The device should be:

- Removed from service when required configuration cannot be verified
- Labeled Out of Service when appropriate
- Sent for repair or bench evaluation if the problem is device-specific
- Evaluated using appropriate manufacturer documentation and approved system tools
- Repaired or configured only by qualified personnel

Any corrected pump should have its approved library, profile, communication state, and basic pump operation verified before clinical return. Knowing not to improvise medication-safety configuration is proper troubleshooting.

## Clinical Use Tip

Treat the drug library as a controlled medication-safety configuration; never substitute an unapproved local workaround for the facility's authorized deployment process.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Expected drug-library version or identifier
- Library or profile actually displayed
- Clinical area assignment
- Device identifier
- Comparison pump used
- Network status
- Deployment status
- Whether other pumps were affected
- Result after restart
- Final verified configuration
- Final device status

## Final Thought

Medication-library troubleshooting requires both technical verification and configuration control. Confirm assignment, connectivity, and authorized deployment before assuming a device failure, then escalate unresolved discrepancies appropriately.

That is successful troubleshooting.
