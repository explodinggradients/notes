---
title: "GitLab Projects Baseline Requirements"
description: "The hb page outlines baseline configurations that should be setup for GitLab projects which impact the GitLab codebase."
---

## Purpose

The purpose of this page is to outline a minimum set of requirements that should be adhered to when configuring projects at GitLab that ultimately impact the code which makes up the GitLab product and/or which impact the build, release or deployment of GitLab. The end goal being that no changes that ultimately impact the GitLab codebase can be made without review. This page can also help users of GitLab by offering some possible configurations for securing projects they deem critical.

Given GitLab's [commitment to dogfooding](https://about.gitlab.com/handbook/engineering/development/principles/#dogfooding) and keeping in mind GitLab's [Efficiency Value]({{< ref "values#efficiency" >}}) it is important to understand that these baseline project configurations are not required on *all* projects, only those projects which impact the GitLab codebase (directly or indirectly) or are otherwise deemed critical for another communicated reason (note in these instances the rationale of the "why" behind the need for these baseline configurations should be able to be clearly communicated).

That said, it is encouraged for team members to keep these baseline configurations in mind when creating or working in projects as they are designed to improve the security and quality of contributions made in GitLab projects.

## Scope

The scope of the projects which should have these baseline configurations applied are any project which influences the GitLab codebase directly or indirectly and/or which impact the build, release or deployment of GitLab.

Examples of a project that fits this criteria:
- A project that builds a component of GitLab
- A project that builds a bot which helps manage the codebase for a component of GitLab
- A project used for updating a critical non-GitLab system's codebase (e.g. Salesforce)

Examples of a project that *do not* fit this criteria:
- A project that has no code
- A project that builds a bot which doesn't impact the GitLab codebase (e.g a script to convert a YAML file into a CSV)

Project usage may naturally shift over time and it's important to be re-evaluating project usage on an ongoing basis, projects may go in and out of either category so please keep that in mind as you work in projects each day. The hope is that even when a project does have these baseline configurations setup, efficiency isn't decreased as we have team members collaborating on work and avoid working in silos of knowledge that increase our risk of an individual becoming a single point of failure as well. These values also encourage our [Transparency Value]({{< ref "values#transparency" >}}) by getting multiple team members involved in changes.

### I'm not sure where my project fits

That's okay! And certainly not going to be uncommon. If you have questions, please raise them so we can address and try to fit into the appropriate category. We can iterate here on how we categorize projects so we ensure our commitment to Security and Quality, as well as Efficiency.

### My project doesn't fit seem to fit the criteria but I still need these configurations?

There also may be instances when a project doesn't strictly meet our general criteria for requiring baseline configurations but for some reason it is determined that the project should be configured using the baseline configurations. In these instances the rationale of the "why" behind the need for these baseline configurations should be able to be clearly communicated. If many similar rationales are being provided for projects that don't appear to meet the existing criteria, it is likely an indicator that the scope and criteria of projects should be adjusted.

## Protected Branch Baseline Configurations

As a general rule, we want to protect our branches in such a way that we [require everyone to submit MRs for that protected branch](https://docs.gitlab.com/ee/user/project/protected_branches.html#require-everyone-to-submit-merge-requests-for-a-protected-branch). This requirement to use an MR allows for an easier trail to follow of changes made and rationale behind them, and most importantly, it requires an MR to be used to make changes to the protected branch which works hand-in-hand with our configured MR Approval Rules. If accounts can push direct to the protected branch, that account does not have to use an MR and can make changes without another team member's involvement.

### Example 1 of Protected Branch Settings configured to Require an MR

![Example 1 of Protected Branch Settings configured to Require an MR](https://about.gitlab.com/images/protected_branch_settings_example.jpg "Example of Protected Branch Settings")

See [Note on usage of Code Owners]({{< ref "gitlab_projects_baseline_requirements#note-on-usage-of-code-owners" >}})

## MR Approval Rule Configurations

MRs should be reviewed following GitLab's [Code Review Guidelines](https://about.gitlab.com/handbook/engineering/workflow/code-review/). To ensure MRs are not merged with unreviewed commits, [MR Approval Rules](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/settings.html#approval-settings) should be enabled in one of the two below methods.

### Example 1 of MR Approval Rules configured WITHOUT Code Owners

![Example 1 of MR Approval Rules configured WITHOUT Code Owners](https://about.gitlab.com/images/MR_approvals_without_code_owners.jpg "Example 1 of MR Approval Rules configured WITHOUT Code Owners")

### Example 2 of MR Approval Rules configured WITH Code Owners

![Example 2 of MR Approval Rules configured WITH Code Owners](https://about.gitlab.com/images/MR_approvals_with_code_owners.png "Example 2 of MR Approval Rules configured WITH Code Owners")

See [Note on usage of Code Owners]({{< ref "gitlab_projects_baseline_requirements#note-on-usage-of-code-owners" >}})

## Note on usage of Code Owners

Note that not all projects will have Code Owners enabled as it may not be necessary in all instances.

If a project does use Code Owners, the Proteced Branch settings should be configured to have "Code owner approval" toggled **ON** and an appropriately configured Code Owners file should be created. The GitLab Docs defines how Code Owners work and [how to set up Code Owners](https://docs.gitlab.com/ee/user/project/codeowners/#set-up-code-owners).

The [MR Approval Rules should also be configured to utilize Code Owners](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/rules.html#code-owners-as-eligible-approvers) and require at least one Code Owner to approve MRs with affected file types

Please review thoroughly and ask questions in the `#sec-assurance` slack channel, or tag in the MR you're setting up Code Owners with if there is any confusion!

## Ongoing Monitoring

Please note that projects that meet the criteria for requiring these baseline configurations may be selected at any point for testing of configurations by the [GitLab Security Compliance team]({{< ref "./security-assurance/security-compliance" >}}) as part of our continuous control monitoring program to make sure we're adhering to the guidance outlined on this page. Please see the [GCF Security Control Lifecycle]({{< ref "security-control-lifecycle" >}}) page for an overview of the program.

## References

- [GitLab Repositories](https://about.gitlab.com/handbook/engineering/gitlab-repositories/#creating-a-new-project) (for guidance on creating a new project)
- [Change Management Policy]({{< ref "change-management-policy" >}})
- [GCF Security Control Lifecycle]({{< ref "security-control-lifecycle" >}})
