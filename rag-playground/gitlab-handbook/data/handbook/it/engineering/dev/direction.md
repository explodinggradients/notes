---
title: "IT Engineering Development Direction"
description: "This handbook page provides information about the IT Engineering sub-department."
---

## Overview

Our long term focus is on reducing or replacing IT 1.0 tech debt with a greenfield approach for IT 2.0 using our Automation Philosophy as guiding principles and focusing on Level 4 automations and engineering simpler solutions to reduce Level 5 automations to Level 4 complexity.

Our team is good at foreshadowing and working on projects proactively that will offer benefits to the organization in 3-12 months to solve root cause problems instead of continuing to engineer workarounds for systemtic symptoms.

The overarching philosophy has shifted to focus on backend integrations development that doesn't require a frontend UI in the traditional MVC sense. We have found that eliminating a web UI saves us a lot of headache and allows us to focus more on that last 20% of business logic that we need to solve for.

Most of our next-gen automation is focused on API calls, CLI scripts, GitLab CI/CD jobs, and Slackbot interactions.

## Leadership Highlights

> Most projects relate to a thematic "IT 2.0" greenfield direction that removes a lot of technical debt.

1. **Architecting** next-generation automation and integration between IT managed systems that provides data consistency, reliability, strong security, and audibility.
1. **Building** Archie to programmatically provision and deprovision users in GitLab, Google, Okta, and Slack groups that are provisioned and deprovisioned manually today as part of baseline entitlements, career mobility, and offboarding issue templates. This has significant time savings for dozens of team members, and mitigates many problems that we face with audit and compliance observations. Many other services we work with depend on a reliable directory source and this has the potential of being a valuable SSOT.
1. **Consolidating** and refactoring [Demo Systems](https://about.gitlab.com/handbook/customer-success/demo-systems) web applications and legacy tech debt.
1. **Developing** HackyStack v2 with improved cost management features, offboarding automation, Slack integration, and evaluating the future direction of Terraform environments that can be embedded in the GitLab product.
1. **Escalation engineering** and emergency response for IT Operations and Security teams, and providing assistance to team members with all of the systems that we build and manage.
1. **Factor** in cost, security, compatibility, maintainability and user experience when making decisions.
1. **Growing other team members’ skill sets** through mentorship to improve operational efficiency and encourage professional development.
1. **Helping** team members with all systems that we build and manage.
1. **Iterating** continuously as part of our company values.

## Quick Links

- [List of Epics](https://gitlab.com/groups/gitlab-com/it/dev/-/epics)
- [Epics Gantt Chart (Development Only)](https://gitlab.com/groups/gitlab-com/it/dev/-/roadmap?state=all&sort=end_date_asc&layout=MONTHS&timeframe_range_type=CURRENT_YEAR&progress=WEIGHT&show_progress=true&show_milestones=false&milestones_type=ALL)
- [Epics Gantt Chart (IT)](https://gitlab.com/groups/gitlab-com/it/-/roadmap?state=all&sort=end_date_asc&layout=MONTHS&timeframe_range_type=CURRENT_YEAR&progress=WEIGHT&show_progress=true&show_milestones=false&milestones_type=ALL)

### Initiatives at a Glance

- [dev&23 IT Automation v2 (GLabIT)](https://gitlab.com/groups/gitlab-com/it/dev/-/epics/23)
- [dev&26 IAM and RBAC v3](https://gitlab.com/groups/gitlab-com/it/dev/-/epics/26)
- [dev&25 HackyStack and Sandbox Cloud](https://gitlab.com/groups/gitlab-com/it/dev/-/epics/25)
- [dev&22 Open Source Packages and SDKs](https://gitlab.com/groups/gitlab-com/it/dev/-/epics/22)

### Roadmap Timelines

Since IT Systems Engineers split their time between Engineering and Operations (development happens as time allows), we are not able to provide accurate timeline forecasting (including quarterly OKRs) and instead provide stack ranked priority. All roadmap start and end dates are estimates and are not commitments.

One engineer is the DRI for each epic and are managers of one for efficiency. This allows each of us to focus on our strengths and be DRIs for the projects that we're passionate about and go deep into the programming headspace as needed without coordination. We still collaborate when we run into tough engineering challenges and we still perform peer MR reviews on all code.

We work on 1-3 projects at a time and the project priority increases as the business need increases at the discretion of the IT Engineering team. Any epics with a P1 are top of mind and are being worked on in the current quarter or are in the up next queue. Any epics with P4 are considered wishlist. Please keep in mind that projects are often interrupted with distractions from day-to-day Slack and issue requests.

## Architecture Diagrams

### Color Key

```mermaid
graph TD
KEY_ADDED["FY24 Added"]:::cyan
KEY_MAINTAINED["FY24 Maintained"]:::emerald
KEY_REFACTOR["FY24 Consolidate/Refactor"]:::yellow
KEY_DEPRECATE["FY24 Deprecate"]:::red

classDef slate fill:#cbd5e1,stroke:#475569,stroke-width:1px;
classDef red fill:#fca5a5,stroke:#dc2626,stroke-width:1px;
classDef orange fill:#fdba74,stroke:#ea580c,stroke-width:1px;
classDef yellow fill:#fcd34d,stroke:#ca8a04,stroke-width:1px;
classDef emerald fill:#6ee7b7,stroke:#059669,stroke-width:1px;
classDef cyan fill:#67e8f9,stroke:#0891b2,stroke-width:1px;
classDef sky fill:#7dd3fc,stroke:#0284c7,stroke-width:1px;
classDef violet fill:#c4b5fd,stroke:#7c3aed,stroke-width:1px;
classDef fuchsia fill:#f0abfc,stroke:#c026d3,stroke-width:1px;
```

### Demo and Training Systems

#### gitlabdemo.com

```mermaid
graph TD
subgraph "Laravel App Logic"
    subgraph "Student UI"
        GITLABDEMO_COM_STUDENT_INVITATION_CODES("Redeem Invitation Code"):::yellow
        GITLABDEMO_COM_STUDENT_CREATE_USER("Create GitLab User Account"):::yellow
        GITLABDEMO_COM_STUDENT_CREATE_GROUP("Create GitLab Group"):::yellow
    end
    subgraph "Admin UI"
        GITLABDEMO_COM_ADMIN_INVITATION_CODES("Create and Manage<br />Invitation Codes"):::yellow
        GITLABDEMO_COM_ADMIN_CREATE_GROUP("Create GitLab Group for Session"):::yellow
    end
    GITLABDEMO_COM_ADMIN_INVITATION_CODES --> GITLABDEMO_COM_STUDENT_INVITATION_CODES
    GITLABDEMO_COM_STUDENT_INVITATION_CODES --> GITLABDEMO_COM_STUDENT_CREATE_USER
    GITLABDEMO_COM_STUDENT_INVITATION_CODES --> GITLABDEMO_COM_STUDENT_CREATE_GROUP
    GITLABDEMO_COM_ADMIN_CREATE_GROUP -.- GITLABDEMO_COM_STUDENT_CREATE_GROUP
end
subgraph "GCP Project demosys-mgmt"
    direction LR;
    DEMO_COM_APP["Linux Nginx Server"]:::red
    DEMO_COM_LARAVEL["Laravel Application (link)"]:::red
    DEMO_COM_SQL["MySQL Database"]:::red
    DEMO_COM_APP -.- DEMO_COM_SQL
    DEMO_COM_LARAVEL --- DEMO_COM_APP
    DEMO_COM_LARAVEL --- DEMO_COM_SQL
    click CS_OMNIBUS "https://cs.gitlabdemo.cloud" "Access System" _blank
    click DEMO_COM_LARAVEL "https://gitlab.com/gitlab-com/it/dev/gitlabdemo-com-app" "Open Repository" _blank
end
subgraph "ops.gitlab.net/it-infra-realm"
    direction LR;
    DEMO_COM_TERRAFORM["demosys-terraform Repo (link)<br />Admin Local Terminal Only"]:::red
    DEMO_COM_ANSIBLE["gitlabdemo-com-ansible (link)<br />Admin Local Terminal Only"]:::red
    click DEMO_COM_TERRAFORM "https://gitlab.com/gitlab-com/it/infra/demosys-terraform" "Open Repository" _blank
    click DEMO_COM_ANSIBLE "https://ops.gitlab.net/it-infra-realm/environments/gcp/gcp-project-demosys-mgmt/gitlabdemo-com-ansible" "Open Repository" _blank
end

classDef slate fill:#cbd5e1,stroke:#475569,stroke-width:1px;
classDef red fill:#fca5a5,stroke:#dc2626,stroke-width:1px;
classDef orange fill:#fdba74,stroke:#ea580c,stroke-width:1px;
classDef yellow fill:#fcd34d,stroke:#ca8a04,stroke-width:1px;
classDef emerald fill:#6ee7b7,stroke:#059669,stroke-width:1px;
classDef cyan fill:#67e8f9,stroke:#0891b2,stroke-width:1px;
classDef sky fill:#7dd3fc,stroke:#0284c7,stroke-width:1px;
classDef violet fill:#c4b5fd,stroke:#7c3aed,stroke-width:1px;
classDef fuchsia fill:#f0abfc,stroke:#c026d3,stroke-width:1px;
```

#### gitlabdemo.cloud

```mermaid
graph TD
subgraph "Laravel App Logic"
    subgraph "Team Member UI"
        GITLABDEMO_CLOUD_CREATE_USER("Create GitLab User Account"):::yellow
        GITLABDEMO_CLOUD_CREATE_GROUP("Create GitLab Group"):::yellow
    end
    GITLABDEMO_CLOUD_CREATE_USER --> GITLABDEMO_CLOUD_CREATE_GROUP
end
subgraph "GCP Project demosys-app-demo-cloud"
    direction LR;
    DEMO_CLOUD_APP["Linux Nginx Server"]:::red
    DEMO_CLOUD_LARAVEL["Laravel Application (link)"]:::red
    DEMO_CLOUD_SQL["MySQL Database"]:::red
    DEMO_CLOUD_APP -.- DEMO_CLOUD_SQL
    DEMO_CLOUD_LARAVEL --- DEMO_CLOUD_APP
    DEMO_CLOUD_LARAVEL --- DEMO_CLOUD_SQL
    click DEMO_CLOUD_LARAVEL "https://gitlab.com/gitlab-com/it/dev/gitlabdemo-cloud-app" "Open Repository" _blank
end
subgraph "ops.gitlab.net/it-infra-realm"
    direction LR;
    DEMO_CLOUD_IAC["app-gitlabdemo-cloud-iac Repo (link)<br />Terraform CI/CD Pipeline"]:::red
    click DEMO_CLOUD_IAC "https://ops.gitlab.net/it-infra-realm/environments/gcp/gcp-project-app-gitlabdemo-cloud/app-gitlabdemo-cloud-iac" "Open Repository" _blank
end
classDef slate fill:#cbd5e1,stroke:#475569,stroke-width:1px;
classDef red fill:#fca5a5,stroke:#dc2626,stroke-width:1px;
classDef orange fill:#fdba74,stroke:#ea580c,stroke-width:1px;
classDef yellow fill:#fcd34d,stroke:#ca8a04,stroke-width:1px;
classDef emerald fill:#6ee7b7,stroke:#059669,stroke-width:1px;
classDef cyan fill:#67e8f9,stroke:#0891b2,stroke-width:1px;
classDef sky fill:#7dd3fc,stroke:#0284c7,stroke-width:1px;
classDef violet fill:#c4b5fd,stroke:#7c3aed,stroke-width:1px;
classDef fuchsia fill:#f0abfc,stroke:#c026d3,stroke-width:1px;
```

#### gitlabsandbox.cloud

```mermaid
graph TD
subgraph "Laravel App Logic"
    direction LR;
    subgraph "AWS Accounts"
        SANDBOX_AWS_CREATE_ACCOUNT("Create AWS Account"):::yellow
        SANDBOX_AWS_CREATE_USER("Create AWS IAM User"):::yellow
        SANDBOX_AWS_ATTACH_ROLE("Attach Role to User"):::yellow
        SANDBOX_AWS_CREATE_ACCOUNT --> SANDBOX_AWS_CREATE_USER
        SANDBOX_AWS_CREATE_USER --> SANDBOX_AWS_ATTACH_ROLE
    end
    subgraph "GCP Projects"
        SANDBOX_GCP_CREATE_PROJECT("Create GCP Project"):::yellow
        SANDBOX_GCP_ATTACH_USER("Attach User to Project"):::yellow
        SANDBOX_GCP_ATTACH_ROLE("Attach Role to User"):::yellow
        SANDBOX_GCP_CREATE_PROJECT --> SANDBOX_GCP_ATTACH_USER
        SANDBOX_GCP_ATTACH_USER --> SANDBOX_GCP_ATTACH_ROLE
    end
    subgraph "Terraform Environments"
        SANDBOX_TF_CREATE_GROUP("Create GitLab Group (GCP Project)"):::yellow
        SANDBOX_TF_CREATE_PROJECT("Create GitLab Project<br />(Environment Template)"):::yellow
        SANDBOX_TF_IMPORT_PROJECT("Import Repository<br />(Terraform Example Repo)"):::yellow
        SANDBOX_TF_CREATE_GCP_SERVICE_ACCOUNT("Create GCP Service Account"):::yellow
        SANDBOX_TF_CI_VAR_GCP_SERVICE_ACCOUNT("Create CI/CD Variable<br />for Service Account"):::yellow
        SANDBOX_TF_CREATE_DNS_ZONE("Create GCP DNS Subdomain Zone"):::yellow
        SANDBOX_TF_SET_CI_VARS_FOR_PROJECT("Set CI/CD Variables for GCP Project"):::yellow
        SANDBOX_TF_CREATE_GROUP --> SANDBOX_TF_CREATE_PROJECT
        SANDBOX_TF_CREATE_PROJECT --> SANDBOX_TF_IMPORT_PROJECT
        SANDBOX_TF_IMPORT_PROJECT --> SANDBOX_TF_CREATE_GCP_SERVICE_ACCOUNT
        SANDBOX_TF_CREATE_GCP_SERVICE_ACCOUNT --> SANDBOX_TF_CI_VAR_GCP_SERVICE_ACCOUNT
        SANDBOX_TF_CI_VAR_GCP_SERVICE_ACCOUNT --> SANDBOX_TF_CREATE_DNS_ZONE
        SANDBOX_TF_CREATE_DNS_ZONE --> SANDBOX_TF_SET_CI_VARS_FOR_PROJECT
    end
end
subgraph "GCP Project hackystack-mgmt"
    direction LR;
    SANDBOX_CLOUD_APP["Linux Nginx Server"]:::red
    SANDBOX_CLOUD_SQL["Cloud SQL MySQL Database"]:::red
    SANDBOX_CLOUD_LARAVEL["Laravel Application (link)"]:::red
    SANDBOX_CLOUD_APP -.- SANDBOX_CLOUD_SQL
    SANDBOX_CLOUD_LARAVEL --- SANDBOX_CLOUD_APP
    SANDBOX_CLOUD_LARAVEL --- SANDBOX_CLOUD_SQL
    click DEMO_CLOUD_LARAVEL "https://gitlab.com/gitlab-com/it/dev/hackystack-laravel" "Open Repository" _blank
end
subgraph "ops.gitlab.net/it-infra-realm"
    direction LR;
    SANDBOX_CLOUD_IAC["app-gitlabdemo-cloud-iac Repo (link)<br />Terraform CI/CD Pipeline"]:::red
    click SANDBOX_CLOUD_IAC "https://ops.gitlab.net/it-infra-realm/environments/gcp/gcp-project-hackystack-mgmt/gitlabsandbox-cloud-app-iac" "Open Repository" _blank
end
classDef slate fill:#cbd5e1,stroke:#475569,stroke-width:1px;
classDef red fill:#fca5a5,stroke:#dc2626,stroke-width:1px;
classDef orange fill:#fdba74,stroke:#ea580c,stroke-width:1px;
classDef yellow fill:#fcd34d,stroke:#ca8a04,stroke-width:1px;
classDef emerald fill:#6ee7b7,stroke:#059669,stroke-width:1px;
classDef cyan fill:#67e8f9,stroke:#0891b2,stroke-width:1px;
classDef sky fill:#7dd3fc,stroke:#0284c7,stroke-width:1px;
classDef violet fill:#c4b5fd,stroke:#7c3aed,stroke-width:1px;
classDef fuchsia fill:#f0abfc,stroke:#c026d3,stroke-width:1px;
```

### IT Automation v1

#### IT Ops CLI Scripts

```mermaid
graph LR
subgraph "Laravel App Logic"
    CLI_SCRIPTS_GITLAB_ISSUE("gitlab-issue:* CRUD Commands (link)"):::yellow
    CLI_SCRIPTS_GITLAB_CONTRIBUTIONS("gitlab-event:* Contribution/Standup Reports (link)"):::yellow
    CLI_SCRIPTS_GITLAB_KANBAN("gitlab-issue:* Kanban Reports (link)"):::yellow
    CLI_SCRIPTS_GITLAB_GROUP_CRUD("gitlab-group:* CRUD Commands (link)"):::yellow
    CLI_SCRIPTS_GITLAB_USER_CRUD("gitlab-user:* CRUD Commands (link)"):::yellow
    CLI_SCRIPTS_GOOGLE_CRUD("google-workspace:* CRUD Commands (link)"):::yellow
    CLI_SCRIPTS_OKTA_CRUD("okta:* CRUD Commands (link)"):::yellow
    CLI_SCRIPTS_SLACK_REPORTS("slack:* Reports (link)"):::yellow
    CLI_SCRIPTS_SNIPEIT("snipe-it:* CRUD Commands (link)"):::yellow
    click CLI_SCRIPTS_GITLAB_ISSUE "https://gitlab.com/gitlab-com/it/dev/it-ops-laravel-cli-scripts#gitlab-issue-tracker" "Open Repository" _blank
    click CLI_SCRIPTS_GITLAB_CONTRIBUTION "https://gitlab.com/gitlab-com/it/dev/it-ops-laravel-cli-scripts#gitlab-events-and-standup-reports" "Open Repository" _blank
    click CLI_SCRIPTS_GITLAB_KANBAN "https://gitlab.com/gitlab-com/it/dev/it-ops-laravel-cli-scripts#gitlab-issue-tracker-kanban-board" "Open Repository" _blank
    click CLI_SCRIPTS_GITLAB_GROUP_CRUD "https://gitlab.com/gitlab-com/it/dev/it-ops-laravel-cli-scripts#gitlab-group-and-user-provisioning" "Open Repository" _blank
    click CLI_SCRIPTS_GITLAB_USER_CRUD "https://gitlab.com/gitlab-com/it/dev/it-ops-laravel-cli-scripts#gitlab-group-and-user-provisioning" "Open Repository" _blank
    click CLI_SCRIPTS_GOOGLE_CRUD "https://gitlab.com/gitlab-com/it/dev/it-ops-laravel-cli-scripts#google-workspace" "Open Repository" _blank
    click CLI_SCRIPTS_OKTA_CRUD "https://gitlab.com/gitlab-com/it/dev/it-ops-laravel-cli-scripts#okta-application-group-and-user-provisioning" "Open Repository" _blank
    click CLI_SCRIPTS_SLACK_REPORTS "https://gitlab.com/gitlab-com/it/dev/it-ops-laravel-cli-scripts#slack" "Open Repository" _blank
    click CLI_SCRIPTS_SNIPEIT "https://gitlab.com/gitlab-com/it/dev/it-ops-laravel-cli-scripts#snipe-it" "Open Repository" _blank
end
subgraph "Local Laptop"
    direction LR;
    CLI_SCRIPTS_LARAVEL["Laravel CLI Application (link)"]:::yellow
    click CLI_SCRIPTS_LARAVEL "https://gitlab.com/gitlab-com/it/dev/it-ops-laravel-cli-scripts" "Open Repository" _blank
end
classDef slate fill:#cbd5e1,stroke:#475569,stroke-width:1px;
classDef red fill:#fca5a5,stroke:#dc2626,stroke-width:1px;
classDef orange fill:#fdba74,stroke:#ea580c,stroke-width:1px;
classDef yellow fill:#fcd34d,stroke:#ca8a04,stroke-width:1px;
classDef emerald fill:#6ee7b7,stroke:#059669,stroke-width:1px;
classDef cyan fill:#67e8f9,stroke:#0891b2,stroke-width:1px;
classDef sky fill:#7dd3fc,stroke:#0284c7,stroke-width:1px;
classDef violet fill:#c4b5fd,stroke:#7c3aed,stroke-width:1px;
classDef fuchsia fill:#f0abfc,stroke:#c026d3,stroke-width:1px;
```

#### Asset Scripts

```mermaid
graph LR
subgraph "Asset Scripts Laravel App Logic"
    ASSET_SCRIPTS_JAMF("jamf:* Reports"):::yellow
    ASSET_SCRIPTS_OKTA("okta:* Reports"):::yellow
end
subgraph "Local Laptop"
    ASSET_SCRIPTS_LARAVEL["Laravel CLI Application"]:::yellow
end
classDef slate fill:#cbd5e1,stroke:#475569,stroke-width:1px;
classDef red fill:#fca5a5,stroke:#dc2626,stroke-width:1px;
classDef orange fill:#fdba74,stroke:#ea580c,stroke-width:1px;
classDef yellow fill:#fcd34d,stroke:#ca8a04,stroke-width:1px;
classDef emerald fill:#6ee7b7,stroke:#059669,stroke-width:1px;
classDef cyan fill:#67e8f9,stroke:#0891b2,stroke-width:1px;
classDef sky fill:#7dd3fc,stroke:#0284c7,stroke-width:1px;
classDef violet fill:#c4b5fd,stroke:#7c3aed,stroke-width:1px;
classDef fuchsia fill:#f0abfc,stroke:#c026d3,stroke-width:1px;
```

#### Archie Scripts

```mermaid
graph LR
subgraph "Laravel App Logic"
    ARCHIE_SCRIPTS_DIRECTORY("directory:* Commands"):::yellow
    ARCHIE_SCRIPTS_POLICY("policy:* Commands"):::yellow
    ARCHIE_SCRIPTS_PROVISIONER("provisioner:* Commands"):::yellow
end
subgraph "Local Laptop"
    ARCHIE_SCRIPTS_LARAVEL["Laravel CLI Application"]:::yellow
    click ARCHIE_SCRIPTS_LARAVEL "https://gitlab.com/gitlab-com/it/dev/archie-laravel-scripts" "Open Repository" _blank
end

classDef slate fill:#cbd5e1,stroke:#475569,stroke-width:1px;
classDef red fill:#fca5a5,stroke:#dc2626,stroke-width:1px;
classDef orange fill:#fdba74,stroke:#ea580c,stroke-width:1px;
classDef yellow fill:#fcd34d,stroke:#ca8a04,stroke-width:1px;
classDef emerald fill:#6ee7b7,stroke:#059669,stroke-width:1px;
classDef cyan fill:#67e8f9,stroke:#0891b2,stroke-width:1px;
classDef sky fill:#7dd3fc,stroke:#0284c7,stroke-width:1px;
classDef violet fill:#c4b5fd,stroke:#7c3aed,stroke-width:1px;
classDef fuchsia fill:#f0abfc,stroke:#c026d3,stroke-width:1px;
```

### GitLab SaaS

#### Learn Labs

```mermaid
graph LR
subgraph "gitlab.com/gitlab-learn-labs"
    LEARN_LABS_ENVIRONMENTS_GROUP["Environments Group"]:::emerald
    LEARN_LABS_SESSION_GROUP["Session Group"]:::emerald
    LEARN_LABS_STUDENT_GROUP("Student Group"):::emerald
    LEARN_LABS_RUNNER_MANAGER["Runner Manager"]:::emerald
    LEARN_LABS_CI_CLUSTER["CI Kubernetes Shared Cluster"]:::emerald
    LEARN_LABS_ENVIRONMENTS_GROUP -.- LEARN_LABS_RUNNER_MANAGER
    LEARN_LABS_ENVIRONMENTS_GROUP -.- LEARN_LABS_CI_CLUSTER
    LEARN_LABS_ENVIRONMENTS_GROUP --> LEARN_LABS_SESSION_GROUP
    LEARN_LABS_SESSION_GROUP --> LEARN_LABS_STUDENT_GROUP
end
subgraph "Instruqt"
    LEARN_LABS_INSTRUQT_CLUSTER["Ephemeral Kubernetes Cluster<br />(per student)"]:::emerald
    LEARN_LABS_INSTRUQT_AWS["Ephemeral AWS Account<br />(per student)"]:::emerald
    LEARN_LABS_INSTRUQT_GCP["Ephemeral GCP Project<br />(per student)"]:::emerald
end
subgraph "ops.gitlab.net/it-infra-realm/.../learn-labs"
    LEARN_LABS_IAC["learn-labs-iac Repo (link)<br />Terraform CI/CD Pipeline"]:::emerald
end
LEARN_LABS_STUDENT_GROUP -- Adv Classes with GitLab Agent --> LEARN_LABS_INSTRUQT_CLUSTER
LEARN_LABS_STUDENT_GROUP -- Adv Classes with AWS --> LEARN_LABS_INSTRUQT_AWS
LEARN_LABS_STUDENT_GROUP -- Adv Classes with GCP --> LEARN_LABS_INSTRUQT_GCP

classDef slate fill:#cbd5e1,stroke:#475569,stroke-width:1px;
classDef red fill:#fca5a5,stroke:#dc2626,stroke-width:1px;
classDef orange fill:#fdba74,stroke:#ea580c,stroke-width:1px;
classDef yellow fill:#fcd34d,stroke:#ca8a04,stroke-width:1px;
classDef emerald fill:#6ee7b7,stroke:#059669,stroke-width:1px;
classDef cyan fill:#67e8f9,stroke:#0891b2,stroke-width:1px;
classDef sky fill:#7dd3fc,stroke:#0284c7,stroke-width:1px;
classDef violet fill:#c4b5fd,stroke:#7c3aed,stroke-width:1px;
classDef fuchsia fill:#f0abfc,stroke:#c026d3,stroke-width:1px;
```

### GitLab Self Managed Instances

#### cs.gitlabdemo.cloud

```mermaid
graph LR
subgraph "GCP Project demosys-cs-demo-cloud"
    CS_OMNIBUS["Omnibus Instance (link)"]:::emerald
    CS_USERS("Username GitLab Group"):::emerald
    CS_RUNNER_MANAGER["Runner Manager"]:::emerald
    CS_CI_CLUSTER["CI Kubernetes Cluster"]:::emerald
    CS_OMNIBUS -.- CS_RUNNER_MANAGER
    CS_OMNIBUS -.- CS_CI_CLUSTER
    CS_OMNIBUS --> CS_USERS
    CS_HANDBOOK["Handbook Instructions (link)"]:::violet
    click CS_OMNIBUS "https://cs.gitlabdemo.cloud" "Access System" _blank
    click CS_HANDBOOK "https://about.gitlab.com/handbook/customer-success/demo-systems/#access-shared-omnibus-instances" "Usage Instructions" _blank
end
subgraph "ops.gitlab.net/it-infra-realm/.../cs"
    CS_IAC["cs-gitlabdemo-cloud-iac Repo (link)<br />Terraform CI/CD Pipeline"]:::emerald
    click CS_IAC "https://ops.gitlab.net/it-infra-realm/environments/gcp/gcp-project-demosys-cs-demo-cloud/cs-gitlabdemo-cloud-iac" "Open Repository" _blank
end
classDef slate fill:#cbd5e1,stroke:#475569,stroke-width:1px;
classDef red fill:#fca5a5,stroke:#dc2626,stroke-width:1px;
classDef orange fill:#fdba74,stroke:#ea580c,stroke-width:1px;
classDef yellow fill:#fcd34d,stroke:#ca8a04,stroke-width:1px;
classDef emerald fill:#6ee7b7,stroke:#059669,stroke-width:1px;
classDef cyan fill:#67e8f9,stroke:#0891b2,stroke-width:1px;
classDef sky fill:#7dd3fc,stroke:#0284c7,stroke-width:1px;
classDef violet fill:#c4b5fd,stroke:#7c3aed,stroke-width:1px;
classDef fuchsia fill:#f0abfc,stroke:#c026d3,stroke-width:1px;
```

#### ilt.gitlabtraining.cloud

```mermaid
graph LR
subgraph "GCP Project demosys-ilt-training-cloud"
    ILT_OMNIBUS["Omnibus Instance (link)"]:::red
    ILT_ENVIRONMENTS("Sessions GitLab Group"):::yellow
    ILT_RUNNER_MANAGER["Runner Manager"]:::red
    ILT_CI_CLUSTER["CI Kubernetes Cluster"]:::red
    ILT_OMNIBUS -.- ILT_RUNNER_MANAGER
    ILT_OMNIBUS -.- ILT_CI_CLUSTER
    ILT_OMNIBUS --> ILT_ENVIRONMENTS
    ILT_HANDBOOK["Handbook Instructions (link)"]:::violet
    click ILT_OMNIBUS "https://ilt.gitlabtraining.cloud" "Access System" _blank
    click ILT_HANDBOOK "https://about.gitlab.com/handbook/customer-success/demo-systems/#access-shared-omnibus-instances" "Usage Instructions" _blank
end
subgraph "ops.gitlab.net/it-infra-realm/.../ilt"
    ILT_IAC["ilt-gitlabtraining-cloud-iac Repo (link)<br />Terraform CI/CD Pipeline"]:::red
    click ILT_IAC "https://ops.gitlab.net/it-infra-realm/environments/gcp/gcp-project-demosys-ilt-training-cloud/ilt-gitlabtraining-cloud-iac" "Open Repository" _blank
end
classDef slate fill:#cbd5e1,stroke:#475569,stroke-width:1px;
classDef red fill:#fca5a5,stroke:#dc2626,stroke-width:1px;
classDef orange fill:#fdba74,stroke:#ea580c,stroke-width:1px;
classDef yellow fill:#fcd34d,stroke:#ca8a04,stroke-width:1px;
classDef emerald fill:#6ee7b7,stroke:#059669,stroke-width:1px;
classDef cyan fill:#67e8f9,stroke:#0891b2,stroke-width:1px;
classDef sky fill:#7dd3fc,stroke:#0284c7,stroke-width:1px;
classDef violet fill:#c4b5fd,stroke:#7c3aed,stroke-width:1px;
classDef fuchsia fill:#f0abfc,stroke:#c026d3,stroke-width:1px;
```

#### workshop.gitlabtraining.cloud

```mermaid
graph LR
subgraph "GCP Project demosys-workshop-cloud"
    WORKSHOP_OMNIBUS["Omnibus Instance (link)"]:::red
    WORKSHOP_ENVIRONMENTS("Sessions GitLab Group"):::yellow
    WORKSHOP_RUNNER_MANAGER["Runner Manager"]:::red
    WORKSHOP_CI_CLUSTER["CI Kubernetes Cluster"]:::red
    WORKSHOP_OMNIBUS -.- WORKSHOP_RUNNER_MANAGER
    WORKSHOP_OMNIBUS -.- WORKSHOP_CI_CLUSTER
    WORKSHOP_OMNIBUS --> WORKSHOP_ENVIRONMENTS
    WORKSHOP_HANDBOOK["Handbook Instructions (link)"]:::violet
    click WORKSHOP_OMNIBUS "https://ilt.gitlabtraining.cloud" "Access System" _blank
    click WORKSHOP_HANDBOOK "https://about.gitlab.com/handbook/customer-success/demo-systems/#access-shared-omnibus-instances" "Usage Instructions" _blank
end
subgraph "ops.gitlab.net/it-infra-realm/.../workshop"
    WORKSHOP_IAC["workshop-gitlabtraining-cloud-iac Repo (link)<br />Terraform CI/CD Pipeline"]:::red
    click WORKSHOP_IAC "https://ops.gitlab.net/it-infra-realm/environments/gcp/gcp-project-demosys-workshop-cloud/workshop-gitlabtraining-cloud-iac" "Open Repository" _blank
end
classDef slate fill:#cbd5e1,stroke:#475569,stroke-width:1px;
classDef red fill:#fca5a5,stroke:#dc2626,stroke-width:1px;
classDef orange fill:#fdba74,stroke:#ea580c,stroke-width:1px;
classDef yellow fill:#fcd34d,stroke:#ca8a04,stroke-width:1px;
classDef emerald fill:#6ee7b7,stroke:#059669,stroke-width:1px;
classDef cyan fill:#67e8f9,stroke:#0891b2,stroke-width:1px;
classDef sky fill:#7dd3fc,stroke:#0284c7,stroke-width:1px;
classDef violet fill:#c4b5fd,stroke:#7c3aed,stroke-width:1px;
classDef fuchsia fill:#f0abfc,stroke:#c026d3,stroke-width:1px;
```

#### spt.gitlabdemo.cloud

```mermaid
graph LR
subgraph "GCP Project demosys-spt-training-cloud"
    SPT_OMNIBUS["Omnibus Instance (link)"]:::red
    SPT_ENVIRONMENTS("Sessions GitLab Group"):::yellow
    SPT_RUNNER_MANAGER["Runner Manager"]:::red
    SPT_CI_CLUSTER["CI Kubernetes Cluster"]:::red
    SPT_OMNIBUS -.- SPT_RUNNER_MANAGER
    SPT_OMNIBUS -.- SPT_CI_CLUSTER
    SPT_OMNIBUS --> SPT_ENVIRONMENTS
    SPT_HANDBOOK["Handbook Instructions (link)"]:::violet
    click SPT_OMNIBUS "https://spt.gitlabtraining.cloud" "Access System" _blank
    click SPT_HANDBOOK "https://about.gitlab.com/handbook/customer-success/demo-systems/#access-shared-omnibus-instances" "Usage Instructions" _blank
end
subgraph "ops.gitlab.net/it-infra-realm/.../spt"
    SPT_IAC["spt-gitlabtraining-cloud-iac Repo (link)<br />Terraform CI/CD Pipeline"]:::red
    click SPT_IAC "https://ops.gitlab.net/it-infra-realm/environments/gcp/gcp-project-demosys-spt-training-cloud/spt-gitlabtraining-cloud-iac" "Open Repository" _blank
end
classDef slate fill:#cbd5e1,stroke:#475569,stroke-width:1px;
classDef red fill:#fca5a5,stroke:#dc2626,stroke-width:1px;
classDef orange fill:#fdba74,stroke:#ea580c,stroke-width:1px;
classDef yellow fill:#fcd34d,stroke:#ca8a04,stroke-width:1px;
classDef emerald fill:#6ee7b7,stroke:#059669,stroke-width:1px;
classDef cyan fill:#67e8f9,stroke:#0891b2,stroke-width:1px;
classDef sky fill:#7dd3fc,stroke:#0284c7,stroke-width:1px;
classDef violet fill:#c4b5fd,stroke:#7c3aed,stroke-width:1px;
classDef fuchsia fill:#f0abfc,stroke:#c026d3,stroke-width:1px;
```

#### gitops.gitlabsandbox.cloud

```mermaid
graph LR
subgraph "GCP Project hackystack-gitops"
    GITOPS_OMNIBUS["Omnibus Instance (link)"]:::emerald
    GITOPS_ENVIRONMENTS("Environments GitLab Group"):::emerald
    GITOPS_RUNNER_MANAGER["Runner Manager"]:::emerald
    GITOPS_OMNIBUS -.- GITOPS_RUNNER_MANAGER
    GITOPS_OMNIBUS --> GITOPS_ENVIRONMENTS
    GITOPS_HANDBOOK["Handbook Instructions (link)"]:::violet
    click GITOPS_OMNIBUS "https://gitops.gitlabsandbox.cloud" "Access System" _blank
    click GITOPS_HANDBOOK "https://about.gitlab.com/handbook/infrastructure-standards/realms/sandbox/#how-to-create-a-terraform-environment" "Usage Instructions" _blank
end
subgraph "ops.gitlab.net/it-infra-realm/.../gitops"
    GITOPS_IAC["gitops-gitlabsandbox-cloud-iac Repo (link)<br />Terraform CI/CD Pipeline"]:::emerald
    click GITOPS_IAC "https://ops.gitlab.net/it-infra-realm/environments/gcp/gcp-project-hackystack-gitops/gitops-gitlabsandbox-cloud-iac" "Open Repository" _blank
end
classDef slate fill:#cbd5e1,stroke:#475569,stroke-width:1px;
classDef red fill:#fca5a5,stroke:#dc2626,stroke-width:1px;
classDef orange fill:#fdba74,stroke:#ea580c,stroke-width:1px;
classDef yellow fill:#fcd34d,stroke:#ca8a04,stroke-width:1px;
classDef emerald fill:#6ee7b7,stroke:#059669,stroke-width:1px;
classDef cyan fill:#67e8f9,stroke:#0891b2,stroke-width:1px;
classDef sky fill:#7dd3fc,stroke:#0284c7,stroke-width:1px;
classDef violet fill:#c4b5fd,stroke:#7c3aed,stroke-width:1px;
classDef fuchsia fill:#f0abfc,stroke:#c026d3,stroke-width:1px;
```
