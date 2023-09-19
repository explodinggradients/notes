---
layout: markdown_page
title: Troubleshooting license purchase errors
description: "How to troubleshoot GitLab license purchasing errors"
category: GitLab Self-Managed licenses
---


Customers may report encountering the following error message when purchasing additional seats for their licensed GitLab Self-Managed instance:

> The Charge is not allowed to be updated on MM/DD/YYYY

This is caused by a customer renewing their license more than once so the newest license starts at a future date more than a year into the future and then refunding the future dated license.  The future dating in the system causes problems with the present such as being able to add additional seats.

## Example

- Customer renews their license for `2020-03-01` to `2021-03-01` then renews again for `2021-03-01` to `2022-03-01`
- The newest license for `2021` to `2022` becomes the only available license for download
- Working with `support` and `accounts receivable` the customer requests a refund on the newest license
- Due to the nature of the Zuora billing system this creates an effective future date for amending the existing license which cannot be changed
- The customer now sees the error `The Charge is not allowed to be updated on 03/19/2021` when trying to add seats
- To fix this the `accounts receivable` team need to go into the subscription and completely rebuild the subscription in Zuora by creating a `0` invoice for internal purposes that the customer never sees
