---
title: DEWR
description: Support Operations documentation page for dotcom escalation weekly reports
canonical_path: "/handbook/support/readiness/operations/docs/gitlab/dewr"
---

## What is the DEWR

DEWR (Dotcom Escalation Weekly Report) is a project within gitlab.com that
generates weekly reports concerning dotcom console escalations.

The source code for it is located
[here](https://gitlab.com/gitlab-com/support/toolbox/dewr).

## How does the DEWR work

ADWR works by utilizing GitLab CI/CD and ruby scripts. It runs in two stages:

- gather
- create

### gather stage

This stage runs the `./bin/gather` script, which includes the DEWR lib files and
calls the function `DEWR::Gather.run!`. This function makes an API request to
gitlab.com to grab all the issues within the
[Support Internal Requests project](https://gitlab.com/gitlab-com/support/internal-requests)
that are in either recent or in an open state. It then compiles these issues
into a JSON file, which is stored as an artifact.

### create stage

This stage runs the `./bin/create` script, which includes the DEWR lib files and
calls the function `DEWR::Create.run!`. This function uses the artifact made in
the [gather stage](#gather-stage) to generate a report (which is an
[DEWR issue](https://gitlab.com/gitlab-com/support/internal-requests/-/issues?scope=all&state=opened&label_name[]=DEWR)).

The body of the created issues comes from parsing the issues from the artifact
made in the [gather stage](#gather-stage).

## When does the DEWR run

Currently, DEWR runs every Saturday at 0000 UTC.

## Change management

As these are maintained via sync repositories, our standard change management
process applies to all DEWR changes. See
[standard change management](/handbook/support/readiness/operations/docs/change_management#standard-change-management)
for more information.

#### Labels to use

For all issues and MRs involving DEWR, the label
`Support-Ops-Category::GitLab Projects` should be used.

#### Change criticality

As this is an internal tool with no direct impact, all issues/MRs related to
DEWR will be classified as
[criticality 4](/handbook/support/readiness/operations/docs/change_criticalities#criticality-4)
