---
schemaVersion: 1
title: "STERIS AMSCO 600 Series Sterilizer - Printer, Cycle Record, or Data Logging Failure"
issueTitle: "Printer, Cycle Record, or Data Logging Failure"
description: "Use this guide when printed or electronic cycle records are missing, incomplete, unreadable, or unavailable despite otherwise normal sterilizer operation."
assetType: "Sterilizer"
manufacturer: "STERIS"
model: "AMSCO 600 Series"
slug: "steris-amsco-600-series-printer-cycle-record-or-data-logging-failure"
dateAdded: "2026-08-17"
taxonomyMode: "reuse"
ccr:
  complaint: "Sterile Processing reported that the AMSCO 600 Series completed cycles but no printed cycle record was produced."
  cause: "Clinical Engineering found the printer paper roll empty."
  resolution: "Installed the appropriate paper, verified proper paper feed and a complete legible record during an approved test cycle, and returned the sterilizer to service."
helpfulDetails:
  - "Printed versus electronic record affected."
  - "Cycle completion status."
  - "Paper condition and loading."
  - "Print quality."
  - "Date/time displayed."
  - "External cable condition."
  - "Other systems affected."
  - "Test print or test-cycle result."
  - "Record successfully transferred or printed."
  - "Final device status."
---

## What This Guide Helps With
Use this guide when printed or electronic cycle records are missing, incomplete, unreadable, or unavailable despite otherwise normal sterilizer operation.

## Step-by-Step Troubleshooting

### 1. Protect Sterilization Documentation Integrity
Do not allow a documentation problem to compromise load traceability or release practices.

Follow facility policy when required cycle records are unavailable, incomplete, or unreadable. Do not recreate or falsify missing sterilization records.

**Expected outcome:** Load release and recordkeeping remain compliant while the documentation issue is investigated.

### 2. Confirm the Exact Documentation Failure
Determine whether the problem involves:
- No printed record.
- Blank or faint printing.
- Paper not feeding.
- Incomplete printout.
- Missing electronic record.
- Incorrect date/time information.
- Intermittent data logging.
- Loss of communication with an external documentation system.

**Expected outcome:** The fault is narrowed to local printing, consumables, local data storage, configuration, or external communication.

### 3. Verify the Sterilizer Completed the Cycle
Confirm whether the sterilizer itself completed the intended cycle normally.

A missing printout does not prove that the cycle failed, and a successful printout does not prove sterilization performance by itself.

**Expected outcome:** Cycle performance and documentation performance are treated as separate issues.

### 4. Check Printer Paper and Loading
Inspect the printer for the correct paper presence and proper loading. Check for an empty roll, improperly routed paper, jam, or damaged leading edge.

Use only appropriate facility-approved consumables.

**Expected outcome:** Paper is present and feeds correctly. If correcting paper loading restores complete readable records, troubleshooting can stop after verification.

### 5. Inspect the Printer Area
Check accessible printer surfaces, cover, feed path, and paper exit for debris or obstruction.

Do not disassemble the printer mechanism beyond routine accessible areas.

**Expected outcome:** The paper path is clear and the printer cover is properly secured.

### 6. Test Normal Print or Record Function
Use normal user-accessible controls to generate an appropriate record or verify printing during an approved test cycle.

Do not alter service configuration to force printer output.

**Expected outcome:** A complete, legible record is produced. If so, verify repeatability and stop troubleshooting.

### 7. Verify Displayed Date and Time
Check the sterilizer's displayed date and time against facility expectations.

If incorrect, follow authorized facility procedures for adjustment. Do not enter restricted service menus or change validated configuration without authorization.

**Expected outcome:** The displayed date and time are correct or the discrepancy is documented for qualified configuration correction.

### 8. Check External Data Connections
If cycle records are transmitted to another system, inspect accessible network, serial, or other communication cabling for secure connections and visible damage.

Compare status with another known-good connection or port only when facility architecture and authorization permit.

**Expected outcome:** External cabling and infrastructure appear intact. If reconnecting a loose accessible cable restores logging, verify successful transfer and stop troubleshooting.

### 9. Determine Whether the Fault Is Local or Network-Wide
Check whether other sterilizers or devices using the same documentation platform are also unable to transmit records.

Coordinate with IT, networking, or the appropriate integration support team when multiple devices are affected.

**Expected outcome:** The problem is isolated to the sterilizer or identified as an infrastructure/system issue and routed appropriately.

### 10. Escalate Persistent Record Failure
If consumables, paper path, normal controls, displayed time, accessible cabling, and infrastructure status are satisfactory but printing or data logging remains unreliable, stop external troubleshooting.

Potential service-level categories include printer hardware, internal communication, storage, controller functions, configuration, or external integration software.

**Expected outcome:** The documentation system is repaired or formally evaluated before routine use resumes where records are required.

## If the Problem Persists
External consumable, connection, and infrastructure causes have been ruled out. Where required records cannot be reliably produced, **remove the sterilizer from service** or restrict its use according to facility policy, **label it Out of Service** when appropriate, and arrange qualified evaluation.

Use current STERIS documentation and approved service methods. Internal printer hardware, controller functions, storage, interfaces, and configuration should be repaired or configured only by qualified personnel.

Before return to normal service, verify successful cycle-record generation and any required external data transfer. Proper documentation is part of the sterilization process, not an optional convenience.

## Clinical Use Tip
When cycle documentation is required for load release, do not substitute handwritten assumptions for missing objective cycle records.

## Work Order Documentation (CCR Method)

CCR = Complaint, Cause, Resolution

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought
Separate sterilization performance from documentation performance, check consumables and connections before assuming internal failure, preserve traceability, escalate unreliable record systems, and clearly document the final verification.

That is successful troubleshooting.
