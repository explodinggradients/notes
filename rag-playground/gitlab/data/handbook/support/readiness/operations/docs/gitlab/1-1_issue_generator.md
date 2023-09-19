---
title: 1-1 issue generator
description: Support Operations documentation page for the 1-1 issue generator
canonical_path: "/handbook/support/readiness/operations/docs/gitlab/1-1_issue_generator"
---

## What is the 1-1 issue generator

The 1-1 issue generator is a project created in house to assist in the creation
of GitLab issues for use in 1 on 1 meetings. This uses a customizable formatting
and various APIs to gather details and present it in a way that is useful to
both manager and report.

The source code for it is located
[here](https://gitlab.com/gitlab-com/support/toolbox/1-1-issue-generator).

## How does the 1-1 issue generator work

This all works utilizing ruby scripting and GitLab CI/CD. The CI/CD component
of this is straight forward, in that it has 4 stages and they run the ruby
scripts within the project.

### Test stage

This stage runs the `./bin/test` file within the repo. That file tests for the
following:

- Is the YAML file able to be parsed?
- Do comment YAML files contain the ticket_review boolean?
- Do comment YAML files contain the comments array?
- Are the template files readable by an ERB renderer?

If any of the above answers are no, then the test stage will fail, preventing
the CI/CD from running further. This is used to prevent merging bad files into
the repo.

#### Gather stage

This stage runs the `./bin/gather` file within the repo. That file runs the
`gather` function within the `Generator::Client` class.

The `Generator::Client.gather` function obtains various data points spanning
from:

- Zendesk Global
- Zendesk US Federal
- Pagerduty
- GitLab.com

It combines all this data into an artifact file.

#### Report stage

This stage runs the `./bin/daily_report` file within the repo. That file takes
the artifact made in the [Gather stage](#gather-stage) and commits it to the
[Daily reports repo](https://gitlab.com/gitlab-com/support/1-1s/daily-reports).

#### Create stage

**Note**: While previous stages ran for multiple people, some jobs in this stage
will only run for a single person at a time.

This stage will run one of three different jobs:

- weekly_report: This creates 1-1 issues for weekly use
- monthly_report: This creates an issue covering a month's worth of data
- quarterly_report: This creates an issue covering the current quarter's worth
  of data

All of the jobs that run will call to a file in the repo that will link to
various functions relating to the job itself. While there is some variance in
how the three run, overall they all gather data from the
[Daily reports repo](https://gitlab.com/gitlab-com/support/1-1s/daily-reports)
and then pass it into an ERB template file. This is then compiled into a
gitlab.com issue via the GitLab API.

## When does 1-1 issue generator run

By using GitLab CI/CD schedules, we have the following set to run at various
intervals:

| Name              | What it does                           | When it runs      |
|-------------------|----------------------------------------|-------------------|
| Gather metrics    | Runs the [Gather stage](#gather-stage) | Daily at 0100 UTC |
| Create 1-1 Issues | Runs the [Create stage](#create-stage) | Daily at 0300 UTC |

## Change management

As these are maintained via sync repositories, our standard change management
process applies to all 1-1 issue generator changes. See
[standard change management](/handbook/support/readiness/operations/docs/change_management#standard-change-management)
for more information.

#### Labels to use

For all issues and MRs involving 1-1 issue generator, the label
`Support-Ops-Category::GitLab Projects` should be used.

#### Change criticality

As this is an internal tool with no direct impact, all issues/MRs related to
1-1 issue generator will be classified as
[criticality 4](/handbook/support/readiness/operations/docs/change_criticalities#criticality-4)
