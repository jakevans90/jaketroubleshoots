---
schemaVersion: 1
title: "Radiometer ABL90 FLEX PLUS Blood Gas Analyzer - Barcode, LIS, or Network Communication Fails"
issueTitle: "Barcode, LIS, or Network Communication Fails"
description: "Troubleshoot barcode, LIS, or network failures caused by labels, cables, ports, connectivity, configuration, middleware, or hospital infrastructure."
assetType: "Blood Gas Analyzer"
manufacturer: "Radiometer"
model: "ABL90 FLEX PLUS"
slug: "radiometer-abl90-flex-plus-barcode-lis-or-network-communication-fails"
dateAdded: "2026-10-07"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that the Radiometer ABL90 FLEX PLUS completed testing but results were not transmitting to the LIS."
  cause: "Clinical Engineering found the external network cable was partially disconnected at the analyzer."
  resolution: "Clinical Engineering reseated the network connection, verified restored connectivity and successful end-to-end result transmission, and returned the analyzer to normal workflow."
helpfulDetails:
  - "Exact communication or barcode symptom"
  - "Whether local analyzer operation was normal"
  - "Barcode condition and known-good test result"
  - "Network cable condition"
  - "Link-status indication"
  - "Other laboratory devices affected"
  - "Known-good cable or port comparison"
  - "Approved communication settings observed"
  - "LIS or middleware availability"
  - "End-to-end test result"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoot barcode, LIS, or network failures caused by labels, cables, ports, connectivity, configuration, middleware, or hospital infrastructure.

## Step-by-Step Troubleshooting

### 1. Protect Patient Identification and Result Reporting

Do not rely on an unreliable barcode or LIS connection for patient identification or automated result transmission. Follow the laboratory's approved downtime or manual-verification process.

Confirm whether the failure involves barcode reading, order retrieval, result transmission, network connectivity, or several functions.

**Expected outcome:** Patient identification and result reporting remain controlled while the exact communication problem is defined.

### 2. Verify the Analyzer Is Otherwise Functional

Confirm the ABL90 FLEX PLUS is initialized, ready, and capable of local operation without unrelated analytical or system faults.

**Expected outcome:** The problem is isolated to identification or communication rather than a broader analyzer failure.

### 3. Check the Barcode and Label

Inspect the affected barcode for wrinkles, smearing, poor contrast, damage, incorrect orientation, contamination, or placement that prevents reliable reading.

Test a known-good barcode when available.

**Expected outcome:** A known-good barcode reads successfully. If so, the original label or printing process is the likely cause and troubleshooting can stop for the analyzer.

### 4. Inspect Network and Communication Connections

Check externally accessible network or communication cables for loose connectors, broken latches, damage, severe bends, or disconnection.

If permitted by facility practice, reseat the cable at the analyzer and approved wall or network connection.

**Expected outcome:** Communication cabling is secure and undamaged. If connectivity returns, proceed to end-to-end verification.

### 5. Check Link and Connection Status

Observe available network or communication status indicators without entering unauthorized service menus. Determine whether the analyzer appears connected to the network.

Compare with other analyzers or devices on the same network segment when useful.

**Expected outcome:** The analyzer has an active physical connection. If multiple devices are affected, escalate to LIS, middleware, or IT support rather than assuming analyzer failure.

### 6. Isolate Analyzer Versus Infrastructure

Determine whether the issue affects only the ABL90 FLEX PLUS or also other laboratory devices.

Where approved, test the analyzer's external network cable or connection using a known-good equivalent or verified network port without altering network configuration.

**Expected outcome:** The failure is isolated to the analyzer connection, local cabling, or shared infrastructure.

### 7. Verify Approved Communication Configuration

Review user-accessible or institution-approved communication settings for obvious changes only if Clinical Engineering is authorized to do so. Compare against documented known-good configuration.

Do not guess IP addresses, LIS destinations, ports, or protected interface parameters.

**Expected outcome:** The analyzer configuration matches approved records. Any discrepancy is corrected only through authorized change control.

### 8. Perform End-to-End Verification

After correction, test the complete workflow as applicable: barcode identification, order receipt, test processing, result transmission, and receipt by the LIS or downstream system.

**Expected outcome:** Patient/sample identification and communication function correctly across the complete intended path. Troubleshooting can stop.

## If the Problem Persists

Barcode condition, external cabling, physical connectivity, local configuration, and obvious infrastructure issues have been ruled out. The remaining problem may involve the barcode reader, analyzer network hardware, LIS interface, middleware, switch configuration, firewall rules, routing, server availability, or another service-level system.

The analyzer should be removed from clinical communication service when safe patient identification or result transmission cannot be assured. Label it Out of Service if the analyzer cannot be safely used under approved downtime procedures.

Further evaluation should involve:

- Appropriate Radiometer service documentation.
- Clinical Engineering or qualified analyzer service personnel.
- Laboratory information-system support.
- Middleware support when applicable.
- Hospital IT/network staff when infrastructure is implicated.
- Approved test equipment and documented configuration records.

Do not make unauthorized network or interface changes. Complete end-to-end communication verification before normal workflow resumes.

Knowing when to stop external troubleshooting and escalate is proper troubleshooting.

## Clinical Use Tip

A result shown correctly on the analyzer is not proof that it reached the correct patient record; verify the complete analyzer-to-LIS communication path after repair.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Separate barcode, analyzer, cabling, network, middleware, and LIS causes logically before changing configuration. Protect patient identification, verify the entire communication path after correction, and document which portion of the system actually failed.

That is successful troubleshooting.
