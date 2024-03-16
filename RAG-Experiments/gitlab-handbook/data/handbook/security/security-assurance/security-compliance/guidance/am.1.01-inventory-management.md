---
title: "AM.1.01 - Inventory Management Control Guidance"
---

## Control Statement

GitLab maintains an inventory of system devices, which is reconciled quarterly.

## Context

The purpose of this control is to ensure we are monitoring the systems in use by GitLab. We can't prove we are protecting all GitLab systems if we don't have an up-to-date inventory of those systems.

### Current status of this control

1. GitLab team-member endpoints:
    - Team-member workstations are tracked with JAMF endpoint management
    - A google form sent to all on-boarding team-members records the ownership and serial number of laptops
1. Production systems:
    - Backend system inventories are not maintained, but strong naming conventions exist
    - For GCP, that constitutes most of GitLab's production architecture; we can evaluate the GCP systems/services, discover new systems, and assign ownership

## Scope

This control applies to all GitLab endpoint workstations as well as virtual assets within our hosting providers.

## Ownership

- IT Operations owns the workstation assets portion of this control
- Infrastructure owns the system and service portions of this control

## Guidance

The scope of this control is broad by design. Asset inventories are the source of truth for what team-member workstations, systems, and services constitute GitLab as a company. If we want to verify if we are collecting logs on 100% of the systems we are required to collect logs for, this inventory allows us to cross reference the logs we have with all the systems for which these logs should exist.

1. Team-member workstations
    - Confirm the information that will be tracked via JAMF
    - Create and document a process to regularly review team-members assets and validate that all new workstations are being tracked
    - Backfill information for workstations that were issued before this process existed
1. Backend Systems
    - Export all GCP systems/services into a markdown table
    - Work with the infrastructure team to assign ownership to each asset
    - Create and document a process to regularly review these assets and validate that the inventory is accurate

## Additional control information and project tracking

Non-public information relating to this security control as well as links to the work associated with various phases of project work can be found in the [Inventory Management control issue](https://gitlab.com/gitlab-com/gl-security/security-assurance/sec-compliance/compliance/issues/761).

### Policy Reference

- [Endpoint Management at GitLab](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/endpoint-management/)

## Framework Mapping

- ISO
  - A.8.1.1
- PCI
  - 9.6.1
  - 9.7
  - 9.7.1
