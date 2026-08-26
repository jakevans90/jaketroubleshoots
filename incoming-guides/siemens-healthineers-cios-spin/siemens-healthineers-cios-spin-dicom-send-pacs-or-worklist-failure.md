---
schemaVersion: 1
title: "Siemens Healthineers Cios Spin C-Arm - DICOM Send, PACS, or Worklist Failure"
issueTitle: "DICOM Send, PACS, or Worklist Failure"
description: "Addresses failed image transfer or worklist retrieval caused by network connectivity, destination availability, workflow selection, configuration, or infrastructure problems."
assetType: "C-Arm"
manufacturer: "Siemens Healthineers"
model: "Cios Spin"
slug: "siemens-healthineers-cios-spin-dicom-send-pacs-or-worklist-failure"
dateAdded: "2026-08-26"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported the Cios Spin could acquire images but studies remained pending and would not transmit to PACS."
  cause: "Clinical Engineering found the external Ethernet cable had been connected to an inactive wall network port after the system was moved."
  resolution: "The system was connected to the verified imaging-network port, pending images transmitted successfully, and receipt was confirmed at PACS."
helpfulDetails:
  - "DICOM function affected."
  - "PACS destination affected."
  - "Worklist availability."
  - "Exact send status or message."
  - "Ethernet cable condition."
  - "Wall port tested."
  - "Link indicator status."
  - "Recent system relocation."
  - "Other modalities affected."
  - "PACS or network team findings."
  - "Successful destination confirmation."
  - "Pending-study status."
  - "Final device status."
---

## What This Guide Helps With
Addresses failed image transfer or worklist retrieval caused by network connectivity, destination availability, workflow selection, configuration, or infrastructure problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Preserve Clinical Data
A DICOM or worklist problem usually does not require interruption of safe image acquisition, but do not assume images are archived merely because they are visible locally.

Ensure the clinical team understands the communication failure and follows the facility's approved process for retaining images and documenting patient information until connectivity is restored.

Do not delete unsent studies while troubleshooting.

**Expected outcome:** Clinical data are preserved and patient care can continue using the approved downtime workflow.

### 2. Confirm Which DICOM Function Is Failing
Determine whether the failure affects:
- Modality worklist retrieval.
- PACS image send.
- All destinations.
- One specific destination.
- One study only.
- All new studies.
- Connectivity after system relocation.
- Query/retrieve or another configured workflow.

Record any displayed failure message exactly.

**Expected outcome:** The issue is narrowed to a specific DICOM function or destination.

### 3. Verify the Local Network Connection
Inspect the Cios Spin's accessible network connection.

Check:
- Ethernet cable seating.
- Cable damage.
- Wall jack connection.
- Accessible link/activity indicators.
- Whether the system was recently moved to a different room or port.

Use a known-good approved network cable or known-good port comparison when appropriate and authorized.

**Expected outcome:** A valid physical network link is present. If restoring the connection restores DICOM service, proceed to end-to-end verification.

### 4. Confirm Other System Communication Is Normal
Verify the Cios Spin is otherwise operating normally and that workstation communication is stable.

If local workstation or system communication is also failing, address that broader system issue before focusing on PACS.

**Expected outcome:** The problem is isolated to network/DICOM communication rather than a general workstation failure.

### 5. Verify Patient and Workflow Selection
Confirm that the correct patient, exam, and destination workflow were selected.

For worklist problems, confirm search criteria or filters are not unintentionally excluding the expected patient.

Do not create duplicate patient records simply to bypass a worklist problem unless the facility's approved downtime workflow requires it.

**Expected outcome:** User-level workflow conditions are not blocking worklist retrieval or image sending.

### 6. Determine Whether the Problem Is Device-Specific
When possible, compare with another networked imaging device on the same network area or confirm with PACS/IT personnel whether the destination is available.

If multiple modalities cannot reach the same PACS or worklist service, the issue is likely infrastructure-side rather than specific to the Cios Spin.

**Expected outcome:** The failure is localized to the Cios Spin or identified as a broader network/PACS issue.

### 7. Review Operator-Accessible DICOM Status
Check the system's accessible send queue, study status, or communication indicators where available.

Determine whether studies are:
- Pending.
- Failed.
- Waiting for a destination.
- Repeatedly retrying.

Do not alter DICOM AE titles, addresses, ports, or protected network configuration unless the change is authorized and based on verified configuration records.

**Expected outcome:** The communication state is understood without introducing configuration changes.

### 8. Coordinate Infrastructure Checks
If the physical network connection is valid, coordinate with PACS or network support to verify:
- Destination service availability.
- Network port status.
- VLAN or routing availability where applicable.
- Whether network changes were recently made.
- Whether the modality is reaching the destination.

Clinical Engineering should provide the device identity and observed behavior without guessing at network configuration.

**Expected outcome:** Infrastructure-side problems are identified or ruled out.

### 9. Perform End-to-End DICOM Verification
After correction, perform the appropriate approved test:
- Retrieve the expected worklist.
- Send a test or approved study.
- Confirm receipt at the intended PACS or destination.
- Confirm patient and study information are correct.
- Verify pending studies transmit successfully when appropriate.

**Expected outcome:** DICOM communication completes end to end. Troubleshooting can stop.

### 10. Escalate Unresolved Device-Side DICOM Problems
If the network path and destination are verified but the Cios Spin still cannot retrieve worklists or send images, escalate for service-level network or DICOM configuration evaluation.

Do not perform undocumented configuration changes or factory resets.

**Expected outcome:** The device is appropriately restricted or removed from service if required by facility workflow until reliable image transfer is restored.

## If the Problem Persists
Once the physical network, workflow, destination availability, and infrastructure have been ruled out, remaining causes may involve DICOM configuration, software services, network-interface hardware, stored credentials or certificates where applicable, or service-level system configuration.

The Cios Spin should be:
- Removed from service or placed under an approved imaging-downtime workflow as required by facility policy.
- Labeled appropriately if not clinically usable.
- Sent for qualified evaluation when the failure is device-side.
- Evaluated using Siemens Healthineers documentation and authorized network/PACS tools.
- Configured only by qualified personnel using verified site parameters.

Before normal use resumes, confirm both image transfer and worklist functionality as applicable and ensure required studies have reached their intended destination.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
A locally saved image is not the same as a successfully archived image; verify PACS receipt before considering the transfer problem resolved.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**


## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Preserve clinical data, verify the physical network and workflow before changing configuration, coordinate appropriately with IT or PACS teams, and confirm the complete DICOM path before closing the work order.

That is successful troubleshooting.
