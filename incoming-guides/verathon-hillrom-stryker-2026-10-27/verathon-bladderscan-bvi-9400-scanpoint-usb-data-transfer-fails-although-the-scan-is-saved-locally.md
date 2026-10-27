---
schemaVersion: 1
title: "Verathon BladderScan BVI 9400 Bladder Scanner - ScanPoint/USB Data Transfer Fails Although the Scan Is Saved Locally"
issueTitle: "ScanPoint/USB Data Transfer Fails Although the Scan Is Saved Locally"
description: "Troubleshoots saved scans that will not transfer through ScanPoint or USB because of connections, computer recognition, workflow, configuration, or infrastructure."
assetType: "Bladder Scanner"
manufacturer: "Verathon"
model: "BladderScan BVI 9400"
slug: "verathon-bladderscan-bvi-9400-scanpoint-usb-data-transfer-fails-although-the-scan-is-saved-locally"
dateAdded: "2026-10-27"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that scans were saved on the BladderScan BVI 9400 but would not transfer to the ScanPoint workstation."
  cause: "Clinical Engineering found the USB data cable had an intermittent connection and the scanner disconnected when the cable was moved."
  resolution: "Clinical Engineering replaced the cable with a known-good compatible cable and verified that a test scan saved locally and transferred successfully to the authorized workstation."
helpfulDetails:
  - "Whether the scan remained available locally"
  - "Whether one or all scans were affected"
  - "ScanPoint or USB workflow involved"
  - "Workstation tested"
  - "USB port tested"
  - "Cable and connector condition"
  - "Device-recognition behavior"
  - "Known-good cable or workstation comparison"
  - "Accessible configuration observed"
  - "IT or application errors reported"
  - "Successful end-to-end transfer result"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots saved scans that will not transfer through ScanPoint or USB because of connections, computer recognition, workflow, configuration, or infrastructure.

## Step-by-Step Troubleshooting
### 1. Protect Patient Data and Maintain Clinical Workflow

Do not erase, overwrite, or repeatedly manipulate locally stored patient data while troubleshooting a transfer failure. Follow facility privacy and data-handling requirements.

If transferred results are required for immediate clinical workflow, provide an approved alternate documentation method while troubleshooting proceeds.

**Expected outcome:** Patient care and data integrity are preserved while the transfer problem is evaluated. If the scanner itself cannot reliably retain or display the scan, remove it from service and address that issue separately.

### 2. Confirm the Scan Is Actually Saved Locally

Using normal review functions, verify that the reported scan is present in local storage and can be opened or reviewed on the scanner.

Confirm whether the transfer problem affects:

- One saved scan
- All saved scans
- USB transfer only
- ScanPoint transfer only
- Every receiving computer

**Expected outcome:** The local scan is confirmed intact and the failure is isolated to the transfer path. If the scan was never saved, the issue is not a transfer failure and troubleshooting should follow the appropriate acquisition or storage workflow.

### 3. Inspect the External Data Connection

Inspect the applicable USB cable, data cable, connector, port, cradle, or communication accessory for:

- Loose connections
- Bent or damaged connector features
- Debris
- Cable damage
- Strain at the connector
- Incorrect cable placement

Reseat external connections securely.

**Expected outcome:** All external data connections are secure and undamaged. If reseating restores reliable transfer, repeat the transfer and troubleshooting can stop after verification.

### 4. Verify the Receiving Computer or Workstation Is Available

Confirm that the intended workstation is powered on and functioning normally.

For ScanPoint-related workflow, verify that the expected application environment is available to authorized staff and that no obvious application or computer error is preventing communication.

Do not change hospital security settings, drivers, firewall policies, or network configuration without authorization.

**Expected outcome:** The receiving workstation is available and ready for the intended transfer. If a workstation problem is identified, route that portion of the issue to the appropriate IT or application support team.

### 5. Verify USB Recognition

