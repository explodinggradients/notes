---

title: Name Squatting Policy
description: "Workflow for releasing a namespace deemed dormant by GitLab's Name-squatting Policy"
category: GitLab.com
subcategory: Accounts
---



### Overview

According to the [statement of support](/support/gitlab-com-policies/#name-squatting-policy), namespaces may be released when they meet the appropriate criteria, and requested **by a paid customer** (member of a paid namespace or a self-managed customer migrating to SaaS).

**IMPORTANT NOTE:** If you have any situation that is unusual, or does not fall under the workflow below, [open an Issue](https://gitlab.com/gitlab-com/gl-security/security-operations/trust-and-safety/operations/-/issues/new?issuable_template=General%2BUncategorized) with Security Operations. Describe the situation and request them to review and provide guidance.

**NOTE:** When applying any of the macros ensure to replace the placeholder **“REQUESTEDNAME”** with the namespace requested.

### Workflow

1. Search for the requested namespace in GitLab.com admin: [users](https://gitlab.com/admin/users) or [groups](https://gitlab.com/admin/groups), once found visit the GitLab admin page for the namespace.
1. Apply the [`Support::SaaS::Name Squatting Policy::Internal Checklist`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360051569860) macro in Zendesk. Please remember, impersonating a user will reset the Last Sign-In values on the user account such as `Last Sign-In IP` and `Last Sign-in at` (Impersonation should be avoided when reviewing activity on a Personal Namespace).
1. Answer all questions in the **Internal Checklist** (Yes/No) ensuring to cross-check the information found in the admin section.
1. If the namespace is eligible for immediate release, follow [Request successful](#request-successful).
1. If the namespace is eligible for release, but requires attempting to contact the owner, follow [Namespace needs owner contact](#namespace-needs-owner-contact).
1. If the namespace is not eligible for release, follow: [Namespace is not available](#namespace-is-not-available).

### Namespace needs owner contact

Contact Owner:

1. Create a **new Zendesk ticket** with the **namespace owner's email address** as the requester (found in admin) by following [**this specific workflow to create ticket and user**](https://handbook.gitlab.com/handbook/support/readiness/operations/docs/zendesk/tickets/#creating-tickets-for-outbound-requests)
1. Apply the macro `General::Outbound Contact Request` that ensure the new ticket routes properly and the end-user we wish to contact receives the correct notification.
1. Apply the [`Support::SaaS::Name Squatting Policy::Contact Namespace Owner`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360051465059) macro and mark the ticket as **On-hold**.
1. Make an internal comment providing a link to the **namespace requester's ticket**.

If the group contains multiples owners, contact one owner per ticket. Limit to 3 owners if more (you can pick the owners that have the most recent *Last activity* in the page `https://gitlab.com/groups/<group_name>/-/group_members` or/and the owner(s) that is(are) listed as *Source* if still an owner at the time of the namesquatting request).

Requester's Ticket:

1. Copy the ticket's link and add it to the **Internal Checklist**.
1. Reply to the requester with the [`Support::SaaS::Name Squatting Policy::First Response`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360051569840) macro and mark ticket as **On-hold**.

#### Namespace owner responded

If the namespace owner makes a response (don’t remove my namespace) follow these steps:

1. Use the following snippet as the response in the **namespace owner's** ticket and set the ticket to `solved`:

<details>
  <summary markdown="span">Namespace Owner Response - Received</summary>

  <p>Hi,</p>

  <p>Thank you for confirming that you wish to maintain control of the requested namespace.  Per our [Name Squatting Policy](https://about.gitlab.com/handbook/support/workflows/namesquatting_policy.html#namespace-owner-responded), we have cancelled this request and will not release your namespace.</p>

  <p>I'll mark this ticket as solved, please reach out if you have any further questions.</p>
</details>

1. Apply the [`Support::SaaS::Name Squatting Policy::Failed Namespace Request`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360051465039) to the **namespace requester's ticket**.

#### Namespace owner has not responded

If after one week there has been no response, apply the [`Support::SaaS::Name Squatting Policy::Contact Namespace Owner`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360051465059) macro a second time (replace `within 2 weeks` in the macro with the due date. Eg. `**before the 25th of March**`) and mark the ticket as **On-hold**.

After two weeks, the ticket will be **automatically marked as open and an email sent to the assigned engineer**.

If the namespace owner has made no response, follow the [Request successful](#request-successful) steps.

### Request successful

If the request is successful, follow these steps:

For users, change the owner's username with [Chatops](https://docs.gitlab.com/ee/development/chatops_on_gitlabcom.html):

1. In Slack, run `/chatops run user idle <owner_username>`.
1. Add an [Admin note](https://about.gitlab.com/handbook/support/workflows/admin_note.html).

If you'd prefer to use admin, or for groups, rename the owner's namespace with these steps:

1. Navigate to the namespace in admin - [users](https://gitlab.com/admin/users) or [groups](https://gitlab.com/admin/groups)
1. Select “Edit” on the profile.
1. Append "_idle" to the username in case of a user, or to the group URL in case of a group.
1. Add an [Admin note](https://about.gitlab.com/handbook/support/workflows/admin_note.html).
1. Save changes.

In Zendesk:

1. Apply the [`Support::SaaS::Name Squatting Policy::Successful Namespace Request`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360051569820) macro to the **Namespace requesters ticket** and mark the ticket as **Solved**.

### Namespace is not available

1. Apply [`Support::SaaS::Name Squatting Policy::Failed Namespace Request`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360051465039) macro and mark ticket as **Solved**.

### FAQs

1. **Does a login in response to a name squatting request mean that the account is active?**

   No, the user has to explicitly reply to the name squatting request saying "I want to keep my namespace". If the user hasn't responded and has just logged in, send a final message saying something like, "I see you logged in at X, but you need to let us know here if you want to keep your namespace".

1. **What constitutes data in the account?**

   A group, a project, etc. means data. Unless the project or group is empty, or there's been no activity for 2 or more years.

1. **Is namespace squatting permitted?**

   Namespace squatting is not permitted as explicitly stated in our [terms](https://about.gitlab.com/terms/). User and group names are provided on a first-come, first-served basis and may not be reserved.

1. **Does using a trademark in a way that has nothing to do with the product or service for which the trademark was granted considered a violation of trademark policy?**

   Using another's trademark in a way that has nothing to do with the product or service for which the trademark was granted is not a violation of trademark policy. Claiming trademark infringement is a legal process, and we will not release a namespace for trademark violation without a court order.

1. **Should we release a namespace even if the request might seem questionable?**

   Yes, we should always release the namespace as long as it meets the release criteria. Trust and Safety will take the necessary steps to mitigate any abusive activity which may subsequently originate from the namespace. See [Support Team Meta issue 3145](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/3145) for discussion and additional context from Support, Legal, and Trust and Safety.

__________________

**Macros**

- [`Support::SaaS::Name Squatting Policy::Failed Namespace Request`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360051465039)
- [`Support::SaaS::Name Squatting Policy::Internal Checklist`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360051569860)
- [`Support::SaaS::Name Squatting Policy::First Response`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360051569840)
- [`Support::SaaS::Name Squatting Policy::Contact Namespace Owner`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360051465059)
- [`Support::SaaS::Name Squatting Policy::Successful Namespace Request`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360051569820)

**Automations**

- [`Status::Open::Reopen namesquatting On-hold tickets after 1 week`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=20012489&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+94693587)
