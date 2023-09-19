---
title: "Security Assurance"
---

<link rel="stylesheet" type="text/css" href="/stylesheets/biztech.css" />

## Overview

As a member of the [Security department]({{< ref "../_index.md#assure-the-customer" >}}), the Security Assurance sub-department provides GitLab customers with a high level of assurance around the security of GitLab SaaS service offerings.

There are five teams in the Security Assurance sub-department.

## <i id="biz-tech-icons" class="fas fa-tasks"></i> Security Assurance Sub-Department

<table id="core-competencies">
  <tr>
    <th class="text-center">
        <i class="fas fa-hands-helping i-bt"></i>
        <h5>Governance & Field Security</h5>
    </th>
    <th class="text-center">
        <i class="fas fa-bullseye i-bt"></i>
        <h5>Security Compliance</h5>
    </th>
    <th class="text-center">
        <i class="fas fa-shield-alt i-bt"></i>
        <h5>Security Risk</h5>
    </th>
  </tr>
  <tr>
      <td>
        <ul>
            <li><a href="{{< ref "governance" >}}"> Governance Team Page </a></li>
            <li><a href="{{< ref "field-security" >}}"> Field Security Team Page </a></li>
        </ul>
      </td>
      <td>
        <ul>
            <li><a href="{{< ref "security-compliance" >}}"> Security Compliance, Commercial Team Page </a></li>
            <li><a href="{{< ref "dedicated-compliance" >}}"> Security Compliance, Dedicated Team Page </a></li>
        </ul>
      </td>
      <td>
        <ul>
            <li><a href="{{< ref "security-risk" >}}"> Security Risk Team Page </a></li>
        </ul>
      </td>
  </tr>
</table>

## <i class="fab fa-gitlab fa-fw" style="color:rgb(107,79,187); font-size:.85em" aria-hidden="true"></i> Core Competencies of Security Assurance Teams

### Field Security Core Competencies

