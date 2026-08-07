---
schemaVersion: 1
title: "ZOLL Propaq MD Defibrillator - Wi-Fi, Cellular, or Data Upload Failure"
issueTitle: "Wi-Fi, Cellular, or Data Upload Failure"
description: "Wireless or cellular communication fails, or clinical data will not upload because of signal, network availability, configuration, destination, or communication-path problems."
assetType: "Defibrillator"
manufacturer: "ZOLL"
model: "Propaq MD"
slug: "zoll-propaq-md-wi-fi-cellular-or-data-upload-failure"
dateAdded: "2026-08-07"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Propaq MD showed wireless connectivity but uploaded patient data was not reaching the intended destination."
  cause: "Clinical Engineering confirmed normal device connectivity and found that the receiving interface was unavailable during the reported period."
  resolution: "The interface issue was corrected by the appropriate support team and successful end-to-end test data transmission and receipt were verified."
helpfulDetails:
  - "Wi-Fi or cellular pathway affected"
  - "Connection indicator"
  - "Signal behavior"
  - "Rooms or locations tested"
  - "Comparison with another device"
  - "Network or infrastructure status"
  - "Destination selected"
  - "Upload attempt result"
  - "Receiving-system status"
  - "End-to-end verification"
  - "Final device status"
---

## What This Guide Helps With

Wireless or cellular communication fails, or clinical data will not upload because of signal, network availability, configuration, destination, or communication-path problems.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Use an Alternate Workflow
Communication failure should not delay urgent clinical care.

If data transmission is required immediately, use the facility's approved alternate workflow while Clinical Engineering evaluates connectivity.

**Expected outcome:** Patient care and required documentation continue despite the communication failure.

### 2. Confirm the Exact Communication Complaint
Determine whether the issue involves:

- Wi-Fi not connecting
- Cellular connection unavailable
- Data upload failing
- Intermittent transmission
- Connection only failing in specific locations
- Device appears connected but destination receives nothing
- One type of transmission failing while others work

**Expected outcome:** The affected communication pathway is identified.

### 3. Check Visible Connection Status
Review the device's normal user-accessible network or communication indicators.

Note whether the unit shows:

- No connection
- Weak or changing connection
- Connected status
- Transmission attempt without completion

Do not enter unauthorized service menus.

**Expected outcome:** The current communication state is documented before changes are made.

### 4. Check Location and Signal Conditions
Move the device, if operationally appropriate, to a known-good area where similar devices normally connect.

Compare behavior in:

- The reported room
- A nearby known-good location
- Another area on the same network when practical

**Expected outcome:** A coverage or location-specific problem is separated from a device-specific problem.

### 5. Compare With Other Devices
Determine whether another similarly configured device can connect or upload from the same location.

If multiple devices are affected, involve the appropriate network, cellular, or infrastructure support team.

**Expected outcome:** The problem is identified as either device-specific or infrastructure-wide.

### 6. Verify Basic Device Configuration Without Unauthorized Changes
Review permitted visible information such as:

- Intended communication method
- Expected network or service selection
- Destination selection
- Device date and time when relevant to the workflow

Do not alter security credentials, protected network profiles, or institutional configuration without authorization.

**Expected outcome:** No obvious workflow or configuration mismatch prevents communication.

### 7. Reestablish the External Connection
When allowed by facility practice, perform a normal disconnect/reconnect or restart of the communication process using user-accessible controls.

Avoid factory resets or configuration clearing.

**Expected outcome:** The connection reestablishes normally. If data transmission succeeds afterward, verify repeatability and troubleshooting can stop.

### 8. Test a Controlled Data Upload
Use an approved test workflow or non-patient test record where available.

Confirm:

- Transmission begins
- Transmission completes
- The intended destination receives the record

**Expected outcome:** End-to-end communication is verified rather than relying solely on the device's connection icon.

### 9. Verify Infrastructure and Destination Availability
If the Propaq MD appears connected but uploads fail, confirm with the appropriate support group whether:

- The wireless infrastructure is available
- Cellular service is available
- The intended application or receiving system is operational
- Required interfaces are functioning

**Expected outcome:** A downstream or infrastructure failure is identified before the device is sent for repair unnecessarily.

### 10. Perform Final Functional Verification
After correction, test the relevant connection in a known-good location and confirm successful data delivery.

Where appropriate, repeat testing in the original location.

**Expected outcome:** The Propaq MD consistently connects and uploads data to the intended destination. Troubleshooting can stop.

### 11. Escalate Persistent Communication Failure
If one Propaq MD remains unable to communicate while comparable devices and infrastructure function normally, escalate the device for service-level evaluation.

**Expected outcome:** The unresolved communication hardware, configuration, software, or interface problem receives appropriate technical support.

## If the Problem Persists

After signal strength, location, comparable devices, visible settings, destination availability, infrastructure status, and controlled transmission testing have been ruled out, the remaining cause may involve communication hardware, protected configuration, software, authentication, network infrastructure, cellular provisioning, or a downstream application interface.

The device should be:

- Removed from service if the communication failure prevents safe intended use
- Labeled Out of Service when appropriate
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Configured or repaired only by qualified and authorized personnel

Coordinate with networking, cybersecurity, clinical systems, or manufacturer support when the failure crosses organizational boundaries.

Verify end-to-end data receipt before closing the work order.

Knowing when to stop device troubleshooting and escalate to infrastructure support is proper troubleshooting.

## Clinical Use Tip

A connection indicator alone does not prove successful communication; confirm receipt at the intended destination.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Keep communication problems from delaying care, distinguish device failure from coverage, infrastructure, and destination problems, verify the complete end-to-end path, escalate to the correct support group, and document both device and receiving-system results.

That is successful troubleshooting.
