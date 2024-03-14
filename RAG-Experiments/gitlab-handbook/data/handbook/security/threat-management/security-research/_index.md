---
title: "Security Research"
---

## Team Focus

Security Research focuses on identifying, investigating, and developing solutions for security problems for which current best practices are not sufficient. This work is focused on improving the security posture of the product and the company, but always with an eye for contributing new functionality as a differentiator. Additionally, we aim to share our results as widely as appropriate in order to educate fellow team members and bring awareness to the Gitlab Security program.

The team focus for the security research team falls into the two following categories in order to align with the [role description]({{< ref "/handbook/security#security-research" >}}):

- Secure GitLab
- Raise awareness

### Secure GitLab

The Security Research team is part of the Threat Management sub-department. In order to secure GitLab the product and GitLab the company, the security research team will conduct research in areas such as:

- [FOSS applications and dependencies used within GitLab](#gitlab-ecosystem-security-testing)
- GitLab's own codes bases
- Software, hardware and services used by the company

The specific topic is chosen individually per quarter to set as an OKR. As the
security research OKRs are twofold any research steps and outcomes should be
documented in detail such that the other OKR category “raise awareness” can
succeed based on the actual research steps.

### Raise awareness

Typically “raising awareness” is a matter of presenting concrete research
results in a suitable way. This might include:

- Handbook updates
- GitLab documentation updates
- Blog posts
- Conference presentations
- [GitLab Security Tech Notes](https://gitlab-com.gitlab.io/gl-security/security-tech-notes/)
- Papers or other forms of write ups

Even if the outcome of the research is not yielding any spectacular
outcomes the approaches and procedures conducted during the research
phase should be documented and published. Depending on the impact or importance
of the published research the [external communication team]({{< ref "/handbook/security#security-external-communications" >}}) might be involved
within the publication.

## Methodology

### Lightbulb Ideas

Lightbulb ideas are those inspired ideas that are interesting, but may not be
not fully developed. These ideas are interesting to capture as they
encourage discussion and push us to think broadly. They
might become research proposals, a side project, or stay just an idea for
future inspiration. Lightbulb ideas are labeled with
`~security-research::lightbulb`, and the team periodically discusses open
lightbulb ideas during the security research sync.

### Issue Labels

To help align and communicate the goals of our projects, the `~Security Focus::`
and `~Research Goal::` scoped labels are used. One label from each group should
be applied to team issues upon creation.
be applied to :bulb: issues upon creation.

### Security Focus labels

[`~Security Focus::`](https://gitlab.com/groups/gitlab-com/gl-security/-/labels?subscribed=&search=Security+Focus)
labels are used to align an issue with the broad high-level focus areas of the
Security division, based on the risks and priorities of the business. The list
is meant to be stable, but not static.

- `Security Focus::Cloud and Infrastruture Security` - Related to the
secure configuration and use of company production and non-production
cloud and infrastructure environments.
- `Security Focus::Data Security Governance` - Related to the controls,
processes, and policies concerning protection of the data trusted to the
company.
- `Security Focus::Identity and Access Management` - Related to authentication
and authorization to business services and data.
- `Security Focus::Supply-chain Security` - Related to the establishment of
trust in 3rd party code, data, and services necessary for the business.
- `Security Focus::Other` - Related to anything not fitting into the four main focus areas.

### Research Goal labels

[`~Research Goals::`](https://gitlab.com/groups/gitlab-com/gl-security/security-research/-/labels?search=Research+Goal&subscribed=)
 labels are used to communicate the high-level goal of a project.

- `Project Goal::Risk Identification & Quantification` - The project aims to identify,
quantify, and communicate risk(s).
- `Project Goal::Risk Mitigation` - The project aims to reduce or eliminate
a particular risk.
- `Project Goal::Team Maturity::Processes` - The project aims to mature team
processes and improve understanding of how the team works.
- `Project Goal::Team Maturity::Technical Growth` - The project aims to grow
the team's understanding of a technical area. The focus is on learning which
can be applied in future projects.

### Research Topic Discovery

#### Team Members

As experts, security research team members are given space to direct their own
projects. To do so, they use data from a number of different sources to decide
where their focus can be impactful to the business, and the larger security
community.

Some sources of data include:

- Their own security background
- Security questions/problems raised within GitLab
- Outreach with GitLab team members
- Security industry trends

#### Team Manager

The role of the team manager is to support and guide team members in their data
discovery. This includes sharing information that they may collect, and
facilitating communication with other team members. One example of where the
manager can be impactful is raising security questions/problems identified
within the company.

#### Collaborators

As a catch-all category, we invite anyone interested in working with the security
research team to reach out to us. We are always looking for opportunities to
support security and company initiatives.

### Proposals for Research Projects

#### Creating Research Proposals

Prior to the beginning of a quarter, security research team members will propose
a research problem as their focus project. The proposals can be in an entirely
new problem space, or an extension of previous work. In both cases, a proposal
issue is created in the [Security Research issue tracker](https://gitlab.com/gitlab-com/gl-security/security-research/sec-research/-/issues/new?issuable_template=Research%20Proposal)
using the `Research Proposal` template.

As security research entails the study of the unknown, the goal of the proposal issues
is to document known information and the
[research questions](https://en.wikipedia.org/wiki/Research_question) to be
addressed. It is expected that they will be living documents that evolve as
new information is collected.

The issue is used to capture the following information. Full details are
available in the issue template.

- Problem Description
- Research Question(s)
- Business Impact, including the impacted teams
- Project Methods and Outputs
- Tasks for the quarter
- Total project time frame

When a proposal is created, the `~security-research::proposal` label should be
applied. The `@gitlab-com/gl-security/security-research` handle is also cc'd
so that feedback can be collected from team members.

If the work is an extension of previous work, the new issue should be linked
to the previous issue.

#### Proposal Review

Once created, each research proposal will be reviewed by the other team
members, the team manager, and other stakeholders. These reviews are used to
clarify and focus the project, and validate alignment with
business goals. This step of the process is collaborative, and everyone is invited
to provide feedback. The final decision to move forward with the project is
shared between the team member and the team manager.

When a proposal is accepted, the `~security-research::accepted` label should be
applied.

If it is decided between the team member and the team manager to not move
forward, an explanation should be added as a comment to the issue, and the
issue should be closed.

#### Communicating Results

At the end of each quarter, the team member will share with stakeholders their
results. In addition, to meet the team goal of widely
share the results of our work, the results might be used in public
communication. In some cases, due to the sensitivity
of the work, the results will only be shared with the company, until which
time they can be shared more widely.

In addition to the results with stakeholders, a retrospective should be added
to the quarterly issue.

This summary will help to capture:

- What was accomplished for the quarter.
- Tasks that were not completed.
- What went well/What could have been done differently.
- A recommendation on additional work that should be done in the problem space.
- A list of recommended actions to be taken, if applicable, with a focus on the remediation of vulnerabilities, reduction of risk, or strengthing of security controls.

After the summary has been completed, the issue should be closed.

### Current and past Research Projects

#### Package Hunter

Modern dependency management systems like npm and bundler make reusing code easy and ubiquitous. This increases developer productivity and reduces the time to implement applications. However, dependency management systems also bring new challenges. Even for relatively small applications, the number of 3rd-party dependencies quickly grows to several hundred. Because these dependencies are critical to an application's security, they must be carefully vetted for vulnerabilities and malicious code. Performing this task manually is typically not feasible due to the amount of dependency code being vast and developer time is precious. Automated tools are essential in supporting the review of dependencies and preventing malicious dependencies from entering an application's supply-chain. To tackle this challenge, we have developed Package Hunter, a tool to identify malicious npm modules and Ruby Gems. Package Hunter monitors the system calls of application dependencies during their installation. If any suspicious system calls are observed, an alert is created and brought to the attention of the development team.

Package Hunter is open source. Head over to the [project](https://gitlab.com/gitlab-org/security-products/package-hunter) site to try Package Hunter out. There are [instructions](https://gitlab.com/gitlab-org/security-products/package-hunter#installation) for running your own Package Hunter instance and the [CI template](https://gitlab.com/gitlab-org/security-products/package-hunter-cli/-/blob/main/ci/template/Package-Hunter.gitlab-ci.yml) get's you started with analyzing your dependencies in your CI pipeline.

We also welcome contributions. If you are interested in participating in the development of Package Hunter, please see our [contribution guide](https://gitlab.com/gitlab-org/security-products/package-hunter/-/blob/main/CONTRIBUTING.md).

### GitLab Ecosystem Security Testing

The Security Research team within GitLab conducts security assessments on Open Source Software on a regular basis.

This page describes the reasoning, approach and workflows related to those efforts.

#### Strengthening the OSS ecosystem for everyone

GitLab relies on a vast amount of Open Source Software, this is not limited to direct code dependencies but also other components in use within the company. To strengthen the overall security posture of GitLab and all other users of our OSS dependencies the Security Research team maintains [a list of to-be-assessed OSS projects](https://gitlab.com/gitlab-com/gl-security/security-research/ecosystem-security/-/blob/main/projects.yaml) (internal link). The list is filled from the following categories:

- **Cornerstone Project** (1)
  - This category is intended for widely used OSS projects with potentially large code bases.
- **Dependencies of the GitLab Application** (3)
  - Includes code dependencies and other open source projects that ship with GitLab.
- **Developer Tooling Projects** (3)
  - Projects which are used every day on developer machines.
- **Infrastructure/IT Components** (3)
  - Projects we rely on while running the company and the product.

In total there are ten projects in four different categories to pick from. The categories are to ensure our work has a broad impact. The projects are chosen and prioritized by the following factors:

- Data access [(red/orange/green)]({{< ref "data-classification-standard#data-classification-levels" >}})
- GitLab API scopes used (if any)
- Functionality provided, especially aiming for high-impact features like:
     - authentication and authorization
     - file access
     - up/download handling
     - handling of secrets
- Adoption within and beyond GitLab, how widely is the project used?


When a project from this list gets assessed the spot on the list will be filled with another project to always keep the funnel filled.

#### Documentation

Every project and relevant artifacts will be documented internally in the  [sec-research](https://gitlab.com/gitlab-com/gl-security/security-research/sec-research/) repository while the project is ongoing. This repository should be the SSOT for any results and will contain the raw artifacts, write-ups and any PoCs if applicable.

Once the project is concluded and any security issues identified are closed, public facing documentation will be published in the [Threat Management tech notes](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-public/red-team-tech-notes) repository. Where applicable, blog posts containing in-depth technical background on the research will be created in collaboration with the the External Security Communications team.

#### Metrics

We're capturing the following metrics for the Ecosystem Security Testing to
gain insight into overall progress and impact of the program:

1. Review issues closed per quarter
1. Issues identified per review
1. GitLab improvement issues opened per review

To measure `Review issues closed per quarter` and `Issues identified per review`, the following labels were created in the [Ecosystem Security issue tracker](https://gitlab.com/gitlab-com/gl-security/security-research/ecosystem-security/-/labels) (internal link):

- `~EcosystemSecurity::Project`
- `~EcosystemSecurity::Finding`

In order to measure `GitLab improvement issues opened per review` the following label
can be used in the [`gitlab-com`](https://gitlab.com/gitlab-com) and [`gitlab-org`](https://gitlab.com/gitlab-org) groups:

- `~SecResearch Followup::Ecosystem`

### Code Review Sessions

Upon [request from team members](https://gitlab.com/gitlab-com/gl-security/security-research/sec-research/-/issues/new?issuable_template=Code%20review%20session)(internal link) the Security Research team will host "Code Review Sessions"
in which we'll pair on security reviews for a given piece of code. Those sessions will be
recorded.

The reviews will all be around vulnerability identification.

The intention for these sessions is learning on both sides, challenge us with some
interesting new technologies or software concepts, and in return we'll do our best to
share our approaches in vulnerability identification to the given codebase.

### Vulnerability Disclosure Guidelines

Vulnerability disclosure can be a delicate process and there is no one-size-fits-all approach for reporting parties. Within the Security Research Team we'll try to report each vulnerability the most effective way, focusing on timely remediation within our GitLab's infrastructure and fix on the vendor's side while respecting embargoes which might be in place.

For third party software listed in our [tech stack](https://about.gitlab.com/handbook/business-technology/tech-stack-applications/) any vulnerability disclosures should be coordinated with the respective owner of the tech stack item. They might have additional contacts on the vendor side, or more context how to implement a temporary mitigation for an identified vulnerability.

Depending on the actual risk and exposure it might be needed to further limit the information around the disclosure. In such cases it is recommended to involve the [SIRT]({{< ref "sirt" >}}).

## Bug bounties and speaker fees

As a result of Security Research it might occur that a team member gets offered
a bug bounty for some reported vulnerability which has been identified during
their working hours at GitLab. In such a case the payment of the bounty should
be instead donated to a charity by the vendor.

The same should be done for potential speaker fees which might be offered for
conference presentations which are held on behalf of GitLab.

Any kind of bug bounties/fees being offered based on privately conducted
research and speaking engagements are of course not required to be donated to
charity.
