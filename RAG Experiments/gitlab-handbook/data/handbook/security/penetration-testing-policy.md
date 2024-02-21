---
title: "Penetration Testing Policy"
---

{{% alert title="This is a Controlled Document" color="danger" %}}
Inline with GitLab's regulatory obligations, changes to [controlled documents]({{< ref "controlled-document-procedure" >}}) must be approved or merged by a code owner. All contributions are welcome and encouraged.
{{% /alert %}}

A penetration test is a process to identify security vulnerabilities in an application or infrastructure in order to evaluate the security of the system.

GitLab performs external, independent penetration testing at least annually with a firm that has a strong reputation within the security industry. This testing is done against production and internal systems, if it is determined that a significant change has been made to applications or infrastructure.

## Purpose

The purpose of this test is to secure personal, confidential, and sensitive data.

A penetration test determines whether or not defensive measures employed on the system are strong enough to prevent security breaches. Penetration test reports also suggest the countermeasures that can be taken to reduce the risk of the system being attacked.

## Scope of Penetration Testing

The scope of a GitLab's Penetration Testing may vary due to a number of factors including priority and resources but will be explicitly outlined prior to any Penetration Testing taking place. On an annual basis, a third party penetration test will be performed, targeting the core gitlab application stack for the GitLab.com and GitLab Dedicated production environments. A white-box testing approach is used, and the testing targets web applications and web services (e.g. API), external network perimeter, and cloud infrastructure configuration.

## Roles & Responsibilities

| Role | Responsibility |
|----|-------|
| GitLab Team Members | Responsible for following the requirements in this policy |
| Security Team | Responsible for implementing and executing this policy |
| Security Management (Code Owners) | Responsible for approving significant changes and exceptions to this policy |

## Procedure

### Why GitLab should perform Penetration Testing

1. To meet the information security compliance requirements at GitLab and to implement an effective security strategy.
1. Independent testing brings a new perspective which reduces the likelihood of undiscovered errors made by GitLab.
1. Assure customers that their data is secure and that vulnerabilities are identified and remediated.
1. Many customers request evidence of penetration testing as part of contract negotiations.
1. Penetration testing at regular intervals is done to protect information systems against security breaches.
1. As a check to ensure that critical, sensitive, and personal data is secured while in-transit.
1. To find security vulnerabilities in an application or infrastructure which reduces the number of vulnerabilities discovered through 3rd party reporting, which saves GitLab money.
1. To assess the business impact of successful attacks.

### 1. Reporting and Analysis

Findings provided by a third-party penetration testing is reported to the Security Assurance team through specific systems and contract agreed upon.

### 2. Ingestion

Once the third-party provides a report of findings, we will manually ingest each of the findings (low and above). Issues are opened for each of the findings and assigned to specific team members and departments.

### 3. Validation

Validation issues should be tagged based on the severity recommended by the third-party to be triaged by the corresponding team. The following labels exist to track the workflow:

- `risk treatment::remediate`: This label is applied to issues that have been reviewed and agreed upon that will be remediated according to the defined SLAs.

- `risk treatment::mitigate severity::remediate`: This label is applied to issues that have been mitigated by another process and the residual risk reviewed and agreed upon that will be remediated according to the defined SLAs.

- `risk treatment::accept`: This label identifies that the finding has been validated as legitimate and has an approved exception (risk acceptance) issue to account for a business need. For additional details refer to the [Vulnerability Management Risk Acceptance (non-FedRAMP process)]({{< ref "./threat-management/vulnerability-management#non-fedramp-process" >}}).

- `risk treatment::mitigate severity::accept`: This label is applied to issues that have been mitigated by another process and the residual risk reviewed and agreed for risk acceptance. For additional details refer to the [Vulnerability Management Risk Acceptance (non-FedRAMP process)]({{< ref "./threat-management/vulnerability-management#non-fedramp-process" >}}).

- `risk treatment::false positive`: This label is used in an issue that is misstated or additional considerations were not present that will change its outcome. Additional information needs to be provided to indicate a false positive.

- `risk treatment::operational requirement`: This label is used if the issue is not able to be remediated due to technical constraints. This state will keep the issue open until it is able to be remediated in the future.

### 4. Remediation

Remediation is the part of the process in which a validated findings is fixed. SLAs are in place to help prioritize findings based on severity. The remediation SLA timeframes begin as soon as a finding is formally communicated and reported by the third-party pen testing. Once a finding is remediated, the third-party pen testing will validate that the finding is indeed remediated.

## Exceptions

Exceptions to this policy will be tracked as per the [Information Security Policy Exception Management Process]({{< ref "_index.md#information-security-policy-exception-management-process" >}}).

## References

- Parent Policy: [Information Security Policy]({{< ref "_index.md" >}})
