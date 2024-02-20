---
title: Account deletions
description: Support Operations documentation page for the account deletion form and processor
canonical_path: "/handbook/support/readiness/operations/docs/gitlab/account_deletions"
---

## What is the account deletion form?

The account deletion form is a simple HTMl form generated via GitLab Pages that
is used for account deletion and data privacy requests.

The source code for it is located
[here](https://gitlab.com/gitlab-com/support/support-ops/forms/account-deletion).

## What is the account deletion processor?

The account deletion processor is a set of scripts that handle requests sent
from the account deletion form.

The source code for it is located
[here](https://gitlab.com/gitlab-com/support/support-ops/other-software/account-deletion-processor).

## What are the triage policies?

Utilizing the
[GitLab Triage Gem](https://gitlab.com/gitlab-org/ruby/gems/gitlab-triage), the
triage policies are a group of conditions and actions that are enacted upon
issues within the
[Account Deletion and Other Requests project](https://gitlab.com/gitlab-com/gdpr-request).

The source code for it is located
[here](https://gitlab.com/gitlab-com/gdpr-request/-/blob/master/.triage-policies.yml)

## How does it all work?

The account deletion form, when submitted, sends an AJAX request to trigger a
pipeline on ops.gitlab.net. This then runs the code of the account deletion
processor.

The account deletion processor will then analyze the response to determine the
validity of the request itself. The end result of this analyzing is an issue
being created via service desk.

The triage policies of the project where the issue is made then act on the issue
depending on the various conditions used within.

## Change management

As these are maintained via sync repositories, our standard change management
process applies to all account deletion form or processor changes. See
[standard change management](/handbook/support/readiness/operations/docs/change_management#standard-change-management)
for more information.

#### Labels to use

For all issues and MRs involving account deletion form changes, the label
`Support-Ops-Category::Forms` should be used.

For all issues and MRs involving account deletion processor or triage policy
changes, the label `Support-Ops-Category::GitLab Projects` should be used.

#### Change criticality

As this tool is vital to properly handling account deletion and data privacy
requests, all issues/MRs related to any of the components of account deletion
will be classified as either
[criticality 1](/handbook/support/readiness/operations/docs/change_criticalities#criticality-1)
or
[criticality 2](/handbook/support/readiness/operations/docs/change_criticalities#criticality-2)
