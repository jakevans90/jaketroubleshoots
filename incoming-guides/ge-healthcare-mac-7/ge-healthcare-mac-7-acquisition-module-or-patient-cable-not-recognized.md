---
schemaVersion: 1
title: "GE Healthcare MAC 7 Electrocardiograph (EKG) Machine - Acquisition Module or Patient Cable Not Recognized"
issueTitle: "Acquisition Module or Patient Cable Not Recognized"
description: "Troubleshooting an acquisition module or patient cable that is not detected because of connection, accessory, connector, compatibility, or external hardware problems."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "GE Healthcare"
model: "MAC 7"
slug: "ge-healthcare-mac-7-acquisition-module-or-patient-cable-not-recognized"
dateAdded: "2026-08-27"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the MAC 7 would not recognize the connected patient cable and acquisition module."
  cause: "Clinical Engineering found the patient cable connector was damaged and failed recognition while a known-good cable was detected normally."
  resolution: "Replaced the defective patient cable and verified consistent accessory recognition and normal ECG acquisition using an ECG simulator."
helpfulDetails:
  - "Accessory not recognized."
  - "Whether failure was constant or intermittent."
  - "Connector condition."
  - "Accessories reseated."
  - "Known-good cable or module tested."
  - "Compatibility verified."
  - "Behavior before and after restart."
  - "ECG simulator results."
  - "Final device status."
---

## What This Guide Helps With

Troubleshooting an acquisition module or patient cable that is not detected because of connection, accessory, connector, compatibility, or external hardware problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Confirm the Failure

If an ECG is clinically required, provide another verified electrocardiograph rather than troubleshooting while the patient waits for necessary diagnostic testing.

Confirm exactly which accessory is not recognized and whether the condition is constant or intermittent.

**Expected outcome:** Patient care continues safely and the affected acquisition component is clearly identified.

### 2. Disconnect and Reseat the Accessory

Remove the acquisition module or patient cable from its accessible connection and inspect the orientation before reconnecting it fully.

Do not force connectors. Confirm that the connector reaches its normal seated position without unusual resistance.

**Expected outcome:** The connected accessory is detected normally. If recognition returns and remains stable, proceed to final verification.

### 3. Inspect External Connectors

Inspect connector housings and accessible contacts for bent areas, contamination, moisture, debris, cracked plastic, loose fit, or damaged strain relief.

Do not attempt internal connector repair or contact realignment beyond approved external maintenance.

**Expected outcome:** Connectors are clean, dry, undamaged, and mechanically secure. Any visibly damaged accessory should be removed from service.

### 4. Verify the Correct Accessory

Confirm that the acquisition module, patient cable, and associated lead set are intended and approved for the MAC 7 configuration in use.

Do not assume that a physically similar accessory is electrically or functionally compatible.

**Expected outcome:** The connected accessory is appropriate for the system. If an incorrect accessory was being used, replace it with the correct approved component and retest.

### 5. Substitute a Known-Good Patient Cable

If available, connect a compatible known-good patient cable while leaving the rest of the setup unchanged.

Observe whether the system now recognizes the acquisition path normally.

**Expected outcome:** Recognition returns with the known-good cable, identifying the original cable as the likely external cause. Remove the defective cable from use.

### 6. Substitute a Known-Good Acquisition Module

If the cable tests normally and an approved compatible module is available, substitute the acquisition module and repeat detection testing.

Use one substitution at a time.

**Expected outcome:** The MAC 7 recognizes the known-good module consistently. If so, remove the original module from service for appropriate evaluation.

### 7. Restart the System Normally

If external connections and accessories appear normal, perform a controlled restart using the normal user-accessible shutdown and startup process.

Do not repeatedly power-cycle a device that displays signs of electrical damage, overheating, or other unsafe behavior.

**Expected outcome:** The system completes startup and recognizes the connected acquisition hardware. If recognition is restored and remains stable, continue to final verification.

### 8. Verify ECG Acquisition

Using an approved ECG simulator, verify that the recognized acquisition module and patient cable produce stable ECG signals across the intended leads.

Confirm that disconnecting and reconnecting the accessory does not produce intermittent detection problems.

**Expected outcome:** The system consistently recognizes the acquisition path and acquires valid simulated ECG signals. The device may return to service if all required checks pass.

### 9. Escalate Persistent Recognition Failure

If known-good compatible accessories are not recognized, or recognition is intermittent at the device connection, stop external troubleshooting.

**Expected outcome:** The MAC 7 is removed from service and routed for evaluation of the device-side interface or another service-level fault.

## If the Problem Persists

External cable, module, seating, compatibility, and restart causes have been addressed. Remaining possibilities include a device-side connector problem, acquisition interface fault, configuration issue, software problem, or another internal service-level condition.

The device should be:

- Removed from service.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Complete ECG acquisition and accessory-recognition verification after repair before returning the unit to clinical service. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Do not rely on an acquisition module or cable that reconnects only intermittently; provide another verified ECG system until the connection is proven reliable.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Begin with safe continuity of care and rule out connection, connector, compatibility, and accessory problems before suspecting the MAC 7 itself. Confirm reliable recognition and ECG acquisition before return to service.

That is successful troubleshooting.
