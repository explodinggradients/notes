---
title: Guide and Theme
description: Support Operations documentation page for Zendesk Guide and our theme
canonical_path: "/handbook/support/readiness/operations/docs/zendesk/guide"
---

## What is Zendesk Guide?

Zendesk Guide is the system that generates the support portal and related
matters, such as:

- Help articles
- General appearance
- Built-in integrations

A more general way to think of it is it is the Help Center.

## Accessing Zendesk Guide

The main way to access Zendesk Guide is to click the 4 squares in the top-right
of the page and then select Guide. This will open up the Zendesk Guide in a new
tab.

From there, you can click on `Guide admin` in the top-right of the page to get
to the admin page for Zendesk Guide.

**Note**: If you do not see the `Guide admin` link, you are likely in preview
mode. At the top of the screen, this should be indicated, along with a link you
can click to leave preview mode.

## Components of Zendesk Guide

On the admin page for Zendesk Guide, you will find several icons on the
left-hand side of the page:

| Position | Icon Description | Meaning          |
|:--------:|------------------|------------------|
| 1        | Open book        | Manage articles  |
| 2        | Text bubble      | Moderate content |
| 3        | 3 lines          | Arrange content  |
| 4        | Eyeball          | Customize design |
| 5        | User with lock   | User permissions |
| 6        | Gear             | Settings         |

#### Manage articles

This section is where you manage articles that are used in Zendesk Guide. From
here you can publish/unpublish articles, modify labels/author/permissions,
archive/unarchive articles, and delete articles.

Clicking on an article will bring up the editor for said article.

#### Moderate content

This section is where you would do moderation on content. As we do not use user
content (comments, articles, etc.), this section can be ignored.

#### Arrange content

This section let's you rearrange and import content. As we largely do not use
articles, this section can be ignored.

#### Customize design

