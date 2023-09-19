---
title: "Security Risk Team"
---

## <i class="fas fa-bullseye" style="color:rgb(110,73,203)" aria-hidden="true"></i> Security Risk Mission{#security-risk-mission}

To improve security at GitLab by enabling informed and intelligent decision making through proactive identification, monitoring, and reporting of security risks.

## <i class="far fa-lightbulb" style="color:rgb(110,73,203)" aria-hidden="true"></i> Core Competencies{#core-competencies}

----

### <i class="fas fa-shield-alt" style="color:rgb(253,109,38)" aria-hidden="true"></i> Security Operational Risk Management (StORM) Program{#storm}

An integrated Operational Risk Management program which focuses on the identification, assessment, continuous monitoring, and reporting of security risks across the organization. Visit the [StORM Program & Procedures]({{< ref "storm-program" >}}) handbook page for additional details, including a quick introduction to Risk Management at GitLab as well as information about the purpose, scope, and specific procedures executed as part of the program.


{{% panel header="**Need to communicate a potential risk to the team?**" header-bg="warning" %}}
Please refer to the [communication section of the StORM Program & Procedures]({{< ref "storm-program#communication-of-risks-to-the-security-risk-team" >}}) page for information on the various ways that team members can use to escalate potential risks to the Security Risk Team.
{{% /panel %}}

### <i class="fas fa-hands-helping" style="color:rgb(253,109,38)" aria-hidden="true"></i> Security Third Party Risk Management (TPRM) Program{#tprm}

The TPRM Program is focused on identifying and assessing the incremental security risk impact that may develop over the lifecycle of GitLab's relationship with various third parties. Our program is integrated within the [Procurement](https://about.gitlab.com/handbook/finance/procurement/) process and is built to continuously monitor third parties based on risk. Additional information can be found on the [Third Party Risk Management]({{< ref "third-party-risk-management" >}}) handbook page.

### <i class="fas fa-exclamation-triangle" style="color:rgb(253,109,38)" aria-hidden="true"></i> Business Impact Analysis (BIA) and Critical System Tiering (CST){#bia}

The [Business Impact Analysis]({{< ref "business-impact-analysis" >}}) (BIA) helps determine the systems critical to serving GitLab's Customers. It also helps determine the prioritization of system restoration efforts in the event of a disruption.

The Security Risk Team facilitates a BIA for all new systems. A BIA is performed or previously collected BIA data is validated for existing systems based on [Critical System Tiering (CST)]({{< ref "critical-systems#critical-systems-tiering-methodology" >}}).

### <i class="fas fa-warehouse" style="color:rgb(253,109,38)" aria-hidden="true"></i> Asset Inventory Maintenance{#asset-inventory}

Establishing a complete and accurate inventory of assets is key to the success of GitLab's Risk Program. As such, the Security Risk Team collaborates closely with IT and Business Owners to ensure new systems are added to the [Tech Stack](https://about.gitlab.com/handbook/business-technology/tech-stack-applications/#roles-and-responsibilities) and that associated data is maintained via our BIA processes.

----

## <i class="fas fa-tasks" style="color:rgb(110,73,203)" aria-hidden="true"></i> Metrics and Measures of Success{#metrics}

- [StORM Program Risk Heatmap]({{< ref "/handbook/security/performance-indicators#operational-security-risk-management-tier-2-risks" >}})
- [Third Party Risk Management - Residual Risk Ratings]({{< ref "/handbook/security/performance-indicators#third-party-risk-management" >}})

## <i class="fas fa-users" style="color:rgb(110,73,203)" aria-hidden="true"></i> Team Members{#team-members}

