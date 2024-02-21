---
layout: handbook-page-toc
title: "TPM.1.01 - Third Party Assurance Review Control Guidance"
---

## Control Statement

A vendor security review is performed at the time of procurement for new third party vendors. A results report is created detailing vendor risk level and any observations noted and the results are considered as part of vendor contracting.

## Context

It's common for companies like GitLab to offload risk and services to third parties.; most SaaS companies these days rely heavily on other SaaS products. In order to create a chain of trust, the security control for any third party providers GitLab uses need to be validated. Since the security of a whole system is only as good as the least secure component, we need to do everything we can to ensure that all third party providers used by GitLab meet or exceed the bar we have set for security controls.

An auditor will, dependent on the scope of the audit, select a sample of third-party vendors or review all that handle GitLab RED or ORANGE data to validate review of their security practices has been completed.

## Scope

This control applies to all third party providers that interact with data within the GitLab production environment, or any third party providers that a GitLab production system relies upon.

## Ownership

Control Owner:

- `Security Compliance`

Process Owner:

- Security Compliance

## Guidance

- The easiest way to satisfy this control is to review all third party provider SOC2 Type 2 reports for appropriate scope and efficacy of controls.
- If a SOC2 Type 2 report is not available, we can send these third party providers a GitLab security questionnaire to gather the necessary information about the security controls they have in place and the approximate state of maturity of that third party provider.

## Additional control information and project tracking

Non-public information relating to this security control as well as links to the work associated with various phases of project work can be found in the [Third Party Assurance Review control issue](https://gitlab.com/gitlab-com/gl-security/security-assurance/sec-compliance/compliance/issues/922).

### Policy Reference

[Third Party Risk Management Procedure]({{< ref "third-party-risk-management" >}})

## Framework Mapping

- SOC
  - CC3.2
  - CC6.4
  - CC9.2
- PCI
  - 12.8.3
  - 9.5
  - 9.5.1
