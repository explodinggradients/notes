---
title: "GitLab Security Operations On-Call Guide"
---

{{% alert title="This is a Controlled Document" color="danger" %}}
Inline with GitLab's regulatory obligations, changes to [controlled documents]({{< ref "controlled-document-procedure" >}}) must be approved or merged by a code owner. All contributions are welcome and encouraged.
{{% /alert %}}

The Security Operations sub-department is collectively responsible for responding to reports of actual or potential security incidents on a 24/7/365 basis.
- The SIRT (Security Incident Response Team) generally responds to reports of suspicious activities (e.g. Phishing, hacking, social engineering) and security alerts.
- The Trust & Safety team generally responds to reports of cryptomining, platform SPAM, abuse, bullying and violations of terms of service.

Prior to scheduling planned time off, Security Operations team members should consult with the team to ensure proper coverage will be available.

Security Operations Managers also share in On-Call responsibilities and need to ensure proper coverage for escalations and emergencies. The Security department maintains a series of On-Call escalations to ensure that every reported incident is responded to in a reasonable timeframe.

On-Call scheduling for SIRT is organized in Pager Duty within the `Security Responder` policy.

On-Call scheduling for Trust & Safety is organized in Pager Duty within the `Trust & Safety Responder` policy.

## On-Call Security Handoff times

Standard handoff times are as scheduled. However, team members are empowered to agree on a temporary modified handoff schedule as long as those involved agree and the team is notified in the team’s Slack channel.

SIRT
- 23:00 to 07:00 UTC –> APAC - 8 hours
- 07:00 to 15:00 UTC –> EMEA - 8 hours
- 15:00 to 23:00 UTC –> AMER - 8 hours

Trust and Safety
- 23:00 to 07:00 UTC –> APAC - 8 hours
- 07:00 to 15:00 UTC –> EMEA - 8 hours
- 15:00 to 23:00 UTC –> AMER - 8 hours


## Weekend On-Call Security Responsibilities

The Weekend On-Call Security team member will be responsible for covering On-Call responsibilities from AMER Friday evening until APAC Monday morning according to the established On-Call Security Handoff times.
- The Weekend On-Call Security team member is responsible for timely responding to PagerDuty and the incident response process in accordance with the `"Weekend On-Call Security  Responsibilities"`
- During the weekend hours, the Weekend On-Call Security team member is not expected to be at their computer working unless they are responding to an incident or working on a leadership request for critical deliverables. However, they will be asked to acknowledge any Pager Duty incidents via their mobile phone within 15 minutes, and begin triaging the incident within one hour. Priority 3 Severity 3 and below incidents can be handled by the team as weekday tasks.
- When there is a signficant business need, the Weekend On-Call Security team member  may be responsible for ensuring continuity of critical deliverables as determined by leadership. Critical deliverables will generally consist of, but are not limited to: threat hunting and mitigation, bug fixes, cryptomining, customer impacting SPAM, or detection and response engineering to protect against credible threats.

## Weekend On-Call Security Scheduling

- Weekend On-Call slots for FY24 will be filled on a volunteer basis meaning team members can sign up for the slots that would fit their schedules. The SIRT and Trust and Safety teams will have individual Weekend On-Call schedules so that one person from each team will cover the Weekend On-Call shift. General guidance is that team members should volunteer for the appropriate ratio of qualified team members to weekends requiring coverage. For example, in a team of 12 qualified team members, volunteering for 4 to 5 weekends per year, per person would allow for full coverage. Please note, ratios may change from time to time depending on the size of the team.
- If there are open remaining slots the Security Operations managers will assign slots to team members who have not hit their target amount of slots. For example, if there’s an open slot and a team member that should volunteer for 4 to 5 slots but has signed up for 2, the Manager can allocate the slot to that team member. If the team member is unavailable they would be responsible for finding a replacement.
- In case of emergencies, managers may seek other volunteers and in rare cases may need to assign coverage.

## Weekend On-Call Security Relief

- Current On-Call metrics show an average of less than one weekend page per month.
- Because busy On-Call weekends sometimes happen and in recognition of weekend coverage, GitLab is proactively asking team members to take the next two business days off following their Weekend On-Call shift as time off in lieu, regardless of whether the team member had to respond to an incident.

