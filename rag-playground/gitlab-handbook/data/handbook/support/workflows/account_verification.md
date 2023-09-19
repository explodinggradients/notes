---
title: Account Ownership Verification
category: GitLab.com
subcategory: Accounts
description: "Workflow detailing how and when to verify account ownership including disable 2FA"
---

## Overview

This workflow covers how a user can provide account verification. While the workflow focuses on disabling [Two-factor Authentication](https://docs.gitlab.com/ee/user/profile/account/two_factor_authentication.html) on a GitLab.com account, it should be used for any [account changes](/handbook/support/workflows/account_changes.html).

2FA removal and other account actions can only be completed if the [workflow](#workflow) below is successful.

## User Account Verification

If the user has questions about the email, phone, or credit card verification GitLab is requiring, please refer to the [Internal Handbook for the workflow](https://internal.gitlab.com/handbook/support/#phone-number-verification-issues) to follow.

### Email Verification

As of Aug 16, 2023, Gitlab.com now requires that users without 2FA enabled verify their email address when a login attempt meets certain high-risk criteria. Review the [blog post](https://about.gitlab.com/blog/2023/08/08/gitlab-account-security/) announcing this change. If a user contacts support with questions, use the `Support::SaaS::Abuse::Email Address Verification` macro.

## GitLab Team Members

If the user is a GitLab team member, have them [contact IT Ops](https://about.gitlab.com/handbook/business-technology/end-user-services/).

## Self Service 2FA Removal

In most cases, users can disable 2FA themselves and regain access to their accounts, using one of the following methods:

1. Use a saved [two-factor recovery code](https://docs.gitlab.com/ee/user/profile/account/two_factor_authentication.html#recovery-codes).
1. [Generate new recovery codes via SSH](https://docs.gitlab.com/ee/user/profile/account/two_factor_authentication.html#generate-new-recovery-codes-using-ssh).
    - If a user has an SSH key tied to their account but receives a `Permission denied (publickey)` error, they may need to manually register their private SSH key using `ssh-agent` if they're using a non-default SSH key pair file path. Direct the user to [our documentation](https://docs.gitlab.com/ee/ssh/#configure-ssh-to-point-to-a-different-directory) for guidance on how to solve this.

> As of August 2020, [free users won't be able restore access to accounts](https://about.gitlab.com/blog/2020/08/04/gitlab-support-no-longer-processing-mfa-resets-for-free-users/) if self-service methods do not work for them.

## Disable 2FA With Support Intervention

If a user cannot make use of self-serve methods (lost their account recovery codes and has no SSH key registered), proving they own the account can be difficult. Support intervention for 2FA removal after the above steps have been attempted is only possible for users with an *existing paid plan* when the ticket was created.

If a paid user (part of paid group or paid user namespace) is unable to remove 2FA or otherwise regain access to their account using the above methods and responds with the need for further verification, then the user will need to provide evidence of account ownership before we can disable 2FA on their account.

For security purposes, support will not process 2FA resets for users who are added to a paid subscription for the express purpose of having 2FA disabled on their account.

## Workflow

The workflow applies to all cases where account verification is required.

### Keeping the Ticket Simple and Accurate

Because an ownership-verification ticket is a matter of record, the ticket must be simple, accurate, and tightly focused on the access issue.

1. Do not allow the customer to bring up unrelated topics.
1. Do not add requested CCs to the ticket. Remove any CCs that get added, except:
    1. Exception: Owners of the top-level group may be CCed as required.

### Step 0: Ticket metadata

Ensure that the ticket form, category, subcategory, and topic are accurate.

Most SaaS Account categories have [automations]({{< ref "/content/handbook/support/readiness/operations/docs/zendesk/automations.md" >}}) or [triggers]({{< ref "/content/handbook/support/readiness/operations/docs/zendesk/triggers.md" >}}), including 2FA removal.

### Step 1: Checking user eligibility (2FA requests only)

Before you send the challenges, make sure the user is eligible to receive support for 2FA removal.

#### Conditions for SaaS users

A SaaS user must meet one of the following conditions to be eligible for a 2FA reset.

1. The user on GitLab.com occupies a seat in a paid group on GitLab.com.
1. The user is an [Enterprise User]({{< ref "gitlab-com_overview.md#enterprise-users" >}}).
    - Note: A top-level group owner or user can submit the ticket. If the user is not a member of the group, an [owner vouch](#authenticating-an-owner-vouch) is required, and the [data classification](https://internal.gitlab.com/handbook/support/#data-classification) (GitLab internal) is still Red based on the status of the paid namespace.
1. The user is the primary billing contact on a current invoice for a SaaS purchase.
1. GitLab team member (account managers, CSMs or others) collaborate with the holder of this account in an account management project.
1. The user account is required for SSO access to Customers Portal to manage a paid subscription - see: [Conditions for 2FA Reset when account is used to access Customers Portal](#conditions-when-account-is-used-to-access-customers-portal).

More succinctly: they're paid, they use the account to pay, or we use the account to communicate with them.

While Support typically identifies users by their membership in a paid namespace, there are cases where users cannot be added manually by group owners, such as with [SSO enforcement](https://docs.gitlab.com/ee/user/group/saml_sso/#sso-enforcement) enabled. In these cases:

1. An [Owner vouch](#authenticating-an-owner-vouch) from an owner in the paid namespace is required.
1. Primary email of the account must match the company domain.
1. User must still prove account ownership following the [workflow](#workflow).
   - Include the paid namespace when determining the data classification level.
1. If the user is classed as an [Enterprise user]({{< ref "gitlab-com_overview.md#enterprise-users" >}}), then the user or an owner of the paid group raises the ticket.

#### Account Verification Matrix

The table below provides a summary of the available verification options based on the owner and user type:

| Requester | Target | Rule | Comment
| --- | --- | --- | ---
| Enterprise Owner | Own account | Owner passes challenges on own account, owner vouch (if required), must be provided by a different owner | If no other owner is available for vouch, see [internal handbook](https://internal-handbook.gitlab.io/handbook/support) for other challenges.
| Enterprise Owner | Member of paid group or intent to be added | Owner passes challenges on own account, vouch can come from same owner. Target user does not have to be CCd on ticket. Multiple enterprise users may be handled per ticket |
| Owner | Non-enterprise user | Owner can raise the ticket, user must supply the answers, owner can vouch. One user per ticket |
| Paid User | Own account | User passes challenges on own account. Owner can vouch. |
| Paid User | Other member of same paid group | Target user passes challenges on own account. Communication is direct from the target user who must be CC'd on ticket |
| Free User | Non-member of group with intent to be added | Not allowed - request must come from group owner |

#### Conditions when account is used to access Customers Portal

[Customers Portal](https://customers.gitlab.com) requires all customers to access through a [Linked Gitlab Account](https://docs.gitlab.com/ee/subscriptions/customers_portal.html#link-a-gitlabcom-account).

2FA can be reset when one of following conditions are met:

1. The request is made by the primary billing contact on the latest invoice for a GitLab subscription.
1. The GitLab account is linked to the customers portal account for the primary billing contact on the latest invoice for a subscription purchase.

If one of the above conditions is met the user is eligible for our 2FA reset process.

If an invoice can not be provided, suggest [sign in with legacy email/password](https://customers.gitlab.com/customers/sign_in?legacy=true), where an invoice can be downloaded.

### Step 2: Sending Challenges

If you need a basis for a response where you send the challenges, or in a 2FA ticket, if the user has not answered the challenges, use the `Support::SaaS::2FA::2FA Challenges` [macro](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+103721068).

### Step 3: Evaluating Challenge Answers

> **Note**: In case the user sends back very minimal information and it's clear it's not sufficient or the answers are vague, reply asking for more information immediately after their response. You can provide some additional guidance, such as "please provide the exact date and time of the commit, not just an approximate one".

1. To verify the challenge answers, use [chatops]({{< ref "chatops.md" >}}), the [Zendesk GitLab User Lookup App]({{< ref "/handbook/support/readiness/operations/docs/zendesk/apps.md#gitlab-super-app" >}}) or, for those who have admin access, check at `https://gitlab.com/admin/users/USERNAME`.
1. Use the [ZenDesk GitLab Super App's 2FA Helper]({{< ref "/handbook/support/readiness/operations/docs/zendesk/apps.md#gitlab-super-app" >}}) to determine the [risk factor](https://internal.gitlab.com/handbook/support/#risk-factors-for-account-ownership-verification) (GitLab internal) based on the user's answers. Data classification criteria and any notes are in the [Internal Handbook - Data Classification table](https://internal.gitlab.com/handbook/support/#data-classification) (GitLab internal), which is considered the source of truth. If you need to leave a comment manually (instead of through the app), use the [`Support::SaaS::2FA::2FA Internal Note` macro](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360043856894) to put an internal note on the ticket.
   - [Specific conditions are required to be considered for 2FA resets](#checking-user-eligibility-2fa-requests-only).
   - Challenge answers must be evaluated against a paid namespace if the user is a member of any paid namespace. If the user is not a member of a paid namespace, refer to [Conditions for 2FA Reset Consideration](#checking-user-eligibility-2fa-requests-only) for further guidance.
   - If a group owner is answering on an [enterprise user's]({{< ref "gitlab-com_overview.md#enterprise-users" >}}) behalf, the answers must relate to the group owner's account, not the user's account. Use the same verification process, and [owner vouch process](#authenticating-an-owner-vouch) (the same owner can be the one vouching).
1. **If verification passed:** Request that your decision be peer-reviewed by another member of the team via Slack `#support_gitlab-com`.
1. **If the verification failed**: A peer review is optional, and you may opt to [offer more challenges to the user](#user-fails-to-prove-account-ownership).
1. *Peer reviewer:* In case you disagree, leave an internal note on the ticket stating your thoughts on what the risk factor should be and reply to the Slack conversation for further discussion. If you agree, move to [the next section](#step-4a-user-successfully-proves-account-ownership) on what to do if successful.

#### Authenticating an Owner Vouch

In a paid namespace: If the user elects to have an Owner vouch for their request, apply the macro `Support::SaaS::2FA::2FA ask owner vouch`. This will direct the requestor to have an Owner (top-level) create a Snippet with a Support-provided string. Once they have replied verifying they have done so:

1. Use your Admin or Auditor account to browse to the Snippet provided (e.g. `https://gitlab.com/-/snippets/2057341`)
   - Verify the text of the Snippet matches the string you specified
   - Verify that the author of the Snippet is an Owner and direct member of the top-level paid group
1. If the Owner passes, you may count this towards the account verification challenges.

Note: Due to this [bug](https://gitlab.com/gitlab-org/gitlab/-/issues/337939) some group owners are not able to create snippets. In that case use a [backup method](#backup-methods-for-authenticating-an-owner) instead.

#### Backup methods for authenticating an owner

If a group owner is unable to create a snippet, you may use another method to verify their identity. It must be an action that has been specifically instructed by Support and identifiably unique to the situation. Some examples include having the owner:

- create an issue in a project they have access to with a specific piece of text that you provide.
- create a new project at a path that you provide.
- update their GitLab Status to a specific string.

### Step 4a: User Successfully Proves Account Ownership

This section is typically done by the peer reviewer. If needed, the peer reviewer (or approving manager) may leave an approval note, in which case the original reviewer will perform the actions.

1. For situations other than 2FA, please see [Account Changes workflow]({{< ref "account_changes" >}}).
1. For disabling 2FA: If you agree with the decision, sign into your admin account and locate the username in the users table or by going to `https://gitlab.com/admin/users/usernamegoeshere`
      1. Under the account tab, click `Edit`, add an [Admin Note]({{< ref "admin_note" >}}), and save.
      1. On the account tab, click on `Disable 2FA`.
      1. Use the `Support::SaaS::2FA::2FA Removal Verification - Successful` [macro](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+103772548).

### Step 4b: User Fails to Prove Account Ownership

> **Note**: Do *not* provide hints to answers, or let the user know which challenges they got right or wrong. That is how social engineering works!

1. If the user is unable to pass the risk factor but we have not provided all the applicable challenges, you may offer further challenges. This is true for all users, including owners.
   - Most commonly, an `Owner in the top level namespace` (with a valid subscription) vouch is requested. Use the `Support::SaaS::2FA::2FA ask owner vouch` [macro](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360052221199). See the [Verifying an Owner Vouch section](#authenticating-an-owner-vouch) for more information. The originating email of this request should match a verified email of the Owner's account. If the user is an Owner, vouch must be from a different Owner.
   - For large organizations, please check the Zendesk organization notes to see if they're using the [large customers](#large-customers) workflow before offering the owner vouch challenge.
   - Some challenges can be answered with the help of their colleagues. Use the `Support::SaaS::2FA::2FA Removal Verification - GitLab.com - Failed - Ask colleagues for help` [macro](https://gitlab.com/search?group_id=15990755&project_id=17008590&repository_ref=&scope=blobs&search=360089726039&snippets=false) to let them know which challenges they can try to work with their colleagues to answer.
   - When we receive a subsequent response, go back to [evaluating the challenges](#evaluating-challenge-answers) to see if they now pass.
1. If the user is unable to pass the available challenges:
   1. Inform them that without verification we will not be able to take any action on the account. For 2FA, use the `Support::SaaS::2FA::2FA Removal Verification - GitLab.com - Failed - Final Response` [macro](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+103790308).
   1. Mark the ticket as "Solved".

## Large Customers

For customers who are large enough to have an account management project, a different workflow can be configured for them that will allow Support to more easily disable 2FA for any of their users that require it. Before this process can be used, a GitLab team member from either Customer Success or Sales must perform a few setup steps (described below). If a customer requests this workflow, please refer them to either of those individuals.

### Setup (For CS & Sales)

The steps to follow depend on whether or not the customer has a shared Slack channel with us. Either the customer's Customer Success Manager (CS) or Account Manager (Sales) is responsible for performing this setup. Please proceed to [Shared Slack Channel](#shared-slack-channel) if they do or [No Shared Slack Channel](#no-shared-slack-channel) if they don't.

#### Shared Slack Channel

1. Find out which users within the customer's organization are the ones that will be authorizing GitLab Support to disable 2FA on their users accounts. Obtain **both** the Slack handle and GitLab username of these users.
1. Create a file called `2FA Verification.md` inside of the `.gitlab/issue_templates` directory of the customer's [Account Management](https://gitlab.com/gitlab-com/account-management) project. If that directory does not exist, create it as well.
1. Populate the `2FA Verification.md` file with the template below, taking care to replace the following variables from it with your specific customer's information:
   - `CUSTOMER_SLACK_CHANNEL` - The name of the shared Slack channel that the customer's organization has with us.
   - `SLACK_USERNAME` - The Slack handle of a user that is authorized to allow GitLab Support to disable 2FA for the customer's user accounts.
   - `GITLAB_USERNAME` - The GitLab username of a user that is authorized to allow GitLab Support to disable 2FA for the customer's user accounts.

     <details>
      <summary markdown="span">2FA Verification Template</summary>

       <p>A user in your organization is requesting to have [GitLab two-factor authentication](https://docs.gitlab.com/ee/user/profile/account/two_factor_authentication.html) removed from their account. Please review and complete the highlighted sections below.</p>

       <p>## Support Engineer Instructions
       <p>- [ ] Ping the customer's organization owners in CUSTOMER_SLACK_CHANNEL using the [Notify Customer - Slack](https://about.gitlab.com/handbook/support/workflows/account_verification.html#2-contact-through-slack) template. For this organization the owners are SLACK_USERNAME, SLACK_USERNAME, and SLACK_USERNAME.
       <p>- [ ] Fill out the `Request Details` section below.

       <p>## {+Request Details+}
       <p>- {+User Requesting Reset: USERS_GITLAB_USERNAME+}
       <p>- {+Support Ticket: TICKET_NUMBER+}

       <p>## {+Customer Instructions+}
       <p>- [ ] {+Review the request and get in contact with the user requesting the reset to verify its authenticity.+}
       <p>- [ ] {+Comment on this issue indicating your approval.+}
       <p>- [ ] {+Unassign yourself and any others from this issue.+}
       <p>- [ ] {+Assign to the Support Engineer who opened this issue.+}

       <p>/assign GITLAB_USERNAME GITLAB_USERNAME GITLAB_USERNAME
       <p>/label ~"2FA Reset" ~"Awaiting confirmation"

1. Open a [Support Operations issue](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/organizations/-/issues/new) to request that three pieces of information be added to a customer's Zendesk organization:
   1. A link to the `2FA Verification.md` file you created in the previous step, such as `2FA owner vouch: /path/to/2FA Verification.md/` in the notes.
   1. A link to the customer's account management project in the notes.
   1. The `skip_2fa_automation` tag so that users requesting this won't get the autoresponder.

#### No Shared Slack Channel

1. Find out which users within the customer's organization are the ones that will be authorizing GitLab Support to disable 2FA on their users accounts. Obtain the GitLab username of these users.
1. Create a file called `2FA Verification.md` inside of the `.gitlab/issue_templates` directory of the customer's [Account Management](https://gitlab.com/gitlab-com/account-management) project. If that directory does not exist, create it as well.
1. Populate the `2FA Verification.md` file with the template below, taking care to replace the following variables from it with your specific customer's information:
   - `GITLAB_USERNAME` - The GitLab username of a user that is authorized to allow GitLab Support to disable 2FA for the customer's user accounts.

     <details>
      <summary markdown="span">2FA Verification Template</summary>

       <p>A user in your organization is requesting to have [GitLab two-factor authentication](https://docs.gitlab.com/ee/user/profile/account/two_factor_authentication.html) removed from their account. Please review and complete the highlighted sections below.</p>

       <p>## Support Engineer Instructions
       <p>- [ ] Fill out the `Request Details` section below.

       <p>## {+Request Details+}
       <p>- {+User Requesting Reset: USERS_GITLAB_USERNAME+}
       <p>- {+Support Ticket: TICKET_NUMBER+}

       <p>## {+Customer Instructions+}
       <p>- [ ] {+Review the request and get in contact with the user requesting the reset to verify its authenticity.+}</p>
       <p>- [ ] {+Comment on this issue indicating your approval.+}
       <p>- [ ] {+Unassign yourself and any others from this issue.+}
       <p>- [ ] {+Assign to the Support Engineer who opened this issue.+}

       <p>/assign GITLAB_USERNAME GITLAB_USERNAME GITLAB_USERNAME
       <p>/label ~"2FA Reset" ~"Awaiting confirmation"

1. Open a [Support Operations issue](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/organizations/-/issues/new) to request that two pieces of information be added to the notes section of the customer's Zendesk organization:
   1. A link to the `2FA Verification.md` file you created in the previous step, such as `2FA owner vouch: /path/to/2FA Verification.md/`.
   1. A link to the customer's account management project.

### Usage (For GitLab Support)

If a 2FA ticket is opened by an organization that has had this workflow configured for them, perform the following steps to process the request depending on whether or not the customer has a shared Slack channel with us.

>**Note:** 2FA removal for the user is approved by the Customer via the 2FA Verification template. This means the Customer will confirm with the User having 2FA removed and not support.

#### 1. Create Issue

1. Open a new issue in the issue tracker of the customer's account verification project using the `2FA Verification` template and follow all instructions within it. A link to this template should be in the notes for the organization in Zendesk.

#### 2. Contact Through Slack (skip if no shared Slack channel)

1. Within the customer's shared Slack channel with us, use the template below to alert them to the fact that a new 2FA disable request exists in their account management issue tracker. Be sure to replace the following variables:
   - `SLACK_USERNAME` - The Slack handle of a user that is authorized to allow GitLab Support to disable 2FA for the customer's user accounts. If there are more than one, add them as well.
   - `ISSUE_LINK` - The URL of the 2FA reset issue created on the shared project

     <details>
       <summary markdown="span">Notify Customer - Slack</summary>

       <p>Hi `SLACK_USERNAME` - we've received a request from one of your users to disable 2FA on their account.

       <p>Could you vouch for them by following the steps in this issue: `ISSUE_LINK`?

       <p>Once you've done that, please let me know. If you don't get to this within 24 hours, we'll use our standard account verification procedures to determine if they're eligible for a 2FA reset.

>**Note:** If the customer has created an issue using the `2FA Verification` template themselves and sent us a Zendesk ticket with a link to it, skip this step.

#### 3. Wait For Authorization

Wait for the customer to comment on the issue and approve the request to disable 2FA.

As stressed in the Slack notification template, we will wait for the customer's answer for 24 hours. If no response is received by then, regular 2FA verification will take place via the [challenges workflow](#sending-challenges).

#### 4. Disable 2FA

Once the customer has approved the request, disable 2FA on the user's account, add an [Admin Note]({{< ref "admin_note" >}}) on the user's account, and then close both the support ticket and issue.

Peer review is **not** required. You may make the change yourself.

## **Account Ownership Changes**

There are some conditions under which a change of ownership may be requested by a company with a business relationship with GitLab. Our [support page](https://about.gitlab.com/support/gitlab-com-policies/#ownership-disputes) outlines that these processes are not available for unpaid groups.

The outcome of a successful request is a new or existing user in the namespace will have the Owner role.

### Account Ownership Change Request for Paid Groups

Account Ownership Change Requests are initiated when the sole Owner of a group leaves a company and an authorized representative of the company is seeking to regain control. This process should be a last resort, and self-service options must first be explored.

**If a request is received, verify:**

1. Current paid subscription is applied to the namespace.
1. Sole Owner's primary email address matches company domain.
1. Requestor has a GitLab.com account. Typically this user will already be a member but is not an Owner.

**Ensure that the requestor has exhausted all self-service options:**

- If the existing Owner's account does not have 2FA enabled, suggest that the requestor issue a password reset to the existing Owner's account, and [claim the account](https://docs.gitlab.com/ee/user/group/manage.html#change-the-owner-of-a-group).
- If the existing Owner's account has 2FA enabled, suggest the requestor contact the existing Owner to request that the existing Owner provide the one time password, backup codes, or private ssh key to allow the requestor to regain access, and [claim the account](https://docs.gitlab.com/ee/user/group/manage.html#change-the-owner-of-a-group).

**If no self-service options are viable, follow the steps below:**

1. Use the `Support::SaaS::Account Ownership Change Request (Self-Service Not Possible)` [macro](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360073396100), adding the account owner or account manager in CC if possible.
1. Once you have received the requested document, verify that all of the necessary information is included. If not, follow up with the requestor to obtain any outstanding information. Once the required information has been obtained, carefully follow the next steps.
1. Assess the request to verify if the following criteria have been met:
   1. Self-service options have been suggested and aren’t viable.
   1. The requested document is completely and correctly populated, and is on appropriate letterhead.
   1. The existing Owner has not been active during the last 90 days.
   1. The requestor is using an email address on the same customer email domain as the existing Owner.
   1. The requestor already holds a Maintainer role within the group.
   1. Independent online search analysis supports the information provided (such as: the existing Owner no longer works for the customer; the roles and positions held at the organization by the requestor and signer; and there is no indication of an internal dispute between the requestor and the existing Owner).
1. **If all criteria are met:** [elevate the requestor to Owner role](#how-to-elevate-the-requestor-to-the-owner-role).
1. **If any criteria is NOT met:**
   1. Create a new [Group Owner Change issue](https://gitlab.com/gitlab-com/legal-and-compliance/-/issues/new?issuable_template=group-owner-change) in the [Legal and Compliance project](https://gitlab.com/gitlab-com/legal-and-compliance);
   1. Add a link to the issue to the Zendesk ticket;
   1. Reply to the requestor using the `Legal::General` [macro](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=17008590&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360056569419) and set the ticket to "On-Hold". If you don't receive a reply after the On-Hold ticket reverts to open (4 days), ping in the `#legal` [Slack channel](https://app.slack.com/client/T02592416/C78E74A6L).
   1. After receiving approval from Legal, [elevate the requestor to Owner role](#how-to-elevate-the-requestor-to-the-owner-role).
1. Add an [Admin note]({{< ref "admin_note" >}}) on the group admin page.

#### How to elevate the requestor to the Owner role

1. Using a GitLab `Admin Account`, go to the requestor's 'Namespace - Group - Members' section.
1. Search for the member by name or email address; in the `Max role` column, change the requestor's role to `Owner`.
1. If the requestor is not a member of the group, then press the `Invite members` button at the top right, enter the requestor's email address, and set the role to `Owner`. Press the `Invite` button to save your changes.

## Special Cases

### Twitter

If a user has a pre-listed Twitter account on their GitLab profile, this may be used as an additional factor for proving account ownership.

1. Invite the user to follow `@GLSupport2FA` in a reply to their ticket.
1. Log in to <https://twitter.com/> using the GLSupport2FA twitter account in the 1Password Vault.
   - If the login requires a 2FA code, log in to <https://mail.google.com> using the <techsupport@gitlab.com> gmail credentials. Note: If you are redirected to OKTA login, use the same gmail credentials to log in to OKTA.
1. Go to <https://twitter.com/GLSupport2FA/followers> and confirm the listed Twitter account is in the Followers list.
1. Go to the messages list and send them the following snippet:

```text
Hi,

We recently got a request to <remove the 2FA on | delete | change the primary email address> your GitLab.com account. Since you listed this account there, we're reaching out for confirmation. Please let us know if it was you who initiated this request.

If you don't reply in the positive in 7 days we won't be able to count this towards your proof of account ownership.

Thanks,
GitLab Support
```

If a reply is received within 7 days, account for it in the Risk Factor Worksheet and continue with the workflow. Otherwise, this can be counted as a failed challenge.
