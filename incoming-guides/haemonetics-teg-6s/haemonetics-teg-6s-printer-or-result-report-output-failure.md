---
schemaVersion: 1
title: "Haemonetics TEG 6s Viscoelastic Hemostasis Analyzer - Printer or Result Report Output Failure"
issueTitle: "Printer or Result Report Output Failure"
description: "Addresses missing or poor report output caused by printer power, media, connection, selection, software, or external reporting-path issues."
assetType: "Viscoelastic Hemostasis Analyzer"
manufacturer: "Haemonetics"
model: "TEG 6s"
slug: "haemonetics-teg-6s-printer-or-result-report-output-failure"
dateAdded: "2026-09-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that completed TEG 6s results would not print to the connected report printer."
  cause: "Clinical Engineering found the printer data cable was loose at the printer connection."
  resolution: "Reseated the cable, printed multiple verified reports successfully, confirmed complete readable output, and returned the system to normal service."
helpfulDetails:
  - "Whether local results were available."
  - "Printer power state."
  - "Printer fault indicators."
  - "Paper or media condition."
  - "Cable type and condition."
  - "Known-good cable result."
  - "Output destination selected."
  - "Test report result."
  - "Whether other printers were tested."
  - "Final report status."
---
## What This Guide Helps With

Addresses missing or poor report output caused by printer power, media, connection, selection, software, or external reporting-path issues.

## Step-by-Step Troubleshooting

### 1. Protect Result Availability

If printed reports are part of the clinical workflow, confirm results remain available through another approved method while printer output is unavailable.

Do not delay critical communication solely because a printer is malfunctioning.

**Expected outcome:** Clinicians retain access to verified results through an alternate approved pathway.

### 2. Confirm the Exact Output Failure

Determine whether:
- Nothing prints.
- A blank page prints.
- Output is incomplete.
- Printing is delayed.
- Only some reports fail.
- The analyzer produces results but no print command is completed.

**Expected outcome:** The printer or report-output failure is clearly defined.

### 3. Verify Printer Power and Status

If an external printer is used, confirm:
- It is powered on.
- No obvious fault indicator is present.
- Power connection is secure.
- It is in a normal ready state.

**Expected outcome:** The printer is powered and ready. Correct simple power or ready-state issues and retest.

### 4. Inspect Paper or Media

Check:
- Paper is present.
- Media is loaded correctly.
- No visible jam exists.
- Paper path is unobstructed.
- Covers are fully closed.

Do not perform deep printer disassembly.

**Expected outcome:** Media is properly loaded and the printer is mechanically ready.

### 5. Inspect Data Connections

Check accessible USB, Ethernet, or other approved printer connection for:
- Loose connectors.
- Damaged cable.
- Partially seated plug.
- Physical damage.

Reseat connections where appropriate.

**Expected outcome:** The printer data connection is secure.

### 6. Substitute a Known-Good Cable or Printer Where Practical

Use a known-good compatible cable or approved printer comparison if available.

**Expected outcome:** Output resumes with the substitute component, isolating the external accessory as the cause.

### 7. Verify Report Selection and Output Destination

Confirm the analyzer or connected system is targeting the expected printer or report destination.

Do not change protected configuration without authorization.

**Expected outcome:** The intended output destination is selected.

### 8. Confirm Results Exist Before Troubleshooting Printing

Verify that the analyzer generated and stored or displayed the result locally.

If the result itself is missing, troubleshoot assay generation rather than printer output.

**Expected outcome:** A valid result is available for printing.

### 9. Perform a Test Report

Use an approved non-patient or previously verified result, where allowed, to confirm report generation and print output.

Check:
- Complete content.
- Readability.
- Correct patient or test identification where applicable.
- Stable repeated printing.

**Expected outcome:** The report prints completely and legibly. Troubleshooting can stop.

### 10. Escalate Persistent Output Failure

If the printer is functional, connections are verified, and the analyzer still cannot generate or route reports, escalate for software, configuration, interface, or hardware evaluation.

**Expected outcome:** The unresolved output issue is moved to qualified technical support without affecting patient-result integrity.

## If the Problem Persists

External printer power, media, cable, output destination, and local result availability have been verified. Remaining causes may involve printer electronics, analyzer software, driver or interface configuration, network printing, or another service-level problem.

The affected equipment should be:
- Removed from service if the inability to produce required reports compromises the clinical workflow.
- Labeled **Out of Service** when appropriate.
- Sent for repair or bench evaluation.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Verify complete and accurate report output before normal service resumes.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

A printing failure should never prevent a verified result from reaching the clinical team; use the laboratory's approved alternate reporting process.

## Work Order Documentation (CCR Method)

**CCR = Complaint, Cause, Resolution**

## Helpful Details to Include (If Known)

- Whether local results were available.
- Printer power state.
- Printer fault indicators.
- Paper or media condition.
- Cable type and condition.
- Known-good cable result.
- Output destination selected.
- Test report result.
- Whether other printers were tested.
- Final report status.

## Final Thought

Separate report-generation problems from printer problems, verify power and connections first, confirm the result itself is intact, and require complete readable output before closing the work order.

That is successful troubleshooting.
