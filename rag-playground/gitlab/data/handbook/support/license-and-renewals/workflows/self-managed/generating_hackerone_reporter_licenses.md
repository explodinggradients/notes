---
layout: markdown_page
title: Generating HackerOne Reporter Award Licenses
description: "How to generate a license for Hacker One reporter award recipients"
category: GitLab Self-Managed licenses
---


## Overview

As part of GitLab's [HackerOne program policy](https://gitlab.com/gitlab-com/gl-security/hackerone/configuration/-/blob/master/program-policy.md#L31-33), a reporter who has submitted three or more valid findings to the program is eligible to receive a one-year self-hosted Ultimate license, supporting up to five users. The source of the request will originate from following [the applicable Security Engineering runbook](https://about.gitlab.com/handbook/security/security-engineering/application-security/runbooks/hackerone-process.html#awarding-ultimate-licenses).

### Actioning the Request

The internal request will come through similar to [these](https://gitlab.zendesk.com/agent/tickets/293134) [examples](https://gitlab.zendesk.com/agent/tickets/293092) and should include:

- The contact's name, which will either be a full name OR their HackerOne 'handle'
- The contact's email, which should end with a `@wearehackerone.com` suffix.

With this information, follow the [procedure to create a new license](/handbook/support/license-and-renewals/workflows/self-managed/creating_licenses.html#create-a-new-license), and ensure you use the following:

- Name: (The contact's full name OR HackerOne 'handle')
- Company: `H1 Reporter Award`
- Email: (The contact's email)
- Users count: `5`
- Plan: `Ultimate`
- Trial: `Yes` (tick the checkbox)
- Starts at: (The current date)
- Expires at: (One year from the current date)
- Notes: (Include a link to the internal request ticket)

See [this generated license](https://customers.gitlab.com/admin/license/1023421) for an example of the completed license.

### Responding to the Request

Once you've generated the license, send a public response on the internal request including the requestor, who will be CC'd, confirming that the license has been generated and sent directly to the contact on the email address provided.
