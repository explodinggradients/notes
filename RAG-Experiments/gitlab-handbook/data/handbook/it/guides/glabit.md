---
title: "GLabIT Guide"
description: "GLabIT is a custom IT automation platform to improve our operational efficiency for back office background jobs, change management, provisioning and deprovisioning, and reporting tasks."
---

## Overview

GLabIT (pronounced like "rabbit") is a custom IT automation platform to improve our operational efficiency for back office background jobs, change management, provisioning and deprovisioning, and reporting tasks.

This handbook page provides an overview, however you will find all of the technical details on the [GLabIT Documentation Site](https://gitlab-it.gitlab.io/glabit-docs).

### Background Context

In the past, we used the IT CLI Scripts that were installed on each team member's computer and had API tokens to different systems. GLabIT moves from a client-only model to a [client-server API middleware model](https://gitlab-it.gitlab.io/glabit-docs/cli/overview#introduction) for running scripts, with the added benefit of scheduled background jobs.

As we mature our operations, GLabIT will be a centralized platform to host our new [Level 3 and Level 4 automations](https://about.gitlab.com/handbook/business-technology/it/engineering/automation/) that are more complex than a no-code integration.

## Services

GLabIT is a platform that hosts many automation related (micro-)services and scripts. You can learn more about each service on the respective documentation or handbook page.

| Team     | Service                                                                                  | Roadmap Status    |
| -------- | ---------------------------------------------------------------------------------------- | ----------------- |
| `it-eng` | [ARCHIE Directory](https://gitlab-it.gitlab.io/glabit-docs/archie/overview)              | FY23-Q2 (WIP)     |
| `it-eng` | [ARCHIE Group Policies](https://gitlab-it.gitlab.io/glabit-docs/archie/overview)         | FY23-Q2 (WIP)     |
| `it-eng` | [ARCHIE Group Provisioner](https://gitlab-it.gitlab.io/glabit-docs/archie/overview)      | FY23-Q2 (WIP)     |
| `it-eng` | [HackyStack](https://about.gitlab.com/handbook/infrastructure-standards/realms/sandbox/) | FY23-Q3 (Planned) |
| `it-eng` | [IT Ops CLI Scripts](https://gitlab.com/gitlab-com/it/dev/it-ops-laravel-cli-scripts)    | FY23-Q3 (Planned) |
| `it-eng` | [Demo Systems](https://about.gitlab.com/handbook/customer-success/demo-systems/)         | FY23-Q3 (Planned) |
| `it-eng` | [Training Systems](https://about.gitlab.com/handbook/customer-success/demo-systems/)     | FY23-Q3 (Planned) |

This is an early incubation project. We are in the process of onboarding team members from IT Security, People Ops, Security Automation, Security Compliance, and Vulnerability Management to be able to contribute and/or migrate their scripts to this consolidated platform. Feel free to add projects to this list.

## Get Started

This is an early incubation project. Contact Jeff Martin for details on getting started with GLabIT. This will be updated as we reach alpha and beta stability (see the [roadmap](#roadmap)).

## Reference Links

- [GLabIT Development API](https://glabit-dev.gitlab.systems)
- GLabIT Production API (Coming Soon)
- [GLabIT CLI Package](https://packagist.org/packages/gitlab-it/glabit-cli)
- [Slack Channel](https://slack.com/app_redirect?channel=C04RYCM137A)
- [Issue Tracker](https://gitlab.com/gitlab-com/it/dev/issue-tracker)
  - [Epics Roadmap](https://gitlab.com/groups/gitlab-com/it/dev/-/roadmap?state=opened&sort=start_date_asc&layout=QUARTERS&timeframe_range_type=THREE_YEARS&progress=WEIGHT&show_progress=true&show_milestones=false&milestones_type=ALL&show_labels=false)
- [GLabIT Documentation](https://gitlab-it.gitlab.io/glabit-docs/)
  - [ARCHIE Documentation](https://gitlab-it.gitlab.io/glabit-docs/archie/overview)
  - [CLI Documentation](https://gitlab-it.gitlab.io/glabit-docs/cli/overview)
  - [Reports Documentation](https://gitlab-it.gitlab.io/glabit-docs/reports/overview)
  - [API Documentation](https://gitlab-it.gitlab.io/glabit-docs/api/overview)
  - [Architecture Documentation](https://gitlab-it.gitlab.io/glabit-docs/architecture/overview)
  - [Changelog Documentation](https://gitlab-it.gitlab.io/glabit-docs/changelog/overview)
  - [Contributor Documentation](https://gitlab-it.gitlab.io/glabit-docs/contributor/overview)
- Repositories
  - glabit-docs - [Public Repo](https://gitlab.com/gitlab-it/glabit-docs) - [Read Only Mirror](https://gitlab.com/gitlab-com/it/dev/glabit-docs)
  - glabit-api - [Private Repo](https://gitlab.com/gitlab-it/glabit-api) - [Read Only Mirror](https://gitlab.com/gitlab-com/it/dev/glabit-api)
  - glabit-cli - [Public Repo](https://gitlab.com/gitlab-it/glabit-cli) - [Read Only Mirror](https://gitlab.com/gitlab-com/it/dev/glabit-cli)

## Roadmap

> These dates are subject to change. Please collaborate with Jeff Martin before using these dates as committments for other dependencies or projects.

| Date          | Target                                                          |
| ------------- | --------------------------------------------------------------- |
| 2023-03-17    | `code` [glabit-cli v0.1 Release](https://gitlab.com/gitlab-com/it/dev/glabit-cli/-/blob/main/changelog/0.1-alpha.md)                                  |
| 2023-03-24    | `code` [glabit-cli v0.2 Release](https://gitlab.com/gitlab-com/it/dev/glabit-cli/-/blob/main/changelog/0.2-alpha.md)                                  |
| 2023-04-14    | `infra` **glabit-dev.gitlab.systems Live** (Fake PII Data)      |
| 2023-04-14    | `code` glabit-api v0.1 Release                                  |
| 2023-04-24    | `code` glabit-api v0.2 Release                                  |
| 2023-04-28    | `code` glabit-api + cli v0.3 Release                            |
| 2023-05-05    | `release` **v0.4 Alpha Release (glabit-stg.gitlab.systems)** (Fake PII Data)   |
| 2023-05-05    | `docs` glabit-docs Updated with Alpha Release                   |
| 2023-05-05    | `docs` Handbook Page Updated                                    |
| 2023-05-09    | `collab` AppSec Review Kickoff                                  |
| 2023-05-09    | `collab` Compliance Review Kickoff                              |
| 2023-05-09    | `collab` Contributor Code Orientation                           |
| 2023-05-16    | `collab` Start Weekly Office Hours / AMA (12 Weeks)             |
| 2023-05-19    | `code` v0.5 Release                                             |
| 2023-06-02    | `code` v0.6 Release                                             |
| Early June    | `collab` **Release Readiness Security Review Complete**         |
| Early June    | `infra` **glabit.gitlab.systems Live** (Prod, Real PII Data)          |
| Early June    | `code` **v0.7 Beta Release (glabit.gitlab.systems)**            |
| Early June    | `migrate` **Provisioning Testing with Sales Groups** (EBA team) |
| June          | `migrate` **Start Migrating Baseline Entitlements Groups**      |
| May-June      | `docs` Tutorial Videos Live (Rolling Releases)                  |
| Mid June      | `code` v0.8 Release                                             |
| Late June     | `code` v0.9 Release                                             |
| July          | `migrate` **Finish migrating Google Groups to ARCHIE**          |
| Mid July      | `code` v0.10 Release                                            |
| Mid-Late July | `code` v0.11 Release                                            |
| TBD           | `migrate` Finish migrating Slack Groups to ARCHIE               |
| TBD           | `migrate` Finish migrating Slack Channels to ARCHIE             |
| TBD           | `migrate` Finish migrating GitLab.com Groups                    |
| TBD           | `code` v0.x Releases                                            |
| TBD           | `code` v1.0 Release                                             |
