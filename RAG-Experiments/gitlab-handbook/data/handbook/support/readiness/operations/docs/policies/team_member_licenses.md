---
title: Team member licenses
description: Support Operations policies page for team member licenses
canonical_path: "/handbook/support/readiness/operations/docs/policies/team_member_licenses"
---

## The process

The process for these is:

1. The GitLab team member files an access request (AR) using the
   [GitLab Team Member License request template](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=GitLab_Team_Member_License_request).
1. GitLab team member pings Support Ops.
1. Support Operations logs into the staging
   [staging cDot app](https://customers.staging.gitlab.com/admin/license/new_license)
   and generates the license using the parameters in the AR.
1. Support Operations updates the AR and closes it out.

#### Creating a license

**Note** Before proceeding, please confirm the requested end date on the issue
does not exceed 1 year. If it does, we cannot proceed with the request until
the requester changes that.

![Creating a license via staging cDot](/handbook/support/readiness/operations/images/generating_license_via_staging.gif)

1. Login to the
   [staging cDot app](https://customers.staging.gitlab.com/admins/sign_in) via
   Okta.
1. Click the [Licenses](https://customers.staging.gitlab.com/admin/license) link
   on the left-hand side of the page.
1. Click the
   [+ Add new License](https://customers.staging.gitlab.com/admin/license/new_license)
   at the top of the page.
1. Fill out the details on the form
1. Click the `✓ Save` button at the bottom of the form.

   | Field                   | Value                              |
   |-------------------------|------------------------------------|
   | License Type            | Legacy License                     |
   | Name                    | GitLab team member's full name     |
   | Company                 | `GitLab - Team Member License`     |
   | Email                   | GitLab team member's company email |
   | Zuora subscription ID   | leave this blank                   |
   | Zuora subscription name | leave this blank                   |
   | Users count             | value from the AR                  |
   | Previous users count    | 0 or value from the AR             |
   | Trueup count            | 0 or value from the AR             |
   | Plan code               | value from the AR                  |
   | Trial                   | leave unchecked                    |
   | Start date              | today's date                       |
   | End date                | value from the AR                  |
   | Notes                   | the AR link                        |

#### Updating the issue

After you have generated the license, you need to reply and close out the issue.
To do this, reply with the following:

> The staging license has been generated at this time.
>
> As this is a staging license, please keep in mind you *must* setup your GitLab
> deployment to work with those. For more information on doing this, please see
> [our documentation](https://docs.gitlab.com/omnibus/development/setup.html#use-customers-portal-staging-in-gitlab).
>
> For information on applying a license, please read through
> [our documentation](https://docs.gitlab.com/ee/user/admin_area/license.html#activate-gitlab-ee-with-a-license-file).

After sending that reply, do the following:

- Add time spent on the issue
- Add the label `~SupportOps::Completed` to the issue
- Close the issue
