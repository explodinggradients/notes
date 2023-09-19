---
layout: markdown_page
title: Handling GitLab Dedicated License Requests
description: "How to handle GitLab Dedicated License Requests"
category: GitLab Self-Managed licenses
---


## Workflow for handling GitLab Dedicated Licensing

Currently, GitLab Dedicated license provisioning needs to be handled manually whilst we await the implementation of the EPIC [GitLab Dedicated Automated Provisioning](https://gitlab.com/groups/gitlab-org/-/epics/8799)

In the interim the following steps are required in order to generate the license file and ensure that the request is tracked correctly.

### License requests for new GitLab Dedicated customers

1. Deal Desk manually creates the opportunity quote and adds the GitLab Dedicated SKUs.
1. The quote is synced to Zuora, where the subscription is created.
1. The GitLab Dedicated team reach out to Support via the 'Other Licenses and Renwals issue' [internal request form](https://gitlab-com.gitlab.io/support/internal-requests-form/) providing the SFDC opportunity link and requesting a license file is manually created.
1. L&R Support verifies that the SFDC opportunity is `closed-won` and manually creates the license file.
   - The L&R support engineer adds an internal note containing a link to the license in CustomerDot so that that it can be tracked with the Accounting team for revenue recognition.
   - The L&R engineer sends the license file to the "sold-to" account owner and CC's the GitLab Dedicated team member who raised the ticket.
1. The GitLab Dedicated team notifies revenue recognition & AR for confirmation of provisioning.

### License requests for existing or multi-year licensed GitLab Dedicated customers

1. For renewing or multi-year licensed customers a new GitLab Dedicated license will need to be manually generated at the end date of the customer's subscription.
1. A request to renew a 1 year license subscription may be submitted by the GitLab Dedicated team or another stakeholder such as a customer, Sales or a CSM.
1. Requests should be submitted via the 'Other Licenses and Renewals issue' [internal request form](https://gitlab-com.gitlab.io/support/internal-requests-form/) and should include the corresponding SFDC opportunity link.
1. L&R Support should then implement steps 4 and 5 as detailed in the workflow [License requests for new GitLab Dedicated customers](#license-requests-for-existing-or-multi-year-licensed-gitLab-dedicated-customers). If the request did not orginate from a GitLab Dedicatad team member then please cc `athomas@gitlab.com` on the ticket to inform him that a new license has been issued.

If you have any questions then please reach out to:

GitLab Dedicated Team Product Manager: Andrew Thomas | <athomas@gitlab.com>
Support Engineering Manager: John Lyttle | <jlyttle@gitlab.com>  
