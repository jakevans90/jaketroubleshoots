---
schemaVersion: 1
title: "GE Healthcare OEC 9800 C-Arm - Printer or External Video Output Unavailable"
issueTitle: "Printer or External Video Output Unavailable"
description: "Troubleshoots missing print or video output caused by power, cabling, selected output, destination equipment, media, configuration, or service-level interface faults."
assetType: "C-Arm"
manufacturer: "GE Healthcare"
model: "OEC 9800"
slug: "ge-healthcare-oec-9800-printer-or-external-video-output-unavailable"
dateAdded: "2026-09-04"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that the external video monitor connected to the OEC 9800 displayed no image."
  cause: "Clinical Engineering found the external video cable partially disconnected at the monitor input."
  resolution: "Reseated and secured the cable and verified a stable test image on both the OEC 9800 display and external monitor."
helpfulDetails:
  - "Printer or video output affected"
  - "External device power status"
  - "Cable type and condition"
  - "Connector condition"
  - "Printer media status"
  - "Selected output"
  - "Known-good cable result"
  - "Known-good destination result"
  - "Output image quality"
  - "Final device status"
---
## What This Guide Helps With

Troubleshoots missing print or video output caused by power, cabling, selected output, destination equipment, media, configuration, or service-level interface faults.

## Step-by-Step Troubleshooting

### 1. Protect Patient Care and Determine Clinical Need

Confirm whether printing or external video is required for the current procedure. If the output is essential for clinical documentation or viewing, provide an approved alternate method before continuing.

Expected outcome: Patient care and required documentation are maintained.

### 2. Confirm Which Output Has Failed

Determine whether the problem affects the printer, external video monitor, recorder, or more than one output. Identify whether no signal is present, output is intermittent, or image quality is unacceptable.

Expected outcome: The failed output path is clearly identified.

### 3. Verify Power to External Equipment

Confirm that the printer, monitor, recorder, or other destination device is powered on and completes its normal startup.

Check accessible power cords and indicators.

Expected outcome: The destination equipment has stable power.

### 4. Check External Cables and Connectors

Inspect the video or printer cable for loose connections, bent contacts, damaged insulation, crushed sections, or incorrect seating.

Reconnect carefully without forcing connectors.

Expected outcome: The external signal path is securely connected.

### 5. Check Printer Media or Consumables When Applicable

For a printer problem, inspect accessible paper, media, cartridge, or other consumables as applicable to the installed printer. Verify correct loading and absence of obvious jams.

Expected outcome: The printer is ready to accept a print job.

### 6. Verify the Intended Output or Destination

Using normal operator-accessible controls, confirm that the correct external output or printing destination is selected when the system provides that option.

Do not enter unauthorized configuration menus.

Expected outcome: Output is directed to the intended accessory.

### 7. Test the Destination Independently When Possible

Use an approved known-good source or built-in accessory test, when available, to determine whether the external monitor or printer can function independently of the OEC 9800.

Expected outcome: The problem is isolated to the external accessory or the C-arm output path.

### 8. Substitute a Known-Good Cable or Accessory

If available and compatible, substitute a known-good cable, monitor, or printer connection to isolate the fault.

Expected outcome: If output returns with a known-good component, the defective external accessory or cable has been identified.

### 9. Perform Final Output Verification

After correcting the external cause, send a test print or display a controlled test image through the external video output. Confirm the image is complete, stable, and appropriately reproduced.

Expected outcome: The requested output functions normally and the original complaint cannot be reproduced. Troubleshooting can stop.

### 10. Escalate Persistent Output Failure

If the destination equipment and cable are known good but no output is available from the OEC 9800, remove the system from service if the failed output is required for safe or documented clinical use.

Expected outcome: A service-level output fault is appropriately escalated.

## If the Problem Persists

External power, media, cables, destination equipment, and normal output selection have been ruled out. Remaining causes may involve video-output hardware, printer interfaces, signal conversion, system configuration, image-processing electronics, or software.

The OEC 9800 should be:

- Removed from service when the failed output is clinically required.
- Labeled Out of Service.
- Sent for repair or bench evaluation.
- Evaluated using appropriate GE Healthcare documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Return to service only after the affected print or external video path has been verified.

Knowing when to isolate the external device before opening the imaging system is proper troubleshooting.

## Clinical Use Tip

When an external display is used for procedural viewing, verify the complete video path and displayed orientation before patient use.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Printer or video output affected
- External device power status
- Cable type and condition
- Connector condition
- Printer media status
- Selected output
- Known-good cable result
- Known-good destination result
- Output image quality
- Final device status

## Final Thought

External-output failures should be isolated one segment at a time: destination equipment, power, consumables, cable, connector, and output selection. Verify the complete path before escalating an internal interface problem.

That is successful troubleshooting.
