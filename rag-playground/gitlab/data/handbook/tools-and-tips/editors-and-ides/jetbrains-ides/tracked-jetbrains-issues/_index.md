---
title: "Tracked Jetbrains Issues"
no_list: true
---

## Overview

This is a list of all JetBrains issues which are relevant to GitLab, and we want to follow/upvote
in hopes that they eventually get fixed.

Here's the main issue trackers to look for existing issues before reporting a new one:

- RubyMine: <https://youtrack.jetbrains.com/issues/RUBY>
- GoLand: <https://youtrack.jetbrains.com/issues/GO>
- WebStorm: <https://youtrack.jetbrains.com/issues/WEB>

Each issue we track should have a `H3` section under the [Open Issues](#open-issues) section below.
This could be in table format, but Markdown tables are hard to maintain, and headers have automatic anchor links.

Here's a template example:

```markdown
### RUBY-30422

- Title: Rename can be invoked in empty string shared_examples
- Link: https://youtrack.jetbrains.com/issue/RUBY-30422/Rename-can-be-invoked-in-empty-string-sharedexamples
- Available In: 2022.3 (if the issue is closed, omit this line if the issue is still open)
- Notes: (anything for easy searching within this page, e.g. mention `noinspection` if this is a
  bug for a false positive `noinspection` comment.
```

When an issue is fixed, verify it yourself, and move the issue's entry from the [Open Issues](#open-issues) to the [Closed Issues](#closed-issues) section for reference by people who may still be on an older IDE version. It can be deleted after it has been fixed for one or two IDE releases.

## Handling of issues related to `noinspection` comments

Many of these issues are related to the [suppression of Code Inspection false positives via `# noinspection ...` comments](https://handbook.gitlab.com/handbook/tools-and-tips/editors-and-ides/jetbrains-ides/code-inspection/#suppressing-false-positives-with-noinspection-comments)

When an issue related to `noinspection` is resolved and included in a released version of the IDE:

1. Search the codebase for the corresponding `noinspection` using the issue id (e.g. `RUBY-25400`)
1. Remove the `noinspection` comment and run `Inspect Code` on the file to ensure it is fixed.
1. Move the issue's entry from the [Open Issues](#open-issues) to the [Closed Issues](#closed-issues) section as described above.

## Open Issues

Keep these sections sorted alphabetically. They are headers so that they can be directly linked.

### RUBY-31540

- Title: Invalid RailsParamDefResolve warning when table name does not match class name
- Link: <https://youtrack.jetbrains.com/issue/RUBY-31540/Invalid-RailsParamDefResolve-warning-when-table-name-does-not-match-class-name>
- Notes:
  - Requires `# noinspection RailsParamDefResolve` and other noinspection comments.
  - This is likely due to our non-standard naming of the `Clusters::Agent` model, where
    the table is named `cluster_agents` and must be overridden with
    `self.table_name = 'cluster_agents'`. This also requires overrides and non-standard
    handling in GraphQL mutations. We should consider renaming this table or model to match
    standard rails naming conventions.

### RUBY-25400

- Title: Programmatically defined constants always produce 'Unresolved reference' error
- Link: <https://youtrack.jetbrains.com/issue/RUBY-25400/Programmatically-defined-constants-always-produce-Unresolved-reference-error#focus=Comments-27-7812554.0-0>
- Notes:
  - Requires `# noinspection RubyResolve`
  - UPDATE 2023-07-10: Got a response from JetBrains here: <https://youtrack.jetbrains.com/issue/RUBY-25400/Programmatically-defined-constants-always-produce-Unresolved-reference-error#focus=Comments-27-7813280.0-0> stating limitations and potential workarounds.

### RUBY-31542

- Title: Cannot resolve attributes on ActiveRecord model which is not in standard location
- Link: <https://youtrack.jetbrains.com/issue/RUBY-31542/Cannot-resolve-attributes-on-ActiveRecord-model-which-is-not-in-standard-location>
- Notes:
  - Requires `# noinspection SqlResolve`. It's just a guess that the non-standard model
    location is the root cause.
  - UPDATE 2023-07-10: Got a response from JetBrains here: <https://youtrack.jetbrains.com/issue/RUBY-31542/Cannot-resolve-attributes-on-ActiveRecord-model-which-is-not-in-standard-location#focus=Comments-27-7813387.0-0> providing some information and requesting more info and follow-up

### RUBY-31543

- Title: Fixtures declared with `let_it_be` from `test-prof` gem cannot be found, and give `RubyResolve` warning
- Link: <https://youtrack.jetbrains.com/issue/RUBY-31543/Fixtures-declared-with-letitbe-from-test-prof-gem-cannot-be-found-and-give-RubyResolve-warning>
- Notes: Requires `# noinspection RubyResolve`

### RUBY-31544

- Title: Cannot find fixtures defined with `RSpec::Parameterized::TableSyntax`, causes `RubyResolve` warning
- Link: <https://youtrack.jetbrains.com/issue/RUBY-31544/Cannot-find-fixtures-defined-with-RSpecParameterizedTableSyntax-causes-RubyResolve-warning>
- Notes: Requires `# noinspection RubyResolve`

## Closed Issues
