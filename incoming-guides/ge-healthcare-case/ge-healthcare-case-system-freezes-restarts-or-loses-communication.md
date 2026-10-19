---
schemaVersion: 1
title: "GE Healthcare CASE Stress Test System - System Freezes, Restarts, or Loses Communication"
issueTitle: "System Freezes, Restarts, or Loses Communication"
description: "CASE becomes unresponsive, unexpectedly restarts, or intermittently loses communication with acquisition or exercise-system components."
assetType: "Stress Test System"
manufacturer: "GE Healthcare"
model: "CASE"
slug: "ge-healthcare-case-system-freezes-restarts-or-loses-communication"
dateAdded: "2026-10-19"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the CASE system intermittently lost communication with the ECG acquisition equipment during stress testing."
  cause: "Clinical Engineering reproduced the communication loss and found an external acquisition-interface cable with an intermittent connection."
  resolution: "Replaced the affected interface cable and verified stable ECG acquisition and peripheral communication through repeated functional testing."
helpfulDetails:
  - "What froze, restarted, or disconnected"
  - "Activity occurring when failure happened"
  - "Exact displayed message"
  - "Whether the workstation or only a peripheral restarted"
  - "AC power and UPS status"
  - "Communication cable condition"
  - "External devices connected"
  - "Environmental observations"
  - "Known-good substitution results"
  - "Whether the failure was reproduced"
  - "Relevant logs preserved"
  - "Final stability-test result"
  - "Final device status"
---

## What This Guide Helps With
CASE becomes unresponsive, unexpectedly restarts, or intermittently loses communication with acquisition or exercise-system components.

## Step-by-Step Troubleshooting
### 1. Protect the Patient Immediately
If CASE freezes, restarts, or loses essential communication during an active stress study, stop exercise safely according to clinical protocol and provide verified alternate monitoring. Do not continue relying on an unstable system.

**Expected outcome:** Patient monitoring and exercise safety no longer depend on the unreliable CASE system.

### 2. Document the Exact Failure Before Restarting
Record what froze or disconnected, what the patient and system were doing at the time, and any visible messages. Determine whether the entire workstation restarted or only one peripheral lost communication.

Preserve available logs or event information according to facility procedure when the event may be clinically significant.

**Expected outcome:** Sufficient information is captured to distinguish a workstation failure from a peripheral communication problem.

### 3. Inspect AC Power Stability
Verify power cords, approved power distribution equipment, UPS components if present, and wall receptacle connections are secure. Look for loose plugs or evidence of intermittent external power.

**Expected outcome:** Stable facility power is confirmed. If a loose external power connection caused the restart and correction restores stable operation, proceed to final verification.

### 4. Inspect Communication Cables
Check connections to ECG acquisition hardware, treadmill or ergometer interfaces, network connections, printers, and other relevant peripherals. Look for loose, damaged, crushed, or strained cables.

**Expected outcome:** All required external communication connections are secure and physically intact.

### 5. Remove Nonessential External Devices
With CASE shut down normally, disconnect nonessential removable USB or other external devices that are not required for testing. Restart the system with the minimum approved configuration.

**Expected outcome:** CASE operates stably without unnecessary external devices. If one removable accessory consistently triggers the problem, remove that accessory from service.

### 6. Check the Operating Environment
Confirm vents are not blocked and the workstation is not exposed to unusual heat, dust accumulation around external ventilation openings, liquid contamination, or other obvious environmental stress.

Do not open the workstation solely to investigate cooling.

**Expected outcome:** The system has an appropriate operating environment with unobstructed external ventilation.

### 7. Perform One Controlled Restart
After external checks, restart CASE normally and allow the workstation and required peripherals to initialize fully.

Avoid repeated cycling if the system continues restarting, produces unusual odor or heat, or shows signs of electrical failure.

**Expected outcome:** The system completes startup and remains stable.

### 8. Reproduce the Workflow Without a Patient
Use an appropriate simulator or controlled test setup to operate the system through the workflow associated with the failure. Verify ECG acquisition and communications with required peripherals.

**Expected outcome:** The system remains responsive and connected throughout the representative workflow.

### 9. Isolate Individual External Components
If communication loss recurs, test one external peripheral or communication path at a time using known-good cables or components when possible.

**Expected outcome:** A repeatable external cause is isolated, or external peripherals are ruled out.

### 10. Perform Final Stability Verification
Operate CASE long enough to verify reliable application response, continuous ECG acquisition, required peripheral communication, network availability when applicable, and normal shutdown/startup behavior.

**Expected outcome:** No freeze, unexpected restart, or communication loss occurs during the functional test. The issue is resolved and troubleshooting can stop.

## If the Problem Persists
External power, cabling, peripherals, environmental conditions, and controlled restart have been evaluated. Continued freezing, unexpected restarting, or communication loss may involve workstation hardware, operating system, CASE application software, drivers, acquisition hardware, network infrastructure, or another service-level problem.

Remove the CASE system from service, label it **Out of Service**, and send it for repair or bench evaluation. Preserve relevant event information before repair when possible. Evaluate the system using appropriate GE Healthcare documentation and approved test equipment.

Do not repeatedly return an intermittent system to clinical use simply because one restart temporarily clears the condition. Qualified personnel should complete repair or configuration changes and verify stable operation before release.

## Clinical Use Tip
An intermittent CASE failure during exercise can eliminate both monitoring information and exercise-device control at the worst possible time; treat repeated freezes or communication losses as a removal-from-service condition.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Intermittent failures deserve the same attention as complete failures when they can compromise monitoring or exercise control. Rule out power, connections, accessories, and environment first, preserve useful evidence, verify stability after correction, and remove unresolved systems from service.

That is successful troubleshooting.
