---

title: Support Assisted Customer Requests
description: "GitLab Support Assisted customer requests"
category: References
---

- TOC
{:toc .hidden-md .hidden-lg}

## Overview

At times Support may be called on to assist customers in requests which require taking actions that wouldn't be possible within the normal structure of
the application.

- migrating a set of users from one identity provider to another
- bulk removing 2FA from a set of users

The purpose of this workflow is to demonstrate the structure of a runbook that includes the steps required before, during, and after scheduled customer work.

A **runbook** is an internal document that details how to handle a particular situation in detail. It is highly technical and aimed at the IC doing the action.

## Project to store runbooks

The runbooks will be stored in an issue in the [runbook project](https://gitlab.com/gitlab-com/support/runbooks/-/issues)
Due to the nature of the information on the runbook, the contents will be `confidential`.

## Runbook structure

### Header

| Runbook name        |   |
|---------------------|---|
| Runbook description |   |
| DRI                 |   |
| Schedule at         |   |
| Meeting URL         |   |
| Gitlab Issue        |   |

Runbook name:

#### Runbook name

A name from the runbook. Please use the format: `CUSTOMER` - `REQUESTED TASK`
So for Acme requesting us to enforce 2FA on all of their groups the name would be:
`Acme - Enforce 2FA on All Groups`

#### Runbook description

A small summary of the work to be done, including the expected result from the task.

#### DRI

The owner of the task and main contact for schedule and execution.

#### Schedule at

The agreed date and time to work with the customer on the task. Include the time zone.

#### Meeting URL

The zoom meeting URL to use.

#### GitLab Issue

Link to the GitLab issue created for this request

### Gitlab - Contacts

| Name | Role | Description |
|-------------|------|-------------|
|             |      |             |

A table showing who is attending the call from GitLab and their role during the task.

### Customer - Contacts

| Name | Role | Description |
|-------------|------|-------------|
|             |      |             |

The customer contact section contains who is joining the call from the customer team and their roles.
This table is optional but a useful element to have to increase the efficiency during the task.

### Pre-call checklist

Mark the item if completed otherwise provide details which prevents it.

- [ ] Inform  `#support_gitlab-com` or `#support_self-managed` and `#support_manager` Slack channel about the work to be done with a runbook link

- [ ] Verify that any rollback plan can be execute by an engineer from every region

- [ ] Has a dry-run been performed before the call?

- [ ] Do we have a way to create logs from the actions performed.

### Runbook -Tasks

When possible, link the task name with a project, handbook page, which documents it.

| Task | Outcome | Duration |
|-------------|---------|----------|
|             |         |          |

#### Example

| Task | Outcome | Duration |
|-------------|---------|----------|
| Confirm the users provided state | Success | 10m |
| Modify user with MUser console method  | Success | 1h15m |

### Rollback plan

In the rollback plan, we provide a link for the steps to revert the actions performed. If we have a situation where the rollback requires only a simple explanation, it can be added to the runbook directly.

### Post-call checklist

- [ ] Inform on `#support_gitlab-com` or `#support_self-managed` and `#support_manager` slack channel the about the work completion, the current state, and if any follow up is necessary with documentation links.

### Complete RunBook Example

| Runbook name        |  Acme - Enforce 2FA on all groups |
|---------------------|---|
| Runbook description |  Acme Inc. requires us to enforce 2FA on all of their 2500 groups  |
| DRI                 |  `@john_doe` |
| Schedule at         |  `2020-10-10 - 23:30 PST` |
| Meeting URL         |   example.zoom.com/my/example.meeting|
| Gitlab Issue        |   `https://gitlab.com/gitlab-com/demo/example/example-project/-/issues/1` |

#### Gitlab Contacts

| Name | Role | Description |
|-------------|------|-------------|
| John Doe    |  Technical Execution  | Technical  execution during the change |
| Jane Smith  |  Communication & Technical assistance  | In charge of updates and to support the `technical execution` role |

#### Customer Contacts

| Name | Role | Description |
|-------------|------|-------------|
| Tom Blogs | Systems Engineer | Work verification and support |
| harry Page | IT Manager | Coordination from customer side |

#### Pre-call checklist

[x] - Inform on `#support_gitlab-com` or `#support_self-managed` and `#support_manager` slack channel about the work to be done with a runbook link

[x] - Verify that any rollback plan can be execute by an engineer from every region

[ ] - Has a dry-run been performed before the call?

    `Dry-run cannot be completed due to change requirements`

[x] - Do we have a way to create logs from the actions performed.

#### Runbook - Tasks

| Task | Outcome | Duration |
|-------------|---------|----------|
| Confirm the users provided state | | |
| Remove 2FA from user list  | | |
| Review users with errors   | | |
| Update issue with outcome    | | |

#### Rollback plan

The method used for this change takes an optional parameter `status` which is `disable` by default, to rollback we need to execute the same method adding a parameter `status: 'enable'.

#### Post-call checklist

[x] - Inform on `#support_gitlab-com` or `#support_self-managed` and `#support_manager` slack channel the about the work completion, the current state, and if any follow up is necessary with documentation links.
