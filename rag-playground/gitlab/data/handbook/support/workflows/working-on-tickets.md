---
title: Working on Tickets
category: Handling tickets
description: How to find, select, assign and begin work on support tickets
---

## Introduction

The focus of this page is to be a guide for Support Engineers in
[finding](#views-to-use-in-our-sgg-system),
[selecting](#selecting-tickets), [assigning](#assigning-tickets) and
[beginning work](#providing-a-first-response-to-a-ticket) on support tickets.
For information about working on tickets successfully in the Support Global
Groups environment, please read the
[SE Responsibilities and Priorities](/handbook/support/support-global-groups/#se-responsibilities-and-priorities)
topic on the main Support Global Groups page.

## Views to use in our SGG system

The views within Zendesk are arranged as follows:

| Name | Purpose |
|------|---------|
| [My Assigned Tickets](https://gitlab.zendesk.com/agent/filters/360062369834) | Use this view to manage all of your assigned tickets that are not yet in a `Closed` state. |
| SGG: [group name] | You'll see an alphabetical list of group views here. Each view shows all the non-solved, non-pending tickets for its group. |

## Selecting tickets

Support Engineers should make decisions about what to work on based on the SGG
description of [prioritizing work](/handbook/support/support-global-groups/#prioritizing-work).
Through that process you may:

1. Select a new, unassigned ticket in your group's view using the following approach:

   a. Prioritize paid High priority tickets in your SGG FRT stage view first, even if it is further down the line from “next-to-breach”.

   NOTE: Free user tickets submitted as High priority are the exception. All free user tickets should be prioritized last.

   b. If there aren’t any new High priority tickets, work with your group to assign any *unassigned* High NRT’s.

   c. If all High NRT's are assigned, focus on your assigned High priority NRTs.

   d. If all High priority tickets are addressed, help with Normal or Low priority tickets that are at risk of breaching.

   e. If the next Normal or Low priority ticket to breach is > 4 hours, focus on your NRTs, your group's NRTs, and finally free user tickets (tickets with no SLA).

   Proceed to
   [ticket assignment](#assigning-tickets)

1. Select a new, unassigned ticket in another group's view

   In this situation, follow the guidance in the SGG FAQ to
   [move the ticket to your group](/handbook/support/support-global-groups/sgg-faq.html#3-how-do-i-move-a-ticket-to-a-different-group)
   before proceeding to [ticket assignment](#assigning-tickets)

1. Select an in-progress ticket assigned to someone else

   In this situation, proceed according to the guidance in our SGG FAQ about
   [responding to other SEs’ tickets](/handbook/support/support-global-groups/sgg-faq.html#1-should-ses-respond-to-other-ses-tickets).

## Assigning tickets

When you begin work on a new ticket, as your first step please assign the ticket
to yourself using the `take it` button. In the SGG environment, that shouldn't
prevent anybody from collaborating with you on the ticket. What it ***will*** do
is signal that you're the DRI for providing a great customer experience, as the
ticket progresses towards `Status: Solved`. This enables other team members
seeking to assign themselves New ticket/s from the queue, to move on to reviewing
the next New unassigned ticket.

*NOTE: The SLA clock continues to run until you've sent a public response to
the user!*

### Managing the size of your My Assigned Tickets view

As you're working on tickets each day, be aware of the number of tickets in your
`My Assigned Tickets` view, and of their statuses and needs, so that you can
decide whether you have the right number of tickets. There's no specific number.
Aim to take as many tickets as you can while maintaining customer happiness and
good progress toward resolution on each, **and** having some amount of time to
meet [other responsibilities](/handbook/support/support-global-groups/#se-responsibilities-and-priorities).
While some people might maintain three to ten open, pending and on-hold tickets
in their
[My Assigned Tickets](https://gitlab.zendesk.com/agent/filters/360062369834)
view, others might comfortably maintain closer to twenty tickets. Each person
will need to find the right ticket load for themself.

### Helping with a first response without taking assignment

You might at times know that you can provide a good response on a specific new
ticket, and yet not have room to assign it to yourself. Since **every response
should be part of a ticket that is assigned to somebody**, please place an
internal note describing what your first response would be. You might consider
then looking for another person in your group who can take the ticket, and even
offering to pair with them.

If you send out a first response to avoid a ticket from breaching but do not
have the capacity to take assign it to yourself, consider adding an internal note clearly
stating that you are not assigning the ticket. There's no need to justify why
you aren't taking assignment. This clarity will help ensure that someone else
will assume responsibility for moving the ticket forward.  
In order to minimize the mental effort necessary for the next engineer to catch
up with the ticket, consider adding summary of the problem and as much helpful
information and relevant links as you're able to muster to this internal note
in case your first response doesn't speak for itself.
Additionally consider communicating this in your SGG Slack channel, stating that the ticket needs an assignee
to get more attention and speed up the process of finding an assignee.

### Taking a ticket when you know only the first response

You might at times feel prepared to provide a good first response and yet
not prepared to keep the ticket progressing. When that happens, remember you
have your group, and in fact the whole global team, ready to help you drive the
ticket to a great resolution. You're never alone. So go ahead and accept the
challenge! Assign the ticket to yourself, send out your first response, and
seek help as soon as you need it.

### Assigning and handling tickets which have a different preferred region in your SGG

#### Pathway for handling high priority tickets from a different region

1. If a ticket is marked as "High Priority" and you have the answer, take assignment of the ticket and offer a solution. If the solution does not resolve the issue, proceed with the steps in [Handing over tickets and customer calls between regions](https://about.gitlab.com/handbook/support/workflows/working-on-tickets.html#handing-over-tickets-and-calls-between-regions).
1. If a ticket is marked as "High Priority" and will not breach the FRT (First Response Time) SLA before an hour after the preferred region's support comes online, consider conducting initial research, and recording your findings as an internal note. Do not assign the ticket to yourself.
1. If a ticket is marked as "High Priority" and there's a risk it might breach the FRT SLA time before the preferred region's support is online, take the assignment, send a substantive response to the requester, and then proceed with the steps in [Handing over tickets and customer calls between regions](https://about.gitlab.com/handbook/support/workflows/working-on-tickets.html#handing-over-tickets-and-calls-between-regions).

#### Pathway for handling normal and low priority tickets from a different region

1. If a ticket is not marked as "High Priority," and you're confident in your ability to resolve it, follow these steps:
      - Take assignment of the ticket and prepare the first technical response.
      - Use the ZD macro "clarify preferred region assignment" as part of the first response.
      - If the customer responds and confirms the preferred region, proceed with the steps in [Handing over tickets and customer calls between regions](https://about.gitlab.com/handbook/support/workflows/working-on-tickets.html#handing-over-tickets-and-calls-between-regions).
      - If the customer is okay with out-of-region support, continue to offer assistance and regularly assess customer satisfaction and technical progress. Consider a handover if the ticket's priority changes or if the customer becomes frustrated.
      - If neither of the above scenarios applies, continue to work on the ticket to find a solution.
1. If a ticket is not marked as "High Priority," and it's at risk of breaching the FRT SLA, and you are not confident in resolving the issue, follow these steps:
      - Take assignment of the ticket.
      - Provide a first technical response to the customer.
      - Proceed with the steps in [Handing over tickets and customer calls between regions](https://about.gitlab.com/handbook/support/workflows/working-on-tickets.html#handing-over-tickets-and-calls-between-regions).

#### Pathway for handling tickets handed over from a different region

1. Review the progress of the ticket and check the NRT (Next Response Time) SLA.
   - If you know how to proceed with the ticket:
      - Introduce yourself to the customer, confirm the handover, and provide the next technical response.
   - If additional research is necessary:
      - Introduce yourself to the customer and set clear expectations that further research and a review of the existing information is required before providing the next technical response.

## Providing a first response to a ticket

It's always a good idea when beginning work on a ticket to perform a few routine
steps that can help you to provide a good solution that meets the customer's
needs, and that might save you and the customer time and effort as well.

1. **If you take none of the other steps described in this topic, take this one.
   It is the one most likely to get you very quickly on the right path.**

   Confirm with the customer your understanding of their situation, needs, and
   problem to be solved or question to be answered.
   1. If you're not confident about one or more of these, consider making your
      entire first response a request for clarification **or** a request to
      schedule a quick (15 minute?) meeting solely for clarifying things.
   1. Otherwise, include a quick summary of your understanding near the
      beginning of your response.
1. Look at other current and recent tickets from this customer to find:
   1. Is this ticket related to any of those in any way?
   1. Is there background information in those tickets that give you potentially
      useful information about the customer or their environment? Be sure to
      confirm with the customer that any environmental information is still
      correct and applicable.
   1. Are there any logs you might be able to reuse? Again, confirm their
      relevance with the customer.
1. If there is an organizational note attached to the customer's organization
   in Zendesk, read it carefully for any details about the customer that might
   require you to take specific actions. The note might guide you in how or
   where to communicate with the customer, or provide you with special handling
   instructions, and so on.
1. If the **ticket priority** does not match our
   [Definitions of Support Impact](https://about.gitlab.com/support/definitions/#definitions-of-support-impact),
   inform the customer of the mismatch, suggest the appropriate priority, and
   work to get their agreement. Please consider using the macro
   [General::Changed priority](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/macros/-/blob/master/macros/active/General/Changed%20priority.yaml).
1. If you feel that the ticket has the potential to become an emergency, notify
   the engineer on-call that an emergency might be coming.
1. If you feel that you will need a good amount of time to prepare your first
   response, or if the SLA is about to breach, send an initial and more brief
   response as follows:
    1. Ask any clarifying questions you might have
    1. Explain in brief detail what work you will be doing and by when you will
       update them next. Choose a time that aligns reasonably with the urgency
       of the customer's situation, with your commitments on other tickets, and
       with the actual amount of work you will need to do before responding.
       Be prepared that the customer might respond with a request for you to
       shorten the timeframe. Take a look at this 4-minute video about the
       [SLA Clock](https://www.youtube.com/watch?v=CVue_aHcGlc&list=PL05JrBw4t0Kq13oaMq0DCl2gUz_g1u29o&index=30)
       for further guidance on this workflow.
    1. Submit the ticket as `Open`
    1. Please consider using the
       ['Due Date'](https://handbook.gitlab.com/handbook/support/readiness/operations/docs/zendesk/apps/#zendesk-super-app) and
       ['Reminder'](https://handbook.gitlab.com/handbook/support/readiness/operations/docs/zendesk/apps/#gitlab-reminders-app)
       apps.

## Handing over tickets and customer calls between regions

1. Be sure the ticket is well-documented, including any thoughts you have regarding next steps.
1. Ask in your group's Slack channel for one of the SEs in the target region to assign the ticket to themself, to notify the customer of the transfer and to continue the ticket work where you left off.
1. Visibility: Make sure to use the regional group handle (`@spt-[SGG]-[region]`) so the request is visible for the right group members.
1. CC (@ mention) the [Support Manager on-call](https://about.gitlab.com/handbook/support/on-call/#seeing-which-manager-is-on-call) in the region you want to reach, so they can help ensure the ticket gets assigned.
1. Bonus info: You can also use the Slack ["schedule message"](https://slack.com/help/articles/201457107-Send-and-read-messages#send-or-schedule-messages) feature, to ensure the message pops up within working hours of the intended region.
1. **Until another SE has taken assignment, keep the ticket assigned to yourself and continue to work with the customer.** Be sure to notify the customer that you're working on the transfer.

## Contacting a Customer Success Manager or Account Manager

There are many reasons you may need to bring in a customer's Customer Success Manager (CSM), including but not limited to:

1. Customer needs to discuss their architecture.
1. Customer needs a Professional Services engagement.
1. Customer wants to discuss how best to work with Support.

Depending on the situation, you may need to [STAR]({{< ref "../internal-support/support-ticket-attention-requests.md" >}}) or [start an escalation]({{< ref "emergency-to-escalation-process.md" >}}).
Please refer to the appropriate workflow for those situations.

In the case there is no CSM, contact the Account Manager (AM) - job title varies, Zendesk label is "Account Owner".

If you need to involve the CSM or AM in the conversation, you can use one or more of the following approaches:

1. Add the CSM/AM to the Zendesk ticket as a CC, and let the customer know you've done this. Leave an internal note for additional context if needed.
1. Notify the CSM/AM through Slack, in one of the following ways:
   1. If there is an existing thread discussing the ticket, `@` mention the CSM/AM to add them to the discussion, including a summary in your message for a long thread.
   1. Look for a customer channel (`#a_customerName-internal`) and start a new thread, mentioning the CSM/AM.
   1. Mention the CSM/AM on a new message in the most relevant Support channel: `#spt_managers`, `#support_gitlab-com`, or `#support-self_managed`.

## FAQ

### 1. How many new tickets should I pick up each week?

Each week, every Support Engineer should aim at least to meet, and preferably to exceed, [the
appropriate baseline](/handbook/support/support-engineer-responsibilities.html#ticket-baseline) from the following list for the number of first responses:

- **Self-managed: 6 tickets**
- **SaaS: 7 tickets**
- **SaaS Accounts: 8 tickets**
- **L&R: 24 tickets**

The aim is to ensure equitable ticket distribution among team members. These
numbers are based on ticket volume, number of SEs, and average PTO (15%). We
will continue to monitor ticket volume and number of SEs to make sure the above
guidelines are accurate.

#### What if I can't meet baseline?

There will be times when you may be leading an escalation, working through challenging tickets or focus on non-ticket work and you cannot take on new ticket assignment. This is okay! The key is to make sure you have coordinated with your SGG and Manager so they are aware of the risks to our team.

### 2. What can I do when I'm stuck and I really need help?

   Follow the [how to get help workflow](/handbook/support/workflows/how-to-get-help.html)
   for guidance on this. Reach out to a manager for guidance if you are still
   stuck.

### 3. I'm going to be absent, what do I do with my assigned tickets?

   Please see the [Support Team Member Time Off page](/handbook/support/support-time-off.html)
   for a full description of this situation.

### 4. The customer is absent and wants to keep the ticket open until they're back

   The best course of action in this case is to acknowledge the customer's wish with a public response
   and then set the ticket to **On-Hold** *and* change it to type **Task** with a reminder for yourself
   to check in with the customer x days after their planned return.
   This way, the ticket will permanently stay **On-Hold** for the duration of the customer's absence. See
   [Behavior of `On-Hold` tickets](/handbook/support/workflows/zendesk-ticket-basics.html#behavior-of-on-hold-tickets)
   for details.

### 5. May I reassign a ticket to someone else?

   There are some situations in which it is appropriate to reassign a ticket:

   1. If you'll be absent, follow the guidance given on the
      [Support Team Member Time Off page](/handbook/support/support-time-off.html).
   1. If you've determined that specific expertise outside your own is required
      to resolve the ticket, pair with an expert so that you can get the ticket
      resolved and learn in the process. If that person determines that they
      need to take the lead due to the advanced or complex nature of the
      problem, then:

      1. send a message to the customer informing them that you’ve asked
         another support engineer with relevant expertise to take the ticket,
         that you’ve reviewed the ticket with that engineer, and that you'll
         stay involved in order to help in any way you can
      1. assign the ticket to the expert

   1. If you've become overloaded with tickets, you may look to find one or more
      other SEs to take some of your tickets. Start with your Support Global
      Group, and then look to the larger team if necessary. Be sure you
      discuss each ticket before reassigning it to gain agreement and so that
      the other support engineers don't have to start from scratch. Then add an
      internal note stating the reassignment agreement **and** add a public
      meessage informing the user that you’ve asked another support engineer to
      take the ticket due to your time constraints.

### 6. A customer has confirmed a ticket can be closed but the ticket has no assignee - what should I do?

   This should only happen on rare occasions since in the SGG system all tickets
   should be assigned from the time the first response is made. When it does
   happen, please:

   1. inform the customer that you are changing the ticket status to solved
   1. assign the ticket to the engineer who provided the solution, or if you
      can't make that determination, assign it to an engineer who has
      significantly contributed to the ticket throughout its life cycle

### 7. How many issues or incidents should I handle in a single support ticket?

   As detailed in [Support General Policies](https://about.gitlab.com/support/general-policies/#we-handle-each-incident-within-a-single-support-ticket) it is GitLab's policy to handle each unique issue or incident within a single support ticket.

### 8. How can I open a new ticket on behalf of a customer?

   As detailed in the [Support General Policies](https://about.gitlab.com/support/general-policies/#we-handle-each-incident-within-a-single-support-ticket) it is GitLab policy to handle each individual incident, problem or issue within a single support ticket. If a situation arises where you need to open a new ticket on behalf of a customer then please use the following steps:

1. Go to the [Submit a Request](https://support.gitlab.com/hc/en-us/requests/new) Ticket Portal.
1. Enter the customer's details (Self-Managed or SaaS, email address, subject, problem description etc.).
    - Use the customer's existing Zendesk Ticket to obtain the necessary customer information to complete the form.
1. Once the form is submitted the form will not provide the corresponding ticket id. You can however obtain the new ticket id by performing a search on the customers details such as email address.

Please note: The above approach is required in order to ensure that the ticket is routed correctly and is assigned an SLA.
