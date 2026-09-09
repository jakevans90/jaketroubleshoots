---
schemaVersion: 1
title: "BD Pyxis MedStation ES Medication Dispensing Cabinet - Medication Inventory Count Incorrect or Transaction Will Not Post"
issueTitle: "Medication Inventory Count Incorrect or Transaction Will Not Post"
description: "Inventory or transaction records are incorrect because of workflow, synchronization, communication, compartment, configuration, or backend-system discrepancies."
assetType: "Medication Dispensing Cabinet"
manufacturer: "BD"
model: "Pyxis MedStation ES"
slug: "bd-pyxis-medstation-es-medication-inventory-count-incorrect-or-transaction-will-not-post"
dateAdded: "2026-09-09"
taxonomyMode: "reuse"
ccr:
  complaint: "Pharmacy reported a medication removal transaction from the Pyxis MedStation ES had not posted to the central system."
  cause: "Clinical Engineering found the cabinet had lost network connectivity during the transaction and remained offline."
  resolution: "Restored the network connection and verified the cabinet resynchronized; pharmacy confirmed the transaction record and inventory were reconciled through the approved process."
helpfulDetails:
  - "Medication and compartment involved."
  - "Type of transaction."
  - "Physical versus displayed count."
  - "Cabinet online status."
  - "Synchronization status."
  - "Drawer or compartment recognition."
  - "Whether other cabinets were affected."
  - "Recent restock or inventory activity."
  - "Pharmacy reconciliation findings."
  - "Final transaction and inventory status."
---

## What This Guide Helps With

Inventory or transaction records are incorrect because of workflow, synchronization, communication, compartment, configuration, or backend-system discrepancies.

## Step-by-Step Troubleshooting

### 1. Protect Medication Accountability and Patient Care

Do not change inventory values solely to make the cabinet appear correct.

Notify pharmacy of any discrepancy that could affect controlled medication accountability, medication availability, or patient documentation.

Use the facility's approved discrepancy and downtime procedures.

**Expected outcome:** Medication access and accountability remain controlled while the discrepancy is investigated.

### 2. Confirm the Exact Inventory or Transaction Problem

Determine whether:

- The physical quantity differs from the displayed quantity.
- A remove, return, waste, or other transaction did not post.
- One medication is affected.
- One drawer or pocket is affected.
- Multiple transactions are delayed.
- The cabinet is currently offline.
- The issue followed restocking or inventory activity.

**Expected outcome:** The discrepancy is clearly defined without altering the record prematurely.

### 3. Verify Physical Inventory With Authorized Pharmacy Staff

Clinical Engineering should not independently reconcile medication quantities.

Have authorized pharmacy personnel verify the physical count and identify whether the discrepancy is actual or only electronic.

**Expected outcome:** The true physical inventory is established through the correct medication-control process.

### 4. Check Cabinet Online and Synchronization Status

Verify whether the cabinet is connected to the network and synchronized with the central system.

A transaction may remain pending or fail to post during a communication interruption.

**Expected outcome:** Network and synchronization status are confirmed.

### 5. Determine Whether the Problem Is Local or Widespread

Ask whether similar transaction or inventory issues are occurring at:

- Other drawers in the same cabinet.
- Other Pyxis cabinets.
- Other units in the facility.

**Expected outcome:** The problem is classified as medication-specific, cabinet-specific, or system-wide.

### 6. Inspect the Associated Drawer or Compartment

If the problem involves one location, confirm the drawer, pocket, Cubie, or mini-drawer is:

- Recognized.
- Closing and locking normally.
- Reporting its position correctly.
- Free from obvious obstruction.

Hardware recognition problems can interfere with expected workflow completion.

**Expected outcome:** The medication location functions normally or a compartment-specific problem is identified.

### 7. Review the User-Visible Transaction State

Without entering unauthorized administrative functions, verify whether the cabinet indicates:

- Pending activity.
- Offline condition.
- Incomplete workflow.
- User sign-in problem.
- Synchronization delay.

Do not delete transactions or manually alter database records.

**Expected outcome:** Any visible pending or incomplete state is documented for pharmacy/application support.

### 8. Coordinate With Pharmacy Informatics

Have the appropriate pharmacy or Pyxis administrator review whether the medication, pocket assignment, formulary/configuration, user privilege, and central transaction record are correct.

Clinical Engineering should provide hardware and connectivity findings rather than making pharmacy database corrections unless specifically authorized.

**Expected outcome:** Configuration and backend transaction causes are confirmed or ruled out.

### 9. Verify Correction

After the authorized correction, use a pharmacy-approved test or observed workflow to verify:

- Cabinet remains online.
- The correct compartment is recognized.
- The transaction posts as expected.
- Inventory displays correctly.

**Expected outcome:** Physical inventory and electronic records are consistent and transactions synchronize normally.

If successful, troubleshooting can stop.

### 10. Escalate Persistent Record Discrepancy

If local hardware, connectivity, and approved configuration checks are normal but transactions remain incorrect or fail to post, stop equipment-level troubleshooting.

**Expected outcome:** The issue is escalated to pharmacy application, server, database, or manufacturer support without making unauthorized record changes.

## If the Problem Persists

Common external cabinet, compartment, and communication causes have been ruled out.

Remaining categories may include application configuration, server synchronization, transaction processing, database, interface, or account-level issues.

The cabinet should be:

- Removed from service if medication accountability cannot be assured.
- Labeled **Out of Service** when appropriate.
- Evaluated through pharmacy informatics, IT, manufacturer support, or bench service as applicable.
- Evaluated using approved documentation and tools.
- Repaired or configured only by qualified personnel.

Return to service only after medication records and transaction processing are verified accurate.

Knowing when the problem belongs to pharmacy informatics or backend support instead of hardware repair is proper troubleshooting.

## Clinical Use Tip

Treat unexplained medication-count discrepancies as an accountability issue first, not simply an equipment error.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Preserve medication accountability, separate hardware problems from transaction or database problems, involve pharmacy in reconciliation, and verify both physical and electronic status before closing the work order.

That is successful troubleshooting.