When USB is involved, connect the scanner or approved transfer accessory to the intended workstation and observe whether the operating system recognizes that a device has been connected.

Try another known-good approved USB port on the same workstation when permitted.

Avoid unapproved hubs or adapters during troubleshooting.

**Expected outcome:** The scanner or transfer interface is consistently recognized. If changing from a defective or unsuitable USB port restores transfer, verify another successful transfer and troubleshooting can stop.

### 6. Test a Known-Good USB Cable or Approved Interface Accessory

If the connection uses a removable cable, substitute a known-good compatible cable.

If the transfer depends on an approved cradle or interface accessory, inspect and compare with a known-good compatible accessory when available.

**Expected outcome:** The known-good accessory establishes reliable communication. If the failure follows the cable or external accessory, replace that component, verify successful transfer, and troubleshooting can stop.

### 7. Verify the Normal Transfer Workflow

Repeat the transfer using the facility's established workflow. Confirm the correct patient record or saved examination is selected and that the proper destination or transfer function is being used.

Do not modify configuration simply to make the transfer work unless the correct authorized configuration is known.

**Expected outcome:** The selected saved scan transfers normally through the established workflow. If correct workflow resolves the complaint, document the finding and troubleshooting can stop.

### 8. Compare With Another Authorized Workstation When Available

If facility policy permits, attempt transfer using another workstation known to support the same BVI 9400/ScanPoint workflow.

This helps separate a scanner-side issue from a workstation, USB, software, or local IT issue.

**Expected outcome:** The transfer either succeeds on the second workstation, indicating a workstation/infrastructure issue, or fails consistently with the scanner, indicating further device-side evaluation is needed.

### 9. Verify Configuration Without Unauthorized Changes

Review accessible communication or data-transfer settings and compare them with a known-good scanner when appropriate.

Record observed settings. Do not enter restricted service menus or alter network, software, or device configuration without approved documentation and authorization.

**Expected outcome:** The accessible configuration matches the expected operational setup. If an authorized configuration correction resolves the failure, perform another successful transfer and document the change.

### 10. Perform Final Data-Transfer Verification

After correction:

1. Save an appropriate test scan or test record.
2. Confirm it remains available locally.
3. Transfer it using the normal workflow.
4. Confirm it reaches the intended authorized destination.
5. Verify the transferred record corresponds to the correct test record.

**Expected outcome:** A locally saved record transfers successfully and is correctly received. Troubleshooting can stop when the complete data path has been verified.

### 11. Escalate Unresolved Communication Problems

If local storage operates correctly but transfer continues to fail after connections, cables, ports, workstation availability, workflow, and accessible configuration have been verified, escalate rather than attempting unauthorized software installation or internal hardware repair.

**Expected outcome:** The unresolved transfer problem is routed to the appropriate qualified service, IT, application support, or manufacturer resource.

## If the Problem Persists
Common external causes have been ruled out. Remaining possibilities may involve scanner communication hardware, ScanPoint software or licensing, workstation drivers, operating-system compatibility, device configuration, data-management services, or another IT/service-level condition.

The device should be removed from service if data transfer is required for its intended clinical workflow and an approved alternate process is not available. When removal is necessary, label it **Out of Service** and send it for repair or bench evaluation.

Evaluation should use appropriate manufacturer documentation and approved test equipment. Software, configuration, or hardware changes should be made only by qualified and authorized personnel.

After repair or configuration changes, verify the complete path from local scan storage through transfer to the intended destination before returning the workflow to service.

Knowing when a communication problem requires IT, application, or manufacturer escalation is proper troubleshooting.

## Clinical Use Tip
Verify the complete record path rather than stopping when the computer merely recognizes the scanner; confirm that the correct saved scan reaches the intended destination.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Preserve patient data first, then verify the scanner, cable, USB connection, workstation, workflow, and accessible configuration in order. Do not assume an internal device failure until the complete external communication path has been tested and documented.

That is successful troubleshooting.
