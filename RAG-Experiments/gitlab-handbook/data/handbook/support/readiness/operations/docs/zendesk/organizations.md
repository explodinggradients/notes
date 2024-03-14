---
title: Organizations
description: Support Operations documentation page for Zendesk organizations
canonical_path: "/handbook/support/readiness/operations/docs/zendesk/organizations"
---

## What are Zendesk organizations?

Organizations are simply a collection of users in Zendesk (much like groups). We
use them to also store metadata (synced from Salesforce), which is used to
determine such things as SLA, ARR, etc.

## How are organizations created and maintained?

Organizations in Zendesk are created automatically through our sync script.

> Please do not manually create organizations except in approved situation. This
> can break the ZD<>SFDC integration and cause users to receive incorrect SLAs.
> If you notice an organization needs to be created, please notify support-ops
> to rectify this.

For more information on this, please see
[Zendesk-Salesforce Sync](/handbook/support/readiness/operations/docs/zendesk/zendesk_salesforce_sync)

## Editing Organizations

As a lot relies on organizations being setup properly, this feature requires
admin level abilities currently. If an organization needs to be edited, an issue
should be filed using the
[Zendesk Global Organization](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/organizations/-/issues/new)
or
[Zendesk US Federal Other](https://gitlab.com/gitlab-com/support/support-ops/zendesk-us-federal-project/-/issues/new?issuable_template=Other)
issue template.

## Organization Notes for Zendesk Global

There are two forms of organization notes we utilize:

- Support Operations organization notes
- Support Team organization notes

Support Operations organizations notes are managed via Zendesk in the `Notes`
and `Details` fields on the organization itself.

Support Team organization notes are managed via the
[organizations project](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/organizations).

Aside from Support Operations, all support managers have `Maintainer` access to
the organization project, enabling them the ability to approve and merge MRs in
this repo.

When an organization has a ticket created, a trigger calls to a webhook to
run a pipeline using the
[ticket processor](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/ticket-processor)
(on ops.gitlab.net). This then combines the Support Operations and Support Team
organization notes into internal comments on the ticket itself.

## Organization Notes for Zendesk US Federal

We manage all internal notes on Zendesk itself due to data privacy concerns. As
such, we separate them as such:

- `Notes` are for Support Team organization notes
- `Details` are for Support Operations organization notes

When an organization has a ticket created, a trigger runs to parse both of these
into internal comments on the ticket itself.

## Organizations with outdated information

If you notice an organization in Zendesk contains outdated information or the
information doesn't match what Salesforce is displaying, this would indicate the
sync integration has hit an issue. Luckily, we have the GitLab built sync script
that runs every hour to rectify such issues.

In your due diligence, you would want to create an issue via the
[Zendesk Organization Repo](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/organizations/-/issues/new)
so support-ops can double check to ensure there is nothing blocking the sync.

## Organization fields

#### Current Zendesk Global org fields

| Name                                                                                                                     | ID            | Type      | Field Key                 |
|--------------------------------------------------------------------------------------------------------------------------|:-------------:|-----------|---------------------------|
| [Account Owner](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/360000133994)                  | 360000133994  | Text      | account_owner             |
| [Account Type](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/360000082159)                   | 360000082159  | Drop-down | account_type              |
| [AM Project ID](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/360000092299)                  | 360000092299  | Text      | am_project_id             |
| [ARR](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/1424327)                                 | 1424327       | Decimal   | aar                       |
| [Contact Management Project ID](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/7385051495324) | 7385051495324 | Numeric   | cmp_id                    |
| [Customer Success Manager](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/360000134054)       | 360000134054  | Text      | technical_account_manager |
| [Dedicated SGG](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/5739023764636)                 | 5739023764636 | Drop-down | dedicated_sgg             |
| [Escalated State](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/7765454787740)               | 7765454787740 | Checkbox  | org_in_escalated_state    |
| [Expiration date](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/360001527120)                | 360001527120  | Text      | expiration_date           |
| [GitLab Plan](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/1288848)                         | 1288848       | Drop-down | support_level             |
| [Health Score](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/1900000011334)                  | 1900000011334 | Drop-down | health_score              |
| [Manual Support Upgrade](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/360000209840)         | 360000209840  | Checkbox  | manual_support_upgrade    |
| [Number of Seats](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/360000171880)                | 360000171880  | Decimal   | seats_decimal             |
| [Region](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/360000329019)                         | 360000329019  | Drop-down | org_region                |
| [Restricted Account](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/5661401607452)            | 5661401607452 | Checkbox  | restricted_account        |
| [Sales Segmentation](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/360000080280)             | 360000080280  | Text      | sales_segmentation        |
| [Salesforce ID](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/1288008)                       | 1288008       | Text      | salesforce_id             |
| [SFDC Short ID](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/1900000011354)                 | 1900000011354 | Text      | sfdc_short_id             |

#### Current Zendesk US Federal org fields

| Name                                                                                                                               | ID            | Type      | Field Key                 |
|------------------------------------------------------------------------------------------------------------------------------------|:-------------:|-----------|---------------------------|
| [Account Owner](https://gitlab-federal-support.zendesk.com/admin/people/configuration/organization_fields/360000704052)            | 360000704052  | Text      | account_owner             |
| [Account Type](https://gitlab-federal-support.zendesk.com/admin/people/configuration/organization_fields/360001094611)             | 360001094611  | Drop-down | account_type              |
| [AM Project ID](https://gitlab.zendesk.com/admin/people/configuration/organization_fields/360000092299)                            | 360000092299  | Text      | am_project_id             |
| [ARR](https://gitlab-federal-support.zendesk.com/admin/people/configuration/organization_fields/360001433772)                      | 360001433772  | Numeric   | arr                       |
| [Customer Success Manager](https://gitlab-federal-support.zendesk.com/admin/people/configuration/organization_fields/360000704072) | 360000704072  | Text      | technical_account_manager |
| [Expiration date](https://gitlab-federal-support.zendesk.com/admin/people/configuration/organization_fields/360002828652)          | 360002828652  | Text      | expiration_date           |
| [Health Score](https://gitlab-federal-support.zendesk.com/admin/people/configuration/organization_fields/360002828632)             | 360002828632  | Drop-down | health_score              |
| [Market Segment](https://gitlab-federal-support.zendesk.com/admin/people/configuration/organization_fields/360000712231)           | 360000712231  | Drop-down | market_segment            |
| [Number of Seats](https://gitlab-federal-support.zendesk.com/admin/people/configuration/organization_fields/360000704032)          | 360000704032  | Numeric   | number_of_seats           |
| [Salesforce ID](https://gitlab-federal-support.zendesk.com/admin/people/configuration/organization_fields/360000712211)            | 360000712211  | Text      | salesforce_id             |
| [SFDC Short ID](https://gitlab-federal-support.zendesk.com/admin/people/configuration/organization_fields/360002828612)            | 360002828612  | Text      | sfdc_short_id             |
| [Solutions Architect](https://gitlab-federal-support.zendesk.com/admin/people/configuration/organization_fields/360001525791)      | 360001525791  | Text      | solutions_architect       |
| [Support level](https://gitlab-federal-support.zendesk.com/admin/people/configuration/organization_fields/360000703992)            | 360000703992  | Drop-down | support_level             |

#### Creating organization fields in Zendesk

To create an organization field in Zendesk, you first need to go to the Admin
Center ([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From
there, you need to go to the Organization fields page (People > Configuration >
Organization fields).

After doing so, you will then click the `Add field` button on the top-right side
of the page. This will then load up the new organization field page.

From here, you will:

1. select the type of field
1. enter the display name for the field
1. enter the field key for the field
   - **Note** This cannot be edited once the field is created
1. enter a description for the field
1. enter the field specific values

After doing this, you will then click the blue `Save` button at the bottom-right
of the page.

#### Editing organization fields in Zendesk

To edit an organization field in Zendesk, you first need to go to the Admin
Center ([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From
there, you need to go to the Organization fields page (People > Configuration >
Organization fields).

After doing so, locate the field in question and click on the Display name for
it. This will bring up the organization field editor page.

From here, make the needed changes and then click the blue `Save` button at the
bottom-right of the page.

#### Deactivating organization fields in Zendesk

There are actually two ways to deactivate a organization field in the Zendesk
UI. The quicker way is to go to the organizaton fields page, locate the
organization field in question, and click the three vertical dots on the
right-hand side. This will bring up a sub-menu, which contains the option to
`Deactivate`. Click that option and the organization field will be deactivated.

The alternative way to deactivate an organization field in the Zendesk UI is
from within the organization field editor page. At the top right, click the
Actions button to show a submenu with the `Deactivate` option.

## Organization Permissions

By default, organizations are setup so that the users within it can only see and
comment on their own tickets. This security measure often doesn't work for some
organizations though.

Because of that, we have the ability to setup Shared Organizations, a term
meaning the users in an organization have heightened permissions and can do see
and/or comment on tickets that are not theirs.

#### Shared Organization management

A shared organization is one in which the end-users in said organization have
heightened permissions in regards to tickets created in the organization. The
options available to this are:

- All users can view all tickets but not add comments
- All users can view all tickets and add comments to all tickets
- Specific users can view all tickets but not add comments

To enable this for an organization, a **new** ticket must be filed to Support
Operations using the correct form fields that specific the desire to have a
shared organization setup. This is required as there is a security risk involved
in using a shared organization and the organization itself must accept this
security risk before we can proceed.

Once the ticket comes in, review the fields used on the ticket to determine the
exact setup desired.

##### All users can view all tickets but not add comments

To set this up, go to the organization's page in Zendesk. From there, locate the
`Users` field towards the top-left of the page. Click the drop-down next to it
and select `Can view all org tickets`. Click off the box to save the changes.

Ensure the new drop-down that appears says `...but not add comments` before
concluding the work.

##### All users can view all tickets and add comments to all tickets

To set this up, go to the organization's page in Zendesk. From there, locate the
`Users` field towards the top-left of the page. Click the drop-down next to it
and select `Can view all org tickets`. Click off the box to save the changes.

You will then click the new drop-down that appears and select the option
`...and add comments`. Click off the box to save the changes.

##### Specific users can view all tickets but not add comments

To set this up, you need to locate each user in question in Zendesk first. Once
on the user page, locate the field `Access` towards the top-left of the page.
Click the drop-down next to it and select `Can view tickets from user's org`.
Click off the box to save the changes.

##### Removing a shared organization setup

To remove a shared organization setup, follow the above guides, but instead
ensure the drop-downs use the default options:

- Organizatin: `Can view own tickets only`
- User: `Can view and edit own tickets only`

## User association

There are specific processes and policies around this, so please see
[User Association](/handbook/support/readiness/operations/docs/zendesk/user_association)

#### User Association via Domain Matching

While Zendesk does have the functionality to do domain matching, we have
determined that the security risks inherent in this feature outweigh the
benefits that would be received from its use.

Because of this decsion, as of August 2020, Support Ops will not longer apply
a domain on a Zendesk organization. Any organization that had this applied
prior to this date will have it as a legacy feature.

Because this decision was based on security risks, exceptions will not be made.

## Special situations

There are some situations in which we have to do modifications on organizations
based on the situation itself.

#### Providing gratis support

In some cases, a support manager might determine the best course of action on
an organization that is otherwise ineligible for our support offering is to
provide gratis support.

In such cases, the support manager will file an issue or  merge request in the
[Zendesk Global Organizations project](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/organizations)
to have a Support Team organization note created for the organization. No
action is traditionally needed by Support Operations in most cases unless the
support manager requires assistance in generating the merge request.

#### Migration offerings

In situations where a paid customer is migrating between offerings (SM and
SaaS), and who at the time of a ticket has a paid license to only one of them,
we often desire to provide support to them just the same.

When this occurs, Support or Sales will start the process for a migration
offering. On the Support Operations side, we will need to add a specific
organization note to the organization itself (as a Support Operations
organization note).

The note itself should be:

> This customer is in the process of migrating from one product offering to another. To ensure that during this process their support tickets are given an SLA so that Support Engineers will work on them, you will need to modify the tags on the ticket by removing the starting product's tag and adding the ending product's tag.
>
> Migration information:
>
> - Starting product: INITIAL_OFFERING
> - Ending product: ENDING_OFFERING
> - Self-managed tag(s): SM_TAG
> - SaaS tag(s): SAAS_TAG
>
> When you see this note in a ticket and you are the first to work that ticket, please remove the unneeded SLA tag and add the needed tag based on the subject matter of the ticket.

Be sure to replace the ALL-CAPS tokens with the appropriate values, as described
in this table:

| Term              | Description                                    | Possible values                  |
|-------------------|------------------------------------------------|----------------------------------|
| INITIAL_OFFERING  | The product from which they are migrating      | `SM`, `SaaS`                     |
| ENDING_OFFERING   | The product to which they are migrating        | `SM`, `SaaS`                     |
| SM_TAG            | The self-managed tag the organization is using | `starter`, `premium`, `ultimate` |
| SAAS_TAG          | The SaaS tag the organization is using         | `bronze`, `silver`, `gold`       |

The information needed for the above values should be determined from the issue
filed for the request.

#### Priority Prospects

**Note** This only applies to Zendesk Global. Zendesk US Federal prospects
receive support by default at this time.

By default,
[trial licenses do not include support](https://about.gitlab.com/support/#trials-support)

In specific situations where we desire to grant temporary support for their
trial license, we can setup a priority prospect organization.

##### Process restrictions

- Only 30 priority prospects can exist at any one time. The current reference
  sheet containing who is a priority prospect can be found
  [here](https://docs.google.com/spreadsheets/d/11p3aBj1LTr-ngk1wxoMlae-UvJ3bOTuQHd48so2ZcXU/edit?usp=sharing)
  (internal only)
- An area sales manager must approve a request to create or extend a priority
  prospect
- No more than 2 extensions can be done for a priority prospect.

##### Support restrictions

- This does not include emergency support
- This does not include upgrade assistance support
- This does not include migration assistance support
- This does not include architecture review support
- This does not include namesquatting requests
- This should only be for
  [PoVs](https://about.gitlab.com/handbook/customer-success/solutions-architects/tools-and-resources/pov/)
  involving errors from a setup (and not the setup process itself)
- A maximum of 3 contacts are able to create support tickets for the
  organization.
- This does not include Shared organization setup
- All response times are reasonable effort and will be given an internal SLO of
  24 hours.
- Everything within the
  [statement of support](https://about.gitlab.com/support/statement-of-support/)
  applies.
- This is solely for **prospects**. This means the account type in Salesforce is
  `Prospect`. This cannot be applied to any type of account other than a
  `Prospect`

##### Information for the customer

The customer should never submit a ticket before this process is fully completed
(as indicated by Support Operations in the request issue). Doing so before that
can result in the ticket being rejected.

Once the process is fully completed, the customer should be informed of the
following vital information for submitting tickets:

- All SaaS related tickets should be submitted via
  [this form](https://support.gitlab.com/hc/en-us/requests/new?ticket_form_id=334447&tf_360005241679=saas_prospect_customer)
  unless it is specifically about SaaS Account related matters
- All SaaS Account related matters should be submitted via
  [this form](https://support.gitlab.com/hc/en-us/requests/new?ticket_form_id=360000803379&tf_360005241679=saas_prospect_customer)
- All Self-Managed related tickets should be submitted via
  [this form](https://support.gitlab.com/hc/en-us/requests/new?ticket_form_id=426148&tf_360005182220=sm_prospect_customer)
- Every ticket should ensure the "Tell us about your GitLab subscription" field
  uses the value "Sales Assisted Trial". Any other one could cause routing
  issues for them. This above links automatically populate that when used.
- All tickets must be filed using the contact emails provided in the request.
  Any others will be rejected by the system (and the ticket closed).

##### Setup checks

Before we can proceed, we need to check the following:

- We are not at 30 priority prospects in the
  [current list of priority prospects](https://docs.google.com/spreadsheets/d/11p3aBj1LTr-ngk1wxoMlae-UvJ3bOTuQHd48so2ZcXU/edit?usp=sharing).
  If we are at 30, we need to respond to the issue as such and close it out:
  > I am seeing we are currently at 30 priority prospects. As such, we are not
  > able to set any more up until one of the current one expires or is canceled.
  > Please speak with Sales leadership regarding this matter.
  >
  > Once others have expired or been canceled, you can file a new issue to
  > potentially get your account added as a priority prospect.
  >
  > As such, we are not able to proceed and will close out this issue.
  >
  > /close

- The account in Salesforce has a type of `Prospect`. Only accounts with that
  type are eligible for this setup. If the account does not have a type of
  `Prospect`, you should respond with this information in the issue and close it
  out:
  > I am seeing the SFDC account in question for this request does not have an
  > account type of `Prospect`. Because of technical limitations in the
  > relationship between SFDC accounts and Zendesk organizations, we are not
  > able to setup priority prospect status on accounts unless their SFDC account
  > is listed as `Prospect`.
  >
  > As such, we will not be able to proceed on this request and will now close
  > the issue.
  >
  > You might want to reach out in #spt_managers to speak to a support manager
  > bout other options that may be able to be used for this account.
  >
  > /close

- The ARR listed on the opportunity is over $100,000 or the `Reason for Status`
  given deems the account eligible for priority prospect status. If neither
  situation is satisfied, we need to request further clarification:
  > We are seeing the ARR for this opportunity is under $100,000 and the
  > justification would not satisfy the needs for priority prospect status. Can
  > you please clarify further on why this opportunity requires priority
  > prospect status?

  - NOTE: You should seek Support Operations Manager approval to proceed at this point.

- The prospect is not listed on the
  [list of former priority prospects](https://docs.google.com/spreadsheets/d/1TdMbce83HqSA04mfamqcY7DurNbRs_sqdD68udU0Frw/edit?usp=sharing).
  If they are, we would need to decline the request and close out the issue:
  > We are seeing this account was a priority prospect in the past. As such,
  > they would not qualify to be a priority prospect once more. As such, we are
  > not able to proceed and will close out this issue.
  >
  > /close

- The issue has approval from a member of Sales leadership. If it does not, we
  would need that to occur first. You can choose to wait for that to be obtained
  or reply with something like:
  > I am seeing this has not yet been approved by a member of Sales leadership.
  > We cannot proceed without that being obtained. Please have a member of Sales
  > leadership approve this request **with a comment** so we can proceed.

##### Zendesk setup

After passing all the checks, we can proceed with the setup. The first stage of
the setup begins within Zendesk.

Start by ensuring none of the listed support contacts have existing tickets. If
you do find existing tickets, they need to be closed completely before we can
proceed. Review the ticket to determine if this is an acceptable task. If you
determine it is not, post the ticket in the issue with the message:

> We are seeing the users requested in this issue have a non-closed ticket:
>
> - LIST
> - OF
> - TICKETS
>
> These would need to be completely closed before we could proceed. Please speak
> with the user(s) about the ticket about us closing the ticket before we can
> proceed. Once you have done so, please reply back letting us know they have
> been informed.

You can close a ticket via the API, with a curl request such as:

```bash
curl -ss https://gitlab.zendesk.com/api/v2/tickets/TICKET_ID \
   -H "Content-Type: application/json" \
   -u support-ops@gitlab.com/token:YOUR_ZD_ADMIN_TOKEN \
   -X PUT \
   -d '{"ticket": {"status": "closed"}}'
```

Replacing:

- `TICKET_ID` with the ticket's ID
- `YOUR_ZD_ADMIN_TOKEN` with your admin Zendesk API tokena

##### Organization setup

After doing so, you then need to create the organization in Zendesk. Do this by
hovering over the `+ Add` button at the top-left of Zendesk and then clicking
`Organization`. This will cause a pop-up modal to appear. In the modal, set the
`Name` to `PP: NAME_OF_SFDC_ACCOUNT` (replacing `NAME_OF_SFDC_ACCOUNT` with the
exact name from the Salesforce account). **The domains field should *always* be
empty**.

With that created, you need to edit some of the organization fields:

| Field                  | Value                        |
|------------------------|------------------------------|
| Salesforce ID          | PRIORITY PROSPECT            |
| SFDC Short ID          | PRIORITY PROSPECT            |
| GitLab Plan            | See below                    |
| ARR                    | 0                            |
| Account Owner          | The requester from the issue |
| Account Type           | Prospect                     |
| Manual Support Upgrade | Check this box               |
| Expiration Date        | 30 days from setup           |

For `GitLab Plan`, you need to review the opportunity to determine if this is
a SaaS or Self-Managed opportunity. If you cannot determine it, please ask the
requester on the issue to clarify that.

If it is SaaS, use `Prospect SaaS`. If it is Self-Managed, use `Prospect SM`.

After setting up the organization, you need to add the support contacts from the
issue to the organization.

##### Current priority prospect list setup

After setting it all up on the Zendesk side, you need to add an entry in the
[current list of priority prospects](https://docs.google.com/spreadsheets/d/11p3aBj1LTr-ngk1wxoMlae-UvJ3bOTuQHd48so2ZcXU/edit?usp=sharing).

To do this, populate each field with the following:

| Field            | Value                                                |
|------------------|------------------------------------------------------|
| SFDC ID          | `=hyperlink("SFDC_ACCOUNT_LINK", "SFDC_ACCOUNT_ID")` |
| Org Name         | `=hyperlink("ZD_ORG_LINK", "SFDC_ACCOUNT_NAME")`     |
| SFDC Opportunity | `=hyperlink("SFDC_OPP_LINK", "SFDC_OPP_ID")`         |
| Approver         | `=hyperlink("REQUEST_ISSUE_LINK", "APPROVER")`       |
| Started          | Today's date (YYYY-MM-DD)                            |

Where:

- `SFDC_ACCOUNT_LINK` is the Salesforce account link
- `SFDC_ACCOUNT_ID` is the Salesforce account's 18 digit ID
- `ZD_ORG_LINK` is the link the organization in Zendesk
- `SFDC_ACCOUNT_NAME` is the Salesforce account's name
- `SFDC_OPP_LINK` is the Salesforce opportunity link
- `SFDC_OPP_ID` is the Salesforce opportunity's ID
- `REQUEST_ISSUE_LINK` is the request issue
- `APPROVER` is the name of the approving member of Sales leadership

##### Setting up a reminder

After all that is setup, you need to setup a reminder in Slack to expire the
organization's priority prospect status. You can do this using the command:

`/remind expire LINK on DATE`

Replacing `LINK` with the Zendesk organization link and `DATE` with the
expiration date.

##### Updating the issue

After all this done, let the requester know this has now been setup:

> This has been setup at this time. It is set to expire `DATE`.
>
> /label ~"SupportOps::Completed"
>
> /spend TIME
>
> /close

Replacing:

- `DATE` with the date of expiration (30 days from today)
- `TIME` with the time spent working the issue

##### Extension

For extensions, we merely need to ensure it has approval from a member of Sales
leadership. If it does, you need to:

1. Edit the `Expiration date` on the Zendesk Organization to 30 days beyond
   it's current value
1. Set the `First extension` value for the entry on the
   [current list of priority prospects](https://docs.google.com/spreadsheets/d/11p3aBj1LTr-ngk1wxoMlae-UvJ3bOTuQHd48so2ZcXU/edit?usp=sharing)
   to `Yes`.
1. Set the `Approver` value next `First extension` to for the entry on the
   [current list of priority prospects](https://docs.google.com/spreadsheets/d/11p3aBj1LTr-ngk1wxoMlae-UvJ3bOTuQHd48so2ZcXU/edit?usp=sharing)
   to `=hyperlink("REQUEST_ISSUE_LINK", "APPROVER")`
   - `REQUEST_ISSUE_LINK` is the request issue
   - `APPROVER` is the name of the approving member of Sales leadership

You will then update the issue with a comment:

After all this done, let the requester know this has now been setup:

> The extension has been enabled at this time. The new expiration date is `DATE`.
>
> /label ~"SupportOps::Completed"
>
> /spend TIME
>
> /close

Replacing:

- `DATE` with the date of expiration (30 days from today)
- `TIME` with the time spent working the issue

##### Cancellation

For these, we simply need to cancel the priority prospect status. See
[Expiring priority prospects](#expiring-priority-prospects) for details on doing
that.

After that is all done, update the issue with a comment:

> The priority prospect status has now been canceled.
>
> /label ~"SupportOps::Completed"
>
> /spend TIME
>
> /close

Replacing:

- `TIME` with the time spent working the issue

##### Expiring priority prospects

To expire a priority prospect:

1. Close out any open tickets they currently have
1. Unassociate the users on the organization
1. Uncheck the box on the organization for `Manual Support Upgrade`
1. Add `Expired` to the beginning of the organization's name, followed by a
   space
1. Add `FORMER` to the beginning of the organization's `Salesforce ID`, followed
   by a space
1. Add `FORMER` to the beginning of the organization's `SFDC Short ID`, followed
   by a space

After doing so, you need to populate the data into the
[list of former priority prospects](https://docs.google.com/spreadsheets/d/1TdMbce83HqSA04mfamqcY7DurNbRs_sqdD68udU0Frw/edit?usp=sharing)
for tracking purposes:

| Field        | Value                                                        |
|--------------|--------------------------------------------------------------|
| Org Name     | The Salesforce account's name                                |
| SFDC ID      | `=hyperlink("SFDC_ACCOUNT_LINK", "SFDC_ACCOUNT_ID")`         |
| Tickets      | The number of tickets the organization created               |
| Customer?    | If the SFDC account now shows them as a customer             |
| CARR         | The `CARR (This Account)` value on SFDC account              |
| Proposed ARR | The opportunity ARR from the original request issue          |
| Status Ended | The month and year when the status expired (e.g. March 2021) |

Where:

- `SFDC_ACCOUNT_LINK` is the Salesforce account link
- `SFDC_ACCOUNT_ID` is the Salesforce account's 18 digit ID

After doing all of that, you can erase the entry on the
[current list of priority prospects](https://docs.google.com/spreadsheets/d/11p3aBj1LTr-ngk1wxoMlae-UvJ3bOTuQHd48so2ZcXU/edit?usp=sharing).

## Change management

As the organization changes are unique in deployment, please see
[Zendesk organizations change management](/handbook/support/readiness/operations/docs/change_management#zendesk-organizations-change-management)
for more information.

#### Labels to use

For all issues and MRs involving organization fields, the label
`Support-Ops-Category::Orgs and Users` should be used.

#### Change criticality

Due to wildly varying nature and impact adding/editing/deleting Zendesk
organizations can impose, all issues/MRs related to Zendesk organizations need
to have the their criticality
[manually determined](/handbook/support/readiness/operations/docs/change_criticalities#determining-criticality)
