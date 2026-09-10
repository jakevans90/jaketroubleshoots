---
schemaVersion: 1
title: "Philips Lumify Ultrasound System - DICOM Connection, Worklist, or PACS Transfer Failure"
issueTitle: "DICOM Connection, Worklist, or PACS Transfer Failure"
description: "Troubleshoot Lumify DICOM, worklist, and PACS communication failures by checking network access, destinations, patient data, configuration, and infrastructure."
assetType: "Ultrasound System"
manufacturer: "Philips"
model: "Lumify"
slug: "philips-lumify-dicom-connection-worklist-or-pacs-transfer-failure"
dateAdded: "2026-09-10"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Lumify system connected to wireless networking but could not retrieve the DICOM worklist."
  cause: "Clinical Engineering found the mobile device was connected to a different wireless network than the approved clinical network."
  resolution: "Clinical Engineering connected the device to the approved network and verified successful worklist retrieval and PACS transfer of a test study."
helpfulDetails:
  - "Whether worklist, transfer, or both failed"
  - "Exact application message"
  - "Wireless network connected"
  - "Whether other devices are affected"
  - "DICOM destination selected"
  - "Patient information present"
  - "Worklist test result"
  - "Transfer test result"
  - "Known-good device comparison"
  - "Receiving-system confirmation"
  - "Final equipment status"
---

## What This Guide Helps With
Troubleshoot Lumify DICOM, worklist, and PACS communication failures by checking network access, destinations, patient data, configuration, and infrastructure.

## Step-by-Step Troubleshooting
### 1. Protect Patient Workflow and Preserve Studies
Do not delete locally retained studies because PACS transfer is failing. If imaging must continue, follow the facility's approved downtime or alternate imaging workflow.

Expected outcome: Patient care continues and acquired studies remain protected while connectivity is evaluated.

### 2. Identify the Failed DICOM Function
Determine whether the failure affects worklist retrieval, image transfer, or both.

Record any displayed message and confirm whether the problem affects every patient or only one exam.

Expected outcome: The failed portion of the DICOM workflow is clearly identified.

### 3. Verify Mobile Device Network Connection
Confirm that the Lumify mobile device is connected to the expected approved network and that the connection is stable.

Verify that airplane mode, disabled wireless networking, or connection to an unintended network is not the cause.

Expected outcome: The mobile device is connected to the correct network. If restoring the approved network resolves DICOM communication, verify the complete workflow and troubleshooting can stop.

### 4. Determine Whether the Problem Is Device-Specific
Check whether other approved devices or systems on the same network can communicate with the same clinical destination when that information is available.

Do not make infrastructure changes based solely on one device failure.

Expected outcome: The problem is narrowed to Lumify or identified as a broader network, PACS, or interface issue.

### 5. Verify Patient and Exam Information
For study-transfer problems, confirm that required patient and examination information is present and correctly entered or selected from the worklist.

Do not alter clinical data merely to force a transfer.

Expected outcome: The study contains the information required by the normal workflow.

### 6. Review Normal DICOM Destination Selection
Confirm that the intended configured worklist or PACS destination is selected within authorized user-accessible settings.

Compare with another known-good Lumify configuration if available rather than changing unknown values.

Expected outcome: The correct approved destination is selected. If an incorrect destination selection caused the problem, restore the approved selection and verify communication.

### 7. Test Worklist and Transfer Separately
Attempt an approved worklist query. Separately, send a nonpatient test study or approved existing test object when permitted.

Expected outcome: Testing determines whether inbound worklist communication, outbound study transfer, or both are affected.

### 8. Compare With a Known-Good System
If available, compare the affected Lumify device with another working system on the same network and destination.

Document differences such as network connection, application configuration, or destination selection without copying settings blindly.

Expected outcome: The comparison identifies a likely device-specific configuration or infrastructure difference.

### 9. Verify the Complete Clinical Path
After correction, retrieve an approved test worklist entry when applicable, acquire or select a test study, send it, and confirm receipt at the receiving system.

Expected outcome: Worklist and transfer functions complete successfully end to end. Troubleshooting can stop.

### 10. Escalate Persistent Communication Failure
If the network is connected and the approved Lumify configuration appears correct but communication still fails, stop external troubleshooting and involve the appropriate IT, PACS, network, or Philips support resource.

Expected outcome: The problem is escalated with enough technical detail to continue infrastructure or service-level evaluation.

## If the Problem Persists
External device and workflow causes have been ruled out. Remaining possibilities include network segmentation, firewall rules, PACS availability, DICOM configuration, credentials or certificates, application-level communication faults, or other infrastructure conditions.

Remove the device from service if required clinical transfer cannot be performed safely under the facility workflow. Label it Out of Service when appropriate and send it for bench or configuration evaluation. Use appropriate Philips documentation, approved network tools, and organizational IT procedures. Network or DICOM configuration changes should be completed only by authorized personnel.

Before return to service, verify the full communication path from Lumify through the intended receiving system. Proper troubleshooting includes recognizing when the problem has moved beyond the device itself.

## Clinical Use Tip
A successful network connection does not prove the complete DICOM path is working; verify the study at the actual receiving destination.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought
DICOM troubleshooting should follow the entire communication path. Confirm the device, network, workflow, and destination before assuming internal failure, and involve infrastructure teams when the evidence points beyond the ultrasound system.

That is successful troubleshooting.
