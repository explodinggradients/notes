---

title: Metrics Analysis - Hypothesis and Actions
description: "How to analyze Support metrics hypotheses"
---

## Purpose

This page documents hypothesis for metrics dips and techniques for evaluating them.
Additionally it includes specific actions that might be used to shore lagging metrics up.

## FRT is below target

---

### Ticket volume is too high

#### Past Analysis


##### [2020-09-01](https://gitlab.com/gitlab-com/support/metrics/-/issues/1)

**Evidence Gathered:**

- Historical FRT achievement from
  - [Support KPIs - SM => FRT SM](https://gitlab.zendesk.com/explore/dashboard/593393F9EDD57F39F9745F442B691EEAD106AA49B6C907D3D50046FBB4AC151E/tab/12396242)
  - [Support KPIs - SaaS => FRT SaaS](https://gitlab.zendesk.com/explore/dashboard/593393F9EDD57F39F9745F442B691EEAD106AA49B6C907D3D50046FBB4AC151E/tab/12396192)
- Headcount by month from [Support Hiring Reports](https://drive.google.com/drive/search?q=support%20hiring%20reports)
- Ticket count by month

**Approach:**

- Examined historical achievement by area to see if a specific type of tickets is behind the dip in performance
- Took a look at historical and current ticket volume to see if there are any outliers (e.g. a large increase in tickets over the past period)
- Peered into the ratio of tickets / engineer over the past year

#### Shaping Actions


If ticket volume is too high:

- Determine what is driving that volume. If it's:
  - a specific problem type, investigate automation or clarifying workflows to increase efficiency for these problem types.
  - a specific incident, shape macros or workflows to increase efficiency, consider assigning a specific set of engineers to focus on these types of tickets.
  - a lack of headcount, focus on hiring and shape onboarding to increase the speed at which engineers can answer certain ticket problem types.
  - a general increase, focus on "burst mode" workflows; arrange groups of individuals to focus on first responses and setting customer expecations.

---

### A time-consuming workflow is causing a dip in performance

#### Past Analysis


#### [2020-09-01: FRT Hawks spending more time on needs-org tickets is causing a dip in performance](https://gitlab.com/gitlab-com/support/metrics/-/issues/6)


**Evidence Gathered:**

- Tickets opened by email that had no plan (that is: emails that might trigger the needs-org workflow)

**Approach:**

- Examine number of tickets that might trigger the needs-org workflow
- Understand which of these tickets actually triggered the workflow
- Determine amount of time we could save by adjusting the workflow

#### Shaping Actions


If you suspect a time consuming workflow is causing a dip in performance:

- Identify the number of tickets that would fall under the workflow
- Verify that the workflow is being evenly applied to the set of tickets in question
- See if there any efficiency gains to be made through automation

---

### Dedicating resources to a specfic set of tickets has reduced the overall capacity of the team

#### Past Analysis


##### [2020-09-01: Adding resources more dedicated to US Federal has reduced the overall capacity of the team](https://gitlab.com/gitlab-com/support/metrics/-/issues/7)

**Evidence Gathered:**

- [YTD Incoming Tickets by Priority](https://gitlab-federal-support.zendesk.com/explore/dashboard/5D43737D8DD3E9472A3B176CE984ADCA2391368E94E7F578AE97B14D39152F96)
- Team size (Global and in AMER)
- Ticket resolution target

**Approach:**

- Examined theoretical capacity loss by looking at tickets/engineer reduced from "general" queues.
- Looked at AMER and Global theoretical loss
- Examined theoretical capacity loss by repeating the above caluclation with "actual" close rates.
- Examined "worst case" capacity loss by assuming 100% of productivity taken by this queue.

##### [2020-09-01: Adding L&R has drawn resources away from the rest of the queues that haven’t been replenished.](https://gitlab.com/gitlab-com/support/metrics/-/issues/5)

**Evidence Gathered:**

- [Public and internal comments per form among L&R focused engineers](https://docs.google.com/spreadsheets/d/1Zbfq--98a_PIazUi-8jMcFzT4znXEav8S42caeAuZyc/edit?usp=sharing)
- Prior engineer experience (self-managed or SaaS) for L&R focused engineers
- [Public and internal comments per form among engineers not focused on L&R](https://docs.google.com/spreadsheets/d/1Zbfq--98a_PIazUi-8jMcFzT4znXEav8S42caeAuZyc/edit#gid=1091975505)

**Approach:**

- Examined capacity loss by looking at effort toward L&R tickets that reduced effort in engineer experience areas
- Compared effort toward L&R tickets with effort in general queues for engineers with experience in those queues (e.g L&R ticket effort is ~10% of total SaaS ticket effort)
- Examined "worst case" capacity loss by assuming 100% of effort/productivity taken by this queue.

#### Shaping Actions


If dedicating team-members to a specific set of tickets has reduced capacity:

- hire
- look for efficiency gains through better workflows, processes and automation
- determine if there are any gains to be made through engineering effort and communicate the impact

---

### Tickets have increased in difficulty

#### Past Analysis


##### [2020-09-01: SaaS Tickets have gotten harder](https://gitlab.com/gitlab-com/support/metrics/-/issues/9)

**Evidence Gathered:**

- [Requestor Wait Time](https://gitlab.zendesk.com/explore/dashboard/36925DBD1F5E3C7BA541DB38D11AC51E0EAAFDD30DCB63FDE83CF1389E555D96/tab/10100682)
- [Time to Resolve](https://gitlab.zendesk.com/explore/dashboard/36925DBD1F5E3C7BA541DB38D11AC51E0EAAFDD30DCB63FDE83CF1389E555D96/tab/10200712)
- [Anecdotes from ICs](https://gitlab.com/gitlab-com/support/metrics/-/issues/1#note_413985941) and data from raised points:
  - [Integrated Cluster growth per month](https://docs.google.com/spreadsheets/d/17nib0Q8Db6E-Ppa2VWjmpmuhBWf0yr5kBEHpnR1eCpI/edit#gid=0)
  - [Package Registry Growth](https://docs.google.com/spreadsheets/d/17nib0Q8Db6E-Ppa2VWjmpmuhBWf0yr5kBEHpnR1eCpI/edit#gid=1324848180)
  - [Internal Issues Per Month](https://docs.google.com/spreadsheets/d/17nib0Q8Db6E-Ppa2VWjmpmuhBWf0yr5kBEHpnR1eCpI/edit#gid=1918925639)

**Approach:**

- Examine data that correlate with difficulty (TTR and Requestor Wait Time)
- Examine anecodotal data about ticket subjects, assuming that these areas may be underserved by experts.

**Notes:**

- The data gathered while examining this hypothesis generated additional falsifiable explanations

#### Shaping Actions


If tickets have increased in difficulty:

- Determine if additional headcount can be applied to this area (temporarily)
- Examine specific areas of challenge and develop training and workflows
- See if there are possibly gains in efficiency through macros, tooling or workflow improvements
- Identify product issues or feature requests that will reduce the impact of challenging ticket areas
- Examine documentation for problem areas, and additional content to help customers self-serve answers

---

### Time-Off impacting performance

#### Past Analysis


##### [2020-09-14: Folks on PTO over summer and F&F days have caused lags in performance](https://gitlab.com/gitlab-com/support/metrics/-/issues/3)

**Evidence Gathered:**

- [Ticket update volume](https://gitlab.zendesk.com/explore#/pivot-table/connection/10438872/query/41841912)
- [Summary spreadsheet showing active contributions to ZD tickets (over 20 ticket updates per engineer per month)](https://docs.google.com/spreadsheets/d/1vEJ2ks8pNeR2HVUn1actQcGEHH1ERxct7_kIDasOWDo/edit#gid=960486526)
- [Zapier enabled PTO calcualtor spreadsheet](https://docs.google.com/spreadsheets/d/1EFpF6_ixLtxaffd9hurvtnbXGpZuXrYAYx-5U4u3M40/edit#gid=1429709856)

**Approach:**

- Examine SLA performance indicators such as FRT/NRT achievement rate and median response times and identify the months or weeks where there was a downward trend.
- Narrow down the performance decline using ticket forms and other attributes.
- Using the Ticket update volume report
  - Correlate the dates with the number of active engineers that were shown to be active that month/week (for example 20 tickets worked on per month per engineer can be considered the target volume).
- Using the Zapier enabled PTO calculator spreadsheet
  - Correlate the dates with the number of IC's on PTO

#### Shaping Actions


If it was identified that PTO impacted our results:

- Determine if additional headcount should be applied on certain dates / days of week.
- Examine our time-off policy and see if it needs to be adjusted - [handbook](https://about.gitlab.com/handbook/support/support-time-off.html).

---

### A single portion of tickets is responsible for decreased FRT results

#### Past Analysis


##### [2020-09-14: A single portion of tickets is responsible for the overall sag in FRT](https://gitlab.com/gitlab-com/support/metrics/-/issues/2)

**Evidence Gathered:**

- 6 Months breakdown per ticket form and problem type [spreedsheet](https://docs.google.com/spreadsheets/d/1kp1VVorywEgYu0_YuMKDMpitSGo4Hjb7zXu-DOt3e0I/edit#gid=169305821)

**Approach:**

- Examine SLA breaches in %, SLA median TTR (Time To Resolve) and the total volume of tickets for each problem type (under the relevant ticket form).
- Compare the results and identify trends and spikes.

#### Shaping Actions


If it was identified that a single portion of our problem types exhibits poor performance (compared to the other problem types).

- Attempt to identify the dates where the volume increased, or the SLA started to decline.
- Identify potential issues that might have impacted our customers or our ability to provide support for these problem types.
- Discuss the decreased performance with the relevant IC's and work with them to try and identify possible blockers and explanations as to why this specific problem type decreased in performance.

---

## Other

### FRT+NRT are below target

### Our staffing isn't spread appropriately vs. the number of tickets that are raised/will breach per hour. We're not asking folks to work the right set of hours

#### Past Analysis

##### [2020-09-15: Our staffing isn't spread appropriately vs. the number of tickets that are raised/will breach per hour. We're not asking folks to work the right set of hours](https://gitlab.com/gitlab-com/support/metrics/-/issues/4)

**Evidence Gathered:**

- [SLA achievement by hour](https://gitlab.zendesk.com/explore/dashboard/3C721536831F0900DBAEBF0052B94FF8D8F3B83114E2D7C27135AA93A31F74FA/tab/12867812)
- [Total number of SLA targets by hour](https://gitlab.zendesk.com/explore/dashboard/3C721536831F0900DBAEBF0052B94FF8D8F3B83114E2D7C27135AA93A31F74FA/tab/12867822)

**Approach:**

- Examine the total number of ticket responses required through the count of achieved SLA updates + breached SLA updates. This takes into account the basic unit of work (a ticket response) and gives a higher-resolution view than a count of tickets.
- Segment ticket responses by hour and by breached/achieved.
- Segment ticket responses by hour and by preferred region of support.

#### Shaping Actions

If it was identified that we're not asking folks to work the right set of hours:

- Ask support engineers to pay more attention to the queues during problematic time periods (e.g. spend the last hour of your day clearing out tickets that will breach in the next 4 hours, encourage crush sessions during that time period, etc.).

If it was identified that our staffing isn't spread appropriately:

- Focus hiring efforts on geographical areas with appropriate daylight coverage to target problematic time periods.
- Consider rebalancing team member ratio between the three major geographic regions (AMER, APAC, EMEA).

<!--
---

### Hypothesis 2 for FRT

#### Past Analysis

#### Shaping Actions

## SSAT is below target

### Hypothesis 1 for SSAT

#### Past Analysis

#### Shaping Actions

## NRT is below target

### Hypothesis 1 for NRT

#### Past Analysis

#### Shaping Actions

---
-->
