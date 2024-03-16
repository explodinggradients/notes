---
title: Emails
description: Support Operations documentation page for Zendesk emails
canonical_path: "/handbook/support/readiness/operations/docs/zendesk/emails"
---

## What are Zendesk emails

As per
[Zendesk](https://support.zendesk.com/hc/en-us/articles/203663256-Getting-started-with-email-in-Zendesk-Support):

> Email is one way that end-users can submit tickets to Zendesk Support and have
> conversations with agents to resolve their issues.

Basically, Zendesk emails enable an end-user to email an address and have a
ticket created from it. Usage of this varies widely from instance to instance.

## Current Zendesk emails in use

Due to the risk of spam/abuse, we do not publicly list these emails. Please see
the listings via Zendesk itself.

## How to create a Zendesk email

**Note**: While you can connect external email addresses to Zendesk, we do not
do this at GitLab. Instead, we create Zendesk email addresses and have the
GitLab email group forward to said Zendesk email address.

To create a Zendesk email, you first need to go to the Admin Center
([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From
there, you need to go to the Emails page (Channels > Talk and email > Email).

You will then hover over `Add address` towards the top-right of the page. This
will have a drop-down appear. In this drop-down, click
`Create new Zendesk address`. A pop-up box will appear asking you to enter the
username for the address. This should match the username of the GitLab email
address exactly (this avoids a lot of confusion).

After doing this, click the black `Create now` button.

**Note**: This does not create the GitLab email address. To have that done, you
will need to file an
[Access Request issue](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues)
to have it created. Make sure in the issue to specify the Zendesk email address
to forward the emails to.

## How to edit a Zendesk email

**Note**: You can only edit the name of a Zendesk email after creation. If you
need to change the address, you will need to delete the existing one and create
a whole new one.

To edit a Zendesk email, you first need to go to the Admin Center
([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From
there, you need to go to the Emails page (Channels > Talk and email > Email).

From here, locate the email address you wish to edit and then click the `edit`
link on the right-hand side of the email address. Doing so will make a pop-up
box appear.

Here, you can edit the name of the address.

## How to delete a Zendesk email

**Warning!** This can be disastrous and can cause issues. Only do this when you
are 110% sure this needs to be done. An unused email address is annoying but
safe. A deleted email address that was in use causes many issues!

To delete a Zendesk email, you first need to go to the Admin Center
([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)). From
there, you need to go to the Emails page (Channels > Talk and email > Email).

From here, locate the email address you wish to delete, hover over it, and then
click the `delete` link.

link on the right-hand side of the email address. Doing so will make a pop-up
box appear. A pop-up box will appear asking you to confirm the deletion. Click
the black `Delete address` button to confirm.

## Change management

As the Zendesk emails changes are unique in deployment, please see
[Zendesk emails change management](/handbook/support/readiness/operations/docs/change_management#zendesk-emails-change-management)
for more information.

#### Labels to use

For all issues and MRs involving Zendesk emails, the label
`Support-Ops-Category::Zendesk Settings` should be used.

#### Change criticality

Due to the nature and impact adding/editing/deleting Zendesk emails imposes,
all issues/MRs related to Zendesk emails will be classified as
[criticality 1](/handbook/support/readiness/operations/docs/change_criticalities#criticality-1)