|Team Member|Role|
|:----------:|:----------:|
|[Ty Dilbeck](https://gitlab.com/tdilbeck)|[Manager, Security Risk](handbook/job-families/security/security-risk/#manager-security-risk)|
|[Eric Geving](https://gitlab.com/ericgeving)|[Senior Security Risk Engineer](handbook/job-families/security/security-risk/#senior-security-risk-engineer)|
|[Kyle Smith](https://gitlab.com/kylesmith2)|[Senior Security Risk Engineer](handbook/job-families/security/security-risk/#senior-security-risk-engineer)|
|[Ryan Lawson](https://gitlab.com/rlawson1)|[Senior Security Risk Engineer](handbook/job-families/security/security-risk/#senior-security-risk-engineer)|
|[Nirmal Devarajan](https://gitlab.com/ndevarajan)|[Security Assurance Engineer](handbook/job-families/security/security-risk/#security-risk-engineer-intermediate)|

## <i class="fa-solid fa-d" style="color:rgb(110,73,203)" aria-hidden="true"></i> Functional DRIs{#dris}

While the [DRI](https://about.gitlab.com/handbook/people-group/directly-responsible-individuals/#characteristics-of-a-project-dri) is the individual who is ultimately held accountable for the success or failure of any given project, they are not necessarily the individual that does the tactical project work. The DRI should consult and collaborate with all teams and stakeholders involved to ensure they have all relevant context, to gather input/feedback from others, and to divide action items and tasks amongst those involved.

DRIs are responsible for ensuring a [handbook-first approach](https://about.gitlab.com/company/culture/all-remote/handbook-first-documentation/) to their project(s) and challenging existing processes for [efficiency]({{< ref "values#efficiency" >}}).

|Function     |DRI|
|:----------:|:----------:|
|[Annual Risk Assessment]({{< ref "storm-program#storm-procedures" >}})     |Kyle Smith|
|[Business Impact Analysis - Design And Requirements]({{< ref "business-impact-analysis" >}})     |Kyle Smith|
|[Business Impact Analysis - Reporting and Periodic BIA Execution]({{< ref "business-impact-analysis" >}})     |Nirmal Devarajan|
|[Critical System Tiering]({{< ref "critical-systems#determining-critical-system-tiers" >}})     |Kyle Smith|
|[Ongoing SecRisk-Related Observations Management]({{< ref "observation-management-procedure#introduction-to-observation-management-at-gitlab" >}})     |Ty Dilbeck|
|[Ongoing Risk Treatment](storm-program#storm-procedures)     |Kyle Smith|
|[Ongoing TPRM Assessments]({{< ref "third-party-risk-management" >}})     |Ryan Lawson|
|[Periodic SOX CUEC Facilitation]({{< ref "sox_cuec_mapping_procedure" >}})     |Eric Geving|
|[Periodic TPRM Assessments]({{< ref "third-party-risk-management" >}})     |Eric Geving|
|TPRM Data Quality and Emerging Requirements Management | Eric Geving |
|[StORM Metrics and Reporting](storm-program#step-5-annual-storm-reports)     |Kyle Smith|
|TPRM Metrics and Reporting     |Ryan Lawson|

## <i class="fas fa-id-card" style="color:rgb(110,73,203)" aria-hidden="true"></i> Contact the Team{#contact}

- <i class="fas fa-envelope fa-fw" style="color:rgb(219,59,33)" aria-hidden="true"></i> Email: `securityrisk@gitlab.com`
- <i class="fab fa-slack fa-fw" style="color:rgb(219,59,33)" aria-hidden="true"></i> Slack:
   - [#security-risk-management channel](https://gitlab.slack.com/archives/C01EKDNRVFD)
   - [#sec-assurance channel](https://gitlab.slack.com/archives/C0129P7DW75) (includes the broader Security Assurance Team)
   - Mention `@security-risk`
- <i class="fab fa-gitlab fa-fw" style="color:rgb(219,59,33)" aria-hidden="true"></i> GitLab: Tag the team across GitLab using `@gitlab-com/gl-security/security-assurance/security-risk-team`

<a href="{{< ref "security-assurance" >}}" class="btn bg-primary text-white btn-lg">Return to the Security Assurance Homepage</a>
