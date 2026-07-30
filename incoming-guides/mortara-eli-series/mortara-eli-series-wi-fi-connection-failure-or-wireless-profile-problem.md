---
schemaVersion: 1
title: "Mortara ELI Series Electrocardiograph (EKG) Machine - Wi-Fi Connection Failure Or Wireless Profile Problem"
issueTitle: "Wi-Fi Connection Failure Or Wireless Profile Problem"
description: "Troubleshooting wireless connection failure caused by signal, profile, credentials, network availability, configuration, time, or infrastructure problems."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "Mortara"
model: "ELI Series"
slug: "mortara-eli-series-wi-fi-connection-failure-or-wireless-profile-problem"
dateAdded: "2026-07-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Mortara ELI Series EKG machine would not connect to the hospital wireless network or transmit ECGs."
  cause: "Clinical Engineering found the device was assigned to an outdated wireless profile after being moved from another department."
  resolution: "Applied the approved current profile, verified network connection, transmitted a simulator ECG, and confirmed receipt at the destination system."
helpfulDetails:
  - "Exact wireless message."
  - "Network name selected."
  - "Signal behavior by location."
  - "Whether other devices were affected."
  - "Date and time accuracy."
  - "Network address status."
  - "Profile or department observed."
  - "Wired operation result, if applicable."
  - "Test transmission status."
  - "Receiving-system confirmation."
  - "Final device status."
---

## What This Guide Helps With

Troubleshooting wireless connection failure caused by signal, profile, credentials, network availability, configuration, time, or infrastructure problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and ECG Delivery

Do not delay an urgent ECG while attempting to restore Wi-Fi.

Acquire the ECG using an approved alternate workflow, such as local storage, printing, wired connectivity, or another verified EKG machine. Confirm that any locally stored record remains available for later transmission.

**Expected outcome:** The ECG is obtained and preserved while wireless troubleshooting continues.

### 2. Confirm the Exact Wireless Failure

Determine whether:

- Wi-Fi is disabled.

- No networks are visible.

- The correct network is visible but will not connect.

- The device connects but cannot transmit ECGs.

- The connection drops intermittently.

- The failure occurs only in one room or department.

- The problem began after a password, certificate, network, or location change.

Record visible status indicators and displayed messages.

**Expected outcome:** The issue is separated into radio, profile, authentication, signal, network access, or destination communication categories.

### 3. Verify Wireless Is Enabled

Use only normal authorized controls to confirm that Wi-Fi is enabled and the intended wireless profile is selected.

Check whether airplane mode, wireless disablement, or a wired-only profile is active.

**Expected outcome:** Wireless operation is enabled and the approved profile is selected.

### 4. Check Location and Signal Conditions

Move the device to a known-good coverage area without using it on a patient during the test.

Observe whether the network becomes visible or signal strength improves. Consider:

- Shielded rooms.

- Elevators.

- Basement areas.

- Dense equipment placement.

- Recent construction.

- Known access-point outages.

**Expected outcome:** The device detects the expected network in a known-good coverage area. If it works there, the likely cause is environmental or infrastructure-related.

### 5. Compare With Other Wireless Devices

Determine whether other approved EKG machines or clinical devices in the same location are connected.

Do not compare with personal phones as the only network test because they may use different networks, bands, or credentials.

**Expected outcome:** The problem is identified as device-specific or affecting the local wireless infrastructure.

### 6. Restart the EKG Machine

Confirm that no ECG save, export, or transmission is active.

Perform a normal shutdown and restart. Allow the device to complete startup and reconnect without repeated user commands.

**Expected outcome:** The wireless interface initializes and reconnects to the approved network.

### 7. Verify Date and Time

Check the displayed date, time, and time zone.

A significantly incorrect clock can interfere with certificate-based authentication, secure connections, record timestamps, and network services.

Correct the time only through approved operator or administrative methods.

**Expected outcome:** Date and time are accurate and the device can authenticate normally.

### 8. Review the Approved Wireless Profile

Compare the affected device’s normal authorized wireless settings with a working ELI Series device assigned to the same department.

Verify as applicable:

- Network name.

- Security type.

- Site or department profile.

- Authentication method.

- Certificate status.

- Address assignment method.

- Device location.

Do not reveal passwords, export credentials, install unapproved certificates, or change enterprise network settings without authorization.

**Expected outcome:** The device profile matches the approved current network configuration.

### 9. Confirm Network Address and Connectivity Status

Review available network-status information.

Check whether the device receives a valid network address and whether it indicates connection to the intended network. Do not assign a manual address unless authorized and documented.

**Expected outcome:** The device associates with the network and receives valid network configuration.

### 10. Separate Wi-Fi Connection From ECG Transmission

If the device shows a wireless connection but ECGs do not transmit, test normal network functions available to the operator.

Check:

- Correct transmission destination.

- Pending queue.

- Server availability.

- Interface status.

- Department configuration.

- Whether other devices can transmit.

**Expected outcome:** The problem is correctly identified as network association or destination-system communication rather than simply “Wi-Fi.”

### 11. Perform a Controlled Transmission Test

Using approved test data and an ECG simulator:

- Acquire a test ECG.

- Save it.

- Transmit it through Wi-Fi.

Confirm successful status on the device.

Verify receipt at the intended destination.

**Expected outcome:** The complete wireless transmission path works. Troubleshooting can stop and the device may return to service.

### 12. Escalate Persistent or Intermittent Wireless Failure

Remove the device from service or restrict it to an approved alternate workflow if:

- It cannot connect in known-good coverage areas.

- Connection drops unpredictably.

- The wireless profile cannot be validated.

- It connects but records do not reliably reach the destination.

- Certificate or enterprise authentication changes are required.

**Expected outcome:** The device is not returned with an unreliable ECG communication pathway.

## If the Problem Persists

Common external causes involving wireless enablement, location, signal strength, startup state, date and time, profile selection, and local network availability have been ruled out. The remaining issue may involve the wireless adapter, certificate provisioning, enterprise authentication, network access control, access-point configuration, firewall rules, destination services, or device software.

The device should be:

- Removed from service when reliable transmission is required and no approved alternate workflow exists.

- Labeled Out of Service.

- Sent for repair or bench evaluation when device-specific failure is suspected.

- Evaluated using appropriate Mortara documentation and approved test equipment.

- Repaired or configured only by qualified personnel.

Coordinate with network, cybersecurity, clinical applications, and ECG management teams as appropriate. After correction, verify connection, reconnection after restart, and end-to-end test ECG receipt.

Knowing when to escalate a wireless infrastructure or credential problem is proper troubleshooting.

## Clinical Use Tip

A connected Wi-Fi icon does not prove successful ECG delivery; verify the record reaches the intended receiving system.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain ECG availability while checking simple wireless causes before assuming hardware failure. Verify signal, profile, time, network status, and the complete transmission path, then involve the appropriate infrastructure teams when needed. Document both device behavior and destination receipt.

That is successful troubleshooting.
