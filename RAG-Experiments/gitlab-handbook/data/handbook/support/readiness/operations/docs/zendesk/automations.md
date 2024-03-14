---
title: Automations
description: Support Operations documentation page for Zendesk automations
canonical_path: "/handbook/support/readiness/operations/docs/zendesk/automations"
---

## What are Zendesk automations?

As per
[Zendesk](https://support.zendesk.com/hc/en-us/articles/203662236-About-automations-and-how-they-work):

> Automations are similar to triggers because both define conditions and actions
> that modify ticket properties and optionally send email notifications to
> customers and agents. Where they differ is that automations execute when a
time event occurs after a ticket property was set or updated, rather than
immediately after a ticket is created or updated.

The simpler way to think of it is automations are triggers that do not run
instantly. They are time based than event based.

## How do we maintain them?

Instead of managing Zendesk automations via Zendesk itself, we instead use
GitLab projects to maintain them. This allows us to have version-controlled
automations.

You can find our Zendesk automation projects via:

- [Zendesk Global](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/automations)
- [Zendesk US Federal](https://gitlab.com/gitlab-com/support/support-ops/zendesk-us-federal/automations)

## Creating an automation via Zendesk

To create an automation in Zendesk, you first need to go to the Admin Center
([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From
there, you need to go to the Automations page (Objects and rules > Business
rules > Automations).

After doing so, you will then click the `Add automation` button on the top-right
side of the page. This will then load up the new automation page.

From here, you will:

1. enter a title for the automation.
1. enter the conditions that **all** must be met to trigger this automation.
1. enter the conditions of which **any** of them can trigger this automation (in
   conjunction with the **all** conditions).
1. enter the actions for the automation to perform

After doing this, you will then click the blue `Create automation` button.

**Note**: By default, the automation's position will be set to the bottom of the
select category. To adjust this, see [Positioning](#positioning).

## Editing an automation via Zendesk

Editing a Zendesk automation is very similar to
[creating one](#creating-an-automation-via-zendesk). You will follow the same
steps to get the automations page. Instead of clicking the `Add automation`
button, you will instead locate the automation to edit in the list and click on
the title (if your automation is currently inactive, you will need to click the
`Inactive` tab, located above the list of automations).

Doing so will bring up the automation editor page. From here, you can tweak the
various aspects of the automation. Once you have the edits in place, ensure the
dropdown at the bottom right says `Update` and click the blue `Submit` button.

## Deactivating an automation via Zendesk

There are actually two ways to deactivate an automation in the Zendesk UI. The
quicker way is to go to the automation page, locate the automation in question,
hover over it, and click the three vertical dots on the right-hand side. This
will bring up a sub-menu, which contains the option to `Deactivate`. Click that
option and the automation will be deactivated.

The alternative way to deactivate an automation in the Zendesk UI is from within
the automation editor page. At the bottom right, ensure the dropdown says
`Deactivate` and then click the blue `Submit` button.

**Note**: Deactivating an automation does not change its position. This value is
retained in the backend. Re-enabling the automation will have it take the same
position it was in while previously active.

## Positioning

Many components of Zendesk using positioning to determine the overall run order.
With automations being time-based events, it is not often as important to worry
about positioning as with something like triggers or views. We should still
strive to be very deliberate in the positioning we use. A good thought to have
is "what order would I want these running in if they all ran at once?"

By default, new automations gain a position of `N+1`, where `N` is the highest
position value of all automations currently in Zendesk (both active and
inactive). This is desired and we should *rarely* need to change this.

To edit positions in the Zendesk UI, go to the automations page. From there,
click the three horizontal dots at the top-right of the page (on the same line
as the search bar). That will bring up a sub-menu with the option
`Reorder page.` Clicking that will then allow you to drag and drop the list of
automations into the order you desire. After making the changes, click the blue
`Save` button at the top right of the page.

**Note**: Both active and inactive automations have a integer positional value.
While this does not matter in the UI, it will matter in the repo sync we
utilize.

## Automation standards

To ensure all automations we utilize are both consistent in nature and
transparent in their actions, we strive to meet some standards on all
automations we work with.

#### Naming standards

As Zendesk automations do not support categorization at this time, we have
implemented a naming standard to help categorize the automations we have. This
standard is as follows:

`What it impacts::What it does/Who it impacts::Name of automation`

###### Example 1

If you were making an automation to send a notification to Jason once a ticket
has been in an open state for more than 24 hours, you would use the automation
name of:

`Notifications::Jason::Notify ticket has been open for more than 24 hours`

This is because:

- the `What it impacts` is "Notifications", since it sends a notification.
- the `What it does/Who it impacts` is "Jason", since it sends a
  notification to Jason.
- the `Name of automation` can be whatever the creator wants for this, but it
  should be relatively short and describe the automation in a way that anyone
  who knows our naming standards can look at it and know what it does.

###### Example 2

If you were making an automation that sets a ticket to `Closed` after it has
been in the state of Solved for 24 hours, you would use the automation name of:

`Status::Close::Autoclose after 24 hours solved`

This is because:

- the `What it impacts` is "Status", since it impacts a ticket's status.
- the `What it does/Who it impacts` is "Close", since it closes a ticket.
- the `Name of automation` can be whatever the creator wants for this, but it
  should be relatively short and describe the automation in a way that anyone
  who knows our naming standards can look at it and know what it does.

#### Condition standards

Generally speaking, we aim to make automation conditions as simple as
possible. When possible, you should use condition sets that are very specific
and succinct. As an example, if you wanted an automation to only run when the
form is `Support Ops`, it is better to simply put a condition of "Form is
Support Ops" than adding exclusions for *every* other form. This can take time
and practice to learn, so when in doubt, pair with the rest of the Support Ops
team!

## Change management

As these are maintained via sync repositories, our standard change management
process applies to all Zendesk automations. See
[standard change management](/handbook/support/readiness/operations/docs/change_management#standard-change-management)
for more information.

#### Labels to use

For all issues and MRs involving automations, the label
`Support-Ops-Category::Automations` should be used.

#### Change criticality

As automations tend to have far less of an impact, adding/editing/deleting
Zendesk automation issues/MRs will be classified as either
[criticality 2](/handbook/support/readiness/operations/docs/change_criticalities#criticality-2)
or
[criticality 3](/handbook/support/readiness/operations/docs/change_criticalities#criticality-3)
