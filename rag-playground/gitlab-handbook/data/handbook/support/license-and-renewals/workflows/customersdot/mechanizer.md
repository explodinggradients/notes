---

title: Mechanizer 
category: CustomersDot
description: How to use the mechanizer for L&R requests. 
---





## Overview

This workflow details how to use the Zendesk App that utilizes the [Mechanizer](https://gitlab.com/gitlab-com/support/toolbox/mechanizer) to automate CustomersDot console related tasks.

The Mechanizer is [currently in maintenance mode](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/4299). Our product goal is to migrate the features in Mechanizer to CustomersDot ([epic](https://gitlab.com/groups/gitlab-org/-/epics/6828)).

## Existing Automations

The new ZD Mechanizer app can be found by opening the ZD App side bar. You must scroll down to find it; it is shown below several other apps.

In the app you will have the option to select from the following request types:

#### Note

**Your GitLab Username** will be automatically added to the form.

### Set compute minutes to namespace

Allows setting additional compute minutes to a customer namespace to the value specified in the `Extra minutes` field.

> **WARNING:** Additional compute minutes added this way will last **indefinitely** until used. If the request is to provide "extra compute minutes" during the trial period only, use the [Manage GitLab Plan and Trials option](#manage-gitlabcom-plan-and-trials) which will change the *usage quota* to match a paid plan quota for the duration of the trial.

The form has two required fields:

- **Namespace**: The customer namespace as it appears in the URL.
- **Extra minutes**: The value of compute minutes to add. (***Note:** This will update the 'Additional Minutes' value.* )

### Enable compute minutes

*Currently labeled: `Enable CI Minutes` in the ZD Mechanizer App.*

Remove the restrictions for using compute minutes for groups who are part of a sales assisted trial.

- **Namespace**: The customer namespace as it appears in the URL.

### Force Associate

Associates a group with a subscription. All fields are required.

- **Namespace**: The customer namespace as it appears in the URL.
- **Subscription ID**: The unique ID of the purchased subscription in Salesforce

### Manage GitLab.com Plan and Trials

Updates GitLab Subscription or customer trial. You can use it for the following cases:

1. Downgrade to Free
1. Trials
    1. Change Plan
    1. Renew/extend Date
1. "Extend" an existing active or expired subscription for .com.
    - Note: To "extend" a subscription, a trial is triggered on the namespace. An old trial order is used if it exists. Otherwise, a new trial is created.

Please note that in order to extend or renew a trial, the customer **MUST** have an active trial because a CustomersDot account needs to exist.  If the prospect has not yet initiated a trial themselves, please have them do so via the [customers portal](https://customers.gitlab.com/trials/new?gl_com=true).

These two  fields are mandatory:

- **Namespace**: The customer's namespace as it appears in the URL.  For example, if the customer namespace is located at <http://gitlab.com/gitlab-com> then the namespace would be `gitlab-com`. Please confirm through your own observation and through communication with Sales, the CSM, or the customer that the namespace is the one with the subscription or trial to be updated.
- **Plan**: The subscription plan that you would like applied for the customer's group.  If the `free` option is selected, the customer's namespace will immediately be downgraded and the trial or subscription ended.

These two fields are optional:

- **End Date**: The updated date the plan will end.
- **Sales Manager Approval**: The GitLab.com username (without a preceding @) of the sales manager who approved a trial extension. This approval should be via chatter on the SFDC opportunity.

Required to "extend" a subscription:

- **Subscription name**: The name of the existing (active or expired) subscription tied to the namespace.

> Note: When a new trial is created, it has the default trial values (30-day, ultimate, 400 compute quota), so you need to re-run "Update GitLab Plan" again with the requested values.

### Clear Subscription

Unlink a group from a subscription. Note: The group will be downgraded to Free if the subscription being unlinked is a Premium or Ultimate subscription or trial.

- **Subscription name:** The subscription to be removed from a namespace.

### Unlink GitLab.com Account

Unlinks the GitLab.com account that is tied to the CustomersDot account provided.

- **Customer ID:** CustomersDot customer account ID.

Uses the `unlink_customer` function.

### Emergency license generation

Generates a legacy Ultimate trial license valid for 10 days and emails it to the customer email specified in the form.
The use of this feature should be limited for any emergency license requests when L&R is unavailable, such as during the weekends.

- **Customer email:** The email where the license will be sent. We recommend sending the license to the ticket requester's email, unless specified otherwise.
- **User count:** Total number of users in the license.

A note on **User Count**:

For Self-Managed licences, GitLab will refuse to install a license key with less than the current number of billable users. Therefore, **User Count** for a trial license should *at least* be the same number as the current number of billable users plus any true-ups owed (if any).  For example, if 25 current billable users, and 5 true-ups owed, set **User Count** to at least 30.

### Add storage to a namespace

Sets additional storage for a namespace to the value specified in the `Extra storage (MiB)` field

- **Namespace:** The customer namespace as it appears in the URL.
- **Extra storage (MiB):** Additional space to add in MB

### Set max seats

Modifies the highest number of seats used on the namespace during the current subscription term.  

#### Note

This will change the total seats owed in the GitLab.com subscription. Before using this option check with a support manager.

- **Namespace:** The customer namespace as it appears in the URL.
- **Max Seats number:** New value for max seats.
