---
title: "GitLab Security Compliance Controls"
---

Security controls are a way to state our company's position on a variety of security topics. It's not enough to simply say "We encrypt data" since our customers and teams will naturally want to know "what data do we encrypt?" and "how do we encrypt that data?". When all of our established security controls are operating effectively this creates a security program greater than the sum of its parts. It demonstrates to our stakeholders that GitLab has a mature and comprehensive security program that will provide assurance that data within GitLab is reasonably protected.

## GitLab Control Framework (GCF)

We have tried to take a comprehensive approach to our immediate and future security compliance needs. Older and larger companies tend to treat each security compliance requirement individually which results in independent security compliance teams going out to internal teams with multiple overlapping requests. For example, at such a company you might have one database engineer that is asked to provide evidence of how a particular database is encrypted based on SOC2 requirements, then again for ISO requirements, then again for FedRAMP requirements. This approach can be visualized as follows:

```mermaid
graph TD;
    SOC2_Requirement1-->Team1;
    SOC2_Requirement1-->Team2;
    SOC2_Requirement2-->Team1;
    SOC2_Requirement2-->Team2;
    FedRAMP_Requirement1-->Team1;
    ISO_Requirement1-->Team2;
```

Given our [efficiency value]({{< ref "values#efficiency" >}}) here at GitLab we wanted to create a set of security controls that would address multiple underlying requirements with a single security control which would allow us to make fewer requests of our internal teams and efficiently collect all evidence we would need for a variety of audits at once. This approach can be visualized as follows:

```mermaid
graph TD;
    SOC2_Requirement1-->GCF;
    SOC2_Requirement2-->GCF;
    FedRAMP_Requirement1-->GCF;
    ISO_Requirement1-->GCF;
    GCF-->Team1;
    GCF-->Team2;
```

As our security compliance goals and requirements have evolved so have our requirements and constraints related to our security control framework. Our GCF is currently based on NIST SP 800-53.

## Security Control Lifecycle

The lifecycle of our security controls can be found at [this handbook page]({{< ref "security-control-lifecycle" >}}). As part of the security control lifecycle, all GCF security controls are reviewed and tested at a minimum on an annual basis or as required by regulation.

GCF security controls are assessed at the entity level or the system level depending upon the nature of the control.

GCF security controls assessed at system level are based upon the system's [critical system tiering]({{< ref "critical-systems" >}}). Dependent upon the system's tier, a subset of GCF controls are evaluated based upon overall risk and impact to the organization. This is broken out as follows:


