---
title: "Security Automation"
---

![Security Automation Workflow](https://docs.google.com/drawings/d/e/2PACX-1vRXr9HELOOYpeZDEH6RJgWxpurkoxbFa_V_NLzVO9ehdFF_L8KV3J9n9lJqfADefUx8ghzVXvGd2m09/pub?w=1305&h=417)

The Security Automation team strives to protect GitLab and our customers as well as save us money through the automation of processes within Security Department teams, our primary customers. Our work is developed by dogfooding the product, similar to any traditional engineering development team at GitLab, and hosted on internal infrastructure co-managed by the Infrastructure Security team. Working closely with the Anti-Abuse team and other product teams, we often bring our research-driven and internal automations to the product for all to benefit through escalating levels of dogfooding. The following sections describe how to engage with us and how we operate as a team:

## 1. Identify Your Needs

Teams within the Security Department are on the bleeding edge of the security needs and optimizations necessary for the health, growth, and maturity of the organization and the product. The Security Automation team is their focused software development research and development arm for internal automations and their possible evolution into product features. We are here to assist in any or all parts of the DevSecOps lifecycle within the department.

If you have an automation idea or have already started developing one, feel free to engage with our team through office hours or using the product and through our intake process. These needs and optimizations are brought to our attention weekly through our intake process, developed bi-weekly through agile iterations, maintained through quarterly-created tech debt and maintenance epics, and expanded into product features.

## 2. Engage with the Team

### 2.A. Asynchronously through Slack or Email

**Slack Channels**

- #security-automation - our public-facing channel
- #security-automation-team - our private, team-only channel

**Emails**

- security-automation@gitlab.com

### 2.B. Synchronously through Office Hours

Everyone is welcome to join our biweekly office hours by adding our [Security Automation Calendar](https://calendar.google.com/calendar/u/1?cid=Y19vdXFmMjNhYmc3MnRqMjM1b2Q2ODhqc2ZvZ0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t).

### 2.C. Asynchronously through Issues or Epics

Security automation requests can come from anywhere in the form of epics or issues, tagged with the `~secauto` label, either in the `gitlab-org` or `gitlab-com` top-level namespaces. SecAuto team members are required to subscribe to this label, in both namespaces, to optimize our triaging process.

#### 2.C.1. Through Issues

If you already have an issue that needs our attention, please add the `~secauto` label. This is useful for configuration changes, API reviews, or other smaller bodies of work. Depending on the top-level namespace, your issue will appear on one of our two issue intake boards:

- [Internal Issue Board (`gitlab-com`)](https://gitlab.com/groups/gitlab-com/-/boards/5070723)
- [Product Issue Board (`gitlab-org`)](https://gitlab.com/groups/gitlab-org/-/boards/5070728)

#### 2.C.2. Through Epics

For larger bodies of work, create an epic in either the `gitlab-org` or `gitlab-com` top-level namespace. The `gitlab-com` namespace tracks internal-only automation work we are doing for the Security Department that has little to no possibility of becoming a product feature. The `gitlab-org` namespace tracks dogfooding automation work we are doing or intend to do with Product Engineering, likely the Anti-Abuse team, but potentially any product engineering team. Whichever is the case, please use the following template:

```markdown
## Team(s)
<!-- What teams would be involved in making this automation or feature? –>
- Team 1 (@DRI)
…

## Description
<!-- What is this automation or feature and why is it needed? –>

## Savings
<!-- How many hours or dollars per week this automation will save? –>

## When
<!-- When is this needed by?  –>

## Goals
<!-- What high-level goals are attempting to be accomplished? –>

## Definition of Done
<!-- How will you know when this epic is done? –>

/label ~"secauto"
/iteration *"Current::Security Automation" // for isolated issues only
/label *"Staff+ Initiative" // for Staff+ Initiative epics only
```

If you already have bite-sized bodies of work or a list of components of work, feel free to also create epic sub issues as that will help us immensely as we go to plan out the quarter. The more details the better. Depending on the top-level namespace chosen, your epic will appear on one of our two tracking boards:

- [Internal Epic Board (`gitlab-com`)](https://gitlab.com/groups/gitlab-com/-/epic_boards/34210)
- [Product Epic Board (`gitlab-org`)](https://gitlab.com/groups/gitlab-org/-/epic_boards/34211)

## 3. Intake Process

### 3.A. Intake Labels

The security automation team uses this set of labels in both `gitlab-org` and `gitlab-com` to track the lifecycle of an issue or epic during intake.

| Label | Description |
| ----- | ----------- |
| `secauto` | A brand new issue or epic, ready for triaging by the team |
| `secauto::ready` | The issue or epic has been triaged by the team, augmented with planning data as outlined below, and will be pulled in through an upcoming iteration |

### 3.B. Issue and Epic Triaging

Every Tuesday, the Security Automation team will review all of the issues and epics on the boards linked above.

**For issues, we will:**

- Assign a weight (if one is missing)
- Assign a team member to function as the DRI
- Set the description to contain the definition of done or add checkboxes to describe the definition of done if it has multiple verification steps
- Schedule the issue for either the current or an upcoming iteration, depending on when it is needed
- Add the label `secauto::ready` to indicate the issue has been triaged

**For epics, we will:**

- Assign a team member to function as the DRI
- Add an upcoming quarter’s `~FYyy-Qq` label for when the work is expected to be done (unless it is urgent enough to disrupt other epic work during the current quarter)
- Add the label `secauto::ready` to indicate the issue has been triaged

In these ways, all issues and epics will be scheduled within a week of the issue propagating to our boards.

### 3.C. Epic Planning

Within the first month of any quarter during one of our Tuesday meetings, we will plan out the epics for the quarter by dividing it into the many sub issues necessary to meet the epic’s definitions of done. This process involves creating these sub issues and assigning time weights to them based according to the [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence):

- **1** - smallest, easiest, quickly completed
- **2** - small
- **3** - medium
- **5** - large
- **8** - largest, most effort

Issues sized at 8 or higher should be broken down into smaller issues to avoid having issues that linger beyond a two week period.

### 3.D. Tech Debt & Maintenance

At the beginning of each quarter, a separate tech debt and maintenance epic will be created to contain all issues the team feels solves some legacy tech debt accumulated and maintenance items that need to be addressed over the quarter.

### 3.E. Staff+ Initiatives

In parallel to the outlined process of letting Security Department needs directly drive our work, Staff-level engineers on the Security Automation team are able to create and lead a staff+ initiative epic of work. Only one of these initiatives can be active for any quarter and these are subject to manager approval. These initiatives seek to solve higher-level cross-functional security concerns that might not be immediately apparent from departmental needs.

Staff+ initiatives are tracked as epics, using the same template above, in the `gitlab-org` or `gitlab-com` top-level namespaces. They are treated essentially the same as all other epic bodies of work for the Security Automation team and will go through the same quarterly epic planning process. Likely, due to their cross-functional nature, more than one team and DRI will be identified in the epic template. These epics should also bear the `~Staff+ Initiative` label, making them appear on one of the department’s [Staff+ Initiative epic boards]({{< ref "/job-families/security/security-engineer#staff-initiatives" >}}).

### 3.F. Prepared Issues and Epics

This marks the completion of the intake process and all epics and issues that have been prepared through it are ready to be brought into development iterations.

## 4. Development

### 4.A. Development Labels

The security automation team uses this set of labels in both `gitlab-org` and `gitlab-com` to track the lifecycle of an issue or epic during development.

| Label | Description |
| ----- | ----------- |
| `secauto::ready` | The issue or epic has been triaged by the team, augmented with planning data as outlined below, and will be pulled in through an upcoming iteration |
| `secauto::in-progress` | The issue or epic is in the current iteration and is being actively worked on |
| `secauto::blocked` | The issue or epic is being blocked by an external dependency |
| `secauto::cancelled` | The issue or epic has been cancelled |

### 4.A. Development Lifecycle

The Security Automation team operates within two-week iterations, which go from Tuesday to Tuesday. Every other Tuesday, at the same cadence as the intake process, the team meets synchronously to bring prepared issues from the current quarter’s epics (or isolated issues) into the next iteration, being careful not to commit to a sum of issue weight’s too much above our average iteration velocity. In this way, our epics and isolated issue boards function as the primary backlogs for the team.

### 4.B. Average Iteration Velocity (KPI)

The average of the sum of closed issue weights at the time of closure of an issue in an iteration over the last five iterations is our iteration velocity and is the primary KPI ([key performance indicator]({{< ref "/handbook/security/performance-indicators#security-automation-iteration-velocity-average" >}})) for the Security Automation team. We use this metric to determine the health of the team (health status and descriptions on KPI handbook page), self-organizing and improving our internal processes via this handbook page as necessary.

### 4.C. Required Code Review

Every issue with an associated MR must have this MR go through a code review from a team member that was not the DRI for the issue. This reviewer is chosen at random using the `Picker` Slack bot in our `#security-automation-team` channel and then assigned as the reviewer in the MR.

### 4.D. Confirming the Definition of Done

Before issues can be closed out to affect our KPI, we must confirm that they meet their definition of done. This is done in one of three ways:

- The issue’s description is itself the definition of done and a DRI for the issue determines if this definition is met for closing
- The issue contains a definition of done, usually in the form of checkboxes, that will be verified by the issue’s DRI for closing
- The issue contains a definition of done that tags another verification user, usually on another team, that should be assigned to the issue for verification of done
- Through a live show-and-tell demonstration of the solution to the issue so that the team can collectively determine if the solution is viable

## 5. Deployment

Automations are deployed via GitLab CI/CD pipelines to our GCP Security Department subfolder environment, which exists in the same top-level billing organization as most of the other infrastructure that runs GitLab.com. This environment is managed holistically using our [Terraform configuration and modules repositories](https://gitlab.com/gitlab-com/gl-security/terraform) by both the Security Automation team and the Infrastructure Security team.

### 5.A. GKE, Istio, and Knative

Security Automation’s specific subfolder and infrastructure is also managed via a [separate Terraform repository](https://gitlab.com/gitlab-com/gl-security/engineering-and-research/automation-team/terraform), which lays out our GCP Kubernetes, Istio, and Knative infrastructure. By using Knative service architecture, we are able to code in the cloud-agnostic languages of our choosing, providing autonomous, simpler and more iterative pathways to convert our automation services into product features while dogfooding and developing for the GitLab product. Moreover, this environment auto-scales our automations so that we do not have to be as concerned about spikes in GitLab.com usage.

### 5.B. Examples & Important Repositories

- [Authomize Sync](https://gitlab.com/gitlab-com/gl-security/engineering-and-research/automation-team/authomize)
- [SecAuto Example Service](https://gitlab.com/gitlab-com/gl-security/engineering-and-research/automation-team/example-service-python)
- [Spamcheck](https://gitlab.com/gitlab-com/gl-security/engineering-and-research/automation-team/spam/spamcheck)

### 5.C. Infrastructure Security

While the Security Automation team is heavily involved with our environment and the environment of the department, we strive to focus on the development tooling and experience of the environment and not its maintenance and reliability. This is why we work closely with the [Infrastructure Security team]({{< ref "infrastructure-security" >}}) to ensure the health of this environment for automations specific to GitLab.com and its infrastructure.

## 6. Expand

Should an automation written for GitLab.com living in our Knative environment be identified as a possible product feature, the Security Automation team will assist in its development into the product by working closely with the [Anti-Abuse team](https://about.gitlab.com/handbook/engineering/development/sec/govern/anti-abuse) and potentially [other product and development teams](https://about.gitlab.com/handbook/product/categories/#devops-stages) that need to be involved. If this is the case, the following processes should occur:

- Any existing code repositories will be moved from [`gitlab-com/gl-security`](https://gitlab.com/gitlab-com/gl-security) to [`gitlab-org/gl-security`](https://gitlab.com/gitlab-org/gl-security) or to any place in the `gitlab-org` product hierarchy that makes sense for their visibility
- A cross-functional epic should be created in the top-level `gitlab-org` namespace that represents the body of work to expand or extend an automation into a product feature
- A DRI from the Anti-Abuse team should be co-assigned to this new epic
- All future epics, repos, issues, and MRs should exist only in the `gitlab-org` namespace going forward

After this epic is made and scheduled, the Security Automation team will collaborate with all product development teams involved to assist in the expansion of a security automation into a living, breathing full-fledged and jointly developed product feature.
