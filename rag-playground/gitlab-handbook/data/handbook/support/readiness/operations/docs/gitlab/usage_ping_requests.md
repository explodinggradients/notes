---
title: Usage ping requests
description: Support Operations documentation page for usage ping requests
canonical_path: "/handbook/support/readiness/operations/docs/gitlab/usage_ping_requests"
---

## What is the usage ping request form?

The usage ping request form is a simple HTMl form generated via GitLab Pages
that is sent to [Zapier](https://zapier.com/app/zap/125573569) for processing.

The source code for it is located
[here](https://gitlab.com/gitlab-com/support/support-ops/forms/usage-ping-request-form).

## How does it all work?

The usage ping request form, when submitted, sends an AJAX request to
[Zapier](https://zapier.com/app/zap/125573569). This then runs python code
within the zap itself.

<details>
<summary>Python code in zap</summary>

```python
import requests

def body(hostname, email):
  message = "To whom it may concern,\n\n" \
            "I am requesting the deletion of usage ping data related to the hostname of my GitLab instance: `%s`.\n\n" \
            "Thank you." % (hostname)
  return message

def subject(hostname):
  message = "Usage ping request - %s" % hostname
  return message

email = input_data['email']
hostname = input_data['hostname']

url = 'https://api.mailgun.net/v3/mg.gitlab.com/messages'
files = {
  'from': (None, 'techsupport@gitlab.com'),
  'to': (None, 'incoming+gitlab-com-usage-ping-request-27544965-issue-@incoming.gitlab.com'),
  'subject': (None, subject(hostname)),
  'text': (None, body(hostname, email)),
  'h:Reply-To': (None, email),
}
requests.post(url, files=files, auth=('api', input_data['mailgun_key']))
```

</details>

The zap will create an issue in the
[Usage Ping Request project](https://gitlab.com/gitlab-com/usage-ping-request)
via service desk.

## Change management

As these are maintained via sync repositories, our standard change management
process applies to all usage ping request changes. See
[standard change management](/handbook/support/readiness/operations/docs/change_management#standard-change-management)
for more information.

#### Labels to use

For all issues and MRs involving usage ping request form changes, the label
`Support-Ops-Category::Forms` should be used.

For all issues and MRs involving usage ping request processor changes, the label
`Support-Ops-Category::GitLab Projects` should be used.

#### Change criticality

All issues/MRs related to any of the components of usage ping request will be
classified as either
[criticality 3](/handbook/support/readiness/operations/docs/change_criticalities#criticality-1)
or
[criticality 4](/handbook/support/readiness/operations/docs/change_criticalities#criticality-2)
