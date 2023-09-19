---
title: "Information Security Management System"
---

{{% alert title="This is a Controlled Document" color="danger" %}}
Inline with GitLab's regulatory obligations, changes to [controlled documents]({{< ref "controlled-document-procedure" >}}) must be approved or merged by a code owner. All contributions are welcome and encouraged.
{{% /alert %}}

## Purpose

GitLab has adopted the ISO/IEC 27001:2013, ISO/IEC 27017:2015 and ISO/IEC 27018:2019 standards for our information security management system (ISMS) to provide GitLab team members, customers and community members with a high level of assurance on the robustness of our information security policies, standards and procedures, and the strength of our control environment. The purpose of this document is to define the boundaries and objectives of GitLab's ISMS.

## Scope

The scope of GitLab's ISMS is limited to the production resources that directly support GitLab SaaS subscriptions: GitLab.com and GitLab Dedicated.

#### Assets

Assets within the scope of the ISMS include: customer data, software, people, and internal information assets to host and operate the cloud-based solution.

External assets that are subject to shared responsiblity include cloud service providers. The scope of shared responsibility considerations include: assets maintained and stored in the cloud computing environment, infrastructure assets management, processes that run on a multi-tenant virtualized environment, and cloud service administration.

#### Excluded from Scope

As an all remote company, there are no physical office locations in the scope of the ISMS. Contracted third party data center services to include physical and environmental controls are not in scope and are managed by the third party service providers.

#### Locations

GitLab's headquarter mailing address is in scope and covers all sub organizations. Please note this is a mailing address only, there is no physical location to visit:

- GitLab Inc, 268 Bush Street #350, San Francisco, CA 94104, United States of America

### Organizational Units

Business functions included in the scope of the ISMS include:
- Engineering - Chief Information Security Officer; Security Assurance sub-department; Application Security, Security Operations, Security Incident Response (SIRT), Infrastructure Security teams
- Engineering - VP of Development
- Engineering - VP of Infrastructure and Quality
- Finance - VP of Information Technology
- People Operations - VP of Total Rewards and People Operations, Technology and Analytics
- Legal - VP of Legal Operations; Senior Director, Contracts and Legal Operations; Director of Legal, Privacy and Product

### Interested Parties

This ISMS governs GitLab security operations. Interested parties include:

- Customers
   - Require GitLab to operate according to this ISMS to protect their information
- Shareholders/owners of the business
   - Require GitLab to operate in a secure manner to maintain a sustainable business
- Team Members
   - GitLab requires Team Members to operate in a secure manner as defined by this ISMS. Require GitLab to operate in a secure manner to maintain services and provide continued employment

## ISMS Roles and Responsibilities

| Role | Responsibility |
| --- | --- |
| ISMS Council | Oversight, implementation and continual improvement of the ISMS |
| Chief Information Security Officer | Executive sponsor of the ISMS; coordinate, promote and improve information security; establish information security policy |
| Security Management (Code Owners) | Owner of the ISMS responsible for approving significant changes and exceptions of the ISMS |
| Security Assurance | Reporting on the performance of the information security management system to top management; security risk assessments and treatment; continuous monitoring and auditing; customer assurance activities; security awareness program; security governance activities |
| Application Security | Manage third party penetration and bug bounty programs; provide input to the software development lifecycle; manage application vulnerability program; administer security champions program; maintain application security tools; identify security risks |
| Security Operations | Monitor, manage and report on security incidents; monitor compliance with security policies through technical tools; identify security risks; monitor and respond to abuse of SaaS subscriptions |
| Infrastructure Security | Manage infrastructure vulnerability program; maintain infrastructure security tools; identify security risks |
| Other ISMS Business units | Implement, operate and/or administer information security requirements; remediate information security findings; collaborate with the Security department |
| All GitLab Team Members | Awareness of responsibilities as it relates to information security; adherence to information security controlled documents; reporting of suspected security violations |

## Implementation Manual Procedure

### Leadership

GitLab is committed to information security. The general objective for the ISMS is to protect GitLab's confidential information and assets against new and existing security and privacy risks while maintaining confidentiality, integrity and availability. Objectives for individual security controls are inherited by the in scope security standards and regulations which are: ISO 27001, and SOC 2 Type 2 Security.

The ISMS council, comprised of Security and Privacy (Legal) leadership, shall meet on a minimum of an annual basis to discuss the state of the ISMS and measure the fulfillment of all ISMS objectives. The following topics will be covered:

- Review of membership and objectives
- ISMS Internal Audit Results
- Significant controlled document updates
- Results of the Annual Security Risk Assessment
- Changes to Risk Heatmap (trends)
- Output from Continuous Control Monitoring
- Observations (CA/PAs)
- Changes that could affect the ISMS
- Feedback and improvements
- ISMS inputs and outputs

### Planning