When scheduled for the Weekend On-Call Security shift team members should:
- Submit time off in lieu for the next two business days immediately following their Weekend On-Call shift. Because this time off is intended to provide team members with immediate relief, these days cannot be moved to days later in the week or month, regardless of other planned or unplanned time off.
- If a holiday or Friends and Family day falls on the next business day, time off in lieu can be taken for the subsequent two days.
- Commit to covering the Weekend On-Call shift. Avoid signing up for weekends you are unable to cover, or otherwise have a conflict.
- Find replacement coverage if you cannot commit to covering the entire weekend.

## Weekday On-Call Engineer Responsibilities

Security Operations provides weekday On-Call coverage using a follow-the-sun model. Weekday On-Call Security Engineers are the team members that cover the On-Call responsibilities during their region's sunny time.
- A Weekday On-Call shift typically covers one working week, from Monday to Friday.
- The Weekday On-Call Security Engineer is expected to cover the triage engineer role, and should generally be the first responder to alerts and incidents as they are presented via Pager Duty and via the various Slack and alerting channels.

## Weekday On-Call Engineer Responsibility to delegate

- Weekday On-Call Engineers are expected to delegate incidents to other Engineers after performing initial triage, and they are empowered to call upon other available team members for assistance. In general, more severe incidents such as S2 or higher, or higher-priority incidents such as P2 or higher, should only be delegated to team members available in the current sunny region. Less severe and less urgent issues such as S3 and P3 or lower, can be delegated to any team member not on PTO in any region. This allows the team to spread the workload across the global team while maintaining adequate coverage and response times.
- Sometimes, team members are working on a high-priority assignment and are temporarily unavailable for delegation. Team members who are not available for delegation must communicate that transparently in the team’s primary Slack channel.

## Weekday On-Call Paging Workflow

The Weekday On-Call paging workflow is currently designed to follow this escalation path:
1. Security Engineers in the sunny region are paged either all at once, or in a round-robin fashion, with one designated weekday On-Call Security Engineer per region. Team members not designated as the On-Call Security Engineer can and should provide assistance if the On-Call Security Engineer misses the page.
1. The Security Operations manager in the sunny region is paged as a backup.
1. Security Managers who volunteer as backups are then paged.
1. The Security Operations Director is paged.

## Security Managers On-Call

In addition to the Security Engineers being On-Call, the Security Managers across the GitLab Security Department act as backups in the event the Security Engineers are unable to acknowledge security pages. PagerDuty will automatically engage the Security Manager On-Call if the Security Engineers don’t acknowledge the first two page attempts, with each attempt being `15 minutes apart`.

It's the responsibility of the Security Manager On-Call to:

