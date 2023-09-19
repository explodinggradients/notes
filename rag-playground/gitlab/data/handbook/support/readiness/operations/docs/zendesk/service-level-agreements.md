---
title: Service Level Agreements
description: Support Operations documentation page for Zendesk SLAs
canonical_path: "/handbook/support/readiness/operations/docs/zendesk/service-level-agreements"
---

## Zendesk calls them service level agreements, we do not

What appears here is all titled service level agreements, or SLAs, but many of
these are internal service level objectives, or SLOs, instead. They are titled
as service level agreement, or SLA, because that is what Zendesk calls the
setting. Nothing detailed herein is an actual, legal service level agreement.

## What are Zendesk service level agreements?

As per
[Zendesk](https://support.zendesk.com/hc/en-us/articles/204770038-Defining-and-using-SLA-policies):

> A Service Level Agreement, or SLA, is an agreed upon measure of the response
> and resolution times that your support team delivers to your customers.
> Providing support based on service levels ensures that you're delivering
> measured and predictable service. It also provides greater visibility when
> problems arise.

## Creating a service level agreement via Zendesk

**Note**: Some SLA policies are tied to the contracts our customers sign upon
getting a subscription. This means these changes can cause a huge impact. Please
ensure all change management processes are being followed.

To create a service level agreement in Zendesk, you first need to go to the
Admin Center
([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From
there, you need to go to the Service level agreements page (Objects and rules >
Business rules > Service level agreements).

After doing so, click the white `Add policy` button. This will then display a
new SLA where you will enter:

- a name for the SLA policy.
- a description for the SLA policy.
- the conditions to be met for the SLA policy to be applied.
- the response times for various SLA metrics.
  - At GitLab, we only use First reply time and Next reply time.
- The hours of operation for the SLA clocks to tick in.

After doing so, click the black `Save` button to create the SLA policy.

## Editing a service level agreement via Zendesk

**Note**: Some SLA policies are tied to the contracts our customers sign upon
getting a subscription. This means these changes can cause a huge impact. Please
ensure all change management processes are being followed.

To edit a service level agreement in Zendesk, you first need to go to the Admin
Center
([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From
there, you need to go to the Service level agreements page (Objects and rules >
Business rules > Service level agreements).

After doing so, locate the SLA policy to edit and click on it. This will open
the SLA policy settings, where you can make the needed changes,

After doing so, click the black `Save` button to update the SLA policy.

## Deleting a service level agreement via Zendesk

**Note**: Some SLA policies are tied to the contracts our customers sign upon
getting a subscription. This means these changes can cause a huge impact. Please
ensure all change management processes are being followed.

To delete a service level agreement in Zendesk, you first need to go to the Admin
Center
([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From
there, you need to go to the Service level agreements page (Objects and rules >
Business rules > Service level agreements).

After doing so, locate the SLA policy to edit and hover over it. You will then
click the gear icon on the right-hand side of the SLA policy. From there, click
on `Delete`. A pop-up box will appear asking you to confirm the deletion. To
confirm, click the black `Delete policy` button.

## Service level agreement standards

To ensure all SLA policies we utilize are both consistent in nature and
transparent in their actions, we strive to meet some standards on all SLA
policies we work with.

### Naming standards

The name used for the SLA policy should be simple, clear, and concise. You want
the name to convey what the SLA policy is used for.

### Condition standards

Generally speaking, we aim to make SLA policy conditions as simple as possible.
When possible, you should use condition sets that are very specific and
succinct. As an example, if you wanted a SLA policy to only run when the form is
`Support Ops`, it is better to simply put a condition of "Form is Support Ops"
than adding exclusions for *every* other form. This can take time and practice
to learn, so when in doubt, pair with the rest of the Support Ops team!

## Change management

As these are maintained via sync repositories, our standard change management
process applies to all Zendesk service level agreements. See
[standard change management](/handbook/support/readiness/operations/docs/change_management#standard-change-management)
for more information, but please also note
[Service level agreements information](/handbook/support/readiness/operations/docs/change_management#service-level-agreements-information)

#### Labels to use

For all issues and MRs involving service level agreements, the label
`Support-Ops-Category::Zendesk Settings` should be used.

#### Change criticality

Due to the nature and impact adding/editing/deleting Zendesk service level
agreements imposes, all issues/MRs related to Zendesk service level agreements
will be classified as
[criticality 1](/handbook/support/readiness/operations/docs/change_criticalities#criticality-1)

## Notes

The SLA badge/timer will always show the hours until a target is due, or how
long the target has been breached in calendar hours and days, even if an SLA
policy is based on business hours.
