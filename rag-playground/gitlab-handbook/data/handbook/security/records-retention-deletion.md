---
title: "Records Retention & Disposal"
---

{{% alert title="This is a Controlled Document" color="danger" %}}
Inline with GitLab's regulatory obligations, changes to [controlled documents]({{< ref "controlled-document-procedure" >}}) must be approved or merged by a code owner. All contributions are welcome and encouraged.
{{% /alert %}}

## Purpose

The GitLab records retention and disposal standard lists the specific retention and secure disposal requirements for critical GitLab records. These minimum requirements inform design and maintenance decisions for all GitLab [tier 1 and tier 2 critical systems]({{< ref "critical-systems" >}}).

## Scope

The below retention and secure disposal requirements apply to all GitLab records enumerated in the table below stored in GitLab [tier 1 and tier 2 critical systems]({{< ref "critical-systems" >}}).

## Roles & Responsibilities

| Role  | Responsibility |
|-----------|-----------|
| GitLab Team Members | Responsible for following the requirements in this controlled document. |
| Security Compliance Team | Responsible for reviewing and maintaining this controlled document. |
| Control Owners | Responsible for defining and implementing procedures to support the below requirements. |
| Security Assurance Management (Code Owners) | Responsible for approving significant changes and exceptions to this controlled document. |

## Retention & Disposal Requirements Procedure

| Record                                             | Retention Requirement     | Disposal Requirement      |
|----------------------------------------------------|---------------------------|---------------------------|
| Business continuity plan approvals                 | 3 years                   | [GCP/AWS Secure Deletion] |
| Business continuity test results                   | 3 years                   | [GCP/AWS Secure Deletion] |
| Production backup tests                            | 1 year                    | [GCP/AWS Secure Deletion] |
| Production changes                                 | 3 years                   | [GCP/AWS Secure Deletion] |
| Security policy review/approvals                   | 3 years                   | [GCP/AWS Secure Deletion] |
| Terms of service acceptance                        | As long as user is active | [GCP/AWS Secure Deletion] |
| Access request/change records                      | 1 year                    | [GCP/AWS Secure Deletion] |
| Team-member offboarding issues                     | Varies by local laws                   | [GCP/AWS Secure Deletion] |
| System access reviews                              | 1 year 3 months           | [GCP/AWS Secure Deletion] |
| Shared and group authentication reviews            | 1 year 3 months           | [GCP/AWS Secure Deletion] |
| Production audit logs                              | 1 year                    | [GCP/AWS Secure Deletion] |
| GCP firewall configuration artifacts               | 1 year                    | [GCP/AWS Secure Deletion] |
| Job roles and responsibilities                     | 1 year                    | [GCP/AWS Secure Deletion] |
| Security incident communication to customers       | 3 years                   | [GCP/AWS Secure Deletion] |
| Personnel-file records                             | Varies by local laws      | [GCP/AWS Secure Deletion] |
| 1:1 meeting notes                                  | Varies by local laws      | [GCP/AWS Secure Deletion] |
| On-boarding tickets                                | Varies by local laws                    | [GCP/AWS Secure Deletion] |
| Annual risk assessment report                      | 2 years                   | [GCP/AWS Secure Deletion] |
| Risk treatment plans                               | 3 years                   | [GCP/AWS Secure Deletion] |
| Security observation issues                        | 3 years                   | [GCP/AWS Secure Deletion] |
| Board of Directors meeting minutes                 | Indefinite                | N/A                       |
| Release notes                                      | 1 year                    | [GCP/AWS Secure Deletion] |
| Critical system activity logs                      | 60 days                   | [GCP/AWS Secure Deletion] |
| Security monitoring alerts/metrics                 | 3 years                   | [GCP/AWS Secure Deletion] |
| Vendor security review issues                      | 3 years                   | [GCP/AWS Secure Deletion] |
| Customer-signed MSA's                              | Indefinite                | N/A                       |
| Vendor NDA's                                       | Indefinite                | N/A                       |
| Annual security awareness training records         | 3 years                   | [GCP/AWS Secure Deletion] |
| Secure coding training records                     | 2 years                   | [GCP/AWS Secure Deletion] |
| Penetration testing reports and remediation issues | 2 years                   | [GCP/AWS Secure Deletion] |
| System patch records                               | 1 year                    | [GCP/AWS Secure Deletion] |
| Source code scanning results                       | 1 year                    | [GCP/AWS Secure Deletion] |
| ZenDesk tickets                                    | 3 years                   | [GCP/AWS Secure Deletion] |
| Nonpublic information review records               | 3 years                   | [GCP/AWS Secure Deletion] |
| Role-based security training records               | 3 years                   | [GCP/AWS Secure Deletion] |
| Audit log review records                           | 3 years                   | [GCP/AWS Secure Deletion] |
| Security assessment reports/observation            | 3 years                   | [GCP/AWS Secure Deletion] |
| Security configuration reviews/alerts              | 3 years                   | [GCP/AWS Secure Deletion] |
| Security authorization records                     | 3 years                   | [GCP/AWS Secure Deletion] |
| System connection requirements                     | 3 years                   | [GCP/AWS Secure Deletion] |
| Configuration change records                       | 3 years                   | [GCP/AWS Secure Deletion] |
| Security impact analysis records                   | 3 years                   | [GCP/AWS Secure Deletion] |
| Production asset inventory                         | 3 years                   | [GCP/AWS Secure Deletion] |
| BC training records                                | 3 years                   | [GCP/AWS Secure Deletion] |
| Production backups                                 | Organizationally-defined  | [GCP/AWS Secure Deletion] |
| Customer data backups                              | Organizationally-defined  | [GCP/AWS Secure Deletion] |
| Employment applications and interview notes (US-based applicants only)| 4 years (updated 2021-07)|N/A          |
| Temporary Files with PII data                      | As long as needed for business purpose | Per System's default deletion schedule            |

## Exceptions

Exceptions to these requirements will be tracked as per the [Information Security Policy Exception Management Process]({{< ref "_index.md#information-security-policy-exception-management-process" >}}).

## References

- Parent Policy: [Information Security Policy]({{< ref "_index.md" >}})
- [Controlled Document Procedure]({{< ref "controlled-document-procedure" >}})
- [Data Classification Standard]({{< ref "data-classification-standard" >}})
- [Google Cloud Platform data deletion](https://cloud.google.com/security/deletion)
