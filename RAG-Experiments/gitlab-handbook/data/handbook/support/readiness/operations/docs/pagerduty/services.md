---
title: Services
description: Support Operations documentation page for Pagerduty services
canonical_path: "/handbook/support/readiness/operations/docs/pagerduty/services"
---

## What are Pagerduty services

As per
[Pagerduty](https://support.pagerduty.com/docs/services-and-integrations):

> A technical service reflects a discrete piece of functionality that is wholly
> owned by one team. One or more technical services combine to deliver
> customer-facing or business capabilities.

Services interact with `/chatops oncall` commands to display who is currently
on-call in Slack.

## Current services used by support

#### Customer Support

- [Service link](https://gitlab.pagerduty.com/service-directory/PL3TX00)
- Escalation policy: Customer Emergency Rotation
- Integrations
  - Zendesk
  - API
  - Customer Emergency Escalation Channel
- Extensions and Add-Ons
  - Slack V2

#### Incident Management - CMOC

- [Service link](https://gitlab.pagerduty.com/service-directory/P1PRQ6J)
- Escalation policy: Incident Management - CMOC Rotation
- Integrations
  - Slack to PagerDuty
  - Pingdom to CMOC
  - woodhouse
- Extensions and Add-Ons
  - Slack V2

#### Support Managers

- [Service link](https://gitlab.pagerduty.com/service-directory/PTFI8XR)
- Escalation policy: Support Managers
- Integrations
  - Slack
- Extensions and Add-Ons
  - Slack V2

#### AMER Response Crew

- [Service link](https://gitlab.pagerduty.com/service-directory/PZLOI4B)
- Escalation policy: Support Managers
- Integrations
  - Email
- Extensions and Add-Ons
  - Slack V2

#### Customer Support - US Federal

- [Service link](https://gitlab.pagerduty.com/service-directory/P8K2XHK)
- Escalation policy: US Federal Customer Emergency Rotation
- Integrations
  - N/A
- Extensions and Add-Ons
  - N/A

## Change management

As the Pagerduty changes are unique in deployment, please see
[Pagerduty change management](/handbook/support/readiness/operations/docs/pagerduty/change_management)
for more information.

#### Labels to use

For all issues and MRs involving Pagerduty fields, the label
`Support-Ops-Category::Pagerduty` should be used.

#### Change criticality

Due to wildly varying nature and impact adding/editing/deleting things in
Pagerduty can impose, all issues/MRs related to Pagerduty need
to have the their criticality
[manually determined](/handbook/support/readiness/operations/docs/change_criticalities#determining-criticality)
