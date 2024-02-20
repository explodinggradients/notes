---
title: "IT Self Service"
description: "The IT Self Service handbook page provides all of our team members easy access to all of the processes and solutions for IT related services."
---

This IT Self Service handbook page provides all of our team members with a SSOT knowledge base directory of all the processes and solutions related to IT whether you've just started at GitLab or have been here awhile.

We have several teams at GitLab that focus on specific functions typically handled by an IT organization. Our Tech Stack applications have a wide range of [System Owners](https://about.gitlab.com/handbook/business-technology/#cross-department-system-owners) across the organization that may not be managed day-to-day by the Information Technology department outside of a security and compliance function.

Our handbook is organized per function and result, so the goal of this page is to provide cross-links to other handbook pages and sections that have the answers you're looking for, even if it's on a different department's handbook page. Please contribute any crosslinks if we missed anything.

## Helpdesk

If you can't find what you're looking for in the handbook, please ask in the `#it_help` Slack channel. If you do not have access to Slack (rare), please email `it-help@gitlab.com`.

We have IT Analysts available 24x5 to assist or fix anything you need related to your laptop, applications you use, or credentials used to sign in. You can see all of the applications that we manage in the [IT Tech Stack](#it-tech-stack) below. We escalate to IT Systems Engineers, IT Security, or other team members as needed.

> Our team uses an on-call schedule so please ask in the Slack channel instead of contacting a team member via Slack DM directly.

**Product Related:** For general GitLab or product questions, ask in `#questions`. For performance, outage, or UI bugs or breaking changes with GitLab.com (SaaS), please ask in `#is-this-known`.  You can check the `#production` channel for active incidents related to the GitLab.com service.

**Security Related:** If you have a broader question about security topics that is not blocking you from doing your work, feel free to ask in the `#security` channel where security team members can help answer.

**Emergency Lost Device:** If you lose any device that contains your credentials or GitLab data (laptop, phone, tablet, YubiKey, thumb drive, etc.), report it using `/security` in Slack to engage the [SIRT on-call engineer](https://about.gitlab.com/handbook/security/security-operations/sirt/engaging-security-on-call.html#engage-the-security-engineer-on-call). They will take immediate action to deactivate or wipe compromised devices and/or credentials. If you do not have Slack accessible, you can email `panic@gitlab.com` from your work email address or personal email address (that is on file in Workday).

**Emergency Personal Situation:** If you need emergency support from the GitLab People (HR) Team, please follow the [handbook instructions](https://about.gitlab.com/handbook/people-group/#in-case-of-emergency).

---

## How Can We Help?

There is a lot of information on this page. We've added emoji to help you get started.

- 🆕 If you are onboarding (new to GitLab), this is a helpful section for you to check out.
- 👀 Frequently asked questions

### Team Assistance

- 🆕 [Ask the Helpdesk](#helpdesk)
- 👀 [Account Recovery](#account-recovery) (Password and 2FA/MFA Reset)
- [Create a Security Incident](https://about.gitlab.com/handbook/security/security-operations/sirt/engaging-security-on-call.html)
- [IT Compliance Issues](https://gitlab.com/gitlab-com/business-technology/it-compliance/it-compliance-issue-tracker/-/issues)
- [IT Engineering Issues](https://gitlab.com/gitlab-com/business-technology/engineering/operations/issue-tracker)
- [IT Infrastructure Issues](https://gitlab.com/gitlab-com/business-technology/engineering/infrastructure/issue-tracker/-/issues)
- [IT Security Issues](https://gitlab.com/gitlab-com/business-technology/it-compliance/it-security/-/issues)

### Self Service

- 🆕 👀 [Access Requests](#access-requests)
- [Contractors and Vendors](#contractors-and-vendors)
- [Hardware Orders and Expense Reimbursements](#hardware-orders-and-expense-reimbursements)
- 🆕 👀  [Laptop Configuration Checklist](#laptop-configuration)
- [Laptop Software Upgrades](#laptop-software-upgrades)
- [Mobile Devices](#mobile-devices)
- 🆕 [Onboarding Checklist](#onboarding)
- [Offboarding Checklist](#offboarding)
- 🆕👀 [Security Policies](#security-policies)
- [Tech Stack and User Guides](#tech-stack)
  - 🆕 👀 [IT Tech Stack and User Guides](#it-tech-stack)
  - [Data Team Tech Stack](#data-team-tech-stack)
  - [Finance Tech Stack](#finance-tech-stack)
  - 👀 [Infrastructure Shared Services Tech Stack](#infrastructure-shared-services-tech-stack)
  - [Infrastructure Reliability Tech Stack](#infrastructure-reliability-tech-stack)
  - [People Tech Stack](#people-tech-stack)
  - [Sales Tech Stack](#sales-tech-stack)
  - [Security Tech Stack](#security-tech-stack)

### Team Handbook Pages

See the [Team Directory](#team-directory) for a list of related teams and their handbook pages.

---

## Access Requests

- 👀 Access Requests User Guide
- Baseline Access Entitlements User Guide

## Account Recovery

- 1Password Recovery
- GitLab.com Password Reset
- GitLab.com 2FA Reset
- Google Password Reset
- Okta Password Reset
- Okta 2FA Reset

## Contractors and Vendors

- Contractor Onboarding User Guide
- Contractor Onboarding Manager Guide
- Contractor Onboarding Runbook

## Hardware Orders and Expense Reimbursements

All laptops should be purchased by IT unless you have been granted an exception.

- Laptop Order User Guide (New Hire)
- 👀 [Laptop Replacement User Guide (Refresh)](/handbook/it/guides/laptop-replacement)
- 👀 Laptop Order and Shipping Status Runbook
- 👀 Laptop Model Standards Policy
- Laptop Exceptions Policy
- 👀 Laptop Replacement and Refresh Policy
- Laptop Replacement and Refresh Runbook
- 👀 Laptop Decommission and Return Policy
- 👀 Laptop Troubleshooting User Guide
- Laptop Repairs and Warranty User Guide

You can purchase your own monitors, peripherals, and accessories based on the guidance in the expense reimbursement policy.

- 👀 [Home Office Equipment and Supplies Reimbursement Policy (Monitors and Peripherals)](https://about.gitlab.com/handbook/finance/procurement/office-equipment-supplies/)

When you leave GitLab, home office equipment and supplies under $1,000 USD per item don't need to get returned and are okay for you to keep. Any reimbursed expenses greater than $1,000 USD per item (or over) is classed as company property and you will be required to return the item(s).

In most cases, this means that you get to keep your monitor(s), keyboard, mouse, headphones, webcam, standing desk, etc. See the Laptop Decommission and Return Policy to learn more about your laptop.

## Laptop Configuration

After you have finished configuring your laptop, please follow the Pre-Labbing Security Checklist to ensure that you have configured your machine with all of our security best practices.

> These are listed in suggested installation order.

- Mac Getting Started Checklist
- Mac System Preferences and Security Settings
- Linux Getting Started Checklist
- Okta Authentication
- Google Mail (Gmail)
- Jamf Self Service
- Asset Management Acknowledgement
- 1Password
- Touch ID MFA
- YubiKey MFA
- Slack
- Google Chrome
- GitLab.com SaaS
- Zoom
- Visual Studio (VS) Code
- [NordLayer VPN](/handbook/it/guides/nordlayer)
- Google Calendar
- Google Docs
- Google Drive
- iTerm
- Homebrew Package Manager
- Okta Apps
- Pre-Labbing Security Checklist

## Laptop Software Upgrades

- Laptop MacOS Upgrade User Guide
- Laptop Software Upgrade User Guide

## Mobile Devices

- Mobile Device Application Policy
- Other Services and Devices Policy
- iPhone/iPad Apps Setup Guide
- iPhone 2FA/MFA Guide
- Android Apps Setup Guide
- Android 2FA/MFA Guide

## Onboarding

- Onboarding Laptop Hardware Orders
- Onboarding IT Helpdesk Office Hours Zoom Call
- Laptop Configuration Checklist
- GitLab.com User Ultimate License for Team Members
- GitLab.com Group Ultimate License for Demos
- Pre-Labbing Security Checklist

## Offboarding

- Pre-Checkout Offboarding Checklist
- Last Day Checklist
  - Laptop Wipe Runbook
- Post-Offboarding
  - Account Deprovisioning
  - GitLab.com Username Policy
  - GitLab.com Groups Policy
  - Manager Delegation Runbook
  - Offboarding Issue Tasks Runbook
  - Slack Alumni Channel Runbook

## Security Policies

These policies are a cross-collaboration between the IT and Security department.

- [Acceptable Use Policy](https://about.gitlab.com/handbook/people-group/acceptable-use-policy)
- [Data Classification Standards](https://about.gitlab.com/handbook/security/data-classification-standard.html) - RED, ORANGE, YELLOW, GREEN
- [Home WiFi Configuration Policy](https://about.gitlab.com/handbook/security/network-isolation/)
- [Laptop Asset Management Policy](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/endpoint-management/)
- Laptop Disk Encryption Policy
- [Laptop Monitoring Policy](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/endpoint-management/edr/)
- Laptop System Configuration Policy
  - [macOS](https://about.gitlab.com/handbook/security/#laptop-or-desktop-system-configuration)
  - [Linux](/handbook/tools-and-tips/linux/)
- [Mobile Device Application Policy](https://about.gitlab.com/handbook/people-group/acceptable-use-policy/#bring-your-own-device-byod)
- Other Services and Devices Policy
- [Password and MFA Policy](https://about.gitlab.com/handbook/security/password-standard.html)
- [Personal Access Token Policy](https://about.gitlab.com/handbook/security/#personal-access-tokens)
- [Security Awareness Policy](https://about.gitlab.com/handbook/security/#security-awareness)
- [Security Phishing User Guide](https://about.gitlab.com/handbook/security/#how-to-identify-a-basic-phishing-attack)

---

## Tech Stack

The Tech Stack is a list of all the technology that GitLab currently uses to support the business.

Historically, the Tech Stack was a YAML file with a list systems/applications/tools used by all departments and details the business purpose/description, the owners, the provisioners, the teams that access the tool and other details. This is still the SSOT for a directory of applications.

- [Overview](https://about.gitlab.com/handbook/business-technology/tech-stack)
- [SSOT YAML](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml)
- [Managing the Tech Stack](https://about.gitlab.com/handbook/business-technology/tech-stack-applications)
- [Change Management](https://about.gitlab.com/handbook/business-technology/change-management/)
- [IT Engineering Issues](https://gitlab.com/gitlab-com/business-technology/engineering/operations/issue-tracker/-/issues)

As we continue to iterate, we are creating public handbook pages with user guides (below), internal handbook pages with admin guides, and link architecture and security documentation/issues/reviews from the admin guide.

### IT Tech Stack

- [1Password User Guide](https://about.gitlab.com/handbook/security/#accounts-and-passwords) - Password management and security best practices guide
- 1Password Shared Vault Guide - Accessing and managing vaults with shared credentials
- [Apple iCloud User Guide](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding101/#apple-id) - Apple identity and sync services
- [Calendly User Guide](/handbook/tools-and-tips/other-apps/#calendly) - Calendar scheduling assistant
- [Domain Names and DNS Records](/handbook/it/guides/domains-dns) - Domain name purchases, transfers, and DNS records
- [DriveStrike](/handbook/it/guides/drivestrike)
- GitLab SaaS (gitlab.com) User Guide - Getting started with using GitLab.com for work
- GitLab SaaS (gitlab.com) Team Member User Management - User provisioning, password and 2FA resets, and internal user support
- GitLab SaaS (gitlab.com) Team Member Groups - Department, team and project group/project namespace management
- GitLab SaaS (gitlab.com) Team Member Licenses
  - [Ultimate license for users](https://about.gitlab.com/handbook/incentives/#gitlab-ultimate)
  - [Ultimate license for demo groups](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=GitlabCom_Licensed_Demo_Group_Request)
- GitLab Dev (dev.gitlab.org) User Guide - Development builds and OAUTH for legacy services
- GitLab Ops User Guide - Infrastructure-as-code configuration repositories
- [Google Calendar User Guide](/handbook/communication/#google-calendar) - Calendar
- Google Chrome User Guide - Web browser
- Google Data Studio User Guide - Business intelligence reports
- Google Drive User Guide - File storage
- Google Mail (Gmail) User Guide - Email
- Google Groups and Email Lists Guide - Group member permissions and mailing lists
- Google Workspace User Guide - Google Services
- [Jamf User Guide](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/endpoint-management/jamf/) - Asset and endpoint management
- Loom User Guide - Video recording and sharing
- LucidChart User Guide - Diagram software
- [MacOS User Guide - Operating System](/handbook/tools-and-tips/mac/)
- [Nira User Guide](/handbook/it/guides/nira) - Google Drive permissions
- [NordLayer User Guide](/handbook/it/guides/nordlayer) - Public WiFi VPN
- [Okta User Guide](https://about.gitlab.com/handbook/business-technology/okta/) - Identity Management (IAM and SSO)
  - [Okta Verify & Okta Device Trust](https://internal-handbook.gitlab.io/handbook/it/okta-device-trust/) (Internal)
- Okta Groups Guide - Identity Management
- [Okta Apps SSO Integration Guide](https://about.gitlab.com/handbook/business-technology/okta/okta-enduser-faq/#how-do-i-request-an-app-to-be-added)   - Identity Management
- [SentinelOne User Guide](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/endpoint-management/edr/) - Endpoint Detection and Response (EDR) Laptop Monitoring
- [Slack User Guide](https://about.gitlab.com/handbook/communication/#slack) - Chat collaboration
- Slack Channel Guide - Chat collaboration
- Slack Groups Guide - Chat collaboration
- Slack Guest (Contractor, Customer, Vendor) Guide - Chat collaboration
- Slack Integrations (Bots, Webhooks, etc) Guide - Chat collaboration
- Slack Workspace Guide - Chat collaboration
- [Zoom User Guide](/handbook/tools-and-tips/zoom/) - Video collaboration

### Data Team Tech Stack

See the [Data Team](https://about.gitlab.com/handbook/business-technology/data-team/) handbook page to learn more.

- [GitLab Data Dashboard Catalog](https://about.gitlab.com/handbook/business-technology/data-team/data-catalog/)
- [GitLab Data Platform](https://about.gitlab.com/handbook/business-technology/data-team/platform/)
  - Airflow
  - Fivetran
  - SiSense (formerly Periscope)
  - Snowflake
  - [Snowplow](https://about.gitlab.com/handbook/business-technology/data-team/platform/snowplow/)
  - Stitch

### Finance Tech Stack

See the [Finance Ops](https://about.gitlab.com/handbook/business-technology/enterprise-applications/financeops/) handbook page to learn more.

- Adaptive Planning
- Avalara
- CaptivateIQ
- Coupa
- DocuSign
- EdCast
- Expensify
- FloQast
- Mavenlink
- NetSuite
- Platypus (custom built)
- Stripe
- Tipalti
- TripActions
- Workiva
- Xactly
- [Z-Revenue (RevPro)](https://about.gitlab.com/handbook/finance/accounting/finance-ops/Revenue-Accounting/tech-stack-guide-zuora-revenue/)
- [Zuora Billing](https://about.gitlab.com/handbook/finance/accounting/finance-ops/billing-ops/zuora-billing/)

### Infrastructure Shared Services Tech Stack

This is a cross-collaboration between [IT Infrastructure](https://about.gitlab.com/handbook/business-technology/engineering/infrastructure), [Reliability Engineering](https://about.gitlab.com/handbook/engineering/infrastructure/team/reliability/), and [Infrastructure Security](https://about.gitlab.com/handbook/security/security-engineering/infrastructure-security/) with audit and monitoring by [Security Incident Response Team (SIRT)](https://about.gitlab.com/handbook/security/security-operations/sirt/).

- Amazon Web Services (AWS)
- [Domain Names and DNS Records](/handbook/it/guides/domains-dns)
- [GitLab Demo Systems](https://about.gitlab.com/handbook/customer-success/demo-systems/)
- [GitLab Sandbox Cloud (HackyStack) - AWS Accounts & GCP Projects](/handbook/infrastructure-standards/realms/sandbox/)
- Google Cloud Platform (GCP)
- [Infrastructure Standards](/handbook/infrastructure-standards)
- Teleport Console (SSH & Database Access)

### Infrastructure Reliability Tech Stack

See the [Engineering Infrastructure](https://about.gitlab.com/handbook/engineering/infrastructure/) handbook page to learn more.

- [Production Architecture](https://about.gitlab.com/handbook/engineering/infrastructure/production/architecture/)
- [Environments](https://about.gitlab.com/handbook/engineering/infrastructure/environments/) handbook pages
- [Runbooks](https://gitlab.com/gitlab-com/runbooks/) repository to learn more.
- [config-mgmt (Source - Limited Access)](https://ops.gitlab.net/gitlab-com/gl-infra/config-mgmt)
- [config-mgmt (Internal Mirror)](https://gitlab.com/gitlab-com/gl-infra/config-mgmt/)

### People Tech Stack

See the [People Group Engineering](https://about.gitlab.com/handbook/people-group/engineering/) handbook page to learn more.

- [Career Mobility](https://about.gitlab.com/handbook/people-group/engineering/career-mobility)
- [Employment Issues](https://about.gitlab.com/handbook/people-group/engineering/employment-issues)
- Greenhouse - Applicant Tracking System (ATS)
- [Offboarding Automation](https://about.gitlab.com/handbook/people-group/engineering/offboarding)
- [Onboarding Automation](https://about.gitlab.com/handbook/people-group/engineering/onboarding)
- [Slack Bot: People Connect](https://about.gitlab.com/handbook/people-group/engineering/people-connect-bot) - HR Help Desk Tickets
- 👀 [Slack Bot: Discretionary Bonus Nominator](https://about.gitlab.com/handbook/people-group/engineering/nominatorbot) - Discretionary bonus submission form
- [Slack Bot: Time Off by Deel](https://about.gitlab.com/handbook/paid-time-off/#time-off-by-deel) - Out of office management
- [Other Slack Integrations](https://about.gitlab.com/handbook/people-group/engineering/slack-integrations/)
- [Workday User Guide](https://about.gitlab.com/handbook/people-group/workday/workday-guide/) - Human Resources Information System (HRIS)

### Sales Tech Stack

See the [Sales](https://about.gitlab.com/handbook/sales/) and [Field Operations](https://about.gitlab.com/handbook/sales/field-operations/) handbook pages to learn more.

### Security Tech Stack

See the [Security Tools (internal)](https://internal-handbook.gitlab.io/handbook/security/#security-tooling) handbook page to learn more.

---

## Team Directory

#### Business Technology

- [Business Technology Data Team](https://about.gitlab.com/handbook/business-technology/data-team)
- [Business Technology Enterprise Applications Team](https://about.gitlab.com/handbook/business-technology/enterprise-applications)
  - [Business Systems Analysts "BSA" Team](https://about.gitlab.com/handbook/business-technology/enterprise-applications/bsa/)
  - [Finance Operations](https://about.gitlab.com/handbook/business-technology/enterprise-applications/financeops/)
- [Business Technology Procurement Team](https://about.gitlab.com/handbook/business-technology/data-team)
- [Business Technology Program Management (PMO) Team]

#### IT Department

- [IT Compliance and Security](https://about.gitlab.com/handbook/business-technology/it-compliance)
- [IT Engineering](https://about.gitlab.com/handbook/business-technology/engineering)
- IT Helpdesk Analysts
- [IT Infrastructure](https://about.gitlab.com/handbook/business-technology/engineering/infrastructure)

#### Infrastructure Shared Services

- [Infrastructure Security Team](https://about.gitlab.com/handbook/security/security-engineering/infrastructure-security/)
- [IT Infrastructure](https://about.gitlab.com/handbook/business-technology/engineering/infrastructure)
- [Reliability Engineering Team](https://about.gitlab.com/handbook/engineering/infrastructure/team/reliability/)

#### People Team

- [People Connect Helpdesk](https://about.gitlab.com/handbook/people-group/people-connect)
- [People Group](https://about.gitlab.com/handbook/people-group)
- [People Tools and Technology](/handbook/)
- [People Group Engineering Issue Tracker](https://gitlab.com/gitlab-com/people-group/peopleops-eng/people-group-engineering/-/issues)

#### Security Department

- 👀 [Departmental Structure](https://about.gitlab.com/handbook/security/#departmental-structure)
  - [Security Assurance Sub-department](https://about.gitlab.com/handbook/security/security-assurance/)
    - [Field Security](https://about.gitlab.com/handbook/security/security-assurance/field-security/)
    - [Security Compliance](https://about.gitlab.com/handbook/security/security-assurance/security-compliance/)
    - [Security Governance](https://about.gitlab.com/handbook/security/security-assurance/governance/)
    - [Security Risk](https://about.gitlab.com/handbook/security/security-assurance/security-risk/)
  - [Security Engineering Sub-department](https://about.gitlab.com/handbook/security/security-engineering/)
    - [Application Security](https://about.gitlab.com/handbook/security/security-engineering/application-security/)
    - [Security Automation](https://about.gitlab.com/handbook/security/security-engineering/automation/)
  - [Security Operations Sub-department](https://about.gitlab.com/handbook/security/security-operations)
    - [Security Incident Response Team "SIRT"](https://about.gitlab.com/handbook/security/security-operations/sirt)
    - [Trust and Safety](https://about.gitlab.com/handbook/security/security-operations/trustandsafety/)
    - [Infrastructure Security](https://about.gitlab.com/handbook/security/security-engineering/infrastructure-security/)
    - [Security Logging](https://about.gitlab.com/handbook/security/security-engineering/security-logging)
  - [Security Threat Management Sub-department](https://about.gitlab.com/handbook/security/threat-management)
    - [Red Team](https://about.gitlab.com/handbook/security/threat-management/red-team)
    - [Security Research](https://about.gitlab.com/handbook/security/threat-management/security-research/)

## How To Contribute

Did we miss something? Did you find the answer on another handbook page? Please feel free to [submit an MR](/handbook/handbook-usage) or let one of the code owners for this page know.
