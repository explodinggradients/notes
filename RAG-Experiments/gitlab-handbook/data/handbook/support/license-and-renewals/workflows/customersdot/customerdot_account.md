---
title: CustomerDot Account Related Problems
category: CustomersDot
description: Using the customer console for internal requests is only for special cases where the existing tools won't allow us to complete the task at hand.
---

## Overview

Sometime customers would have trouble accessing their account. This page would help you troubleshoot the problem.

### Customer cannot sign in even after password reset

This could be due to the following reasons:

#### 1. Password reset email was requested from https://gitlab.com

It's possible that customer request password reset email from https://gitlab.com/users/password/new.
We can confirm this by searching through the mailgun log. To locate the password reset email:

1. You can find the mailgun log in credential in 1password for support team.
1. On the left panel, expand `Sending` and go to `Logs`
1. On the top left, click the `Domain` dropdown and choose `customers.gitlab.com` and enter the customer email to search for recent email. You can also search in `mg.gitlab.com` domain to confirm whether the password reset email was requested on GitLab.com or on customers.gitlab.com
1. If no password reset was sent, we can issue a password reset email or ask the customer to request a password reset email from https://customers.gitlab.com/customers/password/new

#### 2. The CustomersDot account has not been confirmed

When the account is not confirmed, the customer cannot log in. To view whether an account is confirmed:

1. Sign into CustomerDot with your admin account
1. Find the customer account
1. Click on the `i` icon on the customer account or `Show` if you're already viewing the account
1. The confirmation is shown in `Confirmed at` field

#### 3. The customer is trying to sign in using another email address

Situations may arise where a customer has used a different email address for their [customers portal](https://customers.gitlab.com/customers/sign_in) account and their GitLab.com account. It may also be possible that a customer has signed up more than once using different email addresses (e.g. `firstname_lastname@organization.com` and `firstname.lastname@organization.com`). In scenarios such as these, please explain the differences to the customer, and clarify which email address they have have used for their GitLab subscription.

#### 4. The customer hasn't confirmed their email address

If the customer has not confirmed their email, we can resend the confirmation email using [this form](https://customers.gitlab.com/customers/confirmation/new) and get back to the customer.
