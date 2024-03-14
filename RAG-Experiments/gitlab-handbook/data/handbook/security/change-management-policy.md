---
title: "Change Management Policy"
---

{{% alert title="This is a Controlled Document" color="danger" %}}
Inline with GitLab's regulatory obligations, changes to [controlled documents]({{< ref "controlled-document-procedure" >}}) must be approved or merged by a code owner. All contributions are welcome and encouraged.
{{% /alert %}}

## Purpose

The purpose of the Change Management Policy is to ensure that a standard set of minimum requirements are established for changes that are made to production systems and supporting infrastructure across the organization.

These requirements are meant to provide a level of consistency across how changes are managed from the initial change request through to production deployment. These requirements have been established based on the GitLab Control Framework which is based on NIST SP 800-53, ISO 27001 and SOC 2 standards.

## Scope

Changes, in the context of this policy, are defined as **modifications** to the production environment and include supporting infrastructure and key corporate systems. The policy applies to changes that are made to systems assigned a [Critical System Tier]({{< ref "critical-systems" >}}) of `Tier 1 Mission Critical`, `Tier 2 Business Critical`, and `Tier 3 Business Operational`.

**Modifications** include, but are not limited to:
- Creation/development/implementation of new systems, integrations, features, key reports, databases, etc.
- Changes to configurations
- Deployment of patches or vendor supplied changes not managed by the vendor
- Modifications to data schemas
- System deprecation
- New access or role creation
- Broadly speaking, any change that will impact how team members carry out their responsibilities

{{% note %}}
While Tier 4 Administrative systems are not subject to the scope of this policy, team members are encouraged to proactively adopt the requirements established by this policy across all systems, especially if there is a good probability that a system may move from a `Tier 4 Administrative` system to a [higher system tier]({{< ref "critical-systems" >}}) handbook page.
{{% /note %}}

### Applicable Change Management Procedures:

In conjunction with this policy, supplemental change management procedures are formally documented to describe the standard operating procedure/workflow for executing changes in accordance with this policy and the [Controlled Document Procedure]({{< ref "controlled-document-procedure" >}}). GitLab's current change management procedures are listed below for reference, including a brief statement on the applicable scope for each change procedure. Additional information on scope is provided directly on each respective procedure's handbook page:

