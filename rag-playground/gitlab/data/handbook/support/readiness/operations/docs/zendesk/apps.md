---
title: Apps
description: Support Operations documentation page for Zendesk apps
canonical_path: "/handbook/support/readiness/operations/docs/zendesk/apps"
---

## What is a Zendesk App

A Zendesk App is an application (written in HTML/CSS/JS) that runs in a location
of Zendesk. What it does and how it does it varies greatly from application to
application. Applications can be run in a great many places, but the traditional
locations are:

Applications can be run in a great many places, but the traditional locations
are:

- [Ticket sidebar](https://developer.zendesk.com/apps/docs/support-api/ticket_sidebar)
- [User sidebar](https://developer.zendesk.com/apps/docs/support-api/user_sidebar)
- [Organization sidebar](https://developer.zendesk.com/apps/docs/support-api/organization_sidebar)
- [Navbar](https://developer.zendesk.com/apps/docs/support-api/nav_bar)
- [Background](https://developer.zendesk.com/apps/docs/support-api/background)

You can see more resources on application locations via the
[Zendesk Developer Manifest Reference](https://developer.zendesk.com/apps/docs/developer-guide/manifest#location)
documentation.

Zendesk applications tend to come from one of two areas:

- [Zendesk Marketplace](https://www.zendesk.com/apps/)
- Developed in-house

## Zendesk Global App List

### Advanced Search

Advanced Search is an app that provides a simple visual interface for
constructing complex search queries against tickets, users, and organizations
(orgs). It also enables you to export the search results in a CSV format.

App information:

- Located in the navbar
- This application was developed by
  [Zendesk](https://www.zendesk.com/marketplace/partners/zendesk/) and is
  available in the
  [Zendesk Marketplace](https://www.zendesk.com/apps/support/advanced-search/).

### GitLab Reminders App

The Reminders App appears in the navbar and allows the agent a more specialized
view of tickets they are involved in. It currently shows:

- Tickets assigned to you with a pending/overdue task that are not in a Closed
  state
- Recent tickets you have viewed
- Tickets assigned to you that are not in a Closed state
- Tickets you are CC'd on that are not in a Closed state

It also allows you to quickly manage your tasks by seeing the notes you have
left for said task, when it is due, and a button to quickly mark the task as
done (remove the notes and due date).

App information:

- Located in the navbar
- This application was developed in-house and can be found
  [GitLab Reminders App project](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/zendesk-apps/gitlab-reminders-app).

### GitLab Super App

A plugin controlled app that can do several things GitLab related

The current plugins are:

- **User Lookup**
  > This lets you search gitlab.com for a username or email. It then displays information based on the results.
- **Namespace Lookup**
  > This lets you search gitlab.com for a namespace. It then displays information based on the results.
- **Collaboration Project**
  > This checks the organization for a collaboration project ID. If one exists, it then provides a link to said project.
- **Two Factor Auth Helper**
  > This creates a usable form to checking if a 2FA verification has passed. It calculates the Risk Factor from the Data Classification and modifies it to reflect the passed challenges.
- **Email Suppressions**
  > This searches mailgun for suppressions from bounces (note it does not do it on complaints or unsubscribes). It will display the results (with the message for the suppression).
  >
  > It also gives the option of removing the suppression (if one if found). Doing so deletes it from mailgun and adds an intenral comment on the ticket with the results of the suppression deletion.
- **Fieldnotes**
  > This app checks the [Fieldnotes project](https://gitlab.com/gitlab-com/support/fieldnotes/-/issues) for any existing Issues which reference the current Zendesk ticket ID. If no existing Issues are found, then agents are able to create a new Fieldnotes Issue from directly within the Zendesk ticket.

App information:

- Located in the ticket sidebar
- Restricted by Group:
  - Support AMER
  - Support APAC
  - Support EMEA
- This application was developed in-house and can be found
  [Zendesk Super App project](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/zendesk-apps/gitlab-super-app).

### GitLab Views

The GitLab Views appears in the navbar and allows the agent a more customizable
set if Zendesk views.

App information:

- Located in the navbar
- Restricted by Group:
  - Support AMER
  - Support APAC
  - Support EMEA
  - Support Managers
  - Support Ops
- This application was developed in-house and can be found
  [GitLab Views App project](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/zendesk-apps/gitlab_views).

### Mechanizer

This app incorporates [Mechanizer](https://about.gitlab.com/handbook/support/license-and-renewals/workflows/customersdot/mechanizer.html)
into Zendesk.

App information:

- Located in the ticket sidebar
- Restricted by Group:
  - Support AMER
  - Support APAC
  - Support EMEA
- This application was developed in-house and can be found at
  [Mechanizer project](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/zendesk-apps/mechanizer/)

### Notifications App

This app handles posting notifications at the top of the screen, depending on
various conditions and user settings.

**Note**: This app is *opt-in*. This means nothing will happen unless you modify
your user settings to receive notifications.

App information:

- Located in the Top Navigation of Zendesk Global
- Restricted by Group:
  - Support AMER
  - Support APAC
  - Support EMEA
  - Support Managers
  - Support Ops
- This applicate was developed in-house and can be found at
  [Notification app project](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/zendesk-apps/notification-app)

#### Current events that trigger the app

The following events will send data to the app for notification processing:

- Agent private comment made on ticket
- Agent public comment made on ticket
- Customer public comment made on ticket
- Emergency ticket created
- Escalated ticket created

#### User settings

The current user settings, which will determine what notifications you will (and
will not) recieve are:

- Play notification sound
  - Checking this box tells the app to play the notification sound.
- Notify me for
  - This tells the app what kind of tickets to notify you for
  - Values:
    - Assigned tickets only
    - CC'd tickets only
    - Tickets within my SGG only
    - All tickets
- Notify me about
  - This tells the app what kind of events to notify you for
  - Values:
    - All public comments (agent and customer)
    - Only public comments from agents
    - Only public comments from customers
    - Only private comments
    - All types of comments
- Also notify me for escalated ticket creation
  - This dictates if you want to be notified via the app when an escalated
    organization creates a ticket.
  - **Note** This works *independently* of all other settings.
- Also notify me for emergency ticket creation
  - This dictates if you want to be notified via the app when an emergency
    ticket is created.
  - **Note** This works *independently* of all other settings.

For information on editing your personal user settings, please see
[Zendesk's documentation](https://support.zendesk.com/hc/en-us/articles/4408819930906-Editing-your-personal-settings-in-Zendesk-Chat-Support-accounts#topic_gfh_rqm_4fb).

#### Future iterations

This app is slated to grow consistently with new forms of notifications. Keep an eye on
[Support Readiness milestones](https://gitlab.com/groups/gitlab-com/support/support-ops/-/milestones?search_title=Support+Ops+Deployment&state=&sort=),
the [SWIR](/handbook/support/#support-week-in-review),
and other channels of communications for updates (as well as this seciton of the docs).

### Out of Office

This will enable an agent to mark when they are out of office in Zendesk, which
then updates tickets and makes it visible in the views.

Managers are also able to do this for their reports.

App information:

- Located in the navbar
- Restricted by Group:
  - Support AMER
  - Support APAC
  - Support EMEA
- This application was developed in-house and can be found
  [Out of Office project](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/zendesk-apps/out-of-office/)

### Support Ops Super App

A plugin controlled app that can do several things Support Ops related

The current plugins are:

- **Namespace Lookup**
  > This lets you search gitlab.com for a namespace. It then displays information based on the results. This is related to the one in the GitLab Super App, but instead it shows less information and shows the SFDC IDs it is associated with.

App information:

- Located in the ticket sidebar
- Restricted by Role:
  - Admin
- This application was developed in-house and can be found
  [Support Ops Super App project](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/zendesk-apps/support-ops-super-app).

### Unbabel

Powered by state-of-the-art AI and a worldwide community of translators,
Unbabel delivers translation at enterprise scale. We help you serve customers
in any language, with fast, native-quality translations of your customer
support tickets in Zendesk.

App information:

- Located in the ticket sidebar
- Restricted by Group:
  - Support AMER
  - Support APAC
  - Support EMEA
- This application was developed by Unbabel and is available in the
  [Zendesk Marketplace](https://www.zendesk.com/apps/support/unbabel-for-zendesk-support/).

#### Configuring Unbabel in Zendesk

Every Agent profile in Zendesk needs to be individually configured so that only
tickets submitted in the [supported languages](https://about.gitlab.com/support/portal/#language-support) are translated.

To do this you can use [a javascript snippet](https://gitlab.com/gitlab-com/support/toolbox/snippets/snippets/1971515) created internally.

You can also do the configuration manually by following these steps.

1. Open any existing ticket in Zendesk and navigate to and open the Apps sidebar.
1. Scroll to the Unbabel app and click on Settings.
   ![App](/images/support/Unbabel_App_New.png)
   ![Settings](/images/support/Unbabel_Settings_New.png)
1. Add all the languages *except* those supported by GitLab to the "Languages you speak" list.
   ![Languages](/images/support/Unbabel_Languages_New.png)
1. When you are finished, click the Save button.

#### Replying with a Translation

To request a translation automatically, simply reply as you normally would as
an internal note with the #unbabel hashtag included at the top of your content.
As per our
[working with tickets](/handbook/support/workflows/working-on-tickets.html#what-is-the-working-on-tickets-workflow)
workflow, please remember to assign yourself to the ticket if the ticket
doesn't currently have an assignee when you respond.

Please also ensure that the `unbabel_en`, `unbabel_reply`,
`unbabeled` tags are included, otherwise your response might not be translated
automatically. Should this happen, you will need to add the missing tags, and
create a new internal note with the #unbabel hashtag included at the top of
your content.

Once you submit your response, it may take several seconds for Unbabel to
automatically translate your internal comment, but it can take several minutes
if a human is required to manually translate your internal comment. To view the
status of the translation, you can open the Apps sidebar in the ticket, and
scroll down to the **Unbabel for Zendesk Support** box.

![Translation required](/images/support/Unbabel_Translation_Required.png)

After a translated response has been sent to the customer via Unbabel it is
necessary to manually set the ticket status as **Pending** since Unbabel will
incorrectly set the ticket status as **Open**. You must do this with an *empty
comment* (remove any `#unbabel` added by the plugin, before you Submit as
Pending).

#### Excluding Text from Translation

The highlighted code can be skipped for translation by adding 3 brackets around
the text:

```string
<<< text/code >>>
```

The above can also be used to protect sensitive information from a human
translator when sending a translation request.

#### Disabling Unbabel in a Specific Ticket

Sometimes Unbabel is triggered if a customer's signature was written in a
language that requires translation but the customer replies in English, and the
translation is not needed. In this case, there is a way to disable Unbabel in
this specific ticket:

- Open the ticket in question.
- Click Apps > Unbabel for Zendesk Support.
- `Change` the `Customer language` to `English`.

From now on, Unbabel will not be triggered in this ticket.

#### Help with Translation

If for some reason you have difficulty in understanding the automated
translation, an actual human intervention can actually be requested. Simply
click the link `Can’t understand the translation?` in the Unbabel app box and
this will send your response for translation to Unbabel editors.

#### Best Practices for Unbabel

As indicated in the training session, please keep in mind of the following best
practices when writing a response for translation.

- Respond in one language
  - It is likely that you can speak another language and understand what the
    customer is trying to say. Please ensure that you only use the English
    language when responding tickets as the system may not detect the language
    correctly.
- Copy only the body of the content that needs translation.
  - When referring to a quoted texts from our customers, please only use the
    content that requires translation. Including snippets/code/elements may
    take more time to translate and could result in a mistranslation.
- Mind the punctuation.
  - Punctuation can be sometimes tricky for Unbabel so please be sure there are
    no unnecessary periods/punctuations in between.
- Single Word Use
  - It is likely that the response you are sending may be lost in translation,
    for example the word `pass` would differ to a `boarding pass`.

#### Zendesk Triggers

Unbabel relies on two Zendesk triggers to work properly. These should *never*
be changed, as it can cause significant problems.

- [Unbabel for agent](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=20010334&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360057239500)
- [Unbabel for user](https://gitlab.com/search?utf8=%E2%9C%93&group_id=2573624&project_id=20010334&scope=&search_code=true&snippets=false&repository_ref=master&nav_source=navbar&search=id%3A+360057239480)

#### Zendesk Super App

A plugin controlled app that can do several things Zendesk related

The current plugins are:

- **Due date picker**
  > This allows you to customize what the Due Date for a Task ticket is set for. By default, Zendesk only allows setting the date. This enables you to set the date, time, and timezone.
  >
  > You can also set the Due Date Note and disable (or enable) task notifications using this app.
- **Escalated tickets**
  > This searches for tickets under the organization that have been escalated within the last 6 months.
- **Related tickets**
  > This looks for tickets related to the current one based off the category (or subcategory) the ticket is currently using. It then displays up to 5 of them (sorted by the update_at value of the ticket, descending).
- **Support Uploader**
  > A simple app to create FTP credentials for a ticket.
- **Attachments**
  > Displays attachments present on the ticket.

App information:

- Located in the ticket sidebar
- Restricted by Group:
  - Support AMER
  - Support APAC
  - Support EMEA
- This application was developed in-house and can be found
  [Zendesk Super App project](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/zendesk-apps/zendesk-super-app).

## Zendesk US Federal App List

Zendesk US Federal has some similiar apps as Zendesk Global. The ones they have
in common are:

- [Advanced Search](#advanced-search)
- [GitLab Reminders App](#gitlab-reminders-app)
- [Out of Office](#out-of-office)
- [Ticket Redaction App](#ticket-redaction-app)

### Architecture Diagrams

This app uses the Organization field `AM Project ID` to check for an existing
Account Management project. If it finds it, it will then link to that
project’s Architecture Diagram.

**NOTE**: The AM Project ID field is manually populated. To get that added in,
you would want to submit a Support Ops Project issue.

App information:

- Located in the ticket sidebar
- This application was developed in-house and can be found
  [GitLab Architecture project](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/zendesk-apps/gitlab-architecture).

### Due Date Picker

This is a GitLab built app that allows you to customize what the Due Date for a
Task ticket is set for. By default, Zendesk only allows setting the date. This
enables you to set the date, time, and timezone.

App information:

- Located in the ticket sidebar
- This application was developed in-house and can be found
  [Due Date Picker project](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/zendesk-apps/due-date-picker).

### GitLab User Lookup

This app looks in Salesforce and GitLab.com for a contact or account based on
the requestor’s email address and provided GitLab.com username. If it finds a
GitLab.com account, it will present some basic account information as well as
the membership of the user (and the corresponding plans of said memberships).
The app also does checks to determine if the requester is an enterprise user.
If it determines they are, it displays this in the app's output and auto-tags
the ticket using the `enterprise_user` tag.

App information:

- Located in the ticket sidebar
- This application was developed in-house and can be found
  [GitLab User Lookup](https://gitlab.com/gitlab-com/support/support-ops/zendesk-global/zendesk-apps/gitlab-user-lookup).

### Show Related Tickets

This uses the ticket subject to search for other tickets with a similar
subject. This helps to locate potentially related tickets you can check to see
how they were solved.

App information:

- Located in the ticket sidebar
- This application was developed by
  [Zendesk](https://www.zendesk.com/marketplace/partners/zendesk/) and is
  available in the
  [Zendesk Marketplace](https://www.zendesk.com/apps/support/show-related-tickets/).

## Understanding Zendesk Apps

Before you can start creating and editing apps in Zendesk, it is important to
understand the ins and outs of both Zendesk Apps and
[Zendesk Apps framework](https://developer.zendesk.com/documentation/apps/app-developer-guide/using-the-apps-framework/).

There is a lot to this, so the Zendesk documentation is the best resource you
have to learn the various ins and outs. This training documentation will cover
what is viewed at "the most important" parts, but it is highly recommended you
read and reference the
[Zendesk developer documentation](https://developer.zendesk.com/documentation/apps/app-developer-guide/getting_started/)
as often as possible.

### ZAT

ZAT, or Zendesk App Tools, is a ruby gem that makes working with Zendesk Apps
locally considerably easier. It is highly recommended you install it on your
computer:

```bash
gem install rake
gem install zendesk_apps_tools
```

To update it:

```bash
gem update rake
gem update zendesk_apps_tools
```

Sometimes on Mac terminal, you will get write permission error. You may use:

```bash
sudo gem update rake
sudo gem update zendesk_apps_tools
```

Note: ZAT is having issues with Ruby version `3.0.0 and plus`. You'll likely
need to use old stable versions like `2.6.3p62`

### manifest.json

This file is used to configure you application. As such, it is very important
and vital it is accurate.

The common configuration settings are:

| Setting          | What it does | Required? |
|------------------|--------------|:---------:|
| name             | Specifies the name of the app | Y |
| author           | Specifies the author of the app | Y |
| version          | Specifies the app version | Y |
| frameworkVersion | Specifies the framework version to use | Y |
| location         | Specifies where the app appears | Y |
| defaultLocale    | Specifies the locale of the app | Y |
| parameters       | The parameters to pass to the app during installation | N |
| domainWhitelist  | The domains to allow use of secure parameters | N |
| private          | Specifies whether the app can be only be installed in the app developer's account or not | N |

### Location

This setting determines where the app will appear and run. This is a very
important setting. The first setting determines the product type location, and
within that setting you can specify many other configurations, including the
physical location the app will appear in. For the product type location, we
always use `support`.

The physical locations are as follows:

| String                 | Location/Purpose |
|------------------------|------------------|
| `ticket_sidebar`       | The right side of all ticket view pages |
| `new_ticket_sidebar`   | The right side of all new ticket pages |
| `ticket_editor`        | A button on the ticket editor box |
| `nav_bar`              | An icon on the left-side navigation bar |
| `top_bar`              | An icon on the right side of the top menu |
| `user_sidebar`         | The right side of all user view pages |
| `organization_sidebar` | The right side of all organization view pages |
| `background`           | The app runs in the background and does not display anywhere |
| `modal`                | Used when the app creates modals |

Within the physical location settings, you can include more configuration
settings, with the most common being:

| String     | What it does | Variable type |
|------------|--------------|---------------|
| `autoHide` | Tells the app to auto-collapse on first load | Boolean |
| `autoLoad` | Tells the app to automaticall local (defaults to true) | Boolean |
| `signed`   | Specifies whether or not to use signed URLs | Boolean |
| `url`      | The URL of the page to display in the iframe of the app | String |
| `size`     | The initial app size (configure this in the app instead) | JSON |

As an example, to have an app load "<https://google.com>" automatically in the
ticket sidebar with a starting height of 200px, your configuration block would
look like this:

```json
"location": {
  "support": {
    "ticket_sidebar": {
      "autoLoad": true,
      "url": "https://google.com/",
      "size": {
        "height": "200px"
      }
    }
  }
}
```

As another example, to have your app load in both the user and organization
pages, rendering the locale `assets/iframe.html` file, you would do this:

```json
"location": {
  "support": {
    "user_sidebar": "assets/iframe.html",
    "organization_sidebar": "assets/iframe.html",
  }
}
```

### Parameters

This is where you would define variables you want the app to use during
installation.

### Domain whitelists

If your app is using secure parameters and you plan to make requests outside of
Zendesk, you must whitelist the domains in question. Each parameter is a hash
that contains the following:

- `name`: the name of the parameter
- `type`: the type of parameter
- `secure`: ensures users cannot see the variable value when making HTTP
   requests (you should *always* use this)
- `require`: specifies if the parameter is required for installation

As an example, to use two required parameters (`param1` and `param2`), both of which are text parameters in a secure way, you would do the following:

```json
"parameters": [
  {
    "name": "param1",
    "type": "text",
    "secure": true,
    "required": true
  },
  {
    "name": "param2",
    "type": "text",
    "secure": true,
    "required": true
  }
]
```

During the installation of the app, Zendesk will ask you to give the values for
these parameters. To utilize this in the code of your app, you will use this:

`{{setting.NAME_OF_PARAMETER}}`

Where `NAME_OF_PARAMETER` is the name you gave the parameter in the
manifest.json file.

### init

To create a client instance of the ZAF (Zendesk App Framework) client, you need
to ensure the following is present in the javascript of your app:

```javascript
var client = ZAFClient.init();
```

### App resizing

To resize the app during runtime, you would use the `invoke` class, specifying
you wish to invoke the `resize` function. This is done like so:

```javascript
// First line shown to clarify you use the ZAF client object to do this
var zafclient = ZAFClient.init();
zafclient.invoke('resize', { width: '100%', height: '100px' });
```

### Required javascript library

To utilize the ZAT, you must include the following javascript in your app's
HTML file(s):

```html
<script src="https://static.zdassets.com/zendesk_app_framework_sdk/2.0/zaf_sdk.min.js"></script>
```

### Getting metadata

To get metadata and use it in your app, you need to use the ZAF client's `get`
function. This takes an array of values to get from the ticket metadata, which
you use in a function.

As an example, to get the ticket requester's name and the ticket's organization,
and then log them to the console, you would do the following:

```javascript
// First line shown to clarify you use the ZAF client object to do this
var zafclient = ZAFClient.init();
zafclient.get(['ticket.requester.name', 'ticket.organization']).then(function(data) {
  console.log("Ticket requester name: " + data['ticket.requester.name']);
  console.log("Ticket organization: " + data['ticket.organization']);
});
```

As another example, to get the ticket's due date and the due date notes (a
custom ticket field) and then log them to the console, you would do the
following:

```javascript
// First line shown to clarify you use the ZAF client object to do this
var zafclient = ZAFClient.init();
zafclient.get(['ticket.customField:due_date', 'ticket.customField:custom_field_360017383799']).then(function(data) {
  console.log("Due date": + data['ticket.customField:due_date']);
  console.log("Due date notes:" + data['ticket.customField:custom_field_360017383799']);
});
```

### Making requests

Your app might need to make requests, whether they be "internal" (i.e. within
Zendesk itself) or external. To do this, we use the `request` function of the
client object.

The format of this is *very* close to that of making
[AJAX requests](https://api.jquery.com/jquery.ajax/) in jQuery. The format you
will normally use is:

```javascript
// First line shown to clarify you use the ZAF client object to do this
var zafclient = ZAFClient.init();
zafclient.request({
  method: 'REQUEST_TYPE',
  url: 'URL_TO_USE',
  contentType: 'CONTENT_MEDIA_TO_SEND',
  data: DATA_OBJECT,
  secure: BOOLEAN,
  headers: HEADERS_OBJECT
}).then(function(data) {
  // do stuff
});
```

The exact parameters in the request will vary from request to request.

As an example, if you wanted to update the due date of a ticket, you might do:

```javascript
// First line shown to clarify you use the ZAF client object to do this
var zafclient = ZAFClient.init();
zafclient.request({
  method: 'PUT',
  url: '/api/v2/tickets/123456.json',
  contentType: 'application/json',
  data: JSON.stringify({
    due_at: new Date('2021-01-01').toISOString()
  }),
  secure: BOOLEAN,
  headers: HEADERS_OBJECT
}).then(function(data) {
  console.log('Due date updated to 2021-01-01');
});
```

As another example, if you wanted to make a GET request to gitlab.com to find
information about user ID 987654, using a secure parameter from app
installation, you might do:

```javascript
// First line shown to clarify you use the ZAF client object to do this
var zafclient = ZAFClient.init();
zafclient.request({
  method: "GET",
  url: 'https://gitlab.com/api/v4/users/987654?private_token={{setting.GitLab_token}}',
  secure: true
}).then(function(data) {
  console.log('User email: ' + data.email);
});
```

## How to create a Zendesk App

To create a Zendesk app, you will first make a new folder on your local computer
(where you will build the app) and cd into the new directory:

```bash
jcolyer@jcolyer-Desktop:~$ mkdir my_new_app
jcolyer@jcolyer-Desktop:~$ cd my_new_app
```

From there, run the command `zat new` and fill out the requested details (author
name, author email, app URL, app name, iFrame URI, directory). After doing so,
you will have the baseline files you need to create your application.

```text
jcolyer@jcolyer-Desktop:~/my_new_app$ zat new
Enter this app author's name:
 test
Enter this app author's email:
 test@test.com
Enter this app author's url:
 https://gitlab.com/test/my_new_app
Enter a name for this new app:
 Test App
Enter your iFrame URI or leave it blank to use a default local template page:
 (assets/iframe.html)
Enter a directory name to save the new app (will create the dir if it does not exist):
 (./)
       exist
      create  README.md
      create  assets/iframe.html
      create  assets/logo-small.png
      create  assets/logo.png
      create  assets/logo.svg
      create  manifest.json
      create  translations/en.json
```

From here, you will edit the files for your app. By default,
`assets/iframe.html` will be the main file you will work out of (although you
can have the javascript load from a separate file and work from there if you so
desire).

Once you are done creating your application, you will need to package it. To do
this, run the command `zat package`:

```text
jcolyer@jcolyer-Desktop:~/my_new_app$ zat package
        info  Checking for new version of zendesk_apps_tools
     warning  Your version of Zendesk Apps Tools is outdated. Update by running: gem update zendesk_apps_tools
    validate  OK
     warning  Please note that the name key of manifest.json is currently only used in development.
     package  adding translations/en.json
     package  adding manifest.json
     package  adding README.md
     package  adding assets/logo.png
     package  adding assets/iframe.html
     package  adding assets/logo-small.png
     package  adding assets/logo.svg
     package  created at ./tmp/app-20210920131122.zip
```

Alternatively to this, you can manually package the app using the `zip` command:

```bash
jcolyer@jcolyer-Desktop:~/my_new_app$ zip -r application.zip - -x .git
jcolyer@jcolyer-Desktop:~/my_new_app$
```

The created zip file it what contains your Zendesk App. Go to the Admin Center
([Zendesk Global](https://gitlab.zendesk.com/admin/) /
[Zendesk US Federal](https://gitlab-federal-support.zendesk.com/admin/)), locate
the Apps management pages under `Apps and integrations` > `Apps` >
`Zendesk Support apps`. On this page, click the white `Upload private app`
button in the top-right of the page.

On this page, enter the App's name and select the zip file from your local
computer. After doing so, click the black `Upload` button. A pop-up will appear
asking you to confirm the upload. Click the black `Upload` button once more to
confirm.

After it installs the app, you will be brought to the app management page for
your new app. If you used any parameters, you would add them here. You also have
the option to set role or group restrictions if needed. As a general rule, all
apps that need to be restricted should have group restrictions in place unless
there is a specific need for role restrictions. Once you are done, click the
blue `Install` button.

## How to update a Zendesk App

To update an app, you edit the code and the version (found in the manifest.json
file) and package it up (much like when
[creating an app](#how-to-create-a-zendesk-app)).

After doing so, go to the Admin Center and locate the Apps management pages
under `Apps and integrations` > `Apps` > `Zendesk Support apps`. On this page,
locate the app you are updating, hover over it, and click the down arrow that
appears (next to a gear icon). Click the `Update` option to proceed.

From here, it is basically the same as creating a new app. You select the file
from your local computer, click the black `Upload` link, and the app updates.

## How to deactivate a Zendesk App

**Note** To keep the Apps management page clean, we aim to uninstall an app
instead of just deactivating it.

To deactivate an app, go to the Admin Center and locate the Apps management
pages under `Apps and integrations` > `Apps` > `Zendesk Support apps`. On this
page, locate the app you are deactivating, hover over it, and click the down
arrow that appears (next to a gear icon). Click the `Uninstall` option to
proceed. A pop-up will ask you to confirm the uninstall process. Click the blue
`Uninstall` button to confirm.

## Testing an app

There are two ways to test a Zendesk app before you put it into production:

### Locally

**Note**: This cannot be done if your app is using secure parameters. Instead,
you would need to install the app into the Sandbox and test from there.

To test your app locally, cd into the app directory on your local computer and
then run the `zat server` command. This will start up a ZAT server on your
computer. Once it has booted up, go to a Zendesk URL and put `?zat=true` at the
end. This will now load the apps from your local computer, allowing you to test
out the app locally.

### Via the Sandbox

If your app is using secure parameters, you will need to test via the Sandbox
instead. Follow the process for [creating an app](#how-to-create-a-zendesk-app)
or for [updating an app](#how-to-update-a-zendesk-app) (whichever fits best) to
get the app into the Sandbox and then you can test from there.

## Change management

As these are maintained via repositories, our standard change management process
applies to all Zendesk apps. See
[standard change management](/handbook/support/readiness/operations/docs/change_management#standard-change-management)
for more information.

### Labels to use

For all issues and MRs involving apps, the label
`Support-Ops-Category::Apps` should be used.

### Change criticality

As Zendesk apps tend to have far less of an impact, adding/editing/deleting
Zendesk apps will be classified as either
[criticality 3](/handbook/support/readiness/operations/docs/change_criticalities#criticality-3)
or
[criticality 4](/handbook/support/readiness/operations/docs/change_criticalities#criticality-4)
