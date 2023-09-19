---

title: Billing, invoice and payments requests
category: General
description: Billing and invoicing requests require action from our Billing/Accounts Receivable team.
---



- TOC
{:toc .hidden-md .hidden-lg}

## Overview

Billing and invoicing requests require action from our Billing/Accounts
Receivable team.

The following information is helpful to provide to the AR team when transfering
tickets, but not required.

1. Subscription #
1. Subscription information - copy & paste from `Manage Purchases` in
   [CustomersDot](https://customers.gitlab.com/customers/sign_in)
1. Zuora ID - available in the [CustomersDot](https://customers.gitlab.com/customers/sign_in)
   under the `Edit` tab
1. Salesforce Account ID - available in the [CustomersDot](https://customers.gitlab.com/customers/sign_in)
   under the `Edit` tab

## Billing

### Zuora contact change

When a customer wants to change the contact for current and future purchases.

> **Note:** *Billing doesn't have a vetting process, so we need to vet the
customer as far as possible before passing the request*

1. Verify that they are associated with the account / authorised to make the
   request, by checking the following:
   - if they are a contact in SFDC
   - if their domain name matches the company/previous contact
   - checking if they are the owner of the group (for a SaaS subscription)
   - if they pass the [account ownership verification](https://about.gitlab.com/handbook/support/license-and-renewals/workflows/customersdot/associating_purchases.html#ownership-verification)
1. Use the [`Support::L&R::Zuora Contact Change`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=360072090060) macro to transfer the ticket to AR to update the bill to and sold to contact in Zuora

Support will still generate a manual license if new contact wants an updated
license. Zuora update is primarily effective for future purchases.

NOTE: The `Sold to` contact in Zuora usually receives the license, renewal reminders and comms about changes to the subscription (e.g renewal success/fail). The `Bill to` contact in Zuora will receive invoices as well as renewal reminders.

### Billing processes to know about

#### Requests From Billing Team for Support to Verify and Update Sold To Details

The Billing Team will generally handle changes to the `Bill To` contact information, but occasionally may need to rely on our team to vet changes to `Sold To`.  In such events, they will pass a ticket over to the Support team, in which case you can review and act on the request pursuant to the steps outlined in the [Ownership Verification workflow]({{< ref "associating_purchases#other-notable-workflows-involving-customersdot" >}}), and the steps to [update Sold To
details]({{< ref "associating_purchases#update-zuora-sold-to-contact-using-customersdot" >}}).

- Refer to their internal [wiki page here](https://gitlab.com/gitlab-com/Finance-Division/finance/-/wikis/Process-for-BTST-Information-Updates-and-Invoice-Request#update-request-for-st-email) for additional details.

#### Zuora entity change

When billing processes an [entity change](https://gitlab.com/gitlab-com/Finance-Division/finance/-/wikis/Process-for-change-of-entity),
billing creates a second Zuora account for the customer, with a different entity
than the original.

To identify entity changes, check the `Renewal subscription` field in a Zuora subscription.
The original (and now cancelled) subscription will point at a `Renewal subscription` that can be used to search for the new Zuora account.

##### Effect on Self-Managed subscriptions

When an entity change happens at renewal, it can impact how licenses are
generated. If you are troubleshooting a license issue, check Zuora to see if
there are 2 accounts with different entities to confirm if an entity change took
place.

The issue that we will see more often is the renewal license not generated with
previous users or trueups. In the event of the license being impacted by the
entity change, we can assist with a manual license.

##### Effect on SaaS subscriptions

As part of the [entity change](https://gitlab.com/gitlab-com/Finance-Division/finance/-/wikis/Process-for-change-of-entity) process,
the Billing team sets the new Zuora account to `silent` when creating the relevant quote, opportunity, and subscription from the previous account.

The `silent` account setting results in no **Order** being created in [Customers Portal](https://customers.gitlab.com/customers/sign_in).
You can confirm that a Zuora account is `silent` by checking **Billing and Payment Info** -> **Communication Profile**.

**NOTE:** A subscription in the Customers Portal account may be visible but it would be impossible to link it to a group because of lack of an Order entry.

These situations are handled by following the steps in the [Billing Entity Change: Associate Subscription](https://gitlab.com/gitlab-com/support/internal-requests/-/blob/master/.gitlab/issue_templates/Billing%20Entity%20Change%3A%20Associate%20Subscription.md)
issue template.

### How to handle Billing Entity changes using the CustomersDot Rails console

<div class="panel panel-gitlab-orange">
**Console Hacks Deprecation Notice**
{: .panel-heading #console-hacks-notice}
<div class="panel-body">

Following the [discussion and decision to be more pushy than hacky](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/4299)
using console commands in CustomersDot, this workflow is documented **as a temporary workaround only** while the Fulfillment team works on
integrating Billing entity changes in the product.

The progress on Fulfillment's work can be followed in these reported issues:

- [Process for, and gaps around, Billing Entity Change from Fulfillment perspective](https://gitlab.com/gitlab-org/fulfillment-meta/-/issues/537)
- [Billing Entity Change: SaaS Subscriptions should provision correctly](https://gitlab.com/gitlab-org/customers-gitlab-com/-/issues/4376)
- [Spike: Provision an SM License correctly after a Billing Entity Change](https://gitlab.com/gitlab-org/customers-gitlab-com/-/issues/3044)

This workflow will be removed once the above issues are fixed.

</div>
</div>

When a Billing Entity Change occurs, there will be two Zuora accounts and two subscriptions; the old subscription would be on the canceled Zuora account, the new subscription would be on the active Zuora account. The newly created subscription will very possibly not have an Order object created for it, because the billing workflow sets the communication profile to `silent` during creation, which prevents Zuora from making callouts to CustomersDot. An Order is required to link a subscription to a namespace on GitLab, so you will need to create one.

To create an Order and link the namespace to the new subscription:

1. The support engineer requires [console access to CustomersDot](/handbook/support/license-and-renewals/workflows/customersdot/customer_console.html). There is not currently a way to fullfil it via mechanizer.
1. [Find the old and new Zuora Accounts](#finding-zuora-accounts)
1. Confirm the CustomersDot account has the new `Zuora account` ID
1. [Create an Order for the new subscription](/handbook/support/license-and-renewals/workflows/customersdot/customer_console.html#create_order_from_zuora)
1. [Link the new subscription to the group](/handbook/support/license-and-renewals/workflows/customersdot/customer_console.html#force_reassociation)
1. Confirm the `Max seats used` is reset to current seats in use count. If not, update it using the [account_seats](/handbook/support/license-and-renewals/workflows/customersdot/customer_console.html#reset-max-seats) function.
    - This step may be needed here to adjust their `Max seats used` to their `Seats currently in use`, because this process does not automatically reset that like it normally would during a renewal. You may need to use discretion here if the customer's max historical seatcount is wildly different from what they are currently paying for.

Examples of this workflow:

- <https://gitlab.com/gitlab-com/support/internal-requests/-/issues/10633>
- <https://gitlab.com/gitlab-com/support/internal-requests/-/issues/10585>

#### Finding Zuora accounts

For the above workflow, you need to locate both of the Zuora accounts in question. The entity change results in a new billing account being created, and the SaaS subscription(s) being recreated on that account.

- From CustomersDot: If you know the CustomersDot account, at least one of the Zuora accounts will be present in the `History` tab and you can work from there.
- From SFDC: You can usually find both Zuora account IDs by looking at the SFDC account -> Billing Accounts.  In the best case, there will be only 2 accounts listed there, the new and the old.  But often there are several billing accounts associated with a customer account. The billing account in SFDC will have an Account Number in the format of `A000XXXXX`. This can be searched directly in Zuora from the search page on Customer Accounts. Alternatively, the SFDC billing account shows a Zuora ID md5 hash, which you can supply to Zuora by editing this URL: `https://www.zuora.com/apps/CustomerAccount.do?method=view&id=ZUORA-ID-MD5-HASH-GOES-HERE`

If the above suggestions do not work, either use a different method for locating them, and/or see below on [Finding subscriptions](#finding-subscriptions).

When creating an order for the new subscription, the `create_order_from_zuora` function will query the Customer object, look at their Zuora subscriptions, and create the order based on that, so the CustomersDot account **must be pointing at the new Zuora account**.  If it is not, make sure you are looking at the right account, and if you are, then just update the `Zuora account` field to the correct ID. Billing team usually handles that, though.

#### Finding subscriptions

- Easily identify the old/cancelled subscription via console:

   ```ruby
   pp Order.find_by(subscription_name: "old-subscription-name")
   id: 123456,
   customer_id: 123456,
   product_rate_plan_id: "2c92a00d76f0d5060176f2fb0a5029ff",
   subscription_id: "MD5-HASH-HERE",
   subscription_name: "old-subscription-name",
   start_date: timestamp,
   end_date: timestamp,
   quantity: 216,
   gl_namespace_id: "1234567",
   gl_namespace_name: "group-name",
   amendment_type: "RemoveProduct",
   trial: false,
   last_extra_ci_minutes_sync_at: nil,
   zuora_account_id: "MD5-HASH-HERE",
   ```

   You can also try just locating all subscriptions ever linked to the group namespace:

   ```ruby
   pp Order.where(gl_namespace_id: xxxxxx)
   ...
   ...
   customer_id: 123456,
   product_rate_plan_id: "2c92a00d76f0d5060176f2fb0a5029ff",
   subscription_id: "MD5-HASH-HERE",
   subscription_name: "old-subscription-name",
   ...
   ...
   ```

   You may notice that the `end_date` is the **renewed** `end_date`, because it was renewed and then cancelled, so don't get tripped up by that. The important parts are the `subscription_name`, and if needed, the `customer_id`, `subscription_id`, and `zuora_account_id`.
- From SFDC both subscriptions will be listed in the SFDC account under Subscriptions and/or Subscription Product & Charges. You should notice they point at 2 different billing accounts, and one of the susbcriptions will be marked as `Cancelled`.  You can use both of these to locate the Zuora accounts if you haven't already. Generally, the subscription with the higher ID number will be the new one. Alternatively if you can locate the relevant quotes in SFDC that have their status as `Sent to Z-Billing`, the quotes will have the **Zuora Subscription ID md5 hash**.
- If you have their CustomersDot account, the new subscription should also appear under their `Zuora Subscriptions` tab. If not, either there exists another CustomersDot account (try searching by just contact email domain), or possibly the CustomersDot account wasn't updated.

Once you locate a `subscription_id` you can directly access the subscription by editing this URL: `https://www.zuora.com/apps/Subscription.do?method=view&id=ZUORA-ID-GOES-HERE`.

In Zuora, the old / cancelled subscription may also have a field `Renewal subscription`, which lists the name of the newly created subscription.

## Cancellations, Downgrades, and Refunds

### Cancellations

When a customer wishes to cancel their subscription and they are not interested
in waiting until the subscription expires.

1. Make sure that there aren't any other types of queries that would need the
   Support team's attention
1. Use the [`General::Accounts Receivable`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360038646513) macro to transfer the ticket to AR to
   process the cancellation. They will reply to the customer once done and issue
   a refund if applicable.

### Downgrades

There is currently [no ability to downgrade a subscription from a self-service perspective](https://gitlab.com/gitlab-org/customers-gitlab-com/issues/368).

Plan downgrades should only be done at renewal. However, if the customer purchased the wrong plan as a new subscription, send
the request to the AR team by selecting the `Accounts Receivable` macro and ask that the incorrect purchase be cancelled so that a new subscription can be purchased on the Premium plan.

If a SaaS Ultimate customer would like to renew for a Premium plan, advise them to purchase a Premium subscription and link their group to the new subscription. Ensure that they have set their Ultimate subscription to expire/cancel on the end date.

If a Self-managed Ultimate customer would like to renew for a Premium plan, refer them to Sales for assistance.

### Refunds

GitLab provides subscriptions on an annual basis which are not eligible for termination / refund for a customer's convenience. When a refund request is made, our billing team uses [this internal guide](https://gitlab.com/gitlab-com/Finance-Division/finance/-/wikis/Refund-Approvals-Sales-Assisted-&-Web-Direct) (GitLab internal) to determine if a refund is appropriate.

1. Determine the reason that the customer is cancelling and requesting a refund.
1. Let the customer know that the billing team will advise whether a refund is possible and process the request if appropriate.
1. Make sure that there aren't any other types of queries that would need the
   Support team's attention
1. Use the [`General::Accounts Receivable`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360038646513) macro to transfer the ticket to AR to advise and process if relevant. They will reply to the customer once done.

Note: we cannot do partial refunds, so when a refund is requested, the whole
subscription will have to be cancelled and refunded. See [Renewal reversal](/handbook/support/license-and-renewals/workflows/billing_contact_change_payments.html#renewal-reversal) for accidental renewal scenarios.

## Invoice

### Request copy of invoice

Check first if the invoice is available in [CustomersDot](https://customers.gitlab.com/customers/sign_in).

- If yes: walk the customer through locating the invoices under Payment History for future self-service ability.
- If no: Use the [`General::Accounts Receivable`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360038646513) macro to transfer the ticket to AR to
  process the request. They will reply to the customer once done.

### Invoice modification

When a customer wishes to modify their invoice for tax or administration purposes.

1. Verify that the invoice exists in the system
1. Make sure that there aren't any other types of queries that would need the
   Support team's attention
1. Use the [`General::Accounts Receivable`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360038646513) macro to transfer the ticket to AR to
   process the request. They will reply to the customer once done.

## Payments

### Requests to make a payment/payment failed

Use the [`General::Accounts Receivable`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360038646513) macro to transfer the ticket to AR to
process the request. They will reply to the customer once done.

### Credit card removal

When a customer wishes to remove their credit card from their CustomersDot
account.

1. Make sure that there aren't any other types of queries that would need the
   Support team's attention.
1. Use the [`General::Accounts Receivable`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360038646513) macro to transfer the ticket to AR to
   process the request. They will reply to the customer once done.

### Renewal reversal

When a customer has accidentally renewed twice or mistakenly.

1. Determine the reason that the renewal has to be reversed
1. Use the [`General::Accounts Receivable`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360038646513) macro to transfer the ticket to AR,
   they will reverse the renewal so that the subscription is in the same state
   as before the renewal and refund the renewal if applicable

### Requests for split payments

When a customer has a payment limit on their card, preventing a single payment for the full amount of their purchase, Billing is able to charge the card in "batches".

1. Get information on the limit and the total cost of the purchase the customer wishes to make.
1. Use the [`General::Accounts Receivable`](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360038646513) macro to transfer the ticket to AR to
   process the request. They will reply to the customer once done.

Note that in some cases, the total amount is too large to charge in 2 batches and Billing might request that a sales-assisted order is done instead. If you're unsure whether this would be the case, you can tag [at]Billing-ops in Chatter on the Account or Opportunity in SFDC to double-check with them.
