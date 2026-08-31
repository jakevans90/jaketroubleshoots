---
schemaVersion: 1
title: "Stryker Neptune Surgical Fluid Management System - Manifold, Port, or Disposable Not Recognized"
issueTitle: "Manifold, Port, or Disposable Not Recognized"
description: "Use when the Neptune does not recognize an installed manifold, suction port, or compatible disposable despite apparently normal installation."
assetType: "Surgical Fluid Management System"
manufacturer: "Stryker"
model: "Neptune"
slug: "stryker-neptune-manifold-port-or-disposable-not-recognized"
dateAdded: "2026-08-31"
taxonomyMode: "reuse"
ccr:
  complaint: "OR staff reported that the Neptune would not recognize the installed suction manifold."
  cause: "Clinical Engineering found that the original disposable would not seat and recognize correctly, while a known-good compatible manifold was recognized normally."
  resolution: "Replaced the suspect disposable, verified stable recognition and normal suction operation, and returned the unit to service after functional verification."
helpfulDetails:
  - "Exact displayed message or indicator condition"
  - "Affected manifold or port"
  - "Disposable type and condition"
  - "Whether the disposable was newly installed"
  - "Evidence of contamination or incomplete seating"
  - "Known-good disposable test result"
  - "Results from another available port"
  - "Recognition status before and after correction"
  - "Final device status"
---
## What This Guide Helps With

Use when the Neptune does not recognize an installed manifold, suction port, or compatible disposable despite apparently normal installation.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Suction Availability

If the Neptune is supporting an active procedure and suction availability is unreliable, provide an alternate verified suction source before troubleshooting.

Do not manipulate contaminated disposables or waste connections while they are actively required for patient care. Follow appropriate PPE and infection-control precautions.

**Expected outcome:** Patient care continues with reliable suction while the Neptune is evaluated. If alternate suction is unavailable, remove the Neptune from clinical dependence before proceeding.

### 2. Confirm the Exact Recognition Problem

Identify which manifold, port, or disposable is not being recognized. Note any displayed message, unavailable function, indicator condition, or change that occurred immediately before the problem.

Determine whether the problem affects one connection or every compatible connection.

**Expected outcome:** The affected disposable or connection is clearly identified. If the issue was caused by an incorrect selection or incomplete setup and recognition returns after correction, troubleshooting can stop after functional verification.

### 3. Inspect the Disposable for Correct Type and Condition

Verify that the disposable is appropriate for the Neptune configuration in use and has not been damaged, deformed, contaminated at the interface, or previously used beyond its intended application.

Do not attempt to modify or bypass disposable-recognition features.

**Expected outcome:** The disposable is compatible, intact, and properly prepared for installation. Replace a questionable disposable with an approved known-good item when appropriate.

### 4. Remove and Reinstall the Disposable

Using appropriate PPE, remove the affected manifold or disposable according to the normal external installation method. Inspect the mating surfaces for debris, fluid contamination, deformation, or incomplete engagement.

Reinstall it fully without forcing the connection.

**Expected outcome:** The disposable seats securely and is recognized. If recognition is restored and remains stable during functional testing, troubleshooting can stop.

### 5. Inspect the Port and External Interface

Inspect the affected port for visible contamination, dried material, damaged guides, bent or obstructed interface features, or evidence that the disposable cannot seat completely.

Clean only external surfaces using approved methods. Do not insert tools into sensing mechanisms or disassemble the port.

**Expected outcome:** The interface is clean and unobstructed. If recognition returns after approved external cleaning and reseating, proceed to final verification.

### 6. Test With a Known-Good Compatible Disposable

Install a new or verified known-good compatible disposable.

Compare the result with the original item.

**Expected outcome:** A known-good disposable is recognized normally. If so, remove the suspect disposable from use and complete functional verification. If multiple known-good disposables fail on the same port, suspect a device-side recognition problem.

### 7. Compare Other Available Ports When Applicable

If the system configuration permits, test another appropriate port with a known-good compatible disposable.

Do not change clinical configuration solely to work around a suspected defective port during patient care.

**Expected outcome:** Other ports recognize compatible disposables normally. A problem isolated to one port supports removing the unit from service for evaluation if that port is required for intended use.

### 8. Verify Normal Operation After Correction

Confirm the disposable remains recognized through normal startup and readiness checks. Verify suction or associated functionality without introducing fluid into inappropriate areas.

**Expected outcome:** Recognition is stable and the associated function operates normally. If all checks pass, troubleshooting is complete and the unit may proceed through applicable return-to-service requirements.

### 9. Escalate an Unresolved Recognition Failure

If compatible known-good disposables remain unrecognized, recognition is intermittent, or the external interface appears damaged, stop external troubleshooting.

**Expected outcome:** The Neptune is removed from service and referred for qualified bench evaluation rather than used with unreliable disposable detection.

## If the Problem Persists

Common external causes such as incorrect installation, disposable damage, contamination, incomplete seating, and a defective disposable have been ruled out.

The remaining problem may involve the disposable-recognition system, port sensing hardware, internal connections, configuration, or another service-level condition.

The device should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate Stryker documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

After repair, perform appropriate functional and safety verification before returning the Neptune to clinical use. Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Never rely on a Neptune with intermittent disposable recognition during an active procedure; establish alternate suction before removing it from service.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter; optional explanatory prose may follow. -->



## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Protect the patient first, then verify the disposable, seating, port condition, and known-good substitutions before assuming an internal recognition failure. Escalate unresolved or intermittent recognition problems and document the complaint, cause, correction, and final verification clearly.

That is successful troubleshooting.
