---
schemaVersion: 1
title: "Radiometer ABL90 FLEX PLUS Blood Gas Analyzer - Printer or Report Output Is Missing or Incomplete"
issueTitle: "Printer or Report Output Is Missing or Incomplete"
description: "Troubleshoots missing, partial, faint, or unavailable printed and electronic reports caused by paper, settings, connections, workflow, or output configuration."
assetType: "Blood Gas Analyzer"
manufacturer: "Radiometer"
model: "ABL90 FLEX PLUS"
slug: "radiometer-abl90-flex-plus-printer-or-report-output-is-missing-or-incomplete"
dateAdded: "2026-10-30"
taxonomyMode: "reuse"
ccr:
  complaint: "Laboratory staff reported that the ABL90 FLEX PLUS displayed complete patient results but the local printer produced blank reports."
  cause: "Clinical Engineering found the thermal paper roll had been installed in the incorrect orientation."
  resolution: "Reinstalled the approved paper correctly, printed multiple complete test reports successfully, verified readability, and returned the analyzer to normal use."
helpfulDetails:
  - "Whether the result displayed normally on the analyzer"
  - "Whether the issue affected local print, electronic output, or both"
  - "Paper condition and orientation"
  - "Printer feed behavior"
  - "Whether output was blank, faint, or incomplete"
  - "Manual versus automatic printing results"
  - "Report/output settings observed"
  - "Communication cable condition"
  - "Network or interface status"
  - "Whether other laboratory devices were affected"
  - "Destination system tested"
  - "End-to-end verification result"
  - "Final analyzer status"
---

## What This Guide Helps With

Troubleshoots missing, partial, faint, or unavailable printed and electronic reports caused by paper, settings, connections, workflow, or output configuration.

## Step-by-Step Troubleshooting

### 1. Protect Patient Results and Confirm an Alternate Reporting Method

If clinical decisions depend on the analyzer result, confirm the result is available through an approved alternate reporting path before troubleshooting the printer or report interface.

Do not discard or repeat patient testing solely because the printed copy is unavailable unless required by laboratory policy.

**Expected outcome:** Patient results remain accessible through an approved method while the reporting problem is evaluated.

### 2. Confirm What Output Is Failing

Determine whether the issue involves:

- No printed report
- Blank paper
- Partial printout
- Missing analytes
- Faint or unreadable print
- Electronic report not transmitted
- Printed output working while electronic output fails
- Electronic output working while local printing fails

Confirm whether the analytical results are visible on the analyzer itself.

**Expected outcome:** The problem is isolated to a specific output method rather than the analytical measurement itself. If the result is present and only one output destination is affected, continue troubleshooting that path.

### 3. Verify Analyzer Readiness and Result Completion

Confirm the analyzer completed the sample measurement normally and that the full expected result exists before evaluating the printer.

A report cannot contain values that were never generated or that the analyzer appropriately withheld.

**Expected outcome:** The analyzer has a complete valid result available for reporting. If missing information is due to an incomplete analytical result rather than output failure, address the analytical condition instead.

### 4. Inspect Printer Paper and Loading

For local printer problems, inspect the paper supply and verify that the correct approved paper is loaded properly.

Check for:

- Empty roll
- Incorrect orientation
- Folded or damaged paper
- Improper seating
- Jammed paper
- Debris around the accessible paper path

Do not force paper through the mechanism.

**Expected outcome:** Paper is correctly loaded and advances normally. If correcting the paper installation restores complete printing, troubleshooting can stop after a successful test report.

### 5. Inspect the Accessible Printer Path

Open only user-accessible printer areas and check for torn paper, labels, debris, or other obstruction.

If the printer feeds paper but produces blank output, verify the paper type and orientation before assuming a failed print mechanism.

**Expected outcome:** The accessible paper path is clear and correctly loaded. If clearing an obstruction restores printing, troubleshooting can stop after verification.

### 6. Verify Output and Print Settings

Review normal accessible settings to confirm local printing or the required report destination is enabled for the applicable workflow.

Determine whether the problem began after a configuration change, software update, service activity, or changes to laboratory workflow.

Do not modify restricted communication or clinical configuration without authorization.

**Expected outcome:** The intended report destination is enabled and the applicable normal settings are correct. If correcting an authorized setting restores output, troubleshooting can stop.

### 7. Compare Manual and Automatic Printing

If supported by the normal analyzer workflow, attempt to print an existing completed result manually and compare it with automatic printing after a test.

This helps distinguish a printer hardware issue from a workflow or automatic-output setting.

**Expected outcome:** Manual and automatic printing either both function or the failure is isolated to one workflow. If manual printing works and the automatic print setting is corrected, troubleshooting can stop.

### 8. Verify Electronic Output Connections When Applicable

If the missing report involves LIS, network, middleware, or another external destination, confirm the analyzer's external communication connection is secure.

Inspect accessible Ethernet or other communication cabling for looseness, damage, or incorrect connection. Compare with a known-good connection where appropriate.

Do not change network parameters without coordination with the responsible integration or IT team.

**Expected outcome:** External communication cabling is secure and the analyzer shows normal connectivity. If reconnecting a loose cable restores report transmission, troubleshooting can stop after end-to-end verification.

### 9. Determine Whether the Problem Is Device-Specific or Infrastructure-Specific

Check whether other analyzers or laboratory systems using the same external reporting destination are also affected.

If multiple devices cannot send reports, involve the appropriate LIS, middleware, integration, or network support team rather than repeatedly altering the ABL90 FLEX PLUS.

**Expected outcome:** The scope of the failure is identified as local to the analyzer or external infrastructure. If the external system is confirmed as the cause, document the handoff and stop device-level troubleshooting.

### 10. Perform End-to-End Functional Verification

After correcting the issue, generate or use an approved test result and confirm that the required information appears completely at the intended destination.

For printer problems, verify readable output without missing sections. For electronic reporting, confirm receipt at the intended system rather than relying only on a local “sent” indication.

**Expected outcome:** The complete report reaches the intended destination accurately and consistently. When this result is achieved, troubleshooting can stop and the analyzer may remain or return to service as appropriate.

## If the Problem Persists

If paper loading, accessible printer path, output settings, result completeness, external connections, and infrastructure conditions have been ruled out, the problem may involve the internal printer mechanism, print electronics, communication interface, software, report formatting, or service-level configuration.

The analyzer should be:

- Removed from service if required reporting cannot be reliably maintained and no approved alternate workflow exists
- Labeled **Out of Service** when continued use would create a patient-result documentation risk
- Sent for repair or bench evaluation
- Evaluated using appropriate Radiometer documentation and approved test equipment
- Repaired or configured only by qualified personnel

Do not disassemble the printer mechanism beyond authorized access, perform board-level repairs, or change network or reporting configuration without approval.

After repair or configuration correction, verify the complete reporting path from analyzer result generation through the intended clinical destination before return to service.

Knowing when a problem belongs to the analyzer versus the LIS, middleware, printer hardware, or network infrastructure is an important part of proper troubleshooting.

## Clinical Use Tip

Verify that the complete result reaches the clinical record or other approved destination; a successful local print does not prove electronic reporting is working.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Separate analytical problems from reporting problems before replacing hardware. Start with paper, workflow, settings, and connections, verify the full reporting path, escalate internal or infrastructure failures appropriately, and document both the cause and successful end-to-end verification.

That is successful troubleshooting.
