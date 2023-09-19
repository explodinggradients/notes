---
title: Agents
description: Support Operations documentation page for Zendesk agents
canonical_path: "/handbook/support/readiness/operations/docs/zendesk/agents"
---

## Zendesk Global user fields

| Name                                                                                              | ID            | Type      | Field Key       |
|---------------------------------------------------------------------------------------------------|---------------|-----------|-----------------|
| [GitLab User ID](https://gitlab.zendesk.com/admin/people/configuration/user_fields/360000106219)  | 360000106219  | Numeric   | gitlab_user_id  |
| [GitLab username](https://gitlab.zendesk.com/admin/people/configuration/user_fields/360000106179) | 360000106179  | Text      | gitlab_username |
| [Manager Tag](https://gitlab.zendesk.com/admin/people/configuration/user_fields/5051734877596)    | 5051734877596 | Text      | manager_tag     |
| [Not Available](https://gitlab.zendesk.com/admin/people/configuration/user_fields/5051748442140)  | 5051748442140 | Checkbox  | not_available   |
| [User Region](https://gitlab.zendesk.com/admin/people/configuration/user_fields/4417373033234)    | 4417373033234 | Drop-down | user_region     |

## Zendesk US Federal user fields

| Name                                                                                                              | ID            | Type      | Field Key       |
|-------------------------------------------------------------------------------------------------------------------|---------------|-----------|-----------------|
| [GitLab User ID](https://gitlab-federal-support.zendesk.com/admin/people/configuration/user_fields/360001583892)  | 360001583892  | Numeric   | gitlab_user_id  |
| [GitLab username](https://gitlab-federal-support.zendesk.com/admin/people/configuration/user_fields/360001592971) | 360001592971  | Text      | gitlab_username |
| [Manager Tag](https://gitlab-federal-support.zendesk.com/admin/people/configuration/user_fields/6884606867988)    | 6884606867988 | Text      | manager_tag     |
| [Not Available](https://gitlab-federal-support.zendesk.com/admin/people/configuration/user_fields/6884591898260)  | 6884591898260 | Checkbox  | not_available   |

## Provisioning

#### For Zendesk US Federal

As these require the
[tech stack provisioner](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml)
to manually provision these, an
[Access Request issue](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new)
is required.

Once one has been received, the process will go as follows:

1. Email `people-connect@gitlab.com` the following:
   - Subject: US Citizenship Verification Request
   - Body:
     > Greetings all!
     >
     > Can you verify if NAME is a US Citizen? They are requesting access to the
     > Federal Zendesk instance via ISSUE which does require it.
     >
     > Thanks!

   - Replace NAME with the requester's name
   - Replace ISSUE with the link to the Access Request issue
1. Note the Access Request issue that you have contacted the People team to
   verify US citizenship.
1. If the People team verifies the citizenship:
   - Create the Light Agent manually in the Zendesk US Federal instance.
   - Go into Okta and assign the app to the requester
   - Update the issue letting them know it has been provisioned.
1. If the People team cannot verify the citizenship:
   - Comment on the Access Request issue noting citizenship could not be
     confirmed and that the issue will be closed, as no further action can be
     taken without verification from the People team.
1. You may then provision the user in Zendesk US Federal. Do this by:
   1. Create the user in Zendesk (the role to be used should be included in the
      role based entitlement access request issue). Ensure their groups and other
      such settings are accurate (see the access request issue).
   1. Associate Zendesk Global app in Okta (see
      [Assigning an app via Okta](#assigning-an-app-via-okta) for more info) if
      required.

#### As part of role entitlement on Zendesk Global

2 days after someone starts working at GitLab, an access-request issue is
generated based off their role based entitlements. We would manually provision
users based off the request itself.

to do this, you will need to:

1. Create the user in Zendesk (the role to be used should be included in the
   role based entitlement access request issue). Ensure their groups and other
   such settings are accurate (see the access request issue).
1. Associate Zendesk Global app in Okta (see
   [Assigning an app via Okta](#assigning-an-app-via-okta) for more info) if
   required.

#### For light agents on Zendesk Global

To obtain a Light Agent in Zendesk Global, the requester must send an email to
`gitlablightagent.2lba7m@zapiermail.com`. After doing so, they will receive an
automated reply with the result of your request. It must be sent via a GitLab
Google / Gmail account. Any other address will be declined. The Subject and
Body fields of the email can be empty in the email itself, as they have no
bearing on the process for this.

Once set up, the requester will need to wait up to 24 hours for the account to
be assigned the Zendesk Global app in Okta. Once the Zendesk Global app is
assigned, the requester should be able to log in. If that doesn't work correctly
for the requester, they should reach out via the in slack via
[#support-operations](https://gitlab.slack.com/archives/C018ZGZAMPD).
In most cases, people who don't get access within the 24 hours already had an
issue occur on the Okta side.

##### How does this work

When the email is sent to Zapier, it will first validate the email address used.
If it is a gitlab.com email address, it will then locate the user in Zendesk
Global.

If the user is found, it will ensure they are marked as ana gent with the role
of Light agent.

If the user is not found, it will create the user and then ensure they are
marked as and gent with the role of Light agent.

#### By special request

Any special request issues to provision on either Zendesk instance not related
to role based entitlements need to be assigned to a Support Operations Manager
and handled by them.

## Special setups

#### Support team

The Support team (including Support Readiness) utilizes sync mechanisms to
manage various aspects of our agents:

- [Zendesk Global](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/agents)
- [Zendesk Us Federal](https://gitlab.com/gitlab-com/support/support-ops/zendesk-us-federal/agents)

These run daily pipelines that sync various aspects of an agent to Zendesk, such
as:

- GitLab.com user ID
- GitLab.com username
- Groups
- Manager tag
- Name
- Out of Office status
- Signature
- Some user tags
- User region (Zendesk Global only)

Any modifications to a Support agent in Zendesk will be overridden by this.

#### Partner Support team

This is a specialized group of light agents who are allowed to file some types
of Internal Requests. These agents will need the tag `partner_support_agent`
added on their Zendesk account.

#### Order Management team

This is a specialized group of light agents who are allowed to file some types
of Internal Requests. These agents will need the tag `order_management_team`
added on their Zendesk account.

#### OEM  Management team

This is a specialized group of light agents who are allowed to file some types
of Internal Requests. These agents will need the tag `oem_management_team`
added on their Zendesk account.

## Deprovisioning

You will, from time to time, get a request to deprovision an agent (these will
mostly stem from Offboarding tasks). To deprovision an agent, go to that
agents's page in Zendesk and do the following:

- Unassign any active tickets (less than Closed) from that agent (assign them to
  their manager)
- Remove any of the agent's tags from Tags section
- Demote the agent's role to that of end-user
- Suspend the end-user
- After doing so, do the following on the issue requesting the deprovisioning
  - Check the corresponding boxes on the request issue
  - Add the label `SupportOps::Completed`
  - Add your time spent on the issue
  - Unsubscribe from the issue (optional)

## Assigning an app via Okta

**Note** This is not normally needed unless something went wrong with the
automated provisioning process.

To assign an app to a user in Okta, you first need to go to the
[Okta admin dashboard](https://gitlab-admin.okta.com/admin/dashboard). From
there, click on `Applications` on the left-hand side of the page, then select
the `Applications` option that appears below it. This will take you to the
[applications page](https://gitlab-admin.okta.com/admin/apps/active).

From this page, click the application you are needing to assign (which should be
[Zendesk Global](https://gitlab-admin.okta.com/admin/app/zendesk/instance/0oa7db6n2mJ6XP0oL356/#tab-assignments)
or
[Zendesk US Federal](https://gitlab-admin.okta.com/admin/app/zendesk/instance/0oa17cyes3JepgPZg357/#tab-assignments)
for the sake of this documentation page).

After doing so, click the blue `Assign` button, then select the
`Assign to People` option. You will search (by email) for the person in
question. After locating them, click the blue `Assign` link to the right of the
row of that person.

On the pop-up that appears, simply click the blue `Save and Go Back` button to
complete the assignment.

## Change management

As the agents changes are unique in deployment, please see
[Zendesk agents change management](/handbook/support/readiness/operations/docs/change_management#zendesk-agents-change-management)
for more information.

#### Labels to use

For all issues and MRs involving agents that are not related to provisioning and
deprovisioning, the label `Support-Ops-Category::Orgs and Users` should be used.

For ones relating to provisioning and deprovisioning, see the above sections.

#### Change criticality

Due to wildly varying nature and impact adding/editing/deleting Zendesk
agents can impose, all issues/MRs related to Zendesk organizations need to have
their criticality
[manually determined](/handbook/support/readiness/operations/docs/change_criticalities#determining-criticality)
