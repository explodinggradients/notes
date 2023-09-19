---
title: Support Global Groups
description: Support Global Groups main page
---

The Support Global Groups way of working is based on the knowledge that people are much
more successful when working in small self-organizing groups than when working in large ones.
GitLab Support is definitely a big group, and it's only getting bigger! So now
it has become very difficult for Support Engineers in this large, global
environment to connect with other team members, to know who to contact when
they need help, to feel heard, and to be successful in their work.

With the introduction of Support Global Groups (SGG) in May of 2022, we aimed
to create for all Support Engineers a smaller, safer space for belonging,
which still maintains their full access to the support, knowledge and
experience of our global Support Team. Another important aspect of SGG is that
it provides for each SE a less intimidating, easier to grasp, more manageable
set of work for which they share responsibility with their small, close group.

In this environment, we have observed and received feedback from
our Support Engineers during SGG trials that they feel less
work-induced stress and more happiness and job satisfaction overall. With
that happiness comes greater energy, more and better innovation, greater
efficiency, and better results for our customers and our company. We see SGG
as a strong foundation for success as the Support Team continues to scale.

For a little more of an introduction to SGG, please see this 9-minute
[video](https://youtu.be/BvYiQkNJOno) created by four Support Engineers who
participated in the SGG Trials: Andrew, Ryan, Daniel and Ben.

## SGG Basics

### The System

- There are 5 Support Global Groups - this number will go up over time as the
  Support Team grows
  - each group has about 1/5 each of the SaaS and SM SEs from each of the three
    regions
  - each group has a representative blend of tenure and skill level
  - product expertise is distributed reasonably between the groups
  - the groups are all named after trees from around the world:
    - [Baobab](groups/baobab)
    - [Ginkgo](groups/ginkgo)
    - [Kapok](groups/kapok)
    - [Maple](groups/maple)
    - [Pine](groups/pine)

#### Zendesk

- Inbound support tickets are automatically distributed in a round-robin
  fashion to the groups
  - there is a separate distribution for SaaS, Saas-Account, Free-user and SM tickets - if there are 5
    groups then each group will get 1/5 of the SaaS tickets, 1/5 of the SaaS-Account tickets, 1/5 of the Free-user tickets, and 1/5 of the SM
    tickets
  - any supported ticket is routed via SGG except: L&R tickets, GitLab Incidents tickets and Emergencies tickets
- Each group works primarily out of a single Zendesk view, named `SGG: [group name]`
  - the view shows only the tickets that were distributed to the group
  - the view shows all non-solved, non-pending tickets for the group
  - the view is grouped by ticket stage to support prioritization of FRTs
    and Needs-Org
  - the view is visible to everyone in Support to aid in collaboration
- A ticket is assigned to a group by setting the value of the `SGG` field to
  the name of the group
- A Support Engineer is assigned to a group by adding text in the format
  `SGG: [group name]` to the `Groups` section of their entry in the
   [support-team.yaml](https://gitlab.com/gitlab-com/support/team/-/blob/master/data/support-team.yaml)
   file

#### Slack

- Each group has its own Slack channel named `spt_gg_[group name]`
- Each Slack channel is public
- Pinned to each Slack channel are:
  - a link to this page
  - a link to the group's handbook page
  - a link to the Support Team page showing the group's membership
  - a link to a permanent Zoom room for that group to use in collaborating

##### Daily Stand-up Bot

The [SGG Slackbot's](https://gitlab.com/gitlab-com/support/support-ops/other-software/sgg-slackbot) Daily Stand-up posts each morning for each region regularly, in a number of channels to advise global groups of different information. For further details of the different variations, please refer to the SGG handbook page of the group you are curious about.

###### Daily Stand-up Bot for Licensing and Renewals in APAC

In the APAC region, team members who have a shared focus on the Licensing and Renewals work also utilises the Daily Stand-up Bot, posted to the [#support_licensing-subscription](https://gitlab.slack.com/archives/C018C623KBJ) channel in Slack, which supports them in ensuring support coverage reliability of the Licensing and Renewal tickets across APAC [Support hours](https://about.gitlab.com/support/#definitions-of-gitlab-global-support-hours).

###### Modifying your group's Daily Stand-up Bot

To request modifications to the Daily Stand-up Bot in your channel, please create an [SGG Slackbot issue.](https://gitlab.com/gitlab-com/support/support-ops/other-software/sgg-slackbot/-/issues/new)

### SE Responsibilities and Priorities

---

**>>>>>>>> The primary responsibility of each Support Engineer is the success of their
group. <<<<<<<<**

---

#### "Success of their group" means

- Achieving our [target](https://about.gitlab.com/handbook/support/performance-indicators/#service-level-agreement-sla)
  of delivering a meaningful first response on tickets assigned to the group
  within SLA at least 95% of the time
- Delivering timely and meaningful updates on all tickets assigned to the
  group, resulting in high quality resolutions
- Working together to fulfill the group's responsibility to manage and resolve
  all tickets that are assigned to the group. This includes things like:
  - monitoring the view and distributing the tickets
  - maintaining progress on tickets when the assignee is unavailable
  - reaching out to managers or other groups when help is needed to fulfill
    this responsibility
  - collectively taking responsibility for escalated tickets within the group
- All group members participating on a daily basis in supporting the rest of
  the group by sharing knowledge, assisting on tickets, and contributing to
  group process development and improvement
- Recognizing and seeking additional help from managers and other groups when capacity is at risk due to OOO, on-call, or increased work loads. Suggestions include:
  - Strategizing as a group ahead of time (if you see capacity is at risk)
  - Asking for manager help in the #spt_gg_forest Slack channel
  - Initiating a [branch out session](https://about.gitlab.com/handbook/support/support-global-groups/branch-out-sessions.html) to ask other groups for help
- All group members participating in onboarding new group members
  to ensure that newcomers feel comfortable asking questions.
  The group can decide how they want to approach it.
  This can include things like:
  - regular group crush/pairing/coffee chat sessions
  - identifying tickets that would help push a new group member out of their comfort zone
  - encouraging a new group member to ask for help
- All group members holding each other accountable for contributing
  appropriately to the group's success
- Ensuring that all tickets are assigned at the time of first response
  - Ownership is important for delivering a great customer experience and
    for keeping tickets moving toward resolution
  - In SGG, assigned tickets remain visible in the group view, so **everyone
    can and may contribute**

#### Prioritizing work

Each Intermediate and Senior Support Engineer should generally be prioritizing their daily
work according to the following list. Interviews, training, special assignments
and other time-bound commitments are examples of good temporary exceptions to
these priorities. Your group might also determine a different workflow or
distribution of work that would create a different prioritized list.

You should think of this list as a tool for helping you to make decisions. When
there are multiple things to be done, these priorities should guide you toward
deciding which of them to do first.

1. Handle:
   - Emergencies if you are the Support Engineer On-Call, or if the Engineer On-Call needs help
   - Incidents if you are the CMOC
   - [Account escalations](https://about.gitlab.com/handbook/customer-success/csm/escalations/) if you are a DRI or contributing member on an active escalation.
1. Handle [STARred tickets](/handbook/support/internal-support/support-ticket-attention-requests.html) that are assigned to you or your group.
1. Make sure that all new tickets in your group's view receive a meaningful
   first response within SLA
1. Make sure your assigned tickets are all up to date and progressing
   appropriately
1. Make sure there are no unassigned tickets in your group by:
   1. Taking assignment if you have capacity
   1. Asking others in the group to do so if you don't
   1. [Bring the ticket to managers](/handbook/support/workflows/how-to-get-help.html#bring-the-ticket-to-managers) if the group is at capacity
1. Help on tickets assigned to others in your group by:
   1. posting an internal note with relevant helpful information, OR
   1. answering questions from the assignee in your group Slack channel, OR
   1. asking the assignee if they'd like to pair on the ticket, OR
   1. responding directly to the customer, **preferably only if a response
      is needed urgently AND the assignee is unavailable to work the ticket**
1. Assist with Slack requests in [Support Pods](/handbook/support/workflows/working-with-pods) you participate in (if applicable)
1. Attend to indirect ticket work you have to do, such as:
   - docs updates
   - issue creation or contributions
   - training
1. Help on tickets within your [Support Pods](/handbook/support/workflows/working-with-pods) (if applicable) by:
1. posting an internal note with relevant helpful information, OR
1. asking the assignee if they'd like to pair on the ticket
1. Help on tickets outside of FlexiPods and assigned to other groups (Seniors may recognize if other groups are struggling and can decide if a group has the capacity to help)

#### Maximizing group success

- Get to know each other! Make connections! Build relationships!
  - have coffee chats
  - have weekly meetings just for fun, maybe cross-regional
  - discover each other's skills
- Collaborate!
  - consider inter-regional handover calls
  - use the group's Zoom room for pairing sessions
  - ask the group for help on tickets
  - respond to requests for help even if you have to say "I can't"
- Talk to each other in your Slack channel:
  - find out who is in today, and talk about covering for those who are out
  - decide who will keep an eye on the queue and when
- Get organized - initiate and participate in conversations about things like:
  - how the group will manage tickets and the queue when group members are
    on PTO or have other commitments
  - how to handle preferred region in tickets

#### Global Collaboration

We are all part of a global team of 100+ support engineers and in
SGG we have the benefit of both working in a small familiar group
and of the broad experience and expertise of our full global team.
Flexipods is one example of cross-group collaboration, some others are:

- pairing sessions
- crush sessions (including [branch out sessions](https://about.gitlab.com/handbook/support/support-global-groups/branch-out-sessions.html))
- sharing questions to a broader audience in #support_gitlab-com and
  #support_self-managed and #support_team-chat

#### Escalate to Unblock (Asking for Manager Help)

Managers are here to help and support SGG team members. If you or your global group feel blocked, and want help on any of the following, we've created [#spt_gg_forest](https://gitlab.slack.com/archives/C03LL7Z2291) for all SGG team members to use in collaborating more closely with Support managers:

- provide guidance around SGG strategies
- help identify and discuss challenges that require manager attention and/or support
- highlight successes across SGGs
- provide support around particular customer situations in an SGG (handover assistance, difficult customer handling, etc.)

## SGG History

For a timeline table of the history of SGG and the many issues involved, please see [this SGG History Google doc](https://docs.google.com/document/d/1w6TZyxJSQZIHZoJqRkWOG7wW7aRwPGk-QeiUHZNAQXY/edit) for a summary.

## FAQ

For answers to the most common questions about SGG, please review the
[SGG FAQ](/handbook/support/support-global-groups/sgg-faq.html) page.

## Training Plan for launch May 2022

Please see the [Training Plan page](/handbook/support/support-global-groups/training-plan.html)
