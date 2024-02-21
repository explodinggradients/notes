---
title: "Critical System Tiering Methodology"
summary: "The purpose of the Critical Systems Tiering Methodology is to support GitLab in identifying and understanding the specific systems utilized across the organization that are considered essential in order to maintain operations."
---

## Purpose

The purpose of the Critical Systems Tiering Methodology is to support GitLab in categorizing systems based on their effect on GitLab's SaaS subscriptions and the achievement of Gitlab's [mission]({{< ref "mission#mission" >}}) and [strategy]({{< ref "strategy" >}}). Ultimately, this provides GitLab with a mechanism to take a proactive approach to comprehensive risk management which considers risks, such as information security and privacy risks, impacting business operations across the organization. Additionally, by classifying systems into specific tiers, GitLab will be in a better position to appropriately prioritize risk mitigation activities and tailor internal controls based on a system's related tier.

## Scope

The critical systems tiering methodology is applicable to all systems utilized across GitLab which are tracked within the [Tech Stack](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml) to ensure that all systems are vetted completely and accurately using a consistent and standardized methodology.

## Roles and Responsibilities

|Role|Responsibility|
|----------|------------------------------|
|[Security Risk Team](/handbook/security/security-assurance/security-risk/)|Executes an annual review of critical system tiers and makes adjustments as necessary. Owns the Critical System Tiering Methodology and supports the identification of and assignment of a critical system tier as needed.|
|[IT Compliance](/handbook/business-technology/it-compliance/)|Supports defining of critical system tier in conjunction with the Security Risk Team when new systems are added to the tech stack.|
|Business and Technical Owners of Systems|Provide complete and accurate data about the systems that they own so that an accurate tier is assigned.|

## Critical System Tiering Procedure

Defining what a critical system means at GitLab can be complex given the nature of our environment and the number of integrations that exist across the many systems that are used to carry out business activities. As part of Gitlab's [Business Impact Analysis (BIA)]({{< ref "business-impact-analysis" >}}) process, we obtain inputs that enable the assignment of a critical system tier per system. The inputs used to determine system criticality tiers include, but are not limited to, the following:

1. If the system experienced a disruption or outage, would there be an immediate impact to GitLab.com SaaS subscriptions?
1. If the system experienced a disruption or outage, which of the following would describe the impact to GitLab?
   - Critical business functions (i.e., indirectly affects revenue generation, requires constant availability for effective business operation)
   - Operational business functions (i.e., affects efficiency/cost of operation)
   - Administrative functions (i.e., affects GitLab team members only on an individual basis (e.g., quality of life, individual productivity))

