---
schemaVersion: 1
title: "Abbott Alinity c Clinical Chemistry Analyzer - Calibration/QC Passes Locally but Results Do Not Release to LIS"
issueTitle: "Calibration/QC Passes Locally but Results Do Not Release to LIS"
description: "Identify result-transmission failures involving analyzer status, release rules, LIS communication, network connections, or host-interface configuration."
assetType: "Clinical Chemistry Analyzer"
manufacturer: "Abbott"
model: "Alinity c"
slug: "abbott-alinity-c-calibration-qc-passes-locally-but-results-do-not-release-to-lis"
dateAdded: "2026-11-25"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that completed Alinity c chemistry results were not appearing in the LIS despite acceptable calibration and QC."
  cause: "Clinical Engineering found that the external Ethernet connection at the system-control workstation was disconnected."
  resolution: "The network cable was securely reconnected, communication status recovered, and laboratory personnel verified successful delivery of an authorized test result to the correct LIS record."
helpfulDetails:
  - "Affected assay and specimen identifier"
  - "Analyzer result status"
  - "QC and calibration status"
  - "Host communication messages"
  - "Network link indicators"
  - "Cable and switch-port findings"
  - "Interface queue or rejection status"
  - "Transmission timestamps"
  - "LIS acknowledgment"
  - "Final end-to-end verification"
---

## What This Guide Helps With

Identify result-transmission failures involving analyzer status, release rules, LIS communication, network connections, or host-interface configuration.

## Step-by-Step Troubleshooting

### 1. Protect Result Reporting and Patient Care
- Notify laboratory personnel that results may not be reaching the Laboratory Information System (LIS).
- Confirm that clinicians have an approved alternate method for receiving urgent results.
- Do not assume results are available to clinical staff because they appear on the analyzer.
- Prevent duplicate or uncontrolled manual result entry.
- Follow the laboratory's downtime and result-reconciliation procedures.

Expected outcome: Patient-result communication remains controlled while the interface issue is investigated.

### 2. Confirm the Result-Release Failure
- Identify one affected specimen using its laboratory-approved identifiers.
- Verify that calibration and QC status are acceptable for the associated assay.
- Determine whether the patient result is complete, held, pending review, transmitted, or rejected.
- Ask laboratory personnel to confirm whether the result appears in the LIS.
- Document the analyzer result status and receiving-system status.

Expected outcome: The failure is identified as a result hold, transmission failure, or receiving-system problem.

### 3. Verify Result-Release Rules and Holds
- Coordinate with laboratory personnel to review applicable result-release requirements.
- Check for unresolved QC holds, sample flags, operator review requirements, or autoverification rules.
- Confirm that the result is eligible for transmission under the validated laboratory workflow.
- Do not bypass clinical validation or release restrictions.

Expected outcome: The result is confirmed eligible for release, or the laboratory identifies a legitimate hold. If correcting an approved workflow issue restores verified reporting, troubleshooting can stop.

### 4. Check Analyzer and Host Communication Status
- Review the Alinity c host or interface connection status.
- Check for disconnected, unavailable, or communication-error indications.
- Determine whether the failure affects one assay, selected specimens, or all results.
- Compare the timing with network maintenance, software changes, or LIS downtime.
- Record the exact interface message when available.

Expected outcome: The communication state and scope of the problem are established.

### 5. Inspect External Network Connections
- Verify the physical network connection at the approved analyzer or system-control connection point.
- Inspect accessible Ethernet cabling for damage or loose connectors.
- Check available port-link indicators.
- Coordinate with IT to confirm the assigned switch port and network service are operational.
- Do not change IP addresses, VLAN assignments, or interface settings without authorization.

Expected outcome: The external network path is physically connected and its operational status is verified.

### 6. Coordinate an End-to-End Interface Check
- Have IT or the LIS interface team review the relevant host connection and message queues.
- Determine whether results are leaving the Alinity c interface.
- Check whether the interface engine receives and accepts the messages.
- Confirm that specimen identifiers, test mappings, and receiving-system rules are valid.
- Review available rejection or acknowledgment information.
- Avoid repeated retransmission until duplicate-result handling is established.

Expected outcome: The failure is localized to analyzer release, transmission, interface processing, or LIS acceptance.

### 7. Verify Result Delivery After Correction
- Use an approved test transaction or laboratory-authorized specimen workflow.
- Confirm that the result leaves the analyzer.
- Verify receipt and correct association with the intended specimen in the LIS.
- Confirm test identity, units, status, and relevant flags remain intact.
- Have laboratory personnel reconcile any outstanding results.

Expected outcome: Results transmit accurately and appear in the correct LIS records. Troubleshooting can stop.

### 8. Escalate Persistent Interface Problems
- If physical communication is verified but messages still fail, coordinate further investigation with Abbott, IT, and the LIS vendor.
- Preserve event logs and interface timestamps.
- Keep the affected interface out of clinical use until controlled reporting is restored.

Expected outcome: The unresolved communication fault is assigned to the appropriate support team.

## If the Problem Persists

After checking result eligibility, analyzer interface status, external cabling, and LIS reception, remaining causes may include interface-engine configuration, message mapping, network infrastructure, software, or internal communication faults.

The affected analyzer interface or module should be:

- Removed from service for electronic result reporting and labeled **Out of Service** when reliable operation cannot be assured.
- Sent for repair or bench evaluation when an analyzer-side fault is suspected.
- Evaluated using approved Abbott, network, and LIS diagnostic procedures.
- Repaired or configured only by qualified, authorized personnel.
- Returned to service after successful end-to-end result transmission and laboratory acceptance testing.

Knowing when to stop external troubleshooting prevents accidental corruption or duplication of clinical results.

## Clinical Use Tip

Always verify result delivery at the receiving LIS, not just the analyzer transmission screen. Successful transmission does not automatically prove correct patient-record association.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Result-release troubleshooting must protect data integrity and patient communication. Determine whether results are held, unsent, or rejected before changing equipment or network conditions. Verify the full reporting path, escalate configuration issues, and document successful delivery.

That is successful troubleshooting.
