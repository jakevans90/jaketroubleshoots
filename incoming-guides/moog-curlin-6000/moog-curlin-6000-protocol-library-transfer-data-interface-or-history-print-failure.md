---
schemaVersion: 1
title: "Moog CURLIN 6000 Infusion Pump - Protocol Library Transfer, Data Interface, or History Print Failure"
issueTitle: "Protocol Library Transfer, Data Interface, or History Print Failure"
description: "Troubleshoots transfer, interface, or history-print failures caused by cables, connected equipment, communication setup, power, software state, or infrastructure."
assetType: "Infusion Pump"
manufacturer: "Moog"
model: "CURLIN 6000"
slug: "moog-curlin-6000-protocol-library-transfer-data-interface-or-history-print-failure"
dateAdded: "2026-09-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported the CURLIN 6000 history would not print through the normal workstation connection."
  cause: "Clinical Engineering found the communication cable was damaged and the pump completed the same workflow normally with a known-good cable."
  resolution: "Replaced the damaged cable, verified successful history printing through the approved workstation setup, and returned the pump to service."
helpfulDetails:
  - "Exact failed function"
  - "Displayed message"
  - "Pump power state"
  - "Cable and connector condition"
  - "Workstation or printer used"
  - "Interface hardware involved"
  - "Known-good cable result"
  - "Comparison-pump result"
  - "Configuration observed"
  - "Whether the failure was pump-specific or infrastructure-wide"
  - "Successful final workflow test"
  - "Final device status"
---
## What This Guide Helps With
Troubleshoots transfer, interface, or history-print failures caused by cables, connected equipment, communication setup, power, software state, or infrastructure.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Therapy and Data
Do not interrupt active patient therapy solely to troubleshoot a communication or printing problem. Use another verified pump if technical work requires disconnecting or reconfiguring the device.

**Expected outcome:** Therapy and clinically relevant data are protected before technical troubleshooting begins.

### 2. Confirm the Exact Function That Failed
Identify whether the failure involves protocol-library transfer, a data interface, history retrieval, or history printing. Record any displayed message and determine what connected computer, interface, printer, cable, or application was involved.

**Expected outcome:** The failed portion of the workflow is clearly identified rather than treating all communication problems as a pump failure.

### 3. Check Pump Power and Basic Operation
Confirm the pump starts normally and remains stable. A communication fault should not be investigated until basic device operation is reliable.

**Expected outcome:** The pump operates normally apart from the reported data function. If broader pump instability is present, remove it from service and address that condition first.

### 4. Inspect External Cables and Connections
Inspect communication cables, adapters, connectors, and accessible ports for looseness, bent contacts, contamination, damage, or incorrect connection. Reseat only connections intended for routine use.

**Expected outcome:** The physical communication path is secure and undamaged. If reseating an external connection restores operation, troubleshooting can stop after verification.

### 5. Verify the Connected Device or Application
Confirm the intended computer, printer, interface hardware, or approved software is powered, available, and not displaying an obvious communication problem. Do not modify institutional network or application configuration without authorization.

**Expected outcome:** The receiving or sending system is available for communication. If the problem lies with the external system, route it to the appropriate support group.

### 6. Substitute Known-Good External Components
When available, use a known-good cable, adapter, printer connection, or approved interface path to determine whether the failure follows an accessory.

**Expected outcome:** A successful transfer or print with the known-good component isolates the original accessory as the cause.

### 7. Compare With Another Compatible Pump
If appropriate, test the same external communication setup with another verified compatible CURLIN 6000. This helps distinguish pump-specific faults from application, cable, printer, or infrastructure problems.

**Expected outcome:** If multiple pumps fail on the same connection, investigate the external system or infrastructure. If only one pump fails, continue pump-specific evaluation.

### 8. Verify Authorized Configuration
Confirm observable communication settings and workflow selections are consistent with the institution's approved configuration. Do not change protected settings, protocol libraries, drug libraries, or communication parameters without authorization and change control.

**Expected outcome:** No obvious unauthorized or incorrect configuration explains the failure. If an approved configuration correction is required, route it through the appropriate process.

### 9. Retest the Complete Workflow
Repeat the originally failed transfer, interface, or print process using known-good external components and the approved configuration.

**Expected outcome:** The complete workflow succeeds consistently. If successful, troubleshooting can stop.

### 10. Escalate Unresolved Communication Failure
If the pump alone continues to fail after external cables, connected devices, and approved configurations are verified, remove it from service as appropriate to local policy and send it for technical evaluation.

**Expected outcome:** A pump-specific interface or software fault is isolated without unauthorized internal troubleshooting.

## If the Problem Persists
External cables, connectors, computers, printers, interface equipment, and basic approved configuration have been evaluated. Remaining causes may involve pump communication hardware, software, institutional interface infrastructure, application configuration, or other service-level conditions.

When pump-specific failure is suspected, remove the device from service, label it **Out of Service**, and send it for repair or bench evaluation. Use appropriate manufacturer documentation and approved test equipment. Network, library, and interface configuration changes should be performed only by authorized qualified personnel. Verify the complete communication workflow before return to service.

Recognizing when the problem belongs to the pump, application, interface, or infrastructure is proper troubleshooting.

## Clinical Use Tip
A successful pump-to-computer connection is not enough; verify the complete data path through the intended destination when the complaint involves transfer or documentation.

## Work Order Documentation (CCR Method)
<!-- CCR examples come from front matter; optional explanatory prose may follow. -->



## Helpful Details to Include (If Known)
<!-- rendered from front matter -->

## Final Thought
Troubleshoot the entire communication chain from the external connection outward, preserve approved configuration control, and isolate pump faults from workstation or infrastructure problems before escalating.

That is successful troubleshooting.