|Tier |     GCF Control Scope |     ZenGRC Link|
|--|--|--|
|Tier 0 Entity|Entity-Level Controls| [Link](https://gitlab.zengrc.com/sor/listing/controls?p=eyJzb3IiOnsicGFnZVNpemUiOjIwMCwiY29sdW1ucyI6WyJ0aXRsZSIsInNsdWciLCJkZXNjcmlwdGlvbiIsInRlc3RQbGFuIiwic3RhdHVzIiwiY2FfXzExMiIsImFzc2Vzc21lbnRzIl0sImNvbHVtblNpemVzIjpbeyJuYW1lIjoidGVzdFBsYW4iLCJzaXplIjozNzR9LHsibmFtZSI6Im1hcHBpbmdzLnByb2dyYW1zIiwic2l6ZSI6MzgxfV0sImZpbHRlcnMiOnsiQU5EIjpbeyJmIjoiY2FfXzM0MyIsIm8iOiI9IiwidiI6IlRpZXIgMCBFbnRpdHkifSx7ImYiOiJtYXBwaW5ncy5wcm9ncmFtcyIsIm8iOiI9IiwidiI6IlByb2dyYW06NDIifV19fX0%3D&page=1)|
|Tier 1 Mission Critical|All "In-Scope" System-Level Controls| [Link](https://gitlab.zengrc.com/sor/listing/controls?p=eyJzb3IiOnsicGFnZVNpemUiOjIwMCwiY29sdW1ucyI6WyJ0aXRsZSIsInNsdWciLCJkZXNjcmlwdGlvbiIsInRlc3RQbGFuIiwic3RhdHVzIiwiY2FfXzExMiIsImFzc2Vzc21lbnRzIl0sImNvbHVtblNpemVzIjpbeyJuYW1lIjoidGVzdFBsYW4iLCJzaXplIjozNzR9LHsibmFtZSI6Im1hcHBpbmdzLnByb2dyYW1zIiwic2l6ZSI6MzgxfV0sImZpbHRlcnMiOnsiQU5EIjpbeyJPUiI6W3siZiI6ImNhX18zNDMiLCJvIjoiPSIsInYiOiJUaWVyIDEgTWlzc2lvbiBDcml0aWNhbCJ9LHsiZiI6ImNhX18zNDMiLCJvIjoiPSIsInYiOiJUaWVyIDIgQnVzaW5lc3MgQ3JpdGljYWwifV19LHsiZiI6Im1hcHBpbmdzLnByb2dyYW1zIiwibyI6Ij0iLCJ2IjoiUHJvZ3JhbTo0MiJ9XX19fQ%3D%3D&page=1)|
|Tier 2 Business Critical|Subset of System-Level Controls| [Link](https://gitlab.zengrc.com/sor/listing/controls?p=eyJzb3IiOnsicGFnZVNpemUiOjIwMCwiY29sdW1ucyI6WyJ0aXRsZSIsInNsdWciLCJkZXNjcmlwdGlvbiIsInRlc3RQbGFuIiwic3RhdHVzIiwiY2FfXzExMiIsImFzc2Vzc21lbnRzIl0sImNvbHVtblNpemVzIjpbeyJuYW1lIjoidGVzdFBsYW4iLCJzaXplIjozNzR9LHsibmFtZSI6Im1hcHBpbmdzLnByb2dyYW1zIiwic2l6ZSI6MzgxfV0sImZpbHRlcnMiOnsiQU5EIjpbeyJmIjoiY2FfXzM0MyIsIm8iOiI9IiwidiI6IlRpZXIgMiBCdXNpbmVzcyBDcml0aWNhbCJ9LHsiZiI6Im1hcHBpbmdzLnByb2dyYW1zIiwibyI6Ij0iLCJ2IjoiUHJvZ3JhbTo0MiJ9XX19fQ%3D%3D&page=1)|

> Note that to arrive at all controls that are Tier 1 you must filter for all controls with Tier 1 OR Tier 2 designation (since all Tier 2 controls also are included in Tier 1). The filters above have accounted for this nuance and can be confirmed by selecting "Filter" in the top right of ZenGRC and confirming filters being applied.

## Control Ownership

Control Owner - Ensures that the design of the control and the control activities operate effectively and is responsible for remediation of any control activities that are required to bring that control into a state of audit-readiness.

Process Owner - Supports the operation of the control and carries out the process designed by the control owner. The process owner is most likely to be interviewed by an auditor to determine whether or not the process is operating as intended.

## Security Control Changes

The GitLab Security Compliance team is responsible for ensuring the consistency of the documentation of the security controls listed below. While normally we welcome any GitLab team member to make edits to handbook pages, please be aware that even small changes to the wording of any of these controls impacts how they satisfy the requirements for the security frameworks they map to. Because of this, we ask any changes that need to be made to this page and the underlying guidance pages to start with a message in the [#sec-assurance](https://slack.com/app_redirect?channel=sec-assurance) slack channel. The compliance team will then engage with you and make any appropriate changes to these handbook pages.

## GitLab IT General Controls (ITGCs)

ITGCs are a subset of the GCF controls. Please refer to [GitLab SOX ITGC Compliance](https://internal.gitlab.com/handbook/finance/sox-internal-controls/) (internal only) for details.

## Security System Intake

To assess newly acquired/developed systems that enable security controls OR are/may be in scope for compliance programs for potential inclusion into our [GitLab Control Framework (GCF)]({{< ref "sec-controls#gitlab-control-framework-gcf" >}}) and compliance programs  (e.g., [Security Compliance Program]({{< ref "../security-compliance#-core-competencies" >}}) and [SOX Program](https://about.gitlab.com/handbook/internal-audit/sarbanes-oxley/)).

### 1. System identification

Our goal is to identify systems that enable security controls (e.g., access management system) OR systems that are (or may be) subject to regulatory (e.g., SOX) or compliance requirements (SOC2) as early as possible via our [Third Party Risk Management (TPRM) Program]({{< ref "third-party-risk-management" >}}). As we engage with third parties for new systems, we assess the use of the system and whether or not it meets the criteria described above. Existing systems can also be ingested into the Security Compliance Intake process. Examples of these could include systems whose functionality has expanded to support security controls or instances where our understanding of a security control has improved resulting in the identification of a previously uncredited supporting system.

If the system meets the criteria, we open up a new [Security Compliance Intake Issue](https://gitlab.com/gitlab-com/gl-security/security-assurance/security-compliance-commercial-and-dedicated/security-compliance-intake/-/issues/new?issue[title]=System%20Intake:%20%5BSystem%20Name%20FY2%23%20Q%23%5D&issuable_template=intakeform).

### 2. Creating Security Compliance Intake Issue

[Security Compliance Intake Issue](https://gitlab.com/gitlab-com/gl-security/security-assurance/security-compliance-commercial-and-dedicated/security-compliance-intake/-/issues/new?issue[title]=System%20Intake:%20%5BSystem%20Name%20FY2%23%20Q%23%5D&issuable_template=intakeform) asks the author to include details related to the system including:

- System overview
- Implemented security controls or impacted regulatory or compliance program
- Link to TPRM review and results
- Link to most recent [Business Impact Analysis]({{< ref "business-impact-analysis" >}}) and [Critical System Tier]({{< ref "critical-systems#critical-systems-tiering-methodolgy" >}}) (CST)
- Control owner details
- Deployment model and implementation status
- Data classification
- Regulatory scope (supported by Security Compliance and [Internal Audit](https://about.gitlab.com/handbook/internal-audit/))
The author of the issue completes as much of the issue as they can and assigns it to the Security Risk team for completion/triage (if the issue is not originally created by the Security Risk team).

### 3. Security Compliance workflow

Once the Security Compliance Intake issue is populated, Security Risk assigns the issue to the Security Compliance team to complete the following tasks to incorporate the system into our Security Compliance Program:

- Notify stakeholders and system owners of upcoming testing requirements
- Incorporate testing requirements (driven by CST and regulatory/compliance requirements) and recommendations into the fiscal year audit schedule
- Determine when [user access reviews]({{< ref "access-reviews" >}}) for the new system need to start and communicate to compliance teams

## List of NIST 800-53 controls by family (Used by Commercial and Dedicated teams beginning FY24 Q1)

*Detailed sub-controls are included in the various control family pages*

For full control descriptions where they have yet to be completed OR where full details of the control are required, please visit the corresponding control page on the [official NIST page](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home)

Note: In some instances, GitLab has created custom controls for the GCF which expand upon the NIST framework. GitLab has applied the NIST naming convention to these controls for ease of control family grouping. If you cannot find corresponding NIST control guidance for a GCF control on the [official NIST page](https://csrc.nist.gov/projects/cprt/catalog#/cprt/framework/version/SP_800_53_5_1_0/home), it's likely a custom control. Please reach out to #sec-assurance in Slack for any questions regarding any controls.

{{% details summary="Access Control (AC)" %}}

> [<i class="fa-solid fa-file-lines"></i> Access Control (AC)]({{< ref "../security-compliance" >}})

 This control family contains controls that cover access to systems, networks, and devices. Controls provide guidance on the implementation of access policies, account management, and topics like user privileges; aiming to lower the risk of unapproved access to a range of systems, devices, or networks.

| Control | Title | Description |
|---------|-------------|---------------|
|     AC-1     |     Policy and Procedures          |     Develop, document, and disseminate an access control policy and procedures that address the controls in the Access Control (AC) family implemented within GitLab Inc. and its associcated in-scope systems.     |
|     AC-2     |     Account Management v2          |     Develop and document processes for defining, authorizing, monitoring, and modifying user access to GitLab's systems.     |
|     AC-2(3)     |     Account Management - Disable Accounts v2          |     To be completed.     |
|     AC-3     |     Access Enforcement          |     Enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.     |
|     AC-3(7)     |     Access Enforcement - Role-based Access Control          |     To be completed.     |
|     AC-4     |     Information Flow Enforcement          |     Enforce approved authorizations for controlling the flow of information within and between GitLab's systems.     |
|     AC-6(5)     |     Least Privilege - Privileged Accounts          |     Restrict privileged access to appropriate individuals while adhering to the principle of least privilege when determining who receives privileged access.     |
|     AC-6(7)     |     Least Privilege - Review of User Privileges v2          |     Perform an access review of all account privileges to ensure principle of least privilege is adhered to for all accounts.     |
|     AC-7(2)     |     Unsuccessful Logon Attempts - Purge or Wipe Mobile Device          |     To be completed.     |
|     AC-17     |     Remote Access v2          |     Establish requirements and authorization controls before allowing remote access connections to GitLab's systems.     |
|     AC-17(2)     |     Remote Access - Protection of Confidentiality and Integrity Using Encryption          |     To be completed.     |
|     AC-18     |     Wireless Access          |     Establish requirements and authorization controls before allowing wireless network connections to GitLab's systems.     |
|     AC-18(1)     |     Wireless Access - Authentication and Encryption          |     To be completed.     |
|     AC-19     |     Access Control for Mobile Devices          |     Establish requirements and authorization controls before allowing mobile device connections to GitLab's systems.     |
|     AC-19(5)     |     Access Control for Mobile Devices - Full Device or Container-based Encryption          |     To be completed.     |
|     AC-21     |     Information Sharing          |     Develop, document, and disseminate information classification and sharing guidance for users.     |
|     AC-22     |     Publicly Accessible Content          |     Implement a process to remove nonpublic information and to review and approve content prior to opening such content to the public.     |
{{% /details %}}

{{% details summary="Awareness & Training (AT)" %}}
> [<i class="fa-solid fa-file-lines"></i> Awareness & Training (AT)](https://about.gitlab.com/handbook/security/security-assurance/security-compliance/)

This control family helps to ensure users of information systems are adequately trained to identify threats. A particular focus is improving awareness of different operational risks and threats to privacy or system security. Requirements around the creation of training policy, records, and feedback helps to fine-tune the organization’s approach to cybersecurity training.

| Control | Title | Description |
|---------|-------------|---------------|
|     AT-1     |     Policy and Procedures          |     Develop, document, and disseminate a training policy and procedures that address the controls in the Awareness and Training (AT) family implemented within GitLab Inc.     |
|     AT-2     |     Literacy Training and Awareness          |     Provide security and privacy literacy training to team members and incorporate lessons learned from internal or external security incidents or breaches.     |
|     AT-2(2)     |     Literacy Training and Awareness - Insider Threat          |     To be completed.     |
|     AT-3     |     Role-based Training          |     Provide role-based security and privacy training to appropriate team members and incorporate lessons learned from internal or external security incidents or breaches where appropriate.     |
|     AT-4     |     Training Records          |     Document and monitor security and privacy training activities and retain associated training records.     |
{{% /details %}}

{{% details summary="Audit and Accountability (AU)" %}}
> [<i class="fa-solid fa-file-lines"></i> Audit and Accountability (AU)]({{< ref "../security-compliance" >}})

This control family provides guidance on procedures for event logging and auditing. Controls cover the baseline content of audit records, the capacity of log storage, and the process for monitoring and reviewing logs. Log audits are an important part of identifying the cause of breaches or system issues, and are a tool for accountability.

| Control | Title | Description |
|---------|-------------|---------------|
|     AU-1     |     Policy and Procedures          |     Establishment of audit and accountability policy and procedures that address the controls in the AU family implemented within systems and organizations.     |
|     AU-2     |     Event Logging v2          |     Identify events for logging that are relevant to the security of systems and the privacy of individuals and implement a program to support GitLab's event logging requirements.     |
|     AU-3     |     Content of Audit Records v2          |     Audit record content that may be necessary to support the auditing function of event outcomes including indicators of event success or failure and event-specific results, such as system security and privacy posture after the even occurred.     |
|     AU-6(4)     |     Audit Record Review, Analysis, and Reporting - Central Review and Analysis          |     To be completed.     |
|     AU-6(5)     |     Audit Record Review, Analysis, and Reporting - Integrated Analysis of Audit Records          |     To be completed.     |
|     AU-11     |     Audit Record Retention v2          |     Retaining audit records for organization-defined time period consistent with records retention policy to provide support for after-the-fact investigations of incidents and to meet regulatory and organizational information retention requirements.     |
{{% /details %}}

{{% details summary="Assessment, Authorization, and Monitoring (CA)" %}}
> [<i class="fa-solid fa-file-lines"></i> Assessment, Authorization, and Monitoring (CA)]({{< ref "../security-compliance" >}})

This control family focuses on the continuous monitoring and improvement of security and privacy controls. It covers the creation of an assessment plan and the delegation of the team to carry out control assessment. Controls also cover the creation of a plan of action and milestones (POAM), an integral document for identifying and fixing vulnerabilities or weaknesses.

| Control | Title | Description |
|---------|-------------|---------------|
|     CA-1     |     Policy and Procedures          |     Establishment of assessment, authorization, and monitoring policy and procedures that address the controls in the CA family implemented within systems and organizations.     |
|     CA-2     |     Control Assessments          |     Selection of assessors with the required skills and technical expertise to develop effective assessment plans to determine the accuracy and completeness of whether the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting requirements.     |
|     CA-2(1)     |     Control Assessments - Independent Assessors          |     To be completed.     |
|     CA-2(2)     |     Control Assessments - Specialized Assessments          |     To be completed.     |
|     CA-2(3)     |     Control Assessments - Leveraging Results from External Organizations          |     To be completed.     |
|     CA-3     |     Information Exchange          |     System information exchange requirements between two or more systems.     |
|     CA-7     |     Continuous Monitoring          |     Continuous monitoring facilitating ongoing awareness of the system security and privacy posture to support organizational risk management decisions.     |
|     CA-7(1)     |     Continuous Monitoring - Independent Assessment          |     To be completed.     |
|     CA-7(3)     |     Continuous Monitoring - Trend Analyses          |     To be completed.     |
|     CA-8     |     Penetration Testing          |     Specialized testing to identify vulnerabilities that could be exploited by adversaries.     |
|     CA-8(1)     |     Penetration Testing - Independent Penetration Testing Agent or Team          |     To be completed.     |
|     CA-9     |     Internal System Connections          |     Connections between organizational systems and separate constituent system components.     |
{{% /details %}}

{{% details summary="Configuration Management (CM)" %}}
> [<i class="fa-solid fa-file-lines"></i> Configuration Management (CM)]({{< ref "../security-compliance" >}})

This control family focuses on the configuration of software and devices on the network. Controls cover the creation of a configuration policy, the creation of a baseline configuration of the system, and the management of unauthorized configuration or devices. Configuration controls lower the risk of unauthorized hardware or software being installed on the system, or vulnerabilities caused by changes to settings.

| Control | Title | Description |
|---------|-------------|---------------|
|     CM-1     |     Policy and Procedures          |     Establishment of configuration management policy and procedures that address the controls in the CM family implemented within systems and organizations.     |
|     CM-2     |     Baseline Configuration v2          |     Documented, formally reviewed, and agreed-upon specifications for systems or configuration items within those systems.     |
|     CM-3     |     Configuration Change Control v2          |     Systematic proposal, justification, implementation, testing, review, and disposition of system changes, including system upgrades and modifications.     |
|     CM-4     |     Impact Analyses          |     Analysis of changes to determine potential security and privacy impacts prior to change implementation.     |
|     CM-5     |     Access Restrictions for Change v2          |     Physical and logical access restrictions associated with changes to the system only by qualified and authorized individuals for purposes of initiating changes.     |
|     CM-6     |     Configuration Settings v2          |     Parameters that can be changed in the hardware, software, or firmware components that affect the security and privacy posture or functionality of the system.     |
|     CM-6(1)     |     Configuration Settings - Automated Management, Application, and Verification          |     To be completed.     |
|     CM-7(1)     |     Least Functionality - Periodic Review          |     To be completed.     |
|     CM-8     |     System Component Inventory          |     Inventory for effective accountability of system components.     |
|     CM-8(3)     |     System Component Inventory - Automated Unauthorized Component Detection          |     To be completed.     |
|     CM-9     |     Configuration Management Plan v2          |     Established to satisfy the requirements in configuration management policies while being tailored to individual systems defining processes and procedures for how configuration management is used to support system development life cycle activities.     |
|     CM-10     |     Software Usage Restrictions          |     Software license tracking in accordance with contract agreements and copyright laws.     |
|     CM-10(1)     |     Software Usage Restrictions - Open-source Software          |     To be completed.     |
|     CM-11     |     User-installed Software          |     Established policies governing the permitted and prohibited actions regarding software installation by users.     |
|     CM-11(2)     |     User-installed Software - Software Installation with Privileged Status          |     To be completed.     |
{{% /details %}}

{{% details summary="Contingency Planning (CP)" %}}
> [<i class="fa-solid fa-file-lines"></i> Contingency Planning (CP)]({{< ref "../security-compliance" >}})

This control family prepares organizations for system failures and breaches. Controls cover the planning for alternative processing or storage sites and the creation of system backups to help mitigate system downtime. Other controls focus on contingency planning, including training and plan testing. This family of controls is important for mitigating the damage from a system outage or network breach, establishing clear plans to restore normal operation.

| Control | Title | Description |
|---------|-------------|---------------|
|     CP-1     |     Policy and Procedures          |     Establishment of contingency planning policy and procedures that address the controls in the CP family implemented within systems and organizations.     |
|     CP-2     |     Contingency Plan v2          |     Achieving continuity of operations for organizational mission and business functions to address system restoration and implementation of alternative mission or business processes when systems are compromised or breached.     |
|     CP-2(2)     |     Contingency Plan - Capacity Planning          |     To be completed.     |
|     CP-3     |     Contingency Training          |     Assignment of roles and responsibilities of organizational personnel to ensure that the appropriate content and level of detail is included in such training.     |
|     CP-4     |     Contingency Plan Testing v2          |     To determine the effectiveness of the plans and identify potential weaknesses.     |
|     CP-6     |     Alternate Storage Site          |     The maintainence of duplicate copies of information and data and processing capability if the primary storage site is not available.     |
|     CP-7     |     Alternate Processing Site          |     Geographically distinct processing sites providing processing capability if the primary processing site is not available.     |
|     CP-9     |     System Backup v2          |     Mechanisms employeed to protect the integrity of system-level and user-level information.     |
|     CP-9(1)     |     System Backup - Testing for Reliability and Integrity          |     To be completed.     |
|     CP-9(6)     |     System Backup - Redundant Secondary System          |     To be completed.     |
|     CP-10     |     System Recovery and Reconstitution v2          |     The execution of contingency plan activities for recovery and reconstitution of the system to a known state within an organziation-defined time period consist with recovery time and recovery point objectives after a disruption, compromise, or failure.     |
{{% /details %}}

{{% details summary="Identification and Authentication (IA)" %}}
> [<i class="fa-solid fa-file-lines"></i> Identification and Authentication (IA)]({{< ref "../security-compliance" >}})

This control family controls the reliable identification of users and devices. Different controls focus on different elements of safe user or device authentication. Controls strengthen user management policies, lowering the risk of unauthorized access to the system.

| Control | Title | Description |
|---------|-------------|---------------|
|     IA-1     |     Policy and Procedures          |     Establishment of identification and authentication policy and procedures that address the controls in the IA family implemented within systems and organizations.     |
|     IA-2     |     Identification and Authentication (organizational Users)          |     To uniquely identify and authenticate organizational users and associate that unique identification with processes acting on behalf of those users.     |
|     IA-2(1)     |     Identification and Authentication (organizational Users) - Multi-factor Authentication to Privileged Accounts v2          |     To be completed.     |
|     IA-5     |     Authenticator Management v2          |     To manage system authenticators.     |
|     IA-5(1)     |     Authenticator Management - Password-based Authentication          |     To be completed.     |
|     IA-5(6)     |     Authenticator Management - Protection of Authenticators          |     To be completed.     |
{{% /details %}}

{{% details summary="Incident Response (IR)" %}}
> [<i class="fa-solid fa-file-lines"></i> Incident Response (IR)]({{< ref "../security-compliance" >}})

This control family controls all aspects of responding to a serious incident. This includes training and planning for potential incidents, as well as plans for actively monitoring and responding to incidents as they occur. Enhanced controls cover specific types of incidents that distinct organizations might face. Incidents may include data breaches, breakdowns in the supply chain, public relations damage, or malicious code in the system.

| Control | Title | Description |
|---------|-------------|---------------|
|     IR-1     |     Policy and Procedures          |     Establishment of incident response policy and procedures that address the controls in the IR family implemented within systems and organizations.     |
|     IR-2     |     Incident Response Training          |     Training associated with the assigned roles and responsibilities of organizational personnel to ensure that the appropriate content and level of detail are included in such training.     |
|     IR-3     |     Incident Response Testing          |     The testing of incident response capabilities to determine their effectiveness and identify potential weaknesses or deficiencies.     |
|     IR-4     |     Incident Handling          |     To implement incident handling capability for incidents that is consistent with the incident response plan and includes preparation, detection and analysis, containment, eradication, and recovery.     |
|     IR-5     |     Incident Monitoring          |     To track and document incidents.     |
|     IR-6     |     Incident Reporting          |     The requirement for personnel to report suspected incidents.     |
|     IR-8     |     Incident Response Plan v2          |     To develop and implement a coordinated approach for incident response capability.     |
|     IR-9(2)     |     Information Spillage Response - Training          |     To be completed.     |
|     IR-9(3)     |     Information Spillage Response - Post-spill Operations          |     To be completed.     |
|     IR-9(4)     |     Information Spillage Response - Exposure to Unauthorized Personnel          |     To be completed.     |
{{% /details %}}

{{% details summary="Maintenance (MA)" %}}
> [<i class="fa-solid fa-file-lines"></i> Maintenance (MA)]({{< ref "../security-compliance" >}})

This control family deals with all elements of system maintenance, including software updates, logging, and inspection tools. It covers the need for timely maintenance to lower the risk of operational outages, and outlines policy and the management of maintenance personnel.

| Control | Title | Description |
|---------|-------------|---------------|
|     MA-1     |     Policy and Procedures          |     Establishment of maintenance policy and procedures that address the controls in the MA family implemented within systems and organizations.     |
{{% /details %}}

{{% details summary="Media Protection (MP)" %}}
> [<i class="fa-solid fa-file-lines"></i> Media Protection (MP)]({{< ref "../security-compliance" >}})

This control family covers the use, storage and safe destruction of media and files helping to lower the risk of information breaches and leaks.

| Control | Title | Description |
|---------|-------------|---------------|
|     MP-1     |     Policy and Procedures          |     Establishment of media protection policy and procedures that address the controls in the MP family implemented within systems and organizations.     |
|     MP-2     |     Media Access          |     Restrict access to organization-defined types of digital and/or non-digital media to an organization-defined personnel or roles.     |
|     MP-3     |     Media Marking          |     To mark system media indicating the distribution limitations, handling caveats, and applicable security markings (if any) of the information; and exempt organization-defined types of system media from marking if the media remain within organization-defined controlled areas.     |
|     MP-5     |     Media Transport          |     To protect and control organization-defined types of system media during transport outside of controlled areas using organization-defined controls.     |
|     MP-5(3)     |     Media Transport - Custodians          |     To be completed.     |
|     MP-6     |     Media Sanitization          |     To sanitize all digital and non-digital system media subject to disposal or reuse, whether or not the media is considered removable.     |
|     MP-6(2)     |     Media Sanitization - Equipment Testing          |     To be completed.     |
|     MP-6(8)     |     Media Sanitization - Remote Purging or Wiping of Information          |     To be completed.     |
|     MP-7     |     Media Use          |     To restrict or prohibit the use of organization-defined types of system media on organization-defined systems or system components and prohibit the use of portable storage devices in organizational systems when such devices have no identifiable owner.     |
{{% /details %}}

{{% details summary="Physical and Environmental Protection (PE)" %}}
> [<i class="fa-solid fa-file-lines"></i> Physical and Environmental Protection (PE)]({{< ref "../security-compliance" >}})

This control family covers physical access to devices and facilities, and the mitigation of threats to facilities. Controls cover policies for physical access to system controls, including monitoring access and visitors, as well as the monitoring of devices and assets. Other controls cover responses to physical threats, such as emergency lighting or power and the relocation to alternative facilities.

| Control | Title | Description |
|---------|-------------|---------------|
|     PE-1     |     Policy and Procedures          |     Establishment of physical and environmental protection policy and procedures that address the controls in the PE family implemented within systems and organizations.     |
 {{% /details %}}

{{% details summary="Planning (PL)" %}}
> [<i class="fa-solid fa-file-lines"></i> Planning (PL)]({{< ref "../security-compliance" >}})

This control family covers privacy and system security plans (SSPs), including system architecture, management processes, and the setting of baseline system settings.

| Control | Title | Description |
|---------|-------------|---------------|
|     PL-1     |     Policy and Procedures          |     Establishment of planning policy and procedures that address the controls in the PL family implemented within systems and organizations.     |
|     PL-2     |     System Security and Privacy Plans          |     Scoped to the system and system components within the defined authorization boundary and contain an overview of the security and privacy requirements for the system and the controls selected to satisfy the requirements.     |
|     PL-4     |     Rules of Behavior          |     To establish and provide to individuals requiring access to the system, the rules that describe their responsibilities and expected behavior for information and system usage, security, and privacy.     |
|     PL-4(1)     |     Rules of Behavior - Social Media and External Site/application Usage Restrictions          |     To be completed.     |
|     PL-8     |     Security and Privacy Architectures          |     To be consistent with the organization-wide security and privacy architectures, which are integral to and developed as part of the enterprise architecture.     |
|     PL-10     |     Baseline Selection          |     Predefined sets of controls specifically assembled to address the protection needs of a group, organization, or community of interest.     |
 {{% /details %}}

{{% details summary="Program Management (PM)" %}}
> [<i class="fa-solid fa-file-lines"></i> Program Management (PM)]({{< ref "../security-compliance" >}})

This control family covers all elements of the management of an information system, including a variety of processes, programs, and plans. This includes an information security program plan, risk management strategy, and critical infrastructure plan.

| Control | Title | Description |
|---------|-------------|---------------|
|     PM-1     |     Information Security Program Plan          |     Establishment of a formal document that provides an overview of the security requirements for an organization-wide information security program and describes the program management controls and common controls in place or planned for meeting those requirements.     |
|     PM-2     |     Information Security Program Leadership Role          |     To appoint a senior agency information security officer with the mission and resources to coordinate, develop, implement, and maintain an organization-wide information security program.     |
|     PM-2(1)     |     Information Security Program Leadership Role - Board of Directors Oversight and Communication          |     To be completed.     |
|     PM-3     |     Information Security and Privacy Resources          |     To include the resources needed to implement the information security and privacy programs in capital planning and investment requests and document all exceptions to this requirement.     |
|     PM-4     |     Plan of Action and Milestones Process          |     Developed with an organization-wide perspective, prioritizing risk response actions and ensuring consistency with the goals and objectives of the organizations.     |
|     PM-6     |     Measures of Performance          |     To develop, monitor, and report on the results of information security and privacy measures of performance.     |
|     PM-8     |     Critical Infrastructure Plan          |     To address information security and privacy issues in the development, documentation, and updating of a critical infrastructure and key resources protection plan.     |
|     PM-9     |     Risk Management Strategy          |     To establish an expression of the security and privacy risk tolerance for the organization, security and privacy risk mitigation strategies, acceptable risk assessment methodologies, a process for evaluating security and privacy risk across the organization with respect to the organization’s risk tolerance, and approaches for monitoring risk over time.     |
|     PM-9(1)     |     Risk Management Strategy - Fraud Considerations          |     To be completed.     |
|     PM-9(2)     |     Risk Management Strategy - Significant Change Considerations          |     To be completed.     |
|     PM-10     |     Authorization Process          |     To manage the security and privacy state of organizational systems and the environments in which those systems operate through authorization processes.     |
|     PM-11     |     Mission and Business Process Definition          |     To define organizational mission and business processes with consideration for information security and privacy and the resulting risk to organizational operations, organizational assets, individuals, other organizations, and the Nation.     |
|     PM-15     |     Security and Privacy Groups and Associations          |     To establish ongoing contact with security and privacy groups and associations in an environment of rapidly changing technologies and threats.     |
|     PM-18     |     Privacy Program Plan          |     To develop and disseminate a formal document that provides an overview of an organization’s privacy program.     |
|     PM-20     |     Dissemination of Privacy Program Information          |     To maintain a central resource webpage on the organization’s principal public website that serves as a central source of information about the organization’s privacy program.     |
|     PM-20(1)     |     Dissemination of Privacy Program Information - Privacy Policies on Websites, Applications, and Digital Services          |     To be completed.     |
|     PM-21     |     Accounting of Disclosures          |     To develop and maintain an accurate accounting of disclosures of personally identifiable information.     |
|     PM-22     |     Personally Identifiable Information Quality Management          |     Steps that organizations take to confirm the accuracy and relevance of personally identifiable information throughout the information life cycle.     |
|     PM-25     |     Minimization of Personally Identifiable Information Used in Testing, Training, and Research          |     Develop, document and implement policies and procedures to address the use of personally identifiable information for internal testing, training, and research.     |
|     PM-26     |     Complaint Management          |     To implement a process for receiving and responding to complaints, concerns, or questions from individuals about the organizational security and privacy practices.     |
|     PM-28     |     Risk Framing          |     To identify the assumptions, constraints, risk tolerance, priorities, and trade-offs when conducted at the organization level and in consultation with stakeholders throughout the organization including mission, business, and system owners.     |
|     PM-29     |     Risk Management Program Leadership Roles          |     Senior accountable official for risk management leads the risk executive (function) in organization-wide risk management activities.     |
|     PM-30     |     Supply Chain Risk Management Strategy          |     To develop an organization-wide strategy for managing supply chain risks associated with the development, acquisition, maintenance, and disposal of systems, system components, and system services.     |
 {{% /details %}}

{{% details summary="Personnel Security (PS)" %}}
> [<i class="fa-solid fa-file-lines"></i> Personnel Security (PS)]({{< ref "../security-compliance" >}})

This control family covers different policies and procedures around the management of personnel. This includes the process for terminating personnel contracts and the relative risk of each position to information security.

| Control | Title | Description |
|---------|-------------|---------------|
|     PS-1     |     Policy and Procedures          |     Establishment of personnel security policy and procedures that address the controls in the PS family implemented within systems and organizations.     |
|     PS-2     |     Position Risk Designation          |     To establish the foundation of an effective and consistent suitability and personnel security program.     |
|     PS-3     |     Personnel Screening          |     To screen individuals prior to authorizing access to the systems.     |
|     PS-3(1)     |     Personnel Screening - Classified Information          |     To be completed.     |
|     PS-3(3)     |     Personnel Screening - Information Requiring Special Protective Measures          |     To be completed.     |
|     PS-4     |     Personnel Termination          |     Termination of individual employment.     |
|     PS-5     |     Personnel Transfer          |     Permanent reassignments or transfers of individuals or of such extended duration as to make the actions warranted.     |
|     PS-6     |     Access Agreements          |     Signed access agreements with acknowledgement that individuals have read, understand, and agree to abide by the constraints associated with organizational systems to which access is authorized.     |
|     PS-6(2)     |     Access Agreements - Classified Information Requiring Special Protection          |     To be completed.     |
|     PS-7     |     External Personnel Security          |     To establish personnel security requirements, including security roles and responsibilities for external providers.     |
|     PS-8     |     Personnel Sanctions          |     To employ a formal sanctions process for individuals failing to comply with established information security and privacy policies and procedures.     |
|     PS-9     |     Position Descriptions          |     To establish specification of security and privacy roles in individual organizational position descriptions to facilitate clarity in understanding the security or privacy responsibilities associated with the roles and the role-based security and privacy training requirements for the roles.     |
{{% /details %}}

{{% details summary="Personally Identifiable Information (PII) Processing and Transparency (PT)" %}}
> [<i class="fa-solid fa-file-lines"></i> Personally Identifiable Information (PII) Processing and Transparency (PT)]({{< ref "../security-compliance" >}})

This control family helps to safeguard sensitive data, focusing on consent and privacy. Organizations can lower the risk of data breaches by properly managing personally identifiable information.

| Control | Title | Description |
|---------|-------------|---------------|
|     PT-1     |     Policy and Procedures          |     Establishment of personally identifiable information processing and transparency policy and procedures that address the controls in the PT family implemented within systems and organizations.     |
|     PT-3     |     Personally Identifiable Information Processing Purposes          |     To identify and document the purpose for processing providing organizations with a basis for understanding why personally identifiable information may be processed.     |
|     PT-9     |     Physical Copies          |     To restrict, control, and track the creation and destruction of physical documents containing personally identifiable information.     |
{{% /details %}}

{{% details summary="Risk Assessment (RA)" %}}
> [<i class="fa-solid fa-file-lines"></i> Risk Assessment (RA)]({{< ref "../security-compliance" >}})

This control family focuses on the assessment of system vulnerabilities and relevant risk. Controls cover the development of risk response procedures, and the use of vulnerability monitoring tools and processes.

| Control | Title | Description |
|---------|-------------|---------------|
|     RA-1     |     Policy and Procedures          |     Establishment of risk assessment policy and procedures that address the controls in the RA family implemented within systems and organizations.     |
|     RA-2     |     Security Categorization          |     To describe the potential adverse impacts or negative consequences to organizational operations, organizational assets, and individuals if organizational information and systems are compromised through a loss of confidentiality, integrity, or availability.     |
|     RA-3     |     Risk Assessment          |     To consider threats, vulnerabilities, likelihood, and impact to organizational operations and assets, individuals, other organizations, and the Nation.     |
|     RA-5     |     Vulnerability Monitoring and Scanning v2          |     To mnitor and scan for vulnerabilities in the system and hosted applications when new vulnerabilities potentially affecting the system are identified and reported.     |
|     RA-7     |     Risk Response          |     To respond to findings from security and privacy assessments, monitoring, and audits in accordance with organizational risk tolerance.     |
|     RA-7(1)     |     Risk Response - Insurance Considerations          |     To be completed.     |
|     RA-8     |     Privacy Impact Assessments          |     An analysis of how personally identifiable information is handled to ensure that handling conforms to applicable privacy requirements, determine the privacy risks associated with an information system or activity, and evaluate ways to mitigate privacy risks.     |
|     RA-9     |     Criticality Analysis          |     To identify critical system components and functions by performing a criticality analysis.     |
{{% /details %}}


{{% details summary="System and Services Acquisition (SA)" %}}
> [<i class="fa-solid fa-file-lines"></i> System and Services Acquisition (SA)]({{< ref "../security-compliance" >}})

This control family includes the allocation of resources and the creation of system development life cycles. Controls help organizations create a safe acquisition process for new systems and devices, safeguarding the integrity of the wider system and data. Controls also cover the development and testing process for new systems, including developer training and security processes.

| Control | Title | Description |
|---------|-------------|---------------|
|     SA-1     |     Policy and Procedures          |     Develop, document, and disseminate system and services acquisition policy and procedures that address the controls in the Service Acquisition (SA) control family implemented within GitLab Inc. and it's associated in-scope systems and services.     |
|     SA-2     |     Allocation of Resources          |     Allocate required resources to protect information security and privacy requirements related to system and services acquisition and sustainment as part of the business planning and capital planning and investment process.     |
|     SA-3     |     System Development Life Cycle          |     Establish a system development life cycle to support the successful development, implementation, and operation of GitLab's systems.     |
|     SA-4     |     Acquisition Process          |     Establish an acquisition process covering security and privacy requirements to support system, system component and system service acquisitions and implementations.     |
|     SA-4(1)     |     Acquisition Process - Functional Properties of Controls          |     To be completed.     |
|     SA-4(2)     |     Acquisition Process - Design and Implementation Information for Controls          |     To be completed.     |
|     SA-4(8)     |     Acquisition Process - Continuous Monitoring Plan for Controls          |     To be completed.     |
|     SA-4(9)     |     Acquisition Process - Functions, Ports, Protocols, and Services in Use          |     To be completed.     |
|     SA-4(10)     |     Acquisition Process - Use of Approved PIV Products          |     To be completed.     |
|     SA-8     |     Security and Privacy Engineering Principles v2          |     Develop and implement systems security and privacy engineering principles in the specification, design, development, implementation, and modification of system and system components.     |
|     SA-9(1)     |     External System Services - Risk Assessments and Organizational Approvals          |     To be completed.     |
|     SA-9(2)     |     External System Services - Identification of Functions, Ports, Protocols, and Services          |     To be completed.     |
|     SA-9(3)     |     External System Services - Establish and Maintain Trust Relationship with Providers          |     To be completed.     |
|     SA-9(4)     |     External System Services - Consistent Interests of Consumers and Providers          |     To be completed.     |
|     SA-9(5)     |     External System Services - Processing, Storage, and Service Location          |     To be completed.     |
|     SA-15     |     Development Process, Standards, and Tools          |     Establish a development process that supports GitLab's change management program and addresses GitLab's security and privacy requirements.     |
|     SA-21     |     Developer Screening          |     Establish and implement access controls and screening criteria for external developers performing work on acquired systems and services.     |
{{% /details %}}

{{% details summary="System and Communications Protection (SC)" %}}
> [<i class="fa-solid fa-file-lines"></i> System and Communications Protection (SC)]({{< ref "../security-compliance" >}})

This control family covers the protection of system boundaries and the safe management of collaborative devices. Controls provide in-depth guidance on set-up and ongoing management of systems, including access, partitions, and usage restrictions.

| Control | Title | Description |
|---------|-------------|---------------|
|     SC-1     |     Policy and Procedures          |     Establishment of system and communications protection policy and procedures that address the controls in the SC family implemented within systems and organizations.     |
|     SC-5     |     Denial-of-service Protection          |     To protect against or limit the effects of denial-of-service events.     |
|     SC-7     |     Boundary Protection v2          |     To monitor and control communications at the external managed interfaces to the system and at key internal managed interfaces within the system.     |
|     SC-7(5)     |     Boundary Protection - Deny by Default — Allow by Exception          |     To be completed.     |
|     SC-7(9)     |     Boundary Protection - Restrict Threatening Outgoing Communications Traffic          |     To be completed.     |
|     SC-7(10)     |     Boundary Protection - Prevent Exfiltration          |     To be completed.     |
|     SC-7(12)     |     Boundary Protection - Host-based Protection          |     To be completed.     |
|     SC-8     |     Transmission Confidentiality and Integrity v2          |     To protect the confidentiality and integrity of transmitted information.     |
|     SC-12     |     Cryptographic Key Establishment and Management          |     To establish and manage cryptographic keys when cryptography is employed within the system.     |
|     SC-18     |     Mobile Code          |     Develop and implement a program to define acceptable and unacceptable mobile code and mobile code technologies, and authorize, monitor, and control the use of mobile code within GitLab's systems.     |
|     SC-18(1)     |     Mobile Code - Identify Unacceptable Code and Take Corrective Actions          |     To be completed.     |
|     SC-18(2)     |     Mobile Code - Acquisition, Development, and Use          |     To be completed.     |
|     SC-28     |     Protection of Information at Rest v2          |     To protect the confidentiality and/or integrity of information at rest.     |
|     SC-28(3)     |     Protection of Information at Rest - Cryptographic Keys          |     To be completed.     |
{{% /details %}}

{{% details summary="System and Information Integrity (SI)" %}}
> [<i class="fa-solid fa-file-lines"></i> System and Information Integrity (SI)]({{< ref "../security-compliance" >}})

This control family focuses on maintaining the integrity of the information system. Controls cover topics like protection from malicious code and spam, and procedures for ongoing system-wide monitoring.

| Control | Title | Description |
|---------|-------------|---------------|
|     SI-1     |     Policy and Procedures          |     Establishment of system and information integrity policy and procedures that address the controls in the SI family implemented within systems and organizations.     |
|     SI-2     |     Flaw Remediation v2          |     To identify, report, and correct system flaws.     |
|     SI-3     |     Malicious Code Protection v2          |     To implement malicious code protection mechanisms at system entry and exit points to detect and eradicate malicious code.     |
|     SI-4     |     System Monitoring v2          |     Internal and external monitoring of systems to detect attacks and indicators of potential attacks.     |
|     SI-4(23)     |     System Monitoring - Host-based Devices v2          |     To be completed.     |
|     SI-5     |     Security Alerts, Advisories, and Directives          |     To receive system security alerts, advisories, and directives from organization-defined external organizations] on an ongoing basis.     |
|     SI-12     |     Information Management and Retention          |     To manage and retain information within the system and information output from the system to cover the full life cycle of information, in some cases extending beyond system disposal in accordance with applicable laws, executive orders, directives, regulations, policies, standards, guidelines and operational requirements.     |
|     SI-12(1)     |     Information Management and Retention - Limit Personally Identifiable Information Elements          |     To be completed.     |
|     SI-12(3)     |     Information Management and Retention - Information Disposal          |     To be completed.     |
|     SI-13     |     Predictable Failure Prevention          |     To determine mean time to failure (MTTF) to address potential failures of system components that provide security capabilities.     |
|     SI-18     |     Personally Identifiable Information Quality Operations          |     To confirm the accuracy and relevance of personally identifiable information throughout the information life cycle.     |
|     SI-18(4)     |     Personally Identifiable Information Quality Operations - Individual Requests          |     To be completed.     |
{{% /details %}}

{{% details summary="Supply Chain Risk Management (SR)" %}}
> [<i class="fa-solid fa-file-lines"></i> Supply Chain Risk Management (SR)]({{< ref "../security-compliance" >}})

This control family covers policies and procedures to counter risks in the supply chain. This includes processes to assess and manage suppliers, and the inspection of supply chain systems and components.

| Control | Title | Description |
|---------|-------------|---------------|
|     SR-1     |     Policy and Procedures          |     Establishment of supply chain risk management policy and procedures that address the controls in the SR family implemented within systems and organizations.     |
|     SR-2     |     Supply Chain Risk Management Plan          |     To develop a plan for managing supply chain risks associated with the dependence on products, systems, and services from external providers, as well as the nature of the relationships with those providers that present an increasing level of risk to an organization.     |
|     SR-2(1)     |     Supply Chain Risk Management Plan - Establish SCRM Team          |     To be completed.     |
|     SR-3     |     Supply Chain Controls and Processes          |     To establish a process or processes to identify and address weaknesses or deficiencies in the supply chain elements and processes of organization-defined system or system component in coordination with organization-defined supply chain personnel.     |
|     SR-3(3)     |     Supply Chain Controls and Processes - Sub-tier Flow Down          |     To be completed.     |
|     SR-3(4)     |     Supply Chain Controls and Processes - Termination of Vendor and Business Partner Relationships          |     To be completed.     |
|     SR-3(5)     |     Supply Chain Controls and Processes - Confidentiality Commitments          |     To be completed.     |
|     SR-3(6)     |     Supply Chain Controls and Processes - Cloud Services - Shared Roles and Responsibilities Agreements          |     To be completed.     |
|     SR-3(7)     |     Supply Chain Controls and Processes - Cloud Services - Special Contractual Considerations          |     To be completed.     |
|     SR-3(8)     |     SOC Report CUEC Review          |     Review of Service Provider CUECs to ensure adequate coverage of identified control areas passed onto the end user.     |
|     SR-4     |     Provenance          |     To document, monitor, and maintain valid provenance of the systems, system components, and associated data.     |
|     SR-5     |     Acquisition Strategies, Tools, and Methods          |     To employ acquisition strategies, contract tools, and procurement methods to protect against, identify, and mitigate supply chain risks of organization-defined acquisition strategies, contract tools, and procurement methods.     |
|     SR-6     |     Supplier Assessments and Reviews          |     To assess and review the supply chain-related risks associated with suppliers or contractors and the system, system component, or system service they provide.     |
|     SR-6(1)     |     Supplier Assessments and Reviews - Testing and Analysis          |     To be completed.     |
|     SR-8     |     Notification Agreements          |     To establish agreements and procedures with entities involved in the supply chain for the system, system component, or system service.     |
|     SR-9     |     Tamper Resistance and Detection          |     To implement a tamper protection program for the system, system component, or system service.     |
|     SR-9(1)     |     Tamper Resistance and Detection - Multiple Stages of System Development Life Cycle          |     To be completed.     |
|     SR-12     |     Component Disposal          |     To dispose of organization-defined data, documentation, tools, or system components.     |
{{% /details %}}

## References

<a href="{{< ref "../security-compliance" >}}" class="btn bg-primary text-white btn-lg">Return to the Security Compliance</a>
