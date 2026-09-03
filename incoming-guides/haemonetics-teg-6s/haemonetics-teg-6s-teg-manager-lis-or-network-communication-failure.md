---
schemaVersion: 1
title: "Haemonetics TEG 6s Viscoelastic Hemostasis Analyzer - TEG Manager, LIS, or Network Communication Failure"
issueTitle: "TEG Manager, LIS, or Network Communication Failure"
description: "Troubleshoots lost communication between the analyzer, TEG Manager, LIS, and network infrastructure using external connectivity and configuration checks first."
assetType: "Viscoelastic Hemostasis Analyzer"
manufacturer: "Haemonetics"
model: "TEG 6s"
slug: "haemonetics-teg-6s-teg-manager-lis-or-network-communication-failure"
dateAdded: "2026-09-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that TEG 6s results were available locally but were not appearing in TEG Manager or the LIS."
  cause: "Clinical Engineering found the analyzer Ethernet cable was not fully seated at the network connection."
  resolution: "Reseated the network cable, verified restored connectivity and successful end-to-end result transmission, and returned the analyzer to normal service."
helpfulDetails:
  - "Local result availability."
  - "TEG Manager status."
  - "LIS status."
  - "Ethernet link indication."
  - "Cable condition."
  - "Wall port tested."
  - "Known-good cable result."
  - "Other analyzers affected."
  - "Server or interface availability."
  - "Visible network configuration."
  - "End-to-end transmission result."
---
## What This Guide Helps With

Troubleshoots lost communication between the analyzer, TEG Manager, LIS, and network infrastructure using external connectivity and configuration checks first.

## Step-by-Step Troubleshooting

### 1. Protect the Result Reporting Workflow

If analyzer results are clinically required but electronic transmission is unavailable, use the laboratory's approved downtime or alternate reporting process.

Do not assume a result was delivered merely because testing completed locally.

**Expected outcome:** Results remain available to clinicians through a verified pathway while communication troubleshooting proceeds.

### 2. Define Where Communication Stops

Determine whether:
- The analyzer has a local result.
- TEG Manager receives the result.
- The LIS receives the result.
- Only patient or order information fails to arrive.
- All network communication is absent.
- Only one analyzer is affected.

**Expected outcome:** The failed segment of the communication path is identified.

### 3. Verify Analyzer Network Status

Inspect accessible network indicators and the analyzer's normal connection status display, if available.

Record any displayed connection message without changing configuration.

**Expected outcome:** The analyzer shows either an established connection or a clearly isolated network failure.

### 4. Inspect Ethernet Connections

If wired networking is used, verify:
- Cable is fully seated.
- Connector latch is intact.
- Cable is not crushed, cut, or damaged.
- Wall jack or network interface is secure.

Reseat accessible connections.

**Expected outcome:** Physical network connections are secure. If communication resumes, verify result transmission and stop troubleshooting.

### 5. Substitute a Known-Good Network Cable

Use a known-good compatible cable when practical.

**Expected outcome:** Communication is restored with the replacement cable, confirming the original cable was defective.

### 6. Verify the Network Port

Coordinate with IT or network support to confirm the connected port is active and assigned as intended.

Do not make unauthorized network changes.

**Expected outcome:** The port is active and appropriate for the analyzer. Infrastructure issues are escalated to the responsible team.

### 7. Compare Other Systems

Check whether:
- Other TEG 6s analyzers are communicating.
- Other devices on the same network segment are affected.
- TEG Manager or LIS is generally available.

**Expected outcome:** A device-specific failure is separated from a broader server or network outage.

### 8. Verify Approved Communication Configuration

Review visible network or interface settings against known-good documentation or another properly configured analyzer.

Do not change IP, server, interface, or protected communication parameters without authorization.

**Expected outcome:** No obvious configuration mismatch is identified, or an authorized configuration correction restores communication.

### 9. Perform End-to-End Verification

After corrective action, verify the entire intended pathway:
- Test or approved verification data exists locally.
- Data reaches TEG Manager if applicable.
- Data reaches the LIS if applicable.
- Patient/order association remains correct.

**Expected outcome:** Communication succeeds across the complete configured path. Troubleshooting can stop.

### 10. Escalate Unresolved Communication Failure

If cabling, network port, server availability, and approved configuration are verified but communication remains unavailable, escalate to the appropriate Clinical Engineering, IT, LIS, or vendor support path.

**Expected outcome:** The problem is transferred to the team responsible for the unresolved infrastructure, interface, or application layer.

## If the Problem Persists

External causes involving physical cabling, network port availability, server availability, interface path, and visible configuration have been ruled out. Remaining causes may involve internal network hardware, analyzer software, interface services, TEG Manager, LIS middleware, firewall rules, routing, or other infrastructure-level conditions.

The analyzer should be:
- Removed from service if communication failure prevents safe result identification or approved reporting.
- Labeled **Out of Service** when required.
- Sent for repair or bench evaluation if the analyzer itself is implicated.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Complete end-to-end communication verification before return to normal workflow.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Confirm the complete path from analyzer to receiving system; a locally displayed result does not prove that the clinician or LIS received it.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Local result availability.
- TEG Manager status.
- LIS status.
- Ethernet link indication.
- Cable condition.
- Wall port tested.
- Known-good cable result.
- Other analyzers affected.
- Server or interface availability.
- Visible network configuration.
- End-to-end transmission result.

## Final Thought

Troubleshoot the communication path in layers, starting at the physical connection and ending at the receiving application, verify end-to-end delivery, and escalate at the correct infrastructure boundary.

That is successful troubleshooting.