- [Infrastructure Change Management Procedure](https://about.gitlab.com/handbook/engineering/infrastructure/change-management/), for changes made to environments and cloud infrastructure services directly supporting the `GitLab.com SaaS product`
- [Business Technology Change Management Procedure](https://about.gitlab.com/handbook/business-technology/change-management/), for changes made to production systems/tools/infrastructure that `do not` directly support the `GitLab.com SaaS product`
- [Organizational Change Management Procedure](https://about.gitlab.com/handbook/organizational-change-management/), for organization-wide impacting changes, such as significant team restructures, revisions to hot button policies, etc.
- [Security Change Management Procedure]({{< ref "security-change-management-procedure" >}}) for changes made to systems and applications owned by Security and processes owned by Security sub-departments.

## Roles & Responsibilities

|Role|Responsibility|
|----------|---------------|
|Security Compliance Team|Responsible for the continuous monitoring of change management procedures across the relevant systems through security control testing to ascertain adherence to this policy|
|Technical System Owners<br><br>Business System Owners<br><br>System Administrators|Responsible for ensuring the minimum requirements established by this policy are implemented in procedure and executed consistently|
|Team Members|Responsible for following change management procedures in a way that aligns with this policy|
|Control Owners|Responsible for defining and implementing change management procedures that meet or exceed the minimum requirements that have been established by this policy|

## Change Management Policy

The minimum change management requirements described below have been identified based on change management controls established by the [GitLab Control Framework (GCF)]({{< ref "sec-controls#gitlab-control-framework-gcf" >}}). These controls are subject to internal and external audits and therefore provide the minimum requirements for change management across the organization.

### Change Management Policy Guidance

Supplemental change management procedures must incorporate the requirements called out in the sections below:
   - [Change Request Documentation Requirements](#change-request-documentation-requirements)
   - [Change Testing Requirements](#change-testing-requirements)
   - [Change Review and Approval Requirements](#change-review-and-approval-requirements)
   - [Change Deployment Requirements](#change-deployment-requirements)

#### Change Request Documentation Requirements

- Details on why the change is being requested
- Information about the Impact of the Change (e.g. does the change impact team members? and if so, in what capacity?)
- Testing procedures, including the [change testing requirements](#change-testing-requirements) documented below
- Change type, if applicable (e.g. teams may opt to have different procedures for emergency changes, standard changes, configuration changes, etc.) or use a singular procedure for all changes, regardless of the type of change.
- Change rollback/backout procedures in the event a deployed change does not function as intended
- Specific requirements for peer review(s), approvals, and post-deployment verification, as applicable (e.g requirements may be based on change type)
- Change Communication: who are the relevant stakeholders that need to be notified of the change (e.g. if the change impacts all team members, how will team members be notified?)

#### Change Testing Requirements

- Where possible, changes are tested in a non-production environment. The exception to this requirement would be changes to systems in which GitLab does not have a environment separate from production. Team members are required to leverage test accounts/test data where feasible if testing must be conducted in a production system due to lack of availability of a non-production environment.
- Documented testing requirements / test plans, which consider the following, as applicable:
   - security testing (e.g. if there is sensitive data involved)
   - manual testing / reconciliations (e.g. new finance report created to support month end activities - testing should include verifying calculated totals are complete and accurate and intended account data is included)
   - configurations changes are tested to confirm they function as intended
   - any additional testing procedures applicable based on the nature of the change
- Testing is documented and includes the team members who performed the testing. The results and evidence of testing is attached/linked back to the change request

#### Change Review and Approval Requirements

- Once developed and tested, a change is formally reviewed and approved. Review(s) and approval(s) meet the following requirements:
   - Reviewer(s) and approver(s) must be different than the team members who worked on/developed the change
   - Reviewer(s) and approver(s) must not make changes to the change that do not go through additional approval/review by another individual
   - Where technically feasible, tools or systems utilized to develop, test, and approve changes should be configured in a way that prohibits unauthorized changes to be made without the appropriate approval(s). Subsequently, configurations should also restrict the ability for team members who developed and/or tested a change from being able to approve their change.
- Reviewer(s) and Approver(s), alongside dates of review and approval, are documented on the change request to ensure auditability

#### Change Deployment Requirements

- Where possible, changes are deployed by a different team member than the team member(s) who developed the change. If this is not possible, team members must confirm that additional changes/development work does not take place after the change has been approved. If additional work is completed after a change has been approved for deployment, additional review(s) and approval(s) should be obtained prior to the change being deployed.
- Date of deployment is documented on the change request to ensure auditability
- Where possible, post-deployment verifications are completed and comments/documentation are linked to the change request (e.g. change is successful and functioning as anticipated in production)

#### Additional Guidance

1. Change requests can be tied back to a specific change or changes from the system (e.g. as part of external audits, an auditor will ask for a population of changes from the SYSTEM itself instead of the change request repository. A sample of changes will be requested from this population and for each change, the related change request/change documentation will need to be provided)
1. Where it is not technically feasible for systems to be configured in a way that restricts the ability for those involved with the development of a change from being able to deploy a change, team members should consider some sort of periodic review of changes. The review should ensure that changes are not being deployed by an individual without a separate and appropriate individual's approval (or identify an alternative mechanism or process to monitor for this)
1. Some minimum requirements may not be applicable based on the type of change (e.g. emergency changes typically don't require approvals prior to deployment due to the need to deploy emergency changes quickly). Change procedures should clearly document exceptions to the minimum requirements in this policy and the mechanisms in place to meet the requirements of this policy (e.g. for emergency changes, a post-deployment verification is performed and retroactive approvals are obtained and documented on the emergency change request within a specified period of time)

{{% alert title="When in doubt, consult with Security Assurance" color="warning" %}}
Team members who have questions about the minimum requirements in this policy or the appropriateness of change procedures that they maintain should consult with the [Security Assurance Team]({{< ref "security-assurance" >}}) as needed.
{{% /alert %}}

## Exceptions

Exceptions to this policy will be tracked as per the [Information Security Policy Exception Management Process]({{< ref "_index.md#information-security-policy-exception-management-process" >}}). Procedure exceptions will be tracked by the procedure owner and must be approved by management.

## References

- [Controlled Document Procedure]({{< ref "controlled-document-procedure" >}})
- [Critical System Tiers]({{< ref "critical-systems" >}})
- [GitLab Control Framework (GCF)]({{< ref "sec-controls#gitlab-control-framework-gcf" >}})
- [Information Security Policy Exception Management Process]({{< ref "_index.md#information-security-policy-exception-management-process" >}})
