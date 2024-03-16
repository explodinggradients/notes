---
title: Sandbox
description: Support Operations documentation page for Zendesk sandbox
canonical_path: "/handbook/support/readiness/operations/docs/zendesk/sandbox"
---

## What is the Zendesk Sandbox

The Zendesk Sandbox is a replica Zendesk instance you can use to test, learn,
replicate, etc. in an environment that is separated from production instances.

We utilize the Zendesk Sandbox in all our change management processes. This
allows us a safe and secure place to test changes/updates/etc. so we can
ensure the implementations we push into production are both stable and well
vetted.

## Where are the sandboxes?

You can locate the sandboxes via:

- [Global](https://gitlab1545832369.zendesk.com/agent/)
- [US Federal](https://gitlabfederalsupport1585318082.zendesk.com/agent)

## How to access the Zendesk Sandbox

With the Sandbox instance, we only have 50% of the seats our production Zendesk
instance has available. As such, not every person has a Sandbox account. To
request one, please utilize an
[access request issue](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new)
to have one provisioned. Please make sure to include:

- Why you need access to it
- How long you need access to it
- If you need heightened permissions
- Why you need heightened permissions (if applicable)
- Which instance's Sandbox access is being requested (Global / U.S. Federal)

The provisioner for these requests will be the Support Operations Manager
(@jcolyer).

When going to login, keep in mind Okta is not able to be used on the sandboxes,
so you will have to login via email address and password.

## What do we use the sandbox for?

We utilize the sandbox heavily to test all change requests. Everything we do
related to Zendesk should be tested in the sandbox first, with the results of
said test reviewed by the requester.

## Test Users and Organizations

To help both facilitate easy testing and keep the sandbox in a clean state,
Support Operations has created some test organizations and users you can use.
Whenever possible, please utilize these organizations and users to test "end
user" experiences.

| User Name                | User Email                        | Organization | Tags |
|--------------------------|-----------------------------------|--------------|------|
| Bronze Test 1            | <bronzetest1@example.com>           | Bronze Test Organization            | bronze                 |
| Bronze Test 2            | <bronzetest2@example.com>           | Bronze Test Organization            | bronze                 |
| Bronze Test 3            | <bronzetest3@example.com>           | Bronze Test Organization            | bronze                 |
| Community Test 1         | <communitytest1@example.com>        | Community Test Organization         | community              |
| Community Test 2         | <communitytest2@example.com>        | Community Test Organization         | community              |
| Community Test 3         | <communitytest3@example.com>        | Community Test Organization         | community              |
| Gold Test 1              | <goldtest1@example.com>             | Gold Test Organization              | gold                   |
| Gold Test 2              | <goldtest2@example.com>             | Gold Test Organization              | gold                   |
| Gold Test 3              | <goldtest3@example.com>             | Gold Test Organization              | gold                   |
| Premium Test 1           | <premiumtest1@example.com>          | Premium Test Organization           | premium                |
| Premium Test 2           | <premiumtest2@example.com>          | Premium Test Organization           | premium                |
| Premium Test 3           | <premiumtest3@example.com>          | Premium Test Organization           | premium                |
| Priority Prospect Test 1 | <priorityprospecttest1@example.com> | Priority Prospect Test Organization | priority_prospect      |
| Priority Prospect Test 2 | <priorityprospecttest2@example.com> | Priority Prospect Test Organization | priority_prospect      |
| Priority Prospect Test 3 | <priorityprospecttest3@example.com> | Priority Prospect Test Organization | priority_prospect      |
| SaaS Prospect Test 1     | <saasprospecttest1@example.com>     | SaaS Prospect Test Organization     | prospect prospect_saas |
| SaaS Prospect Test 2     | <saasprospecttest2@example.com>     | SaaS Prospect Test Organization     | prospect prospect_saas |
| SaaS Prospect Test 3     | <saasprospecttest3@example.com>     | SaaS Prospect Test Organization     | prospect prospect_saas |
| Silver Test 1            | <silvertest1@example.com>           | Silver Test Organization            | silver                 |
| Silver Test 2            | <silvertest2@example.com>           | Silver Test Organization            | silver                 |
| Silver Test 3            | <silvertest3@example.com>           | Silver Test Organization            | silver                 |
| SM Prospect Test 1       | <smprospecttest1@example.com>       | SM Prospect Test Organization       | prospect prospect_sm   |
| SM Prospect Test 2       | <smprospecttest2@example.com>       | SM Prospect Test Organization       | prospect prospect_sm   |
| SM Prospect Test 3       | <smprospecttest3@example.com>       | SM Prospect Test Organization       | prospect prospect_sm   |
| Starter Test 1           | <startertest1@example.com>          | Starter Test Organization           | starter                |
| Starter Test 2           | <startertest2@example.com>          | Starter Test Organization           | starter                |
| Starter Test 3           | <startertest3@example.com>          | Starter Test Organization           | starter                |
| Ultimate Test 1          | <ultimatetest1@example.com>         | Ultimate Test Organization          | ultimate               |
| Ultimate Test 2          | <ultimatetest2@example.com>         | Ultimate Test Organization          | ultimate               |
| Ultimate Test 3          | <ultimatetest3@example.com>         | Ultimate Test Organization          | ultimate               |

If you find you need other test organizations/users, please create an issue via the
Support Operations
[issue tracker](https://gitlab.com/gitlab-com/support/support-ops/support-ops-project/-/issues/new?issuable_template=Support%20Ops%20Issue%20Template).
