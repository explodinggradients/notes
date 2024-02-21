---

title: "IT Engineering - Development"
description: "This handbook page provides information about software development in the IT Engineering sub-department."
---

## Overview

The IT Engineering Development team develops custom software applications, automation, APIs and integrations that support internal IT automation for business efficiency and processes managed by the IT department.

Many of our projects focus on providing self service access request provisioning to our tech stack applications and supporting IT Infrastructure services, including the [Demo Systems](https://about.gitlab.com/handbook/customer-success/demo-systems) and [Sandbox Cloud](/handbook/infrastructure-standards/realms/sandbox).

## Direction

See our [IT Engineering Development Direction](/handbook/it/engineering/dev/direction) handbook page to learn more.

## Team

| Name                                                                        | Role                              |
|-----------------------------------------------------------------------------|-----------------------------------|
| [Peter Kaldis](https://about.gitlab.com/company/team/#pkaldis)              | Senior Manager, IT Engineering    |
| [Jeff Martin](https://about.gitlab.com/company/team/#jeffersonmartin)       | Senior IT Systems Engineer        |
| [Dillon Wheeler](https://about.gitlab.com/company/team/#dillonwheeler)      | Senior IT Systems Engineer        |

## Repositories

We strongly believe in open source software and publish many of our repositories as open source. Some projects that are built as internal tools are not open sourced due to perceived security hardening risks.

[Source Code Repositories](https://gitlab.com/gitlab-it)

### Internal Projects

- [Demo Systems - Demo Cloud](https://gitlab.com/gitlab-com/business-technology/engineering/tools/gitlabdemo-cloud-app)
- [Demo Systems - Training Cloud](https://gitlab.com/gitlab-com/business-technology/engineering/tools/gitlabdemo-com-app)
- [IT Ops CLI Scripts](https://gitlab.com/gitlab-com/business-technology/engineering/tools/it-ops-laravel-cli-scripts)

### Open Source Projects

- [HackyStack](https://gitlab.com/gitlab-com/business-technology/engineering/tools/hackystack)
- [SDK - GitLab](https://gitlab.com/gitlab-it/gitlab-sdk)
- [SDK - Google Auth](https://gitlab.com/gitlab-it/google-auth-sdk)
- [SDK - Google Cloud](https://gitlab.com/gitlab-it/google-cloud-sdk)
- [SDK - Google Workspace](https://gitlab.com/gitlab-it/google-workspace-sdk)
- [SDK - Okta](https://gitlab.com/gitlab-it/okta-sdk)
- [Terraform Modules](https://gitlab.com/gitlab-com/sandbox-cloud/terraform-modules)

## History

The IT Engineering Development team was formed in April 2021.

From late 2019 to mid 2021, [Jeff Martin](https://gitlab.com/jeffersonmartin) was a Senior Demo Systems Engineer in the Customer Success department and was focused on automating ephemeral infrastructure access requests and provisioning for demo, experiment, sandbox, and training use cases by creating small [Laravel](https://laravel.com/docs) applications for the v1 iteration of each standalone point solution.

| Project Name (Handbook Page)                                                                                               | URL                         | Purpose                                                                                                                                                                                                                            | Current Investment                  | Future State                                    |
| -------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ----------------------------------------------- |
| [Demo Systems - Demo Cloud](https://about.gitlab.com/handbook/customer-success/demo-systems/)                              | <https://gitlabdemo.cloud>    | Provisioning user accounts on several always-on Omnibus instances used for demos and internal experiments.                                                                                                                         | None                                | Replace with Archie                             |
| [Demo Systems - Training Cloud](https://about.gitlab.com/handbook/customer-success/demo-systems/#invitation-code-creation) | <https://gitlabdemo.com>      | Customer, marketing prospect, partner, and internal students redeem an invitation code to generate temporary credentials for performing training hands-on labs in different always-on Omnibus instances used for training classes. | Limited Maintenance                 | Rewrite for GitLab.com and Instruqt Integration |
| [HackyStack / Sandbox Cloud](https://about.gitlab.com/handbook/infrastructure-standards/realms/sandbox/)                   | <https://gitlabsandbox.cloud> | Provisioning AWS accounts, GCP projects, IAM users and roles, and automated Terraform scaffolding for sandbox experiments.                                                                                                         | 24x5 Support, Next-Gen Architecture | Discovery in Progress                           |

[Dillon Wheeler](https://gitlab.com/dillonwheeler) joined GitLab as an IT Systems Engineer in April 2021, and Jeff transferred over to IT in June 2021 and the Demo Systems and Sandbox Cloud projects became an IT Engineering managed service.

In late 2021 and early 2022, we started creating [GitLab Access Manager (GLAM)](https://docs.google.com/presentation/d/1j54otOxYwng33WA2UKbRaGoyE5bw9cAv3Jm02l4XFMM/edit#slide=id.g123a13deda8_0_405)(internal), however we found the scope was bigger than what we needed and the project was cancelled in favor of a vendor solution or smaller iteration.

As part of GitLab Access Manager development, we discovered the need for standardized vendor API response parsing. We created several SDKs for the vendors that IT works with day-to-day to allow us to uniformly interact with each vendor. These SDKs have been invaluable across multiple code repositories and have been contributed to the PHP open source community on [Packagist](https://packagist.org/packages/gitlab-it/).

| Project Name                                                              | Current Investment | Future State |
| ------------------------------------------------------------------------- | ------------------ | ------------ |
| [gitlab-sdk](https://gitlab.com/gitlab-it/gitlab-sdk)                     | v3 Dev             | Maintained   |
| [google-auth-sdk](https://gitlab.com/gitlab-it/google-auth-sdk)           | Maintained         | Maintained   |
| [google-cloud-sdk](https://gitlab.com/gitlab-it/google-cloud-sdk)         | v3 Dev             | v3.x Dev     |
| [google-workspace-sdk](https://gitlab.com/gitlab-it/google-workspace-sdk) | v3 Dev             | v3.x Dev     |
| [okta-sdk](https://gitlab.com/gitlab-it/okta-sdk)                         | v3 Dev             | Maintained   |
| [slack-sdk](https://gitlab.com/gitlab-it/slack-sdk)                       | v1 Dev             | v1.x Dev     |

As part of the GitLab Access Manager retrospective, we came up with our Automation Philosophy which allows us to focus on keeping it super simple and catering to the skillsets and time available on our team.

In 2021 and 2022, we were able to efficiently iterate by adding scripts to the [IT Ops Laravel CLI Scripts](https://gitlab.com/gitlab-com/business-technology/engineering/tools/it-ops-laravel-cli-scripts) repository which was originally a developer scratch pad and became a boring solution that was adopted for IT production purposes. We now run several scripts in scheduled CI/CD pipelines and most IT team members use the CLI scripts in their local Terminal. This has had valuable benefits during incident response with our ability to implement new automation functionality in 15-60 minutes without any headaches.

In 2023 (FY24), we are focused on moving from our v1 viable architecture to a v2 mature ecosystem as we reduce our IT process tech debt and move towards next-generation automation. We're continuing to consolidate our isolated scripts and manual processes, and refactoring our legacy applications (ex. Demo Systems and HackyStack) using the backend API, CLI, CI/CD, and Slackbot approaches.

As we learn more through the current iterations, we'll evaluate what approach makes sense for future iterations. It is unclear yet whether we will continue focusing on isolated point solutions, consolidate into a unified backend API, or take a hybrid approach with modular microservices.

See the [IT Engineering Development Direction](/handbook/it/engineering/dev/direction) handbook page to learn more.
