---
schemaVersion: 1
title: "United Imaging uMR 790 MRI System - Workstation Freezes or Loses Communication"
issueTitle: "Workstation Freezes or Loses Communication"
description: "Troubleshoots console freezing, application unresponsiveness, and communication loss caused by workstation, cabling, network, peripherals, startup, or infrastructure conditions."
assetType: "MRI System"
manufacturer: "United Imaging"
model: "uMR 790"
slug: "united-imaging-umr-790-workstation-freezes-or-loses-communication"
dateAdded: "2026-09-25"
taxonomyMode: "reuse"
ccr:
  complaint: "MRI staff reported that the uMR 790 console lost communication with the scanner during exam setup."
  cause: "Clinical Engineering found an accessible network connection at the workstation was partially seated."
  resolution: "The connection was secured, workstation-to-scanner communication remained stable, and normal exam setup functionality was verified."
helpfulDetails:
  - "What part of the workstation froze"
  - "Exact communication message"
  - "Mouse and keyboard response"
  - "Workstation power status"
  - "Cable condition"
  - "Network status"
  - "Whether other systems were affected"
  - "Restart result"
  - "Recurrence after restart"
  - "Final communication status"
---
## What This Guide Helps With

Troubleshoots console freezing, application unresponsiveness, and communication loss caused by workstation, cabling, network, peripherals, startup, or infrastructure conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Dependence on the Frozen Console
If a patient examination is active, do not continue using an unreliable workstation or communication path.

Safely end or transfer the clinical workflow according to local procedures before restarting or disconnecting equipment.

**Expected outcome:** The patient is no longer dependent on an unstable console or communication path.

### 2. Define the Failure
Determine whether:
- The mouse and keyboard do not respond
- The application is frozen
- The entire workstation is unresponsive
- Scanner communication is lost
- The system repeatedly disconnects and reconnects
- Only one networked function is affected

Record any displayed message.

**Expected outcome:** The scope of the problem is clear.

### 3. Check Local Workstation Power and Peripherals
Verify:
- Display is powered
- Workstation power indicators are normal
- Keyboard and mouse connections are secure
- No external peripheral is visibly damaged
- No accidental cable disconnection has occurred

**Expected outcome:** Basic workstation hardware and accessible connections appear normal. If restoring a peripheral connection resolves the issue, verify operation and stop.

### 4. Check External Communication Connections
Inspect accessible network and system communication cables for secure seating, damage, strain, or recent movement.

Do not disturb internal scanner communication hardware.

**Expected outcome:** External communication connections are secure and undamaged. If reseating an approved connection restores stable communication, verify and stop.

### 5. Determine Whether the Problem Is Local or Infrastructure-Wide
Check whether other network-dependent MRI functions are affected.

If multiple devices or hospital systems are also experiencing communication problems, coordinate with IT or network support rather than assuming scanner failure.

**Expected outcome:** The problem is identified as local to the MRI system or part of a wider infrastructure issue.

### 6. Perform an Approved Normal Restart
If the system is not actively supporting a patient and site procedures permit, perform a normal workstation or application restart.

Avoid repeated forced shutdowns.

**Expected outcome:** The workstation restarts normally and restores stable communication. If so, continue to verification and stop.

### 7. Check for Recurring Freeze Conditions
After restart, observe whether:
- Controls respond normally
- Scanner status updates correctly
- No repeated disconnect occurs
- Normal workflow navigation is stable

If the workstation freezes again, do not continue cycling power.

**Expected outcome:** Operation remains stable. If instability returns, remove the system from service.

### 8. Check Environmental Conditions
Inspect for excessive heat, blocked workstation ventilation, liquid exposure, or unusual equipment-room conditions.

**Expected outcome:** No environmental problem is affecting the console. If overheating or contamination is suspected, discontinue use until evaluated.

### 9. Perform Final Communication Verification
Confirm:
- Workstation-to-scanner communication
- Acquisition control
- Patient/study workflow
- Required network functions
- Stable operation over an appropriate verification period

**Expected outcome:** Communication remains stable and the workstation is responsive. Troubleshooting can stop.

### 10. Escalate Persistent Freezing or Communication Loss
If power, accessible cabling, peripherals, network availability, and normal restart have been checked and the condition persists, stop troubleshooting.

**Expected outcome:** The system is taken out of service for qualified evaluation.

## If the Problem Persists

Common external causes have been ruled out. Remaining categories may include workstation hardware, software, storage, internal communication interfaces, system controllers, operating-system problems, network configuration, or infrastructure issues requiring specialized support.

The device should be:
- Removed from service
- Labeled **Out of Service**
- Sent for repair or service evaluation
- Evaluated using United Imaging documentation and approved diagnostic methods
- Repaired or configured only by qualified personnel

Coordinate with hospital IT when network infrastructure may contribute.

Knowing when to stop external troubleshooting is proper troubleshooting. Confirm stable workstation and scanner communication before return to service.

## Clinical Use Tip

Do not repeatedly force-restart the MRI workstation during an unstable examination; preserve study status and patient safety before restarting system components.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- Helpful details come from front matter. -->

## Final Thought

Workstation problems should be separated into local console, external connection, scanner communication, and hospital infrastructure causes before internal failure is assumed. Protect active studies, verify stable operation after correction, and document the full communication path.

That is successful troubleshooting.
