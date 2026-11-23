---
schemaVersion: 1
title: "GE Healthcare OEC One CFD C-Arm - System Will Not Boot or the Workstation Repeatedly Restarts"
issueTitle: "System Will Not Boot or the Workstation Repeatedly Restarts"
description: "Use this guide when the C-arm will not complete startup, loses power, freezes during boot, or the workstation repeatedly restarts."
assetType: "C-Arm"
manufacturer: "GE Healthcare"
model: "OEC One CFD"
slug: "ge-healthcare-oec-one-cfd-system-will-not-boot-or-the-workstation-repeatedly-restarts"
dateAdded: "2026-11-23"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the OEC One CFD workstation repeatedly restarted during startup and could not be used for imaging."
  cause: "Clinical Engineering found the system connected to an intermittently powered receptacle while the C-arm itself operated normally from a verified outlet."
  resolution: "Clinical Engineering moved the system to an approved functioning receptacle and verified repeated startup, stable operation, and normal imaging readiness."
helpfulDetails:
  - "Exact point where startup fails"
  - "Any displayed message"
  - "AC outlet tested"
  - "Power-cord condition"
  - "External accessories connected"
  - "Ventilation and fan observations"
  - "Whether the problem changes with outlet location"
  - "Number of controlled startup tests performed"
  - "Functional-test result"
  - "Final device status"
---

## What This Guide Helps With

Use this guide when the C-arm will not complete startup, loses power, freezes during boot, or the workstation repeatedly restarts.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Move the Case to Reliable Equipment

Do not attempt to continue a procedure using a C-arm that cannot complete startup or repeatedly restarts. Provide another verified imaging system when imaging is required.

Expected outcome: Clinical care continues without dependence on the unstable system.

### 2. Confirm the Failure Pattern

Determine whether the system is completely dead, begins startup but stops, reaches the application and then restarts, or loses power when a specific function is used. Record any displayed message before it disappears.

Expected outcome: The boot or restart behavior is clearly characterized.

### 3. Inspect the AC Power Source

Verify that the power cord is fully connected, the plug and cord are undamaged, and the receptacle is appropriate and functioning. Test the outlet using an approved method or move to a known-good approved outlet when permitted.

Expected outcome: Reliable AC power is available. If normal startup occurs from a verified outlet, troubleshoot the original power source rather than the C-arm.

### 4. Inspect the Power Cord and External Power Components

Check the complete accessible power cord, strain relief, plug, and inlet area for cuts, overheating, looseness, contamination, or physical damage.

Expected outcome: The external power path is intact. Any damaged power component requires removal from service until repaired or replaced.

### 5. Disconnect Nonessential External Accessories

Remove nonessential external peripherals or accessories that can be safely disconnected under normal operation. Leave required system components connected.

Expected outcome: The system starts normally without the nonessential accessory. If so, isolate the accessory or peripheral before returning the C-arm to service.

### 6. Perform One Controlled Power Cycle

If power is stable and no damage is found, shut the system down normally when possible, disconnect from AC if appropriate, allow the shutdown to complete, and restart once. Avoid repeated cycling of a unit that continues to fail.

Expected outcome: The workstation completes startup and remains stable. If the fault immediately returns, proceed to escalation.

### 7. Observe for Heat, Fan, or Environmental Issues

Check for blocked external vents, unusual heat, abnormal fan noise, fluid contamination, or operation in an unusually hot environment. Do not open internal assemblies solely to investigate cooling.

Expected outcome: External ventilation is unobstructed and no obvious environmental cause is present.

### 8. Verify Stability After Startup

If the system boots, leave it operating long enough to confirm that the workstation remains stable. Exercise normal user functions without initiating patient imaging.

Expected outcome: The workstation remains powered and responsive without unexpected restart.

### 9. Perform Final Functional Verification

Confirm normal startup, user-interface operation, image-system readiness, basic positioning controls, and acquisition using an approved test method.

Expected outcome: The system completes startup consistently and remains stable through functional testing. If successful, troubleshooting can stop.

### 10. Escalate Persistent Boot or Restart Failure

If the workstation repeatedly restarts, freezes, or fails to boot after power and external accessories have been ruled out, do not proceed into internal power supplies, computers, boards, or storage components.

Expected outcome: The system is removed from service and referred for qualified evaluation.

## If the Problem Persists

External AC power, power cord condition, environmental factors, and nonessential accessories have been ruled out. The remaining problem may involve internal power distribution, workstation hardware, storage, operating software, cooling, communication between system components, or another service-level subsystem.

Remove the device from service, label it Out of Service, and send it for repair or bench evaluation. Evaluate it using appropriate GE Healthcare documentation and approved test equipment. Internal computer, power-supply, software-recovery, or configuration work should be performed only by qualified personnel.

Return-to-service testing should verify repeated cold startup, stable operation, normal controls, imaging readiness, and acquisition.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A C-arm that boots successfully once after repeated restart failures should not be considered reliable until sustained operation and repeat startup are verified.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Verify the external power path before assuming workstation failure, avoid repeated uncontrolled restarts, confirm sustained stability after correction, and escalate internal boot problems appropriately.

That is successful troubleshooting.
