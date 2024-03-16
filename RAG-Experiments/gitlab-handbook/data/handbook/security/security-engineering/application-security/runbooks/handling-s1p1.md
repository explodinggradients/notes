---
layout: handbook-page-toc
title: "Application Security Engineer Handling priority::1/severity::1 Issues"
---

The following process is a supplement to the first few steps of the [critical release process](https://gitlab.com/gitlab-org/release/docs/blob/master/general/security/process.md#critical-security-releases)

Once a potential severity::1/priority::1 issue is made known. The appsec engineer steps are as follows:

## Triage

1. Triage and verify the issue as you normally would [triage a report]({{< ref "hackerone-process" >}}).
1. To help SecOps quickly determine impact and log analysis, comment in the security issue with the summarized reproduction steps (HTTP Requests, generated log messages, images, etc).
1. After escalating, do an investigation to try to determine if there are other immediately vulnerable components or other impacts.

## Escalate

1. [Engage the Security Engineer on-call]({{< ref "engaging-security-on-call" >}}) with a link to the issue, a summary of what has happened, and an description of what SIRT may need to do.
1. Engage the appropriate [engineering manager and product manager of the affected component](https://about.gitlab.com/handbook/product/categories/) in both the issue **and** in the appropriate Slack channels.
1. If help from the GitLab Dedicated team is needed, [follow the runbook to escalate to their engineer on call](https://gitlab-com.gitlab.io/gl-infra/gitlab-dedicated/team/runbooks/on-call.html#escalating-to-an-on-call-person).
1. Ping `@appsec-leadership` in the `#sec-appsec` Slack channel with a link to the issue. This will help team leadership and other engineers get up to speed, in case they need to step in.

## Mitigate

Sometimes the fix is very simple, sometimes it's not. If the impact to users is greater than the time it takes to apply the long-term fix, you will need to consider a [short term solution](#short-term) as well as the [long term](#long-term) one. Otherwise, if you and the development team are confident the fix is straightforward and simple, then you only need to do the long term fix and roll it out in a critical security release.

### Short term

1. Collaborate with the development, security, and SRE/infrastructure teams to brainstorm short term solutions until a long term patch can be released.
  - Be sure to consider both GitLab SaaS and GitLab Dedicated
1. Analyze the impact for each option.
  - How effective is it at solving the problem?
  - How many customers are affected by this decision?
  - How exactly are they affected?
  - What's the magnitude?
  - What other positive and negative consequences are there?
1. Choose the solution that best balances the concerns above with the concerns of participating teams.
1. Approval is not required, but clear communication of decision is necessary. Notify the Director of Security, Directory of Infrastructure, and any other parties involved with the proposals and decision.
1. Once the short term solution has been delivered, validate that the fix was effective.

Some past short term options have been:
- Cloudflare rule to block certain endpoints.
- Disable a specific feature using feature flags or application configuration.
- Deploy a [hotpatch](https://gitlab.com/gitlab-org/release/docs/blob/master/general/deploy/post-deployment-patches.md).

### Long term

1. Follow the [flowchart]({{< ref "deciding-gitlab-com-deployment" >}}) to decide which type of release is best suited for the current issue.
1. Open an [RCA issue](https://gitlab.com/gitlab-com/gl-security/rcas/-/issues/) to start the RCA process.

## Handoff

Appsec engineers are not on-call. That means when the assigned appsec engineer's end of day arrives, they are responsible for handing it off to an appsec engineer in a subsequent timezone.

Provide a brief summary of the current status and outstanding or upcoming tasks required of AppSec. Provide useful links like the SIRT issue, comms document, slack links. Ideally also schedule a short synchronous call with the person to whom you're handing over, to discuss and answer questions.

Share that a handover has happened in the incident's Slack channel, and cross-post to other relevant channels like #sec-appsec. A message template like the following may be appropriate:

> 🤝 AppSec Handover 🤝  I have handed over to `@username` for any AppSec needs, as I am close to the end of my working day. [Include details on how we will continue to deliver on any tasks that AppSec is DRI for].

### Family and Friends Day Coverage

[Family and Friends Days]({{< ref "family-and-friends-day" >}}) are days where GitLab publicly shuts down. The AppSec [rotation spreadsheet](https://docs.google.com/spreadsheets/d/18vz84dgTfetTaBjbOCXaLKNfzLYMiy_tBW6RfEUYYHk/edit#gid=1486863602) indicates who is available from the AppSec team on those days. There will be one AppSec engineer covering for each timezone region (AMER, EMEA, APAC) during each F&F Day. Team members assigned to this rotation are expected to move their F&F Day to another day as they see fit.
