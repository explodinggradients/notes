---

title: GitLab Dedicated Overview
category: GitLab Dedicated
description: "Gitlab Dedicated Support overview."
---



### Overview

[GitLab Dedicated](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/), from a support perspective, works as a combination of SaaS and Self-Managed. Customers have full Admin access to the instance, but no access to the infrastructure, nor to the backend configurations. This workflow captures the differences, and details of providing support for GitLab Dedicated.

If you'd like to work on GitLab Dedicated tickets, consider [creating an issue using the template](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Dedicated) in Support Training, and read the [overview](https://gitlab-com.gitlab.io/gl-infra/gitlab-dedicated/team/).

### Administrative access to a Dedicated instance

The GitLab Dedicated team does **not** have administrative access to the [Admin Area](https://docs.gitlab.com/ee/administration/) in the GitLab application on Dedicated instances and neither does the GitLab Support team. Select individuals in the customer organization do have access to the **Admin Area**. Any support requests that require a GitLab instance administrator to make a change in the Admin Area, for example resetting 2FA, has to be performed by the appropriate team within the customer organization.

### Working with logs

Working with logs [has been moved]({{< ref "dedicated_logs" >}})

### Working with Grafana

Working with Grafana [has been moved]({{< ref "dedicated_instance_health" >}})

### Switchboard

The Switchboard section [has been moved]({{< ref "dedicated_switchboard" >}})

#### Monitoring system graphs are for internal use

We do not share internal graphs from our monitoring systems with Dedicated customers. The reason for this is that as the SaaS provider, we manage the underlying environment. Sharing internal graphs would not be actionable by the customer since they don't have access to the environment and these graphs may not be interpreted correctly without a proper understanding of our system.

### View instance metadata and upgrade history

GitLab Dedicated tenants are defined in the
[Switchboard repository's `tenant_models` directory](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/sandbox/switchboard_la/-/tree/main/tenant_models).

- To view a customer's instance metadata, click on the appropriate `json` file.
- To view a customer's instance upgrade history, view the appropriate `json`
  file's commit history and search for commits that mention `gitlab`.
- Use the blame feature to find why individual lines or changes were added.
  It makes it easier to find MRs and Issues with additional context.

### Configuration changes

GitLab Dedicated uses the [Cloud Native Hybrid reference architecture](https://docs.gitlab.com/ee/administration/reference_architectures/10k_users.html#cloud-native-hybrid-reference-architecture-with-helm-charts-alternative). Instance implementation and changes are done via the [instrumentor project](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/instrumentor)

When any changes to the tenant instance are required, raise an issue in the [GitLab Dedicated issue tracker](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues) using a [Support Request template](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues/new?issuable_template=support_request).

If it's an emergency, [escalate the emergency](#escalating-an-emergency-issue) and contact GitLab Dedicated infrastructure team on Slack, using channel [`#g_dedicated-team`](https://gitlab.slack.com/archives/C025LECQY0M).

### Filing issues

In cases where Customer Support needs to interact with GitLab Dedicated engineers to gather information or similarly debug a problem at tenant's request (when Grafana or OpenSearch does not suffice), raise an issue in the [GitLab Dedicated issue tracker](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues) using a [Support Request template](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/issues/new?issuable_template=support_request).

### Escalating an Emergency issue

Emergencies from GitLab Dedicated will come through the [Customer Emergencies On-call Rotation](https://about.gitlab.com/handbook/support/workflows/customer_emergencies_workflows.html) as with other emergency types.

The GitLab Dedicated Infrastructure team has a 24/7 PagerDuty rotation: [GitLab Dedicated Platform Escalation](https://gitlab.pagerduty.com/schedules#PE57MNA). To [manually create a PD Incident](https://about.gitlab.com/handbook/support/workflows/support_manager-on-call.html#manually-triggering-a-pagerduty-notification_) use the [Dedicated Platform Service](https://gitlab.pagerduty.com/service-directory/P1H70IW) or use the Slack command `/pd trigger` and choose "Dedicated Platform Service" as the Impacted Service to escalate an emergency to an SRE after initial triage and analysis.

### Troubleshooting tips

#### Tagging logs while running tests

Customers can add a custom identifier, such as the ticket ID, to the `user-agent` field when testing. This makes it easier to filter logs related to the test.

For example:

```bash
curl -k -vvv -A"GitLabSupport012345" "https://tenant.gitlab-dedicated.com/users/sign_in"
```
