---
title: Change management
description: Support Operations documentation page for Pagerduty change management
canonical_path: "/handbook/support/readiness/operations/docs/pagerduty/change_management"
---

## Schedule changes

**Note** This only applies for the non-shadow schedules. For changing shadow
schedules, please see [shadow schedule changes](#shadow-schedule-changes).

#### Create an issue

At the start of each quarter, you should start by making an issue in our
[Pagerduty project](https://gitlab.com/gitlab-com/support/support-ops/other-software/pagerduty)
using the
[issue template](https://gitlab.com/gitlab-com/support/support-ops/other-software/pagerduty/-/issues/new?issuable_template=Quaterly%20schedule%20changes)
to do so.

Fill out all the required areas of the issue based on the template. Make sure
to assign the issue to all the DRIs from the operations team that will be
working it.

The milestone should be the one relating to the first deployment of the new
quarter. So if the new quarter starts 2023-11-01, you'd want to use the
milestone `Support Ops Deployment: 2023-11-01`.

#### Prepare the spreadsheet

At the start of the quarter, you will need to clean up the sheet from the
previous quarter and then prepare it for the current quarter.

To start, you should first generate the new rows you will be needing. To do
this, highlight a group of cells for the schedule (all the columns) consisting
of at least 3 rows, click on the blue circle at the bottom-right of the
highlighted cells, and then drag your mouse down a good number of rows. This
will auto-generate it for you. You can then remove any extra rows at the bottom
you do not need for the following quarter.

With that done, you need to clean out the dropdowns you just created. Highlight
then and hit the `DEL` key on your keyboard to do so (do **not** hit the
backspace key, as it will completely remove the dropdown itself).

After doing so, you need to use either Pagerduty or the previous quarter's
values to determine the values for all the blank dropdowns. Your aim is to show
what the various schedules will look like for the next quarter
*without any changes*.

After that is done, highlight the previous quarters cells, right click, and
hover over `Delete cells`, and click on `Delete cells and shift up`.

You will do this for every schedule on every sheet.

After doing all this, make sure to update the issue you are working out of by
checking the box for `Prepare the spreadsheet` and adding the time spent doing
all this.

#### Unlock the sheet for edits

At the start of the second month of the quarter, you will be asking those
approved to make changes to the dropdowns. For this to occur, you need to unlock
the dropdowns for the approved users.

To do this, go to a sheet you need to unlock, click `Data` at the top menu of
the page, and select `Protect sheets & ranges`. This will bring up all the
protections currently in place.

Locate the one for dropdowns, click on it, and then click `Change permissions`.
Doing so will bring up a modal displaying our custom protections.

For unlocking it, you need to ensure the following boxes are checked:

- Kate Grechishkina <khrechyshkina@gitlab.com>
- support-managers <support-managers@gitlab.com>

After checking the boxes by those entries, click the green `Done` button.

You will need to do this for all locked sheets (the ones with a lock symbol by
their name on the tabs at the bottom of the page).

#### Request edits

At the start of the second month of the quarter, you are ready to perform
perhaps the simplest step: you need to let managers know you are ready for them
to submit edits.

On your issue, ping managers with the following message:

> Greetings @gitlab-com/support/managers !
>
> We are now opening the \[Support Pagerduty Worksheet](<https://docs.google.com/spreadsheets/d/1FdUzVXCZleopfteC2QxW7LJwyylGWGl9hwXHMPkRHbQ/edit?usp=sharing>) for edits for the next quarter!
>
> Please review the spreadsheet and add any edits you wish to see occur for next quarter. The due date for this is YYYY-MM-01

Replacing `YYYY-MM` with the year and month of the last month of the quarter.

After doing all this, make sure to update the issue you are working out of by
checking the box for `Request edits` and adding the time spent doing all this.

#### Lock in the edits

At the start of the third month of the quarter, you will need to lock the sheets
back down.

To do this, go to a sheet you need to unlock, click `Data` at the top menu of
the page, and select `Protect sheets & ranges`. This will bring up all the
protections currently in place.

Locate the one for dropdowns, click on it, and then click `Change permissions`.
Doing so will bring up a modal displaying our custom protections.

For locking it, you need to ensure the following boxes are not checked:

- Kate Grechishkina <khrechyshkina@gitlab.com>
- support-managers <support-managers@gitlab.com>

After un-checking the boxes by those entries, click the green `Done` button.

You will need to do this for all locked sheets (the ones with a lock symbol by
their name on the tabs at the bottom of the page).

#### Implement the changes

During the final month of the quarter, your objective is to setup all the
schedules we use to align with the requested changes in the
[Support Pagerduty Worksheet](https://docs.google.com/spreadsheets/d/1FdUzVXCZleopfteC2QxW7LJwyylGWGl9hwXHMPkRHbQ/edit?usp=sharing).

To do this, there is a script located in our
[Pagerduty project](https://gitlab.com/gitlab-com/support/support-ops/other-software/pagerduty)
called
[handle_pd_changes](https://gitlab.com/gitlab-com/support/support-ops/other-software/pagerduty/-/blob/master/handle_pd_changes).

To utilize this, you will need to download a CSV of each of the locked sheets.
To do that, you will go to the sheet in question, click `File` at the top menu,
hover over `Download`, and then click `Comma Separate Values (.csv)`. Doing so
will download that specific sheet to your computer.

You will then navigate to the location of the
[Pagerduty project](https://gitlab.com/gitlab-com/support/support-ops/other-software/pagerduty)
repo on your local computer.

Run the `bundle` command to download the needed gems. An example out this would
look like:

```bash
jason@laptop:~/dev/gitlab-com/support/support-ops/other-software/pagerduty$ bundle
Using concurrent-ruby 1.2.2
Using i18n 1.14.1
Using minitest 5.18.1
Using tzinfo 2.0.6
Using activesupport 7.0.6
Using bundler 2.4.10
Using faraday-em_http 1.0.0
Using faraday-em_synchrony 1.0.0
Using faraday-excon 1.1.0
Using faraday-httpclient 1.0.1
Using multipart-post 2.3.0
Using faraday-multipart 1.0.4
Using faraday-net_http 1.0.1
Using faraday-net_http_persistent 1.2.0
Using faraday-patron 1.0.0
Using faraday-rack 1.0.0
Using faraday-retry 1.0.3
Using ruby2_keywords 0.0.5
Using faraday 1.10.3
Using faraday_middleware 1.2.0
Using json 2.6.3
Using oj 3.13.23
Using yaml 0.2.1
Bundle complete! 5 Gemfile dependencies, 23 gems now installed.
Use `bundle info [gemname]` to see where a bundled gem is installed.
```

After doing so, you should verify you have the two needed environment variables
set in your local environment (see the project's
[README](https://gitlab.com/gitlab-com/support/support-ops/other-software/pagerduty/-/tree/master#variables-needed)
for more details).

After that has been done, you will run the script with the needed parameters to
create all the overrides needed for the next quarter (again, see the project's
[README](https://gitlab.com/gitlab-com/support/support-ops/other-software/pagerduty/-/tree/master#definitions-for-running-the-script)
for more details).

The output should show you if each override was created correctly. If you see a
status of 201, it was successful. If you see anything else, it did not succeed
(and manual intervention will be required).

An example of the script running would look like:

```bash
jason@laptop:~/dev/gitlab-com/support/support-ops/other-software/pagerduty$ ./handle_pd_changes AMER Emergencies 1 temp.csv
Status 201 for 2024-01-29T16:00:00Z to 2024-01-29T22:00:00Z
Status 201 for 2024-01-30T16:00:00Z to 2024-01-30T22:00:00Z
Status 201 for 2024-01-31T16:00:00Z to 2024-01-31T22:00:00Z
```

After you have run that script, go into Pagerduty and check the corresponding
schedule for accuracy.

Once you have done this for all schedules, check off the corresponding boxes on
the issue you are working out of (and add the time spent).

#### Announce the implementation

The final step is to announce the implementation and close out the issue. You
will first make a comment to ping the managers

> Greetings @gitlab-com/support/managers !
>
> We have now implemented the changes requested from the \[Support Pagerduty Worksheet](<https://docs.google.com/spreadsheets/d/1FdUzVXCZleopfteC2QxW7LJwyylGWGl9hwXHMPkRHbQ/edit?usp=sharing>) into Pagerduty.
>
> Please help communicate this to your reports and remind them to check the schedules for their oncall periods next quarter.

You will then add the time spent for this last bit, add the tag
`SupportOps::Completed`, and close out the issue (ensuring you check off the
corresponding boxes on the issue you are working out of).

## Shadow schedule changes

As these do not have an impact on our production schedules, we can implement
these when requested. These will stem from issues within the
[Pagerduty project](https://gitlab.com/gitlab-com/support/support-ops/other-software/pagerduty).

Implement the changes and let the requester know they are in place. If others
are already using the shadow rotation, make sure to mention it to them as well.

## Escalation policy changes

This can be a very destructive action. As such, only an Operations manager or
Support Readiness Director should make these changes.

## Service changes

This can be a very destructive action. As such, only an Operations manager or
Support Readiness Director should make these changes.

## Spreadsheet setup

The
[Support Pagerduty Worksheet](https://docs.google.com/spreadsheets/d/1FdUzVXCZleopfteC2QxW7LJwyylGWGl9hwXHMPkRHbQ/edit?usp=sharing)
is setup in a very specific way to facilitate planning for the next quarter's
changes.

#### Dropdowns reflect the entire pool of possible people for that dropdown

Each dropdown's content is determined based on the pool of possible people that
could be used. This is done via a range on the People sheet.

Never make edits directly to the dropdown values. If you need to add or remove
someone from the possible options, please do so on the People sheet.

#### We have many protections in place

We have several protections in place on the sheet to prevent editing cells that
are not meant to be edited:

| Name of protection                    | Sheet              | Definition                                      |
|---------------------------------------|--------------------|-------------------------------------------------|
| AMER - Customer Emergencies headers   | AMER - Emergencies | Whole sheet except F2:F1000, M2:M1000, T2:T1000 |
| AMER - Customer Emergencies dropdowns | AMER - Emergencies | 2:1000                                          |
| AMER - CMOC headers                   | AMER - CMOC        | Whole sheet except F2:F1000                     |
| AMER - CMOC dropdowns                 | AMER - CMOC        | 2:1000                                          |
| US Federal headers                    | US Federal         | Whole sheet except F2:F1000, M2:M1000, T2:T1000 |
| US Federal dropdowns                  | US Federal         | 2:1000                                          |
| APAC - Customer Emergencies headers   | APAC - Emergencies | Whole sheet except F2:F1000, M2:M1000           |
| APAC - Customer Emergencies dropdowns | APAC - Emergencies | 2:1000                                          |
| APAC - CMOC headers                   | APAC - CMOC        | Whole sheet except F2:F1000, M2:M1000           |
| APAC - CMOC dropdowns                 | APAC - CMOC        | 2:1000                                          |
| EMEA headers                          | EMEA               | Whole sheet except F2:F1000, M2:M1000           |
| EMEA dropdowns                        | EMEA               | 2:1000                                          |
| Managers headers                      | Managers           | Whole sheet except F2:F1000, M2:M1000, T2:T1000 |
| Managers dropdowns                    | Managers           | 2:1000                                          |
| SSAT headers                          | SSAT               | Whole sheet except F2:F1000                     |
| SSAT dropdowns                        | SSAT               | 2:1000                                          |
