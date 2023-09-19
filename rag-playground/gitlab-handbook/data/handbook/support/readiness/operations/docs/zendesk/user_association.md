---
title: User Association
description: Support Operations documentation page for Zendesk user association
canonical_path: "/handbook/support/readiness/operations/docs/zendesk/user_association"
---

User association is a very specific and particular process. This is for both
security and accuracy.

## Via Zendesk

**Note** This only applies to Zendesk Global for organizations not using a
contact management project.

Before proceeding, ensure a user has either
[proved their support entitlement](#proving-support-entitlement) or the request
to associate the user in question is coming from an already associated user (of
and organization not using a contact manaement project).

If the organization does not have a contact management project, you may then
associate the user to the organization by copying the full organization name
and then pasting it in the `Org` input field for the user in question (make sure
to click the organization that appears after doing so to finish the
association).

#### Proving support entitlement

When a user is not associated to an organization, they may need to prove their
support entitlement. You can request this using the macro
`Support::Support Ops::Proof of support entitlement`.

Once the user has replied with the requested information, the next steps depend
on the product offering being used (see
[Locating the Salesforce ID for SaaS customers](#locating-the-salesforce-id-for-saas-customers)
or
[Locating the Salesforce ID for Self-Managed customers](#locating-the-salesforce-id-for-self-managed-customers)
 for more info). Ultimately, we need to get the Salesforce ID so we can search for them in
Zendesk.

**Note**: This can be tricky and some nuisances can occur. If you encounter
issues locating an account, please reach out to your fellow Support Operations
Specialists for assistance.

Once the Salesforce ID is located, search Zendesk to locate the organization.
You want to search based on the salesforce_id field, so you would want your
search query to look like:

`salesforce_id:ID_NUMBER*`

<https://gitlab.zendesk.com/agent/search/1?copy&type=organization&q=aaa>
Replacing `ID_NUMBER` with the Salesforce ID you located (putting the asterisk
at the end ensures your search will work regardless of the ID value being the 15
or 18 character ID). Make sure to click the `Organizations` tab of the search
results!

Once you have located the organization, check if it has a contact management
project or not. The quickest way to do this is to go to the organization's page
and check if the `Contact Management Project ID` field is blank or not.

If the organization has a contact management project, we cannot proceed forward.
The organization would need to add the user in question via the contact
management project.

>> Note: If customer purchased AWS license (AWS AMI with GitLab domain email),
please use [this organization](https://gitlab.zendesk.com/agent/organizations/9306291514524)
to associate. Please read the organization notes carefully.

##### Locating the Salesforce ID for SaaS customers

For SaaS customers, we need to use a combination of the `GitLab Super App` and
the `Support Ops Super App`.

To start, you will need to locate the parent namespace that has a valid paid
subscription. To do this, search for the user in question via the GitLab Super
App, using the `User Lookup` plugin. Once you have done the search, click the
`Group memberships` list and review the output provided. You are looking for a
namespace with a paid subscription (bronze, silver, or gold) that is **not** an
internal team member namespace. You want the value right after `groups/` in the
URL (and nothing after it).

An alternative is if, when you do the `User Lookup`, you see the
`Provisioned by` value shows an ID or namespace. If that is the case, you can
use that value.

**Note** If the user not a a member of a paid namespace and the value of
`Provisioned by` is null, the user has not passed proving support entitlement.
They will need to be added to a paid namespace before we can proceed.

With that value, use the `Namespace Lookup` plugin in the Support Ops Super App
to search for the top-level namespace. The output from this plugin will give you
the namespace's ID.

##### Locating the Salesforce ID for Self-Managed customers

For Self-Managed customers, we need to locate them in
[cDot](https://customers.gitlab.com/admin):

1. Locate the customer account in [cDot](https://customers.gitlab.com/admin)

- If given a license ID number:
    1. Navigate to
       `https://customers.gitlab.com/admin/license/xxx` (replacing `xxx` with
       the license ID)
    1. Copy the `Email` on the license and search cDot using that (via the
       [customer page](https://customers.gitlab.com/admin/customer)). Make sure
       to end on the `Show` page of the customer pages.
- If given the license email. search the licenses (via the
    [license page](https://customers.gitlab.com/admin/license)). Then use the
    information detailed above (`If given a license ID`).

1. Locate the billing account of the customer in
   [cDot](https://customers.gitlab.com/admin). This is done on the customer page
   by clicking the link for `Billing accounts`
1. Copy the Salesforce ID

## Via contact management projects

**Note** This only applies to Zendesk Global.

As the organization controls who is/isn't in the contacts.yaml files for these,
we are not involved on these.

For information on managing a contact management project, please see
[Contact Management Projects](/handbook/support/readiness/operations/docs/gitlab/contact_management_projects).

## Via the zendesk-salesforce sync

**Note** This only applies to Zendesk US Federal.

As the management of organization contacts is handled solely via the
zendesk-salesforce sync, we are not involved on these.

For information on how the contacts are sync, please see
[Zendesk US Federal users sync](/handbook/support/readiness/operations/docs/zendesk/zendesk_salesforce_sync/#zendesk-us-federal-users-sync)

## Change management

These are done solely via tickets.
