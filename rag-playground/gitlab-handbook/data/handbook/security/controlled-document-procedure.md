---
title: "Controlled Document Procedure"
description: "GitLab deploys control activities through policies and standards that establish what is expected and procedures that put policies and standards into action."
---

{{% alert title="This is a Controlled Document" color="danger" %}}
Inline with GitLab's regulatory obligations, changes to [controlled documents]({{< ref "controlled-document-procedure" >}}) must be approved or merged by a code owner. All contributions are welcome and encouraged.
{{% /alert %}}

## Purpose

GitLab deploys control activities through policies and standards that establish what is expected and procedures that put policies and standards into action.

The purpose of this procedure is to ensure that there is consistency in developing and maintaining controlled documents at GitLab utilizing a hierarchal approach for managing legal and regulatory requirements.

There are two types of documentation at GitLab:

1. Controlled Documents: Formal policies, standards and procedures.
1. Uncontrolled Documents: Informal runbooks, certain handbook pages, guidelines, blog posts, templates, etc.

Everyone at GitLab is welcomed and encouraged to submit an MR to create or suggest changes to controlled documents at any time.

## Scope

This procedure applies to all [controlled documents](#list-of-controlled-documents) developed in support of GitLab's statutory, regulatory and contractual requirements. Uncontrolled documents are dynamic in nature and not in scope of this procedure.


## Roles & Responsibilities:

| Role  | Responsibility |
|-----------|-----------|
| Security Compliance Team | Responsible for implementing and maintaining Security Policies and oversight of supporting standards and procedures as part of ongoing continuous control monitoring |
| Security Governance Team | Responsible for conducting annual controlled documents review
| Security Assurance Management (Code Owners) | Responsible for approving changes to this procedure |
| Control Owners | Responsible for defining and implementing procedures to support Security policies and standards |

## Procedure

### Definitions by Hierarchy

![CD Pyramid](/handbook/security/security-assurance/images/CDPyramidv2.png)

Footnote: <sub>https://docs.google.com/presentation/d/125LxBkIx0gj42Ooky8hcx9HY2GEjfomDRdR_o-qbOpc/edit#slide=id.g1234fd827e0_0_0</sub>

- Policy: A policy is a high-level statement of intent and defines GitLab's goals, objectives and culture. Statutory, regulatory, or contractual obligations are commonly the root cause for a policy’s existence. Policies are designed to be centrally managed at the organizational level (e.g. Security Compliance Team or Legal & Ethics Compliance Team).
- Standard: Standards are mandatory actions or rules that give formal policies support and direction by providing specific details that enable policies to be implemented. Standards may take the form of technical diagrams.
- Procedure: Procedures are detailed instructions to achieve a given policy and, if applicable, supporting standard and provid step-by-step instructions to follow. Procedures are decentralized and managed by process/control owners where a security control is translated into a business process.

### Creation

At minimum, controlled documents should cover the following key topic areas:

- Purpose: Overview of why the controlled document is being implemented.
- Scope: Who or what does the controlled document apply to.
- Roles & Responsibilities: Who is responsible for doing what. This should refer to departments or roles instead of specific individuals.
- Policy Statements, Standard or Procedure: The details.
- Exceptions: Define how exceptions to the controlled document will be tracked.
- References:  Procedure documents should map back to a governing policy or standard, and may relate to one or more procedures or other uncontrolled documentation.

### Publishing

Creation of, or changes to, controlled documents must be approved by management or a formally designated representative of the owning department as defined in the Code Owners file prior to publishing.

Most controlled documents will be published to our public facing [handbook]({{< ref "/" >}}). However, if there is [non public data]({{< ref "data-classification-standard" >}}) included in the controlled document, it should be published via an *internal facing only* mechanism (e.g. an internal GitLab project or an internal only handbook page). Controlled documents should be accessible to all internal team members.

### Review

Controlled documents are required to be reviewed and approved on at least an annual basis. Controlled documents may be updated ad-hoc as required by business operations. Ad-hoc changes do not need to be reviewed and approved, but can only be merged by a code owner of the controlled document.

Reviewers of controlled documents are required to

1. Ensure that ["say why not just what" transparency]({{< ref "values#say-why-not-just-what" >}}) is easily understood in the description. The title should be concise but clear on the what.
1. Ensure that announcements for team members are scheduled ([Slack, company newsletter](https://about.gitlab.com/handbook/people-group/employment-branding/people-communications/)), and tick off the [MR template task](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/.gitlab/merge_request_templates/Default.md).

#### List of Controlled Documents

<details markdown="1">

| Document Name | Description | URL | Code Owners |
| :----: | :--------------------------------------: | :----: |:----:  |
| Acceptable Use Policy | Specifies requirements related to the use of GitLab computing resources and data assets by GitLab team members so as to protect our customers, team members, contractors, company, and other partners from harm caused by both deliberate and inadvertent misuse. | [https://about.gitlab.com/handbook/people-group/acceptable-use-policy/](https://about.gitlab.com/handbook/people-group/acceptable-use-policy/)| Security, Legal and PeopleOps |
| Access Level Wristband Colors | Establishes access level categories for managing access to systems at GitLab | [https://about.gitlab.com/handbook/it/policies/access-level-wristbands/](https://about.gitlab.com/handbook/it/policies/access-level-wristbands/) | IT Management |
| Access Management Policy | Specifies Centralized access management ensuring that the authorized GitLab team-members have access to the correct data and systems at the correct level. | [https://about.gitlab.com/handbook/security/access-management-policy.html](https://about.gitlab.com/handbook/security/access-management-policy.html)| Security Assurance Management |
| Access Review Procedure | Defines the importance of the User access review process as an important control activity required for internal and external IT audits, helping to minimize threats, and provide assurance of who has access to what. | [https://about.gitlab.com/handbook/security/security-assurance/security-compliance/access-reviews.html](https://about.gitlab.com/handbook/security/security-assurance/security-compliance/access-reviews.html)| Security Compliance Team |
| Application Vulnerability Management Procedure | Designed to provide insight into our environments, promote healthy patch management among other preventative best-practices, and remediate risk; all with the end goal to better secure our environments and our product. | [https://about.gitlab.com/handbook/security/security-engineering/application-security/vulnerability-management.html](https://about.gitlab.com/handbook/security/security-engineering/application-security/vulnerability-management.html) | Security Management |
| Audit Logging Policy | Ensures the proper operation and security of critical information system activity. | [https://about.gitlab.com/handbook/security/audit-logging-policy.html](https://about.gitlab.com/handbook/security/audit-logging-policy.html) | Security Assurance Management |
| Backup Procedure | Documents that our production databases are taken every 24 hours with continuous incremental data (at 60 sec intervals). | [https://about.gitlab.com/handbook/engineering/infrastructure/production/#backups](https://about.gitlab.com/handbook/engineering/infrastructure/production/#backups) | Infrastructure Management Team |
| Backup Recovery Testing Procedure | Documentation implementing a backup testing pipeline to detect whether or not the backup is actually restorable and in good shape. | [https://gitlab.com/gitlab-com/gl-infra/gitlab-restore/postgres-gprd/blob/master/README.md](https://gitlab.com/gitlab-com/gl-infra/gitlab-restore/postgres-gprd/blob/master/README.md) | Infrastructure Management Team |
| Business Continuity Plan | Documentation of our overall organizational program for achieving continuity of operations for business functions. Continuity planning addresses both information system restoration and implementation of alternative business processes when systems are compromised. | [https://about.gitlab.com/handbook/business-technology/gitlab-business-continuity-plan/](https://about.gitlab.com/handbook/business-technology/gitlab-business-continuity-plan/) | Information Technology Team |
| Business Impact Analysis (BIA) | Documents how we identify and prioritize system components by correlating them to mission critical processes that support the functioning of GitLab. | [https://about.gitlab.com/handbook/security/security-assurance/security-risk/storm-program/business-impact-analysis.html](https://about.gitlab.com/handbook/security/security-assurance/security-risk/storm-program/business-impact-analysis.html) | Security Risk Team |
| Change Management Policy | A policy establishing the minimum requirements for changes related to production systems and supporting infrastructure across the organization. | [https://about.gitlab.com/handbook/security/change-management-policy.html](https://about.gitlab.com/handbook/security/change-management-policy.html) | Security Management |
| Change Management Procedure | Specifies requirements to manage changes in the operational environment with the aim of doing so (in order of highest to lowest priority) safely, effectively and efficiently. | [https://about.gitlab.com/handbook/engineering/infrastructure/change-management/](https://about.gitlab.com/handbook/engineering/infrastructure/change-management/) | Infrastructure Management Team |
| Control Health and Effectiveness Rating (CHER) Procedure | A rating system to help determine the health and effectiveness of security controls. | [https://about.gitlab.com/handbook/security/security-assurance/control-health-effectiveness-rating.html](https://about.gitlab.com/handbook/security/security-assurance/control-health-effectiveness-rating.html) | Security Assurance Management |
| Controlled Document Procedure | Deploying control activities through policies and standards that establish what is expected and procedures that put policies and standards into action ensuring there is consistency in developing and maintaining controlled documents at GitLab utilizing a hierarchal approach for managing legal and regulatory requirements. | [https://about.gitlab.com/handbook/security/controlled-document-procedure.html](https://about.gitlab.com/handbook/security/controlled-document-procedure.html) | Security Assurance Management |
| Cryptography Standard | Defines approved cryptographic algorithms, settings, and cryptographic modules for the purposes of encrypting data at rest or in transit within the various systems and subsystems used by the GitLab product. | [https://about.gitlab.com/handbook/security/cryptographic-standard.html](https://about.gitlab.com/handbook/security/cryptographic-standard.html) | Security Management |
| Data Classification Standard | Defines data categories and provides a matrix of security and privacy controls for the purposes of determining the level of protection to be applied to GitLab data throughout its lifecycle. | [https://about.gitlab.com/handbook/security/data-classification-standard.html](https://about.gitlab.com/handbook/security/data-classification-standard.html) | Security Assurance Management |
| Data Protection Impact Assessment (DPIA) Policy | Ensures that our use of personal data is fully understood, that risks to the rights and freedoms of individuals resulting from the processing of personal data are carefully examined and that all appropriate measures are put in place to protect these rights throughout the lifecycle of the processing. DPIAs, in conjunction with the associated forms and guidance, should be used to ensure that our obligations and policies in this area are met. |[https://about.gitlab.com/handbook/legal/privacy/dpia-policy/](https://about.gitlab.com/handbook/legal/privacy/dpia-policy/)| Security Management |
| Data Management Standard | Documents how the data team delivers results that matter securing our data. | [https://about.gitlab.com/handbook/business-technology/data-team/data-management/](https://about.gitlab.com/handbook/business-technology/data-team/data-management/) | Data Team Management |
| Data Platform Guidelines | Identifies our guidelines for the data flow diagram, system tiers and access. | [https://about.gitlab.com/handbook/business-technology/data-team/platform/](https://about.gitlab.com/handbook/business-technology/data-team/platform/) | Data Team Management |
| Database Disaster Recovery Procedure | Documents our disaster recovery for databases. | [https://about.gitlab.com/handbook/engineering/infrastructure/database/disaster_recovery.html](https://about.gitlab.com/handbook/engineering/infrastructure/database/disaster_recovery.html) | Infrastructure Management Team |
| Disaster Recovery Procedure| Documents our disaster recovery. | [https://gitlab.com/gitlab-com/gl-infra/readiness/-/blob/master/library/disaster-recovery/index.md](https://gitlab.com/gitlab-com/gl-infra/readiness/-/blob/master/library/disaster-recovery/index.md) | Infrastructure Management Team |
| Encryption Policy | Documents the encryption process in which data is securely encoded at rest and in transit to remain hidden from or inaccessible to unauthorized users to better protect private, proprietary and sensitive data and enhance the security of communication between client applications and servers. | [https://about.gitlab.com/handbook/security/threat-management/vulnerability-management/encryption-policy.html](https://about.gitlab.com/handbook/security/threat-management/vulnerability-management/encryption-policy.html) | Security Threat Management |
| EndPoint Management Procedure | GitLab utilizes centralized laptop management for company-issued laptops. | [https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/endpoint-management/](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/endpoint-management/) | Business Technology Management |
| Expense Policy | Establishes the requirements for submitting expenses at GitLab. | [https://about.gitlab.com/handbook/finance/expenses/](https://about.gitlab.com/handbook/finance/expenses/) | Finance Management |
| FedRAMP Vulnerability Deviation Request Procedure | Establishes a process for managing vulnerabilities that cannot be remediated within SLAs. | [https://about.gitlab.com/handbook/security/security-assurance/dedicated-compliance/POAM-Deviation-Request-Procedure.html](https://about.gitlab.com/handbook/security/security-assurance/dedicated-compliance/POAM-Deviation-Request-Procedure.html) | Security Assurance Management |
| GCF Security Control Procedure | GCF Security Controls identified that need to be implemented by the security compliance team and dedicated team for compliance or regulatory reasons, these controls follow an established process in order to make that implementation successful. | [https://about.gitlab.com/handbook/security/security-assurance/security-compliance/security-control-lifecycle.html](https://about.gitlab.com/handbook/security/security-assurance/security-compliance/security-control-lifecycle.html) | Security Compliance Management |
| GitLab Password Standards | Passwords are one of the primary mechanisms that protect GitLab information systems and other resources from unauthorized use. Constructing secure passwords and ensuring proper password management is essential. | [https://about.gitlab.com/handbook/security/password-procedure.html](https://about.gitlab.com/handbook/security/password-standard.html) | Security Assurance Management |
| GitLab Terms of Service | Documents the terms of service when using GitLab | [https://about.gitlab.com/terms/](https://about.gitlab.com/terms/) | GitLab Legal |
| Information Security Management System (ISMS) | Documents the boundaries and objectives of GitLab's ISMS | [https://about.gitlab.com/handbook/security/ISMS.html](https://about.gitlab.com/handbook/security/ISMS.html) | Security Assurance Management |
| Infrastructure Vulnerability Management Procedure | This procedure provides insight into the GitLab production environment, promotes healthy patch management among other preventative best-practices, and remediates risk; all with the end goal to better secure our environments and our product | [https://about.gitlab.com/handbook/security/threat-management/vulnerability-management/Infrastructure-vulnerability-procedure.html](https://about.gitlab.com/handbook/security/threat-management/vulnerability-management/Infrastructure-vulnerability-procedure.html) | Security Threat Management |
| IT Help Team Standards | Documents IT Support responsibilities for onboarding and managing company assets. | [https://about.gitlab.com/handbook/business-technology/team-member-enablement/self-help-troubleshooting/](https://about.gitlab.com/handbook/business-technology/team-member-enablement/self-help-troubleshooting/) | Business Technology Management |
| IT Ops Policy and Standards | Documents IT Operations responsibilities for onboarding and managing company assets. | [https://about.gitlab.com/handbook/business-technology/employee-enablement/it-ops-team/](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/) | Business Technology Management |
| Network Security Management Procedure | Documents network security and privacy requirements for the safety of GitLab's network infrastructure | [https://about.gitlab.com/handbook/engineering/infrastructure/network-security/](https://about.gitlab.com/handbook/engineering/infrastructure/network-security/) | Infrastructure Management |
| Off-boarding Procedure | Documents off-boarding step by step process that covers all the steps necessary to successfully part ways with an employee following their resignation or termination. When done well, a clear offboarding process ensures a smooth transition for both the company and the departing employee. | [https://about.gitlab.com/handbook/offboarding/offboarding_standards/](https://about.gitlab.com/handbook/people-group/offboarding/offboarding_standards/) | People Management |
| Penetration Testing Policy | Document determines whether or not defensive measures employed on the system are strong enough to prevent security breaches. Penetration test reports also suggest the countermeasures that can be taken to reduce the risk of the system being attacked. | [https://about.gitlab.com/handbook/security/penetration-testing-policy.html](https://about.gitlab.com/handbook/security/penetration-testing-policy.html) | Security Assurance Management |
| People Policies | These policies document the benefits, procedures, and requirements of the company. | [https://about.gitlab.com/handbook/people-policies/](https://about.gitlab.com/handbook/people-policies/) | People Management |
| Production Architecture | The GitLab.com core infrastructure is primarily hosted in Google Cloud Platform's (GCP) us-east1 region (see Regions and Zones)—and we use GCP iconography in our diagrams to represent GCP resources. We do have dependencies on other cloud providers for separate functions. Some of the dependencies are legacy fragments from our migration from Azure, and others are deliberate to separate concerns in the event of cloud provider service disruption. This document does not cover servers that are not integral to the public facing operations of GitLab.com. | [https://about.gitlab.com/handbook/engineering/infrastructure/production/architecture/](https://about.gitlab.com/handbook/engineering/infrastructure/production/architecture/) | Infrastructure Management Team |
| Records Retention & Disposal Procedure | Documents the specific retention and secure disposal requirements for critical GitLab records. | [https://about.gitlab.com/handbook/security/records-retention-deletion.html](https://about.gitlab.com/handbook/security/records-retention-deletion.html) | Security Risk Management |
| Security Operational Risk Management Procedure | The Information Security Risk Management Program performs risk analysis of information resources that store, process or transmit an organization's data. The purpose of the Security Operational Risk Management (“StORM”) program at GitLab is to identify, track, and treat security operational risks in support of GitLab's organization-wide objectives. The Security Risk team utilizes the procedures below to ensure that security risks that may impact GitLab's ability to achieve its customer commitments and operational objectives are effectively identified and treated. | [https://about.gitlab.com/handbook/security/security-assurance/security-risk/storm-program/](https://about.gitlab.com/handbook/security/security-assurance/security-risk/storm-program/) | Security Risk Management |
| Security Change Management Procedure | Outlines the procedural change management steps as they relate to the Security Department. | [https://about.gitlab.com/handbook/security/security-change-management-procedure](https://about.gitlab.com/handbook/security/security-change-management-procedure.html) | Security Assurance Management |
| Security Compliance Observation Creation Procedure | Defines the risks identified at the information system or business process levels and details the creation process for observations. | [https://about.gitlab.com/handbook/security/security-assurance/observation-management-procedure.html](https://about.gitlab.com/handbook/security/security-assurance/observation-management-procedure.html) | Security Compliance Management |
| Security Compliance Observation Remediation Procedure | Defines the risks identified at the information system or business process levels and details the remediation process for observations. | [https://about.gitlab.com/handbook/security/security-assurance/observation-remediation-procedure.html](https://about.gitlab.com/handbook/security/security-assurance/observation-remediation-procedure.html) | Security Compliance Management |
| Security Incident Communications Plan Procedure | Documents the communication response plan to map out the who, what, when, and how of GitLab in notifying and engaging with internal stakeholders and external customers on security incidents. This plan of action covers the strategy and approach for security events which have a ‘high’ or greater impact as outlined in GitLab’s risk scoring matrix. | [https://about.gitlab.com/handbook/security/security-operations/sirt/security-incident-communication-plan.html](https://about.gitlab.com/handbook/security/security-operations/sirt/security-incident-communication-plan.html) | Security Management |
| Security Incident Response Guide | Documents the responsibilities of all GitLab team members when responding to or reporting security incidents. | [https://about.gitlab.com/handbook/security/security-operations/sirt/sec-incident-response.html](https://about.gitlab.com/handbook/security/security-operations/sirt/sec-incident-response.html) | Security Management |
| Security Operations On-Call Guide (Major Incidents) | Documents how the Security Operations Team (SecOps) is collectively on-call 24/7/365, split into 12-hour shifts Monday to Friday and 48-hour coverage Saturday and Sunday. | [https://about.gitlab.com/handbook/security/secops-oncall.html#major-incident-response-workflow](https://about.gitlab.com/handbook/security/secops-oncall.html#major-incident-response-workflow) | Security Assurance Management |
| Security Trainings Procedure | Describes the security awareness training program that provides ongoing training to GitLab team members that enhances knowledge and identification of cybersecurity threats, vulnerabilities, and attacks. | [https://about.gitlab.com/handbook/security/security-assurance/governance/sec-training.html](https://about.gitlab.com/handbook/security/security-assurance/governance/sec-training.html) | Security Assurance Management |
| Third Party Risk Management Program | Documents the process in order to minimize the risk associated with third party applications and services. The Security Risk Team performs security reviews on new and renewing third party vendors that are requested through the procurement process. | [https://about.gitlab.com/handbook/security/security-assurance/security-risk/third-party-risk-management.html](https://about.gitlab.com/handbook/security/security-assurance/security-risk/third-party-risk-management.html) | Security Risk Management |
| Token Management Standard | Outlines "GitLab's" approved standards for token usage, settings, and distribution for the purposes of providing authentication and authorization within the various systems and subsystems used to support "GitLab's" product. | [https://about.gitlab.com/handbook/security/token-management-standard.html](https://about.gitlab.com/handbook/security/token-management-standard.html) | Security Assurance Management |
| Vulnerability Management Standard | Documents the continual process of identifying, prioritizing, mitigating and remediating vulnerabilities. This standard will focus on impact to in-scope GitLab systems in order to reduce the risk relating to security vulnerabilities that could impact the achievement of GitLab goals. | [https://about.gitlab.com/handbook/security/threat-management/vulnerability-management/](https://about.gitlab.com/handbook/security/threat-management/vulnerability-management/) | Security Threat Management |

</details>

## Exceptions

Exceptions to controlled documents must be tracked and approved by the controlled document approver(s) via an auditable format. An exception process should be defined in each controlled document.

Exceptions to this procedure will be tracked as per the [Information Security Policy Exception Management Process]({{< ref "_index.md#information-security-policy-exception-management-process" >}}).

## References

- Parent Policy: [Information Security Policy]({{< ref "_index.md" >}})
- [GCF Compliance Controls]({{< ref "sec-controls" >}})
- [Data Classifiation Standard]({{< ref "data-classification-standard" >}})
- [Controlled Documents Work Instruction](https://gitlab.com/gitlab-com/gl-security/security-assurance/governance/controlled-documents-program/-/blob/main/runbooks/controlled_document_annual_review_work_instruction.md)
