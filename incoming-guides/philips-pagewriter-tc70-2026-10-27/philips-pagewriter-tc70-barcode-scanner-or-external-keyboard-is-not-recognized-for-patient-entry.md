---
schemaVersion: 1
title: "Philips PageWriter TC70 Electrocardiograph (EKG) Machine - Barcode Scanner or External Keyboard Is Not Recognized for Patient Entry"
issueTitle: "Barcode Scanner or External Keyboard Is Not Recognized for Patient Entry"
description: "Troubleshoots barcode scanner or external keyboard detection problems involving connections, accessory compatibility, ports, configuration, and external device failure."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "Philips"
model: "PageWriter TC70"
slug: "philips-pagewriter-tc70-barcode-scanner-or-external-keyboard-is-not-recognized-for-patient-entry"
dateAdded: "2026-10-27"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the PageWriter TC70 barcode scanner did not respond when entering patient information."
  cause: "Clinical Engineering found the scanner cable was loose at the external connection and the scanner was not being consistently detected."
  resolution: "Clinical Engineering reseated the scanner connection, verified repeated barcode entries with test data, completed a functional ECG acquisition, and returned the device to service."
helpfulDetails:
  - "Accessory type"
  - "Whether the accessory powered on"
  - "Port or connection used"
  - "Cable and connector condition"
  - "Whether built-in patient entry worked"
  - "Known-good accessory substitution results"
  - "Whether recognition changed after restart"
  - "Configuration observed"
  - "Accuracy of scanned or typed information"
  - "Final functional verification"
  - "Final device status"
---

## What This Guide Helps With
Troubleshoots barcode scanner or external keyboard detection problems involving connections, accessory compatibility, ports, configuration, and external device failure.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow

Do not delay an urgent ECG because an optional patient-entry accessory is unavailable. If necessary, use the PageWriter TC70's normal supported patient-entry method or another verified electrocardiograph.

Do not troubleshoot accessories while they are delaying clinically necessary ECG acquisition.

**Expected outcome:** Clinical staff can continue patient care while the accessory issue is evaluated separately.

### 2. Confirm the Exact Recognition Problem

Determine whether the barcode scanner or keyboard:

- Is completely unresponsive
- Has power but produces no input
- Works intermittently
- Enters incorrect characters
- Works in some fields but not others
- Stopped working after being moved or reconnected

Test the accessory in an appropriate patient-entry field using non-patient test information.

**Expected outcome:** The failure is clearly identified as accessory detection, input failure, or application/workflow behavior. If the accessory works normally during repeated tests, document the findings and monitor as appropriate.

### 3. Confirm Normal PageWriter Operation

Verify the PageWriter TC70 starts normally, its touchscreen and built-in controls respond, and patient information can be entered through the normal device interface.

A broader control or operating-system problem should not be misdiagnosed as a scanner or keyboard failure.

**Expected outcome:** The PageWriter operates normally except for the external input accessory. If multiple controls or peripherals fail, remove the device from service for broader evaluation.

### 4. Inspect and Reseat the External Accessory

Disconnect and inspect the scanner or keyboard connection when safe.

Check for:

- Loose connection
- Damaged cable
- Bent or damaged connector features
- Contamination
- Cracked accessory housing
- Damaged strain relief
- Signs of liquid exposure

Reconnect the accessory securely to the intended supported connection.

**Expected outcome:** The accessory has an intact cable and secure connection. If reseating restores reliable operation, repeat patient-entry tests and stop troubleshooting when the result remains stable.

### 5. Verify the Correct Connection Point

Confirm the accessory is connected to the appropriate external port intended for that device configuration.

If multiple externally accessible ports exist, do not randomly move the accessory between ports unless the intended connection is known from approved documentation or local configuration records.

**Expected outcome:** The accessory is connected to its correct supported interface. If correcting the connection restores operation, verify repeated input and stop troubleshooting.

### 6. Verify Accessory Compatibility

Confirm the barcode scanner or keyboard is an approved or known-supported accessory for the PageWriter TC70 configuration.

An accessory may physically connect yet not be supported or configured for use with the system.

Do not alter drivers, operating-system settings, or unauthorized configuration options to force unsupported hardware to operate.

**Expected outcome:** The accessory is confirmed appropriate for the device. If it is unsupported, restore the approved accessory configuration rather than modifying the electrocardiograph.

### 7. Test With a Known-Good Compatible Accessory

When available, connect an approved known-good scanner or keyboard of the same supported type.

Also test the suspect accessory on another compatible PageWriter TC70 if permitted and practical.

Use one substitution at a time to determine whether the failure follows the accessory or stays with the ECG machine.

**Expected outcome:** The comparison isolates the problem to the accessory or the PageWriter connection/configuration. If a defective accessory is identified, replace it and proceed to final verification.

### 8. Check Patient-Entry Configuration

Review normal user-accessible or authorized configuration related to patient-entry accessories. Confirm the device has not recently been reconfigured, restored, replaced, or moved from another department with a different accessory setup.

Do not enter restricted service menus or modify unrelated settings.

**Expected outcome:** The expected patient-entry configuration is present and consistent with local standards. If an authorized configuration correction restores the accessory, verify operation and document the change.

### 9. Restart and Recheck Peripheral Detection

If clinically appropriate, perform a normal restart of the PageWriter TC70 with the accessory connected as intended.

After startup, verify that the scanner or keyboard responds consistently.

**Expected outcome:** The accessory remains detected after restart and accepts repeated test entries. If recognition remains stable, troubleshooting can stop.

### 10. Perform Final Functional Verification

Test the complete patient-entry workflow using non-patient test data:

1. Enter information using the external accessory.
2. Confirm characters or scanned data appear correctly.
3. Repeat several entries.
4. Confirm the device remains responsive.
5. Confirm normal ECG acquisition can still be completed.

**Expected outcome:** The scanner or keyboard produces accurate, repeatable patient-entry data without affecting ECG operation. The device may be returned to service according to department policy.

### 11. Escalate Persistent Recognition Failure

If an approved known-good accessory is not recognized after external connections and authorized configuration have been verified, stop external troubleshooting.

Possible causes now extend beyond normal accessory troubleshooting.

**Expected outcome:** The device is removed from service if the failed functionality is required for the intended clinical workflow and routed for appropriate technical evaluation.

## If the Problem Persists

Common external causes have been ruled out. Remaining possibilities may include a failed external interface, internal peripheral communication problem, software/configuration problem, or infrastructure-related patient-entry integration issue.

The PageWriter TC70 should be:

- Removed from service when the failed accessory function is required for safe or correct clinical workflow.
- Labeled **Out of Service** when removed.
- Sent for repair or bench evaluation.
- Evaluated using appropriate Philips documentation and approved test equipment.
- Configured or repaired only by qualified personnel.
- Functionally verified before return to service.

Do not proceed into internal USB/interface hardware or operating-system modifications without appropriate authorization. Stopping after external causes have been eliminated is proper troubleshooting.

## Clinical Use Tip

Confirm patient identifiers entered by scanner or keyboard before ECG acquisition; incorrect demographic entry can create a valid ECG linked to the wrong patient.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- rendered from front matter -->

## Final Thought

Maintain the clinical ECG workflow while checking external connections, accessory condition, compatibility, known-good substitutions, and authorized configuration before assuming an internal interface failure. Escalate unresolved problems and document the complete CCR clearly.

That is successful troubleshooting.
