---
title: Change Management
description: Support Operations documentation page for change management
canonical_path: "/handbook/support/readiness/operations/docs/change_management"
---

## Standard change management

With the standard change mangement process, we use automations to handle our
deployments. This shifts the responsibilities you have when working a request
that would utilize our standard change management process.

Through the automation, all deployments are automatically done on the first of
the month. This means when you create a request, you should determine if the
workload required for the request can be done in a proper amount of time so that
it is completed on the next deployment date. You should consider the time needed
for development, testing, testing review, and the requester's indicated
preferences in making your decision.

Once you have decided on the decision, you will add the corresponding milestone
to the issue (and subsequent MR) to indicate the deployment it belongs to. You
should also ensure the deployment date the request will fall into is
communicated to the requester.

Once you are done working the request, you would simply merge the changes into
the corresponding repository. The automation will handle it from there on the
deployment date.

#### Cutoff date

The cutoff date for new requests to be added into the upcoming deployment is 5
business days before the next deployment date. Our business days are Monday
through Friday, so if the deployment day is on a Monday, this would mean the
previous Monday is the cutoff date.

Any request filed after the cutoff date will not be able to put into the
upcoming deployment without approvals from both a Support Director and Readiness
Director.

#### Exceptions

All exceptions to the standard change management process should be done by a
Support Readiness, Operations Manager. This member of leadership will analyze
the milestone and determine what impact the exception will cause. They will then
explain what the impact of the exception would be, pinging all of the Support
Directors. The Support Directors would discuss the exception and what impact it
will have and come back with a decision.

The Support Readiness, Operations Manager will then make the needed changes to
issues/merge requests in the current milestone to accomodate the exception.

#### Service level agreements information

The following process is *required* for all Zendesk SLA changes that impact any
customer facing ticket.

1. An issue should be created in
   [support-team-meta](https://gitlab.com/gitlab-com/support/support-team-meta/)
   using the
   [Requested Change Template](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/new?issuable_template=Requested%20Change).
1. The support team discusses the desire to change, citing reason and potential
   impact.
1. The Support Ops Manager, @jcolyer, is pinged in the issue once the
   discussion is over and a decision has been reached, with approval from at
   least ONE Senior Support Manager.
1. The Support Ops Manager will make an issue in the
   [legal tracker](https://gitlab.com/gitlab-com/legal-and-compliance/-/issues)
   requesting the change.
1. Once legal has approved, the Support Ops Manager will announce the plan to
   make the SLA change to the support team via both slack (#support_team-chat)
   and the SWIR. It should be scheduled for the next Saturday, during
   non-business hours.
   - If legal does not approve, the Support Ops Manager will update the
     original issue and close it out.
1. The Support Ops Manager will implement the change. Following the
   implementation, the Support Ops Manager will announce the change has been
   made via both slack (#support_team-chat) and the SWIR.
1. The Support Ops Manager will update relevant documentation with the change.
1. The Support Ops Manager will update the original issue and close it out.

#### Change Deployment Scripts

Our standard change deployments are done via scripts running on ops.gitlab.net
via pileine schedules. You can locate the source code
[here](https://gitlab.com/gitlab-com/support/support-ops/support-ops-tools/change-deployment).

## Immediate deployments

Some items we work on will warrant immediate deployments. In situations like
these, merging things into the master branch should result in a deployment.

For anything that does not follow this behavior, please see the
[special situations](#special-situations).

## Special situations

#### Support team page change management

All changes to the support team page would follow the nature of
[Immediate deployments](#immediate-deployments).

#### Zendesk agents change management

For any changes relating to Support team, the
[sync](/handbook/support/readiness/operations/docs/zendesk/agents#support-team)
will handle them, and thus the
[Standard change management](#standard-change-management) can be used.

For all other cases, you will have to manually make the changes in Zendesk
itself.

#### Zendesk emails change management

As we currently do not do syncs on Zendesk emails, you will have to make the
changes in Zendesk itself.

#### Zendesk group change management

As we currently do not do syncs on Zendesk groups, you will have to make the
changes in Zendesk itself.

#### Zendesk macros change management

Due the nearly non-existent impact macros have, these follow the nature of
[Immediate deployments](#immediate-deployments)

#### Zendesk organizations change management

For changes to the Support Team organization notes can follow
[Immediate deployments](#immediate-deployments).

Changes not controlled by the
[Zendesk-Salesforce Sync](/handbook/support/readiness/operations/docs/zendesk/zendesk_salesforce_sync)
are not synced and would need to be done manually in Zendesk itself.

#### Zendesk role change management

As we currently do not do syncs on Zendesk roles, you will have to make the
changes in Zendesk itself.

#### Zendesk schedules change management

As we currently do not do syncs on Zendesk schedules, you will have to make the
changes in Zendesk itself.

#### Zendesk settings change management

As we currently do not do syncs on Zendesk settings, you will have to make the
changes in Zendesk itself.

#### Zendesk theme change management

Due to the nature of Zendesk themes, simply committing changes to the master
branch will have no effect. As such, changes to the theme must be done via
[Zendesk Guide](/handbook/support/readiness/operations/docs/zendesk/guide).

#### Zendesk webhook change management

As we currently do not do syncs on Zendesk webhoooks, you will have to make the
changes in Zendesk itself.
