---
title: "Content Websites"
---

## Overview

This area has traditionally been referred to as *"the handbook"*, but over time has grown in scope to include multiple sites, projects, repos, and types of content.

Therefore, we are using the term "content websites" here to avoid ambiguity and properly frame discussions around this scope of responsibility.

See our [direction page](/handbook/content-websites/direction/) for detailed plans.

## Team Structure

The maintainer of this page (as indicated in the sidebar) is considered the [DRI](https://about.gitlab.com/handbook/people-group/directly-responsible-individuals/) for GitLab's "content websites". At present this team falls under the [Chief of Staff Team to the CEO](/job-families/chief-executive-officer/strategy-and-operations/) and the job family for engineers working on these projects is [defined as a specialty](/job-families/engineering/development/fullstack/#specialties).

This page further documents the scope and responsibilities of the DRI and their engineering reports.

## What are the content websites?

1. The public [`about.gitlab.com`](/) website:
    1. While often referred to as "the handbook", this website also serves a wide variety of other content including the [handbook](https://about.gitlab.com/handbook/), the [blog](https://about.gitlab.com/blog/), [releases](https://about.gitlab.com/releases/), category direction pages, many marketing pages, and other uncategorized documentation for various areas of GitLab.
    1. `about.gitlab.com` is primarily backed by the [`gitlab-com/www-gitlab-com`](https://gitlab.com/gitlab-com/www-gitlab-com) project and repo.
    1. Some of the content for `about.gitlab.com` is also backed by the [`gitlab-com/marketing/digital-experience/buyer-experience`](https://gitlab.com/gitlab-com/marketing/digital-experience/buyer-experience) project and repo, such as [small-business](https://about.gitlab.com/small-business) and [enterprise](https://about.gitlab.com/enterprise). The plan is to migrate more content from the `gitlab-com/www-gitlab-com` project to the `gitlab-com/marketing/digital-experience/buyer-experience` project.
1. The ["Internal Handbook" at `internal-handbook.gitlab.io`](https://internal-handbook.gitlab.io/):
    1. This website contains content that falls into the [not public](https://about.gitlab.com/handbook/communication/confidentiality-levels/#not-public) category. More details are available in [the Internal Handbook usage page](https://about.gitlab.com/handbook/handbook-usage#the-internal-handbook)
    1. The Internal Handbook is backed by the [`internal-handbook/internal-handbook.gitlab.io`](https://gitlab.com/internal-handbook/internal-handbook.gitlab.io) project and repo.

### What MAY be content websites?

These sites require further investigation, evaluation of current ownership, and a clearer definition of responsibilities:

- The compensation calculator at [`comp-calculator.gitlab.net`](https://comp-calculator.gitlab.net/)
- Project SuperSonics at [`gitlab-com.gitlab.io/licensing/`](https://gitlab-com.gitlab.io/licensing/)
- People Operations aka [POPS internal handbook](https://about.gitlab.com/handbook/people-group/engineering/pops-internal-handbook/)

### What are NOT content websites?

- The [`gitlab.com`](https://gitlab.com) SaaS site.
- The [`docs.gitlab.com`](https://docs.gitlab.com) product documentation site.
- Any other GitLab-managed or GitLab-owned website other than what is described above

## Content Websites DRI

1. Responsible for all aspects of these content websites, including:
    1. All business critical content for the content sites.
    1. All shared and supporting aspects of the content sites, including infrastructure, code, architecture, projects, security, CI/CD, builds, deployments, upgrades, performance, scalability, metrics, monitoring, etc.
    1. Triaging all issues and support requests, and delegating them to other responsible groups as appropriate.
    1. Providing on-call support for high-priority incidents or outages, and [escalating to infrastructure, reliability engineering, or other groups](https://about.gitlab.com/handbook/about/on-call#when-to-hand-over-to-reliability-engineering) as appropriate.
    1. Project management, [planning](https://gitlab.com/groups/gitlab-com/-/epics/423), and reporting for the above.
1. The [Digital Experience](https://about.gitlab.com/handbook/marketing/digital-experience/) team under [Michael Preuss](https://gitlab.com/mpreuss22) also has responsibility for the marketing-related areas of the site. These areas include the [`gitlab-com/marketing/digital-experience/buyer-experience`](https://gitlab.com/gitlab-com/marketing/digital-experience/buyer-experience) project and repo, as well as other content. The exact areas are still not fully defined, and this should also be clarified as part of [the definition of DRIs.](https://gitlab.com/gitlab-com/Product/-/issues/3273)

## Support process for content websites

There is currently information describing differing support policies for the content websites in various places, and some of this info may be inconsistent or outdated. For example, the ["Handbook On-Call"](https://about.gitlab.com/handbook/about/on-call) page, or the [Handbook Support](https://about.gitlab.com/handbook/about/support#where-do-i-report-handbook-issues-and-request-help) page.

All of this information should be cleaned up and consolidated when a final DRI is assigned. In the meantime, this is the process to obtain support:

1. Simple git or technical questions with MRs conflicts, markdown formatting errors, linting errors, pipeline failures, etc. can be asked in the [`#mr-buddies`](https://gitlab.slack.com/archives/CLM8K5LF4) slack channel.
1. High-priority questions regarding broken master, outages, security concerns, etc. can be asked in the [`#handbook-escalation`](https://gitlab.slack.com/archives/CVDP3HG5V) channel. See the existing ["Handbook On-Call - When to escalate an issue"](https://about.gitlab.com/handbook/about/on-call#when-to-escalate-an-issue) section for what types of issues are appropriate to be asked in this channel.
    1. If there is not an existing issue, you may be asked to create one in the [www-gitlab-com project](https://gitlab.com/gitlab-com/www-gitlab-com/-/issues) for tracking and prioritization purposes.
    1. Please use the `Content Websites Support (about.gitlab.com or internal-handbook.gitlab.io)` issue template.
    1. Make sure to included the `~content-websites-support` label.
    1. Link to the new issue in `#handbook-escalation` for triage.
1. For other topics not falling under either of the two above categories, for example, a feature request, a general question about content, etc.:
    1. You can start by asking a question or discussing it in the [`#handbook`](https://gitlab.slack.com/archives/C81PT2ALD) channel for the public `about.gitlab.com` site, or in the [`#internal-handbook`](https://gitlab.slack.com/archives/C02GABPC4UV) for the Internal Handbook.
    1. If you determine action is needed (and you can't fix it yourself with an MR), open a new issue in the [www-gitlab-com project](https://gitlab.com/gitlab-com/www-gitlab-com/-/issues). If this is related to the internal handbook, you can make the issue confidential as necessary.
    1. Apply the `~content-websites-support` label.
    1. Link to the issue in `#handbook` or `#internal-handbook` for triage.
