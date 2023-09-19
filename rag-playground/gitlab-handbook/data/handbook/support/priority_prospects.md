---
title: Priority Prospects
description: Details on how the priority prospect system works
---

## Overview

By default, [trial licenses do not include support](https://about.gitlab.com/support/#trials-support).

If you've been contacted by a prospect whose evaluation of GitLab includes evaluating support expertise or SLA performance, as a member of the Sales team **you can grant request temporary support for their trial license**. Please note this is only available for 30 days. After that point, the account will be downgraded back to the standard levels for a trial/prospect, unless an extension request is filed and approved.

Free access to support granted in this way is not for any customer who wants it, but for strategically important prospects for whom evaluation of support is part of their decision criteria. There may be many factors Sales leadership will consider in deciding which prospects are eligible. Generally, prospects with potential ARR of less than $100,000 may not be likely to be approved.

## Process Restrictions

- Only 30 priority prospects can exist at any one time. The current reference
   sheet containing who is a priority prospect can be found (internal)
  [here](https://docs.google.com/spreadsheets/d/11p3aBj1LTr-ngk1wxoMlae-UvJ3bOTuQHd48so2ZcXU/edit?usp=sharing)
- An area sales manager must approve a request to create or extend a priority
  prospect
- No more than 2 extensions can be done for a priority prospect.

## Support Restrictions

- This does not include [emergency support](https://about.gitlab.com/support/#how-to-trigger-emergency-support)
- This does not include [upgrade assistance support](https://about.gitlab.com/support/scheduling-upgrade-assistance/)
- This does not include migration assistance support
- This does not include architecture review support
- This does not include [namesquatting requests](/support/workflows/namesquatting_policy.html)
- This should only be for [PoVs](https://about.gitlab.com/customer-success/solutions-architects/tools-and-resources/pov/) involving errors from a setup (and not the setup
  process itself)
- A maximum of 3 contacts are able to create support tickets for the organization
- This does not include [shared organization setup in Zendesk](https://about.gitlab.com/support/managing-support-contacts/#shared-organizations)
- All response times are reasonable effort and will be given an internal SLO of
  24 hours.
- Everything within [the statement of support](/support/statement-of-support/) applies.
- This is solely for **prospects**. This means the account type in Salesforce
  is `Prospect`. This cannot be applied to any type of account other than a
  `Prospect`.

## Requests

### Requesting a new priority prospect

Requests to create a new priority prospect are done via issue in the
support-ops-project repo. The template for this can be found
[here](https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/issues/new?issuable_template=Priority%20Prospect%20Creation%20Request).

Once submitted, have a regional sales manager comment on the issue approving the
request. From there, Support Operations will work the request.

Creating a new one can take up to 24 hours to complete, pending no issue
preventing it from being done. You should plan for this delay as much as is possible.

**NOTE**: Customers should *not* submit any tickets until this process is
completed. Doing so can result in the tickets being rejected, as the
priority prospect status is only applied on tickets filed **after** the request
has been completed.

Once the expiration date has been hit, the account will be reverted back to a
free, non-supported prospect. If there is a need to extend it, please file a
[request extension](#requesting-an-extension)
a week prior to the expiration date.

### Requesting an extension

Requests to extend an existing priority prospect are done via issue in the
support-ops-project repo. The template for this can be found
[here](https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/issues/new?issuable_template=Priority%20Prospect%20Extension%20Request).

**NOTE**: Keep in mind these should be filed a week prior to the expiration
date to avoid issues.

Once submitted, have a regional sales manager comment on the issue approving the
request. From there, Support Operations will get approval from Support
leadership work the request.

### Requesting a cancellation

Requests to cancel an existing priority prospect are done via issue in the
support-ops-project repo. The template for this can be found
[here](https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/issues/new?issuable_template=Priority%20Prospect%20Extension%20Request).

This should be done in a case where it has been decided to cancel priority
prospect status.

## Information for the customer

The customer should never submit a ticket before this process is fully completed
(as indicated by Support Operations in the request issue). Doing so before that
can result in the ticket being rejected.

Once the process is fully completed, the customer should be informed of the
following *vital* information for submitting tickets:

- All SaaS related tickets should be submitted via
  [this form](https://support.gitlab.com/hc/en-us/requests/new?ticket_form_id=334447),
  unless it is specifically about SaaS Account related matters
- All SaaS Account related matters should be submitted via
  [this form](https://support.gitlab.com/hc/en-us/requests/new?ticket_form_id=360000803379)
- All Self-Managed related tickets should be submitted via
  [this form](https://support.gitlab.com/hc/en-us/requests/new?ticket_form_id=426148)
- Every ticket should ensure the "Tell us about your GitLab subscription" field
  uses the value "Sales Assisted Trial". Any other one could cause routing
  issues for them.
- All tickets must be filed using the contact emails provided in the request.
  Any others will be rejected by the system (and the ticket closed).
