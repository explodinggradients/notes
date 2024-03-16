---
title: "Security Compliance, Dedicated Markets Team"
---

## <i class="fas fa-bullseye" style="color:rgb(110,73,203)" aria-hidden="true"></i> Security Compliance (Dedicated Markets) Mission

Our Mission is to advance customer trust with a focus on customers operating in highly regulated industries or who otherwise have unique security and compliance requirements. We will accomplish this mission by:

1. Enabling [GitLab Dedicated](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/#gitlab-dedicated) to be the most trusted DevSecOps offering in the market, demonstrated by security certifications and attestations.
1. Achieving and maintaining industry-specific security certifications such as [FedRAMP]({{< ref "fedramp-compliance" >}}) and [FIPS 140-2 compliance](https://docs.gitlab.com/ee/development/fips_compliance.html#fips-compliance) for the U.S. Public Sector.
1. Applying compliance automation and compliance-as-code guardrails to minimize [toil](https://sre.google/sre-book/eliminating-toil/) and enable product, development, and infrastructure teams.
1. Use our own product ([dogfooding]({{< ref "values#dogfooding" >}})) to meet key security controls, improve our offering, and demonstrate to customers how they can do the same.

For more information on the direction of the GitLab Dedicated category, please see [this page](https://about.gitlab.com/direction/saas-platforms/dedicated/).

## <i class="far fa-lightbulb" style="color:rgb(110,73,203)" aria-hidden="true"></i> Core Competencies

As a member of the [Security Assurance]({{< ref "security-assurance" >}}) sub-department, and fork of the existing [Security Compliance team]({{< ref "../security-compliance" >}}), we share many of the same core competencies. The difference between our teams is in the product/system scope (GitLab Dedicated and any future offerings for highly regulated markets) and the security certifications we are pursuing.

1. [Security Certifications, Attestations, and Initiatives]({{< ref "../../security-assurance/dedicated-compliance/certifications" >}})
   - External Audit Coordination
   - [Gap Assessments/Readiness Assessments]({{< ref "gap-analysis-program" >}})
1. [Observation and Remediation Management]({{< ref "observation-management-procedure" >}})
   - Identifying control weaknesses and gaps (observations)
   - Remediation recommendations
   - Tracking remediation plans to completion
1. [Continuous Monitoring of GitLab's Security Controls]({{< ref "sec-controls" >}}) which are mapped to applicable regulatory requirements and security certifications/frameworks we have committed to.
   - [User Access Reviews]({{< ref "access-reviews" >}})
   - [Business Continuity Plan (BCP)](https://about.gitlab.com/handbook/business-technology/gitlab-business-continuity-plan/) and [Information System Continuity (ISCP)]({{< ref "information-system-contingency-plan-iscp" >}}) testing
1. Industry and Regulatory Monitoring and Insights
   - Monitoring drafts and changes to relevant laws, executive orders, directives, regulations, policies, standards, and guidelines.
   - Collaborating on responses to relevant RFIs, RFQs, RFPs, and requests for public comment.
   - Monitoring changes government contractual language that could impact public sector security and compliance posture.

Some of our work is [not public]({{< ref "confidentiality-levels#not-public" >}}) for now. Please see the [internal handbook](https://internal.gitlab.com/handbook/engineering/fedramp-compliance/) to find out more about what our team is working on, or reach out to us.

## <i class="fa-solid fa-magnifying-glass"></i> Vision and Focus Areas

Security Compliance is part of the [2nd line of defense](https://www.isaca.org/resources/isaca-journal/issues/2018/volume-4/roles-of-three-lines-of-defense-for-information-security-and-governance#:~:text=While%20the%20three%20lines%20of,explore%20ways%20to%20optimize%20outputs) and our goal is identify and treat risks early before they have more severe impacts later on (i.e. regulatory or reputational). We strive to partner with the 1st line of defense (Engineering, Product, and other parts of the organization) to shift compliance left where it is both more effective and less burdensome. To achieve that vision, we need to focus on the following areas and solicit feedback from other parts of the organization:

- Meet our stakeholders where they are
   - Learn the key projects, architectures, and technologies of the products we support
- Reduce [toil](https://sre.google/sre-book/eliminating-toil/) for control owners and ourselves
   - Automate controls as part of the 1st line of defense and look for efficiencies
- Modernize and scale
   - Identify and implement Governance, Risk, and Compliance (GRC) best practices and "cloud native compliance" solutions
- Measure success and impact on customer trust
   - Identify actionable key performance indicators (KPIs) and key risk indicators (KRIs) for leadership

## Where we work

The single source of truth for all of our work will soon be the [SecComp Dedicated Markets issue board](https://gitlab.com/groups/gitlab-com/-/boards/5913253?label_name[]=Sub-Department%3A%3ASecComp%20Dedicated%20Markets).

We primarily work out of projects in the [Security Assurance sub-group](https://gitlab.com/gitlab-com/gl-security/security-assurance) including our [team issue tracker](https://gitlab.com/gitlab-com/gl-security/security-assurance/team-security-dedicated-compliance/team-files), the [FedRAMP Certification project](https://gitlab.com/gitlab-com/gl-security/security-assurance/fedramp/fedramp-certification), the GitLab instance inside the FedRAMP Authorization Boundary (limited access, AWS GovCloud), and the [GitLab Dedicated issue tracker](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team).

## How we work

Much of our work is not visible to the rest of GitLab due to regulatory mandates outside of our control. In order to bring as much transparency ans visibility into our work, it is critical that we continue to use the gitlab.com/gitlab-com/ group as much as possible, even if used to track tasks that are completed elsewhere. This is important to take extra steps to increase visibility into our work because it directly enables sales for new SaaS offerings, contributes to the security of self-managed GitLab, and makes it possible to enter new markets that were not previously possible.

### Scheduled meetings

We try to avoid meetings at all costs and prefer to work async. We have a weekly call with all of Security Compliance, which includes time for a breakout discussion specific for Dedicated Markets. In addition to that, we also have recurring calls necessary for our FedRAMP program which are necessary for contributing the working group, and logging meeting minutes (external audit artifacts) associated with the configuration control board and compliance sync.

We also have weekly 1:1s and skip levels in line with the GitLab philosophy.

### Agile Project Management

We use an [agile project management](https://about.gitlab.com/solutions/agile-delivery/) approach for our work, leveraging as many GitLab platform features as we can. We use epics, issues, and issue/epic boards to organize our work, as they complement each other. For some of the work, we also use roadmaps, milestones, burndown charts.

#### Issue Board

The single source of truth for all of our work will soon be the [SecComp Dedicated Markets issue board](https://gitlab.com/groups/gitlab-com/-/boards/5913253?label_name[]=Sub-Department%3A%3ASecComp%20Dedicated%20Markets).

We encourage, but currently do not require, the use of issue weights, to log estimated hours, and health status. The exception is for recurring continuous monitoring tasks which do require both of these.

#### Epics

We currently have the following epics:
- Epics tracking our [FedRAMP Continuous Monitoring](https://gitlab.com/groups/gitlab-com/gl-security/security-assurance/fedramp/-/epics?state=opened&page=1&sort=start_date_desc) tasks for that month
- Epics to track quarterly user access reviews
- Epics to track annual contingency/disaster recovery planning and incident response tabletop, which we help facilitate
- Epics tracking annual external audits and penetration tests
- Miscellaneous epics

We are currently investigating whether Epic Boards would add value to the way we organize and view all the work we're doing.

### Labels

At GitLab, we like to label everything. It provides critical metadata on epics and issues because GitLab issues do not [support custom fields](https://gitlab.com/groups/gitlab-org/-/epics/235).

1. **All issues should have our sub-department label: `Sub-DepartmentSecComp Dedicated Markets`.**
1. Team labels: `team::fedramp compliance` or `team::dedicated compliance`.
1. Scoped `seccomp workflow::` labels.

Any new labels should be created at the gitlab-com group level so to that it can be used across sub-groups and projects.

#### Workflow labels

We leverage scoped workflow labels to track different stages of work. These are important because we rely on our issue board for team meetings, reporting up to leadership, metrics, and spreading visibility into our work.

| Open (no workflow label) | `seccomp workflow::triage` | `seccomp workflow::ready` | ~`seccomp workflow::in progress` | `seccomp workflow::blocked` | `seccomp workflow::complete` | `seccomp workflow::cancelled` |
|---------------------------|--------------------------|-------------------------|-------------------------------|---------------------------|----------------------------|-----------------------------|
| Backlog. Issues that are drafts, not ready for triage, or otherwise not necessary to report on the team's Issue Board. (Might Do) | Skip to `seccomp workflow::ready` if work is well defined. These issues need peer review or further refinement and prioritization so they can be included in the Ready bucket. (Should Do) | Prioritized backlog - these issues will be picked up as other issues are closed. (To Do) | Issues that are being actively worked by the team and should have a health status and an assignee. Stale issues with this label should be moved to blocked or cancelled. | Issues that are blocked and need a resolution plan or escalation. Move to `seccomp workflow::in progress` once unblocked. | Issue closed because work is completed as described. | Issue closed because the work was cancelled because it was no longer needed or relevant. |

### Milestones and burndown charts

Currently, we use monthly milestones and a burnup/burndown chart to track recurring FedRAMP continuous monitoring tasks. [Here is an example](https://gitlab.com/groups/gitlab-com/gl-security/security-assurance/-/milestones/4#tab-issues). The work itself is taking place within the FedRAMP Authorization Boundary, however this allows us to increas visibility into that work and include it in metrics. For more informatioin on these tasks, including how the issues are imported at the beginning of every month, please refer to [this document](https://gitlab.com/gitlab-com/gl-security/security-assurance/fedramp/fedramp-certification/-/blob/main/conmon_templates/Importing%20ConMon%20Issues.md?ref_type=heads).

## <i class="fa-solid fa-chart-mixed" style="color:rgb(110,73,203)" aria-hidden="true"></i> Metrics and Measures of Success

1. [Security Control Health](/handbook/security/performance-indicators/#security-control-health)
1. [Security Observations](/handbook/security/performance-indicators/#security-observations-tier-3-risks)
1. [FedRAMP Vulnerability Posture (limited access)](https://app.periscopedata.com/app/gitlab/1125380/FedRAMP-Vulnerability-Posture)
1. [Vulnerability Deviation (Exception) Requests](https://gitlab.com/gitlab-com/gl-security/security-assurance/team-security-dedicated-compliance/poam-deviation-requests/insights/#/issues)

## <i class="fas fa-id-card" style="color:rgb(110,73,203)" aria-hidden="true"></i> Contact the Team

|  Program | DRI | Responsibilities |
| --- | --- | --- |
| Security Compliance (Dedicated Markets) team manager | [@corey-oas](https://gitlab.com/corey-oas) | FedRAMP Authorization Program and compliance/certification roadmap for GitLab Dedicated and GitLab Dedicated for U.S. Government)
| GitLab Dedicated security compliance | [@daniel-ch](https://gitlab.com/daniel-ch) | Continuous monitoring, gap assessments, and external audit coordination (e.g. SOC 2 Type 2). |
| FedRAMP Information System Security Officer (ISSO) | [@niben01](https://gitlab.com/niben01) | FedRAMP vulnerability posture reporting, maintaining Plan of Action & Milestone reporting, and deviation requests |
| FedRAMP Continuous Monitoring Program | [@kbray](https://gitlab.com/kbray) | Continuous monitoring improvements and automation, significant change identification, and compliance documentation maintenance |

- Slack
   - Feel free to tag us with `@dedicated_compliance` or `@sec-compliance-team` to reach the entire Security Compliance team
   - The `#sec-assurance` slack channel is the best place for questions relating to our team (please add the above tag)
   - FedRAMP questions should be directed to the `# wg_fedramp` channel
- Tag us in GitLab
   - `@gitlab-com/gl-security/security-assurance/team-security-dedicated-compliance`
- Email
   - `security-compliance@gitlab.com`
- Here are our team's GitLab.com [subgroups and projects](https://gitlab.com/gitlab-com/gl-security/security-assurance/security-compliance-commercial-and-dedicated/team-security-dedicated-compliance)
- Interested in joining our team? Check out more [here]({{< ref "/job-families/security/security-compliance#dedicated-markets" >}})!
