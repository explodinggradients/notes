---
title: "Security Architecture review process"
---

<link rel="stylesheet" type="text/css" href="/stylesheets/biztech.css" />

## Overview

Security Architecture review is a holistic assessment of security layers across
infrastructure, application, people, and processes.

## Purpose

- Meet [Security and Compliance requirements]
- Ensure best practices are used
- Ensure [Security Architecture Principles] are followed
- Ensure identified security threats are mitigated
- Bring Risk management early in our processes (design, implementation, management)
- Provide recommendations to minimize damage when a component is compromised

[Security and Compliance requirements]: {{< ref "_index.md#security-architecture-requirements" >}}
[Security Architecture Principles]: {{< ref "_index.md#security-architecture-principles" >}}

## When to conduct a Security Architecture review?

The review process is integrated into the broader [Architecture workflow], but can be triggered for:

- New large projects and initiatives
- New large features
- New significant services
- Cross teams/stage technical changes

And more generally:

- Everything built by GitLab, and meant to be deployed in our infrastructure or our customers'
  infrastructure.
- New or updated architectures processing, storing, or transferring any kind of [RED or ORANGE
  data]({{< ref "data-classification-standard" >}})

[Architecture workflow]: https://about.gitlab.com/handbook/engineering/architecture/workflow/

## How to request a Security Architecture review?

Create an issues in the Security Architecture
[general](https://gitlab.com/gitlab-com/gl-security/security-architecture/general/) project
(internal only.

## Scope

- Cloud infrastructure and services
  - Data encryption in transit over the cloud (example: from customer, through our WAF/CDN, terminating into GCP)
- Network
- Systems
  - Instances
  - Clusters
  - Virtual machines
  - Hardening
- Application
  - Third party (integrations, APIs, data transfers)

## Process

The Security Architecture review is conducted by a [Security Architect] who will:

- Identity and isolate components
- Start with external facing ones
- Go inward, deeper
- What have component access to?
  - Data → If not minimal data, can we move it?
  - Authentication (credentials)
- Follow our [Security Architecture Principles]
- Maintain a list of actors

The threats identified can be avoided (different architecture) or mitigated (security controls).

[Security Architect]: {{< ref "/job-families/security/security-engineer#security-architect" >}}

### SMEs

Depending on the type of change being reviewed, the Security Architect can involve:

- the Application Security team:
  - to create [Threat Models]
  - to conduct [AppSec reviews]
- the InfraSec team:
  - to review and make recommendations:
    - Network
    - Cloud infrastructure and services
    - Systems
- The Security Compliance team
- The Cryptography Officer

[Threat Models]({{< ref "../threat-modeling" >}})
[AppSec reviews]({{< ref "../_index.md#internal-application-security-reviews" >}})

## Result

Report (markdown file should be enough: searchable, collaborative, authoritative, like for threat modeling:
Validation of the solution:
  - Requirements are met
  - Risk assessment
