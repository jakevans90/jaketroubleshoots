---
schemaVersion: 1
title: "GE Healthcare OEC One CFD C-Arm - Display Monitor Is Blank, Flickers, or Shows the Wrong Image Source"
issueTitle: "Display Monitor Is Blank, Flickers, or Shows the Wrong Image Source"
description: "Use this guide when a display is blank, unstable, flickering, or presenting the wrong image or workstation source."
assetType: "C-Arm"
manufacturer: "GE Healthcare"
model: "OEC One CFD"
slug: "ge-healthcare-oec-one-cfd-display-monitor-is-blank-flickers-or-shows-the-wrong-image-source"
dateAdded: "2026-11-23"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that the OEC One CFD display intermittently went blank when the monitor assembly was repositioned."
  cause: "Clinical Engineering found a loose external video connection that changed state when the display was moved."
  resolution: "Clinical Engineering secured the connection and verified stable live and stored-image display through repeated monitor repositioning and functional testing."
helpfulDetails:
  - "Display affected"
  - "Blank, flicker, frozen, or wrong-source symptom"
  - "Monitor power indication"
  - "Power-cable condition"
  - "Video-cable and connector condition"
  - "Source selection observed"
  - "Comparison with another display"
  - "Known-good cable substitution"
  - "Whether movement affects the symptom"
  - "Final display and imaging verification"
  - "Final device status"
---

## What This Guide Helps With

Use this guide when a display is blank, unstable, flickering, or presenting the wrong image or workstation source.

## Step-by-Step Troubleshooting

### 1. Protect Clinical Workflow

Do not continue a procedure if the required fluoroscopic image cannot be viewed reliably. Move to another verified display or imaging system if the operator cannot safely monitor the procedure.

Expected outcome: Clinical imaging is not performed using an unreliable display.

### 2. Confirm Which Display Is Affected

Determine whether one monitor or all displays are affected and whether the problem is a blank screen, intermittent image, flicker, incorrect source, frozen image, or loss of clinical video only.

Expected outcome: The affected display and symptom are clearly identified.

### 3. Verify the Monitor Has Power

Check the monitor's normal power indication and verify that any externally accessible power connection is secure. Inspect the power cable and connection for damage.

Expected outcome: The display has stable power. If restoring an external power connection corrects the issue, proceed to functional verification.

### 4. Inspect External Video Connections

Inspect accessible video cables, connectors, adapters, and strain reliefs for looseness, damage, contamination, or partial insertion. Reseat external connections intended for normal service access.

Expected outcome: All accessible video connections are secure. If the image becomes stable, test the monitor through normal system operation before closing the work order.

### 5. Verify the Correct Source Is Selected

Confirm that the display is set to the intended normal video source or input. Do not change protected system routing configuration without authorization.

Expected outcome: The intended imaging source is displayed. If an incorrect input selection caused the problem, correct it and verify normal operation.

### 6. Compare With Another Display

If another integrated or approved display shows the correct image, compare behavior. This helps distinguish an image-generation problem from an individual monitor or cable problem.

Expected outcome: The failure is narrowed to a display path, source-selection problem, or broader workstation output issue.

### 7. Substitute a Known-Good Accessible Cable When Appropriate

If an approved compatible external video cable can be safely substituted, use it to determine whether the existing cable is intermittent.

Expected outcome: The known-good cable produces a stable image. If so, replace the defective cable and verify the complete display path.

### 8. Check for Position-Related Intermittency

Gently move only externally accessible cables and normal monitor positioning components while observing the display. Do not stress connectors or open monitor housings.

Expected outcome: The image remains stable. If flicker occurs consistently when an external cable is moved, remove or replace the affected cable.

### 9. Perform Final Image-Display Verification

Verify that the correct live fluoroscopic image, stored images, menus, and expected workstation source are displayed without flicker, blanking, distortion, or unintended switching.

Expected outcome: Display operation is stable and the correct source is shown consistently. If successful, troubleshooting can stop.

### 10. Escalate Persistent Display Failure

If the monitor remains blank, flickers with known-good external connections, or displays an incorrect source despite normal user settings, stop before opening the monitor or altering internal video-routing configuration.

Expected outcome: The affected system or display is removed from service as required and referred for qualified repair.

## If the Problem Persists

External power, video connections, source selection, and accessible cabling have been ruled out. The remaining problem may involve the monitor, internal video distribution, workstation graphics output, software, internal cabling, or protected routing configuration.

Remove the device from service if reliable clinical viewing is unavailable, label it Out of Service, and send it for repair or bench evaluation. Use appropriate GE Healthcare documentation and approved test equipment. Internal display repair or protected routing configuration should be performed only by qualified personnel.

Before return to service, verify all required display sources, live and stored imaging, image stability, and monitor operation through normal C-arm use.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A monitor that intermittently blanks during C-arm movement should be treated as unreliable even if the image immediately returns.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Maintain a reliable clinical image path, check power, cabling, and source selection before assuming monitor failure, verify stability under normal movement, and escalate internal video faults appropriately.

That is successful troubleshooting.
