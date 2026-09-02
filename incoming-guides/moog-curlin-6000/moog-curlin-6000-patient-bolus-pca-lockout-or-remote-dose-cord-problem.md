---
schemaVersion: 1
title: "Moog CURLIN 6000 Infusion Pump - Patient Bolus, PCA Lockout, or Remote Dose Cord Problem"
issueTitle: "Patient Bolus, PCA Lockout, or Remote Dose Cord Problem"
description: "Troubleshoots patient-dose activation problems caused by remote cord connection, accessory damage, programmed therapy restrictions, control state, or pump recognition failure."
assetType: "Infusion Pump"
manufacturer: "Moog"
model: "CURLIN 6000"
slug: "moog-curlin-6000-patient-bolus-pca-lockout-or-remote-dose-cord-problem"
dateAdded: "2026-09-02"
taxonomyMode: "reuse"
ccr:
  complaint: "Nursing reported the patient's remote dose button intermittently failed to register requests on the CURLIN 6000."
  cause: "Clinical Engineering found the remote dose cord had an intermittent connection, while a known-good compatible cord operated consistently."
  resolution: "Replaced the defective remote dose cord, verified reliable dose-request recognition in an approved nonpatient test configuration, and returned the pump to service."
helpfulDetails:
  - "Patient-dose symptom reported"
  - "Displayed response to dose request"
  - "Whether a lockout condition was active"
  - "Cord and button condition"
  - "Connector condition"
  - "Known-good cord result"
  - "Cross-test result"
  - "Intermittent behavior"
  - "Therapy configuration observed"
  - "Final functional test"
  - "Final device status"
---
## What This Guide Helps With
Troubleshoots patient-dose activation problems caused by remote cord connection, accessory damage, programmed therapy restrictions, control state, or pump recognition failure.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Maintain Therapy
If patient-controlled dosing is required and cannot be delivered reliably, notify the clinical team and provide an approved alternate method or verified pump. Do not troubleshoot the active PCA pathway while the patient depends on it.

**Expected outcome:** The patient's prescribed analgesia or therapy is maintained safely.

### 2. Confirm the Exact Complaint
Determine whether the patient button does nothing, works intermittently, appears accepted but no dose is delivered, or is being rejected because of the programmed therapy state. Record displayed messages or indicators associated with the attempt.

**Expected outcome:** Accessory failure is distinguished from expected therapy lockout or another programmed restriction.

### 3. Inspect the Remote Dose Cord
Examine the cord, button, connector, strain relief, and housing for cuts, crushing, contamination, loose parts, or liquid exposure. Remove visibly damaged accessories from service.

**Expected outcome:** The accessory is physically intact. If damage is found, do not continue using that cord.

### 4. Verify the Connection
With the pump removed from patient use, confirm the remote dose cord is inserted into the correct external connection and seats securely without excessive force or looseness.

**Expected outcome:** The accessory is fully connected and recognized as intended. If reseating the connection restores reliable activation, continue to final verification.

### 5. Check the Programmed Therapy State
Verify that the pump is operating in the intended authorized therapy configuration and determine whether a dose request is expected to be available at the time of testing. Do not alter lockout parameters or protected clinical programming merely to bypass normal therapy restrictions.

**Expected outcome:** Expected lockout behavior is distinguished from failure of the button or pump. If the reported event was normal programmed behavior, document the finding and stop troubleshooting after verifying correct operation.

### 6. Substitute a Known-Good Dose Cord
Connect a known-good compatible remote dose accessory to the same pump in a controlled test configuration.

**Expected outcome:** If the known-good cord functions normally, the original accessory is defective. If both fail, continue evaluating the pump.

### 7. Cross-Test the Suspect Cord When Appropriate
If institutional procedures permit, test the suspect cord on another compatible verified pump using a nonpatient setup.

**Expected outcome:** If the fault follows the cord, remove that accessory from service. If the cord works normally elsewhere, investigate the original pump.

### 8. Verify Dose-Request Recognition
Using an approved test configuration that does not affect a patient, confirm that eligible dose requests are recognized consistently. Do not rely solely on the tactile click of the button.

**Expected outcome:** The pump consistently recognizes an eligible activation and responds according to the configured test state. Successful operation means troubleshooting can stop.

### 9. Inspect for Intermittency
Observe the cord and connector during normal nonpatient handling. Do not aggressively flex the cable or manipulate contacts.

**Expected outcome:** Dose recognition remains stable. Any intermittent activation or connection is unacceptable for patient use.

### 10. Escalate Persistent Pump-Side Failure
If multiple known-good accessories are not recognized or eligible dose requests remain unreliable, remove the pump from service. Do not attempt internal connector or board repair without authorized service documentation.

**Expected outcome:** A pump-side control or interface fault is referred for qualified repair.

## If the Problem Persists
External cord damage, connection problems, accessory failure, and expected PCA lockout behavior have been evaluated. Remaining causes may involve the pump's external interface, input circuitry, software state, configuration, or another service-level fault.

Remove the pump from service, label it **Out of Service**, and send it for repair or bench evaluation. Use manufacturer documentation and approved test equipment. Configuration or repairs should be performed only by qualified personnel. Verify dose-request operation and all required pump functions before return to clinical service.

Knowing when an intermittent patient-dose control requires escalation is proper troubleshooting.

## Clinical Use Tip
A patient-controlled dose button must be dependable; an intermittent button or connection should be treated as failed even if it works during some attempts.

## Work Order Documentation (CCR Method)
<!-- CCR examples come from front matter; optional explanatory prose may follow. -->



## Helpful Details to Include (If Known)
<!-- rendered from front matter -->

## Final Thought
Separate normal PCA restrictions from genuine accessory failure, verify the complete patient-dose pathway with controlled testing, and remove unreliable controls from service.

That is successful troubleshooting.
