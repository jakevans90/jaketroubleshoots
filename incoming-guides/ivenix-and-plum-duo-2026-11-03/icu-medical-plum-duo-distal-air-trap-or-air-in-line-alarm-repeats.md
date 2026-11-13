---
schemaVersion: 1
title: "ICU Medical Plum Duo Infusion Pump - Distal Air Trap or Air-in-Line Alarm Repeats"
issueTitle: "Distal Air Trap or Air-in-Line Alarm Repeats"
description: "Troubleshoots recurring air-related alarms caused by visible bubbles, tubing orientation, cassette loading, disposables, fluid handling, or sensing problems."
assetType: "Infusion Pump"
manufacturer: "ICU Medical"
model: "Plum Duo"
slug: "icu-medical-plum-duo-distal-air-trap-or-air-in-line-alarm-repeats"
dateAdded: "2026-11-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported repeated air-in-line alarms despite visually clear tubing."
  cause: "Clinical Engineering found intermittent microbubbles entering through a loose upstream connection on the administration set."
  resolution: "Replaced the administration set, fully primed the line, verified alarm behavior, and confirmed normal operation on both channels."
helpfulDetails:
  - "Exact alarm wording"
  - "Affected channel"
  - "Presence and location of visible air"
  - "Fluid source condition"
  - "Cassette position"
  - "Tubing orientation"
  - "Connection integrity"
  - "Known-good set result"
  - "Channel comparison"
  - "Alarm behavior after restart"
  - "Final device status"
---

## What This Guide Helps With

Troubleshoots recurring air-related alarms caused by visible bubbles, tubing orientation, cassette loading, disposables, fluid handling, or sensing problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Stop Unreliable Delivery
If an air-related alarm repeats during patient therapy, place the infusion in a safe condition and transfer therapy to another verified pump when clinically required. Do not bypass, suppress, or repeatedly clear an air alarm without identifying the cause.

**Expected outcome:** Patient therapy continues safely without depending on an infusion path producing repeated air alarms.

### 2. Confirm the Alarm and Affected Channel
Record the exact alarm wording and identify which channel was active when the alarm occurred. Reproduce the problem only using an appropriate non-patient test setup.

**Expected outcome:** The reported air-related condition is clearly identified and associated with a specific channel or setup.

### 3. Inspect the Entire Fluid Path for Visible Air
Inspect the fluid container, drip chamber if present, tubing, cassette, connectors, injection sites, and distal tubing for bubbles, partially emptied chambers, loose connections, or air entering from the source.

**Expected outcome:** The fluid path is completely primed and visibly free of air.

If visible air is found and correct repriming eliminates the alarm, troubleshooting can stop after successful repeat testing.

### 4. Check Tubing and Cassette Positioning
Verify that the cassette is properly installed and that tubing is routed without twisting, stretching, pinching, or abnormal tension. Confirm tubing is positioned correctly through any external sensing areas.

**Expected outcome:** The cassette and tubing sit normally without conditions that could interfere with air detection.

If repositioning corrects the repeated alarm, verify multiple runs before returning the pump to service.

### 5. Inspect the Administration Set
Examine the disposable for clouding, deformation, damaged tubing, loose fittings, or other abnormalities. Replace questionable consumables rather than attempting to continue testing with a suspect set.

**Expected outcome:** The disposable is intact and appropriate for testing.

### 6. Test With a Known-Good Set
Install a new or verified compatible administration set, prime it carefully, and repeat testing using the same fluid source.

**Expected outcome:** The known-good set operates without recurrent air alarms.

If the alarm does not recur, the original disposable or its setup was the likely cause and troubleshooting can stop after final verification.

### 7. Compare Channels
If practical, test the same known-good setup on each channel independently. Determine whether the alarm follows the disposable/setup or consistently remains with one channel.

**Expected outcome:** Both channels behave consistently with a properly primed known-good set.

A repeatable alarm limited to one channel supports removal from service for further evaluation.

### 8. Check Environmental and Handling Factors
Confirm the tubing is not exposed to conditions that could create or move bubbles during testing, such as agitation of the fluid container, loose fittings, or unusual temperature changes. Ensure the test setup is stable.

**Expected outcome:** No external condition is introducing air into the fluid path.

### 9. Restart and Retest
Perform a normal power cycle with no patient attached, allow startup to complete, then repeat the test with the verified set.

**Expected outcome:** The pump starts normally and no repeated air alarm occurs.

If the pump operates consistently after restart and passes repeated testing, complete final verification.

### 10. Complete Functional Verification
Verify both channels using approved procedures, confirm alarm operation, and ensure the pump reliably detects genuine alarm conditions while avoiding false alarms during a correctly primed test.

**Expected outcome:** The pump operates normally without false recurring air alarms.

## If the Problem Persists

If recurring distal air trap or air-in-line alarms continue with properly primed tubing, correct cassette placement, verified fluid handling, and a known-good disposable, common external causes have been ruled out.

Possible remaining categories include an air-sensing problem, cassette-interface issue, channel-specific sensing condition, calibration or configuration issue, or another internal service-level fault.

The device should be:

- Removed from service
- Labeled **Out of Service**
- Sent for repair or bench evaluation
- Evaluated with appropriate manufacturer documentation and approved test equipment
- Repaired or calibrated only by qualified personnel
- Fully verified before return to clinical use

Do not compensate for recurrent air alarms by disabling or bypassing protective functions.

## Clinical Use Tip

Repeated air alarms during infusion warrant a pump exchange until the complete fluid path and pump have been verified.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Air alarms are safety features and should never be treated as nuisance alarms until the entire external fluid path has been checked. Rule out bubbles, disposables, routing, and connection problems before escalating a persistent sensing problem.

That is successful troubleshooting.
