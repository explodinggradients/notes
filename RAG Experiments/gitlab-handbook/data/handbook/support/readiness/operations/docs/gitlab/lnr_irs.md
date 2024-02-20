---
title: L&R internal requests
description: Support Operations documentation page for the L&R internal requests
canonical_path: "/handbook/support/readiness/operations/docs/gitlab/lnr_irs"
---

## What is the L&R IR form?

The L&R IR form is a simple HTMl form generated via GitLab Pages that is used
for L&R IRs.

The source code for the Global variant is located
[here](https://gitlab.com/gitlab-com/support/support-ops/forms/internal-requests-form).

The source code for the US Federal variant is located
[here](https://gitlab.com/gitlab-com/support/support-ops/forms/us-federal-internal-request-form).

## What is the L&R IR processor?

The L&R IR processor is a set of scripts that handle requests sent from the L&R
IR form.

The source code for the Global variant is located
[here](https://gitlab.com/gitlab-com/support/support-ops/other-software/lnr-ir-processor).

The source code for the US Federal variant is located
[here](https://gitlab.com/gitlab-com/support/support-ops/other-software/lnr-ir-processor-us-federal).

## How does it all work?

The L&R IR form, when submitted, sends an AJAX request to trigger a pipeline on
ops.gitlab.net. This then runs the code of the L&R IR processor.

The L&R IR processor will then analyze the response to determine the validity of
the request itself. The end result of this analyzing is a Zendesk ticket being
created.

## Change management

As these are maintained via sync repositories, our standard change management
process applies to all L&R IR form or processor changes. See
[standard change management](/handbook/support/readiness/operations/docs/change_management#standard-change-management)
for more information.

#### Labels to use

For all issues and MRs involving L&R IR form changes, the label
`Support-Ops-Category::Forms` should be used.

For all issues and MRs involving L&R IR processor changes, the label
`Support-Ops-Category::GitLab Projects` should be used.

#### Change criticality

As this tool is very important in the interactions between sales and support,
all issues/MRs related to any of the components of L&R IRs will be classified as
either
[criticality 2](/handbook/support/readiness/operations/docs/change_criticalities#criticality-1)
or
[criticality 3](/handbook/support/readiness/operations/docs/change_criticalities#criticality-2)
