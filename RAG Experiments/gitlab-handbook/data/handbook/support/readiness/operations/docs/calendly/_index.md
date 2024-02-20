---
title: Calendly Documentation
description: Support Operations documentation page for Calendly
canonical_path: "/handbook/support/readiness/operations/docs/calendly/"
---

## What is Calendly

Calendly is an online appointment scheduling tool the GitLab Support team uses
for scheduling customer calls.

## User management

User management in Calendly is primarily done via the
[Admin Management page](https://calendly.com/app/organization/users). To access
this page after logging in, you would click `My Account` in the top-right of the
page and then select `Admin Management`.

Within this page, you can invite new users, change roles, and remove members.

**Note**: While this is a baseline entitlement for GitLab Support, it is not a
baseline entitlement for the rest of GitLab. As such, non-support users
requesting access to this must submit an access request and it must be reviewed
and approved by a Support Operations Manager.

#### Adding a user

To add a new user, you simply invite them to Calendly via the
[Admin Management page](https://calendly.com/app/organization/users). On that
page, you will click `+ New User` in the top-right of the page. From there, you
will input the email(s) of the user(s) you wish to invite. After inputing the
email(s), click the blue `Next` button. From here, you would select the event
types to add to the user's profile. As we don't do this by default, simply click
the blue `Finish` button. After doing so, the user(s) will be invited to join
the Calendly under our paid subscription.

#### Changing roles

To change a role of a user, locate the user on the
[Admin Management page](https://calendly.com/app/organization/users) and click
the checkbox by their name. After doing so, go to the top of the page and click
the `Change Role` button. Doing so will open a new box with a dropdown
containing a list of all roles. Simply select the new role to use and then click
the blue `Apply` button.

#### Removing a user

To remove a user, locate the user on the
[Admin Management page](https://calendly.com/app/organization/users) and click
the checkbox by their name. After doing so, go to the top of the page and click
the `Remove members` button. Doing so will open a new box two options to select:

- Remove members
- Remove members and delete their accounts

You should only ever use the first option (`Remove members`). After ensuring
that option is checked, click the blue `Remove` button.

## Team management

Managing teams in Calendly is done via the team page in question. For Support
Ops, this is normally the
[GitLab Support Calendly team page](https://calendly.com/event_types/team/44431).
On this page, you can do several things, such as creating managing event types
and adding/removing members.

#### Adding a member

To add a member to a team, click the gear icon to the right of the
`+ New Event Type`. Doing so will open a sub-menu with several options. The one
you will want is `Edit Team`. Clicking this will open the
[team settings editor page](https://calendly.com/teams/44431/edit).
From here, you will go to the `Team Members` section and click in the box that
says `Type to add team member`. From here, start typing the new member's name.
Once the Calendly box shows the user in question, click on their name. Doing
so will add them to the list of team members. Unless the user is going to manage
Calendly, leave the `can manage team` box unchecked. Once you are done there,
click the blue `Save` button at the bottom of the page.

#### Removing a member

To remove a member from a team, click the gear icon to the right of the
`+ New Event Type`. Doing so will open a sub-menu with several options. The one
you will want is `Edit Team`. Clicking this will open the
[team settings editor page](https://calendly.com/teams/44431/edit).
From here, locate the member in question and click the blue `Remove` link below
their name. Once you are done there, click the blue `Save` button at the bottom
of the page.

## Creating an event type

To create a new event type for a team, first navigate to the team page. For
Support Ops, this is normally the
[GitLab Support Calendly team page](https://calendly.com/event_types/team/44431).
From there, click the `+ New Event Type` button on the right side of the page.
On the next page, you will need to determine what kind of event type the meeting
is for:

- Round Robin: cycles between all available
- Collective: scheduling for when all selected are available (basically group
  scheduling that takes everyone's availability into effect)
- Group: allows for inviting multiple people to the same meeting

The exact type to use is going to be based on what you are aiming to do.
Normally, we use Round Robin as our default event type.

Once you have decided the event type to use, click the blue button below said
event type. As we use Round Robin as our default, the remaining instructions
will focus on that event type.

The next page will ask for you event details. Here, you will give the event type
a name and a description. You can also specific an event link if you wish to
customize it (it will default to kebab-case). You also are given the option to
pick an event color (we tend to stick to purple to match GitLab).

After you are done with the event details, click the blue `Next` button to
proceed.

On the next page, you will enter the details of when people can book this event.
This can be a bit complicated, so see
[Managing event types](#managing-event-types) for more details there.

After you are done with that, click the blue `Next` button to proceed.

The next page will have you select the team members to use for the event type
and the default location (ie where the meeting is hosted). Click the check boxes
by the names of who you want in the distribution. For the location, you should
always select `Zoom`.

The top of this asks for how the distribution should be done. By default, we
select `Optimize for availability` so that it benefits the customer first and
foremost.

After you are done with that, click the blue `Next` button to proceed.

At this point, your event type is live and ready to be used. There are many more
options you can use for the event type itself, so make sure to review
[Managing event types](#managing-event-types) for more details.

## Managing event types

To manage an event type, locate the event type in question and click on the gear
icon in the top-right of the box. After doing so, click the `Edit` option in the
sub-menu. Doing so will open the event type editor. From here, there are a lot
of options that can be edited.

#### What event is this

Here you can edit the event's name, description, link, and color.

#### When can people book this event

If you had to pick one section to deem the most complicated part of event types,
this would be it. Here you determine:

- when the event can be booked
- who is available at the various times
- how far one can schedule into the future
- duration of the event_types
- buffer time before and after the event

The exact values to use are going to vary depending on the event and the
preferences of those involved in said event. While most of these values are
straight-forward, the "when the event can be booked" bit is complex and can take
a bit to get the hang of.

Due to the complexity of this section, I highly recommend watching the above
linked video. This section often needs to be tweaked and can be daunting if you
are not familiar with doing so.

#### Team members and locations

Here you will determine who is involved in the event type and the default
location the will use. Any team member who could be selected for a meeting
should have the checkbox by their name checked. The default location should
always be Zoom.

While you can set priority for event booking, we do not by default.

#### Invitee Questions

Here you can customize the questions asked when a user tries to create an
event. What exactly goes here will vary based on use case, but some good
questions to have in there might be:

- What is the ticket ID?
- If your organization in unbable to use Zoom, what platform would you like us
  to try to use?

As it will vary based on the event itself, your judgement will be the best guide
on what to put here.

#### Notifications and Cancellation Policy

Here you can edit the notifications and cancellation policy. By default, we do
not customize this option. It should default to
`Calendar Invitations, No Reminders`.

#### Confirmation Page

At this time we do not use this option. You should not change anything here and
it should default to `Calednly confirmation page, no active links`.

#### Collect Payments

At this time we do not use this option. You should not have anything here and
it should state `no payment method`.
