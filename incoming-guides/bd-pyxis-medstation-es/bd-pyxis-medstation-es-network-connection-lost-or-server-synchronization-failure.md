---
schemaVersion: 1
title: "BD Pyxis MedStation ES Medication Dispensing Cabinet - Network Connection Lost or Server Synchronization Failure"
issueTitle: "Network Connection Lost or Server Synchronization Failure"
description: "The cabinet is offline or not synchronizing because of cabling, wall-port, network, server, configuration, or wider infrastructure problems."
assetType: "Medication Dispensing Cabinet"
manufacturer: "BD"
model: "Pyxis MedStation ES"
slug: "bd-pyxis-medstation-es-network-connection-lost-or-server-synchronization-failure"
dateAdded: "2026-09-09"
taxonomyMode: "reuse"
ccr:
  complaint: "Pharmacy reported the Pyxis MedStation ES was offline and had stopped synchronizing with the central system."
  cause: "Clinical Engineering found the Ethernet cable partially disconnected at the cabinet after the unit had been moved for cleaning."
  resolution: "Reseated the network cable, verified physical link restoration, and confirmed normal online status and synchronization with the pharmacy system."
helpfulDetails:
  - "Exact offline or synchronization message."
  - "Time failure began."
  - "Recent network outage or relocation."
  - "Ethernet cable condition."
  - "Link indicator status."
  - "Wall jack identifier."
  - "Cable or port test results."
  - "Whether other cabinets were affected."
  - "Server availability."
  - "Synchronization result after correction."
  - "Final online status."
---

## What This Guide Helps With

The cabinet is offline or not synchronizing because of cabling, wall-port, network, server, configuration, or wider infrastructure problems.

## Step-by-Step Troubleshooting

### 1. Protect Medication Workflow

Confirm pharmacy and nursing understand that the cabinet may not be communicating normally.

Follow the facility's approved downtime or alternate medication-access process when server-dependent functions cannot be trusted.

**Expected outcome:** Medication access and documentation continue safely while connectivity is evaluated.

### 2. Confirm the Exact Communication Failure

Determine whether the cabinet:

- Shows offline status.
- Cannot synchronize.
- Cannot receive expected updates.
- Cannot post transactions.
- Lost connection after a move, outage, or network maintenance.
- Is the only affected cabinet.

Record any displayed network or synchronization message exactly.

**Expected outcome:** The communication symptom and timing are clearly defined.

### 3. Verify Cabinet Operation

Confirm the cabinet is fully powered and otherwise operating normally.

A cabinet that is frozen, restarting, or partially booted may have a local system problem rather than a network-only issue.

**Expected outcome:** The cabinet is stable and the problem is appropriately isolated to communications.

### 4. Inspect the Network Cable

Inspect the accessible Ethernet cable for:

- Loose connection.
- Damaged locking tab.
- Pinching.
- Cuts.
- Improvised couplers.
- Recent disconnection during cleaning or relocation.

Reseat an accessible connection when permitted.

**Expected outcome:** The network cable is intact and securely connected.

If connection returns and remains stable after reseating, proceed to final verification and stop troubleshooting.

### 5. Check Link Status

Inspect available network-link indicators on accessible cabinet or wall/network interfaces.

If appropriate, test the cable or wall jack using approved Clinical Engineering or network test equipment.

Do not modify switch configuration.

**Expected outcome:** Physical network link is present or a cable/port problem is identified.

### 6. Compare With Nearby Cabinets

Determine whether other Pyxis MedStation ES cabinets in the same area or facility are experiencing similar symptoms.

A multi-device failure suggests a network, server, authentication, or enterprise application problem.

**Expected outcome:** The issue is classified as cabinet-local or infrastructure-wide.

### 7. Verify the Wall Port and Network Path

If the cabinet has no link, coordinate with IT to confirm the wall port and upstream switch connection are active and correctly assigned.

Clinical Engineering may provide:

- Cabinet location.
- Wall jack identifier.
- Device network identifier if available through approved methods.
- Time the failure began.
- Link status.

Do not change VLAN, addressing, firewall, or switch settings without authorization.

**Expected outcome:** The physical network path is verified through the appropriate support team.

### 8. Check Server or Application Availability

If network link is present but synchronization fails, coordinate with pharmacy informatics or the Pyxis system support team to verify central services are available.

**Expected outcome:** Server availability is confirmed and the issue is narrowed to cabinet communication or central infrastructure.

### 9. Verify Recovery

After the network or server problem is corrected, verify:

- Cabinet shows normal online status.
- Synchronization resumes.
- Expected system updates are received.
- Authorized transaction communication functions normally.
- No repeated disconnect occurs.

**Expected outcome:** The cabinet remains connected and synchronizes normally.

If successful, troubleshooting can stop.

### 10. Escalate Persistent Communication Failure

If the cable, wall port, network link, and central server appear normal but the cabinet remains offline, stop external troubleshooting.

Potential remaining causes include local network interface hardware, operating-system network services, application configuration, certificates, or other service-level conditions.

**Expected outcome:** The fault is escalated to the proper technical owner without unauthorized network changes.

## If the Problem Persists

Basic cable, physical link, local power, network path, and server availability have been checked.

The cabinet should be:

- Removed from service if medication availability, inventory integrity, or transaction recording cannot be assured.
- Labeled **Out of Service** when appropriate.
- Sent for technical evaluation or managed on site through approved support channels.
- Evaluated using manufacturer documentation and approved network/service tools.
- Repaired or configured only by qualified personnel.

Return to service only after stable communication and appropriate synchronization are verified.

Knowing when to stop after proving the external network path is proper troubleshooting.

## Clinical Use Tip

When a cabinet is offline, confirm the entire medication transaction and documentation workflow rather than judging functionality only by whether drawers still open.

## Work Order Documentation (CCR Method)


<!-- CCR examples come from front matter. -->

## Helpful Details to Include (If Known)


<!-- Helpful details come from front matter. -->

## Final Thought

Start with the physical network path, distinguish local from system-wide problems, avoid unauthorized configuration changes, and verify synchronization before returning the cabinet to normal service.

That is successful troubleshooting.
