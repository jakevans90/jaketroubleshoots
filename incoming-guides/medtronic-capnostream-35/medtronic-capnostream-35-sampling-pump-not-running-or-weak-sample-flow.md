---
schemaVersion: 1
title: "Medtronic Capnostream 35 Capnography Monitor - Sampling Pump Not Running or Weak Sample Flow"
issueTitle: "Sampling Pump Not Running or Weak Sample Flow"
description: "Troubleshoots absent or weak gas sampling caused by blocked FilterLines, poor connections, moisture, configuration, or internal pump-related problems."
assetType: "Capnography Monitor"
manufacturer: "Medtronic"
model: "Capnostream 35"
slug: "medtronic-capnostream-35-sampling-pump-not-running-or-weak-sample-flow"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that the Capnostream 35 produced a weak waveform and delayed EtCO2 readings."
  cause: "Clinical Engineering found the FilterLine compressed between the monitor mount and transport handle."
  resolution: "The FilterLine was replaced and rerouted, and normal sample flow, waveform response, and alarms were verified."
helpfulDetails:
  - "Exact display or blockage message"
  - "Waveform appearance"
  - "Whether sampling was absent or weak"
  - "FilterLine type and routing"
  - "Presence of moisture or contamination"
  - "Connector condition"
  - "Known-good FilterLine result"
  - "Comparison-monitor result"
  - "Approved flow-test result"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots absent or weak gas sampling caused by blocked FilterLines, poor connections, moisture, configuration, or internal pump-related problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Provide Alternate Monitoring

Do not troubleshoot a suspected sampling-pump failure while the patient relies on the monitor. Move the patient to another verified capnography monitor or provide an approved alternate respiratory-monitoring method.

Remove the Capnostream 35 from the active bedside setup before testing.

**Expected outcome:** Patient monitoring continues without dependence on the suspect sampling system.

### 2. Confirm the Reported Condition

Determine whether the monitor has no waveform, intermittent waveform, slow response, a weak waveform, repeated blockage indications, or no audible or detectable sampling activity.

Confirm whether the condition occurs with all FilterLines or only one accessory.

**Expected outcome:** The suspected flow problem is reproduced and distinguished from a display-only issue.

### 3. Verify Normal Startup and CO2 Activation

Power the monitor normally and confirm that startup completes. Verify that CO2 monitoring is enabled and that the monitor recognizes when a compati…9536 tokens truncated…nfirm that the desired patient, trend, event, and date range are selected before export. Verify that the user is following the authorized normal workflow and has appropriate access.

Do not use restricted service menus or unsupported software utilities.

**Expected outcome:** The export command is available and directed to the correct data set.

### 4. Inspect the USB Device

Check the removable media for physical damage, contamination, write protection, insufficient capacity, or use for unrelated software.

Use only facility-approved and compatible media. Do not connect unknown personal drives.

**Expected outcome:** The USB device is approved, undamaged, writable, and has sufficient available space.

### 5. Inspect the USB Port Externally

Examine the monitor’s USB port for bent contacts, debris, liquid, looseness, or enclosure damage. Do not insert tools or fluids into the port.

**Expected outcome:** The port appears clean, dry, and mechanically intact.

### 6. Reinsert the USB Device Correctly

Remove the USB device, wait for the monitor to complete any pending activity, and reconnect it firmly without excessive force. Allow time for recognition before starting the export.

**Expected outcome:** The monitor recognizes the USB device. If export then completes and the file is verified, troubleshooting can stop.

### 7. Test With Another Approved Known-Good USB Device

Use a second compatible, facility-approved USB device. Keep the exported data set small for the initial test when possible.

**Expected outcome:** The export succeeds with the known-good media, confirming the original USB device was incompatible, full, damaged, or corrupted. Troubleshooting can stop.

### 8. Verify Available Internal and USB Storage

Confirm that the monitor can access the selected record and that the USB device has enough free space. A damaged stored record or full internal memory may also interfere with export.

**Expected outcome:** Both source data and destination storage are available.

### 9. Complete and Verify a Controlled Export

Export a test record or approved nonclinical data set. After the monitor reports completion, safely remove the media according to normal workflow and verify that the expected file exists and can be opened on an approved workstation.

**Expected outcome:** The export completes, the file is present, and its contents correspond to the selected record. If successful, troubleshooting can stop.

### 10. Escalate Persistent Port or Software Failure

If multiple approved USB devices are not recognized or exports repeatedly fail, freeze, or produce corrupted files, remove the device from service when data export is required by the workflow.

Label it **Out of Service** and escalate for USB-port, software, storage, or configuration evaluation.

**Expected outcome:** A monitor with unreliable data transfer is prevented from use in workflows requiring dependable export.

## If the Problem Persists

External media, storage capacity, port condition, record selection, and workflow causes have been ruled out. Remaining categories include damaged USB hardware, internal storage corruption, software failure, incompatible configuration, or a service-level data-management problem.

The monitor should be removed from service when export is clinically or operationally required, labeled Out of Service, and evaluated using manufacturer documentation and approved service tools. Repair and software restoration should be performed only by qualified personnel.

After repair, verify recognition of approved media, successful export, file readability, patient-data integrity, stored-record access, and complete monitor functionality before return to service.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Verify the exported file before deleting or clearing the original patient record from the monitor.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the original data, confirm the authorized workflow, and test with approved known-good media before suspecting internal failure. Persistent export problems require escalation and precise documentation of the data selected, devices tested, and verification results.

That is successful troubleshooting.