- [Sales Training (Security)](https://about.gitlab.com/handbook/sales/onboarding/sqs-learning-objectives/)
- [Sales Enablement (Security)]({{< ref "field-security-rfp" >}})
- [Customer Assurance (Security)]({{< ref "customer-security-assessment-process" >}})
- [Security Evangelization]({{< ref "evangelism" >}})

### Security Governance Core Competencies

- [Security Policies, Standards and Control maintenance]({{< ref "controlled-document-procedure" >}})
- [Security Assurance Metrics]({{< ref "governance#security-assurance-metrics" >}})
- [Regulatory Landscape Monitoring]({{< ref "governance#regulatory-and-compliance-landscape-monitoring" >}})
- [Security Awareness and Training]({{< ref "sec-awareness-training" >}})
- [Security Assurance Application Administration]({{< ref "security-assurance#core-tools-and-systems" >}})
- [Security Assurance Automation]({{< ref "security-assurance-automation" >}})

### Security Risk Core Competencies

- [Security Third Party Risk Management]({{< ref "third-party-risk-management" >}})
- [Tier 2 Operational Security Risk Management]({{< ref "storm-program" >}})
- [Business Impact Assessments]({{< ref "business-impact-analysis" >}})
- [Critical System Tiering]({{< ref "critical-systems" >}})

### Security Compliance, Commercial Core Competencies

- [GitLab.com Production Continuous Control Monitoring/Auditing]({{< ref "sec-controls" >}})
- [GitLab.com Security Certifications]({{< ref "../security-assurance/security-compliance/certifications" >}})
- [GitLab.com Production & SOX ITGC User Access Reviews]({{< ref "access-reviews" >}})
- [Tier 3 Observation Management]({{< ref "observation-management-procedure" >}})
- [GitLab.com Production Readiness: Compliance Assessment]({{< ref "production-readiness-compliance-assessment" >}})

### Security Compliance, Dedicated Core Competencies

- [GitLab Dedicated Production Continuous Control Monitoring/Auditing](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/)
- [GitLab Dedicated Security Certifcations]({{< ref "../security-assurance/dedicated-compliance/certifications" >}})
- [GitLab Dedicated User Access Reviews]({{< ref "access-reviews" >}})
- [Tier 3 Observation Management]({{< ref "observation-management-procedure" >}})
- [GitLab Dedicated Production Readiness: Compliance Assessment]({{< ref "production-readiness-compliance-assessment" >}})

## <i id="biz-tech-icons" class="far fa-newspaper"></i> Core Tools and Systems

The Security Assurance sub department utilizes a variety of tools to carry out day to day activities. The system admin is responsible for the following:

- Configuration changes
- Onboarding/offboarding/transfers (ie Access)
- Upgrades/patching/incidents
- Migrations to new environments
- Restores from backup
- Admin level audit evidence
- Quality oversight (limited scope)

All other actions are the responsibility of the assigned DRI.

| System Name | System Description | Admin | DRI |
|---------|-------------|---------------|---------|
| [ZenGRC](https://about.gitlab.com/handbook/business-technology/tech-stack/#zengrc) | Key system utilized for initiating, tracking/documenting, and completing Governance, Risk, and Compliance related activities. Access is provided as a standard [baseline entitlement for all team members](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/access-requests/baseline-entitlements/#baseline-entitlements-all-gitlab-team-members). Refer to the [ZenGRC FAQ](/handbook/security/security-assurance/zg-faq.html) and [ZenGRC Activities](/handbook/security/security-assurance/zg-activities.html) handbook pages for additional information. | [Donovan Felton](https://gitlab.com/dfelton) | Security Compliance - [Madeline Lake](https://gitlab.com/madlake)<br>Security Risk - [Ty Dilbeck](https://gitlab.com/tdilbeck) |
| [Authomize](https://www.authomize.com/) | Key system utilized by Security Compliance for [User Access Reviews]({{< ref "security-compliance/access-reviews" >}}) | [Donovan Felton](https://gitlab.com/dfelton) | [Alex Frank](https://gitlab.com/alexfrank09) |
| [OneTrust Vendorpedia QRA](https://about.gitlab.com/handbook/business-technology/tech-stack/#onetrust) | Key system utilized for Privacy, Security, and Data Governance for completing customer questionnaires | [Donovan Felton](https://gitlab.com/dfelton) | [Marie-Claire Cerny](https://gitlab.com/marieclairecerny) |
| [OneTrust Vendorpedia Exchange](https://about.gitlab.com/handbook/business-technology/tech-stack/#onetrust) | System utilized for Privacy, Security, and Data Governance for TPRM | [Donovan Felton](https://gitlab.com/dfelton) | [Ty Dilbeck](https://gitlab.com/tdilbeck) |
| [ProofPoint](https://about.gitlab.com/handbook/business-technology/tech-stack/#proofpoint) | Key system utilized for the creation and distribution of our security training and phishing simulations to provide ongoing testing for adherence of various compliance frameworks. | [Donovan Felton](https://gitlab.com/dfelton) | [Joe Longo](https://gitlab.com/jlongo_gitlab) |
| [BitSight](/handbook/security/security-assurance/field-security/independent_security_assurance.html) | Independent Security Rating Platform configured to monitor GitLab's security, identify potential vulnerabilities, and benchmark our security against our competitors. Additionally, BitSight is used to assess and monitor software vendors as part of our Security Third Party Risk Management Program. | [Donovan Felton](https://gitlab.com/dfelton) | [Jeff Burrows](https://gitlab.com/jburrows001) |
| [GitLab](https://about.gitlab.com/handbook/business-technology/tech-stack/#gitlab) - Security Assurance Projects | Primarily used to engage stakeholders via issues, updates to Security Assurance related handbook pages, etc. | Security Assurance Senior Director | Each Team is responsible for their Projects, but everyone can contribute |

## <i id="biz-tech-icons" class="fas fa-users"></i>Contacting the Team

- Join our slack channel: #sec-assurance
- Email: <security-assurance@gitlab.com>

### Team READMEs

- [Byron's README](/handbook/security/readmes/byron-boots/)

## <i class="fas fa-book" style="color:rgb(110,73,203)" aria-hidden="true"></i> References

Check out these great security resources built with our customers in mind:

- GitLab's [Customer Assurance Package](https://about.gitlab.com/security/cap/)
- GitLab's [Security - Trust Center](https://about.gitlab.com/security/)
- GitLab's [Security Team Page]({{< ref "../_index.md" >}})
