---
layout: markdown_page
title: Weekend Emergencies - License Request
description: "Support process for weekend license emergencies"
category: GitLab Self-Managed licenses
---

## Overview

There are times when a customer submits an emergency support request for a new
license to replace their expired one immediately. This is problematic when the
on-call Support Engineer does not have access to CustomersDot.

This workflow describes the steps to be followed by anyone in Support,
regardless of whether they have CustomersDot access, to generate a short-term
temporary Ultimate license to de-escalate a **weekend** emergency.

This workflow does not cover SaaS Subscription Emergencies, see [Customer Emergencies Workflow - SaaS License Emergencies](/handbook/support/workflows/customer_emergencies_workflows.html#saas-subscription-emergencies).

## Scope

License requests for a customer with a **paid** plan, where the license's "grace period" (14 days after expiration) ended within the last 3 days from the current emergency's date.

## Out of Scope

1. Organizations without a **paid** plan.
1. Prospects.

---

## Workflows

### Confirm customer subscription

1. Request from the customer the following screenshots:

    - Admin Area -> Overview -> Dashboard
    - The license page from Admin Area -> License (in newer versions, may say subscription)
1. Add the screenshots to the ticket
1. Go to the Mechanizer ZenDesk App, from the ticket in the right side bar.
1. Enter your username and the user count for the license based on information from the screenshot
1. Enter the email address of the person who opened the ticket
1. The tool will generate and email to the customer a 5-day trial license for the given user count
1. Put a comment in the `#support_licensing-subscription` Slack channel to let the team know that an emergency license was generated with the ticket url

### Considerations

1. All licenses generated with the tool will have a 10 day limit. This cannot be changed through the tool.
1. The license will have generic information. This is intended to facilitate its creation.
1. If the customer mentions that they haven't received the email with the license, go to our
   [internal request issue tracker](https://gitlab.com/gitlab-com/support/internal-requests/-/issues?sort=created_date&state=closed&label_name[]=Mechanizer::Emergency+License+Generation)
   and you will see a closed issue with the title: `[Success] - Created a license
   under [EMAIL] for [X] users`. That issue will have a copy of the license. If
   there aren't any closed issues, you can look for an open issue which will
   have information about the failure. If you find it and no license was
   generated, you can use the tool again to generate another license.