This section lets you manage the appearance of the support portal. As this
section handles edits to the support portal, see [theme](#theme) for more
information.

### User permissions

This page lets you configure the user permissions for the support portal. This
section is separated into 2 more sections:

###### User segments

This section let's you configure user groupings. With our setup, there should
only be two (and these are built into Zendesk Guide):

- Agents and admins (user tpye: Staff)
- Sign-in users (user tpye: Signed-in users)

You should not need to change this section as it is largely unused.

###### Management permissions

This section let's you manage permissions based on user segments. You should not
need to change this section as it is also largely unused.

#### Settings

This page lets you configure the settings for Zendesk Guide. This section is
separated into 3 more sections:

##### Guide settings

Here you handle content management, security, requests, and integrations
settings for the help center. These settings should not normally be changed
without extensive communication and testing, as they can greatly impact the user
experience.

- Content management
  - Anonymous voting on aritcle - unchecked
  - Spam filter
    - Content moderation - checked
    - Moderate all content
  - User profiles - unchecked
- Security
  - Display unsafe content - checked
  - Require sign in - unchecked
- Requests
  - Sort by oldest comment to newest
  - Enable agents to manage requests from Help Center - unchecked
- Integrations
  - Google Analytics - checked
  - Tracking ID is filled out (do not change this)
- Powered by Zendesk logo - unchecked

#### Language settings

Here you can enable multiple languages for the support portal. We currently do
not use any other language than `English (United States)` at this time. The
Help Center name for this language should be `GitLab, Inc.`.

##### Gather settings

This lets you handle how users can provide ideas and ask questions. Generally
speaking, we do not use this section, as we prefer to keep all documentation
on the GitLab side instead of within Zendesk. You should not need to modify
these settings, which should have all of the checkboxes unchecked.

## Articles

#### Adding articles

To add an article, click the `Add` drop-down in the top-left of the page, and
then click `Article`.

This will bring up the Article creation page. From here, you can enter the
various values relating to the article (title, content, permissions, visibility,
etc.). After doing so, you should save the article by clicking the blue `Save`
button in the top-right of the page.

**Note**: Saving an article does **not** publish it.

To public the article, click the down arrow next to the blue `Save` button and
then click `Publish`.

#### Editing the support portal

Editing the support portal (not the forms within it but the portal appearance
itself) is done via Zendesk Guide. From within Zendesk Guide, you would first
go to the [customize design page](#customize-design). From there, you will see
a list of available themes to use. We currently use the `GitLab Support` theme.

To begin editing the theme, you will first click on `Customize` on the live
theme (bottom-right of the theme box). This will take you to the theme editor
page. Here, you will see the theme options on the left-hand side. Tweaks here
are reflected live via the display on the page (right-side, takes up most of the
page).

To change the page you are live viewing (or the role you are seeing it as), you
will use the two drop-downs at the top of the live preview that read `Templates`
and `Preview role`. These are useful for changing the page itself and the
perspective you are viewing the page as. Some pages can only be shown when in a
specific role, so take this into mind when editing the theme settings.

After making any changes, make sure to publish the changes via the blue
`Publish` button in the bottom-right of the page.

**Note**: Changes here do impact the core theme's code, namely the theme's
`manifest.json` file. If you make changes in the theme's settings, you will want
to ensure the theme's files in the zendesk-theme repo is updated as well. See
[exporting/importing the theme](#exporting-and-importing-themes) for more
details on obtaining the code to use.

## Theme

#### Editing the theme settings

Editing the support portal (not the forms within it but the portal appearance
itself) is done via Zendesk Guide. From within Zendesk Guide, you would first
go to the [customize design page](#customize-design). From there, you will see
a list of available themes to use. We currently use the `GitLab Support` theme.

To begin editing the theme, you will first click on `Customize` on the live
theme (bottom-right of the theme box). This will take you to the theme editor
page. Here, you will see the theme options on the left-hand side. Tweaks here
are reflected live via the display on the page (right-side, takes up most of the
page).

To change the page you are live viewing (or the role you are seeing it as), you
will use the two drop-downs at the top of the live preview that read `Templates`
and `Preview role`. These are useful for changing the page itself and the
perspective you are viewing the page as. Some pages can only be shown when in a
specific role, so take this into mind when editing the theme settings.

After making any changes, make sure to publish the changes via the blue
`Publish` button in the bottom-right of the page.

**Note**: Changes here do impact the core theme's code, namely the theme's
`manifest.json` file. If you make changes in the theme's settings, you will want
to ensure the theme's files in the zendesk-theme repo is updated as well. See
[exporting/importing the theme](#exporting-and-importing-themes) for more
details on obtaining the code to use.

#### Editing the theme code

**Warning**: Tweaking code can severely break the functionality of the support
portal. Broken javascript can result in forms not rendering or working properly.
Ensure you perform thorough testing before ever changing production code.

To edit the code itself, you will want to click the white `Edit code` button
when on the theme editor page. Doing so will bring you to the code editor page
for the theme. Here, you can select the various files that make up the theme and
edit the code itself. This is especially useful for tweaking the JS/CSS/etc. of
the theme to enhance it beyond its normal capabilities.

**Note**: This does require an in-depth knowledge of HTML, CSS, JS (including
jQuery), etc. If you do not feel comfortable doing this, please reach out to
your fellow Support Ops team members or a Support Ops Manager for assistance.

Once you are done editing the code, you can either hit `Ctrl+s` (`Cmd+s` for
Mac) on your keyboard or click the white `Publish` button in the top-right of
the page to save/publish the changes to the Zendesk instance.

#### Exporting and importing themes

To export (i.e. download) a theme, go to the themes page and click the three
vertical dots over the theme you wish to download. After doing so, click the
`Download` option. This will then download a zip file containing all the theme
files. You can extract this to see the theme files as needed.

To import a theme (i.e. upload it), go to the themes page and click the blue
`Add theme` button. This will have a drop-down appear. Click `Import theme` on
the drop-down, then select the zip file from your computer. After doing so, the
theme will be uploaded and added to the Zendesk Guide themes page.

#### Converting the repo into a zip file

To convert the zendesk-theme repo into a zip file, you would want to do the
following:

- For Zendesk Global

```bash
rm -fr ~/zendesk-theme-temp
git clone git@gitlab.com:gitlab-com/support/support-ops/zendesk-global/zendesk-theme.git ~/zendesk-theme-temp
cd ~/zendesk-theme-temp
zip -r zendesk-theme - -x .git .gitignore
mv zendesk-theme.zip ~/Downloads/
```

- For Zendesk US Federal

```bash
rm -fr ~/zendesk-theme-temp
git clone git@ops.gitlab.net:gitlab-com/support/zendesk-us-federal/zendesk-theme.git ~/zendesk-theme-temp
cd ~/zendesk-theme-temp
zip -r zendesk-theme - -x .git .gitignore
mv zendesk-theme.zip ~/Downloads/
```

Either script will create a zendesk-theme.zip file in your `Downloads` folder
you can then use for importing.

## Change management

As articles are maintained via sync repositories, our standard change management
process applies to all Zendesk views. See
[standard change management](/handbook/support/readiness/operations/docs/change_management#standard-change-management)
for more information.

As the theme changes are unique in deployment, please see
[Zendesk theme change management](/handbook/support/readiness/operations/docs/change_management#zendesk-theme-change-management)
for more information.

#### Labels to use

For all issues and MRs involving views, the label `Support-Ops-Category::Theme`
should be used.

#### Change criticality

As theme changes have the potential to cause severe customer impact, all
issues/MRs related to Zendesk themes will be classified as either
[criticality 2](/handbook/support/readiness/operations/docs/change_criticalities#criticality-1)
or
[criticality 3](/handbook/support/readiness/operations/docs/change_criticalities#criticality-2)

Changes to articles are always classified as
[criticality 4](/handbook/support/readiness/operations/docs/change_criticalities#criticality-4)
