---
title: "Infrastructure Security Overview"
description: "GitLab's Infrastructure Security provides security oversight of the SaaS."
---

## Team Identity

### Mission

GitLab's Infrastructure Security team is responsible for the planning, execution, and support of proactive initiatives specific to the security of GitLab.com. Its core mission is to become [Infrastructure Department](https://about.gitlab.com/handbook/engineering/infrastructure/)'s stable counterpart in Security. This is achieved by sharing the SRE view of GitLab.com, but with a strong security focus. Infrastructure Security's engagements take place in the form of infrastructure change reviews, SaaS infrastructure access & permissions models, cloud security best practices, operating system security, security monitoring at the host and container level, vulnerability management, and patching policies.

Further details can be found in the [job family description]({{< ref "/job-families/security/infrastructure-security" >}}).

### Vision

We both drive and support the improvement of the security posture of GitLab.com's underlying infrastructure. We operate cross-team and cross-department with relevant stakeholders to provide the required support and help them secure infrastructure. We engage in both ongoing and upcoming endeavor, supporting existing business operations as well as business expansion.

### Team Scope and Distinction

The team's mission overlaps with that of several other teams. That being said, it is important to understand how and where these overlaps take place, and how it all fits together.

#### Infrastructure Security & Infrastructure Department

The [Infrastructure Department](https://about.gitlab.com/handbook/engineering/infrastructure/) is focused on availability, reliability, performance, and scalability efforts of GitLab.com. The fast pace that's intrinsic to running a rapidly growing SaaS can often prove challenging to secure - operational issues, technical & security debt, rapid implementation of new technologies, all present serious security risks that could impact the success of the SaaS in the long run. This is where Infrastructure Security comes into play by serving the Infrastructure Department in 2 specific modes:

- As an **internal consultancy** to help review and challenge decisions from a security standpoint (i.e. how to improve the security of k8s, what to log, what approach to take to access production environments in a secure and auditable way ...)
- As an **external enabler** to simplify security nuances for all the teams and provide smooth engagement to make it easier for all the teams to be better at Infrastructure Security.
  - By contributing to security improvements and enhancements for the different codebases.
  - By building and maintaining tools to improve the audit, detection and response capabilities.
  - By working with the teams in defining policies and procedures to support decision making from an Infrastructure Security perspective.

The role of the Infrastructure Security team can hereby be compared to the role of the Application Security team - the latter helps with the quality of the code, while the former helps with the quality of the infrastructure.

#### Infrastructure Security & Security Incident Response Team - SIRT

The [Security Incident Response Team - SIRT]({{< ref "sec-incident-response" >}}) has historically been the catch-all for most security issues at GitLab. As a result, over the years, SIRT ended up being a temporary owner for many non-SIRT responsibilities. With the introduction of Infrastructure Security, some of these responsibilities have been shifted to this new team. Good examples of some of these responsibilities are vulnerability management and security monitoring.

SIRT's goal is detection and response of anomalies and security events - on the SaaS and on the corporate side of GitLab. As such, SIRT is a very strong partner to Infrastructure Security.


## Team Members

<table>
<thead>
<tr>
<th>Person</th>
<th>Role</th>
</tr>
</thead>
<tbody>
<tr>
<td>Joe Dubail</td>
<td><a href="{{< ref "/job-families/security/infrastructure-security#manager-infrastructure-security" >}}">Manager, Infrastructure Security</a></td>
</tr>
<tr>
<td>Marco Lancini</td>
<td><a href="{{< ref "/job-families/security/security-engineer#principal-security-engineer" >}}">Principal Security Engineer</a></td>
</tr>
<tr>
<td>Paulo Pontes Martins</td>
<td><a href="{{< ref "/job-families/security/infrastructure-security#senior-infrastructure-security-engineer" >}}">Staff Security Engineer, Infrastructure Security</a></td>
</tr>
<tr>
<td>Dhruv Jain</td>
<td><a href="{{< ref "/job-families/security/infrastructure-security#senior-infrastructure-security-engineer" >}}">Senior Security Engineer, Infrastructure Security</a></td>
</tr>
<tr>
<td>Matt Morrison</td>
<td><a href="{{< ref "/job-families/security/infrastructure-security#senior-infrastructure-security-engineer" >}}">Senior Security Engineer, Infrastructure Security</a></td>
</tr>
<tr>
<td>Uday Govindia</td>
<td><a href="{{< ref "/job-families/security/infrastructure-security#senior-infrastructure-security-engineer" >}}">Senior Security Engineer, Infrastructure Security</a></td>
</tr>
</tbody>
</table>


## Working With Us

To request an infrastructure security review, please create an issue using [the security review template](https://gitlab.com/gitlab-com/gl-security/security-operations/infrastructure-security/bau/-/issues/new?issue[title]=Security%20Review%20Request%3A%20{%2B%20Service%2FFeature%20Name%20%2B}&issuable_template=production_readiness)

To engage with the team:

1. [Create an issue](https://gitlab.com/gitlab-com/gl-security/security-operations/infrastructure-security/bau/-/issues) in our issue tracker dedicated to Business as Usual (BAU) activities and general inquiries.
    - It is not necessary to `@mention` anyone. In case you want to mention the whole team, use the `@gitlab-com/gl-security/security-operations/infrastructure-security` handle on GitLab.com.
    - You can also chat with us on Slack in the dedicated `#security-infrasec` channel or by tagging us `@infrasec-team`.
    - You can also refer to the **[InfraSec Team Wiki](https://internal.gitlab.com/handbook/security/infrastructure_security/#team-information)** (internal only) for general information about the team and current projects.
1. The team will triage (and prioritise accordingly) all incoming request during the weekly team sync (usually happening on Tuesday).

## How We Work

### Meetings and Scheduled Calls

Our preference is to work asynchronously, within our project issue tracker as described in [the project management section](#project-management) below.

The team does have set of regular synchronous calls:

- A weekly team sync to discuss progress, blockers, and anything related to the InfraSec team.
    - Everyone in the company is welcome to join.
    - The [agenda is public within GitLab](https://docs.google.com/document/d/1mvmPrG66JpTkj3dbDpnhNybADrUVQwP96DM1trQT89Y) as well.
- A quarterly team retrospective to reflect on what went well in the previous quarter, and discuss what can be improved going forward.
- 1-1s between Individual Contributors and the Engineering Manager.

### Team Pages

- This [Handbook Page](https://about.gitlab.com/handbook/security/security-engineering/infrastructure-security/), which contains general information about the team
- The [Internal Handbook](https://internal.gitlab.com/handbook/security/infrastructure_security/), which is the operational source of truth for the team. Everyone is **encouraged** to check it out for team's information
- The [Infrastructure Security GitLab Sub-Group](https://gitlab.com/gitlab-com/gl-security/security-operations/infrastructure-security), which contains EPICs and repositories
- The [Infrastructure Security **Public** Sub-Group](https://gitlab.com/gitlab-com/gl-security/security-operations/infrastructure-security-public), which contains publicly facing resources (e.g., Docker images, etc.)


### Decision Log

Decisions worthy of deliberate discussion (to evaluate pros and cons with actual data) are tracked in our [Decision Log](https://gitlab.com/groups/gitlab-com/gl-security/security-operations/infrastructure-security/-/issues?scope=all&state=opened&label_name[]=%E2%98%81%EF%B8%8F%20InfraSec&label_name[]=InfraSec%3A%3Adecision).

To start discussing a new decision:

1. [Create a new issue](https://gitlab.com/gitlab-com/gl-security/security-operations/infrastructure-security/team-charter/-/issues/new?issuable_template=decision_log) in the InfraSec Team Charter repo
1. Select the `decision_log` template
1. Fill the data as requested

### Project Management

We use Epics, Issues, and Issue Boards to organize our work, as they complement each other:

- The single source of truth for engineering work is the [InfraSec Sub-Group in GitLab](https://gitlab.com/groups/gitlab-com/gl-security/security-operations/infrastructure-security/-/epics). **All Epics will be collected at this level**.
- Having all projects at this level allows us to use a single list for prioritization and enables us to prioritize
work for different services alongside each other.
- Projects are prioritized in line with [the Roadmap](https://docs.google.com/spreadsheets/d/1wFdCaQWd6cTrXp_N9cL6UA6XVhURrcVan8TUyBbV50U/edit#gid=0) and with the [🎯 InfraSec OKRs](https://gitlab.com/groups/gitlab-com/gl-security/security-operations/infrastructure-security/-/wikis/InfraSec-OKRs).
- The [🎯 InfraSec Milestones](https://gitlab.com/groups/gitlab-com/gl-security/security-operations/infrastructure-security/-/milestones/) provide a snapshot of the current progress against each quarter.

#### Team Planning

- For the **long term strategy** of the InfraSec Team, you can refer to:
    - 📊 [InfraSec Roadmap](https://docs.google.com/spreadsheets/d/1wFdCaQWd6cTrXp_N9cL6UA6XVhURrcVan8TUyBbV50U/edit)
    - 🎯 [InfraSec OKRs](https://gitlab.com/groups/gitlab-com/gl-security/security-operations/infrastructure-security/-/wikis/InfraSec-OKRs)
- From a **tactical point of view**, you can refer to:
    - 🎯 [InfraSec Milestones (quarterly)](https://gitlab.com/groups/gitlab-com/gl-security/security-operations/infrastructure-security/-/milestones/)
    - 🗓 [InfraSec Epics for this quarter](https://gitlab.com/groups/gitlab-com/gl-security/security-operations/infrastructure-security/-/epics?scope=all&utf8=%E2%9C%93&state=opened&label_name[]=InfraSec%3A%3Athis-quarter)
    - 🎛 [InfraSec Initiatives Board](https://gitlab.com/groups/gitlab-com/gl-security/security-operations/infrastructure-security/-/boards/2631020) (for the tasks we are currently working on)

#### Project Ownership

Each project has an owner who is responsible for delivering the project.

The owner needs to:

1. Regularly update the status in the Epic description and milestones.
1. Work with others to move project issues through the boards.

#### Labels

Please use the following labels for **project work only**:

| Label                       | Use Case                                                        |
| --------------------------- | --------------------------------------------------------------- |
| `~"☁️ InfraSec"`            | Team Label (to be included in every project-related issue)      |
| `~"InfraSec::triage"`       | For new issues which need to be triaged                         |
| `~"InfraSec::this-quarter"` | For EPICs committed to the current quarter                      |
| `~"InfraSec::decision"`     | For issues to be included in the Decision Log                   |

### Design Documents

Before starting a new project, the team is **encouraged**
to define software designs through design docs.
These design doc documents the high level implementation strategy and key design decisions with emphasis on the trade-offs that were considered during those decisions.

To start discussing a new design:
1. Create a new MR in the [InfraSec Team Charter repo](https://gitlab.com/gitlab-com/gl-security/security-operations/infrastructure-security/team-charter/-/tree/main/designs) with the Design proposal. You can use [this template](https://gitlab.com/gitlab-com/gl-security/security-operations/infrastructure-security/team-charter/-/blob/main/.gitlab/issue_templates/design_doc.md) as a reference for the structure of the Design doc.
1. Fill the data as requested
1. Mark other elements of the team as reviewers

## Additional Resources

### Onboarding

- Infrastructure Security Team [Onboarding Template](https://gitlab.com/gitlab-com/gl-security/security-operations/infrastructure-security/team-charter/-/blob/master/onboarding/onboarding_template.md)
- [InfraSec Entitlements template](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/blob/master/.gitlab/issue_templates/role_baseline_access_request_tasks/department_security/role_security_engineer_infrastructure_security.md)
