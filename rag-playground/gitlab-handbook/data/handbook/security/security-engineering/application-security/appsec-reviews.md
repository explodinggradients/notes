---
title: "Application Security Review Process"
---
<!-- markdownlint-disable MD052 -->

This page details the application security review process for appsec engineers.
The purpose of application security reviews are to proactively discover and
mitigate vulnerabilities in GitLab developed or deployed applications in order
to reduce risk and ultimately help make the company's mission successful.

An application security review may include any or all of the following stages:

- Threat modeling
- In-depth code review
- Dynamic testing

The results of each stage will inform the review done in the next stage.
Ideally, all new features would receive some threat modeling, with
the latter two stages being performed based on the risk profile. Features
already in development or production can receive an appsec review as
well. The testing done is dependent on the circumstances.

### What does an application security review mean for the team owning the feature?

A security review conducted by the application security team is non-blocking.
This means that the team owning the feature should continue with their development plan,
and the expected time investment should be limited to the time necessary to answer
questions asynchronously.

Security issues found, if any, will be triaged following [the standard process][4].
Application security reviews allow us to discover vulnerabilities that exist in GitLab
before they're discovered by a third party and, if the review is done for new features,
we might catch the vulnerabilities even before they make it into a release. It reduces
risk, gives us a better
understanding of the threat model of the given feature, and allows us to proactively
mitigate vulnerabilities.

## Roles & Responsibilities

### Teams

The team owning the feature should proactively involve the Stable Counterpart in
Epics, Issues, and/or MRs which might require a review or their attention. This is primarily the responsibility of the team's Engineering Manager(s) and the Engineer(s) working on the Issue / MR. Ideal trigger points (in order of preference) are when the Epic/Issue/MR is created/updated, when an engineering proposal is updated, or when an engineer is working on the MR.

Teams should have a bias towards involving the Stable Counterpart, to prevent potential
security-sensitive changes from being overlooked.

### Stable Counterparts

One of the goals of the [stable counterpart][3] is to help identify features that
need security review in the area to which they are assigned. Each week Stable Counterparts should
 review Issue boards and recorded weekly team meetings as part of this.

An Application Security team member is on rotation each week to triage Application Security Reviews.

## What Should Be Reviewed?

The application security review queue is a priority queue of application
features for security review. The priority can range from `priority::1` (Critical)
to `priority::4` (Low/Backlog).

Some guidelines for which features should be added to the queue are:
- All new major features
- Features that have had repeat vulnerabilities
- Features related to authorization or authentication
- Features that handle [Red or Orange data][1]
- Features that work with cryptography or other data protection solutions
- Features which touch on topics mentioned in the [secure coding guidelines](https://docs.gitlab.com/ee/development/secure_coding_guidelines.html)

The idea is to capture features determined to be higher risk for
vulnerabilities. It is quite probable that all features, especially `priority::4`
issues, will not get a full review, but by capturing those that are at higher
risk, we can track additional statistics. For example, how many related
vulnerabilities were reported in the bug bounty program. This data can help us
to help iterate on priority.

### Single Issue / MR Pings

Single Issue/MR pings that can be completed by the engineer on triage rotation
do not need a separate issue. This process is primarily for tracking features
over time. With that in mind, if a ping will need additional review, an issue
should be created.

### Adding Features to the Queue / Requesting a Security Review

Separate issues will be used to track the appsec review process, as this
process could outlive the original issue/merge request.

The process is the same for appsec engineers adding something to the backlog
or for team members requesting a review for a GitLab feature:

1. Create an issue in the [Appsec Reviews issue tracker][2] using the [Appsec Review template](https://gitlab.com/gitlab-com/gl-security/appsec/appsec-reviews/-/issues/new?issueable_tempalte=AppSec%20Review)
    1. Set the title to a unique name for the feature
1. Follow the description in the template

### Assigning Priority

Every issue should have a priority assigned to help team members plan
testing. It is up to the application security engineer creating the issue to
determine priority based on the data available to them. If you are not sure
of the appropriate priority, be conservative and assign a higher priority.
It can always be adjusted given feedback from other team members.

Guidelines for Priority (Not comprehensive, please build upon)

| Priority | Criteria |
|----------|----------|
| priority::1       | Red data, AuthN/AuthZ, Crypto, Single severity::1, Repeat severity::2 vulns |
| priority::2       | Orange data, Single severity::2 vulns |
| priority::3       | Yellow data |
| priority::4       | Only standard secure practices necessary |

### Including Threat Modeling in the review

When [threat modeling]({{< ref "../../threat-modeling" >}}) should be done
during the review add the `threat model::needed` label to the original issue or epic and the
appsec review issue. That way we can track the adoption of threat modeling throughout GitLab. When
the threat modeling step is done the
`threat model::done` label should be added to all involved issues and epics. The process for
threat modeling is further defined in its [own handbook page]({{< ref "./runbooks/threat-modeling" >}}).

### Quantifying interactions

The engineering team has created multiple labels with the purpose of quantifying
interactions done by stable counterparts and tracking the status of these interactions.
Stable counterparts should add the right label depending on the status of the interaction
following the conditions below:

- `~sec-planning::in-progress`: The issue or MR is under review.
- `~sec-planning::pending-followup`: Stable counterpart expects to follow up on the review.
- `~sec-planning::complete`: Review finished with comments.
- `~sec-planning::no-action`: Review completed and no action required.

[1]: https://docs.google.com/document/d/15eNKGA3zyZazsJMldqTBFbYMnVUSQSpU14lo22JMZQY/edit
[2]: https://gitlab.com/gitlab-com/gl-security/appsec/appsec-reviews/issues
[3]: {{< ref "./_index.md#stable-counterparts" >}}
[4]: {{< ref "/handbook/security#issue-triage" >}}
