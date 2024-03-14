---
title: "Security Division Maturity Models"
description: "This page describes how to maintain the Security Division maturity models."
---

## Overview

Our maturity models track specific states and behaviors of our teams over time. This gives us a roadmap to deliver better outcomes with increased efficiency.

## Process

Following our sub-values of [dogfooding](/handbook/values/#dogfooding) and adopting [boring solutions](/handbook/values/#boring-solutions),
the process to create and maintain our maturity models is based on GitLab features only.

Each team of the Security Division should maintain their own maturity models.

### Tooling

Maturity models leverage [Issue Boards](https://docs.gitlab.com/ee/user/project/issue_board.html) to organise and track progress on the various processes. These issue boards are located in projects under the team GitLab group in [https://gitlab.com/gitlab-com/gl-security/](https://gitlab.com/gitlab-com/gl-security/) (for example: [https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-internal/red-team-maturity-model/](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-internal/red-team-maturity-model/) for the Red Team).

Each process of the maturity model is presented by an issue with a short title and a longer description.

[Issue labels](https://docs.gitlab.com/ee/user/project/labels.html) are used to define the current level and state of the process.

### Labels

#### Maturity levels

The `Maturity Level::*` label reflects the level of the process and is **mandatory**.
There are five levels defined along the continuum of the model (see the ["Capability Maturity Model" wikipedia page] for more details):

- `Maturity Level::Initial (1)`
- `Maturity Level::Repeatable (2)`
- `Maturity Level::Defined (3)`
- `Maturity Level::Capable (4)`
- `Maturity Level::Efficient (5)`

These labels must use the color `#6699cc` (blue) for consistency.

#### Maturity

The `Maturity::*` label reflects the current state of the process and is **optional**:

- `Maturity::In progress`

These labels must use the color `#8fbc8f` (green) for consistency.

## Resources

- ["Capability Maturity Model" wikipedia page]

["Capability Maturity Model" wikipedia page]: (https://en.wikipedia.org/wiki/Capability_Maturity_Model)
