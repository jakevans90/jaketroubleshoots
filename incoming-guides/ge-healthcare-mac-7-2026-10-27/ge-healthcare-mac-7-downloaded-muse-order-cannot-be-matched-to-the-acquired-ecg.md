---
schemaVersion: 1
title: "GE Healthcare MAC 7 Electrocardiograph (EKG) Machine - Downloaded MUSE Order Cannot Be Matched to the Acquired ECG"
issueTitle: "Downloaded MUSE Order Cannot Be Matched to the Acquired ECG"
description: "Troubleshoot downloaded MUSE orders that cannot be associated with an acquired ECG, including patient-data, order-selection, network, workflow, and configuration causes."
assetType: "Electrocardiograph (EKG) Machine"
manufacturer: "GE Healthcare"
model: "MAC 7"
slug: "ge-healthcare-mac-7-downloaded-muse-order-cannot-be-matched-to-the-acquired-ecg"
dateAdded: "2026-10-27"
taxonomyMode: "reuse"
ccr:
  complaint: "Clinical staff reported that a downloaded MUSE order was visible on the MAC 7 but could not be matched to the patient's acquired ECG."
  cause: "Clinical Engineering found that the wrong downloaded encounter had been selected while the correct patient order was available after refreshing the order list."
  resolution: "Selected the correct order, verified patient information, completed a controlled ECG workflow, and confirmed correct association and transmission to MUSE."
helpfulDetails:
  - "Exact order-matching symptom or displayed message."
  - "Patient/order workflow being used."
  - "Whether the intended order downloaded."
  - "Whether the issue affected one or multiple patients."
  - "Wired or wireless network status."
  - "Cable or network connection tested."
  - "Known-good device or location comparison."
  - "Configuration observations."
  - "MUSE communication status."
  - "Results before and after correction."
  - "Final device status."
---

## What This Guide Helps With

Troubleshoot downloaded MUSE orders that cannot be associated with an acquired ECG, including patient-data, order-selection, network, workflow, and configuration causes.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve the ECG

Do not delay a clinically necessary ECG while troubleshooting order matching. If the MAC 7 cannot reliably associate the study with the intended patient, use another verified workflow or device according to facility policy.

Do not intentionally attach an ECG to an uncertain patient record merely to complete the workflow.

**Expected outcome:** The patient receives required care while the questionable order or record remains isolated from clinical use.

### 2. Confirm the Exact Reported Condition

Determine whether:

- The MUSE order downloads but cannot be selected for the acquired ECG.
- The expected order is missing.
- Multiple similar orders are displayed.
- The ECG was acquired before the correct order was selected.
- The problem affects one patient, several patients, or all downloaded orders.
- The device displays any message associated with order matching or transmission.

Record the exact workflow that produced the problem.

**Expected outcome:** The failure is narrowed to order retrieval, order selection, patient matching, ECG association, or transmission. If the correct order can now be selected and associated without ambiguity, troubleshooting can stop after verification.

### 3. Verify the Patient and Order Information

Compare the downloaded order with the intended patient using the identifiers available in the approved clinical workflow. Check for obvious discrepancies such as:

- Wrong patient selected.
- Duplicate or similar patient records.
- Incorrect encounter or order selected.
- Missing required demographic or order information.
- Manually entered information that differs from the downloaded order.

Do not alter patient identifiers merely to force a match.

**Expected outcome:** The ECG and downloaded order clearly refer to the same intended patient and encounter. If correcting an obvious workflow selection resolves the problem, verify the completed record and stop troubleshooting.

### 4. Refresh the Order List Through the Normal Workflow

Exit the affected order selection screen and perform a normal order refresh or retrieval using the authorized MAC 7 workflow.

Confirm whether the intended order appears after the refresh.

Avoid unauthorized service menus or configuration changes.

**Expected outcome:** The current MUSE order list is available and the intended order can be selected. If the ECG can then be correctly associated and processed, troubleshooting can stop.

### 5. Verify Network Connectivity

Check the MAC 7 network connection used for MUSE communication.

For wired connections:

- Inspect the Ethernet cable and connectors.
- Confirm the connector is fully seated.
- Inspect for damaged cable ends or strain.
- Test with a known-good approved cable or network connection when appropriate.

For wireless configurations, verify the device indicates normal network connectivity without changing security settings.

Determine whether other network-dependent functions are also affected.

**Expected outcome:** The MAC 7 has stable network connectivity. If restoring an external network connection restores order matching, verify normal operation and stop troubleshooting.

### 6. Compare With Another Known-Good Workflow

If available, determine whether another MAC 7 or approved ECG workstation on the same clinical system can retrieve and match the same type of MUSE order.

This comparison can help distinguish between:

- A single-device problem.
- A network-segment problem.
- A MUSE/interface problem.
- A patient/order-specific problem.

Do not use another patient's information as a test record.

**Expected outcome:** The comparison identifies whether the issue follows the MAC 7, the network location, or the MUSE/order workflow.

### 7. Verify Relevant Device Configuration

Using authorized configuration access, verify the MAC 7 remains configured for the intended facility workflow, including the expected MUSE destination or order-management configuration.

Compare relevant settings with a known-good equivalent device if permitted.

Do not change configuration values without an approved reference or documented facility standard.

**Expected outcome:** Required communication and workflow configuration matches the approved configuration. If an authorized correction restores matching, verify the complete workflow and stop troubleshooting.

### 8. Test With a Controlled Non-Patient Workflow

When facility procedures and test resources allow, perform a controlled test using an approved test record or training workflow.

Verify that the MAC 7 can:

1. Retrieve the intended order.
2. Select the correct record.
3. Acquire an ECG from an appropriate simulator if required.
4. Associate the acquisition with the order.
5. Complete the expected transmission or storage workflow.

Do not create fictitious clinical records in a production system unless specifically authorized.

**Expected outcome:** Order retrieval, ECG association, and downstream processing operate normally. If all functions pass, the device may be returned to service according to facility policy.

### 9. Escalate if Matching Remains Unreliable

Remove the MAC 7 from service if patient/order association cannot be performed reliably or if there is a reasonable risk of attaching an ECG to the wrong patient record.

Do not attempt internal board-level repair or unsupported changes to MUSE integration settings.

**Expected outcome:** An unresolved patient-identification or order-matching problem is prevented from affecting clinical records and is escalated appropriately.

## If the Problem Persists

If patient information, order selection, external connectivity, authorized configuration, and the normal workflow have been verified, common external causes have been ruled out.

The remaining problem may involve device software, interface configuration, MUSE integration, network infrastructure, order-management mapping, or another service-level issue.

The MAC 7 should be:

- Removed from service when reliable patient/order association cannot be assured.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation as appropriate.
- Evaluated using current manufacturer documentation and approved test equipment.
- Repaired or configured only by qualified personnel.

Coordinate with the appropriate MUSE, interface, or network support team when evidence indicates the problem is outside the electrocardiograph.

Before return to service, verify correct order retrieval, patient association, ECG acquisition, storage, and transmission.

Knowing when to stop external troubleshooting rather than risking an incorrect patient record is proper troubleshooting.

## Clinical Use Tip

Never force an ECG into a questionable patient or order record; preserve the tracing and resolve patient identity before completing the clinical association.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- rendered from front matter -->

## Final Thought

Protect patient identity first, verify the clinical workflow and external communication path before assuming an internal failure, escalate integration problems appropriately, and clearly document what was found and verified.

That is successful troubleshooting.
