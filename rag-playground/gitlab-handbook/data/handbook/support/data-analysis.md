---
title: Support Engineering Data Analysis Community
description:
---

## Purpose

This page serves as the cornerstone for a Support Engineering data analysis
[community of practice](https://en.wikipedia.org/wiki/Community_of_practice).
Support team members who engage in any form of data extraction and analysis,
either out of interest or as part of their work, can use this page to get an
overview of ongoing planning and analysis efforts in the Support team, current
methods of extracting and analyzing data, and figure out who to collaborate with
on specific topics of interest.

As such, this page contains the following information:

- What's being measured, why it's being measured, and the data is retrieved.
- Who's responsible for it.
- Best practices around data collection and analysis.

### How do these metrics differ from Performance Indicators?

The [Customer Support Department Performance Indicators](../performance-indicators/)
are formal metrics used to keep track of how well the Support team is doing as a
whole.

The any parameters and metrics included in this page are for exploratory
and internal planning purposes and should not be used for reporting on
performance.

The Customer Support Department Performance Indicators are the single source of
truth for those indicators and, in the case of conflict, prevails over any the
content on this page.

### How is this related to the Engineering Analytics Team?

The [Engineering Analytics Team](https://about.gitlab.com/handbook/engineering/quality/engineering-analytics/)
formally works on data analysis for the Engineering Division, including Customer
Support.

The Support Data Analysis Community of Practice is made up of people interested
in the application of data analysis to Support work, but may not have this as a
formal part of their role's responsibilities.

## Parameters

### Support time segments

A common set of time segments Support team members can refer to when discussing
topics which are bound to specific periods of the global day, such as support
engineer availability and workload.

- DRI: Wei-Meng Lee ([@weimeng](https://gitlab.com/weimeng))

The support time segments are based on each region's business hours as defined
in [Preferred Region for Support](/support/#effect-on-support-hours-if-a-preferred-region-for-support-is-chosen)
and were chosen to maximise overlap between region's segments, and to align with
periods of high customer messages received per hour.

![Support time segments](support_time_segments.png)

Note that these are time segments and not geographical segments. What's
important is that we have folks available and actively working Support these
hours. For this reason, the time segments were named "Early", "Middle" and
"Late" instead of "East", "Central" and "West" to avoid any association with
geographic locations.

Here are the time segments in tabular form:

| Region      | Anchor TZ | Local start | Local end | UTC start | UTC end | Length  |
|-------------|-----------|-------------|-----------|-----------|---------|---------|
| AMER-Early  | PT        | 05:00       | 09:00     | 13:00     | 17:00   | 4 hours |
| AMER-Middle | PT        | 09:00       | 13:00     | 17:00     | 21:00   | 4 hours |
| AMER-Late   | PT        | 13:00       | 17:00     | 21:00     | 01:00   | 4 hours |
| APAC-Early  | AEST      | 09:00       | 12:00     | 23:00     | 02:00   | 3 hours |
| APAC-Middle | AEST      | 12:00       | 16:00     | 02:00     | 06:00   | 4 hours |
| APAC-Late   | AEST      | 16:00       | 22:00     | 06:00     | 12:00   | 6 hours |
| EMEA-Early  | CET       | 08:00       | 14:00     | 07:00     | 13:00   | 6 hours |
| EMEA-Late   | CET       | 14:00       | 18:00     | 13:00     | 17:00   | 4 hours |

## Metrics

### Customer wait time

"Customer Wait Time" is one of the [Support Department's KPIs](../performance-indicators/#customer-wait-times)
and is defined as the total amount of time the ticket spends in the "Open" and
"New" states over a ticket's life cycle. Life cycle time is measured using
"Total Time To Resolve".

- DRI: Ilia Kosenko ([@Ikosenko](https://gitlab.com/Ikosenko))

In Zendesk Explore, Customer Wait Time can be calculated using:

```zendesk
VALUE(Requester wait time (hrs)) - VALUE(On-hold time (hrs))
```

`Requester wait time (hrs)` is used instead of `Requester wait time - Business hours (hrs)`
because of the following reasons:

- While business hours does not count time elapsed on weekends, it also does not
  count time elapsed outside of a Preferred Region for Support's business hours.
- To align with Time to Resolution measurement, which does not use business
  hours for the same reason above.

Additionally, the median is used for reporting the Customer Wait Time KPI as
this smooths over the extra time captured over weekends by using `Requester wait time (hrs)`
instead of `Requester wait time - Business hours (hrs)`.

We have chosen to exclude the "On-Hold" state from this metric as our view is
that, when used properly, the Support team member handling the ticket would have
agreed with the customer when a next update is to be expected. This means that
the customer is not waiting without knowing when the next reply would come, and
should not be considered as unnecessary wait time.
