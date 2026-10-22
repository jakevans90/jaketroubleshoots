---
schemaVersion: 1
title: "Drager Atlan A350 Anesthesia Machine - Anesthetic Agent Identification Is Missing or Incorrect"
issueTitle: "Anesthetic Agent Identification Is Missing or Incorrect"
description: "Troubleshoot missing, intermittent, or incorrect anesthetic-agent identification caused by sampling, moisture, agent delivery, configuration, or gas-analysis problems."
assetType: "Anesthesia Machine"
manufacturer: "Drager"
model: "Atlan A350"
slug: "drager-atlan-a350-anesthetic-agent-identification-is-missing-or-incorrect"
dateAdded: "2026-10-22"
taxonomyMode: "reuse"
ccr:
  complaint: "Anesthesia staff reported that the Atlan A350 intermittently failed to identify the anesthetic agent during setup."
  cause: "Clinical Engineering found moisture in the external gas-sampling line causing unstable sample flow to the integrated gas analyzer."
  resolution: "Replaced the contaminated sampling line, verified correct and stable agent identification with an approved functional test, and completed return-to-service checks successfully."
helpfulDetails:
  - "Agent expected during the event."
  - "Agent displayed by the machine."
  - "Whether identification was missing, incorrect, or intermittent."
  - "Other gas values observed."
  - "Sampling-line condition."
  - "Water-trap condition."
  - "Known-good substitutions performed."
  - "Configuration observed."
  - "Whether the issue followed a particular setup or accessory."
  - "Functional test results."
  - "Final device status."
---

## What This Guide Helps With

Troubleshoot missing, intermittent, or incorrect anesthetic-agent identification caused by sampling, moisture, agent delivery, configuration, or gas-analysis problems.

## Step-by-Step Troubleshooting

### 1. Protect the Patient and Verify Anesthetic Delivery Independently

Do not rely on questionable agent identification while a patient is receiving anesthesia.

If the problem occurs during a case:

- Inform anesthesia staff.
- Use appropriate alternate verified monitoring.
- Confirm patient management independently of the questionable analyzer value.
- Move the patient to another verified anesthesia machine if adequate anesthetic-agent monitoring cannot be maintained.

Do not adjust anesthetic delivery solely to make an analyzer identification appear correct.

**Expected outcome:** Safe anesthesia care continues using reliable monitoring while the affected system is evaluated.

Troubleshoot the Atlan A350 off-patient whenever agent identification remains unreliable.

### 2. Confirm the Exact Reported Behavior

Determine whether the system:

- Shows no agent.
- Identifies the wrong agent.
- Alternates between agents.
- Displays an agent only intermittently.
- Displays concentration data without reliable identification.
- Developed the problem after changing agents or machine setup.

Record the actual observed display behavior and test conditions.

**Expected outcome:** The issue is clearly defined as missing, incorrect, delayed, or intermittent agent identification.

If correct identification is consistently demonstrated during controlled testing, document the result and stop troubleshooting.

### 3. Verify the Test Setup and Actual Agent in Use

Confirm with clinical staff or the controlled test setup which anesthetic agent is actually being delivered.

Check that:

- The expected agent source is installed and being used.
- The vaporizer or agent-delivery component is appropriately installed.
- The test is not being performed before sufficient agent reaches the sampling point.
- Residual agent from a previous setup is not confusing the observation.

Clinical Engineering should verify equipment behavior, not alter clinical dosing decisions.

**Expected outcome:** The expected agent in the breathing system is known and can be compared accurately with the analyzer display.

If the displayed identification matches the confirmed agent after allowing the sampling path to stabilize, no further troubleshooting is required.

### 4. Inspect the Gas Sampling Line

Check the external gas-sampling path for:

- Disconnection.
- Kinks.
- Liquid.
- Partial obstruction.
- Cracks.
- Loose fittings.
- Incorrect tubing.
- Poor sampling location.

An impaired sample can affect multiple gas measurements, including agent identification.

**Expected outcome:** The gas sample reaches the analyzer through an intact, dry, open, correctly connected line.

If correcting the sampling line restores correct agent identification, proceed to final verification and stop troubleshooting.

