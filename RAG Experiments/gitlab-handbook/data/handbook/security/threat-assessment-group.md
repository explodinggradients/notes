---
title: "Threat Assessment Group (TAG)"
---

## Overview

Occasionally, there will be an external security event that may require an immediate analysis to determine if that event impacts GitLab or our customers. A recent example of such an event is the [supply chain attack on SolarWinds](https://www.bleepingcomputer.com/news/security/the-solarwinds-cyberattack-the-hack-the-victims-and-what-we-know/) that has impacted potentially thousands of their customers. In order to efficiently analyse and determine what, if any, response from GitLab is appropriate to large scale events such as this we have formed a Rapid Action Threat Assessment Group that will involve stakeholders from across GitLab. This group will intentionally be small and does not replace the function of any existing incident response teams or capabilities but will engage existing processes and teams as necessary.

## Mission

TAG's mission is to quickly understand how an important external security event may impact GitLab or its customers and define what actions or next steps are required. Next steps could be anything from a simple customer communication stating that we are not impacted to a formal incident response process ran by our SIRT team.

## Goal

Our primary goal will be to quickly assess and understand a major external security event and how it impacts GitLab or our customers. While this group will not perform a direct incident response function, other teams such as SIRT and Infrastructure already provide these capabilities, we will help GitLab leadership understand the full impact and what next steps should be taken by GitLab. While it is understood that information about a major external security event may be rapidly evolving our goal will be to move quickly based on currently available information. Where necessary we will iterate on our recommendations as new information becomes available.

## Timing

This group is intended to understand and provide reporting up the management chain in a quick and timely manner. Initial assessments will be provided to Security Leadership within 2 hours of an event becoming known to the team. As needed we will iterate on that assessment and notify stakeholders of any additional or changed information.

## Group Structure

The group is comprised of a small number of engineers from a variety of teams. This allows for a complementary approach to the situation at hand from multiple angles simultaneously. The result of such a diverse group structure is a rapid, efficient and holistic assessment.

### Participating GitLab team members

The group consists of the following individuals:

- Greg Johnson, Staff Security Engineer, Red Team
- Mark Loveless, Staff Security Engineer, Security Research
- Dominic Couture, Staff Security Engineer, Application Security

The DRI of the group is Steve Manzuik

To contact the entire group via Slack a group @tag-sec has been created and may be used.

## Workflow

![tagworkflow2.png](../tagworkflow2.png)

This workflow defines the high level process that will be followed by the Rapid Action Threat Assessment Group.

- Potentially impacting security event; An issue to track the event will be created in the [appropriate project](https://gitlab.com/gitlab-com/gl-security/threat-assessment-group)
- A notification to all stakeholders will be made via Slack informing them that an issue is being assessed for impact to GitLab.
- Additional team members are pulled into the analysis as needed. This will depend on the issue at hand and if additional expertise is needed.
- All available facts and supporting data will be gathered and analysed.
- The corresponding issue will be updated to reflect our analysis and include supporting data.
- An update to stakeholders and Security Leadership will be given via Slack.
- As new data becomes available additional analysis will be conducted.
- The corresponding issue will be updated with any new findings.
- In the event of significant updates to the analysis security leadership will be again notified via Slack.

## Company Advisory

Depending on impact, an advisory may be needed to notify the company of required action or important information.

The process for creating an advisory is as follows:

- Security event warranting an advisory is identified (via SIRT, TAG, …)
- Advisory is crafted by Security Communications and Security Leadership
- Advisory is posted to the notification board
- GitLab team members are notified via email and a message posted to #company-fyi

Advisories will be posted to the [internal security notification dashboard](https://gitlab.com/gitlab-com/gl-security/internal-security-notification-dashboard/-/wikis/*Dashboard:-GitLab-Internal-Security-Notifications*)

If you would like to report an event for advisory consideration please contact TAG by using the slack command @tag-sec
