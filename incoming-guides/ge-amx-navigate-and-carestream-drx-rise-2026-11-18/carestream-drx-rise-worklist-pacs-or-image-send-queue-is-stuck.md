---
schemaVersion: 1
title: "Carestream DRX-Rise Mobile X-Ray System - Worklist, PACS, or Image Send Queue Is Stuck"
issueTitle: "Worklist, PACS, or Image Send Queue Is Stuck"
description: "Troubleshoot missing worklists, queued images, PACS communication failures, network connection problems, and incorrect destination or workflow conditions."
assetType: "Mobile X-Ray System"
manufacturer: "Carestream"
model: "DRX-Rise"
slug: "carestream-drx-rise-worklist-pacs-or-image-send-queue-is-stuck"
dateAdded: "2026-11-18"
taxonomyMode: "reuse"
ccr:
  complaint: "Radiology reported that completed DRX-Rise images remained in the send queue and did not reach PACS."
  cause: "Clinical Engineering found the mobile system had lost its normal wireless network connection in the examination area."
  resolution: "Restored normal network connectivity, resent the queued study through the approved workflow, and confirmed successful receipt in PACS."
helpfulDetails:
  - "Worklist versus send failure"
  - "Exact communication message"
  - "Network connection status"
  - "Location where failure occurred"
  - "Other systems affected or unaffected"
  - "Number of queued studies"
  - "Selected destination"
  - "Retry results"
  - "PACS receipt confirmation"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoot missing worklists, queued images, PACS communication failures, network connection problems, and incorrect destination or workflow conditions.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow and Image Availability
Determine whether images needed for patient care are unavailable to radiology or the interpreting physician. Use the facility's approved alternate workflow when necessary.  
Expected outcome: Patient care does not depend on an unresolved network transfer problem.

### 2. Identify Which Communication Function Failed
Determine whether the issue affects worklist retrieval, image sending, all PACS communication, or only one destination. Record any displayed network or transfer message.  
Expected outcome: The failed communication path is clearly defined.

### 3. Verify Images Are Stored Locally
Confirm completed images remain available on the DRX-Rise before performing any troubleshooting that could affect queued data. Do not delete studies merely to clear a queue.  
Expected outcome: Patient images are preserved locally while communication is investigated.

### 4. Check Network Connection Status
Confirm the system shows its expected wired or wireless network connection and that no cable, adapter, dock, or accessible connection is loose or damaged.  
Expected outcome: The system has a normal physical or wireless network connection.

### 5. Verify Scope of the Problem
Determine whether other imaging systems in the same area can retrieve worklists or send images. This helps distinguish a DRX-Rise problem from a PACS, wireless, or hospital-network outage.  
Expected outcome: The issue is isolated to the mobile system or identified as a broader infrastructure problem.

### 6. Check Destination and Queue Status
Review the normal user-accessible send queue and selected destination. Look for one failed study blocking later transfers or an incorrect destination selection. Do not make unauthorized network or DICOM configuration changes.  
Expected outcome: The intended destination is selected and queue status is understood.

### 7. Retry Communication Through Normal Controls
Retry the failed worklist query or image transfer using the approved interface after confirming network connectivity. Avoid repeated uncontrolled retries that create duplicate sends.  
Expected outcome: Communication resumes and queued images transfer successfully. If so, verify receipt and stop.

### 8. Test in Another Known-Good Network Location When Appropriate
If the mobile unit normally roams between areas, compare behavior in another approved location with known working connectivity.  
Expected outcome: Testing helps isolate the issue to the device or local wireless/network environment.

### 9. Verify End-to-End Image Receipt
Confirm that a test or previously queued image reaches the intended destination and is associated with the correct patient/examination.  
Expected outcome: Successful end-to-end transfer is verified. Troubleshooting can stop.

### 10. Escalate Persistent Communication Failure
If local images are safe but worklist or PACS communication remains unavailable, escalate to the appropriate imaging informatics, PACS, network, or Carestream support team.  
Expected outcome: Service-level troubleshooting proceeds without risking stored patient data.

## If the Problem Persists

Common external connection and workflow causes have been ruled out. Remaining categories include hospital network infrastructure, wireless coverage, PACS availability, DICOM configuration, application software, interface services, or system communication hardware.

If normal clinical workflow cannot be maintained, remove the system from service or restrict it according to facility policy and label it appropriately. Evaluation should use approved Carestream and facility network documentation.

Any network, DICOM, software, or security configuration changes should be made only by authorized personnel.

Return to service should include successful worklist retrieval where applicable, image transmission, and destination receipt verification.

Knowing when to escalate an infrastructure or configuration problem rather than changing settings blindly is proper troubleshooting.

## Clinical Use Tip

Before clearing or restarting any transfer workflow, confirm that all acquired patient images are safely retained.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect stored images, isolate the device from the network or PACS infrastructure before changing configuration, verify the complete communication path, and document the final transfer result.

That is successful troubleshooting.
