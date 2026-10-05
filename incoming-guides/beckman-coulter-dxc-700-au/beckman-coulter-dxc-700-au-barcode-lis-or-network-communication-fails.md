---
schemaVersion: 1
title: "Beckman Coulter DxC 700 AU Clinical Chemistry Analyzer - Barcode, LIS, or Network Communication Fails"
issueTitle: "Barcode, LIS, or Network Communication Fails"
description: "Use when barcodes are not read or orders and results do not move correctly between the analyzer and laboratory information systems."
assetType: "Clinical Chemistry Analyzer"
manufacturer: "Beckman Coulter"
model: "DxC 700 AU"
slug: "beckman-coulter-dxc-700-au-barcode-lis-or-network-communication-fails"
dateAdded: "2026-10-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that the DxC 700 AU was processing samples but results were not reaching the LIS."
  cause: "Clinical Engineering found the external network cable at the analyzer workstation was partially disconnected."
  resolution: "The network connection was reseated, test communication was performed, and successful result transmission to the LIS was verified."
helpfulDetails:
  - "Barcode, order, or result communication affected"
  - "Exact displayed message"
  - "Whether all or some specimens are affected"
  - "Barcode condition"
  - "Network cable condition"
  - "Workstation network status"
  - "Other analyzers affected or unaffected"
  - "LIS or middleware status"
  - "Test transmission result"
  - "Final end-to-end communication status"
---
## What This Guide Helps With

Use when barcodes are not read or orders and results do not move correctly between the analyzer and laboratory information systems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification and Result Integrity
Do not manually associate results with patients unless the laboratory's approved downtime procedure specifically supports it. Use validated downtime workflows when communication is unavailable.

**Expected outcome:** Patient identification and result traceability remain intact during the communication failure.

### 2. Determine the Scope of the Failure
Identify whether the issue is barcode reading, order download, result upload, bidirectional communication, or complete network loss. Determine whether all specimens or only certain records are affected.

**Expected outcome:** The problem is localized to barcode input, analyzer communication, LIS workflow, or broader network infrastructure.

### 3. Check Barcode Quality and Placement
Inspect affected labels for wrinkles, damage, contamination, poor print quality, excessive overlap, or placement that prevents normal reading. Compare with a known-good labeled specimen or test label.

**Expected outcome:** Barcode quality is confirmed or a labeling issue is identified.

### 4. Verify Accessible Communication Connections
Check network and communication cables at accessible analyzer, workstation, or approved interface points. Confirm connectors are secure and show no visible damage.

**Expected outcome:** External communication cabling is intact and securely connected.

### 5. Check Analyzer and Workstation Status
Verify the analyzer and associated workstation show normal operation and no obvious communication-disabled condition. Do not change network configuration, IP information, or interface settings without authorization.

**Expected outcome:** Local analyzer and workstation operation is available for communication.

### 6. Determine Whether the Problem Is Analyzer-Specific
Ask whether other laboratory analyzers or workstations are communicating normally with the LIS. If several devices are affected, engage laboratory IT or interface support before assuming an analyzer failure.

**Expected outcome:** The issue is narrowed to the DxC 700 AU path or identified as a broader LIS/network problem.

### 7. Test the Communication Path With Approved Test Data
When permitted, use a non-patient or approved test record to verify barcode recognition, order receipt, and/or result transmission.

**Expected outcome:** Successful test communication confirms restoration of the path. Troubleshooting can stop after end-to-end verification.

### 8. Verify End-to-End Operation
Confirm information moves correctly through the complete intended path, including analyzer recognition, LIS receipt, and result handling as applicable.

**Expected outcome:** Reliable end-to-end communication is demonstrated without missing or mismatched data.

## If the Problem Persists

Barcode quality, external cabling, local workstation status, and obvious network-wide causes have been ruled out. The remaining issue may involve the analyzer interface, communication service, middleware, LIS configuration, network infrastructure, reader hardware, or software requiring coordinated technical support.

Remove the affected communication workflow from service and use the approved laboratory downtime process. Label the analyzer Out of Service if patient identification or result integrity cannot be maintained. Coordinate evaluation with qualified Clinical Engineering, laboratory IT, LIS/interface support, and Beckman Coulter service as appropriate.

Do not make unauthorized network or interface configuration changes. Return normal electronic workflow to service only after end-to-end communication is verified.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A result visible on the analyzer is not proof that it reached the LIS; verify the complete communication path before declaring the issue resolved.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Communication troubleshooting must protect patient identity and result integrity. Verify labels, external connections, and the complete analyzer-to-LIS path before assuming an internal failure, and coordinate escalation whenever network or interface-level support is required.

That is successful troubleshooting.
