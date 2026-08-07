---
schemaVersion: 1
title: "ZOLL Propaq MD Defibrillator - 12-Lead ECG Acquisition or Transmission Failure"
issueTitle: "12-Lead ECG Acquisition or Transmission Failure"
description: "12-lead ECG cannot be acquired, stored, or transmitted because of electrodes, cables, signal quality, patient data, connectivity, configuration, or network issues."
assetType: "Defibrillator"
manufacturer: "ZOLL"
model: "Propaq MD"
slug: "zoll-propaq-md-12-lead-ecg-acquisition-or-transmission-failure"
dateAdded: "2026-08-07"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that 12-lead ECGs were acquired successfully but would not transmit from the Propaq MD."
  cause: "Clinical Engineering found that the device had no usable network connection in the reported location while 12-lead acquisition itself tested normally."
  resolution: "Connectivity was restored through the appropriate support pathway and successful 12-lead transmission and receipt at the destination were verified."
helpfulDetails:
  - "Acquisition versus transmission failure"
  - "Lead-off indications"
  - "Electrode condition"
  - "Cable condition"
  - "Simulator result"
  - "Patient information entered"
  - "Destination selected"
  - "Wi-Fi or cellular status"
  - "Rooms or locations tested"
  - "Whether other devices were affected"
  - "Receiving-system confirmation"
  - "Final device status"
---

## What This Guide Helps With

12-lead ECG cannot be acquired, stored, or transmitted because of electrodes, cables, signal quality, patient data, connectivity, configuration, or network issues.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve Diagnostic Workflow
If a 12-lead ECG is clinically urgent, obtain it using another verified ECG-capable device rather than delaying diagnosis while troubleshooting.

**Expected outcome:** Clinical decision-making is not delayed by the equipment problem.

### 2. Determine Whether Acquisition or Transmission Is Failing
Ask whether the unit:

- Cannot obtain a 12-lead tracing
- Produces excessive artifact
- Reports disconnected leads
- Completes acquisition but cannot send
- Sends intermittently
- Cannot reach the intended destination
- Fails only in certain rooms or network locations

Treat acquisition and transmission as separate parts of the troubleshooting path.

**Expected outcome:** The failure is isolated to ECG acquisition, stored data, or communication.

### 3. Inspect Electrodes and Lead Placement
For acquisition problems, check:

- Electrode condition
- Proper placement
- Secure adhesion
- Patient skin preparation
- Loose lead snaps
- Incorrect or missing lead connections

**Expected outcome:** All required electrodes have stable contact. If acquisition succeeds after correcting electrodes or placement, verify the tracing and stop acquisition troubleshooting.

### 4. Inspect the 12-Lead Cable and Lead Wires
Examine the cable and lead set for:

- Cuts
- Frayed insulation
- Damaged connectors
- Bent contacts
- Loose lead wires
- Intermittency
- Contamination

**Expected outcome:** The external lead system is intact and stable.

### 5. Substitute Known-Good ECG Accessories
Use known-good compatible cables, lead wires, and simulator connections as appropriate.

**Expected outcome:** If acquisition works with known-good accessories, replace the faulty external component and verify 12-lead acquisition.

### 6. Verify Signal Quality Using an ECG Simulator
Use an approved 12-lead-capable simulator when appropriate.

Confirm that the device can acquire a stable tracing without lead-off indications or excessive artifact.

**Expected outcome:** The Propaq MD successfully acquires a stable simulated 12-lead ECG.

### 7. Verify Required Patient and Destination Information
For transmission problems, confirm that required patient identification, destination selection, or other visible workflow information is entered appropriately.

Do not change protected network or institutional configuration without authorization.

**Expected outcome:** The record contains the information required for normal transmission workflow.

### 8. Check the Communication Path
Determine whether the intended connection uses Wi-Fi, cellular communication, or another supported pathway.

Check:

- Connection status
- Signal availability
- Whether other devices in the same area are affected
- Whether the failure follows the Propaq MD to another known-good location

**Expected outcome:** A local infrastructure problem is distinguished from a device-specific communication problem.

### 9. Attempt a Controlled Transmission
Using approved test data or a test workflow, attempt transmission to the intended receiving system.

Confirm receipt at the destination whenever access permits.

**Expected outcome:** The 12-lead ECG is successfully transmitted and received. If correcting connectivity or destination selection restores transmission, troubleshooting can stop.

### 10. Perform Final Functional Verification
Confirm:

- Stable 12-lead acquisition
- Correct lead recognition
- Successful record storage when applicable
- Successful transmission
- Receipt at the intended destination
- Normal operation after disconnecting test equipment

**Expected outcome:** The entire acquisition-to-destination workflow functions correctly.

### 11. Escalate Persistent Acquisition or Transmission Failure
If 12-lead acquisition fails with a simulator and known-good accessories, or transmission fails despite verified connectivity and infrastructure, remove the affected function or device from service according to clinical risk.

**Expected outcome:** Unresolved acquisition, configuration, communications, or internal faults receive qualified service evaluation.

## If the Problem Persists

If electrodes, lead placement, ECG cables, simulator testing, patient information, destination selection, connectivity, and receiving-system availability have been ruled out, the remaining cause may involve the ECG acquisition system, communication hardware, stored configuration, network infrastructure, receiving system, or another service-level condition.

The device should be:

- Removed from service when required by clinical risk
- Labeled Out of Service when the affected function makes the unit unsuitable for intended use
- Sent for repair or bench evaluation
- Evaluated using appropriate manufacturer documentation and approved test equipment
- Repaired or configured only by qualified personnel and authorized network support staff

Verify successful 12-lead acquisition and end-to-end transmission before return to service.

Knowing when to stop external troubleshooting and involve networking, clinical systems, or manufacturer support is proper troubleshooting.

## Clinical Use Tip

For urgent diagnostic ECG needs, obtain the 12-lead on another verified device before investigating a transmission problem.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Keep diagnostic care moving, separate acquisition problems from communication problems, verify external ECG accessories and the complete transmission path before assuming internal failure, escalate appropriately, and document both local testing and destination receipt.

That is successful troubleshooting.
