---
schemaVersion: 1
title: "Masimo Rad-97 Pulse Oximeter - Unexpected Shutdown During Battery Operation"
issueTitle: "Unexpected Shutdown During Battery Operation"
description: "Unexpected battery shutdown caused by incomplete charging, aged battery capacity, loose power connections, high load, temperature, software, or internal power faults."
assetType: "Pulse Oximeter"
manufacturer: "Masimo"
model: "Rad-97"
slug: "masimo-rad-97-unexpected-shutdown-during-battery-operation"
dateAdded: "2026-08-05"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the Rad-97 shut down unexpectedly during patient transport even though the battery indicator initially showed available charge."
  cause: "Clinical Engineering found that the battery voltage indication dropped abruptly under load and the unit failed the facility’s controlled battery runtime test."
  resolution: "Replaced the approved battery through the authorized service process, verified charging, runtime, low-battery alarms, monitoring, and alarm operation, and returned the device to service."
helpfulDetails:
  - "Battery level before shutdown"
  - "Approximate runtime"
  - "Low-battery warning behavior"
  - "AC power and charging indicators"
  - "Outlet and power supply tested"
  - "Physical battery safety concerns"
  - "Attached accessories"
  - "Shutdown during movement or transport"
  - "Controlled runtime test results"
  - "Final charging, alarm, and device status"
---

## What This Guide Helps With

Unexpected battery shutdown caused by incomplete charging, aged battery capacity, loose power connections, high load, temperature, software, or internal power faults.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Restore Continuous Monitoring

Do not continue using a monitor that shuts down unexpectedly while a patient depends on it.

Transfer monitoring to another verified device and connect the Rad-97 to approved AC power only after it is removed from the patient.

Expected outcome: Patient monitoring continues without risk of another shutdown.

### 2. Confirm the Shutdown Pattern

Determine the displayed battery level before shutdown, estimated operating time, whether alarms occurred, and whether the device restarted when AC power was connected.

Ask whether the shutdown occurs every time on battery or only during transport, movement, or use of attached accessories.

Expected outcome: The shutdown condition is clearly defined.

### 3. Inspect for Battery Safety Concerns

Check for enclosure swelling, excessive heat, odor, leakage, discoloration, or physical damage.

If any battery safety concern is present, do not charge or operate the device. Remove it from service and follow facility battery-handling procedures.

Expected outcome: The unit is safe for controlled testing or isolated immediately.

### 4. Verify the Approved Power Supply and Outlet

Inspect the power supply, cord, plug, and device connector. Connect to a verified outlet and confirm charging indications.

Ensure the connector remains secure and is not intermittently losing AC power.

Expected outcome: The Rad-97 recognizes AC power and begins charging normally.

### 5. Allow a Complete Approved Charge

Charge the device according to facility and manufacturer guidance before testing runtime.

Do not judge battery condition from a brief charge period.

Expected outcome: The battery indicator shows a completed or normal charge state.

### 6. Check Battery Indicator Behavior

Disconnect AC power under controlled bench conditions and observe whether the battery indicator decreases normally or falls abruptly.

Expected outcome: Battery status changes gradually and the device remains operating.

### 7. Remove Nonessential Accessories

Disconnect USB devices, external communication accessories, and other nonessential loads.

Repeat battery operation testing with only required monitoring accessories.

Expected outcome: The device remains powered, or an attached accessory is identified as contributing to abnormal shutdown.

### 8. Inspect the Power Connector During Movement

With the device on AC power, gently reposition the external cord through normal movement and observe for power-source switching or charging interruptions.

Do not stress the connector.

Expected outcome: AC power and charging remain stable without interruption.

### 9. Perform a Controlled Battery Runtime Test

Using approved facility procedures and test conditions, operate the fully charged Rad-97 on battery while monitoring battery indication, alarms, temperature, and shutdown behavior.

Do not place the device into clinical service solely to test runtime.

Expected outcome: The monitor operates reliably for the facility’s accepted test requirement without abrupt shutdown.

### 10. Verify Low-Battery Alarm and Shutdown Behavior

Confirm that low-battery warnings occur before shutdown and that the device does not lose power without adequate warning.

Expected outcome: Battery alarms and shutdown behavior are orderly and repeatable.

### 11. Recheck After Battery Replacement When Authorized

If testing confirms inadequate battery capacity and battery replacement is permitted under approved procedures, install the correct approved battery through qualified service.

Do not improvise battery substitutions.

Expected outcome: The monitor charges normally and passes controlled battery testing.

### 12. Perform Final Functional Verification or Escalate

Verify operation on AC and battery, charging, battery indication, low-battery alarms, monitoring, display, network communication where applicable, and all audible and visual alarms.

If unexpected shutdown persists, remove the device from service.

Expected outcome: The device passes complete verification or is routed for qualified repair.

## If the Problem Persists

External causes such as incomplete charging, unstable AC connection, accessory load, environmental condition, and confirmed battery capacity have been ruled out.

The remaining cause may involve the battery pack, charging system, internal power distribution, battery-management circuitry, software, or another service-level condition. Remove the Rad-97 from service, label it Out of Service, and send it for repair or bench evaluation using current manufacturer documentation and approved test equipment.

Battery replacement, internal repair, and calibration or configuration must be performed only by qualified personnel. Complete electrical safety, charging, runtime, low-battery alarm, and functional testing before return to service.

## Clinical Use Tip

Verify adequate battery condition before transport and keep an alternate monitoring plan available whenever continuous pulse oximetry is required away from AC power.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient from sudden monitoring loss, verify charging and external power before assuming battery failure, test battery performance under controlled conditions, and escalate unresolved shutdowns.

That is successful troubleshooting.
