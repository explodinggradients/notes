---
title: GitLab project setup
description: Support Operations policies page for GitLab project setup
canonical_path: "/handbook/support/readiness/operations/docs/policies/project_setup"
---

## What are GitLab project settings

As per
[GitLab](https://docs.gitlab.com/ee/user/project/settings/):

> The Settings page in GitLab provides a centralized home for your project
> configuration options.

It is through these we often manage how various components of a project work.

## Editing GitLab project settings

To edit GitLab project settings, you would go to the project in question, hover
over the Settings option on the right-hand side, and then click on the category
you wish to edit. From there, locate the setting and modify it. Some settings
save the changes once you make them in the UI, some will require clicking a
button to save the changes.

## Settings Support Operations uses

These are the settings we aim to use by default for all Support Operations
projects.

#### General

- Visibility, project features, permissions
  - Project visibility: Private
- Merge requests
  - Merge method: Merge commit
  - Merge options
    - Show link to create or view a merge request when pushing from the command
      line
    - Enable "Delete source branch" option by default
  - Squash commits when merging
    - Require
  - Merge checks
    - Pipelines must succeed
      - Note: this is only if project utilzies CI/CD
  - Merge suggestions
    - Default description template for merge requests
      - See [Default MR description](#default-mr-description)
- Merge request approvals
  - Approval rules
    - Name: Any eligible user
      - Approvers:
      - Target branch: All branches
      - Approvals required: 0
    - Name: Support Ops
      - Approvers: Support Ops team members
      - Target branch: master
      - Approvals required: 1
  - Approval settings
    - Prevent editing approval rules in merge requests
    - Remove all approvals when commits are added to the source branch
- Default description template for issues
  - See [Default Issue description](#default-issue-description)

#### Repository

- Default branch
  - Default branch: master
  - Auto-close references issues on default branch
- Protected branches
  - Branch: master
    - Allowed to merge: jcolyer nabeel.bilgrami avilla4 dtragjasi secole
    - Allowed to push: jcolyer, No one
  - Allowed to force push: false
  - Code owner approval: true

#### CI/CD

- General pipelines
  - Public pipelines
  - Auto-cancel redundant pipelines
  - Shop outdated deployment jobs
  - Git strategy: get fetch
  - Git shallow clone: 50
  - Timeout: 1h
- Artifacts
  - Keep artifacts from most recent successful jobs
- Variables
  - Whatever is needed for the project's CI/CD

#### Pages

This will vary depending on if the project is using GitLab Pages or not.

## Default MR description

There could be some variance, but normally the default MR description will look
like this:

> Enter your description here
>
> <!-- DO NOT EDIT BELOW THIS LINE -->
>
> The approvers for this Merge request will be @gitlab-com/support/support-ops
>
> /label ~"SupportOps::To Do" ~"Support-Ops-Priority::Normal"
> ~"Support-Ops-Category::CATEGORY" ~"Zendesk::INSTANCE"
>
> /assign ASSIGNEES
>
> /draft

Where:

- `CATEGORY` is the category label to use
- `INSTANCE` is the Zendesk instance this applies to
  - Note: this is not needed is the project doesn't touch Zendesk instances
- `ASSIGNEES` is the assignees of the MR (see
  [division of responsibilities](../index.html#division-of-responsibilities))

## Default Issue description

> \## PROJECT Issue
>
> \*\*Manager Approval** (please mention the manager who approved this request):
>
> \*\*Priority** (please include, if possible, the priority: Critical, Important,
> Normal, Low):
>
> - [ ] Critical
>
> - [ ] Important
>
> - [ ] Normal
>
> - [ ] Low
>
>
> \*\*SLA** (please include, if possible, the expected delivery timeframe):
>
>
> \*\*Requester** (if the person creating this issue isn't the requester, please
> mention the requester below):
>
> \*\*Link to Support-Team-Meta Discussion Issues** (this is required):
>
> \## Description:
>
>
>
> <!-- DO NOT EDIT BELOW THIS LINE -->
>
> DRI from Support Ops for PROJECT based Issues are MAIN (Main) and BACKUP
> (Backup)
>
> /label ~"SupportOps::To Do" ~"Support-Ops-Priority::Normal"
> ~"Support-Ops-Category::CATEGORY" ~"Zendesk::INSTANCE"
>
> /assign ASSIGNEES

Where:

- `PROJECT` is the project name
- `CATEGORY` is the category label to use
- `INSTANCE` is the Zendesk instance this applies to
  - Note: this is not needed is the project doesn't touch Zendesk instances
- `MAIN` is the primary responsible person (see
  [division of responsibilities](../index.html#division-of-responsibilities))
- `BACKUP` is the secondary responsible person (see
  [division of responsibilities](../index.html#division-of-responsibilities))
- `ASSIGNEES` is the assignees of the MR (see
  [division of responsibilities](../index.html#division-of-responsibilities))
