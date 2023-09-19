---
title: Ticket Forms
description: Support Operations documentation page for Zendesk ticket forms
canonical_path: "/handbook/support/readiness/operations/docs/zendesk/forms"
---

## What are ticket form

Ticket forms are the forms utilized by the user to create tickets (when using the web UI). These then translate the responses on the form into ticket metadata.

These fall into one of two types:

- Public - meaning both agents and end-users can see these
- Internal - meaning only agents can see these

## Current Zendesk Global forms

| Name                                                                                           | ID            | Visibility | Category              |
|------------------------------------------------------------------------------------------------|:-------------:|------------|-----------------------|
| [SaaS](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/334447)                        | 334447        | Public     | Support               |
| [SaaS Account](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/360000803379)          | 360000803379  | Public     | Support               |
| [Self-Managed](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/426148)                | 426148        | Public     | Support               |
| [GitLab Dedicated](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/4414917877650)     | 4414917877650 | Public     | Support               |
| [L&R](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/360000071293)                   | 360000071293  | Public     | Support               |
| [Billing](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/360000258393)               | 360000258393  | Public     | Billing               |
| [Professional Services](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/360000647759) | 360000647759  | Public     | Professional Services |
| [Open Partner](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/360000818199)          | 360000818199  | Public     | Support               |
| [Select Partner](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/360000837100)        | 360000837100  | Public     | Support               |
| [Alliance Partners](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/360001172559)     | 360001172559  | Public     | Support               |
| [Support Ops](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/360001801419)           | 360001801419  | Public     | Support Ops           |
| [JiHu](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/360001477519)                  | 360001477519  | Public     | Support               |
| [China Comms Response](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/360001535259)  | 360001535259  | Public     | Support               |
| [Community](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/334467)                   | 334467        | Internal   | Support               |
| [Emergencies](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/360001264259)           | 360001264259  | Internal   | Support               |
| [GitLab Incidents](https://gitlab.zendesk.com/agent/admin/ticket_forms/edit/360001629679)      | 360001629679  | Internal   | Support               |

## Current Zendesk US Federal forms

| Name                                                                                                                        | ID           | Visibility | Category |
|-----------------------------------------------------------------------------------------------------------------------------|:------------:|------------|----------|
| [Support](https://gitlab-federal-support.zendesk.com/admin/objects-rules/tickets/ticket-forms/edit/360000446511)            | 360000446511 | Public     | Support  |
| [Upgrade Assistance](https://gitlab-federal-support.zendesk.com/admin/objects-rules/tickets/ticket-forms/edit/360001434131) | 360001434131 | Public     | Support  |
| [Support Ops](https://gitlab-federal-support.zendesk.com/admin/objects-rules/tickets/ticket-forms/edit/360001421052)        | 360001421052 | Public     | Support  |
| [L&R](https://gitlab-federal-support.zendesk.com/admin/objects-rules/tickets/ticket-forms/edit/360001421072)                | 360001421072 | Public     | Support  |
| [Emergency](https://gitlab-federal-support.zendesk.com/admin/objects-rules/tickets/ticket-forms/edit/360001421112)          | 360001421112 | Public     | Support  |
| [License Issue](https://gitlab-federal-support.zendesk.com/admin/objects-rules/tickets/ticket-forms/edit/360001803151)      | 360001803151 | Internal   | Support  |

## How do we maintain them?

Instead of managing Zendesk ticket forms via Zendesk itself, we instead use
GitLab projects to maintain them. This allows us to have version-controlled
ticket forms.

You can find our Zendesk ticket forms projects via:

- [Zendesk Global](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/ticket-forms-and-fields)
- [Zendesk US Federal](https://gitlab.com/gitlab-com/support/support-ops/zendesk-us-federal/ticket-forms-and-fields)

## Creating a ticket form via Zendesk

To create a ticket form in Zendesk, you first need to go to the Admin Center
([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From
there, you need to go to the Forms page (Objects and rules > Tickets >
Forms).

After doing so, you will click the `Add form` button at the top-right of the
page. This will then load up the new form page.

From here, you will:

1. enter a title form the form
1. determine if the form is internal (agent only) or external (editable for end
   users)
1. what title to show to end users (if the form is editable for end users)
1. What ticket fields to use (and in what order)

After doing this, you will then click the blue `Save` button at the bottom-right
of the page.

From here, you need to edit the *conditions* the form uses for both agents and
end users (for external forms). To do this, locate the form in question and
hover over it. This will allow you to click the three vertical dots on the
right-hand side of the form listing to bring up a pop-up menu. In this menu,
click `Conditions`.

The first page that comes up is the agent conditions. To add a condition, click
the `Add condition` button at the top-right of the page. From here, select which
field the condition applies on. You will then select which value the condition
runs on and what ticket fields to show when the condition is met.

Once you have all the conditions you want for the agent side, click the
drop-down at the top of the page and select `End users`. Here, you will select
the conditions to apply for end-users.

Once you have completed all the conditions you want to add, click the blue
`Save` button in the bottom-right of the page.

## Editing a ticket form via Zendesk

Editing a Zendesk ticket form is very similar to
[creating one](#creating-a-ticket-form-via-zendesk). You will follow the same
steps to get to the forms page.

For editing the ticket form's details/fields, instead of clicking the `Add form`
button, you will instead locate the ticket form to edit in the list and click on
the title. Doing so will bring up the ticket form editor page. From here, you can tweak the
various aspects of the ticket form. Once you have the edits in place, click the
blue `Save` button at the bottom-right of the page.

For editing the ticket form's conditions, instead of clicking the `Add form`
button, you will locate the form in question, hover over the name, and then
click the 3 dots at the far-right side. Doing so will bring up a sub-menu where
you can click the `Conditions` button. Doing so will bring up the form's
conditions editor. Once the edits are in place, click the blue `Save` button at
the bottom-right of the page.

## Deactivating a ticket form via Zendesk

There are actually two ways to deactivate a ticket form in the Zendesk UI. The
quicker way is to go to the forms page, locate the form in question, hover
over it, and click the three vertical dots on the right-hand side. This will
bring up a sub-menu, which contains the option to `Deactivate`. Click that
option and the form will be deactivated.

The alternative way to deactivate a form in the Zendesk UI is from within the
form editor page. At the top-right, clikc the 3 dots to bring up a sub-menu
where you can click the `Deactivate` option.

**Note** You cannot deactivate the default form. You will need to set another
form to the default first.

## Setting the default ticket form via Zendesk

To set the default ticket form in Zendesk, you need to go to the ticket forms
page in the Admin Center. From there, hover over the form in question, click the
3 dots at the right-hand side, and select `Make default`.

## Positioning

By default, new forms gain a position of `N+1`, where `N` is the highest
position value of all forms currently in Zendesk (both active and inactive).
This is desired and we should *rarely* need to change this.

To edit positions in the Zendesk UI, go to the forms page. From there, click the
three horizontal dots at the top-right of the page (on the same line as the
search bar). That will bring up a sub-menu with the option `Edit order.`
Clicking that will then allow you to drag and drop the list of forms into the
order you desire. After making the changes, click the blue `Save` button at the
top right of the page.

## Ticket form standards

To ensure all ticket forms we utilize are both consistent in nature and
transparent in their actions, we strive to meet some standards on all
ticket forms we work with.

#### Naming standards

The name used for the form should be simple, clear, and concise. You want the
name to convey what the form is used for.

#### Title shown to end users

For this, you want the title to indicate what the form is for in a way any
GitLab user would understand. As such, you should use methods such as "Support
for xxx" or "Contact the xxx team".

#### Appearance

Many of the decisions made on how you generate/edit a ticket form is based on
how it will appear for end-users. As such, you should strive to ensure all
changes create a pleasing and simple process for end-users to submit tickets.

## Change management

As these are maintained via sync repositories, our standard change management
process applies to all Zendesk forms. See
[standard change management](/handbook/support/readiness/operations/docs/change_management#standard-change-management)
for more information.

#### Labels to use

For all issues and MRs involving forms, the label
`Support-Ops-Category::Forms` should be used.

#### Change criticality

Due to the nature and impact adding/editing/deleting Zendesk ticket forms
imposes, all issues/MRs related to Zendesk ticket forms will be classified as
either
[criticality 1](/handbook/support/readiness/operations/docs/change_criticalities#criticality-1)
or
[criticality 2](/handbook/support/readiness/operations/docs/change_criticalities#criticality-2)
