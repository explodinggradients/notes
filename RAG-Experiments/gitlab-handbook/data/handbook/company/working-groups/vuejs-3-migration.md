---
title: "Vue.js 3 Migration Working Group"
description: "Learn more about the Vue.js 3 Migration Working Group attributes, goals, roles and responsibilities."
status: active
---

## Attributes

| Property          | Value                                                                                                                                     |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Date Created      | 2023-02-10                                                                                                                                |
| Target End Date   | 2023-10-31                                                                                                                                |
| Slack             | #wg_vue3_migration (only accessible from within the company)                                                                              |
| Google Doc        | [Agenda](https://docs.google.com/document/d/1Ad8mbz5HzMsBI2sR6DgQ34afOn1L1OJy5m_RrrpXaqE/edit) (only accessible from within the company) |
| Epic              | [Link](https://gitlab.com/groups/gitlab-org/-/epics/6252)                                                                                 |
| Overview & Status | See [Exit Criteria Progress](#exit-criteria-progress)                                                                                     |

### Context

[Vue.js 3](https://vuejs.org) is the latest version of the frontend framework used by GitLab.

With [2023-12-31 Vue.js 2](https://v2.vuejs.org/lts/) (which is currently the version used by GitLab) reaches official end-of-life, including security updates and browser compatibility which might affect entire GitLab users.

Additionally, current GitLab codebase relies on subset of libraries which were not updated to be compatible with Vue 3 which might pose additional risks during migration.

We want to ensure that we are not creating additional security risks for our users by using an unmaintained version of a framework. At the same time increasing developer productivity by using new features of the latest version of the framework. Also an upgrade to Vue.js 3 hopefully will result in performance gains through out the application of 20-30% and most probably even more for heavy frontend applications like Code Review for example.

### Exit Criteria

This Working Group has the following goals:

1. Ensure all GitLab projects (including, but not limited to GitLab.com, customers portal, status page, etc.) are using latest Vue.js version
1. Develop & Socialize upgrade strategy for Vue.js 3.
   1. Identify dependencies which are blocking upgrade and ensure that decisions regarding these dependencies will be taken in timely fashion.
   1. Ensure visibility of upgrade process on per-application level
   1. Promote new patterns and update handbook with guidelines appropriate for new framework version
1. Develop a Rollout Strategy and Plan for gradual migration
   1. Create tooling and proper infrastructure to be able to use both framework versions in production during migration process.
   1. Ensure our test suite could be run using both versions of Vue.js to embrace values of iteration of results and allow gradual migration of codebase to Vue.js 3
   1. Implement compatibility layer for unifying differences between framework versions
   1. Create automated tooling (where applicable) to migrate existing Vue.js 2 code to be compatible with latest framework version
   1. Create deprecation strategy for patterns and solutions which are not compatible with Vue.js 3 to rest of the teams
1. Develop and implement a communication plan for the outcomes of the working group.

#### Exit Criteria Progress

| Criteria                                                                                      | Start Date | Completed Date | Progress | DRI     |
| --------------------------------------------------------------------------------------------- | ---------- | -------------- | -------- | ------- |
| Use Vue.js 3 for running test suites                                                          |            |                | 0%       | `@you?` |
| Vue.js 3 upgrade tasks and testing for all groups available                                   |            |                | 0%       | `@you?` |
| Vue.js 3 upgrade tasks and testing by all groups completed.                                   |            |                | 0%       | `@you?` |
| [Use @vue/compat for Vue-related projects](https://gitlab.com/groups/gitlab-org/-/epics/9013) |            |                | 0%       | `@you?` |
| Drop Vue.js 2 support                                                                         |            |                | 0%       | `@you?` |

### Roles and Responsibilities

| Working Group Role | Person                | Title                                                             |
| ------------------ | --------------------- | ----------------------------------------------------------------- |
| Executive Sponsor  | Tim Zallmann          | Senior Director of Engineering                                    |
| Co-Facilitator     | Martin Wortschack     | Engineering Manager, Manage:Import                                |
| Functional Lead    | Illya Klymov          | Senior Frontend Engineer, Manage:Import                           |
| Functional Lead    | Natalia Tepluhina     | Principal Engineer, Plan                                          |
| Functional Lead    | Stanislav Lashmanov   | Senior Frontend Engineer, Create: Code Review                     |
| Functional Lead    | Andrew Fontaine       | Senior Frontend Engineer, Release                                 |
| Member             | Mark Florian          | Staff Frontend Engineer, Manage:Foundations                       |
| Member             | Laura Meckley         | Frontend Engineer, Fulfillment::Billing & Subscription Mgmt       |
| Member             | Andrei Zubov          | Frontend Engineer, Release                                        |
| Member             | Artur Fedorov         | Senior Frontend Engineer, Secure                                  |
| Member             | Frédéric Caplette     | Senior Frontend Engineer, Verify:Pipeline Authoring               |
| Member             | Eduardo Sanz Garcia   | Senior Frontend Engineer, Manage:Authentication and Authorization |
| Member             | Ross Byrne            | Fullstack Engineer, Growth:Acquisition                            |
| Member             | Samantha Ming         | Senior Frontend Engineer, Govern:Threat Insights                            |
