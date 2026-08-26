---
schemaVersion: 1
title: "Siemens Healthineers Cios Spin C-Arm - X-Ray Not Available or Exposure Inhibited"
issueTitle: "X-Ray Not Available or Exposure Inhibited"
description: "Addresses inhibited fluoroscopy or exposure caused by system readiness, controls, interlocks, accessory connections, positioning, configuration, or other external conditions."
assetType: "C-Arm"
manufacturer: "Siemens Healthineers"
model: "Cios Spin"
slug: "siemens-healthineers-cios-spin-x-ray-not-available-or-exposure-inhibited"
dateAdded: "2026-08-26"
taxonomyMode: "reuse"
ccr:
  complaint: "Operating room staff reported the Cios Spin powered normally but fluoroscopy would not activate from the footswitch."
  cause: "Clinical Engineering found the footswitch connector partially disengaged from its external connection."
  resolution: "The connector was properly reseated, fluoroscopy activation was verified with an approved test object, and the system returned to normal operation."
helpfulDetails:
  - "Exact inhibit or warning message."
  - "Imaging modes affected."
  - "Exposure control tested."
  - "Footswitch or hand-switch condition."
  - "Detector readiness."
  - "Emergency-stop status."
  - "Mechanical position."
  - "External connections inspected."
  - "Restart results."
  - "Exposure verification performed."
  - "Final device status."
---

## What This Guide Helps With
Addresses inhibited fluoroscopy or exposure caused by system readiness, controls, interlocks, accessory connections, positioning, configuration, or other external conditions.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Imaging Coverage
If X-ray is unexpectedly unavailable during a procedure, notify the clinical team immediately. Do not continue relying on a system that cannot produce radiation when required.

Provide another verified imaging system if imaging is necessary for continued patient care. Do not bypass radiation safety interlocks or attempt to defeat exposure-inhibit conditions.

**Expected outcome:** Patient care can continue safely without dependence on the affected C-arm.

### 2. Confirm the Exact Exposure Failure
Determine whether:
- Fluoroscopy is unavailable.
- A single-image exposure is unavailable.
- All radiation functions are inhibited.
- The system indicates not ready.
- Exposure begins and stops immediately.
- The problem occurs from only one switch.
- The issue began after repositioning, startup, accessory connection, or mode change.

Record the exact displayed message or status indicator.

**Expected outcome:** The failure is clearly characterized before components are changed.

### 3. Verify the System Is Fully Ready
Confirm that startup has completed and that no unresolved startup, detector, workstation, thermal, communication, or safety condition is preventing imaging.

Allow any normal initialization processes to finish rather than repeatedly commanding exposure during startup.

**Expected outcome:** The system reaches its normal imaging-ready state. If X-ray becomes available, troubleshooting can stop after verification.

### 4. Check the Exposure Control Being Used
Inspect the fluoroscopy footswitch, hand switch, or other approved exposure control for:
- Proper connection.
- Cable damage.
- Pinched wiring.
- Loose connectors.
- Mechanical sticking.
- Fluid contamination.
- Physical damage.

If only one control fails, compare operation using another approved exposure control when appropriate.

**Expected outcome:** A functional exposure control produces the expected command. If replacing or reconnecting an external control restores operation, verify all intended exposure functions before stopping.

### 5. Verify Required System Connections
Inspect accessible cables and connections associated with the C-arm, detector, workstation, and exposure controls.

A communication or detector-readiness problem may inhibit radiation even though the system otherwise appears powered.

Do not open housings or bypass a connection-detection circuit.

**Expected outcome:** Required system components are connected and recognized.

### 6. Check Mechanical Position and Interlock Conditions
Verify the C-arm and associated components are in a valid operating condition and that no emergency stop, collision condition, mechanical lock condition, or other externally evident interlock is active.

Do not defeat a brake, collision safeguard, or safety interlock to obtain X-ray.

**Expected outcome:** No externally correctable safety condition is inhibiting radiation.

### 7. Review Operator-Accessible Mode and Configuration
Confirm that the system is in the intended imaging mode and that an accidental mode selection, examination state, or workflow condition is not preventing exposure.

Compare current settings with a known-good clinical workflow without changing protected calibration or service configuration.

**Expected outcome:** The system is configured for an imaging mode in which the requested X-ray function should be available.

### 8. Perform a Controlled Restart if Appropriate
If all external conditions are normal and the system appears to be in an abnormal software state, complete one controlled shutdown and restart.

After startup, allow all components to initialize and determine whether X-ray readiness returns.

**Expected outcome:** The system reaches a stable ready condition and exposure becomes available. If so, continue to final verification.

### 9. Perform Functional Exposure Verification
Using approved facility procedures and appropriate test equipment or test object, verify:
- Fluoroscopy availability.
- Intended exposure-control operation.
- Detector response.
- Image generation.
- Termination of exposure when the control is released.
- No unresolved warnings or inhibit conditions.

Do not expose staff or patients unnecessarily during testing.

**Expected outcome:** X-ray initiates and terminates correctly and produces the expected image. Troubleshooting can stop after successful verification.

### 10. Remove From Service if Exposure Remains Inhibited
If X-ray remains unavailable after external controls, connections, readiness conditions, positioning, and workflow settings are checked, remove the unit from service.

Internal generator, safety-chain, communication, control, detector, or system-level causes require qualified service evaluation.

**Expected outcome:** A C-arm with unreliable radiation capability is not returned to clinical use.

## If the Problem Persists
Once accessible controls, cables, readiness conditions, positioning, settings, and external interlocks have been ruled out, the remaining cause may involve internal generator systems, exposure-control circuitry, safety chains, communication, detector readiness, software, or configuration requiring service-level evaluation.

The Cios Spin should be:
- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench/service evaluation.
- Evaluated using appropriate Siemens Healthineers documentation and approved radiation test equipment.
- Repaired or configured only by qualified personnel.

Complete required radiation-output, imaging, safety-interlock, and functional testing before return to clinical use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip
Never bypass an exposure inhibit or safety interlock to complete a procedure; provide alternate verified imaging instead.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**


## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Maintain patient safety, verify readiness and external controls before suspecting generator failure, never bypass safety interlocks, and confirm radiation and imaging performance before documenting return to service.

That is successful troubleshooting.
