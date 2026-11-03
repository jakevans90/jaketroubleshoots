---
schemaVersion: 1
title: "Fresenius Kabi Ivenix Infusion System Infusion Pump - Barcode Scanner, Patient ID, or Clinician Authentication Fails"
issueTitle: "Barcode Scanner, Patient ID, or Clinician Authentication Fails"
description: "Barcode reading, patient identification, clinician authentication, badge acceptance, scanner communication, workflow configuration, or network-related identification failures."
assetType: "Infusion Pump"
manufacturer: "Fresenius Kabi"
model: "Ivenix Infusion System"
slug: "fresenius-kabi-ivenix-infusion-system-barcode-scanner-patient-id-or-clinician-authentication-fails"
dateAdded: "2026-11-03"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported that one Ivenix pump would not consistently scan patient wristband barcodes."
  cause: "Clinical Engineering found dried cleaning residue covering part of the scanner window while known-good wristbands scanned normally after cleaning."
  resolution: "Cleaned the scanner window using the approved method, verified successful scans with multiple known-good identifiers and correct patient association, and returned the pump to service."
helpfulDetails:
  - "Type of identifier failing"
  - "Barcode or badge physical condition"
  - "Scanner-window condition"
  - "Whether scanner detects any barcode"
  - "Network status"
  - "Patient encounter status"
  - "Clinician credential status"
  - "Other pumps affected"
  - "Known-good identifier comparison"
  - "Restart result"
  - "Correct patient/clinician association verified"
  - "Final device status"
---

## What This Guide Helps With

Barcode reading, patient identification, clinician authentication, badge acceptance, scanner communication, workflow configuration, or network-related identification failures.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Preserve the Workflow

Do not delay clinically necessary therapy solely because barcode or authentication functions are unavailable. Clinical staff should follow the facility-approved fallback identification and programming workflow.

Expected outcome: Patient care continues safely while identification functions are evaluated.

### 2. Confirm Which Function Is Failing

Determine whether the pump cannot scan any barcode, fails only with patient bands, rejects clinician badges, accepts the scan but does not associate the patient, or loses authentication after successful login.

Expected outcome: The specific failure point is identified.

### 3. Inspect the Barcode or Credential

Check whether the barcode or badge is damaged, wrinkled, wet, faded, partially covered, poorly printed, or otherwise difficult to read.

Expected outcome: The identifier is physically readable. If a replacement wristband, label, or credential resolves the issue, troubleshooting can stop after verification.

### 4. Clean and Inspect the Scanner Window

Inspect the accessible scanner window for residue, scratches, adhesive, dust, or dried cleaning solution. Clean it only using an approved method.

Expected outcome: The scanner window is clean and unobstructed. If scanning returns to normal, verify several identifiers and stop.

### 5. Check Scan Position and Environment

Verify normal scan distance, angle, and lighting conditions without relying on extreme positioning. Check for strong glare or environmental conditions that may interfere with scanning.

Expected outcome: The scanner consistently detects supported barcodes under normal conditions.

### 6. Test Multiple Known-Good Identifiers

Use approved test barcodes, known-good staff credentials, or another valid identifier appropriate to the workflow.

Expected outcome: The test distinguishes a single damaged barcode from a scanner or system problem.

### 7. Determine Whether the Problem Is Local or Widespread

Check whether other Ivenix pumps in the same unit can scan and authenticate normally and whether the same credential works elsewhere.

Expected outcome: A pump-specific problem is separated from an enterprise identity or barcode-system issue.

### 8. Verify Network Connectivity

If scanning succeeds but patient identification or clinician authentication does not complete, confirm the pump is connected to the expected network.

Expected outcome: Network communication is available for systems that require server validation.

### 9. Check Patient and Clinician Context

Verify that the intended patient encounter is active and the clinician credential is valid within the normal hospital system. Clinical Engineering should not bypass expired or unauthorized credentials.

Expected outcome: Valid identity records are available to the workflow.

### 10. Perform a Normal Restart if Appropriate

With the pump out of patient use, restart it normally and allow it to reconnect to the network. Do not change security or authentication configuration outside authorized procedures.

Expected outcome: Scanner and authentication services initialize normally.

### 11. Compare With a Known-Good Pump

Use the same known-good barcode or credential on another Ivenix pump under similar conditions.

Expected outcome: The comparison confirms whether the problem follows the pump, the credential, or the infrastructure.

### 12. Verify the Complete Identification Workflow

Confirm that scanning results in the correct patient, clinician, or medication context without mismatches or stale associations.

Expected outcome: Barcode capture and downstream identification work correctly. Troubleshooting can stop.

## If the Problem Persists

External causes such as damaged barcodes, dirty scanner windows, scanning technique, invalid credentials, incorrect patient context, and basic network connectivity have been ruled out. Persistent problems may involve the scanner hardware, identity-management service, integration middleware, network security, device configuration, or vendor-level software.

Remove the pump from service if reliable identification is required for its intended workflow and cannot be assured. Label it Out of Service and send it for appropriate evaluation. Use approved Fresenius Kabi documentation and authorized IT/security support where required.

Do not bypass authentication controls or create unapproved credentials as a troubleshooting method.

Knowing when to stop external troubleshooting is proper troubleshooting.

## Clinical Use Tip

Always confirm that a successful scan resolves to the correct patient or clinician rather than assuming the barcode read alone proves the workflow is correct.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Identification failures can originate from the barcode, scanner, network, or authentication system. Verify each part in order, maintain a safe fallback workflow, and never bypass security controls to force a result.

That is successful troubleshooting.
