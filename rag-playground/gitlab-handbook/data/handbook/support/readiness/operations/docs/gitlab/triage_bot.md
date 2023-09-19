---
title: Triage bot
description: Support Operations documentation page for the triage bot
canonical_path: "/handbook/support/readiness/operations/docs/gitlab/triage_bot"
---

## What is triage bot

Triage bot is the term we use for automation that utilizes the
[gitlab-triage gem](https://rubygems.org/gems/gitlab-triage) to perform various
tasks automatically.

## Triage bot policies

Triage bot utilizes policies to determine what actions to perform on what items.
Currently, the policies contain rules that can be used on epics, issues, and
merge requests.

Each policy contains rules for the resource set. These rules are contained
within an array that detail what to run on and what to actually do. Each of
these rules usually contains:

- `name` - the name for the rule
- `conditions` - the conditions the rule applies on
- `limits` - the limit to how many items can be grabbed at any time
- `actions` - the tasks to be done on items the rule applies to

### name

This is a simple string that gives the rule a name.

### conditions

This is used to dictate what items the rule will apply to. This can be a simple
set of conditions or a complex one, depending on your needs. There are many
types of conditions you can use. For more information, see the
[GitLab Triage repo](https://gitlab.com/gitlab-org/gitlab-triage).

### limits

This details any limits on the items found. Generally speaking, you will specify
what limit to use and the number of items to applies this to. The limits you can
use are:

- `most_recent` - Limits by the most recent items, using the `created_at` value
  sorted in descending order.
- `oldest` - Limits by the oldest items, using the `created_at` value sorted in
  ascending order.

As an example, to only apply on the 20 most recently created items:

```yaml
limits:
  most_recent: 20
```

As another example, to only apply on the 40 oldest items:

```yaml
limits:
  oldest: 40
```

### actions

This is where you specify what to do on the items found. There are many types of
actions you can use. For more information, see the
[GitLab Triage repo](https://gitlab.com/gitlab-org/gitlab-triage).

## How Support Ops uses triage bot

At 1200  UTC everyday, we run triage-bot via the
[Support Ops Project repo](https://gitlab.com/gitlab-com/support/support-ops).
This utilize the
[Support Ops triage policies](https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/blob/master/.triage-policies.yml)
to perform various triage actions on issues and merge requests we work out of.

Generally speaking, we have rules for:

- Issues
  - Find issues missing a category label
  - Find issues missing a priority label
  - Find issues missing a progress label
  - Find issues missing a milestone
  - Find issues that missed their milestone
  - Find closed issues with incorrect progress label
- Merge requests
  - Find MRs missing a category label
  - Find MRs missing a priority label
  - Find MRs missing a progress label
  - Find MRs missing a milestone
  - Find MRs that missed their milestone
  - Find closed MRs with incorrect progress label
  - Find merged MRs with incorrect progress label

## Useful links

- [gitlab-triage gem](https://rubygems.org/gems/gitlab-triage)
- [GitLab Triage repo](https://gitlab.com/gitlab-org/gitlab-triage)
- [Support Ops triage policies](https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/blob/master/.triage-policies.yml)
