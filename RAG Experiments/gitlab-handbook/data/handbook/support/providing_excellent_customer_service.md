---
title: Providing Excellent Customer Service
category: References
description: Guidance for delivering a great experience to our customers
---

## Understanding customer needs

If a customer asks a question, make sure you fully understand the reason for
their question and what is the end result they are looking for. There may be a
different and better way to achieve their desired end result, so always feel
comfortable asking 'why'.

## Understanding business impact

While waiting for a resolution to this ticket, is the user's business being
affected?

If you don't know the answer to this, make sure you check with the user early on
in the life of the ticket to prevent the ticket becoming an escalation.
Understanding the timescales the user is working to will help you set
expectations and help them meet or adjust project timescales.

## Managing expectations

When you send a user an update, the normal action is to set the ticket status to
`Pending`, which indicates that you are waiting for a reply from them.

You might consider setting an expectation with the customer that you'll check
back with them after an appropriate amount of time to ensure continued progress.

You may also set the ticket status to `On-Hold`, indicating that you are taking some
action and will follow up with the user at a later time.

When putting a ticket `On-Hold`, you should:

- Inform the user when to expect your follow-up message.
- Invite them to inform you if your chosen schedule does not meet their needs
  so that you can adjust your plans accordingly. See also
  [Understanding Business Impact](#understanding-business-impact).
- Aim to provide updates daily, and no less than every four days, which is the [`On-Hold` period length]({{< ref "zendesk-ticket-basics#behavior-of-on-hold-tickets" >}}).

When setting a ticket to `Pending` or `On-Hold`, consider using our [Due Date](https://handbook.gitlab.com/handbook/support/readiness/operations/docs/zendesk/apps/#zendesk-super-app)
and [Reminders](https://handbook.gitlab.com/handbook/support/readiness/operations/docs/zendesk/apps/#gitlab-reminders-app)
apps to help you to meet commitments you make.

### Avoiding giving concrete answers to "when can I expect feature / fix X?"

During the course of your ticket work you may link back to feature requests and bugs. While an issue with an assigned milestone *may* ship in the release indicated,
do not promise that it will be. See more in our [documentation style-guide](https://docs.gitlab.com/ee/development/documentation/styleguide/#promising-features-in-future-versions).

## Emotionally-charged tickets

When customers are putting negative emotions into ticket communications, refer
to the handbook entry on
[how to keep a ticket moving toward resolution when emotions are getting involved](/handbook/support/workflows/emotionally-charged-tickets.html)
for helpful tips and guidance.

## A ticket is close to breaching; I need more time for my full reply

1. Please send the user a short message to update them on the action plan and
   [set clear expectations](#managing-expectations). Doing this will not only
   prevent an SLA breach, it will very likely be well-received by the user.
   Remember, you don't need to have a full answer in order for your message to
   be useful.
1. When sending the short public reply, set the ticket status to `On-hold` or
   `Open`. `On-hold` is useful when waiting for information from another team.
   `Open` is useful when you want to keep the ticket visible to the rest of the
   Support team.
1. When you take the above action, **keep your commitment and get back to the
   user on time and with a full reply including next steps**. Keep in mind
   that you've stopped the SLA clock, so it's up to you to respond on time. **Do
   not take this action if you are not planning to be the one to follow up.**

## Merging tickets

**WARNING:** Any attached files in the to be merged tickets will be shared
across the tickets. Everyone in CC on both of these tickets will receive the
files.

If you're merging two of a user's tickets that are related or are duplicates, be
sure to send a message letting them know what you've done and why. If you don't,
it often causes confusion and they open follow-ups asking why it was closed
without comment. Please note that your Zendesk signature will not be
automatically applied to this message.

## Splitting tickets

Sometimes, it emerges that a customer is dealing with multiple independent
problems in a single ticket, or a user asks about a different problem in an
existing ticket.

It's recommended to keep tickets focused on a single problem that's clearly
described by the ticket Title. You are encouraged to "split" the ticket
**by creating a new ticket on behalf of the user**.

The new ticket should focus on a single issue and keep the original ticket on
the original issue. This helps reduce time to resolution and makes it easier
for us to focus on fixing the problem at hand.

Please see option 3 in [Requesting Support for Customers](/handbook/support/internal-support/#requesting-support-for-customers) for details on how to create a new ticket.

## Removing Information From Tickets

We ask users to send us logs and other files that are crucial in helping us solve the problems they are experiencing. If a user requests deletion of information shared in a support ticket, or if we suspect sensitive information was accidentally shared, the information can be deleted using the [`Ticket Redaction`](https://www.zendesk.com/apps/support/ticket-redaction/) app.

To delete text or attachments from a ticket:

1. Go to the ticket in question and on the right hand nav bar, scroll down until you are able to locate the Ticket Redaction app.
1. In the text box, enter a string of text or source image URL you wish to redact.
1. If you wish to remove an attachment, you can click on the `Redact Attachment` button and choose the attachment you would like to remove.
1. Let the user know what actions you have taken and why. Request the user to rotate any secrets that may have been shared.

If you don't see the Ticket Redaction App in the sidebar, it is likely that you are not assigned to one of the authorized roles (you can check your role in Zendesk profile). In this case, please reach out to `@support_operations` or `@support-managers` in Slack to request deletion. Zendesk roles that have access to Ticket Redaction App:

- Support Staff - Explore
- Support Staff
- Support Managers
- Administrators

## Handling tickets created by GitLab team members

Every now and then, a GitLab team member will forward a support request from a
customer, prospective customer, user, etc. These requests then appear as tickets
from the team member, instead of from the original requestor.

Always reply directly to the original requester, keeping the person who
forwarded it in the CC. You will need to manually alter the "Requester" field of
the ticket, by clicking on the "(change)" link next to the email address of the
apparent requester in the ticket title.

Please see [Requesting Support for Customers](/handbook/support/internal-support/#requesting-support-for-customers)
for more details.

## Communications

### Document your work; provide all context

Add research notes to your tickets, as it's important that we clearly document
all of our work performed throughout a ticket's lifecycle. Not only is this a
good way for you to track your own progress, particularly for lengthy and
challenging tickets, but it also provides your colleagues with a clear
understanding of what has been tried thus far, and enables a smoother transition
if a ticket needs to be reassigned.

#### Copying contents of Slack discussions to internal notes

When using Slack to work with others or communicate internally regarding a
support ticket, please bear in mind [our chat retention policy](/handbook/communication/#slack)
and the [Communication Guidelines (esp. 9.)](/handbook/communication/#general-guidelines).
It's best for future searches in Zendesk to copy relevant advice, notes, ideas,
etc. from Slack to an internal note in Zendesk.

#### Closure summary

If you are the assignee of a ticket, and the customer has confirmed that the
solution you provided has resolved the issue, add a **closure summary** to the
ticket prior to changing the ticket status to solved.

The closure summary should provide a brief outline of the confirmed solution. It
should be written with the goals of giving clarity to the customer with regard
to the solution as well as providing your colleagues with a quick and easy way
to see what solved the customer's problem.

To make it easier for yourself to create a summary, please consider using the
[General::Closing Summary](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/macros/-/blob/master/macros/active/General/Closing%20Summary.yaml) macro, which adds a template as an internal note
populated with some information. You will then need only to fill in the
remaining items with relevant information before copying the completed message
to a public comment for the customer.

Some caveats to bear in mind:

1. You should add a closure summary if the ticket is a long ongoing ticket where
   multiple suggestions have been provided to the customer throughout the ticket
   lifecycle.
1. The macro template ‘Closure Summary’ is available in Zendesk to help guide
   you with formatting a closure summary, you can modify or remove template
   content as deemed necessary.
1. You should not feel the need to add a closure summary if the customer has not
   responded and the ticket has been automatically closed.
1. You should not feel the need to add a closure summary if the ticket has a
   short life span and the solution is easy identifiable from the ticket history.
   (For example: If the resolution was a simple link to documentation.)
