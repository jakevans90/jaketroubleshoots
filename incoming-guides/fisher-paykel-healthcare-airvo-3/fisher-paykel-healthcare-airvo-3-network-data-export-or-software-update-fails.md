---
schemaVersion: 1
title: "Fisher & Paykel Healthcare Airvo 3 High-Flow Oxygen System - Network, Data Export, or Software Update Fails"
issueTitle: "Network, Data Export, or Software Update Fails"
description: "Troubleshoots supported communication, data-transfer, connection, configuration, media, and software-update problems without altering unauthorized system settings."
assetType: "High-Flow Oxygen System"
manufacturer: "Fisher & Paykel Healthcare"
model: "Airvo 3"
slug: "fisher-paykel-healthcare-airvo-3-network-data-export-or-software-update-fails"
dateAdded: "2026-10-13"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Airvo 3 could not complete a supported data transfer."
  cause: "Clinical Engineering found the external communication connection was not fully seated and the device was not maintaining the data link."
  resolution: "Clinical Engineering reseated the connection, verified successful data transfer, confirmed normal respiratory and alarm functions, and returned the device to service."
helpfulDetails:
  - "Exact communication or update message"
  - "Function being attempted"
  - "Software version observed"
  - "External cable or adapter condition"
  - "Approved media used"
  - "Network port or infrastructure tested"
  - "Known-good substitutions"
  - "Configuration observed"
  - "Update or export result"
  - "Primary device functions verified afterward"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots supported communication, data-transfer, connection, configuration, media, and software-update problems without altering unauthorized system settings.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Separate Therapy From Connectivity
Do not interrupt active respiratory therapy to troubleshoot optional communication, data export, or software functions. If troubleshooting requires restart, disconnection, or configuration changes, remove the Airvo 3 from patient use first.

**Expected outcome:** Clinical therapy is not disrupted by technical troubleshooting.

### 2. Confirm the Exact Failure
Determine whether the issue involves a supported network connection, failure to export information, failure to recognize approved media or accessories, inability to begin an update, or an update that reports an error.

Record the exact message and the step at which the process fails.

**Expected outcome:** The communication, export, or update failure is clearly defined.

### 3. Verify Normal Device Operation First
Confirm that the Airvo 3 completes startup and performs its primary respiratory functions normally. A device with broader startup, power, or control problems should not be treated as an isolated connectivity problem.

**Expected outcome:** The device itself is operational and the problem is isolated to the requested secondary function.

### 4. Inspect External Connections and Accessories
Inspect applicable external communication cables, adapters, approved removable media, or network connections for damage, looseness, contamination, incorrect insertion, or incompatible components.

**Expected outcome:** External connection hardware is intact and correctly installed.

### 5. Reseat the Applicable Connection
With the device in a safe nonpatient condition, disconnect and reconnect the affected external cable, adapter, or approved media.

**Expected outcome:** The connection is recognized and the requested operation succeeds. If so, proceed to final verification.

### 6. Substitute a Known-Good External Component
When applicable, test with a known-good approved cable, adapter, media device, network port, or other external component. Change one item at a time.

**Expected outcome:** Successful operation with the replacement identifies the original external component or infrastructure path as the cause.

### 7. Verify Network or Infrastructure Availability
For supported networked functions, confirm the connected network port and required infrastructure are operational. Coordinate with IT or the responsible clinical systems team when the problem extends beyond the device.

Do not alter VLANs, security settings, network addressing, or managed infrastructure without authorization.

**Expected outcome:** The infrastructure path is confirmed available or the problem is isolated outside the Airvo 3.

### 8. Verify User-Accessible Configuration
Confirm that applicable supported communication or export settings match the approved site configuration. Compare with a known-good device configuration when permitted.

Do not enter restricted service menus or make undocumented configuration changes.

**Expected outcome:** The failure is not caused by an obvious approved configuration mismatch.

### 9. Verify Software or Update Package Requirements
For a software update, confirm that the update is appropriate for the exact device configuration and was obtained through an approved source. Follow manufacturer instructions exactly.

Do not install unofficial software, interrupt an update unnecessarily, downgrade software without authorization, or repeatedly retry a failed update without understanding the failure.

**Expected outcome:** The correct approved update method and package are being used.

### 10. Repeat the Function Under Controlled Conditions
Retry the export, supported communication function, or approved update after external connection and infrastructure problems have been corrected.

**Expected outcome:** The requested operation completes normally. If successful, continue to full functional verification.

### 11. Perform Final Functional Verification
After any communication or software work, verify normal startup, controls, alarms, airflow, humidification, stored configuration, and any affected communication function before returning the Airvo 3 to clinical use.

**Expected outcome:** Both primary respiratory operation and the affected secondary function are normal. Troubleshooting can stop.

### 12. Escalate Persistent Communication or Update Failures
If known-good external connections, infrastructure, approved media, and accessible configuration have been verified but the problem remains, stop troubleshooting before making unauthorized software or internal hardware changes.

**Expected outcome:** The device or issue is referred to the appropriate qualified service, IT, cybersecurity, or manufacturer support pathway.

## If the Problem Persists

Common external connection, accessory, media, infrastructure, and accessible configuration causes have been ruled out. A persistent problem may involve internal communication hardware, software, corrupted data, protected configuration, network infrastructure, compatibility, or another service-level condition.

If the failure compromises required clinical functionality, remove the Airvo 3 from service and label it **Out of Service**. Send the device for bench evaluation or manufacturer-authorized service as appropriate. Evaluate it using Fisher & Paykel Healthcare documentation and approved test equipment. Software installation, protected configuration changes, or internal repair should be performed only by qualified personnel.

Following software or hardware service, perform complete return-to-service verification rather than testing only the network or export function. Knowing when to escalate a software or infrastructure problem is proper Clinical Engineering troubleshooting.

## Clinical Use Tip

Treat connectivity as secondary to respiratory safety; never interrupt reliable high-flow therapy simply to troubleshoot data transfer, networking, or a software update.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Connectivity and software problems should be isolated without compromising respiratory therapy. Verify connections, accessories, infrastructure, approved configuration, and software sources before assuming internal failure, escalate protected or persistent issues, and document both the corrective action and full return-to-service verification.

That is successful troubleshooting.
