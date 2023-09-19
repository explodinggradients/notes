---

title: Quarterly Subscription Reconciliations
category: General
description: Workflow to assist customers with Quarterly Reconciliations.
---



## General Workflow

**Do**

- Explain how QSR works, and set appropriate expectations on any next steps.
- Be sure to set the **Transaction Issue Type** to `Quarterly Subscription Reconciliation` for tracking purposes.

**Don't**

- pass the ticket to Billing/AR
- pause QSR, or reset max seats without documented approval

When a customer contacts support regarding QSR, as a first line of contact you can use the [`Support::L&R::Refund or cancellation request on quarterly subscription reconciliation` macro](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/macros/-/blob/master/macros/active/Support/L&R/Refund%20or%20cancellation%20request%20on%20quarterly%20subscription%20reconciliation.yaml), or you can craft a manual response based on it.  If sending a response in your own words, it's important to follow the general guidelines and information used in the macro to be sure that we are setting appropriate and consistent expectations.

Try to explain QSR, how it works, and consider linking to the [documentation page for it](https://docs.gitlab.com/ee/subscriptions/quarterly_reconciliation.html).  There's also individual [SaaS focused](https://docs.gitlab.com/ee/subscriptions/gitlab_com/#how-seat-usage-is-determined) and [self-managed focused](https://docs.gitlab.com/ee/subscriptions/self_managed/#billable-users) documentation pages explaining how billable seats are calculated.

Refer to [this issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/3540#quarterly-subscription-reconciliation) for in-depth explanations.

## Dispute Escalation and Resolution

If the customer would like to dispute a reconciliation, either pending or processed:

- advise the customer that you will be putting them in contact with their sales account manager
- follow the workflow on [Working with Sales]({{< ref "working_with_sales#general-workflow" >}}) to inform the account manager in SFDC.
- Do not pause/disable QSR yourself except in extenuating circumstances ([see below](#pausing-qsr-on-a-subscription))
- Do not reset Max Seats on the namespace ([see below](#resolving-max-seats-overages))

Given that support team has no influence over the process at this point, direct the customer to continue all discussions with their sales manager, and the ticket may then be closed.

### Pausing QSR on a subscription

**Important:** Support team should not be disabling QSR on a subscription except in the cases of confirmed bug behavior.

1. If QSR needs to be disabled on a subscription due to a customer dispute or any other non-bug issue, refer to the sales-ops handbook page on [How To Temporarily Pause Quarterly Subscription Reconciliation](https://about.gitlab.com/handbook/sales/field-operations/order-processing/#how-to-temporarily-pause-auto-renewal-quarterly-subscription-reconciliation-and-operational-data).  The sales account manager should be following this workflow to request a temporary pause on QSR.

1. In the event a bug has been confirmed which is causing an incorrect QSR amount to be quoted, due to the time-sensitive nature of reconciliations Support team have the ability to disable QSR manually on a subscription through the customersDot Admin interface, and we should do so in these cases.

   - Navigate to the customer's account and view the Zuora Subscriptions tab (`/admin/customer/:id/zuora_subscriptions`)
   - Use the drop down menu under **Quarterly Coterms** to select Yes/No
     - Switch to `No`
   - Click Update.

#### When manually pausing QSR

1. You will need to take responsibility for ensuring that it becomes reactivated after a bug-fix or other work-around has been implemented.
   - Consider the [due date app](https://handbook.gitlab.com/handbook/support/readiness/operations/docs/zendesk/apps/#zendesk-super-app), [reminder app](https://handbook.gitlab.com/handbook/support/readiness/operations/docs/zendesk/apps/#gitlab-reminders-app), Slack's built-in reminder tool, or whatever works for you.

## Resolving Max Seats Overages

**Important:** Do not reset a namespace's `Max Seats` without the necessary approvals in chatter. View this step as waiving trueups, and refer to the sales-ops handbook page [Waived True-Ups: Policy and Approval Requirements](https://about.gitlab.com/handbook/sales/field-operations/order-processing/#waived-true-ups-policy-and-approval-requirements)

If approvals are given for resetting `Max Seats`, you can use the ZenDesk Mechanizer App > Max Seats tool, or do so through console access.  Document the action in the relevant ticket, or in an [internal-request](https://gitlab-com.gitlab.io/support/internal-requests-form/). In the case where QSR is approved for refund, approval for `Max seats` reset is still needed.

Be sure that you are setting this value such that it only eliminates the approved and waived overages. In many cases, you can simply set this value to the namespace's current usage, but use some common sense here too like reviewing the ticket, screenshots, customer interactions, etc to be sure you are setting the proper amount.  Ask in slack if you're unsure.

**Important:** If a QSR is refunded, max user count must be reset by opening a ticket with Support. Deal Desk will support this process. [Internal process guide here](https://gitlab.com/gitlab-com/sales-team/field-operations/deal-desk/-/wikis/Web-Direct-Quarterly-Seat-Reconciliation-(QSR)-Refunds).
