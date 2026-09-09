---
schemaVersion: 1
title: "BD Pyxis MedStation ES Medication Dispensing Cabinet - User Login, Badge Reader, or Biometric Authentication Failure"
issueTitle: "User Login, Badge Reader, or Biometric Authentication Failure"
description: "Users cannot authenticate because of credentials, badge reading, biometric recognition, peripheral connection, account, network, or system-level authentication problems."
assetType: "Medication Dispensing Cabinet"
manufacturer: "BD"
model: "Pyxis MedStation ES"
slug: "bd-pyxis-medstation-es-user-login-badge-reader-or-biometric-authentication-failure"
dateAdded: "2026-09-09"
taxonomyMode: "reuse"
ccr:
  complaint: "Staff reported that badges were not being recognized at the Pyxis MedStation ES although the cabinet was otherwise operational."
  cause: "Clinical Engineering found contamination on the external badge-reader surface and confirmed manual authentication remained functional."
  resolution: "Cleaned the badge reader using approved methods and verified successful authentication with an authorized known-good badge and normal secure logout."
helpfulDetails:
  - "Authentication method affected."
  - "Exact displayed message."
  - "One user versus multiple users."
  - "One cabinet versus multiple cabinets."
  - "Known-good badge result."
  - "Biometric sensor condition."
  - "Manual login result."
  - "Network status."
  - "Account status if confirmed by authorized support."
  - "Final authentication verification."
---

## What This Guide Helps With

Users cannot authenticate because of credentials, badge reading, biometric recognition, peripheral connection, account, network, or system-level authentication problems.

## Step-by-Step Troubleshooting

### 1. Protect Medication Access and Security

Do not bypass authentication controls or create unauthorized access to restore medication availability.

Confirm staff have an approved alternate medication-access method if the authentication problem prevents needed medications from being obtained.

**Expected outcome:** Patient care continues while medication-security controls remain intact.

### 2. Confirm the Exact Authentication Failure

Determine whether the problem affects:

- One user.
- Multiple users.
- Badge authentication only.
- Biometric authentication only.
- Manual login.
- All authentication methods.
- One cabinet or multiple cabinets.

Record any displayed message exactly.

**Expected outcome:** The scope is narrowed to user-specific, reader-specific, cabinet-specific, or system-wide authentication failure.

### 3. Verify Basic Cabinet Operation

Confirm the touchscreen responds normally and the cabinet is otherwise fully booted.

Check whether other cabinet functions appear normal and whether the device shows an obvious offline or communication condition.

**Expected outcome:** The cabinet is stable enough for authentication testing.

### 4. Inspect the Badge Reader

Inspect the reader and its accessible cable or mounting for:

- Damage.
- Contamination.
- Loose connection.
- Obstruction.
- Evidence of impact or liquid exposure.

Test with a known-good authorized badge when permitted.

Do not use another person's credentials for medication transactions.

**Expected outcome:** A known-good badge is read consistently or the failure is isolated to the badge-reader path.

If the known-good badge works and only the original badge fails, direct the issue to the appropriate badge or access-management process and stop equipment troubleshooting.

### 5. Evaluate Biometric Recognition

If biometric authentication is involved, inspect the sensor surface for contamination or physical damage and clean it only with approved materials.

Determine whether the issue affects one user or all users.

Do not alter biometric enrollment or security configuration unless specifically authorized.

**Expected outcome:** The sensor is clean, intact, and either accepts normal authentication or the failure is confirmed across users.

### 6. Compare Authentication Methods

If available and institutionally permitted, determine whether:

- Badge login fails but manual credentials work.
- Biometrics fail but badge login works.
- All methods fail.

This helps separate a peripheral problem from account or backend authentication problems.

**Expected outcome:** The fault is localized to a specific authentication method or shown to affect the full authentication path.

### 7. Check Network and Server Availability

Authentication may depend on server communication.

Verify external network connection and determine whether other cabinets are experiencing similar login problems. Coordinate with IT, pharmacy informatics, or the Pyxis application support team if the condition appears system-wide.

Do not change security settings or network configuration.

**Expected outcome:** Authentication failure is identified as local or infrastructure-related.

### 8. Verify User Account Status Through the Proper Support Path

If only one user is affected, have the appropriate pharmacy, identity-management, or application administrator confirm:

- Account is active.
- Required permissions remain assigned.
- Badge or biometric enrollment is valid.
- No institutional credential issue exists.

Clinical Engineering should not alter user privileges unless that responsibility is specifically assigned.

**Expected outcome:** User-account causes are either confirmed or ruled out.

### 9. Perform Final Functional Verification

After correction, verify an authorized test user can authenticate using the affected method and that the cabinet returns to the expected secure state after logout.

**Expected outcome:** Authentication is reliable and access control remains secure.

If successful, troubleshooting can stop.

### 10. Escalate Persistent Authentication Failure

If the reader, touchscreen, power, network, and account status appear normal but authentication continues to fail, escalate for authorized application, security, or hardware service.

**Expected outcome:** The unresolved cabinet is routed to the correct technical owner without bypassing security controls.

## If the Problem Persists

External reader condition, user-specific issues, network availability, and basic cabinet operation have been checked.

Possible remaining categories include internal reader electronics, application services, authentication configuration, server integration, or security-system issues.

The cabinet should be:

- Removed from service if secure medication access cannot be assured.
- Labeled **Out of Service** when appropriate.
- Sent for repair or technical evaluation.
- Evaluated using manufacturer documentation and approved service tools.
- Repaired or configured only by qualified and authorized personnel.

Return to service only after secure user authentication and normal cabinet operation are verified.

Knowing when to stop without bypassing an authentication control is proper troubleshooting.

## Clinical Use Tip

Never restore availability by defeating login, badge, biometric, or medication-security controls.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Maintain medication security, isolate whether the problem is user-, peripheral-, cabinet-, or network-related, verify the complete authentication path, and escalate rather than bypassing access controls.

That is successful troubleshooting.
