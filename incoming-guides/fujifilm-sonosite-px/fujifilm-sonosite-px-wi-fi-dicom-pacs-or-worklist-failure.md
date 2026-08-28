---
schemaVersion: 1
title: "Fujifilm Sonosite PX Ultrasound System - Wi-Fi, DICOM, PACS, or Worklist Failure"
issueTitle: "Wi-Fi, DICOM, PACS, or Worklist Failure"
description: "Troubleshoots failed network connection, worklist retrieval, or image transmission caused by connectivity, configuration, destination availability, or infrastructure."
assetType: "Ultrasound System"
manufacturer: "Fujifilm Sonosite"
model: "PX"
slug: "fujifilm-sonosite-px-wi-fi-dicom-pacs-or-worklist-failure"
dateAdded: "2026-08-28"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the SonoSite PX could image patients but could not send studies to PACS."
  cause: "Clinical Engineering found the external network cable connection was loose, while local image storage and system operation were normal."
  resolution: "Reseated the network connection, sent a controlled test image, confirmed receipt at PACS, and returned the system to normal service."
helpfulDetails:
  - "Wi-Fi or wired connection"
  - "Network location or room"
  - "Worklist versus image transmission"
  - "Destination affected"
  - "Network cable condition"
  - "Connection status"
  - "Other modalities affected"
  - "Configuration reviewed"
  - "PACS/IT contacts involved"
  - "Test study or image sent"
  - "Receipt confirmed"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots failed network connection, worklist retrieval, or image transmission caused by connectivity, configuration, destination availability, or infrastructure.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Preserve Images

If network functions fail during clinical use, ensure images remain locally available and follow the facility's approved downtime or alternate documentation workflow.

Do not delete studies or repeatedly modify network settings while trying to restore transmission.

**Expected outcome:** Patient imaging data is preserved and clinical workflow can continue safely.

### 2. Identify Which Network Function Failed

Determine whether the problem involves:

- Wi-Fi connection
- Wired LAN connection
- Worklist retrieval
- DICOM image transmission
- PACS destination
- All network functions
- One destination only
- One room or wireless location only

**Expected outcome:** The failure is narrowed to network access, worklist, transmission, or a specific destination.

### 3. Confirm the Ultrasound System Otherwise Operates Normally

Verify:

- Normal startup
- Imaging functionality
- Local image storage
- Controls
- Patient study creation

**Expected outcome:** The problem is isolated to communications rather than a broader system malfunction.

### 4. Check Physical Network Connections When Wired

For wired operation:

- Inspect the network cable
- Confirm connectors are fully seated
- Check the wall jack or network connection
- Substitute a known-good approved cable when available
- Observe normal user-accessible connection indicators if present

**Expected outcome:** A secure physical network path exists. If replacing or reseating the cable restores communication, continue to end-to-end verification.

### 5. Check Wi-Fi Connection Status

For wireless operation, verify the PX shows connection to the intended facility wireless network through normal user-accessible status information.

Compare behavior in another known-good wireless area if the failure appears location dependent.

Do not create unauthorized hotspots or connect patient equipment to unapproved networks.

**Expected outcome:** The system connects to the intended approved network or the failure is isolated to wireless access.

### 6. Verify Basic Network Configuration

Review authorized user-accessible network information and compare it with the facility's documented configuration.

Check for obvious issues involving:

- Network selection
- IP addressing method
- Addressing information
- Gateway
- DICOM destination
- Worklist destination

Do not guess values or change production configuration without approved information.

**Expected outcome:** The system configuration matches the approved network design or a discrepancy is identified for correction by authorized personnel.

### 7. Determine Whether Other Devices Are Affected

Check with clinical users or appropriate IT/PACS personnel to determine whether:

- Other ultrasound systems can retrieve worklists
- Other modalities can send to the same PACS
- The affected location has a broader network outage
- The DICOM or worklist destination is available

**Expected outcome:** The problem is isolated to the PX or identified as an infrastructure/service issue.

### 8. Test Worklist and Transmission Separately

If possible:

- Attempt worklist retrieval
- Acquire and locally store a nonclinical test image according to facility practice
- Send the test image to the configured destination

**Expected outcome:** The specific failing communication path is identified rather than assuming all DICOM functions are down.

### 9. Verify Destination and Study Selection

Confirm the correct configured destination is selected and the intended study is queued or selected appropriately for transmission.

Do not resend large numbers of patient studies indiscriminately.

**Expected outcome:** The intended image is sent to the correct destination without duplication.

### 10. Perform a Controlled Restart if Appropriate

After confirming infrastructure and configuration, perform a normal restart of the PX when it is not supporting active patient care.

**Expected outcome:** Network services reconnect normally and remain available.

### 11. Confirm End-to-End Communication

After correction:

- Verify network connection
- Retrieve the worklist if applicable
- Send a controlled test image
- Confirm receipt at the intended PACS or receiving system
- Confirm no unintended duplicate or wrong-destination transmission

**Expected outcome:** The complete communication path works from the PX to the intended destination. Troubleshooting can stop when end-to-end operation is verified.

## If the Problem Persists

If cables, Wi-Fi access, basic configuration, destination selection, local operation, and infrastructure status have been checked, the remaining cause may involve DICOM configuration, certificates/security, network services, PACS/worklist infrastructure, application software, or internal network hardware.

The device or communication path should be:

- Removed from network-dependent clinical use if required workflow cannot be safely completed
- Labeled Out of Service when appropriate
- Sent for bench evaluation when a device fault is suspected
- Evaluated using appropriate Fujifilm SonoSite documentation and approved network/test tools
- Repaired or configured only by qualified Clinical Engineering, IT, PACS, or vendor personnel as appropriate

Avoid undocumented network changes or service-menu modifications.

Following correction, verify the complete worklist and/or image transmission workflow before return to normal service.

Knowing when to stop device troubleshooting and involve IT, PACS, or vendor support is proper troubleshooting.

## Clinical Use Tip

A successful network connection alone is not enough; verify the complete path through worklist retrieval or confirmed PACS receipt as applicable.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Network troubleshooting should separate physical connectivity, device configuration, and hospital infrastructure before internal failure is assumed. Always verify the complete communication path and clearly document where the failure was found.

That is successful troubleshooting.
