---
title: A Support Engineering Manager guide to account escalations
description: Guidance to Support Managers for how to handle account escalations
category: Manager
---

## Overview

This page guides Support Managers on the Support Manager DRI role for [Customer Account Escalations](https://about.gitlab.com/handbook/customer-success/csm/escalations/).

An Account Escalation may be initiated by Support Engineering (Support Managers or Engineers) through [converting a customer emergency into an escalation](/handbook/support/workflows/emergency-to-escalation-process.html), or as the result of a [STAR](/handbook/support/internal-support/support-ticket-attention-requests.html). The Customer Success Team may also [initiate an Account Escalation](https://about.gitlab.com/handbook/customer-success/csm/escalations/#initiating-managing-and-closing-an-escalation), engaging the Support team for assistance, depending on the escalation type (not all Account Escalations require Support engagement) and [severity](https://about.gitlab.com/handbook/customer-success/csm/escalations/#definitions-of-severity-levels).

### Account Escalation Team

Each escalation will have an [Escalation DRI](https://about.gitlab.com/handbook/customer-success/csm/escalations/#escalation-dri) leading a team of people contributing toward the successful outcome of the escalation. The team will consist of some (at a minimum the Escalation DRI, Lead Support Engineer, and Support Manager DRI) or all of the following roles:

- Escalation DRI
  - CSM for critical or high severity escalations
  - Support Manager for medium or low severity escalations
- Lead Support Engineer
- Support Manager DRI
- Other CSM Leaders or Account Managers involved
- Product Managers
- Development Engineers

## Responsibilities of the Support Manager DRI

The Support Manager DRI has the following goals:

1. Minimize uncertainties by turning them into well defined risks
1. Help define a set of exit criteria (goals) for the escalation, and guide the efforts of the Support team to work toward achieving those criteria
1. Create and maintain the [Support Escalation issue](https://gitlab.com/gitlab-com/support/escalated-customers/-/issues/new?issuable_template=incident&issue%5Bissue_type%5D=incident) to document our scope and exit criteria, along with other critical details tied to the Escalation
1. Create and maintain the [Escalation retrospective issue](https://gitlab.com/gitlab-com/support/escalated-customers/-/issues/new?issuable_template=account-escalation-retro) linked to the Escalation issue for follow up once an escalation is closed

Additionally, the Support Manager DRI may also be the [Escalation DRI](https://about.gitlab.com/handbook/customer-success/csm/escalations/#escalation-dri) for low or medium severity escalations.

## Uncertainty

Uncertainty is defined as a situation with unknown information. As managers, we need to ask the right questions that will enable us to turn uncertainties into well defined risks that we can then proactively manage. Uncertainty is something we can't prepare for, and in the majority of circumstances may lead to unnecessary use of resources to resolve the situation.

### Example of Uncertainty

Consider the following scenario:

```plain
It has been reported that a customer is experiencing problems with their LDAP configuration, resulting in users being unable to authenticate. During a two-day period, the Support team investigated the issue based on assumptions from the customer's LDAP configuration. We learned from a new customer comment on the third day of the Account Escalation that the customer uses an LDAP proxy that has been misconfigured.

Not knowing this proxy existed caused `uncertainty` that led us to an extended period of troubleshooting, therefore extending the time it took to resolve the problem. Asking questions about the customer architecture could have revealed this information sooner, leading to a better course of action earlier on in the process.
```

Not all uncertainties can be accounted for, however we can attempt to reduce those risks, which will allow us to better scope our work towards achieving the exit criteria of the escalation.

## Workflow

To serve as Support Manager DRI for an Account Escalation, use the following steps.

### Step 0: Preparation

- Ensure the [Customer Success Escalations Process](https://about.gitlab.com/handbook/customer-success/csm/escalations/) has been followed.
- Obtain a clear scope of the customer issues that led to the need for escalation to help you determine the right Lead Support Engineer for the escalation, keeping the customer's timezone in mind. A review of all recent support tickets opened by the customer can help further define this scope.

    **NOTE:** We are currently trialing an [Escalations-focused Support Engineer role](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/4545#designated-escalations-focused-engineers-for-this-trial) in AMER under [this issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/4545). Please reach out to the designated engineer(s) as a first point of contact either to step in as the technical lead or to provide technical guidance and support to the Lead Support Engineer.

- [Open an issue with Support Ops](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/organizations/-/issues) to ask that they check the `Escalated State` field for the organization in ZenDesk.
  - This will add the `org_in_escalated_state` tag to all future tickets opened by the customer.
  - This tag will [add a NOTE to the organization notes](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/triggers/uploads/c9a3e2843eff23572100b53cfca0da0c/Screen_Shot_2022-09-07_at_4.46.01_PM.png) signifying that the account is in an escalated state.

- Open a [Support escalation issue](https://gitlab.com/gitlab-com/support/escalated-customers/-/issues/new?issuable_template=incident&issue%5Bissue_type%5D=incident) under the [Escalated Customers](https://gitlab.com/gitlab-com/support/escalated-customers) project to serve as our Support escalation portfolio. This portfolio will include important details of the escalation, such as Support's purpose (why we are involved), our goals (clear definition of the exit criteria), along with a list of tickets and issues that are tied to the escalation.
  - Consider using the [timeline events](https://docs.gitlab.com/ee/operations/incident_management/incident_timeline_events.html) feature (available only if you create the issue as an incident) to track escalation updates, milestones, communication, and key events.

- Open a [Support Escalation Retrospective issue](https://gitlab.com/gitlab-com/support/escalated-customers/-/issues/new?issuable_template=account-escalation-retro), linking it to the escalation issue, for proactive input and post-escalation follow-up.

### Step 1: Lead Support Engineer Assignment

- Assign a Support Engineer to act as the **Lead Support Engineer** during an Account Escalation. Please ensure that you find an engineer who is in the same region as the escalated customer.

  - If the escalation requires global effort, work with the on-call managers to identify Lead Support Engineers in those other regions.

  - For the AMER region, please reach out to the [Escalations-focused Engineer](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/4545#designated-escalations-focused-engineers-for-this-trial) to take lead or to provide backend support if they are already leading another escalation (see [this issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/4545) for more details).

- Sync with the Lead Support Engineer (and their manager if needed) to evaluate their workload.

  - If necessary, help with handing off any of their assigned tickets and other responsibilities so they can prioritize their efforts on the escalation.

#### Note

From a technical perspective, the Lead Support Engineer will orchestrate the resolution, but they are not expected to be the sole technical owner of the escalation. Their role will be to guide the collaborative efforts between all regions and development teams in order to ensure prompt resolution of the issue.

### Step 2: Define Scope and Exit Criteria

- Define a clear scope of work with the escalation team. Be sure to state the exit criteria (goals). Both the scope and exit criteria need to be documented in the Support Escalation issue.

- Through collaboration with the customer, identify the tickets that relate directly to the escalation, and note those in the Support Escalation issue.

  - The Lead Support Engineer should take assignment of all related tickets.
  - Support Manager DRI's should add themselves to the CC list of all related tickets.

- Make sure the customer understands that lower priority tickets that are out of scope of the escalation may be delayed to ensure our focus remains on the escalated tickets.

### Step 3: Escalation Progress Updates

Work with the escalation team to provide daily or weekly updates in the related Slack channel for the Account Escalation. This is a channel with a name in the format `#esc_<CUSTOMER>`. These updates should include the following:

- Progress toward achieving the exit criteria
- Status
- Current tasks with associated tickets
- Next steps
- Blockers

Help maintain updates (in collaboration with the escalation team) to the escalation tracker Google doc (used to track executive summary updates and customer meeting minutes) and to the Support Escalation issue created under the [Escalated Customers](https://gitlab.com/gitlab-com/support/escalated-customers) project to track Support's technical efforts and progress.

**Side note:** Future desire - consider syncing Slack and Google doc updates or Slack and Support Escalation issue updates via some form of automation.

#### Pausing Daily Updates

Escalations sometimes enter a "monitoring" period, when we don't anticipate any activity for mutiple days. When this occurs, it's appropriate to pause the daily updates. To do so, post in the Slack channel for the Account Escalation and clearly define, 1) the current state of the escalation, and 2) a timeline of when we can expect the updates to resume. For example:

> **Status:** Customer intends to upgrade Redis in their production environment in 5 days (15-Mar-2023).
> **Next steps:** Monitor for any updates from the customer over the next 5 days. If no issues are reported during this time, next update is targeted for 15-Mar-2023.

When daily updates are paused, continue to check every day for activity which would warrant resuming the updates.

### Step 4: Evaluate Progress

Determine if progress on the current tasks has slowed or stalled. If either of these is true, work with the Lead Support Engineer to [escalate further to a specialized development team](https://about.gitlab.com/handbook/engineering/development/processes/Infra-Dev-Escalation/) to ensure that work is progressing in the right direction.

### Step 5: Evaluate Stability and Monitor

Once the customer has stabilized, work with the escalation team to agree on a closing strategy. In most cases, we keep the customer in an escalated state for an agreed period of time to monitor their status. Once the monitoring period has passed with the customer remaining stable, close the escalation.

Before closing the Account Escalation:

- Review the steps listed in the [Customer Success Escalation Page](https://about.gitlab.com/handbook/customer-success/csm/escalations/#closing-the-escalation) and collaborate as needed to complete the closing steps.

- [Open an issue with Support Ops](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/organizations/-/issues) to ask that they uncheck the `Escalated State` field for the organization in ZenDesk.

  - The `org_in_escalated_state` tag will no longer be applied to future tickets opened by the customer. The organization notes will no longer display the escalated heading 1 note.

### Step 6: Retrospective

- In collaboration with the escalation team, complete the retrospective (within 3 weeks of escalation closure) in the issue created.

- Lead the retrospective sync meeting (if one is deemed necessary) to collect any final feedback and ensure all team members are clear on any remaining action items and due dates.

## FAQ

- How do we handle emergency tickets opened by the customer during an Account Escalation?

    > The Lead Support Engineer's main priority during their workday is the escalated customer. In general, an escalated customer should **not** trigger the [regular emergency process](/handbook/support/workflows/customer_emergencies_workflows.html). The Lead Support Engineer will work directly with the customer, and if necessary, request additional resources. The Account Owner must notify support of the emergency in the `#a_customer_escalation` channel.

- What if an emergency occurs out-of-hours for the Lead Engineer?

    > In this case, the customer can trigger our [emergency support process](https://about.gitlab.com/support/#how-to-trigger-emergency-support). There must already be awareness of this possibility among the Lead Support Engineer and Manager DRI, with proactive communication sent to the scheduled on-call Support Engineers, Managers, and Development teams.
    >
    > The Manager and Lead Support Engineer should consider being on "heightened alert" during this time and offer support if possible. However, at a minimum, they will review the emergency when back online to document the troubleshooting efforts taken in the Support escalation incident and timeline, and perform any post-mortem reviews with the customer.

- Is it just one ZD ticket per Account Escalation, or is it sometimes multiple?

    > In principle, an Account Escalation means "this account, for some reason, is in a heightened/risky state".
    >
    > Imagine you're really hungry and are walking to get an apple. You might be slightly more likely to make a rude gesture to a car that cuts you off at the crosswalk than you are usually inclined to.
    >
    > We have the "Escalated State" checkbox on the orgs in Zendesk for this reason: if they're escalated they're likely to be in a heightened state of emotion and urgency all around.
     Individual tickets may or may not be relevant to the exit criteria for the escalation, but all points of contact are relevant to the overall customer sentiment.
    >
    > Be aware and circulate the info to the escalation channel, and let the folks there know to what extent you can contribute to creating a positive customer experience. In turn, let the manager and lead support engineer guide any deviations we may want to take to typical support workflows.

- How often should I initiate a sync meeting? Daily? Weekly?

    > The appropriate cadence for a sync meeting should be determined in collaboration with the escalation team. As a general rule, it is dependent on the severity of the escalation, but there are exceptions.

- If the customer is stable, how long do I need to wait to close the Account Escalation?

    > It depends; ensure the customer is comfortable with the current solution, and their instance status remains stable. Sync with the escalation team to make a decision together, confirming that the exit criteria have been met. There is not a hard rule for this.
