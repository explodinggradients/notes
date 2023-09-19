---
title: Searching in Zendesk
description: Support Operations documentation page for searching in Zendesk
canonical_path: "/handbook/support/readiness/operations/docs/zendesk/searching"
---

## Basic search

To perform a basic search, click the magnifying glass icon in the top-right of
any page within Zendesk. This will reveal a textbox you can type your search
into. After typing your search query, hit the enter/return key on your keyboard.

This will bring up the search results page. The results from your search are
separated into tabbed sections:

- Tickets
- Articles
- Users
- Organizations

If you wish to share these search results, the white `Copy link` button can be
used to create a link that will replicate the search for you to share.

## Advanced searching

This covers searching for more specific information using the Zendesk search
language. All results are still shown much like those within a
[basic search](#basic-search).

#### Searching by tag

To search for objects with a specific tag, you would simply use the syntax:

`tags:tag_name`

As an example, to locate objects using the tag `skip_2fa_automation`, you'd use:

`tags:skip_2fa_automation`

You can search for the negation of this by putting a minus in front of it:

`-tags:tag_name`

If you wanted to search for objects with multiple tags, you'd encapsulate them
in double quotes:

`tags:"tag_name tag_name"`

As an example, if you wanted to find all objects that contains the tags `gold`
and `sev1`, you'd do:

`tags:"gold sev1"`

#### Searching by status

To search by ticket status, you would use the syntax:

`status{operator}status_name`

The status names (and order) are:

1. new
1. open
1. pending
1. hold
1. solved
1. closed

The comment operators are:

| Operator | Meaning                  |
|:--------:|--------------------------|
| `:`      | Equal to                 |
| `<`      | Less than                |
| `<=`     | Less than or equal to    |
| `>`      | Greater than             |
| `>=`     | Greater than or equal to |

You can search for the negation of this by putting a minus in front of it:

`-status:open`

#### Searching by custom organization field

To search by a custom organization field, you use the format:

`field_api_name:query``

The common organization field API names are:

- `salesforce_id` - The 18 character SFDC ID
- `sfdc_short_id` - The 15 character SFDC ID
- `support_level` - The support level of the organization
- `account_type` - The type of organization
- `org_region` - The region of the organization
- `aar` - The ARR of the organization (numeric)

A few examples:

Searching for open partners:

`account_type:open_partner`

Searching for organizations with ARR less than 1000:

`aar<1000`

You can search for the negation of this by putting a minus in front of any that
are text-based.

#### Searching by custom user field

To search by a custom user field, you use the format:

`field_api_name:query`

The common user field API names are:

- `gitlab_username` - An agent's GitLab.com username
- `gitlab_user_id` - An agent's GitLab.com user ID

As an example, to find one where the GitLab.com username is jcolyer, you would
do:

`gitlab_username:jcolyer`

You can search for the negation of this by putting a minus in front of any that
are text-based.

#### Searching by custom ticket field

To search by a custom user field, you use the format:

`custom_field_{id}:value``

where `{id}` is the ticket field ID. This one can be less intuitive as it
requires knowing the ticket field ID. The best resource for this would be the
ticket field sync repos (see [useful links](#useful-links) down below).

You can search for the negation of this by putting a minus in front of any that
are text-based.

#### Searching by satisfaction rating

To locate tickets based on satisfaction rating, you would use the format:

`satisfaction:value`

The possible values are:

- bad - A bad rating without a comment
- badwithcomment - A bad rating with a comment
- good - A good rating without a comment
- goodwithcomment - A good rating with a comment
- offered - The survey has been sent but not responded to

You can search for the negation of this by putting a minus in front of any that
are text-based.

## Advanced searching examples

#### Example 1

Task:

- the preferred region of support is AMER
- the support level of the organization is ultimate
- the satisfaction rating was bad (and had a comment)

`custom_field_360018253094:americas__usa tags:ultimate satisfaction:badwithcomment`

#### Example 2

Task:

- all ticket status except new, solved, and closed
- the assignee is Jason
- the SaaS Account problem type is Namesquatting

`-status:new -status:solved -status:closed assignee:Jason custom_field_360011793260:namesquatting_requests`

## Useful links

- [Zendesk search reference](https://support.zendesk.com/hc/en-us/articles/203663226-Zendesk-Support-search-reference)
