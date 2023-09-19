---
title: Handbook On-Call
---

## Important Update

**See [Content Websites](/handbook/content-websites/) for the latest information about the DRI and support processes for the about.gitlab.com and handbook.gitlab.com site.**

## Introduction

GitLab recognizes that the Handbook is a critical part of empowering team members to do their jobs effectively. As such we have implemented a basic on-call process (refer to [First-response Service Level Objective](#first-response-service-level-objective) below) to ensure that someone is available to assist team members in the event that something is broken in the handbook or if they are having trouble with making updates to it.

## Reporting an issue

Any issues should be reported in the [#handbook-escalation](https://gitlab.slack.com/archives/CVDP3HG5V) channel in Slack.

### When to escalate an issue

Issues should only be escalated to the Handbook On-Call team if it relates to:

1. Master being broken
1. Security incidents
1. Significant broken pages in production (e.g. the values page being unreachable)
1. Broken infrastructure
1. Bugs that prevents team members from accessing important information
1. Time sensitive updates to the Handbook where there are any issue in making the update

## On-call schedule

Until recently members of the `Editor` team were part of the on-call process and members of the [#handbook-escalation](https://gitlab.slack.com/archives/CVDP3HG5V) channel.
Additionally any GitLab team member can volunteer to join the [#handbook-escalation](https://gitlab.slack.com/archives/CVDP3HG5V) channel and help out.

We are looking into formulating alternatives and the future.

### Expectations for being on-call

1. Make sure you are set to receive notifications for the [#handbook-escalation](https://gitlab.slack.com/archives/CVDP3HG5V) channel
1. When an issue is reported:
    1. Acknowledge the team member and let them know you are looking into it
    1. You can check on `#production`, `#incident-management`, and `#is-this-known` to see if it's a know issue with infrastructure or other problems.
    1. Provide an update as soon as you are able to confirm their problem.
    1. You can also post updates in `#website` and/or `#handbook` as appropriate.
    1. Resolve the problem, or provide feedback to the team member on how they can resolve it.
    1. Offer to have a Zoom call to help replicate or resolve the issue if it is not straight forward.

### When to hand over to Reliability Engineering

The Handbook On-Call deals specifically with matters relating to the `www-gitlab-com` repo source code and configuration.
If a reported issue relates to the GitLab product or the infrastructure running the [https://about.gitlab.com](https://about.gitlab.com) website then it should be escalated to the Reliability Engineering team.
To report an incident follow the instructions on the Incident Management page: [https://about.gitlab.com/handbook/engineering/infrastructure/incident-management/#reporting-an-incident](https://about.gitlab.com/handbook/engineering/infrastructure/incident-management/#reporting-an-incident)

### First-response Service Level Objective

All incidents reported in the [#handbook-escalation](https://gitlab.slack.com/archives/CVDP3HG5V) channel, during weekdays (Mon - Fri, 08:00 UTC+0 - 18:00 UTC-7), should receive an initial response of acknowledgement within 1 hour of it being reported.

## Common Incidents and Tips

### Runbook for about.gitlab.com

There is also a [runbook for about.gitlab.com incident handling](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/uncategorized/about-gitlab-com.md).

### Managing broken master alerts in #handbook-escalation

All broken CI pipelines for the `master` branch of the `www-gitlab-com` repo are automatically posted in the Slack channel.
These reports should be investigated and addressed where needed.

Once a report has been looked at, please leave a comment stating the nature of the problem, action taken and add a ✅ reaction to the message to show that it has been handled.

If for some reason there is a large amount of failures resulting in spamming the channel, the error reporting can be turned off in the repo settings: [https://gitlab.com/gitlab-com/www-gitlab-com/-/services/slack/edit](https://gitlab.com/gitlab-com/www-gitlab-com/-/services/slack/edit)

### Merging Urgent MRs

See [the description of this issue](https://gitlab.com/gitlab-com/www-gitlab-com/-/issues/6356) for details on the current workarounds required for [this bug related to the Merge Train](https://gitlab.com/gitlab-org/gitlab/-/issues/214742#note_338664758)

### Stuck Merge Train

To see the status of the merge train (useful when team members are reporting that their MRs seem 'stuck' on the train), see [this issue to check the status and perform a workaround, if necessary](https://gitlab.com/gitlab-org/gitlab/-/issues/217908#when-the-merge-train-in-the-www-gitlab-com-project-might-be-stuck).

TL;DR for workaround: If the first/oldest MR `iid` in [the FIFO list](https://gitlab.com/api/v4/projects/7764/merge_trains?scope=active&per_page=100&sort=asc) (`sort=asc` by ID) is actively running a pipeline and eventually gets merged, then things are moving along, just slowly.  If the first one in the list isn't currently running any pipeline, remove it from the train and re-add it (it should go to the end).
