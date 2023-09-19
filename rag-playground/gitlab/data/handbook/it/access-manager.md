---
title: "GitLab Access Manager (Deprecated)"
description: "The IT Self Service handbook page provides all of our team members easy access to all of the processes and solutions for IT related services."
---

GitLab Access Manager is a custom built full stack application built by the GitLab IT Engineering team that provides a user interface ("UI") for team members, managers, access approvers, audit reviewers, and IT administrators to centrally approve and manage role-based access to the directory of [tech stack applications](https://about.gitlab.com/handbook/business-technology/tech-stack-applications/) ("SaaS providers").

In FY21-Q4, we launched the [GitLab Sandbox Cloud](/handbook/infrastructure-standards/realms/sandbox/), powered by [HackyStack](https://gitlab.com/hackystack/hackystack-portal) to automate the provisioning of AWS accounts, AWS IAM users, GCP projects, and GCP users. This has allowed us to automate a large portion of our AWS and GCP access requests.

In FY22-Q3, we launched the initial technical discovery and custom development prototype of GitLab Access Manager that will replace access request issues with progressive milestones throughout FY23. All remaining manual provisioning will include a streamlined custom web UI and API integration with all of our tech stack applications for user and role provisioning.

## Reference Links

- **DRI:** [Jeff Martin](https://about.gitlab.com/company/team/#jeffersonmartin), [Dillon Wheeler](https://about.gitlab.com/company/team/#dillonwheeler), [Peter Kaldis](https://about.gitlab.com/company/team/#pkaldis)
- **Stable Counterparts:** [Jeff Burrows (Manager, Security Compliance)](https://about.gitlab.com/company/team/#jburrows001), [Derek Isla (Sr. IT Compliance Manager)](https://about.gitlab.com/company/team/#disla)
- `#gitlab-access-manager` Slack Channel
- **Executive Sponsors:** [Rob Rea](https://about.gitlab.com/company/team/#rrea1), [Craig Mestel](https://about.gitlab.com/company/team/#cmestel)
- [Epics](https://gitlab.com/gitlab-com/business-technology/engineering/access-manager/-/epics)
- [Issue Tracker](https://gitlab.com/gitlab-com/business-technology/engineering/access-manager/-/issues)
- [Access Manager Docs (Preview)](https://docs.access.gitlabenvironment.cloud) (internal)
- [Access Manager Docs (Code)](https://gitlab.com/gitlab-com/business-technology/engineering/access-manager/gitlab-access-manager-docs) (internal)
- [Access Manager Application Code](https://gitlab.com/gitlab-com/business-technology/engineering/access-manager/gitlab-access-manager-app) (internal)
- [YouTube Playlist - Weekly Development Demos](https://www.youtube.com/playlist?list=PL05JrBw4t0KoLbqn20qVAX8f-ZGvbb88V)
- [Google Drive Folder with Slide Decks and Architecture Diagrams](https://drive.google.com/drive/folders/1qY4KCTAM26VEmUPPcKFS8EdK1p3McxU_)
- [Development Roadmap](https://drive.google.com/drive/folders/1W1861aFWo8XBoBYbI95FbRX6zDS2bsAr)

### Current State

**This project is deprecated.**

You can track the real-time progress in [GitLab Access Manager](https://gitlab.com/groups/gitlab-com/business-technology/engineering/access-manager) [epics](https://gitlab.com/groups/gitlab-com/business-technology/engineering/access-manager/-/epics) and [issues](https://gitlab.com/gitlab-com/business-technology/engineering/access-manager/-/issues).

The GitLab Access Manager documentation draft is available at [https://docs.access.gitlabenvironment.cloud](https://docs.access.gitlabenvironment.cloud) for internal education and security compliance review.

The application is in the early stages of design and development. Please follow `#gitlab-access-manager` in Slack for real-time updates.

### Future State

**This project is deprecated.**

Access Manager has back-end automation that uses the API for each SaaS provider to automate user account and role provisioning (after approval) and has scheduled deprovisioning of user accounts based on expiration or offboarding date.

There are several additional features for streamlining access/audit reviews and compliance reporting using the UI, API, or CSV exports.

In other words, the functionality of the application focuses on the automation and auditability of the lifecycle of Identity and Access Management ("IAM") and Role Based Access Control ("RBAC") for team members and our tech stack applications.

It is important to distinguish that Access Manager automates the provisioning process for SaaS Provider systems behind the scenes, and users still use Okta as our single sign-on identity provider. For SaaS Providers that do not support Okta authentication, Access Manager uses the API to provision a local authentication username and password that is automatically deprovisioned when the team member access expires or is offboarded.

### Problems We're Solving

> **TLDR:** It takes 4 "people months" per month to do access requests. Team members and contractors are waiting several days to get applications permissioned. Auditing is manual. Offboarding from applications is manual and time consuming for multiple teams.

- **Access Requests:** The process is manual and time consuming for team members and application provisioners in all departments.
- **Data:** We do not have good data/metrics and SLAs cannot be enforced as a result.
- **Timeliness:** Manual process leads to delays and a lack of consistency in how quickly an access request will be fulfilled.
- **Tech Stack:** Maintaining the list of application approvers in the tech stack is manual and challenging leading to inaccuracy, delays, and compliance risk.
- **Audit:** Providing audit evidence is time consuming and not all systems are covered.
- **Automation:** We do not have a platform that will integrate with OKTA or directly with the 250+ apps not currently managed by OKTA. We cannot automate user onboarding and offboarding as a result.
- **Integrations:** No 3rd party vendors support the provisioning of a large enough number of our tech stack apps (API integrations, etc)

### What is the purpose of GLAM?

> **TLDR:** Custom application built by IT Engineering to automate the lifecycle of Identity and Access Management ("IAM") and Role Based Access Control ("RBAC"). Will improve team member experience across the processes of: onboarding, access requests, audit, and offboarding for our vast technology stack.

#### What Access Manager Does

- Provides a UI interface for team members, managers, access approvers, audit reviewers, and IT administrators
- Approval policies (“entitlements”) and Approval Flows (“access requests”) for user accounts and entity provisioning (group/role/permission/etc) on the respective SaaS Provider or Tech Stack application
- Directory of users and advanced dynamic group rules based on department, group/team, and job family
- Back end automation and notification using Okta API and/or SaaS Provider API.
- Automated deprovisioning of user accounts based on expiration or offboarding date.
- Comprehensive database to streamline access/audit reviews and compliance

#### What Access Manager Does Not Do

- GLAM is not a replacement for Okta SSO.
- It is not a Single-sign on provider, or providing a login screen to different applications. You will continue to use Okta to sign in to those applications.
- It is not a secrets/password storage platform. Generated credentials are sent to 1Password or HashiVault (future state)
- Not part of the GitLab product plans. Focused as an internal corporate tool.

### How does Access Manager help GitLab

#### User Experience and Timeliness

- Provisioning and deprovisioning will take minutes, not days (after approved).
- Team members can use a form-based web UI (with backend database) for streamlined access request approval, automated provisioning, and audit management that augments OKTA.
- Approvers have streamlined UI dashboard for current requests, history of approvals, and upcoming access reviews. We also use Slack notifications for approver efficiency.

#### Ease of Process Maintenance

- Reduces manual administrative tasks by automating role-based entitlement and ad-hoc requests.
- Allows us to use dynamic group (department/role) rules for automating access for non-Okta applications.
- Replaces access request Markdown issues and (iteratively) most manual provisioning for users and roles.
- Uses custom built API integrations with Okta (for managed applications) and the vendor API for non-Okta managed tech stack applications to automatically provision (or deprovision) access.

#### Auditability

- Comprehensive logging and auditability of all approval and action flow transactions.
- Easy to generate audit reports for security compliance to perform reviews of least privilege and access across multiple filter criteria.

### Features and Functionality

> This is an excerpt of the [documentation](https://docs.access.gitlabenvironment.cloud) that is only available to team members during early development.

- [Directory and Relationships](https://docs.access.gitlabenvironment.cloud/docs/architecture/features/directory-relationships) - Database relationship mapping for users, groups, roles, applications, and application permission roles
- [Profile Mapping](https://docs.access.gitlabenvironment.cloud/docs/architecture/features/profile-mapping) - Auto association of group memberships based on Okta/HRIS metadata.
- [Access Approvals](https://docs.access.gitlabenvironment.cloud/docs/architecture/features/approvals) - Approval flows for requesting access to a role
- [Scheduled Access Review](https://docs.access.gitlabenvironment.cloud/docs/architecture/features/access-review) - Approval flows for reviewing (auditing) access after pre-configured duration (customizable per role).
- [Slack and Email Notifications](https://docs.access.gitlabenvironment.cloud/docs/architecture/features/notifications) - Slack bot for improved user experience and efficiency for approval transactions. Email confirmations of transactions for multi-factor notification and approver searchability.
- [API Integration](https://docs.access.gitlabenvironment.cloud/docs/architecture/features/api-integration) - API connection to most tech stack applications to perform automated IAM provisioning.
- [Access Provisioning](https://docs.access.gitlabenvironment.cloud/docs/architecture/features/provisioning) - Action flows for provisioning IAM users or role mappings
- [Automated Deprovisioning](https://docs.access.gitlabenvironment.cloud/docs/architecture/features/deprovisioning) - Scheduled expiration dates for access removal based on employment or contract end date that trigger Action Flows for de-provisioning IAM users or roles.
- [Comprehensive Logging](https://docs.access.gitlabenvironment.cloud/docs/architecture/features/logging) - Logging and auditability of all approval and action flow transactions.
- [Audit Reports](https://docs.access.gitlabenvironment.cloud/docs/architecture/features/audit-reports) - Easy to generate reports for security compliance to perform reviews of least privilege and access across multiple filter criteria.
