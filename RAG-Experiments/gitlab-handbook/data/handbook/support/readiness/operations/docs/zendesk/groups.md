---
title: Groups
description: Support Operations documentation page for Zendesk groups
canonical_path: "/handbook/support/readiness/operations/docs/zendesk/groups"
---

## What are Zendesk groups?

As per
[Zendesk](https://support.zendesk.com/hc/en-us/articles/4408886146842-About-organizations-and-groups#topic_iny_3jg_sz):

> Groups collect team members together based on criteria those team members have
> in common. Groups can only contain team members; no end users can be included.
> All agents must be assigned to at least one group, but they can be members of
> more than one. Groups can be used to support organizations. You can designate
> one group as the default group for your account and you can also designate a
> default group for each team member. All new team members you create will be
> added to the default group.

## How do we maintain them?

We currently maintain all groups via Zendesk itself.

## Current Zendesk Global groups

- [Accounts Receivable](https://gitlab.zendesk.com/groups/360008238400)
- [Billing](https://gitlab.zendesk.com/groups/360003910679)
- [China Comms](https://gitlab.zendesk.com/groups/360007080959)
- [General](https://gitlab.zendesk.com/groups/360002757414)
- [Partner Support](https://gitlab.zendesk.com/groups/4560424672028)
- [Professional Services Group](https://gitlab.zendesk.com/groups/360002771760)
- [SGG: Baobab](https://gitlab.zendesk.com/groups/4725956857884)
- [SGG: Ginkgo](https://gitlab.zendesk.com/groups/4427347212434)
- [SGG: Kapook](https://gitlab.zendesk.com/groups/4725931534108)
- [SGG: Maple](https://gitlab.zendesk.com/groups/4427347399698)
- [SGG: Pine](https://gitlab.zendesk.com/groups/4427366542482)
- [Support AMER](https://gitlab.zendesk.com/groups/360002038460?location=admin_center&route=groups)
- [Support APAC](https://gitlab.zendesk.com/groups/360002038360?location=admin_center&route=groups)
- [Support EMEA](https://gitlab.zendesk.com/groups/360001979440?location=admin_center&route=groups)
- [Support Focus: Authentication and Authorization](https://gitlab.zendesk.com/groups/360008238420)
- [Support Focus: CMOC](https://gitlab.zendesk.com/groups/360008266039)
- [Support Focus: L&R](https://gitlab.zendesk.com/groups/360008266119)
- [Support Focus: Secure](https://gitlab.zendesk.com/groups/360008266179)
- [Support Managers](https://gitlab.zendesk.com/groups/360004358239)
- [Support Ops](https://gitlab.zendesk.com/groups/360004215280)

## Current Zendesk US Federal groups

- [General](https://gitlab-federal-support.zendesk.com/groups/360016402951)
- [Security](https://gitlab-federal-support.zendesk.com/groups/360016399052)
- [Support](https://gitlab-federal-support.zendesk.com/groups/360004818031)
- [Support Managers](https://gitlab-federal-support.zendesk.com/groups/360016399072)
- [Support Operations](https://gitlab-federal-support.zendesk.com/groups/360016399032)

## Creating a group in Zendesk

To create a group in Zendesk, you first need to go to the Admin Center
([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From
there, you need to go to the Groups page (People > Team > Groups).

From there, click the blue `Create group` button at the top-right of the page.
When making a group, you will:

1. Enter the name of the group
1. Enter a description of the group
1. Ensure `Make this group private` is **not** checked
1. Ensure `Set as default group` is **not** checked
1. Check the box next to any agents who should be in this group

After doing so, click the blue `Create group` button at the bottom-right of the
page.

## Editing a group in Zendesk

To edit a group in Zendesk, you first need to go to the Admin Center
([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From
there, you need to go to the Groups page (People > Team > Groups).

From there, locate the group in question and click the `edit` link to the
far-right (on the same line as the group's name). From here, you can make the
needed edits and click the blue `Save` button at the bottom-right of the page.

## Deleting a group in Zendesk

To delete a group in Zendesk, you first need to go to the Admin Center
([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From
there, you need to go to the Groups page (People > Team > Groups).

From there, locate the group in question and click the `edit` link to the
far-right (on the same line as the group's name). From here, you can click the
`Delete` button at the bottom-right of the page.

## Change management

As the group changes are unique in deployment, please see
[Zendesk group change management](/handbook/support/readiness/operations/docs/change_management#zendesk-group-change-management)
for more information.

#### Labels to use

For all issues and MRs involving groups, the label
`Support-Ops-Category::Orgs and Users` should be used.

#### Change criticality

Due to the nature and impact adding/editing/deleting Zendesk groups can impose
on agents, all issues/MRs related to Zendesk groups will be classified as either
[criticality 2](/handbook/support/readiness/operations/docs/change_criticalities#criticality-2)
or
[criticality 3](/handbook/support/readiness/operations/docs/change_criticalities#criticality-3)
