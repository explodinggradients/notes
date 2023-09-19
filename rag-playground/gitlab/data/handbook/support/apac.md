---

title: Support Team APAC
description: Support Team APAC home page
---

## Welcome to Support Team APAC's Handbook page

This page documents items specific to Support Team APAC which we have not yet
found a home for in the wider Support Team Handbook.

The intent is to enable APAC Support team members to contribute to Results for
APAC-specific iniatitives, policies, processes and workflows by prioritizing:

1. Transparency, through being [handbook first](https://about.gitlab.com/handbook/handbook-usage/#why-handbook-first)
   and providing a single source of truth for APAC-specific.
1. Iteration, through providing a safe space where APAC Support team members can
   introduce or update APAC-specific policies, workflows and processes without
   creating confusion and uncertainty for the wider Support Team.

Where appropriate, we should always look to move content from this page into
other pages of the wider Support Team Handbook. For an example of how this can
be done, see the [Considerations in APAC section](https://about.gitlab.com/handbook/support/on-call/#considerations-in-apac)
of the GitLab Support On-Call Guide Handbook page.

## General policies

### Support Team APAC is One Team

- APAC Support Readiness department members are part of Support Team APAC too.
- Avoid calling individual manager's direct reports group "my team" or "your team".

### Support engineers should be able to work across all GitLab product platforms

- Support engineers should be willing and able to work on problems for all
  platforms supported by GitLab: SaaS, Dedicated and Self-Managed.

### Support engineers should spend time on work other than L&R work

- ???

## Working principles

Working principles are behaviors that empower team members to carry out the
work of Support Engineering in alignment with the needs of our customers and
our business. They help illustrate what applying GitLab's core values and
operating principles to Support work looks like.

These working principles are complementary to and should be subordinate to
GitLab's core values and operating principles. In case of a conflict between
the two, please create an MR to propose a change to or removal of the working
principles.

### Solve tickets faster

Solving tickets faster can lead to better customer outcomes, and frees up time
for Support team members to do what the team needs or what they want, such as
new tickets, training or code contributions. These questions might help you
apply this operating principle:

- Is what I'm currently doing helping me to solve this ticket faster?
- If we stop or remove a process, will it help us to solve tickets faster?
- Will my ideas and efforts lead us to solve tickets faster as a team?

As we learn more about this operating principle, please leave any thoughts or
feedback in the [discussion issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/4921).

## Operating metrics and measurements

### Cliff of definite underperformance

A support engineer is definitively underperforming when they handle less than 7 tickets in any of 3 of the past 4 weeks.
{: .alert .alert-warning}

A support engineer is considered to have handled a ticket when they leave either
a public or internal comment on a ticket.

**Purpose**

To set clear expectations of when a support engineer's ticket productivity is
so low that they are no longer performing the basic responsibilities of the
role.

<div class="panel panel-warning">
**Warning**
{: .panel-heading}
<div class="panel-body">

If you are above the cliff, it does not necessarily mean that you are meeting
ticket productivity expectations. The full picture of ticket productivity
performance cannot be derived from a single number and must be looked at
holistically with other quantitative and qualitative inputs.

</div>
</div>
{::options parse_block_html="false" /}

**Frequency**

Support engineer productivity should be checked against the measurement on a
weekly cadence.

The measurement itself should be updated on a quarterly cadence, at the start of
each financial quarter.

<details>
  <summary markdown="span">Historical data</summary>

- FY23-Q1: 5
- FY23-Q2: 5
- FY23-Q3: 5
- FY23-Q4: 5
- FY24-Q1: 6
- FY24-Q2: 7

</details>

<details>
  <summary markdown="span">Design considerations</summary>

  The following considerations were made while designing this measurement:

- It should include both direct contributions and collaborative work on tickets.
- It should be easy to remember and keep track of.
- It should be naturally achieved in the normal course of work and not require
    special effort or focus.

</details>

<details>
  <summary markdown="span">Getting the measurement</summary>

  Use the following instructions to set up a Zendesk Explore report which you
  can use to get the Cliff of Definite Underperformance number at the start of a
  new financial quarter.

  **Building the Zendesk Explore report**

  Create a Zendesk Explore report using the `Support - Updates History` dataset.
  Use the following settings:

  1. Metrics:
     - D_COUNT(Tickets updated)
     - D_COUNT(Tickets updated w/comment)
  1. Rows:
     - Updater name
     - Updater region (optional, used to verify that data from outside of APAC is not present)
     - Update - Year
     - Update - Week of Year
  1. Filters:
     - Ticket form - Excluded:
       - L&R (This is excluded because weekly L&R productivity numbers can get very high. Setting a standard derived from this number is unfair to support engineers who do not regularly do L&R.)
     - Updater tags - Selected:
       - `jane_gianoutsos`
       - `ket_slaats`
       - `wei-meng_lee`
     - Comment type - Selected:
       - Internal
       - Public
  1. Visualization type: Table
  1. Result manipulation
     - Result path calculation - D_COUNT(Tickets updated)
       - Pattern: Percentile
       - Path: On rows

  **Getting the measurement from the Zendesk Explore report**

  In the Zendesk Explore report:

  1. Update the date range filter:
     1. Click on `Update - Week of Year`.
     1. Click on "Edit date ranges".
     1. Under the "Date range" pane, click on the "Simple" tab.
     1. Select the "Custom" radio button.
     1. Select "month" in the "Details level" select dropdown.
     1. Select the previous 12-month period ending at the last FY quarter.
     1. Click on "Apply".
  1. Sort the `Tickets updated` column.
  1. Look for the first entry above 15%.
  1. The cliff number will be the value of `Ticket updated w/comment` in that row.

</details>

<details>
  <summary markdown="span">Monitoring the measurement</summary>

  Use the following Zendesk Explore report to provide reporting of how
  individual support engineers' productivity matches up against the Cliff of
  Definite Underperformance.

  **Building the Zendesk Explore report**

  Create a Zendesk Explore report using the `Support - Updates History` dataset.
  Use the following settings:

  1. Metrics:
     - D_COUNT(Tickets updated)
  1. Columns:
     - Update - Year
     - Update - Week of year
       - Filter > Edit date ranges > Advanced:
         - From the beginning of: 4 weeks in the past.
         - To the end of: 1 weeks in the past.
  1. Rows:
     - Updater tags
       - Filter - Selected:
         - `jane_gianoutsos`
         - `ket_slaats`
         - `wei-meng_lee`
     - Updater name
  1. Filters:
     - Comment type - Selected:
       - Internal
       - Public
  1. Visualization type: Table
  1. Chart configuration > Display format:
     - D_COUNT(Tickets updated) > Advanced:

       ```zendesk
       IF (D_COUNT(Tickets updated) >= 7) THEN
       {
           "backgroundColor": "",
           "precision": 0,
           "scale": 1,
           "prefix": "",
           "decimalSeparator": ".",
           "italic": FALSE,
           "bold": FALSE,
           "suffix": "",
           "fontColor": "",
           "thousandsSeparator": " "
       }
       ELIF (IS_NAN(D_COUNT(Tickets updated))) THEN
       {
           "backgroundColor": ""
       }
       ELSE
       {
           "backgroundColor": "#ffcccb"
       }
       ENDIF
       ```

</details>

## Daily Bot in the #support_licensing-subscription slack channel

There is a daily bot that follows the SGG bot format and tags all APAC Support
engineers who have a Focus `name: License and Renewals` listed in their [Support Team Page](https://gitlab.com/gitlab-com/support/team/-/blob/master/data/support-team.yaml) entry.

Example Support Team Bot post:

> *Support Team Bot
Morning APAC @name1 @name2 @name3 @name4 @name5 @name6 @name7. Today we have:  7 working, 1 on PTO:*
>
> *The following people have scheduled PTO:*
> ** Wednesday: @name8*

Support engineers update this post's thread daily to share with each other when
they are covering the queue, so that team members are confident that there are eyes
on the queue when they complete their scheduled time to action these tickets. There
is no strict roster, team members opt-in and share their availability to achieve
coverage.

## Holiday Coverage Planning

We are mindful of [holidays](https://about.gitlab.com/handbook/support/support-time-off.html#holiday-time-off-ticket-management) that impact large parts of the team. The following are official holidays for mostly APAC team members, which we plan coverage for outside of global practices:

| **Holiday**                             | **Date**           | **Countries**              | **Notes**                                                                                                                                  |
|-----------------------------------------|--------------------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| - Australia Day<br>- India Republic Day | 26th January       | Australia, India           | Full region impact as this impacts both our Group 1 and Group 2 on-call coverage.                                                           |
| Easter Friday                           | Movable            | Australia, NZ, Philippines |                                                                                                                                            |
| Easter Monday                           | Movable            | Australia, NZ, Philippines |                                                                                                                                            |
| ANZAC Day                               | 25th April         | Australia, NZ              | Let AMER know in time for the Friday prior due to no coverage for first 2-5 hours of business hours on a Monday.                           |
| Monarch's Birthday                      | 1st Monday in June | NZ                         | Let AMER know in time for the Friday prior due to no coverage for first 2 hours of business hours on a Monday. |
| Monarch's Birthday                      | 2nd Monday in June | Australia (except QLD)     |                                                                                                                                            |
| Independence Day                        | 12th June          | Philippines                | Be aware that this can coincide with Australia's observation of Monarch's Birthday when June 12 is a Monday.                               |

To refer to past planning issues, see issues linked to the [[APAC] Holiday Coverage Planning Issues epic](https://gitlab.com/groups/gitlab-com/support/-/epics/252).

## Regular Sync Sessions

<table>
  <thead>
    <tr>
      <th>Weekly</th>
      <th>Bi-Weekly/Fortnightly</th>
      <th>Monthly/Irregular</th>
   </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>APAC Crush</li>
          <li>EMEA/APAC Crush</li>
          <li>Support Team Call</li>
          <li>L&R Meeting</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Anton Sm's Office Hours</li>
          <li>Julian's Kubernetes Help Sessions</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>APAC/AMER Crush</li>
          <li>Release Review Party</li>
          <li>APAC Office Hours</li>
          <li>Social Call</li>
          <li>APAC Book Club - [Tribal Leadership](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/4854) <br>weekly between 2023-02-16 to 2023-04-06</li>
         </ul>
      </td>
    </tr>
  </tbody>
</table>

- ???
