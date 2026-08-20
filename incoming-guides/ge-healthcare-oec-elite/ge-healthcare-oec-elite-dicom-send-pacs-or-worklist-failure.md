---
schemaVersion: 1
title: "GE Healthcare OEC Elite C-Arm - DICOM Send, PACS, or Worklist Failure"
issueTitle: "DICOM Send, PACS, or Worklist Failure"
description: "Troubleshoots image-send or worklist problems caused by network connectivity, destination availability, patient data, configuration, or infrastructure issues."
assetType: "C-Arm"
manufacturer: "GE Healthcare"
model: "OEC Elite"
slug: "ge-healthcare-oec-elite-dicom-send-pacs-or-worklist-failure"
dateAdded: "2026-08-20"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that studies from the OEC Elite remained local and were not reaching PACS."
  cause: "Clinical Engineering found the external network cable disconnected from the workstation network port."
  resolution: "The network connection was restored and a test study was successfully transmitted and confirmed at PACS."
helpfulDetails:
  - "DICOM send, worklist, or both affected"
  - "Whether all studies are affected"
  - "Local image availability"
  - "Network cable condition"
  - "Link/activity indication"
  - "Other modalities affected"
  - "PACS or worklist service status"
  - "Patient/exam data reviewed"
  - "Authorized configuration observed"
  - "Test transmission result"
  - "Destination confirmation"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots image-send or worklist problems caused by network connectivity, destination availability, patient data, configuration, or infrastructure issues.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow and Image Availability
Confirm images needed for immediate care remain available locally and notify clinical staff when PACS or worklist functionality is unavailable. Use the facility-approved alternate workflow for patient identification or image transfer when necessary.

**Expected outcome:** Patient care and image retention continue while the communication issue is investigated.

### 2. Define the Communication Failure
Determine whether the problem affects DICOM image send, modality worklist, both functions, or only one destination. Confirm whether all studies fail or only a particular patient or exam.

**Expected outcome:** The network problem is narrowed to a specific workflow.

### 3. Verify Local System Operation
Confirm the OEC Elite is otherwise functioning normally and images can be acquired, displayed, and retained locally as expected.

**Expected outcome:** The issue is confirmed as communication-related rather than a general workstation failure.

### 4. Check the Physical Network Connection
Inspect the network cable and accessible connection point for looseness, damage, broken latches, or disconnection. Verify the cable is connected to the intended network port.

**Expected outcome:** A valid physical network connection is present. If correcting the connection restores communication, proceed to final verification.

### 5. Check Link Status
Where externally visible, verify normal network link/activity indication at the device or network port. Compare with facility standards without altering switch configuration.

**Expected outcome:** The physical network path appears active.

### 6. Confirm the Scope of the Outage
Check with clinical staff or IT whether PACS, worklist, or other modalities are experiencing the same issue. Determine whether the destination service is currently available.

**Expected outcome:** The problem is identified as either local to the OEC Elite or part of a broader infrastructure outage.

### 7. Verify Patient and Exam Information
For failures affecting an individual study, confirm required patient and exam information is present and correctly entered. Do not alter completed clinical data without following facility procedures.

**Expected outcome:** The study contains the information needed for normal transmission.

### 8. Review Approved Network and DICOM Configuration
Compare operator-visible or approved configuration information with the facility's documented values. Do not change IP settings, DICOM destinations, application entities, ports, or service-level configuration without authorization.

**Expected outcome:** No obvious configuration discrepancy is identified, or an authorized correction restores communication.

### 9. Perform a Controlled Communication Test
Send an approved test study or repeat an authorized worklist query and verify receipt at the intended destination with the appropriate clinical or IT team.

**Expected outcome:** DICOM send or worklist functionality completes successfully. Troubleshooting can stop once the complete path is verified.

### 10. Escalate Persistent Network or DICOM Failure
If physical connectivity is normal but communication still fails, coordinate with PACS, networking, or vendor support as appropriate.

**Expected outcome:** The unresolved device-versus-infrastructure issue is escalated with useful test results rather than speculative configuration changes.

## If the Problem Persists
Common local cable, connectivity, patient-data, destination-availability, and approved configuration causes have been ruled out. Remaining possibilities may involve network infrastructure, firewall or routing behavior, PACS services, DICOM configuration, application software, or device network hardware.

If local clinical operation is otherwise safe, disposition should follow facility policy for systems with unavailable connectivity. If loss of communication prevents safe workflow or required image retention, remove the OEC Elite from service and label it **Out of Service** until the issue is corrected.

Evaluate using appropriate GE Healthcare documentation and coordinate with PACS and network personnel. Only authorized personnel should change network or DICOM configuration. Verify successful end-to-end transfer before return to normal workflow. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
A successful network link does not prove DICOM operation; verify that the intended study actually arrives at the correct PACS destination.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Preserve images and clinical workflow first, then verify the complete path from physical network connection through patient data and destination availability before assuming a device failure. Coordinate infrastructure escalation appropriately and document end-to-end verification.

That is successful troubleshooting.
