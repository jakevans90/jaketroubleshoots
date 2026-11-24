---
schemaVersion: 1
title: "Mindray TE X Ultrasound System - Voice Control, DICOM, or Network Login Fails"
issueTitle: "Voice Control, DICOM, or Network Login Fails"
description: "Troubleshoots voice-control, DICOM, or login failures caused by connectivity, credentials, peripheral access, network availability, configuration, or infrastructure issues."
assetType: "Ultrasound System"
manufacturer: "Mindray"
model: "TE X"
slug: "mindray-te-x-voice-control-dicom-or-network-login-fails"
dateAdded: "2026-11-24"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the TE X could acquire images but could not retrieve the DICOM worklist or send completed studies."
  cause: "Clinical Engineering found the external network cable disconnected from the cart connection."
  resolution: "Clinical Engineering reconnected the network cable and verified network access, worklist retrieval, successful image transfer, and receipt at the configured destination."
helpfulDetails:
  - "Function that failed"
  - "Wired or wireless connection"
  - "Link or connection status"
  - "Login behavior"
  - "Whether other devices were affected"
  - "DICOM worklist result"
  - "Image-send result"
  - "Destination receipt confirmation"
  - "Voice-control behavior"
  - "Final workflow status"
---

## What This Guide Helps With

Troubleshoots voice-control, DICOM, or login failures caused by connectivity, credentials, peripheral access, network availability, configuration, or infrastructure issues.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow
If the failure prevents required imaging documentation, image transfer, or access to patient information, establish an approved alternate workflow before troubleshooting.

Expected outcome: Imaging and patient-data handling continue safely without relying on the failed function.

### 2. Identify the Failed Service
Determine whether the problem affects voice commands, network authentication, worklist, image transfer, storage destination, or multiple network-dependent functions.

Expected outcome: The failure is narrowed to a specific function or recognized as a broader connectivity problem.

### 3. Verify Basic TE X Operation
Confirm the ultrasound system is otherwise operating normally and is not frozen or displaying broader system errors. Perform a normal restart when clinically appropriate.

Expected outcome: The system boots normally and local imaging functions remain available.

### 4. Check Physical or Wireless Network Connection
For wired operation, inspect the external network cable and connector and confirm expected link indications when available. For wireless operation, confirm the intended network is selected and the system shows a usable connection through normal controls.

Expected outcome: The TE X has an active connection to the intended network.

### 5. Verify Credentials and Login Inputs
Confirm the user is using the appropriate current account, domain, or approved login workflow. Check for simple input errors such as incorrect capitalization or an expired credential without requesting or documenting passwords.

Expected outcome: Valid credentials are accepted. If the account fails on multiple systems, escalate to the appropriate IT or identity-management team.

### 6. Check Voice-Control Conditions
If voice control alone is affected, confirm the feature is enabled through normal controls and inspect accessible microphone openings or attached audio accessories for blockage, disconnection, or contamination. Test in a reasonably quiet environment.

Expected outcome: Voice commands are detected consistently. If only voice control fails while networking remains normal, isolate the issue from the network path.

### 7. Verify DICOM Destination and Worklist Availability
Using approved user-accessible controls, confirm the expected destination or worklist source is selected and determine whether other devices are experiencing the same outage. Do not alter network addresses or protected configuration without authorization.

Expected outcome: The intended destination is available, or the problem is identified as shared infrastructure rather than isolated TE X failure.

### 8. Compare With Known-Good Infrastructure
When practical, test the network drop, cable, or approved wireless environment with known-good equipment, or test the TE X on another approved connection without altering protected network configuration.

Expected outcome: The comparison separates system-level failure from network infrastructure failure.

### 9. Perform Final Workflow Verification
Confirm login, required voice-control function, worklist retrieval if applicable, image transfer, and receipt at the intended destination.

Expected outcome: The complete workflow operates correctly. If only partial communication is restored, continue escalation rather than returning the function to service.

## If the Problem Persists

Common external connection, login, accessory, network-selection, and shared-infrastructure causes have been checked. Remaining causes may include hospital network services, authentication systems, DICOM configuration, software, internal communication hardware, or service-level configuration.

Remove the TE X from service if the communication failure prevents safe or required clinical workflow and no approved workaround exists. Otherwise clearly document the unavailable feature and coordinate with IT, PACS, cybersecurity, or Mindray support as appropriate.

Use approved documentation and authorized configuration methods only. Following repair or configuration changes, verify the complete communication path before returning affected functions to service.

## Clinical Use Tip

A successful local image does not prove successful documentation; verify that required images actually reach the intended PACS or archive destination.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Separate local device operation from voice, authentication, and network services, check the external communication path first, and escalate configuration or infrastructure issues without making unauthorized changes.

That is successful troubleshooting.
