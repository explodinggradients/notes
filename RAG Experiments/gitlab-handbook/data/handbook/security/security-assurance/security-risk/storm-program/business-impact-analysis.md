---
title: "Business Impact Analysis"
description: "Information about the Business Impact Analysis that is carried out periodically by the Security Risk Team"
---

{{% alert title="This is a Controlled Document" color="danger" %}}
Inline with GitLab's regulatory obligations, changes to [controlled documents]({{< ref "controlled-document-procedure" >}}) must be approved or merged by a code owner. All contributions are welcome and encouraged.
{{% /alert %}}

## Purpose

The Business Impact Analysis (BIA) helps determine the systems critical to serving GitLab's Customers. It also helps determine the prioritization of system restoration efforts in the event of a disruption.

A BIA is performed for a system by completing a questionnaire. Each question in the BIA Questionnaire belongs to one of three data collection categories:

1. [Critical System Tier]({{< ref "critical-systems" >}}) (questions that guide how a system is tiered)
1. Supplemental Information (questions that prompt important system details)
1. [Security Best Practices]({{< ref "business-impact-analysis#responses-that-may-result-in-tier-3-observationsrisks" >}}) (questions that reveal potential Information System risks)

System data obtained through the BIA may be referenced for [Business Continuity](https://about.gitlab.com/handbook/business-technology/gitlab-business-continuity-plan/) planning and testing.

**Note:** Additionally, a subset of questions may be included in the BIA Questionnaire to satisfy [global privacy legislation requirements](https://about.gitlab.com/handbook/legal/privacy/privacy-laws.html#gdpr) pertaining to a system's [Personal Data]({{< ref "data-classification-standard#data-classification-definitions" >}}) processing.

## Scope

The BIA covers all systems in GitLab's [Tech Stack](https://about.gitlab.com/handbook/business-technology/tech-stack-applications/). However, the volume and frequency of the BIA is based on [Critical System Tiering]({{< ref "critical-systems" >}}). See the ['BIA Procedures']({{< ref "business-impact-analysis#bia-procedures" >}}) section for more details.

## Roles and Responsibilities

|Role|Responsibility|
|----------|------------------------------|
| [Security Risk Team]({{< ref "../../security-risk" >}}) |Responsible for implementing and executing this procedure periodically based on Critical System Tiering requirements. |
| [Business/Technical Owner](https://about.gitlab.com/handbook/business-technology/tech-stack-applications/#tech-stack-definitions) of a System | Responsible for performing a BIA or validating previously submitted BIA/Tech Stack Data. |
| Security Assurance Management (Code Owners)|Responsible for approving significant changes and exceptions to the BIA. |

## BIA Procedures

### New Systems (Ad-Hoc)

A BIA is initiated as the result of TPRM's process for net new systems (guided by our [report template](https://gitlab.com/gitlab-com/gl-security/security-assurance/security-risk-team/third-party-vendor-security-management/-/blob/master/.gitlab/issue_templates/TPRM%20Assessment%20Report%20Template.md)). An [associated Tracking Issue](https://gitlab.com/gitlab-com/gl-security/security-assurance/security-risk-team/third-party-vendor-security-management/-/blob/master/.gitlab/issue_templates/New%20System%20-%20TS%20Add%20and%20BIA%20Tracking.md) is created by the TPRM engineer to ensure that the new system has a BIA performed and is added to the Tech Stack.  The steps listed below summarize how BIAs are performed for new systems:

1. A formal BIA questionnaire is distributed to the Business/Technical Owner for each system, as listed in the [Tech Stack](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml) or Merge Request related to adding the system to the Tech Stack. Launch a new BIA Questionnaire from GitLab's GRC Application, ZenGRC, by following these steps:
      1. Click 'System of Record' > 'Projects' > 'Business Impact Analysis - New Systems' Project (Select [correct Fiscal Year](https://gitlab.zengrc.com/sor/info/Project/106/info))
      1. Click the 3 dots on the top right-hand corner > 'Send New Questionnaire'
      1. Search for and select the 'Business Impact Analysis (BIA)' questionnaire template
      1. Populate the Recipient Details section. The Recipient is "Internal" (input name/GitLab email of one Business/Technical Owner only).
      1. Search for and select the 'BIA Questionnaire (New System)' email template
      1. Update the Title/Subject, Greeting, Message body, CC and Reply-To @securityrisk@gitlab.com, and Due Date accordingly.  Target completion of the BIA Questionnaire is two weeks.
      1. Click 'Review' > 'Submit' when ready
      1. Map the appropriate System Object to the BIA Questionnaire by clicking the pencil icon in the 'map:system' column.

##### Escalation Path

Security Risk should use discretion when actioning these steps (e.g. consider progress made in completing Tech Stack MR/BIA Questionnaire). Most tech stack / BIA issues are due two weeks from creation.

1. Due Date +1 Business Day: Notify Business/Technical Owner or Delegate in a public Slack channel (e.g. #sec-assurance).
1. Due Date +5 Business Days: Notify Manager of Business/Technical Owner or Delegate in a public Slack channel (e.g. #sec-assurance).
1. Due Date +10 Business Days: Notify SecRisk Manager and consider issuing Risk Acceptance by following the [TPRM Risk Acceptance Process]({{< ref "third-party-risk-management#tprm-risk-acceptance-process" >}}).

### Existing Systems (Frequency based on Critical System Tier)

A BIA is performed or existing BIA data are validated once per fiscal year for each Tier 1 system listed on GitLab's [Tech Stack](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml). BIA data for Tier 2 and 3 systems will be refreshed or validated every 2 years. BIA data for existing Tier 4 systems will not be periodically refreshed or validated due to the low risk they represent to GitLab. In addition to BIA data/response validation, additional questions may be incorporated for the Business/Technical Owner to answer (e.g., questions regarding Technical Debt). The Security Risk Team is responsible for the periodic review and reconciliation of systems which require a BIA year over year. System BIAs will be performed in waves and prioritized by Tier and regulatory need.

### Quality Reviews

The Security Risk team will review the responses to the BIA questionnaires to support completeness and accuracy of the information based on the TPRM assessment performed for the system.

For blank/unknown/obscure responses, engage the Business/Technical Owner via comment functionality within the GRC system, Slack, or a GitLab issue.

### Responses that may result in Tier 3 Observations/Risks

We include some questions in our questionnaire that may lead to the creation of [Tier 3 Observations]({{< ref "observation-management-procedure#scope" >}}). The Security Risk team will review BIA questionnaire responses to identify potential risks to GitLab. Responses that may result in Tier 3 Observations are listed below:

- `Shared Administrative Accounts` = Yes
- `System Specific Recovery Plans` = Insufficient detail in response
- `Authentication Mechanism` ≠ Okta
- `Number of Administrators of the system` < 2

The Security Risk team will follow the observation intake and management process described [here](https://gitlab.com/gitlab-com/gl-security/security-assurance/observation-management/-/blob/master/runbooks/1_Observation%20Intake%20and%20Management.md) for ad-hoc observations.

## Reporting

BIA results are reported via updates to GitLab's Tech Stack. Specific fields like `critical_systems_tier` and `collected_data` are updated accordingly at a system-level should the information from the BIA lead to changes.

## Exceptions

System Proof of Concepts (POC), Proof of Values (POV), and Pilots are exempt from BIA procedures. In the event Tier 1, Tier 2, or Tier 3 systems are added by actors other than Security Risk, these systems will be reviewed as part of the next periodic BIA.

## References

- [Critical System Tiering Methodology]({{< ref "critical-systems" >}})
- [Data Classification Standard]({{< ref "data-classification-standard" >}})
- [Business Continuity Plan](https://about.gitlab.com/handbook/business-technology/gitlab-business-continuity-plan/)
