---
title: "GitLab Application Security Inventory"
description: "The AppSec Inventory is a private GitLab project to identify and track all projects, components, and dependencies that matter for AppSec"
---

## GitLab Application Security Inventory

Securing GitLab means building a security program at scale. The number of changes in the codebase is constantly increasing, along with the number of side projects.
Keeping track of all these moving parts can not rely only upon our current understanding and vision of the GitLab software architecture.
Automation is a key aspect of our work, and GitLab is no exception.

The AppSec Inventory is a private GitLab project to identify and track all projects, components, and dependencies important to us.
The project is available at [https://gitlab.com/gitlab-com/gl-security/engineering-and-research/inventory](https://gitlab.com/gitlab-com/gl-security/engineering-and-research/inventory)
to GitLab team members. The Inventory is built using this [CLI tool](https://gitlab.com/gitlab-com/gl-security/engineering-and-research/gib/).

Not all projects are important, and we certainly don't want to monitor projects that are POCs, demos, or tests.
That's why we need to categorize the projects created by GitLab team members, understand their nature, and make decisions at scale.

### Categories

To quickly identify the purpose and characteristics of a project, a strict categorization is necessary.
The following categories can be used to decorate the projects we want to monitor.

| Categories | Description |
| -------- | ----------- |
| `product` | Used as a component of GitLab at some point |
| `library` | A library, package source, component (not necessarily a `product` one) |
| `deploy` | Used to deploy GitLab.com |
| `website` | Deployed to a website (URL will be required) |
| `api/service` | |
| `green/yellow/orange/red_data` | [Data classification standard](https://about.gitlab.com/handbook/security/data-classification-standard.html) |
| `3rdparty` | Interaction with 3rd parties |
| `demo/test/poc` | |
| `temporary` | Temporary projects (should be removed at some point) |
| `internal` | Available for GitLab team members only |
| `external` | User facing |
| `use_pat` | Personal Access Token being used |
| `marked_for_deletion` | Project should be removed |
| `keep_private` | Should remain private indefinitely |
| `docs` | Used to generate documentation |
| `tooling` | Engineering tooling  |
| `container` | A Docker image is built |
| `fork` | Fork of another project (on gitlab.com or somewhere else) |

### Rules

Rules define actions to take, based on the project categories. These actions are performed by the GitLab Inventory Builder and are currently hard coded. We plan to make them dynamic in the future.

| Categories | Actions |
| -------- | ----------- |
|  All (even if no category is defined) | Download [Dependencies] |
|  `product`, `library` \| `use_pat` \| `website` \| `api/service` \| `green/yellow/red-data` \| `3rdparty` | Download [Vulnerability Reports], [Dependencies], [Protected branches], and [CI/CD configuration] |
|  `fork` | Download [Protected branches] |

### Policies

| Categories | Policies |
| -------- | ----------- |
| `red-data`, `product`, `library` | [SAST], [Dependency Scanning], and [Secret Detection] must be enabled |
| `red-data`, `product`, `library` | *Default branch* must be `protected` (Allowed to merge: `Maintainers`, Allowed to push: `No one`) |
| `use_pat`, `website`+`external` | [Dependency Scanning] and [Secret Detection] must be enabled |
| `website`+`external` + `yellow/orange/red_data` | [DAST] must be enabled. Overall SSL grade must be 'A' or 'A+' |
| `product` + `container` | [Container Scanning] must be enabled |
| `keep_private` | Project `visibility` must be `private` |
| `docs` | [Secret Detection] must be enabled |
| `marked_for_deletion` | Project will be deleted |
| `deprecated` | Project will be archived |
| all | Projects can't have [`internal`](https://docs.gitlab.com/ee/public_access/public_access.html#internal-projects-and-groups) visibility |
| all | *Default branch* must be `protected` |
| all | [`SECRET_DETECTION_HISTORIC_SCAN`](https://docs.gitlab.com/ee/user/application_security/secret_detection/#full-history-secret-detection) must not be set in the CI/CD configuration |

<!-- Identifiers are used for readability of the tables above -->

[CI/CD configuration]: https://docs.gitlab.com/ee/api/lint.html
[DAST]: https://docs.gitlab.com/ee/user/application_security/dast/
[Dependencies]: https://docs.gitlab.com/ee/api/dependencies.html
[Dependency Scanning]: https://docs.gitlab.com/ee/user/application_security/dependency_scanning/
[Secret Detection]: https://docs.gitlab.com/ee/user/application_security/secret_detection/
[SAST]: https://docs.gitlab.com/ee/user/application_security/sast/
[Container Scanning]: https://docs.gitlab.com/ee/user/application_security/container_scanning/
[Vulnerability Reports]: https://docs.gitlab.com/ee/api/project_vulnerabilities.html
[Protected branches]: https://docs.gitlab.com/ce/api/protected_branches.html

These policies are aligned with our [GitLab Projects Baseline Requirements](/handbook/security/gitlab_projects_baseline_requirements.html).

### How to categorize projects

The inventory relies on a folder tree structure, used as a database, in a `data/` folder.
Leaves are folders and can be groups or projects, and they're identified by specific files (`project.json` for projects, `group.json` for groups).
These files are created automatically when syncing the Inventory.

The tree structure reflects the organization of groups and projects in a GitLab instance, in our case: https://gitlab.com.
For example, the [GitLab project](https://gitlab.com/gitlab-org/gitlab/) will be located under [`data/gitlab-org/gitlab/`](https://gitlab.com/gitlab-com/gl-security/engineering-and-research/inventory/-/tree/main/data/gitlab-org/gitlab) in the Inventory.

Projects can be categorized by creating a `properties.yml` file in their folder. This file can contain a `categories` array, with the categories of the project.

For example, to add the `product` and `library` categories:

```yaml
categories:
  - product
  - library
```

Subgroups can be ignored (skipped during synchronization) by adding an `ignore` file into their folder.

Learn more with the [GitLab Inventory Builder Documentation](https://gitlab.com/gitlab-com/gl-security/engineering-and-research/gib/-/blob/main/README.md), and this [example inventory](https://gitlab.com/gitlab-com/gl-security/engineering-and-research/inventory-example).

### Websites

Along with the categorization of the projects, the Inventory is also used to link websites we deploy with their projects. The `properties.yml` file can contain a `urls` array to list all the URLs (starting with `https://`) of a project. These URLs are used to validate the SSL configuration of the servers, and insecure findings are reported.

For example, to add the GitLab website URL:

```yaml
urls:
  - https://gitlab.com
```

### Weekly triage process

A synchronization pipeline runs every week, on Monday mornings. If successful, it will [generate a Merge Request](https://gitlab.com/gitlab-com/gl-security/engineering-and-research/inventory/-/merge_requests) to review the changes.

The review aims to:

1. Categorize newly created projects: Add a `properties.yml` file in the project folder to specify its categories. Ask the project owner in doubt.
1. Ignore newly created groups we don't want to track: Add an `ignore` file if the group should be ignored. Delete its subgroups and projects in the review Merge Request.
1. Review projects and groups updates: Review `project.json` and `group.json` for changes, especially the visibility (public/private).

The Merge Request will report a test coverage, corresponding to the ratio of projects categorized. Ideally, these review Merge Requests keep the same coverage, which means the new projects are categorized before getting merged.