GitLab has implemented a formal [Security Operational Risk Management (“StORM”) program]({{< ref "storm-program" >}}) to identify, rank, track, and treat cybersecurity, IT, and privacy operational risks in support of GitLab's organization-wide objectives. The process for selecting in scope information security controls is executed by the Security Compliance team, leveraging technical functionality from the third party GRC application, and overseen by the Security Risk team. Implementation status is captured in GitLab's GRC application as well as in the Statement of Applicability.

The GitLab Security team executes quarterly cascading [Objectives and Key Results (OKRs)]({{< ref "okrs" >}}) to define our security objectives and a plan for achieving those objectives while ensuring alignment throughout the organization.

### Support

GitLab has implemented a formal security awareness training program that includes: new hire security awareness training, global annual security awareness training and quarterly targeted phishing exercises. These trainings are administered via a third party portal and include a quiz to test understanding of the security topics presented.

A formal [controlled document procedure]({{< ref "controlled-document-procedure" >}}) is in place to ensure that there is consistency in developing and maintaining controlled documents at GitLab utilizing a hierarchal approach. All controlled documents are available to all GitLab team members and the public via the [GitLab handbook]({{< ref "/" >}}) unless otherwise noted. Updates to controlled documents are managed via [GitLab merge requests](https://docs.gitlab.com/ee/user/project/merge_requests/) which are also accessible to all GitLab team members for the entire workflow. An annual review of controlled documents is required by the ISMS owner or assigned representative.

GitLab publishes [Job Families](https://about.gitlab.com/handbook/hiring/job-families/) to define roles and responsibilities based on level for all team members. This information is publicly available and the foundation for team member hiring and performance reviews. On a minimum of an annual basis, GitLab management executes [talent assessments](https://about.gitlab.com/handbook/people-group/talent-assessment/) with team members to ensure competency to Job Family.

### Operations

The [GitLab team handbook]({{< ref "/" >}}) is the central repository for how we run the company. Everything at GitLab is handbook first, to include development of company policies, standards and procedures. Key controlled documents that support the ISMS include:

- [Data Classification Standard]({{< ref "data-classification-standard" >}})
- [Internal Acceptable Use Policy](https://about.gitlab.com/handbook/people-group/acceptable-use-policy/)
- [Security Policies]({{< ref "_index.md#information-security-policies" >}})
- [GitLab Code of Business Conduct and Ethics](https://ir.gitlab.com/static-files/7d8c7eb3-cb17-4d68-a607-1b7a1fa1c95d)
- [Infrastucture Change Management Procedure](https://about.gitlab.com/handbook/engineering/infrastructure/change-management/)
- [Security Operational Risk Management (StORM) Program & Procedures]({{< ref "storm-program" >}})

GitLab has a dedicated Security Compliance team responsible for monitoring design and effectiveness of the [GitLab common control framework]({{< ref "sec-controls" >}}) to ensure GitLab's security objectives are thoughtfully planned, implemented and monitored.

If using a third party service to outsource or supplement security processes, a [third party risk assessment]({{< ref "third-party-risk-management" >}}) is executed prior to onboarding. Critical vendors are also reviewed once per calendar year after onboarding, or at contract renewal if it comes first.

### Performance

GitLab monitors, measures, and improves security controls through various continuous monitoring measures, such as:

- [Continuous control testing/Annual ISMS internal compliance audits]({{< ref "security-control-lifecycle" >}})
- [External audits (SOC 2 Type 2, SOC 3, customer security assessments)]({{< ref "./security-assurance/security-compliance/certifications" >}})
- [Annual security operational risk assessments]({{< ref "storm-program" >}})
- [Annual third-party penetration testing]({{< ref "penetration-testing-policy" >}})
- [Ongoing third party scorecard monitoring (BitSight)]({{< ref "independent_security_assurance#third-party-security-ratings" >}})
- [Infrastructure Vulnerability scanning]({{< ref "./threat-management/vulnerability-management" >}})
- [Application Vulnerability Scanning]({{< ref "./security-engineering/application-security/vulnerability-management" >}})
- [HackerOne bug bounty program]({{< ref "hackerone-process" >}})
- [Audit log monitoring]({{< ref "audit-logging-policy" >}})
- ISMS Council (annual management review)

### Improvement

GitLab is committed to continually improving the suitability, adequacy and effectiveness of the ISMS.

As part of GitLab's tier 2 security operational risk program, each risk identified and triaged through the StORM program is required to undergo a [risk response decision]({{< ref "storm-program#risk-response" >}}). This is an activity that will be discussed with each individual risk owner for the risks that they own. Additionally, GitLab identifies and monitors tier 3 risks, also referred to as observations, as per the [Observation Management Procedure]({{< ref "observation-remediation-procedure" >}}).

## Exceptions

Exceptions to Information Security policies or procedures will be tracked as per the [Information Security Policy Exception Management Process]({{< ref "_index.md#information-security-policy-exception-management-process" >}}).

## References

- Policy: [Information Security Policy]({{< ref "_index.md" >}})
