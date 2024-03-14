---
title: Confirmation Emails
category: GitLab.com
subcategory: Accounts
description: "Workflow for cases when a customer reports they are not receiving their confirmation email"
---

## Overview

This workflow covers cases when a user says they are not receiving their confirmation email. The activation token in a confirmation email will only be valid for 24 hours. Thereafter, the user will need a new confirmation email.

## **Stage 0:** Ticket Triage

Before working the ticket ensure that it's correctly triaged with the `SaaS Account` form and `Did not receive confirmation email` problem type so that
the [SaaS Account Ticket Helper](https://handbook.gitlab.com/handbook/support/readiness/operations/docs/zendesk/apps/#gitlab-super-app) application can activate.

If the user has already correctly chosen the problem type, the automation will activate when an agent opens the ticket for the first time. If the SaaS Account Ticket Helper application fails to solve the issue for any reason, proceed to manually resolve it by going through the steps in the following sections.

## **Stage 1:** Locate Account

Before the issue can be resolved we first need to locate the account in question. This can be done by either checking the [GitLab User Lookup App](#check-gitlab-user-lookup-app) or by checking [GitLab Admin](#check-gitlab-admin).

### Check GitLab User Lookup App

1. Click the `Apps` button located in the top right of the Zendesk interface, while viewing the ticket.
1. Scroll down to the `GitLab User Lookup` app.
1. Observe the results. Check if the app found an account associated with the username or email address provided by the user. If a result was returned for the username lookup only, go to the provided `Admin Link` and check what email address is listed on the account.
1. Proceed to Step 2 under [Check GitLab Admin](#check-gitlab-admin).

**If no account was found** use the Zendesk macro [`Support::SaaS::Account does not exist`](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/macros/-/blob/master/macros/active/Support/SaaS/Account%20does%20not%20exist.yaml) or, if you believe it's applicable, use [`General::Verify account self-managed or .com`](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/macros/-/blob/master/macros/active/General/Verify%20account%20self-managed%20or%20.com.yaml) and then wait for a followup from the user.

### Check GitLab Admin

1. In the GitLab SaaS Admin Area, [search for the user](https://gitlab.com/admin/users) by username to confirm the account exists. Alternatively, search in your browser using [the API](https://gitlab.com/api/v4/users?search=email@email.test) or [ChatOps](https://about.gitlab.com/handbook/support/workflows/chatops.html#user).
1. Check the email address against what the user has reported and then perform one of the following fixes:
    - Did they make a typo when registering? See 👉 [Typo Fix](#typo-fix).
    - Otherwise, they likely are not receiving their confirmation email due to a suppression. See 👉 [Removing a Suppression in Zendesk](#removing-a-suppression-in-zendesk) or [Removing a Suppression in Mailgun](#removing-a-suppression-in-mailgun).

## **Stage 2:** Fix

### Typo Fix

1. Ensure the user is a customer with a current paid subscription. (Do not modify free user accounts. Free users must create new accounts with the correct email address)
1. Ensure the user's account has no activity by checking that the `Confirmed at:` field is blank/nil.
1. Ensure the user's account has no group or project memberships. If the account does have group or project memberships, then the user must pass the [Account Ownership Verification](https://about.gitlab.com/handbook/support/workflows/account_verification.html) workflow before proceding any further.
1. Change the email address to the correct one using one of the following methods:
    - **Admin:**
      1. Pull up the user's account while logged in with your admin account.
      1. Click `Edit`.
      1. Change the email address.
      1. Click `Save changes` when done.
      1. Remove the old mistyped email address from the account which will have been made a secondary email address on the account by clicking the red X next to it.
    - **ChatOps:**
        1. View User: `/chatops run user find <user or email>`
        1. Edit Email: `/chatops run user update_email <username or current email> <new_email@example.com>`
1. Double check that the account now has the proper email address as its primary.
1. Add an [admin note](https://about.gitlab.com/handbook/support/workflows/admin_note.html) to the account.

### Removing a Suppression in Zendesk

1. Click the `Apps` button located in the top right of the Zendesk interface.
1. Scroll down to the `SaaS Account Ticket Helper` app located below the tag locker app.
1. Click the button for `Email Suppressions`.
1. Search for the email address using the search field.
1. If a suppression is found you may optionally click the `copy` button to save the log from Mailgun to your clipboard that you can then paste into an internal comment on the ticket.
1. Click the `Remove the suppression?` button.
1. Send the user a new confirmation email.

If this process doesn't work you'll need to remove the suppression in Mailgun. See 👉 [Removing a Suppression in Mailgun](#removing-a-suppression-in-mailgun).

### Removing a Suppression in Mailgun

If the `SaaS Account Ticket Helper` doesn't work for any reason, we can remove suppressions in Mailgun directly:

1. Click on `Suppressions` along the left-hand side navigation bar.
1. Wait a moment for results to load before searching.
1. Ensure that `mg.gitlab.com` is set as the domain at the top of the page.
1. Enter the email address to be checked into the `Search for recipients` search bar and perform a search.
1. Click the `Delete` button next to an entry and then confirm your selection to remove the suppression.
1. Send the user a new confirmation email. See 👉 [Resend Confirmation Email](#stage-3-resend-confirmation-email).

## **Stage 3:** Resend Confirmation Email

### Primary email

Once the problem has been fixed, if the email is the primary email on the account, you can send the user a [new confirmation email](https://gitlab.com/users/confirmation/new). Afterwards, let the user know you've sent them a new confirmation email and ask them to check their inbox and spam folders.

>**Note:** If a user changes their primary email this will not work. See 👉 [Secondary Email](#secondary-email).

### Secondary email

Instruct the user to sign in and trigger a new confirmation email through their profile by visiting [https://gitlab.com/-/profile/emails](https://gitlab.com/-/profile/emails).

### Wacky State

If the user is unconfirmed, but their primary email address does not match the unconfirmed email address (see [this internal example](https://gitlab.com/gitlab-org/gitlab/-/issues/239098#note_399726260)), then there are two options to resolve:

1. Impersonate the user and click on the "Resend confirmation email" under Email on their Settings > Profile page.
1. File a [console escalation internal request](https://gitlab.com/gitlab-com/support/internal-requests/-/issues/new?issuable_template=GitLab.com%20Console%20Escalation) to set the `unconfirmed_email` to `nil`.

## Extras

### Checking Mailgun

On the first attempt, if our email system could not get through (usually server says it's non-existent or similar), then our mail server will put a suppression on sending further emails.

This is useful to check if emails have been delivered successfully from our end, which could mean that the error is with the users' email provider.

1. Utilize the Mailgun SSO app on your Okta dashboard to log in to [Mailgun](https://app.mailgun.com/app/dashboard).
1. Click on `Sending` along the left-hand side navigation bar.
1. Click on `Logs`.
1. Ensure that `mg.gitlab.com` is set as the domain above the activity graph.
1. Enter the email address to be checked into the search bar, search, and then scan the results to see if mail is being delivered to that address.
    - If email is delayed, respond to the user and ask them to wait.
    - If email is bouncing due to a suppression (evidenced by the message `Not delivering to previously bounced address` in the log) proceed to [Removing a Suppression in Zendesk](#removing-a-suppression-in-zendesk) or [Removing a Suppression in Mailgun](#removing-a-suppression-in-mailgun).
    - If email is marked as `Delivered` and the response code under `delivery-status` is `"code": 250`, this indicates that the user's mail server acknowledged the receipt, and the email delivery was successful.

### Identifying Multiple Suppressions on a Single Domain

Mailgun does not allow us to check for multiple suppressions on the same domain within it's `Suppressions` section, but we can use another method to find them without asking the customer for a list of email addresses that they suspect are being suppressed. To do so:

1. Utilize the Mailgun SSO app on your Okta dashboard to log in to [Mailgun](https://app.mailgun.com/app/dashboard).
1. Click on `Sending` along the left-hand side navigation bar.
1. Click on `Logs`.
1. Ensure that `mg.gitlab.com` is set as the domain above the activity graph.
1. In the search bar enter the customer's domain using `*` as a wildcard for the username.
1. Add a filter for `Event is Permanent Fail`.
1. Scan the results, any email address listed with a `Delivery Status Message` of  `Not delivering to previously bounced address` has been suppressed at one point in time.
1. Navigate to the `Suppressions` tab and enter in an email address from your previous search to confirm whether or not it's currently suppressed.
