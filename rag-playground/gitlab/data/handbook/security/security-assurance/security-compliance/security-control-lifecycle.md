---
title: "GCF Security Control Lifecycle"
---

{{% alert title="This is a Controlled Document" color="danger" %}}
Inline with GitLab's regulatory obligations, changes to [controlled documents]({{< ref "controlled-document-procedure" >}}) must be approved or merged by a code owner. All contributions are welcome and encouraged.
{{% /alert %}}

## Process Overview

![Security Control Lifecycle](../control_lifecycle.png "Security Control Lifecycle")

## Purpose

As new GitLab security controls are identified that need to be implemented by the Security Compliance Teams for compliance or regulatory reasons, these controls follow an established process in order to make that implementation successful.

These lifecycle phases are managed via GitLab's governance, risk and compliance (GRC) application, [ZenGRC](https://info.reciprocitylabs.com/). If your GitLab team is interested in using ZenGRC for your risk and compliance needs, please reach out in the GitLab #sec-assurance slack channel.

## Scope

This document applies to GitLab's security controls being assessed by the Security Compliance Team.

## Roles & Responsibilities

| Role | Responsibility|
| ---- | ------ |
| GitLab Team Members | Responsible for following the requirements of the controls |
| Security Compliance Team | Responsible for execution of security control tests and maintenance of this handbook page |
| Security Compliance Management | Responsible for oversight, escalation and approval of exceptions for this process |
| Security Assurance Management (Code Owners) | Responsible for approving significant changes and exceptions to this procedure |

## Procedure

### Lifecycle Phases Explained

#### Preparation

As new [GCF security controls]({{< ref "sec-controls" >}}) are identified they first must be researched and contextualized to GitLab as a company and to the applicable GitLab systems. The Preparation phase of the control lifecycle covers this initial work required to get controls into a state of ready to be tested.

Additionally, GCF controls that have been previously tested but have an upcoming requirement for renewed testing enter this Preparation phase as well to research and confirm that any changes to the control processes are captured in the updated testing activity.

#### Testing

```mermaid
   graph TD;
   1[Test of Design]-->2[Decision: TOD Pass];
   1-->3[Decision: TOD Fail];
   3-->9[Observation];
   2-->4[Test of OE];
   4-->5[Decision: TOE Pass];
   5-->6[Operating];
   4-->7[Decision: TOE Fail];
   7-->9[Observation];
   9-->8[Remediation];
```

The testing activity consists of 3 major components:
1. Filling out a control testing worksheet as described by the [GitLab control testing manual](https://gitlab.com/gitlab-com/gl-security/security-assurance/grc-application/-/blob/master/Assessments/assessment_testing_manual.md) (GitLab internal link)
1. Validating observations (if any were noted during testing) with the observation owners
1. Recording those observations (if any) according to the [Security Compliance Observation Management process]({{< ref "observation-management-procedure" >}})
   - **Note:** These observations can only be recorded after being validated by the observation owner to ensure that observation is accurate and represents a material deficiency in the security control process

After testing a decision is made about the controls:
- Were any validated observations recorded as a part of testing?
   - If `yes` this control enters the Remediation phase while those observations are in the process of being resolved
   - If `no` this control enters the Operation phase since the control has been determined to be designed and operating effectively to meet security compliance program needs
- Assign a control effectiveness rating to the control as described in the [GitLab control testing manual](https://gitlab.com/gitlab-com/gl-security/security-assurance/grc-application/-/blob/master/Assessments/assessment_testing_manual.md) (GitLab internal link)

#### Remediation

Remediation is the phase of the lifecycle where required changed are made to the design of the security control or the process of the control's operation. Remediation is either performed by the observation owner or is tracked by the observation owner if the observation remediation is blocked by another GitLab team's work. The Security Compliance Team is responsible for tracking all validated observations and continually reporting on those observations to ensure they are tracked, prioritized appropriately, and escalated as needed to meet the security compliance program goals.

#### Operating

Controls that are tested with no observations noted during that testing activity are determined to be in an operational state. This indicates that the design and operating effectiveness of this control are at or above the level required to meet the current needs of the security compliance program.

Controls in an operating state will still need to be re-tested annually or quarterly (as determined by the risk rating of the control) to ensure no substantive changes have occured which would impact the design or operating effectiveness of that control; controls move from the operating state back into the preparation state to prepare the control for the next iteration of testing.

##### *For a listing of application/systems that are currently in-scope for Security Compliance Testing, reference [FY24 Security Compliance Audit Schedule](https://docs.google.com/spreadsheets/d/16Bd5bYG61RDw5t77_Tte8ykG4YARJa5stK2qcdm2CbI/edit#gid=0). Even though [transparency is one of our values]({{< ref "values#transparency" >}}), we are unable to share this document [publicly]({{< ref "confidentiality-levels#not-public" >}}).

## Exceptions

Exceptions to this procedure will be tracked as per the [Information Security Policy Exception Management Process]({{< ref "handbook/security#information-security-policy-exception-management-process" >}}).

## References

- [Information Security Policies]({{< ref "/handbook/security#information-security-policies" >}})
- [Controlled Document Procedure]({{< ref "controlled-document-procedure" >}})

<a href="{{< ref "../security-compliance" >}}" class="btn bg-primary text-white btn-lg">Return to the Security Compliance</a>

