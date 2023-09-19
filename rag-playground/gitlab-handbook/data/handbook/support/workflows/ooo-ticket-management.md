---
title: OOO Ticket Management
category: Handling tickets
description: How to manage assigned tickets when going on scheduled PTO
---

## Overview

This workflow covers how support engineers can asynchronously manage and summarize on-going assigned tickets within Zendesk before they go on PTO. It is recommended to follow this workflow if 3 days or more of PTO are planned.

As part of the workflow, the support engineer going on leave will leave notes on currently Open, Pending and On-Hold tickets for their group with a macro. This macro will provide a summary of the ticket, add the support engineer to the ticket's CC list (in case someone else in the SGG group takes over assignment of the ticket), and adds the `ooo_summary` tag to the ticket.

## Workflow

Go to the [My Assigned Tickets](https://gitlab.zendesk.com/agent/filters/360062369834) view in Zendesk. For each ticket you wish to summarize for your group because you anticipate on-going work will be required, do the following:

1. Use the [OOO Ticket Summary](https://gitlab.com/search?search=360080271299&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar) macro.
1. Fill in the sections of the internal note with details for your SGG group. It is important that you summarize:
   1. what is the problem to be solved
   1. what information has been collected
   1. what actions have been taken
   1. what progress has been made
   1. what are the potential next steps, or that you are uncertain what the next steps are

Feel free to also ask group members if they can pickup tickets in [other forms of communication](https://about.gitlab.com/handbook/communication/#multimodal-communication), such as Slack, but Zendesk should remain as the single source of truth for tickets that need attention from other group members.

## Finding your tickets upon your return

After coming back from PTO, if you want to find the tickets that others picked
up from you, start with this search in Zendesk:
`tags:ooo_summary cc:me updated>2021-09-01`. Replace `2021-09-01` with the date
of the last day you worked before going on leave. This may not be 100% accurate
as someone else may have run the `OOO Ticket Summary` macro on a ticket on which
you happened to be CCed, but it will help you to filter out most tickets.
