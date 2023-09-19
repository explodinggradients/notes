---
title: "Security Assurance Automation"
---

## A dedicated resource

The Security Assurance department is continuously growing both in terms of personnel and breadth of the program. As we continue to scale, self-operating automated processes will become a critical catalyst to driving mission success.

Security Assurance Automation Engineers are a critical dedicated resource that enable the Security Assurance department through the development, implementation, and maintenance of automated processes and controls.

## How does Security Assurance Automation operate?

### Intake process

Security Assurance Automation maintains an internal [Security Assurance Automation project](https://gitlab.com/gitlab-com/gl-security/security-assurance/governance/security-assurance-automation) that is dedicated to the intake of Security Assurance related automation requests. As these requests are received, Security Assurance Automation Engineers triage and prioritize the requests. Once requests have been prioritized, an Epic is opened at the [GitLab Security Assurance Automation](https://gitlab.com/gitlab-com/gl-security/security-assurance/governance/security-assurance-automation-subgroup) sub-group level if appropriate or handled directly in the issue requesting the work. All work related to the automation request is tracked in its associated Epic.

#### Intake process - Control Related Automations

A specific `control_related_automation_request` template exists and should be used for any requests related to automating a component of control testing. These requests will always be promoted to an epic or added to an existing control-specific epic if one already exists. GitLab strives to have a true [Continous Control Monitoring](https://about.gitlab.com/handbook/security/security-assurance/#security-compliance-commercial-core-competencies) program in place, and iterating to that state for controls often involves many intermediate steps. For this reason, we aim to gather as many details up front about the MVP solution that we can work on and implement immediately for a control automation. Gaining an idea of "where we're going" enables a forward looking approach and allows us to maintain a healthy backlog of work to push forward and adapt as capabilities/systems shift throughout the company.

<a href="https://gitlab.com/gitlab-com/gl-security/security-assurance/governance/security-assurance-automation/-/issues/new?issuable_template=new_automation_issue" class="btn bg-primary text-white btn-lg">Open a Security Assurance Automation Request</a>

### SLAs

The Security Assurance team uses scoped labels to identify the priority and indicate the resolution time of automation requests.

- Priority Label - Security Assurance Automation (SAA) followed by the associated priority number.
- Color - The color of the label.
- Description - Criteria the issue must fit to be assigned the label.
- Provide Solution - The time it will take to update the issue and provide a solution to the automation request.


| Priority | Color | Description | Provide Solution |
| -------- | ---------- | --------- | --- |
| `~"SAA::1"` | Red | These issues have a direct, immediate impact on business continuity AND are critical for compliance engagements. These are “drop everything so the team can do work” types of requests.                 | 1 Business Day |
| `~"SAA::2"` | Orange   | These issues have an effect on business continuity or are critical for compliance engagements. | 3 Business Days |
| `~"SAA::3"` | Yellow | These issues are day to day automations that are not critical but greatly reduce time for manual tasks by the team. The bulk of automation issues will live here.                                  | 4 Business Days |
| `~"SAA::4"` | Blue    | These issues are automation ideas that may not have a clear path forward or need additional resources to accomplish.                                          | 7 Business Days |

### What does Security Assurance Automation own?

The Security Assurance Automation team is continuously engineering new automated solutions to manual processes. Below are a few projects that the team maintains.

#### Feedback Bot

[The Feedback Bot](https://gitlab.com/gitlab-com/gl-security/security-assurance/feedback-bot) - A bot that enables team members to send private feedback to other team members through Slack.

#### Escalation Engine

[The Escalation engine](https://gitlab.com/gitlab-com/gl-security/engineering-and-research/automation-team/escalator) - An engine that allows users to take automated actions on issues based on a predetermined set of criteria. The engine runs in a scheduled CI pipeline.

#### Dashboarding

[Sisense Dashboarding](https://app.periscopedata.com/app/gitlab/1092210/ZenGRC_Observations) - Custom dashboards using our analytic tool that integrates with data sources across GitLab.

[Insight Dashboarding](https://docs.gitlab.com/ee/user/group/insights/index.html#configure-your-insights) - Custom issue analytic dashboards native to GitLab.

#### Compliance control monitoring and evidence gathering automation

Conversion of manual compliance control monitoring and evidence gathering processes to partially or fully automated processes. This will save time and reduce the opportunity for human error or oversight as our control framework expands.

## Security Assurance Automation SDLC

### Planning

The planning stage occurs during 1:1s, bi-weekly sprint planning meetings, and Slack conversations. During this stage, we gather the following information:

- Who is requesting the automation project?
- What are they requesting?
- Why are they requesting this project?
    - What efficiencies will be gained?
    - How much time will be saved?
- When is this project expected to be completed by?
- How is the automation expected to function?

As a result of the planning stage, we determine the feasibility of a particular project and attempt to draw out a rough roadmap to completion.

### Analysis

During the analysis stage, we continue to gather details to support accepted projects. Projects are broken down into individual components to support an agile approach to development. Those individual components are represented as child issues under the project Epic or associated tasks/issues for smaller bodies of work.

Each issue to be worked in a given iteration is assigned a weight. The total weight of the Epic allows us to gauge the level of effort required to accomplish a particular project as well as plan for each bi-weekly iteration so we maintain a consistent velocity.

| Weight | Level of Effort |
| -------- | ---------- |
| 1 | Minimal effort |
| 2 | Moderate effort |
| 3 | High effort |

### Design

During the design stage, we aim to accomplish the following:

- Produce a design for the minimum viable product (MVP) solution that will satisfy the automation project's requirements.
- Design components that are modular
- Design components that can be reused to accelerate future development projects

### Development and Testing

During the this stage, code is written to satisfy the requirements of a particular project. Development is accomplished in an iterative manner through many small changes. Project stakeholders may be consulted to ensure continued alignment with project expectations as code is being written.

Security Assurance Automation Engineers run tests on their code to identify bugs, vulnerabilities, and usability conflicts.

### Implementation

During this stage, code is moved from the Sec Auto Dev pipeline into the Sec Auto Live pipeline. If an automation request requires web hosting or a server, the automation will live in the Sec Auto Live private GCP instance.

Once the code is ready for final review, a team member from Security Assurance or Security Automation will review the code and merge the branch. The project is moved to a "Done" state when the solution is operating in an automated private pipeline.

### Maintenance

Routine and break-fix maintenance of automated controls and processes is performed by Security Assurance Automation Engineers for automation related to the sub-department. Pro-active requests for maintenance can submitted through the [Security Assurance Automation project](https://gitlab.com/gitlab-com/gl-security/security-assurance/governance/security-assurance-automation/-/issues/new?issuable_template=new_automation_issue).

Maintenance tasks will be tracked via GitLab Issues similar to all other automation tasks.