- Be available via mobile phone during their On-Call shift if the Security Engineer On-Call does not acknowledge a page.
- Attempt to contact the Security Engineer On-Call to acknowledge the page. **Note: If Slack is not available or an alternative means of communication is required, PagerDuty has cell phone numbers of GitLab team members involved in the on-call process. GitLab also setup a Zoom channel (#Slack Down!) for a backup communications channel.**
- If the Security Engineer On-Call is unresponsive, attempt to contact other Engineers to take on the page. Prioritize based on timezone and region.
- In the event of a high-impact security incident to GitLab, the Security Manager On-Call will be engaged to assist with cross-team/department coordination.

## Weekday Responsibilities

During weekday On-Call shifts the Security Engineer On-Call has these core responsibilities:

1. Acknowledge and respond to pages; delegate
1. Monitor and respond to incidents; delegate
1. Monitor and respond to alerts; delegate
1. Monitor and respond to security related slack channels; delegate
1. Continue critical assignments as determined by management
1. Review and engage on issues marked with the oncall label
1. Improve on-call and incident handling processes

## 1. Engagement: Paging Duties

The On-Call Engineer's primary concern is to provide timely and adequate responses to incoming pages. When receiving a page:
1. Acknowledge the alarm in the corresponding alert Slack channel or through PagerDuty directly
1. Review the contents of the page, the associated GitLab issue any other provided details
1. Resolve the PagerDuty alarm (via Slack or PagerDuty)
1. Notify the reporter(s) that you are responding
1. Triage the incident and contain if S2 or above; otherwise delegate. If while triaging an S2 incident, additional alerts are received, notify a manager and ask the team for support.
1. Notify the reporter(s) of the incident assignment
1. Notify the reporter(s) of containment
1. The team member selected to handle the incident performs the investigation and resolves it; notify the reporter(s) of resolution

If the alarm is not acknowledged within `two 15-minute opportunities`, the Security Incident Manager On-Call will be alerted.

Engineers should acknowledge pages within the first 15 minutes, and perform initial triage of potential incidents within the first hour of the alarm.

Be sure to communicate with the reporter(s):
- That you are acknowledging their page as soon as you have the opportunity to do so.
- That you have contained the security concern as soon as you have the opportunity to do so.

## 2. Review, Engage & The `incident` Label

Occasionally, issues that do not trigger a page are still created in the GitLab-SIRT namespace and will be marked with the `incident` label during the on-call shift, we should watch for and engage on new, as well as existing, open issues to assist towards mitigation/resolution. Those lower-priority incidents are also directly mentioned in the appropriate Slack channel.

These issues are generated through the automated /security workflow and require human intervention for triage.

## 3. Improve On-Call, Incident Handling, and GitLab's Security

As we continue to grow and mature in the operational security space we will have many new experiences, succeed and fail at handling security events, and subsequently learn from them. These learnings should be documented through runbooks, processes, and handbook updates. During On-Call shifts it is the On-Call Security Engineer's responsibility to take notes, look for improvement opportunities in how we handle scenarios, find steps that can be automated, and ask questions about our tools, services, infrastructure, and try to find questionable security areas or risky decisions so that we can improve GitLab's overall security posture.

## 4. Reduce the Backlog

As On-Call periods are typically interrupt driven it can be difficult to work on large projects, this is a good opportunity to reduce the queue of `Backlog` issues. During weekdays, it is the responsibility of the On-Call Engineer to review the backlog board for items that can be accomplished during the On-Call period. When working an issue from the backlog the On-Call Engineer should assign themselves the issue and should  see it through to completion. This may include completing it in the week following their On-Call schedule.

## Incident Ownership

There's a simple rule to incident ownership: Whoever is assigned to the incident after the initial triage, is the person responsible for incident resolution. Use the assignee field in the GitLab incident to identify the responsible person. In some cases, the incident may be high severity and high priority, and may have an assignee per region. In these cases, the work should continue around the globe until the incident is contained and eventually resolved.

Ownership of an incident means being the person responsible for:

- Ensuring continued progression to a contained and resolved state
- Maintaining ongoing 24/7 coverage of high-severity incidents
- Accurate and timely issue tracking and communication with stakeholders
- Adequate handoffs and communications

Being the responsible person does not imply being the sole person to act on these tasks. Hand-off at the end of an On-Call shift, or coordinated breaks during extended incidents, can temporarily assign  another person responsible for these tasks. To coordinate these hand-offs it's essential to equip the next person with all necessary details.

## Incident Hand-off

To best prepare the next Security team member and ensure continued progress, details should be recorded in the page-created issue as well as the team’s slack channel. Details like:

- **Issue Summary**: Brief summary of the issue and details of the current state.
- **Related Issues**: Related GitLab issues being worked on by other teams (Infrastructure, Product Engineering, etc.)
- **Who's Engaged**: Other GitLab team members engaged on the incident
- **Active Zoom Bridge**: «Zoom Bridge URL»
- **Slack Channel(s)/Thread(s)**: #Channel(s) and/or Slack thread link
- **Next Steps**: What are the next steps for the issue and/or what tasks or steps need to be taken by the next Security team member. If other teams are taking action, identify who is responsible for that work and what those actions are.

## Exceptions

Exceptions to this procedure will be tracked as per the [Information Security Policy Exception Management Process]({{< ref "_index.md#information-security-policy-exception-management-process" >}}).

## References

- Parent Policy: [Information Security Policy]({{< ref "_index.md" >}})
