---
title: "Application Security"
description: "The application security team's mission is to support the business and ensure that all GitLab products securely manage customer data."
---
<!-- markdownlint-disable MD052 -->

## Application Security Mission

As part of the Security Engineering sub-department, the application security team's mission is to support the business and ensure that all GitLab products securely manage customer data. We do this by working closely with both engineering and product teams.

## Contacting us

Team members can reach the AppSec team by:

- Asking in `#sec-appsec` or mentioning `@appsec-team` on Slack
- Mentioning `@gitlab-com/gl-security/appsec` on GitLab
- Finding your Stable Counterpart on the [Product sections, stages, groups, and categories](https://about.gitlab.com/handbook/product/categories/) page
- Submit an issue in the [AppSec Team repository](https://gitlab.com/gitlab-com/gl-security/appsec/appsec-team/-/issues)
- For cross team collaboration improvement opportunities, use [this template for collaboration improvement opportunities](https://gitlab.com/gitlab-com/gl-security/appsec/appsec-team/-/issues/new?issuable_template=cross-team-collaboration-improvement)

## Application Security Roadmap

Please see the [Security Engineering Program Strategy document][9].

## Roles & Responsibilities

Please see the [Application Security Job Family page][6].

## Useful resources for AppSec engineers

- [The AppSec private group that contains other private subgroups and projects](https://gitlab.com/gitlab-com/gl-security/appsec)
- [Bug bounty council search](https://gitlab.com/gitlab-com/gl-security/engineering/-/issues?label_name%5B%5D=Bug+Bounty+Council)
- [Upcoming security release](https://gitlab.com/gitlab-org/gitlab/-/issues?sort=created_date&state=opened&label_name%5B%5D=upcoming+security+release)
- [GitLab Project Security dashboard](https://gitlab.com/gitlab-org/gitlab/-/security/dashboard/?project_id=278964&scope=dismissed&page=1&days=90)
- [Security issue board that tracks ongoing issues (hackerone and others)](https://gitlab.com/groups/gitlab-org/-/boards/1216545?label_name[]=security)
- [The latest releases](https://gitlab.com/gitlab-org/gitlab/-/tags)
- [Overview of a project member permissions](https://gitlab.com/help/user/permissions)
- [The DevOps stages and their different groups](https://about.gitlab.com/handbook/product/categories/). This page contains information on the development teams, their areas of focus, and their team members as well as the AppSec stable counterparts. It is used to assign issues to the stable counterparts.
- [The product features listed by groups that own them](https://about.gitlab.com/handbook/product/categories/features/)
- [List of merged security issues in `gitlab-org`](https://gitlab.com/groups/gitlab-org/-/merge_requests?scope=all&state=merged&label_name[]=security&milestone_title=%23upcoming). **Note:** It can include results from the security mirror `gitlab-org/security/`.

The list above is not exhaustive and is subject to be modified as our processes keep evolving.

## Application Security KPIs & Other Metrics in Sisense

- For KPIs and other metrics, please [see this page][7].
- For Embedded KPIs which you filter by section, stage, or group, please [see this page][8].

## General Role Functions

### Stable Counterparts

Please see the [Application Security Stable Counterparts page][4].

### Application Security Reviews

Please see the [Application Security Reviews page][1].

### RCAs for Critical Vulnerabilities

Please see the [Root Cause Analysis for Critical Vulnerabilities page][10]

## Application Security Engineer Runbooks

Please see the [Application Security Engineer Runbooks page index][5]

## Meeting Recordings

The following recordings are available internally only:

- [AppSec Sync](https://drive.google.com/drive/folders/1sxnBhPNDofWg5JmKqrhEl5y4_aWldTbt)
- [AppSec Leadership Weekly](https://drive.google.com/drive/folders/1jyNYP2AOqoOPqr4qGMuh7PGha_j-7brb)

## Backlog reviews

When necessary a backlog review can be initiated, please see the [Vulnerability Management Page][3] for more details.

## GitLab Secure Tools coverage

As part of our [dogfooding effort](https://about.gitlab.com/handbook/product/product-processes/#dogfood-everything),
the [Secure Tools](https://docs.gitlab.com/ee/user/application_security/) are set up on many different GitLab projects (see our [policies]({{< ref "inventory#policies" >}})).
This list is too dynamic to be included in this page, and is now maintained in the [GitLab AppSec Inventory]({{< ref "inventory" >}}).

Projects without the expected configurations can be found in the [inventory violations list](https://gitlab.com/gitlab-com/gl-security/engineering-and-research/inventory/-/issues) (internal link).

## GitLab Inventory

Learn more about the [GitLab AppSec Inventory]({{< ref "inventory" >}}).

## Reproducible Vulnerabilities

Learn how to identify or remediate security issues using real examples with GitLab's [Reproducible Vulnerabilities][11].

## Application Security Automation and Monitoring

Please see the [Application Security Automation and Monitoring page][12]

[1]: {{< ref "appsec-reviews" >}}
[3]: {{< ref "vulnerability-management" >}}
[4]: {{< ref "stable-counterparts" >}}
[5]: {{< ref "./runbooks" >}}
[6]: {{< ref "/job-families/security/application-security" >}}
[7]: https://app.periscopedata.com/app/gitlab/641782/Appsec-hackerone-vulnerability-metrics
[8]: https://app.periscopedata.com/app/gitlab/758795/Appsec-Embedded-Dashboard
[9]: https://docs.google.com/document/d/1Mba9ZhuVr2qBkvR7AqzNTUFMUTapJqiXkPUqc9Gr8io/edit
[10]: {{< ref "root-cause-analysis" >}}
[11]: {{< ref "reproducible-vulnerabilities" >}}
[12]: {{< ref "application-security-automation-monitoring" >}}
