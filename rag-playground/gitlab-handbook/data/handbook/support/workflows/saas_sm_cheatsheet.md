---
title: SaaS, Self-Managed and Dedicated Troubleshooting tables
category: Support Team
subcategory: Uncategorized
description: "Troubleshooting tips for various problems on each GitLab platform type"
---

## Overview

The purpose of this page is to provide a single reference point that
Support Engineers can use when they need troubleshooting tips for various
problems on any GitLab platform. The goal is to make it easier for each
Support Engineer to resolve support tickets regardless of the GitLab
platform involved.


## How to use this page

Find the topic of interest to you, and follow the instructions there in
the table row that matches the appropriate GitLab platform: Self Managed,
SaaS, or Dedicated.

### Auth

|      |       |
|:----:| ----- |
|Self-managed| Self Managed Administrators will need to [configure the desired auth provider](https://docs.gitlab.com/ee/administration/auth/) directly in their gitlab.rb. Any configuration change on this file will require that you run `gitlab-ctl reconfigure` to successfully apply changes.|
|DotCom| Customers will [Configure SAML SSO for Groups](https://docs.gitlab.com/ee/user/group/saml_sso/index.html) directly, by going to **Group > Settings > SAML SSO**.|
|Dedicated| Start the investigation by [searching the logs](/handbook/support/workflows/dedicated_logs). To escalate, [raise an issue with the GitLab Dedicated team]({{< ref "dedicated#filing-issues" >}}).|

### Geo

|      |       |
|:----:| ----- |
|Self-managed| Geo is [configured in the gitlab.rb](https://docs.gitlab.com/ee/administration/geo/setup/) file. It requires a premium or higher subscription. **The steps must be followed in the order in which they appear.**|
|DotCom| *Geo is a Self-Managed feature only.*|
|Dedicated|[Raise issue with Dedicated team](/handbook/support/workflows/dedicated/#filing-issues)|

### Admin Area

|      |       |
|:----:| ----- |
|Self-managed| Administrators of self-managed systems will have access to their instance admin.|
|DotCom| Only GitLab Team Members can make use of administrative tasks on gitLab.com, therefore access is not granted to customers.|
|Dedicated| Customers have instance admins that can access the Admin Area. There is no [GitLab Rails console](https://docs.gitlab.com/ee/administration/operations/rails_console.html) access for customers.|

Use the [Admin Area docs](https://docs.gitlab.com/ee/administration/admin_area.html#gitlab-admin-area) for reference.

### Gitaly

|      |       |
|:----:| ----- |
|Self-managed| [Gitaly](https://docs.gitlab.com/ee/administration/gitaly/) configuration is managed through the **gitlab.rb** file. A customer can configure stand-alone [Gitaly](https://docs.gitlab.com/ee/administration/gitaly/configure_gitaly.html) or leverage [Gitaly Cluster](https://docs.gitlab.com/ee/administration/gitaly/praefect.html) to fulfill its git requirements. Be sure you know which of these types of Gitaly configuration a self-managed customer is using before you begin troubleshooting.|
|DotCom| Gitaly is managed by the infrastructure team of GitLab, so customers do not have access to it.|
|Dedicated|Raise issue with Dedicated team|

### Logs and Performance

|      |       |
|:----:| ----- |
|Self-managed| [GitlabSOS](https://gitlab.com/gitlab-com/support/toolbox/gitlabsos) is a great way to gather all logs from a customer instance in order to investigate further on potential issues.<br/>Similar to GitlabSOS, use [KubeSOS](https://gitlab.com/gitlab-com/support/toolbox/kubesos) if your customer uses Kubernetes instead of source or omnibus installations.<br/>[Fast-stats](https://gitlab.com/gitlab-com/support/toolbox/fast-stats) is a great way to compare performance analytics from and between GitLab Logs.<br/>[Green-hat](https://gitlab.com/gitlab-com/support/toolbox/greenhat)  is an experimental SOS and log parser.|
|DotCom|[Kibana](https://log.gprd.gitlab.net/) provides visualization capabilities on top of the content indexed on an Elasticsearch cluster to find Web based queries. Check the [tips and tricks](https://about.gitlab.com/handbook/support/workflows/kibana.html#tips-and-tricks) to understand what kind of information you can pull using this tool.<br/>[Sentry](https://sentry.gitlab.net/gitlab/gitlabcom/) helps investigate errors across different applications or environments, for example Ruby code related errors. Search on Sentry usually is done using a Correlation ID.<br/>[Grafana](https://about.gitlab.com/handbook/engineering/monitoring/#main-monitoring-dashboards) is used for infrastructure metrics collection for GitLab.com |
|Dedicated|[GitLab Dedicated Logs](/handbook/support/workflows/dedicated_logs/)|

### Architecture

|      |       |
|:----:| ----- |
|Self-managed| Check out the [reference architectures](https://docs.gitlab.com/ee/administration/reference_architectures/) we recommend to our customers and their different variations|
|DotCom| [The GitLab.com architecture](https://about.gitlab.com/handbook/engineering/infrastructure/production/architecture/#infra-current-archi-diagram) is managed by the infrastructure team and cannot be modified to meet individual customer's needs.|
|Dedicated|[GitLab Dedicated](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/) is a fully isolated, single-tenant, SaaS service managed through AWS by the [GitLab Dedicated Group](https://about.gitlab.com/handbook/engineering/infrastructure/team/gitlab-dedicated). GitLab Dedicated tenants [use](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/#availability-and-scalability) the GitLab [Cloud Native Hybrid reference architectures](https://docs.gitlab.com/ee/administration/reference_architectures/index.html#cloud-native-hybrid) with high availability enabled. See the list of [changes from the reference architectures](https://gitlab-com.gitlab.io/gl-infra/gitlab-dedicated/team/architecture/Architecture.html#changes-from-reference-architectures).|
