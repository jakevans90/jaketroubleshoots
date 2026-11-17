---
schemaVersion: 1
title: "Advanced Sterilization Products (ASP) AEROFLEX Endoscope Reprocessor (AER) - AUTOSURE MRC Test Fails or Does Not Produce a Pass/Fail Result"
issueTitle: "AUTOSURE MRC Test Fails or Does Not Produce a Pass/Fail Result"
description: "AUTOSURE minimum recommended concentration testing that fails, stalls, or does not produce a usable pass/fail result despite normal cycle preparation."
assetType: "Endoscope Reprocessor (AER)"
manufacturer: "Advanced Sterilization Products (ASP)"
model: "AEROFLEX"
slug: "advanced-sterilization-products-asp-aeroflex-autosure-mrc-test-fails-or-does-not-produce-a-pass-fail-result"
dateAdded: "2026-11-17"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported the AEROFLEX AUTOSURE MRC test would start but never displayed a pass or fail result."
  cause: "Clinical Engineering found the installed AUTOSURE test consumable was damaged and was not seating correctly in the test position."
  resolution: "Replaced the damaged consumable with an approved known-good test, confirmed proper placement, and verified a complete test with a valid result."
helpfulDetails:
  - "Exact AUTOSURE message displayed"
  - "Whether the test started or remained unavailable"
  - "AERO-OPA chemistry status"
  - "Consumable lot or package condition"
  - "Result with known-good consumable"
  - "Test placement condition"
  - "Any related cycle alarms"
  - "Result before and after correction"
  - "Final device status"
---

## What This Guide Helps With

AUTOSURE minimum recommended concentration testing that fails, stalls, or does not produce a usable pass/fail result despite normal cycle preparation.

## Step-by-Step Troubleshooting

### 1. Protect Patient Safety and Reprocessing Continuity
Do not release an endoscope for patient use when disinfectant concentration verification is incomplete, failed, or uncertain. Remove affected scopes from the normal workflow and use an alternate validated reprocessor or reprocessing process according to facility policy.

Expected outcome: No endoscope is returned to clinical use based on an incomplete or questionable MRC verification. If an alternate validated workflow restores continuity, continue troubleshooting the AEROFLEX out of clinical service.

### 2. Confirm the Exact AUTOSURE Failure
Have staff describe whether the test fails, never begins, remains in progress, produces no result, or completes without a clear pass/fail indication. Review the displayed message and cycle record without clearing useful information.

Expected outcome: The failure is narrowed to initiation, detection, processing, or result reporting. If the test completes normally on repeat setup and produces a valid result, troubleshooting can stop after final verification.

### 3. Verify Normal AEROFLEX Readiness
Confirm the unit powers normally, completes startup, shows no unrelated active faults, and is otherwise ready for processing. Verify the basin and accessible test areas are clean and free of residue or standing liquid that could interfere with normal operation.

Expected outcome: The system is fully initialized with no unrelated condition preventing the AUTOSURE sequence. Correct any simple external readiness issue and repeat the test.

### 4. Inspect the AUTOSURE Consumable and Handling Conditions
Verify the correct approved AUTOSURE MRC test consumable is being used, packaging is intact, and it has been stored and handled according to applicable instructions. Check for contamination, damage, moisture exposure, or an obviously unusable test device.

Expected outcome: A correct, intact test consumable is available. If replacing a questionable consumable restores a valid pass/fail result, troubleshooting can stop.

### 5. Check Test Placement and Accessible Interfaces
Inspect the location where the AUTOSURE test device is inserted, positioned, or presented to the system. Look for obstruction, residue, misalignment, damaged guides, or incomplete seating.

Expected outcome: The test device can be positioned correctly without force and remains properly seated. If reseating it restores normal testing, troubleshooting can stop.

### 6. Use a Known-Good Approved Test Consumable
When permitted by facility procedure, repeat the AUTOSURE test using a known-good approved consumable from a different package or lot. Do not repeatedly consume test supplies if the system clearly cannot initiate or detect the test.

Expected outcome: A known-good test produces a clear result. If multiple approved consumables fail identically, the problem is likely beyond the individual test strip or device.

### 7. Verify Chemistry and Cycle Preconditions
Confirm the AERO-OPA chemistry is recognized and available and that no chemistry-related warning, expired-use condition, or incomplete container recognition is present. Do not bypass chemistry verification.

Expected outcome: The system recognizes the required chemistry and allows the MRC verification sequence under normal conditions. If correcting an external chemistry-recognition issue restores AUTOSURE testing, troubleshooting can stop.

### 8. Perform Final Functional Verification
After correcting an external cause, run the approved verification sequence and confirm the AUTOSURE process completes with an unambiguous result and normal cycle documentation.

Expected outcome: The system provides the expected pass/fail determination and records it correctly. The AER may be returned to service only after required operational checks are satisfactory.

### 9. Escalate an Unresolved AUTOSURE Failure
If known-good consumables, proper placement, normal chemistry recognition, and normal system readiness do not restore the test, stop external troubleshooting.

Expected outcome: The AEROFLEX is removed from service and referred for qualified service evaluation rather than being used without reliable MRC verification.

## If the Problem Persists

Common external causes involving the AUTOSURE consumable, placement, chemistry availability, and system readiness have been ruled out. Remaining causes may involve test detection, internal sensing, software, configuration, or other service-level functions.

Remove the device from service, label it Out of Service, and send it for repair or bench evaluation. Evaluate it using appropriate ASP documentation and approved test equipment. Repair or configuration changes should be performed only by qualified personnel.

Do not return the AEROFLEX to service until AUTOSURE testing operates reliably and required operational verification has been completed. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never release an endoscope when required disinfectant concentration verification is missing, inconclusive, or unreliable.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Reliable MRC verification is part of safe high-level disinfection. Rule out consumables, placement, chemistry status, and basic operating conditions before suspecting internal failure, and document both the cause and successful verification clearly.

That is successful troubleshooting.
