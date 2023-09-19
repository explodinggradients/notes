---
title: "Handbook Roadmap"
description: Documents development plans for the handbook
---

## Introduction

This page will be for documenting and sharing plans for the handbook in true GitLab fashion: [iteratively](/handbook/values/#iteration)
and [transparently](/handbook/values/#transparency). Like the handbook overall, this roadmap will *always* be a work in
progress—a [living document](https://en.wikipedia.org/wiki/Living_document).

Everyone is welcome to browse and contribute to our [open handbook issues](https://gitlab.com/gitlab-com/content-sites/handbook/-/issues).
If there's something you'd like to report or something you'd like to see on this roadmap then please don't hesitate to
[open a new issue](https://gitlab.com/gitlab-com/content-sites/handbook/-/issues). Contributions are welcome and
appreciated!

## Ongoing work

Small improvements such as link updates and text tweaks are constantly being made, but small changes can be made as
quickly as updating the roadmap, so they don't need to be mentioned here unless they are part of a larger effort.

## Roadmap

| What                                   | When                     | Status    |
|----------------------------------------|--------------------------|-----------|
| Handbook Migration                     | March 2023 to March 2024 | Ongoing   |
| Handbook AMA Livestream                | October 2023             | Planning  |
| Handbook Issue Triage Livestream       | October 2023             | Planning  |
| Handbook Client-side Features          | December 2023            |           |
| Handbook Search Improvements           | TBC                      |           |
| New Team and Pets Site                 | TBC                      |           |

### Handbook Migration

After years of exponential growth and evolution and the significant accumulation of technical debt the decision was taken
to migrate the Handbook from `www-gitlab-com` to its own repository and rearchitect how the handbook is generated.
Where as previously the handbook was generated using [Ruby](https://www.ruby-lang.org/) and
[Kramdown](https://kramdown.gettalong.org/index.html) the new handbook is generated using [Hugo](https://gohugo.io/).
This change has significantly decreased the time it takes to generate the site and get changes to the Handbook published.

Migrations are seldom easy.  There is 12 years worth of commit history as well as almost 3000 pages worth of
content with changes and updates being made every day.  This has necessitated an iterative approach to migrating the
handbook.  We've broken the Handbook down in to sections, weighted those section by complexity of the migration and
produced the following Timetable.  During this time content will be split between [https://about.gitlab.com](https://about.gitlab.com)
and [https://handbook.gitlab.com](https://handbook.gitlab.com).

For more details see the [Migration Timetable and Status](#migration-timetable-and-status) section below.

### Introduce Handbook AMA Livestream

The handbook is both a living document and an actively developed web site.  GitLab features are  also constantly being
tried out on the Handbook.  There is a plan to introduce a Ask Me Anything about the Handbook in keeping with our
commitment to our [values](/handbook/values).  This will be a once a month 25 minute livestream initially where people
can ask anything relating to the handbook.

### Introduce Handbook Issue Triage Livestream

To increase [transparency](/handbook/values/#transparency) of how Handbook issues and requests get treated its planned
to introduce a new fortnightly livestream where the issues are gone through, commented on and prioritized.  Any on going
issues will also get updates talked about.

### Client-side Features

The Handbook is a statically generated site by there are times when we need to put out notifications about pages or
on-going work.  The recently lead to the introduction of notifications to the handbook.  This was done primarily to
advise of the ongoing Handbook migration work.  There are plans to build on this to notify of deprecated pages, to
allow a watch list of pages and other client-side features.

### Handbook Search Improvements

Currently there is no combined search between [https://about.gitlab.com](https://about.gitlab.com)
and [https://handbook.gitlab.com](https://handbook.gitlab.com) and the internal handbook.  Additionally the handbook
search feature on [https://handbook.gitlab.com](https://handbook.gitlab.com) is Client Side powered using a script
called Luna.  The vision is that searching the Handbook should be simple and accessible.  Once the migration is completed
the next significant bit of work will be to improve search across the handbooks.

### New Team and Pets site

The current Team and Pets pages in company are quite complex and have not been included in the handbook migration as
these pages aren't really handbook content.  So a decision has been taken to split these pages in to their own site
once the migration has been completed.  This may include other elements such as the compensation calculator and the
organisation chart as well as using WorkDay as the Single Source of Truth for team data.

## Migration Timetable and Status

{{% include "includes/migration-timetable.md" %}}

### Migration calendar

We are providing a Google Calendar with all the dates for the migration in.  This also includes public holidays and notable dates for the US and UK and other dates important to the migration team.

<iframe src="https://calendar.google.com/calendar/embed?src=c_618947374a015de8e6dc270caa157b5d19eb591f3b3dd791200ed02aac0a76e3%40group.calendar.google.com&ctz=Europe%2FLondon" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

If the above iFrame is blank you can also access the [Calendar Directly](https://calendar.google.com/calendar/embed?src=c_618947374a015de8e6dc270caa157b5d19eb591f3b3dd791200ed02aac0a76e3%40group.calendar.google.com&ctz=Europe%2FLondon).

### Why this order

The order is based largely on the table of contents for the handbook but its been weighted slightly so that those sections with lots of Ruby Template files (`erb`) are pushed to the bottom of the list.  The idea is that content which is easier to move is the content which moves first.  This will give more time for those teams who are using ruby templating to move their content to markdown.  Where content can't be easily moved to Markdown this will give the Handbook team time to work with teams to find and develop solutions to meet their needs.

We also hope to run in parallel the migration of the Engineering content from the existing handbook to the new handbook which we hope will reduce the time it takes to migrate all of the content from `www-gitlab-com`.  If we are unable to do this we'll still migrate engineering after Company Handbook Content.

### Dates and order subject to change

This is the order we have identified to migrate content but it is subject to change based on factors such as operational need and how smooth the migration goes for each section.  We won't hesitate to bring forward a migration date if the current piece of content has moved smoothly and quickly.  We'll also communicate changes in [#whats-happening-at-gitlab](https://gitlab.slack.com/archives/C0259241C) and [#handbook](https://gitlab.slack.com/archives/C81PT2ALD) on Slack.

### Migration Status

#### What is moving next?

**What are we moving:** Security

**Status** Expected to complete: 2023-09-08

#### What content is moving

The following content has been earmarked as the next content to move.  This will be done as a pair of large merge requests on `2023-09-05`.  The content will then be checked, markdown errors fixed and merged in to the new handbook.  The content on the about site will be removed and redirects setup `2023-09-08`.

- [ ] Organizational Change Management
- [ ] Security

#### How will this be done

We hope to do this as a series of small MRs over the course of a week.  Each of these sections is typically only a page or two.  So we shall one small section at a time over the course of 4 days.  Each move is a pair of MRs.  One brings the content over to the new handbook while the other removes the content from `www-gitlab-com` and sets up a redirect to the new content.

If you have any questions about this please feel free to ask in [#handbook](https://gitlab.slack.com/archives/C81PT2ALD) on Slack or reach out directly to @jamiemaynard.

### The break down of whats moving

#### Job Families

*Completion Date:* 31st March 2023

**Content to move:**

- [x] Job Families

#### TeamOps

*Completion Date:* 21st April 2023

**Content to move:**

- [x] TeamOps

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#teamops)

#### Company Handbook Content

***Expected Finish Date:*** 11th August 2023

***Content to move:***

- [x] Values
- [x] Being a public company
- [x] Communication
- [x] Handbook
- [x] Key Reviews
- [x] Group Conversations
- [x] E-Group Weekly
- [x] Sustainability
- [x] About the handbook
- [x] Content Websites Responsibility
- [x] Style-Guide
- [x] Inspired By Gitlab
- [x] Executive Business Administrators

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#company-handbook-content)

#### Tools and Tips

**Completed:** 16th May 2023

**Content to move:**

- [x] Tools and Tips

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#tools-and-tips)

#### Infrastructure Standards

**Completed:** 9th June 2023

**Content to move:**

- [x] Infrastructure Standards

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#infrastructure-standards)

#### IT Self Service

**Completed:** 9th August 2023

**Content to move:**

- [x] IT Self Service

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#it-self-service)

#### Support

**Completed** 14th August 2023

**Content to move:**

- [x] Support

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#support)

#### CEO and CoST Team

**Completed:** 2023-08-18

**Content to move:**

- [x] CEO pages
- [x] CoST Team Pages

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#ceo-and-cost-team)

#### Company

**Completed:** 2023-09-01

**Content to move:**

- [x] Company
- [x] Friends and Family Days
- [x] History
- [x] KPIs
- [x] Mission
- [x] Offsite
- [x] OKRs
- [x] Purpose
- [x] Strategy
- [x] Top Cross Functional Initiatives
- [x] Structure
- [x] Working Groups

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#company)

#### Security

**Expected Date:** 2023-09-08

**Content to move:**

- [ ] Organizational Change Management
- [ ] Security

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#security)

#### Culture

**Expected Date:** 2023-09-21

**Content to move:**

- [ ] Company Culture

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#culture)

#### Finance

**Expected Date:** End of September 2023

**Content to move:**

- [ ] Board Meetings
- [ ] Finance
- [ ] Internal Audit
- [ ] Spending Company Money
- [ ] Stock Options
- [ ] Tax

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#finance)

#### Product

**Expected Date:** End of October 2023

**Content to move:**

- [ ] Acquisitions
- [ ] Business Technology
- [ ] Product
- [ ] Product Development

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#product)

#### People Group

**Expected Date:** End of October 2023

**Content to move:**

- [ ] Anti-Harassment
- [ ] Entity
- [ ] Hiring
- [ ] Incentives
- [ ] Labor and Employment
- [ ] Leadership
- [ ] Paid Time Off
- [ ] People Group
- [ ] Total Rewards
- [ ] Travel

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#people-group)

#### Marketing

**Expected Date:** End of November 2023

**Content to move:**

- [ ] Marketing
- [ ] Use-Cases

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#marketing)

#### Sales

**Expected Date:** End of November 2023

**Content to move:**

- [ ] Alliances
- [ ] Customer Success
- [ ] Resellers
- [ ] Sales

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#sales)

#### Legal

**Expected Date:** End of December 2024

**Content to move:**

- [ ] DMCA Policy
- [ ] GDPR Policy
- [ ] Legal

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#legal)

#### Engineering

**Expected Date:** End of February 2023

**Content to move:**

- [ ] Developer Onboarding
- [ ] Engineering

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#engineering)

#### Team

**Expected Date:** End of February 2023

**Content to move:**

- [ ] Team Pages
- [ ] Team Pets

A full breakdown of this sections content files can be viewed on our [Migration details page](/handbook/about/migration-details/#team)

### Refactor and move data

**Target Date:** End of Q4 2023

#### Why move data

The contents of the `www-gitlab-com` data directory is a Source of Truth in its own right.  It is shared by a number of functions of the `www-gitlab-com` repository as well as the `internal-handbook`, `digital-experience` and the new `handbook` .  This represents a significant dependency for all these repositories and the content they drive.

Like the refactor of `www-gitlab-com` refactoring data will allow this dependency to have a single DRI and provide a single place where all repositories which depend on this data to call on.  Data will be benefit from faster pipelines and changes to data can quickly propagated to those repositories that depend on them.

#### Status

This is currently in the planning stages and we'll share more as soon as we can.