Once the information is obtained, it is reviewed by the Security Risk and/or IT Compliance Team to determine which system tier should be assigned to the system. The guidelines used to assign a tier are described in the [Determining Critical System Tiers](#determining-critical-system-tiers) section below.

{{% panel header="**Why do we differentiate between impact to the SaaS subscriptions vs Critical internal business operations?**" header-bg="warning" %}}
Critical system tiers are meant to be leveraged as a driver for prioritizing work that impacts a large number of systems. Utilizing the system tiers provide a meaningful mechanism to prioritize work for systems which are essential to GitLab and its customers. Furthermore, because the core service offering is GitLab.com, systems which have an impact on GitLab's ability to maintain/sustain the continued delivery of GitLab.com are given their own dedicated tier, *Tier 1 Mission Critical*, because of potential impact to all SaaS subscription customers.
{{% /panel %}}

### Determining Critical System Tiers

Systems are assigned a critical system tier based on the following matrix:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
.tg td{border-color:black;border-style:solid;border-width:1px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-zqun{background-color:#ffffff;color:#000000;text-align:center;vertical-align:middle}
.tg .tg-knp3{background-color:#6e49cb;border-color:#000000;color:#ffffff !important;;
  text-align:center;vertical-align:middle}
.tg .tg-clye{background-color:#380d75;color:#ffffff;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-fecx{background-color:#cccccc;color:#000000;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-cc97{background-color:#380d75;color:#ffffff;text-align:center;vertical-align:middle}
.tg .tg-dxvi{background-color:#6e49cb;color:#ffffff;font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-e02t{background-color:#ffffff;border-color:#000000;color:#000000 !important;;
  font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-9hzb{background-color:#FFF;font-weight:bold;text-align:center;vertical-align:top}
</style>
<table class="tg">
<tbody>
  <tr>
    <td class="tg-clye">Critical System Tier (CST) <span style="color:#DB3B21;">*</span></td>
    <td class="tg-dxvi">CST Description</td>
    <td class="tg-dxvi">Examples</td>
    <td class="tg-fecx">Previous CST Tier Mapping</td>
  </tr>
  <tr>
    <td class="tg-e02t">Tier 1 Mission Critical<span style="color:#DB3B21;">**</span></td>
    <td class="tg-zqun">Disruption or breach has an immediate and significant impact to the availability/security of GitLab subscriptions and customer data (See <a href="{{< ref "data-classification-standard#data-classification-definitions" >}}">Data Classification Standard</a> for definitions).</td>
    <td class="tg-zqun">GitLab.com, Google Cloud Platform, Devo</td>
    <td class="tg-zqun">Tier 1 Product</td>
  </tr>
  <tr>
    <td class="tg-e02t">Tier 2 Business Critical<span style="color:#DB3B21;">***</span></td>
    <td class="tg-zqun">Disruption has an immediate and significant impact to critical business functions and customer service.</td>
    <td class="tg-zqun">Okta, Salesforce, Workday</td>
    <td class="tg-zqun">Tier 1 Business and Tier 2 Core</td>
  </tr>
  <tr>
    <td class="tg-e02t">Tier 3 Business Operational</td>
    <td class="tg-zqun">Disruption affects operational business functions, negatively impacting efficiency/cost of operation across departments</td>
    <td class="tg-zqun">DocuSign, Figma, Tableau</td>
    <td class="tg-zqun">Combination of Tier 2 Support and Tier 3 Non-critical and influenced by responses to BIA</td>
  </tr>
  <tr>
    <td class="tg-e02t">Tier 4 Administrative</td>
    <td class="tg-zqun">Affects GitLab team members only at an individual level (e.g., quality of life, individual productivity)</td>
    <td class="tg-zqun">Clockwise, Donut, LinkedIn Learning</td>
    <td class="tg-zqun">Combination of Tier 2 Support and Tier 3 Non-critical and influenced by responses to BIA</td>
  </tr>
</tbody>
</table>
<br/>

{{% panel header="**Notes**" header-bg="primary" %}}
{{% note %}}
<span style="color:#DB3B21;"><b>\*</b></span> As an extension of tiering methodology, the [Data Classification Standard]({{< ref "data-classification-standard" >}}) prescribes **specific** [Security and Privacy]({{< ref "data-classification-standard#security-and-privacy-controls" >}}) control requirements for each data classification level. These requirements should be followed based on a system's data classification, regardless of the system's tier.
{{% /note %}}
{{% note %}}
<span style="color:#DB3B21;"><b>\**</b></span> By default, any system that contains <b>RED Data</b> per the [Data Classification Standard]({{< ref "data-classification-standard#red" >}}) OR is a [Third Party Sub-Processor](https://about.gitlab.com/privacy/subprocessors/#third-party-sub-processors) will be a **Tier 1 Mission Critical** system. This is due to the fact that this data is customer owned and uploaded and as such, has been deemed to be mission critical in nature.
{{% /note %}}
{{% note %}}
<span style="color:#DB3B21;"><b>*\*\*</b></span> By default, any system in-scope for [SOX](https://about.gitlab.com/handbook/internal-audit/sarbanes-oxley/) will be a **Tier 2 Business Critical** system, at minimum.
{{% /note %}}
{{% /panel %}}

### Why does GitLab need this methodology?

Tiering systems utilized across GitLab enables team members to make decisions on prioritizing work related to a specific system(s) based on the assigned tier. As an example, if multiple risks have been identified over a wide variety of systems and require remediation, impacted team members can leverage the assigned critical system tiers to make a decision on how to prioritize remediation activities. This methodology will also provide GitLab with a mechanism to easily identify those systems which are most critical across the organization so that we can proactively protect and secure those systems.

### Maintaining Critical System Tiers

The Critical System Tier for existing systems is re-evaluated as part of the periodic [BIA]({{< ref "business-impact-analysis#existing-systems-frequency-based-on-critical-system-tier" >}}) process. A system's assigned tier can be found in the [tech_stack.yml file](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml) which is the Single Source of Truth for all systems used at GitLab.

## Exceptions

Systems that are exempt from this methodology include any system which carries a data classification of Green. All remaining systems which store or process YELLOW, ORANGE, or RED data are required to have a critical system tier assigned. Data classification will be validated to corroborate that the data stored or processed by the system is truly Green data, per the [Data Classification Standard]({{< ref "data-classification-standard#green" >}}).

## References

- [Business Impact Analysis]({{< ref "business-impact-analysis" >}})
- [Data Classification Standard]({{< ref "data-classification-standard" >}})