### 5. Check the Gas Analyzer Water Trap

Inspect the analyzer water trap for:

- Excess moisture.
- Blockage.
- Contamination.
- Incorrect installation.
- Incomplete seating.
- Physical damage.

Reseat or replace it with a compatible known-good trap if appropriate.

**Expected outcome:** The water trap is correctly installed and gas sampling occurs without obstruction or water-trap indications.

If agent recognition returns after correcting the trap, verify stable operation and stop troubleshooting.

### 6. Check Other Gas Measurements

Observe whether other available gas-analysis values are also missing, unstable, delayed, or implausible.

A problem affecting several measured gases suggests a broader sample-path or analyzer issue rather than isolated agent identification.

Do not use patient exposure as a troubleshooting test.

**Expected outcome:** Other gas measurements remain stable and respond appropriately in an approved controlled test setup.

If all gas values are abnormal, continue troubleshooting the common external sampling path before suspecting agent-specific recognition.

### 7. Substitute Known-Good Sampling Components

Use a known-good compatible:

- Sampling line.
- Water trap.
- External sampling adapter, when applicable.

Change one factor at a time where practical so the cause remains identifiable.

**Expected outcome:** The analyzer correctly identifies the known test agent using verified external sampling components.

If identification is restored after a substitution, replace the defective accessory and stop troubleshooting after final verification.

### 8. Verify Relevant User-Accessible Configuration

Review appropriate user-accessible configuration and operating selections that could affect gas-analysis presentation.

Check for:

- Incorrect operating mode.
- Disabled or hidden display parameters.
- Recent configuration changes.
- Incorrect profile or setup affecting what is displayed.

Do not enter unauthorized service menus or change protected calibration or analyzer parameters.

**Expected outcome:** The system is configured to display and use gas-analysis information as intended.

If correcting an approved configuration setting restores normal agent identification, verify the complete monitoring function before return to service.

### 9. Compare Analyzer Response During a Controlled Functional Test

Using approved test equipment and procedures, verify that the analyzer recognizes an appropriate known gas condition.

Assess:

- Recognition stability.
- Response consistency.
- Whether the displayed agent corresponds with the controlled test condition.
- Whether other gas values remain stable.

Do not attempt field calibration unless specifically authorized and supported by the correct service procedure and equipment.

**Expected outcome:** The analyzer consistently identifies the expected agent during approved testing.

If successful, proceed to final return-to-service checks.

### 10. Perform Final Functional Verification

Before returning the Atlan A350 to clinical service:

- Verify normal startup.
- Confirm stable gas sampling.
- Confirm expected agent identification.
- Verify other relevant gas measurements.
- Verify gas-monitoring alarms.
- Complete applicable anesthesia-machine checkout procedures.

**Expected outcome:** Agent identification and the complete gas-monitoring path function normally and consistently.

If agent identification remains unreliable, do not return the anesthesia machine to service.

## If the Problem Persists

If the actual agent, sampling line, water trap, external connections, operating configuration, and controlled test setup have been verified, the remaining possibilities may include an internal gas-analysis fault, analyzer calibration issue, software or configuration problem, internal sampling fault, or another service-level condition.

The device should be:

- Removed from service.
- Labeled **Out of Service**.
- Sent for repair or bench evaluation.
- Evaluated using appropriate manufacturer documentation and approved test equipment.
- Repaired, calibrated, or configured only by qualified personnel.

Do not perform unauthorized analyzer calibration, internal optical repair, board replacement, or service-menu adjustments. Complete all required gas-analysis, alarm, ventilation, and anesthesia-system testing after corrective service.

Escalating when agent identity cannot be verified reliably is proper troubleshooting.

## Clinical Use Tip

Never use an unexpected agent-identification display as the sole basis for changing anesthetic delivery; verify the monitoring path and clinical situation independently.

## Work Order Documentation (CCR Method)

<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)

<!-- rendered from front matter -->

## Final Thought

Agent-identification problems should be approached as gas-monitoring problems first: protect the patient, verify the actual test condition, inspect the sample path, and rule out consumables and configuration before assuming analyzer failure. Escalate any unresolved or unreliable result and document the verified cause and final testing.

That is successful troubleshooting.
