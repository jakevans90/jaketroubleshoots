---
schemaVersion: 1
title: "Getinge Flow-c Anesthesia Machine - Device Will Not Power On or Complete Self-Test"
issueTitle: "Device Will Not Power On or Complete Self-Test"
description: "Troubleshoots startup, power, and self-test failures caused by external power, connections, accessories, configuration, or readily correctable setup conditions."
assetType: "Anesthesia Machine"
manufacturer: "Getinge"
model: "Flow-c"
slug: "getinge-flow-c-device-will-not-power-on-or-complete-self-test"
dateAdded: "2026-10-13"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported the Getinge Flow-c would power on but would not complete its startup self-test."
  cause: "Clinical Engineering found the AC connection partially disengaged at the machine, causing intermittent power during initialization."
  resolution: "Clinical Engineering reseated the power connection, completed startup and functional checks, and verified normal operation before returning the machine to service."
helpfulDetails:
  - "Exact startup or self-test message"
  - "Whether the machine was completely unresponsive or partially initialized"
  - "AC power and outlet-test results"
  - "Power-cord and connector condition"
  - "Pipeline or cylinder gas status"
  - "Accessories connected during the failure"
  - "Recent relocation, cleaning, or power interruption"
  - "Results after controlled restart"
  - "Final functional-check result"
  - "Final device status"
---
## What This Guide Helps With
Troubleshoots startup, power, and self-test failures caused by external power, connections, accessories, configuration, or readily correctable setup conditions.

## Step-by-Step Troubleshooting
### 1. Protect the Patient and Maintain Anesthesia Capability
Do not troubleshoot an unreliable anesthesia machine while a patient depends on it. If the Flow-c is in clinical use, transition the patient to another verified anesthesia delivery and ventilation method according to facility procedures. Remove the machine from active use if dependable operation cannot be confirmed.

**Expected outcome:** Patient care is maintained independently of the affected machine, allowing safe troubleshooting.

### 2. Confirm the Exact Startup Failure
Determine whether the machine is completely unresponsive, begins powering up but stops, repeatedly restarts, or reaches a self-test that will not complete. Record any displayed message exactly as shown. Ask whether the problem began after relocation, cleaning, accessory replacement, shutdown, or a power interruption.

**Expected outcome:** The failure is reproduced and narrowed to power-up, initialization, or a specific self-test stage.

### 3. Verify Facility AC Power
Confirm the power cord is fully seated at the machine and connected to an appropriate receptacle. Inspect the plug and cord for damage. Verify the receptacle using an approved outlet tester or another appropriate method. Avoid relying only on the presence of nearby powered equipment.

**Expected outcome:** Reliable facility AC power is confirmed at the machine. If restoring AC power corrects startup, verify normal initialization and stop troubleshooting.

### 4. Inspect External Power Connections
Check the accessible power cord, strain relief, connector, and surrounding area for looseness, contamination, scorching, deformation, or physical damage. Do not use the machine with damaged power components.

**Expected outcome:** External power components are intact and securely connected. Damaged equipment is removed from service.

### 5. Check External Accessories and Connections
Inspect attached patient-circuit components, gas hoses, sensors, modules, data cables, and other removable accessories for improper connection or obvious damage. Correct any setup issue using approved components. Disconnect only accessories that can safely be removed and whose removal is permitted for troubleshooting.

**Expected outcome:** Required accessories are correctly installed and no external connection is preventing initialization.

### 6. Verify Required Gas and System Conditions
Confirm required pipeline or cylinder gas sources are available and properly connected as applicable. Check that accessible valves, hoses, and connections are in their normal operating condition. Do not bypass gas-supply safeguards.

**Expected outcome:** Required external gas supplies and connections are available for the machine's startup checks.

### 7. Perform One Controlled Restart
After external conditions have been corrected, shut down and restart the machine using the normal controls. Avoid repeated power cycling if the same fault continues.

**Expected outcome:** The Flow-c completes startup and its required self-test. If it does, continue to final verification and stop troubleshooting.

### 8. Perform Final Functional Verification
Before return to service, complete the applicable manufacturer-required pre-use or functional checks. Verify ventilation capability, gas delivery, alarms, controls, displays, and other safety functions appropriate to the machine.

**Expected outcome:** The machine completes required checks without unresolved faults and performs normally.

## If the Problem Persists
If verified AC power, external connections, gas sources, accessories, and normal startup conditions have been ruled out, the problem may involve an internal power, battery, initialization, software, sensor, or other service-level condition.

Remove the Getinge Flow-c from service, label it **Out of Service**, and send it for repair or bench evaluation. Evaluate it using current manufacturer documentation and approved test equipment. Internal repairs, software recovery, or configuration changes should be performed only by qualified personnel.

Do not return the machine to clinical use until required functional and safety testing has been successfully completed. Recognizing when external troubleshooting has reached its safe limit is proper troubleshooting.

## Clinical Use Tip
Have another verified anesthesia delivery and ventilation method available before troubleshooting any Flow-c that cannot reliably initialize.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought
Protect the patient first, then verify facility power, external connections, gas supplies, accessories, and setup before assuming an internal failure. Escalate persistent startup faults appropriately and document the complaint, confirmed cause, corrective action, and final verification clearly.

That is successful troubleshooting.
