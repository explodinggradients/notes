---
title: "Security Operational Risk Management (StORM) Program & Procedures"
---

{{% alert title="This is a Controlled Document" color="danger" %}}
Inline with GitLab's regulatory obligations, changes to [controlled documents]({{< ref "controlled-document-procedure" >}}) must be approved or merged by a code owner. All contributions are welcome and encouraged.
{{% /alert %}}

{{% panel header="**Not a GitLab team member but want to provide feedback on our StORM program?**" header-bg="primary" %}}
We receive [feedback](https://about.gitlab.com/handbook/people-group/guidance-on-feedback/#feedback-at-gitlab) from GitLab team members regularly and we wanted to provide a mechanism for non-GitLab team members to provide feedback as well to help us [iterate](https://handbook.gitlab.com/handbook/values/#iteration) and align more closely with [our values](https://handbook.gitlab.com/handbook/values). If you are not a GitLab team member and would like to provide feedback on our Security Operational Risk Management (StORM) program or methodology, plese use this [feedback form](https://docs.google.com/forms/d/e/1FAIpQLSfmD4G6CTdpbCe5Aymoz0oD6Z3Oi1X-2xxYzGNbJ2wcYh6uOA/viewform?usp=sf_link) to submit anonymous feedback.
{{% /panel %}}

## Purpose

The purpose of the Security Operational Risk Management (“StORM”) program at GitLab is to enable better [decision-making](https://about.gitlab.com/handbook/leadership/making-decisions/) by identifying, monitoring, treating, and reporting on security operational risks in support of GitLab's [strategy]({{< ref "strategy" >}}). The Security Risk Team utilizes the procedures below to ensure that security risks that may impact GitLab's ability to achieve its customer commitments and operational objectives are effectively managed.

## Scope

The scope of the StORM program is limited to operational, technology-agnostic security risks, e.g., inadequate physical security controls. These risks can be identified in many ways including Risk Assessments, reports from team members, or as a result of compliance activities.

**Out of Scope** Unless they are related to a StORM risk (e.g., security compliance observations that span multiple systems), the following risk-types are not in scope for StORM:

1. Product/GitLab subscription-specific risks (e.g., specific vulnerabilty found within GitLab.com)
1. Operational risks that are not security-related are out of scope (e.g., accounting-related risks)
1. [Individual security compliance observations]({{< ref "observation-management-procedure" >}}) (e.g., inadequate password settings for a specific system)
1. [Enterprise Risk Management (ERM)](https://internal.gitlab.com/handbook/internal-audit/erm/) - internal only. Examples of ERM risks can be found on our [Mitigating Concerns](https://about.gitlab.com/handbook/leadership/mitigating-concerns/) handbook page.

## Roles and Responsibilities

A risk governance structure has been put in place to outline the overall roles and responsibilities of individuals as it relates to StORM. The current governance structure is:

| Role | Responsibility |
| ------ | ------ |
| Risk Owners | - Makes decisions for their specific organizations including how to respond to risks <br>- Provides insight into the day-to-day operational procedures executed by their organization in support of Risk Treatment planning<br>- Responsible for driving risk acceptance and/or implementing remediation activities over the risks identified |
| Security Risk Team | - Coordinates and executes StORM procedures including establishing risk appetite and conducting risk assessments<br>- Maintains the risk register to ensure accuracy and currency<br>- Acts in a Program Management capacity to support the tracking of risk treatment activities<br>- Coordinates peer validation testing after all risk remediation activities have been completed <br>- Periodically reports on the status of security operational risks |
| Risk Manager | This role is assigned per risk to a specific Security Risk team member. Expectations include:<br>- Maintains knowledge on the history, current-state, and direction of their risk<br>- Works with the risk owner or owners to ensure the risk and remediation activity is accurately captured<br>- Identifies, monitors, and participates in associated issues/MRs/epics/working groups that are relevant to their assigned risk<br>- Validates remediation activities<br>- Maps risks to relevant <a href="https://about.gitlab.com/handbook/security/security-assurance/security-compliance/sec-controls.html#gitlab-control-framework-gcf">GCF controls</a>, <a href="https://gitlab.com/groups/gitlab-com/gl-security/security-assurance/-/epics?state=opened&page=1&sort=start_date_desc&label_name[]=Observation+Epics">Root Cause Observation Epics</a>, <a href="https://gitlab.com/gitlab-com/gl-security/security-assurance/observation-management/-/issues/?sort=created_date&state=opened&label_name%5B%5D=ZenGRC%3A%3AObservation&first_page_size=100">Security Compliance Tier 3 Observations</a>, <a href="https://about.gitlab.com/handbook/security/security-assurance/field-security/field-security-study.html">Field Security Study Observations</a>, and other observations noted from security-impacting assessments|
| Manager of Security Risk Team | Provides management level oversight of the StORM program, including continuing reviews of GitLab's Risk Register and acts as a point of escalation as needed |
| Senior Director of Security Assurance | Provides senior leadership level oversight of the StORM program, including a review and approval of the StORM reports |
| CISO | Executive sponsor of StORM program, performs a final review and approval of the risk assessment reports |
| Senior Leadership | Sets the tone of the risk appetite across the organization <br><br>* Leverages information derived from StORM to make strategic decisions |
| Security Assurance Management (Code Owners) | Responsible for approving significant changes and exceptions to this procedure |

## StORM Procedures

### Establishing Risk Appetite and Tolerance

**Tone at the Top**: GitLab's StORM methodology uses a defined Risk Appetite and Risk Tolerance as primary drivers to determine which risks GitLab are willing to accept/take versus which risks we will need to mitigate. These thresholds are defined by Senior Leadership across the organization to ensure the Tone at the Top is aligned with the StORM program. Risk Appetite and Tolerance are reassessed year-to-year. This is done through an annual [Risk Appetite Survey](https://gitlab.zengrc.com/survey_builder/119) based on the [ISO 31000 Risk Management Methodology](https://www.iso.org/iso-31000-risk-management.html). The survey is distributed to individuals operating in a Senior Leadership capacity with direct relations to Security Operations. The responses are averaged to arrive at an overall risk appetite and tolerance.

#### How GitLab Determines Risk Appetite

GitLab’s security risk appetite is determined based on the total average priority order determined by senior leadership on the following risk strategy statements:

- GitLab should seek solutions to transfer risks to others whenever possible (risk taking vs risk transfer)
- GitLab should balance pursuing opportunities that align with organizational objectives against the associated risks (organizational objectives)
- GitLab should respond to all risks impacting the organization, regardless of the level of impact (risk response approach)
- GitLab should respond to risks based on cost, management priorities, and ROI (risk response drivers)

Each risk strategy statement is ranked in order of priority from Highest priority risk strategy to Lowest priority risk strategy by senior leadership. GitLab utilizes the following risk appetite matrix:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-9wq8{border-color:inherit;text-align:center;vertical-align:middle}
.tg .tg-674h{font-weight:bold;background-color:#380d75;color:#ffffff;border-color:inherit;text-align:center;vertical-align:middle}
.tg .tg-yeut{font-weight:bold;background-color:#656565;color:#ffffff;border-color:inherit;text-align:center;vertical-align:middle}
.tg .tg-747f{font-weight:bold;background-color:#6e49cb;color:#ffffff;border-color:inherit;text-align:center;vertical-align:middle}
</style>
<table class="tg">
  <tr>
    <th class="tg-674h">RISK APPETITE<br>APPROACH</th>
    <th class="tg-yeut">RISK SEEKING</th>
    <th class="tg-yeut">RISK RECEPTIVE</th>
    <th class="tg-yeut">RISK NEUTRAL</th>
    <th class="tg-yeut">RISK AVERSE</th>
  </tr>
  <tr>
    <td class="tg-747f">RISK TAKING vs<br>RISK TRANSFER</td>
    <td class="tg-9wq8">Aggressive risk <br>taking is justified</td>
    <td class="tg-9wq8">Seek opportunities to transfer risks <br>with pre-existing vendors as applicable<br>(e.g. don't bring in a new vendor to<br> transfer risks)</td>
    <td class="tg-9wq8">Take a balanced approach to <br>risk taking vs risk transferring</td>
    <td class="tg-9wq8">Exercise caution and accept as little <br>risk as possible by identifying risk <br>transfer solutions</td>
  </tr>
  <tr>
    <td class="tg-747f">ORGANIZATIONAL<br>OBJECTIVES</td>
    <td class="tg-9wq8">Willing to accept a large negative<br> impact to the organization to pursue <br>opportunities that align with objectives</td>
    <td class="tg-9wq8">Willing to accept some negative impact <br>(e.g. LOW risks) to pursue opportunities<br> that align with objectives</td>
    <td class="tg-9wq8">The potential for a negative impact <br>vs objectives are given equal <br>consideration when making a decision</td>
    <td class="tg-9wq8">The potential for a negative impact vs <br>objectives are given equal consideration <br>when making a decision</td>
  </tr>
  <tr>
    <td class="tg-747f">RISK RESPONSE<br>APPROACH</td>
    <td class="tg-9wq8">All risks are acceptable as long <br>as they do not impact our legal <br>and regulatory obligations</td>
    <td class="tg-9wq8">Determine risk response options to <br>help accept or reduce risk levels<br> through internal initiatives</td>
    <td class="tg-9wq8">Risk remediation is favored over <br>risk acceptance</td>
    <td class="tg-9wq8">Risks that cannot be effectively <br>treated or transferred are avoided</td>
  </tr>
  <tr>
    <td class="tg-747f">RISK RESPONSE<br>DRIVERS</td>
    <td class="tg-9wq8">No response action required for risks <br>unless they may represent a<br>contract or regulatory violation</td>
    <td class="tg-9wq8">Risk response actions take into <br>consideration cost effectiveness, <br>management priorities, and return <br>on investment</td>
    <td class="tg-9wq8">Risk response actions emphasize the <br>impact to security over the impact <br>to strategic objectives </td>
    <td class="tg-9wq8">Risk response actions are always taken, <br>regardless of cost effectiveness, <br>management priorities, return on investment, <br>and overall organizational objectives</td>
  </tr>
</table>

*GitLab's Risk Appetite Matrix was formed through consideration of guidance set forth in NIST's [SP 800-39](https://csrc.nist.gov/publications/detail/sp/800-39/final) and [SP 800-30 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final).*

Scoring is performed by individuals operating in at least Senior Leadership capacity within GitLab and spans across multiple departments.

#### Translating GitLab's Security Risk Appetite to Risk Tolerance

Our risk appetite is translated to a tolerance which defines a range in which a [risk score value](#risk-factors-and-risk-scoring) is tolerable and does not require remediation or a risk acceptance, i.e., the risk response will be set to "monitor". Risk scores can range from 1 (lowest) to 30 (highest). The range is defined per Risk Appetite in the table below:

|Risk Averse|Risk Neutral|Risk Receptive|Risk Seeking|
|:---------:|:---------:|:---------:|:---------:|
|1-5|1-10|1-18|1-26|

Risk scores above 26 are considered too risky to be considered within tolerance for any risk appetite.

#### Historical and Current Record of GitLab's Security Risk Appetite

|Fiscal Year|Departments|Risk Appetite|
|:-----:|----------|:-----:|
|FY24|All Departments|Risk Neutral|
|FY23|Engineering, Finance, and Legal|Risk Neutral|
|FY22|E-group, Engineering, Finance, and Legal|Risk Neutral|
|FY21|Engineering, Finance, and Legal|Risk Neutral|

### Risk Identification

#### Communication of Risks to the Security Risk Team

There are multiple ways the team can be engaged for risk:

1. (**Preferred**) If the risk was identified outside of a GitLab issue or MR or is extremely sensitive and requires some discretion, team members can do the following:
   - Join the `#security-risk-management` Slack channel
   - Execute the `Risk Escalation` workflow by clicking on the blue lightning bolt in the bottom right corner of the message box and selecting `Risk Escalation`
   - Fill out the form presented in Slack and submit
   - The Security Risk Team will intake and triage the risk and will follow-up if needed
   - **Note that Slack will not post the details that are entered into the form to the public channel**
1. If the risk is identified within an issue, team members can tag the team directly by @ mentioning `@gitlab-com/gl-security/security-assurance/security-risk-team` on the issue or MR
1. Submit a [Risk Escalation issue](https://gitlab.com/gitlab-com/gl-security/security-assurance/security-risk-team/storm/-/issues/new?issuable_template=risk-escalation) on the StORM Repo.

When documenting risks, team members can leverage [Observation Description guidance]({{< ref "observation-management-procedure#drafting-observation-description-guidance" >}}) for existing issues/observations or [risk drafting guidance](#risk-drafting-guidance).

#### Risks identified during risk assessments

The Security Risk Team may interview/survey GitLab team members operating in a leadership capacity at GitLab in order to identify security operational risks. Risks identified will always be framed in terms of threat sources and threat events, and then assessed against the likelihood of occurrence and the impact to GitLab if the risk event occurs. Additionally, these risks will be assessed against the current internal controls in place to determine the overall residual risk remaining.

In order to effectively identify, manage, and treat operational risks, GitLab has defined a set of threat source categories alongside specific risk factors and risk scoring definitions. Based on these threat sources, various stakeholders across the organization will be identified to participate in the Risk Identification phase. The identification of threat sources and events in relation to operational risks includes multiple considerations. These threat sources and events have been identified based on their potential to have an impact on mission critical objectives in relation to GitLab's operations.

#### Example Threat Sources and Events Considered

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-cly1{text-align:left;vertical-align:middle}
.tg .tg-wa1i{font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-clye{background-color:#380d75;color:#ffffff;font-weight:bold;text-align:center;vertical-align:middle}
</style>
<table class="tg">
  <tr>
    <th class="tg-clye">Threat Source</th>
    <th class="tg-clye">Example Threat Events</th>
  </tr>
  <tr>
    <td class="tg-wa1i">Adversarial</td>
    <td class="tg-cly1">Fraud and theft, insider threat, malicious hacker, and malicious code</td>
  </tr>
  <tr>
    <td class="tg-wa1i">Non-Adversarial</td>
    <td class="tg-cly1">Errors and omission, loss of physical and infrastructure support (e.g. a natural disaster), exposure of sensitive information, changes to systems used to support the business, changes to external environments supporting GitLab, changes to GitLab's business model, or even changes in leadership</td>
  </tr>
</table>

#### Risk Drafting Guidance

StORM Program considerations include both risks (what might happen) and observations (what has happened/non-compliance). For guidance on writing observations, please refer to [Observation Management Procedure Handbook page]({{< ref "observation-management-procedure" >}}).

When drafting a risk, start with a risk statement. This will represent the title of the Risk in our GRC system and is an attempt to condense the risk into a single sentence. In the spirit of [low-context communication]({{< ref "shared-reality#low-context-communication" >}}), avoid using single words or short phrases for the risk statement (e.g., Supply Chain). As we largely deal with negative risks (vs. positive risks/opportunities), starting the statement with negative language like "Failure to", "Inadequate", "Incomplete", "Lack of", etc. is appropriate, but not required. As risks represent what might happen, use "may" before describing the negative effect it *may* have on the confidentiality, integrity, availability, security, and privacy of GitLab data. Example: *Inadequate physical security controls may result in the loss of GitLab/Customer data and physical assets.* The risk description should contain details related to the assets/resources at risk, the event that may occur, the source that would trigger the event (root cause), and the consequence (impact/loss) [source](https://www.srmam.com/post/how-to-write-a-risk-statement).

#### Risk Factors and Risk Scoring

Risk rating/scoring is a favorite topic of risk management/decision support practicioners and [thought](https://hubbardresearch.com/risk-management-modeling/)-[leaders](https://normanmarks.wordpress.com/2022/07/31/risk-assessment-danger/). Scores are subjective and can be influenced by [unconscious biases](https://about.gitlab.com/company/culture/inclusion/unconscious-bias/) of those applying the scores. To help mitigate this risk, we report on risks and request feedback from management to help calibrate and ensure alignment on our highest priorities.

To score each risks, we leverage a formula based on the Likelihood of the risk event occurring and the Impact to GitLab if the event occurred. Likelihood and Impact scores directly determine the overall inherent risk to GitLab.

##### Determining Likelihood of initiation of a threat event

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-cly1{text-align:left;vertical-align:middle}
.tg .tg-nc7u{background-color:#d9ead3;text-align:center;vertical-align:middle}
.tg .tg-clye{font-weight:bold;background-color:#380d75;color:#ffffff;text-align:center;vertical-align:middle}
.tg .tg-f6g8{background-color:#fce5cd;text-align:center;vertical-align:middle}
.tg .tg-nrix{text-align:center;vertical-align:middle}
.tg .tg-28x2{background-color:#ffcccc;text-align:center;vertical-align:middle}
</style>
<table class="tg">
  <tr>
    <th class="tg-clye">Qualitative <br>Score</th>
    <th class="tg-clye">Risk Level</th>
    <th class="tg-clye">Scoring Guidelines</th>
  </tr>
  <tr>
    <td class="tg-nrix">6</td>
    <td class="tg-28x2">CRITICAL</td>
    <td class="tg-cly1">No expertise required to initiate a threat event</td>
  </tr>
  <tr>
    <td class="tg-nrix">5</td>
    <td class="tg-28x2">VERY HIGH</td>
    <td class="tg-cly1">Low level of expertise required to initiate a threat event</td>
  </tr>
  <tr>
    <td class="tg-nrix">4</td>
    <td class="tg-28x2">HIGH</td>
    <td class="tg-cly1">Some expertise required to initiate a threat event</td>
  </tr>
  <tr>
    <td class="tg-nrix">3</td>
    <td class="tg-f6g8">MODERATE</td>
    <td class="tg-cly1">Difficult to initiate a threat event, even with expertise</td>
  </tr>
  <tr>
    <td class="tg-nrix">2</td>
    <td class="tg-nc7u">LOW</td>
    <td class="tg-cly1">Requires significant expertise to initiate a threat event</td>
  </tr>
  <tr>
    <td class="tg-nrix">1</td>
    <td class="tg-nc7u">VERY LOW</td>
    <td class="tg-cly1">Theoretically impossible to initiate a threat event.</td>
  </tr>
</table>

##### Determining the impact of a threat event

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-lboi{border-color:inherit;text-align:left;vertical-align:middle}
.tg .tg-6c9p{background-color:#d9ead3;border-color:inherit;text-align:center;vertical-align:middle}
.tg .tg-22ff{font-weight:bold;background-color:#6e49cb;color:#ffffff;border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-1mkn{font-weight:bold;background-color:#380d75;color:#ffffff;border-color:#000000;text-align:center;vertical-align:middle}
.tg .tg-747f{font-weight:bold;background-color:#6e49cb;color:#ffffff;border-color:inherit;text-align:center;vertical-align:middle}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-oej3{background-color:#fce5cd;border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-sy71{background-color:#ffcccc;border-color:inherit;text-align:center;vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-1mkn" rowspan="2">IMPACT<br>SCORE</th>
    <th class="tg-1mkn" colspan="6">IMPACT AREAS</th>
  </tr>
  <tr>
    <td class="tg-747f">Organizational Output <br>(time, quality, resources)</td>
    <td class="tg-747f">Brand<br>Reputation</td>
    <td class="tg-22ff">Business<br>Continuity</td>
    <td class="tg-22ff">Customers &amp;<br>Stakeholders</td>
    <td class="tg-22ff">Legal &amp;<br>Regulatory</td>
    <td class="tg-22ff">Financial</td>
  </tr>
  <tr>
    <td class="tg-6c9p">VERY LOW (1)</td>
    <td class="tg-lboi">Organizational output is <br>impacted by less than 20%</td>
    <td class="tg-lboi">Limited to reputational damage <br>with no more than one customer <br>within a fiscal period</td>
    <td class="tg-0pky">Outages of non-critical systems <br>that impact GitLab team members</td>
    <td class="tg-0pky">Impact is limited to one <br>customer and/or stakeholder</td>
    <td class="tg-0pky">Breach of company policy <br>occurring once in a fiscal <br>period</td>
    <td class="tg-0pky">Loss up to $999</td>
  </tr>
  <tr>
    <td class="tg-6c9p">LOW (2)</td>
    <td class="tg-lboi">Organizational output is <br>impacted by 30% - 40%</td>
    <td class="tg-lboi">Confined to a limited number of <br>parties (e.g. specific customers) <br>and not publicized</td>
    <td class="tg-0pky">Outages which result in the inability <br>of GitLab to continue sales and finance <br>operations longer than 72+ hours</td>
    <td class="tg-0pky">Impact is limited to 2-3 <br>customers and/or stakeholders</td>
    <td class="tg-0pky">Breach of company policy <br>twice within a fiscal period</td>
    <td class="tg-0pky">Loss between $1,000 <br>and $9,999</td>
  </tr>
  <tr>
    <td class="tg-oej3">MODERATE (3)</td>
    <td class="tg-0pky">Organizational output is <br>impacted by 40% - 50%</td>
    <td class="tg-0pky">Public domain publicity but limited <br>to industry channels and not the <br>broader public</td>
    <td class="tg-0pky">Outages that impact GitLab's <br>ability to do business across 3+ <br>departments</td>
    <td class="tg-0pky">Impact is limited to 4-5 <br>customers and/or stakeholders</td>
    <td class="tg-0pky">Breach of a regulatory and/or <br>contractual obligation</td>
    <td class="tg-0pky">Loss between $10,000 <br>and $499,999</td>
  </tr>
  <tr>
    <td class="tg-sy71">HIGH (4)</td>
    <td class="tg-0pky">Organizational output is <br>impacted by 50% - 75%</td>
    <td class="tg-0pky">Wide-spread publicity but limited <br>parties are impacted</td>
    <td class="tg-0pky">Outages that result in the loss of <br>availability of GitLab for customers <br>for less than 4 hours</td>
    <td class="tg-0pky">Major impact to many <br>customers and/or stakeholders</td>
    <td class="tg-0pky">Regulatory censure and/or action <br>taken against GitLab</td>
    <td class="tg-0pky">Loss between $500,000 <br>and $999,999</td>
  </tr>
  <tr>
    <td class="tg-sy71">VERY HIGH (5)</td>
    <td class="tg-0pky">Organizational output is <br>impacted by 75% or more</td>
    <td class="tg-0pky">Widely publicized</td>
    <td class="tg-0pky">Outages that result in the loss of <br>availability of GitLab for customers <br>for 4+ hours</td>
    <td class="tg-0pky">Major impact to all <br>customers and/or stakeholders</td>
    <td class="tg-0pky">Public regulatory fines and/or major <br>litigation against GitLab</td>
    <td class="tg-0pky">Loss of $1,000,000+</td>
  </tr>
</table>

To arrive at a final impact score, the impact score of all impact categories is averaged.

#### Determining Inherent Risk vs Residual Risk

- Inherent Risk is the risk *before* considering any existing mitigations in place, such as existing controls, internal processes/procedures, etc. and is determined by the following formula:
   > `Inherent Risk = Likelihood x Impact`

- Residual risk is calculated in the same manner as inherent risk, but the likelihood and impact is reassessed based on the known existing controls, processes/procedures, etc. that reduce/mitigate the risk.

#### Determining if a risk is considered Low, Medium, or High

Once the Inherent and Residual risk score is determined, the following table can be used to determine if a risk is considered Low, Medium, or High:

|Risk Rating|Risk Score Range|
|:---------:|:--------------:|
|Low|1-10|
|Medium|11-20|
|High|21-30|

These ratings represent labels for communication purposes rather than what is or is not acceptable. To determine what is an acceptable risk, please refer to [risk tolerances](#translating-gitlabs-security-risk-appetite-to-risk-tolerance).

#### The Impact of Control Health & Effectiveness Rating (CHER) on Risks

In some cases where controls are identified that mitigate a risk, the Security Risk Team considers the CHER of the control that is established based on continuous monitoring performed by the Security Compliance Team. For details on how the Security Compliance Team rates observations, refer to the [Observation Management]({{< ref "observation-management-procedure" >}}) handbook page.

Given that the scope of the StORM program is limited to Tier 2 Operational Risks, any information system level risks (i.e. Tier 3) identified within the organization are typically not included as part of the StORM program as Tier 3 risks should be addressed by one or more internal controls. However, should a control have a high CHER rating, this may be an indicator of a larger risk. Because of this, there are opportunities for Tier 3 risks to escalate to Tier 2 risks. The decision to escalate a Tier 3 risk in this manner will be documented within the Risk Details.

#### Ad-hoc Risk Identification and Assessment

There may be times that risks are identified outside of traditional risk assessments - such as risks that arise from a security incident, risk identified through regular day-to-day business operations, etc. All security operational risks identified ad-hoc are discussed with the Security Risk Team, an inherent risk score is assigned, and a qualitative analysis done to determine if it should be escalated to the risk register.

### Risk Response

For each risk identified, a formal risk response decision is made to determine how GitLab will handle the risk. As part of the risk response procedures, the Risk Owner will make a determination on whether or not to accept a risk or pursue remediation based on our [Risk Appetite and Tolerances](#establishing-risk-appetite-and-tolerance). Treatment plans will be reviewed by the Security Risk Manager or delegate and approval captured via comment in the GRC application or associated GitLab issue.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-cly1{text-align:left;vertical-align:middle}
.tg .tg-wa1i{font-weight:bold;text-align:center;vertical-align:middle}
.tg .tg-clye{font-weight:bold;background-color:#380d75;color:#ffffff;text-align:center;vertical-align:middle}
</style>
<table class="tg">
  <tr>
    <th class="tg-clye">RESPONSE<br>OPTION</th>
    <th class="tg-clye">DEFINITION</th>
  </tr>
  <tr>
    <td class="tg-wa1i">Monitor (do nothing)</td>
    <td class="tg-cly1">The risk score falls within our <a href="#translating-gitlabs-security-risk-appetite-to-risk-tolerance">risk tolerance levels</a>  and no additional actions are required at this time. Risks that have been treated, resulting in a risk score that is within the risk tolerance level will be given the status of Monitor within our GRC system.</td>
  </tr>
  <tr>
    <td class="tg-wa1i">Remediate the Risk</td>
    <td class="tg-cly1">The risk is not within our risk tolerance. Complete a risk remediation plan to remediate the risk through: Sharing the risk (identify and implement solutions to share the risk with other parties), Reducing the likelihood of occurrence, and/or Reducing the level of impact to GitLab</td>
  </tr>
  <tr>
    <td class="tg-wa1i">Accept the Risk</td>
    <td class="tg-cly1">The risk is not within our risk tolerance. Accept or take the risk without executing a remediation plan because the cost to pursue remediation is higher than the potential benefit.</td>
  </tr>
</table>

The risk object in the GRC application will be updated to reflect the agreed upon risk response. If "Remediate the Risk" is selected, the Risk Owner will execute a Risk Treatment Plan. The documented plan and status of the risk treatment will be captured within the GRC application as well. See below for more information about risk response options.

#### Monitor (nothing beyond expected [iteration]({{< ref "values#iteration" >}}))

In the cases where a risk owner has concluded that a risk is within [tolerance](#translating-gitlabs-security-risk-appetite-to-risk-tolerance), no additional action is required besides ensuring that the StORM Program DRI agrees with the treatment option.

#### Remediate the Risk

When choosing to remediate the risk, a specific path must be selected:
- Remediate by reducing the likelihood that the risk could occur
- Remediate by reducing the impact to GitLab if the risk occurs
- Remediate by sharing or transferring the risk with a third party
- Remediate by avoiding the risk by deciding not to start or continue with the activity that gives rise to the risk

Once a path is selected, the Risk Owner is required to provide a [SMART](https://en.wikipedia.org/wiki/SMART_criteria), detailed plan that includes milestones and due dates for working towards risk remediation. The treatment plan must be achievable and address the root cause of the risk event. Additionally and in alignment with our value of [Transparency]({{< ref "values#transparency" >}}), each treatment plan will include a step for documenting the results/outcome of the remediation within the Handbook. If the result of the remediation is considered [not public]({{< ref "values#not-public" >}}) and cannot be documented within the Handbook, it should be documented within our Internal Handbook or an internal runbook. The Security Risk Team will leverage these risk treatment plans to track the status of risk remediation.

If the risk treatment plan is executed and results in a downgrading of the residual risk level for the risk (e.g., the residual risk level goes from High to Moderate), validation of the remediation will be performed and captured within the associated risk object in ZenGRC. Quality review of the downgrade support documentation will be completed by the Security Risk Manager and captured via comment in the GRC application.

#### Accept the Risk

In the cases where a risk owner has opted to pursue a risk acceptance, the following approvals will be required based on risk rating that was assigned to the risk undergoing a risk acceptance:

|Risk Level|Approval Level Required|
|-----|-----|
|HIGH|Risk Owner + Director/VP Level Approval* + E-group Level Approval|
|MODERATE|Risk Owner + Director/VP Level Approval*|

- `*` If the Risk Owner is a Director/VP, no additional Director/VP level approval is required

By accepting the risk, the Risk Owner and risk acceptance approvers (if separate from Risk Owner), agree to reassess the risk on an annual basis to determine whether risk acceptance is the best response option for the respective risk. If risk acceptance is appropriate based on the annual assessment, approvals will be re-obtained based on the risk and approval requirements noted in the table above. Additionally, the Risk Owner will be on point for remediation in the event the risk is realized or risk acceptance is no longer appropriate.

### Risk Tracking and Reporting

Identified risks are formally tracked via an internal risk register. Given the nature of the sensitivity of this information in aggregate, the risk register is [not made public]({{< ref "confidentiality-levels#not-public" >}}), and is not distributed externally. However, a publicly viewable GitLab Risk Register Template is available [here](https://docs.google.com/spreadsheets/d/1Lvn-ZjPNcZ-QMh-pkC6HqjwR-acUf70V9w2pquhRmH0/edit?usp=sharing) for those interested in getting some more insight into the type of information tracked in GitLab's risk register. StORM-related risk activities are centralized within GitLab's GRC tool, ZenGRC. Additional information on the various risk-related activities carried out of ZenGRC can be found on the [ZenGRC Activities]({{< ref "zg-activities#risk-activities" >}}) handbook page.

Historically, we've produced an annual report to summarize our current StORM landscape including new potential risks, updates on our highest risks to support decision-making, and recommendations on actions to take to help mitigate existing risks. Starting in FY24 we will producing a quarterly report in alignment with our values. The template we've used can be found [here](https://docs.google.com/presentation/d/1uwz8sKnf9sWY9Of_GKPtIU2dDa3i6k6xekZENPW41NY/edit?usp=sharing) for reference.

#### StORM Reporting Schedule

The table below outlines planned/completed activities for FY24.

|Timing|Activities|
|-----|-----|
|Q2|Establish FY24 Risk Appetite and release Annual Risk Assessment Report|
|Q3 (September)|Quarterly report (Security Risk Quarterly) |
|Q4 (January)|Quarterly report|


## Exceptions

The only exceptions to this procedure are those risks that are out of scope (as defined above).

## References

- GitLab Handbook References:
    - [GitLab's Communication Page, Not Public Section]({{< ref "confidentiality-levels#not-public" >}})
    - [ZenGRC Activities]({{< ref "zg-activities#risk-activities" >}})
- External References
    - [NIST SP 800-30 Rev. 1](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final)
    - [ISO 31000 Risk Management Methodology](https://www.iso.org/iso-31000-risk-management.html)
