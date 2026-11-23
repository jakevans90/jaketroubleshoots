---
schemaVersion: 1
title: "GE Healthcare OEC One CFD C-Arm - Workstation, DICOM, or Image Export Communication Fails"
issueTitle: "Workstation, DICOM, or Image Export Communication Fails"
description: "Use this guide when worklist, PACS transfer, DICOM communication, workstation communication, or image export does not complete normally."
assetType: "C-Arm"
manufacturer: "GE Healthcare"
model: "OEC One CFD"
slug: "ge-healthcare-oec-one-cfd-workstation-dicom-or-image-export-communication-fails"
dateAdded: "2026-11-23"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that images from the OEC One CFD remained in the send queue and were not reaching PACS."
  cause: "Clinical Engineering found the external Ethernet cable disconnected from the workstation network connection."
  resolution: "Clinical Engineering reconnected the cable and verified the queued study transferred successfully and was received in PACS."
helpfulDetails:
  - "Communication function affected"
  - "Exact message displayed"
  - "Local image storage status"
  - "Wired or wireless connection status"
  - "Cable and network-jack condition"
  - "Network indicator status"
  - "Destination affected"
  - "Queue status"
  - "Whether other devices on the same network path work"
  - "Transfer result after correction"
  - "Final device status"
---

## What This Guide Helps With

Use this guide when worklist, PACS transfer, DICOM communication, workstation communication, or image export does not complete normally.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow and Preserve Images

Do not delete studies, repeatedly resend large queues, or change network configuration during an active case without understanding the impact. Ensure required images remain stored locally and communicate any delay in image availability.

Expected outcome: Clinical images are preserved and an alternate workflow is established if immediate image access is required.

### 2. Identify Which Communication Function Failed

Determine whether the problem affects modality worklist, PACS send, image export, workstation communication, removable media, or all network functions. Record any displayed message and whether the failure affects one destination or multiple destinations.

Expected outcome: The communication failure is isolated to a specific function or path.

### 3. Verify Basic System Operation

Confirm that the imaging workstation is otherwise operating normally and that studies can be acquired, reviewed, and stored locally.

Expected outcome: Local imaging functions operate normally. If the entire workstation is unstable, troubleshoot the workstation problem before focusing on DICOM.

### 4. Inspect External Network Connections

Check the Ethernet cable, network jack, docking or interface connection if applicable, and visible connector indicators. Reseat accessible connections and inspect for damaged locking tabs, bent contacts, or crushed cables.

Expected outcome: The physical network connection is secure. If communication resumes after correcting the external connection, verify successful transfer and stop troubleshooting.

### 5. Test the Facility Network Path

Use approved hospital network troubleshooting methods to determine whether the associated wall port, switch path, or network segment is available. Compare with a known-good device or approved test connection when practical.

Expected outcome: The facility network path is available. If the port or infrastructure is unavailable, escalate to the appropriate IT or network team rather than altering the C-arm.

### 6. Verify Normal Network Configuration Without Changing It

Review user-accessible network status and confirm the system is using the expected connection. Record relevant configuration information if available, but do not change IP, routing, DICOM, wireless, or security settings without authorization.

Expected outcome: No obvious configuration mismatch is identified. If the configuration is incorrect, coordinate correction through the approved service or IT process.

### 7. Determine Whether One Destination or All Destinations Fail

Test an approved worklist server, PACS destination, or export path as appropriate. A failure limited to one destination often points away from the C-arm's general network interface.

Expected outcome: The problem is narrowed to a specific destination or to all communications.

### 8. Check Queue and Study Status

Review the normal user-accessible send queue or study status for pending, failed, or held images. Do not delete unsent clinical data merely to clear the queue.

Expected outcome: The status of affected studies is known. If retrying after restoration of network connectivity successfully transmits the study, troubleshooting can stop.

### 9. Perform an End-to-End Verification

After correcting any external network or workflow issue, acquire or select an approved test study and verify the complete path from the OEC One CFD through the expected destination.

Expected outcome: Worklist retrieval, image transfer, or export completes successfully and the destination confirms receipt.

### 10. Escalate Persistent Communication Failure

If external cabling, network availability, destination status, and normal workflow settings appear correct but communication still fails, avoid unauthorized network or protected DICOM configuration changes.

Expected outcome: The problem is escalated with sufficient information for Clinical Engineering, IT, PACS, or vendor service to continue efficiently.

## If the Problem Persists

External network connections, local workstation operation, destination availability, and basic communication workflow have been checked. The remaining issue may involve DICOM configuration, network security, application services, software, routing, workstation communication components, or hospital infrastructure.

Remove the device from service only if the communication failure prevents safe or required clinical use; otherwise follow facility policy for restricted operation. Label it appropriately when unavailable for intended use and send it for repair or bench evaluation when equipment-side failure is suspected.

Use appropriate GE Healthcare documentation and approved network test methods. Protected network or DICOM configuration should be changed only by qualified and authorized personnel.

Before full return to service, verify the complete communication path and confirm required images are received at the intended destination.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A successful image acquisition does not prove PACS communication is working; verify receipt at the destination before closing the work order.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Preserve clinical images, isolate the communication path logically, check physical and infrastructure causes before configuration, verify the destination received the data, and document escalation clearly.

That is successful troubleshooting.
