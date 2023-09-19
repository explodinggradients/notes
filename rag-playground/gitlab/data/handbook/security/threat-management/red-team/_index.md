---
title: "Red Team"
description: "GitLab's internal Red Team extends the objectives of penetration testing by examining the security posture of the organization and their ability to implement effective cyber defenses."
---

GitLab's internal Red Team conducts security exercises that emulate real-world threats. We do this to help assess and improve the effectiveness of the people, processes, and technologies used to keep our organization secure.

The Red Team does not perform penetration tests, and the work we do is not focused on delivering a list of vulnerabilities in a specific application or service.

Malicious actors are not constrained by the narrow focus of traditional security testing. We must take on this adversarial mindset in order to challenge our own assumptions and identify areas for improvement across our entire organization. We do this by emulating the real-world tactics, techniques, and procedures (TTPs) of threats that are most relevant to our environment.

This approach allows groups across GitLab to practice detecting and responding to threats in a controlled manner. We can then better understand our current defensive capabilities and work to improve them before we are faced with the real thing.

The Red Team operates under a predefined set of [rules of engagement]({{< ref "red-team-roe" >}}). The rules of engagement exist to inform GitLab's team members on how the team operates during engagements. It provides guidelines for determining scope, the ethics we employ during our engagements, how we collaborate as a security team, and how we escalate vulnerabilities and exploits we discover during those engagements.

Further details can be found in the [job family description]({{< ref "/job-families/security/red-team" >}}).

## What the Red Team Does

### Stealth Operations

Stealth operations are our default and preferred way of working. They provide the most realistic opportunity for GitLab to practice responding to real world attacks. During a stealth operation, only a small group of GitLab team members are aware of the details.
We call these people "trusted participants", and they help keep operations safe and productive.

Stealth operations are not a contest. If our Red Team completes an objective undetected, we can offer recommendations to improve our detections. If we trigger a response, we've validated that detection capability in a realistic scenario and allowed the team to work through the same processes they would use when responding to real-life attacks. Both of these scenarios provide valuable feedback to the organization.

These operations require [special rules]({{< ref "red-team-roe#stealth-operations" >}}). Examples of techniques we may use and those we will specifically avoid can be found in [Stealth Operation Techniques]({{< ref "red-team-roe#stealth-operation-techniques" >}}).

### Purple Team Operations

We use the term "*Purple Team*" to describe an open collaboration between our defensive security folks (aka our "Blue Team") and our offensive security folks (aka our "Red Team"). Red + Blue = Purple. When the Purple Team performs an operation, the work is visible to all GitLab team members. This includes building adversary profiles, discussing hypothetical attack and defense scenarios, and emulating attack techniques in our environment.

A stealth operation may be converted to a Purple Team operation after the Red Team has been uncovered. Or, we may plan from the beginning to conduct an operation in the Purple Team style.

You can read more about this process in [Purple Teaming at GitLab]({{< ref "purple-teaming" >}}).

### Opportunistic Attacks

Opportunistic attacks are conducted outside the context of a formalized operation. They can be done at any time, from any source IP address, and against any GitLab-managed asset without prior approval or notification.

This type of work generally involves active attacks against real GitLab systems. It should always support our primary objective to improve the security of GitLab, with a goal to provide [properly labeled recommendations](#recommendations) or merge requests that solve security issues.

Opportunistic attacks are documented in issues that are visible to all team members. We do this work to test hypotheses, prove risks, and generally pursue improvements in a manner that is less structured than a formalized operation.

If vulnerabilities are discovered, we will exploit them and work to safely demonstrate maximum impact. This may involve establishing persistence, escalating privileges, and other common attack techniques.

When immediate action is required, we will follow the standard process for [contacting security](https://about.gitlab.com/handbook/security/#-contacting-the-team). For vulnerabilities that appear wide-spread or recurring, we will create an issue inside the [Vulnerability Management issue tracker](https://gitlab.com/gitlab-com/gl-security/threatmanagement/vulnerability-management/vulnerability-management-internal/vulnerability-management-tracker/-/issues) to implement automated scanning capabilities.

We list examples of [opportunistic attack techniques]({{< ref "red-team-roe#opportunistic-attack-techniques" >}}) inside our rules of engagement.

### Research

Formalized operations and opportunistic attacks both require extensive research, and we factor that in when planning these activities.

Outside of that context, the Red Team may conduct research with an intent to provide helpful information to others in the security industry and the wider GitLab community. This includes blogs, vulnerability disclosures, conference talks, etc.

We will document our progress with any research projects inside GitLab.com. Depending on the sensitivity of the research, we may use a private project until it is ready to share.

As a Red Team, we emulate attackers. That means the information we share may be about how to attack things. We should always consider the safety of others and provide context on how people can use this information to better understand and address security risks.

## Red Team Logistics

### Red Team Operation Workflow

We maintain [public issue templates](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-public/red-team-issue-templates) for planning, executing, and reporting on Red Team operations. At the start of an operation, we open a new epic and use these templates to create issues corresponding to each stage of work.

By using these templates, everyone on the team knows where we are at and what comes next. This helps us to operate asynchornously and to iterate on our processes based on how well the templates work.

### Red Team Report Delivery

All operations end with a final report. We use an issue template which is [shared publicly here](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-public/red-team-issue-templates).

Security risks affect everyone, and it is essential to make our reports approachable and consumable to a broad audience. To achieve this, we make an effort to [use simple language]({{< ref "communication#simple-language" >}}). Our goal is to ensure that anyone in the company can understand the reports, even if they don't have a background in security.

After an operation has concluded, we will create a short video summarizing the operation, which should not exceed five minutes. We will then share the following in `#whats-happening-at-gitlab` and cross-post it in `#security`:

- A very short summary of the operation, including the video overview
- A link to the final report
- A link to the retrospective issue to solicit questions and feedback
- A disclaimer to keep the information [SAFE](https://about.gitlab.com/handbook/legal/safe-framework/#how-do-we-reinforce-safe).
- A tagged list of individual operation participants as well as the Security Incident Response Team (SIRT) as a whole for awareness since not all team members participate in an operation each time.

By doing this, we help foster a culture of security awareness throughout the organization and ensure that everyone can benefit from our work.

### Red Team Metrics

#### Recommendations

 We are currently tracking the recommendations we provide across the organization and breaking them into the following three categories:

- Detections & Alerts (using the label `RTRec::Detection`)
- Security Controls (using the label `RTRec::Control`)
- Processes and Procedures (using the label `RTRec::Process`)

This is done by opening individual issues for each recommendation generated during an operation or opportunistic attack and tagging those issues with specific labels. We can then look back and see the time and effort put into each category and how the recommendations were received and acted upon.

The following issue boards provide a consolidated view of these recommendations. Most issues will be confidential and visible only to GitLab team members:

- [Red Team Recommendations: gitlab-org](https://gitlab.com/groups/gitlab-org/-/boards/5351140)
- [Red Team Recommendations: gitlab-com](https://gitlab.com/groups/gitlab-com/-/boards/5350979)

We will not measure our team's performance based on simply counting the number of recommendations over a specific time period. Instead, we will try to understand how the recommendations ultimately impact the organization and what we can do to become a more effective Red Team.

#### MITRE ATT&CK Heatmap Coverage

We use MITRE's "[ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator)" to generate heatmaps of each completed operation. This is done automatically using CI pipelines and GitLab Pages to host the output. Each operation will have an individual heatmap, and a single combined heatmap will be generated that overlays all previous operations.

This is great way to visualize the types of attack techniques we've emulated, and to help us understand areas we should focus on in future operations.

GitLab team members can [access the application](https://red-team-dashboard-gitlab-com-gl-security-threat-6d74b7b3ac5937.gitlab.io/) as well as [the project that builds it](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-internal/automation/ci-attack-navigator).

#### Red Team Maturity Model

We use a custom maturity model to measure our progress and help guide our decisions. This is losely based on the [Capabilities Maturity Model (CMM)](https://en.wikipedia.org/wiki/Capability_Maturity_Model). Our model contains five stages of maturity, each with very specific behaviors we strive to demonstrate and states we hope to achieve.

We built this using a GitLab issue board, with each maturity level being a list and each item being an issue. We can collaborate inside the issues, discussing our progress and providing links to related issues and merge requests. As we work on specific items, we will add custom labels to indicate an item is in progress, established, or replaced by an item in a latter maturity level.

GitLab team members can view the model [here](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-internal/red-team-maturity-model).

### Red Team Technique Handover

The Red Team will develop new adversary emulation techniques on a regular basis, both during formalized operations and opportunistic attacks. For example, the Red Team may create a bot that logs into development instances and attempts to exploit a specific configuration. Once the risk has been proven and existing detection/response capabilities have been tested, it is time for the technique to be fully disclosed internally.

While this may result in product fixes or infrastructure changes, it is possible that vulnerable configurations may reappear in the environment. At this point, GitLab's [Vulnerability Management]({{< ref "/handbook/security/threat-management/vulnerability-management" >}}) group will take over any ongoing scanning required to monitor for this scenario. The Red Team will share any tools they used for the initial discovery, but Vulnerability Management will generally implement a more production-ready permanent scanning solution.

### Red Team Tooling Development

The Red Team writes a lot of code, most of which will not be used in production environments. We want to prioritize simplicity and usability when writing it. This means writing code that is easy to understand and maintain, rather than worrying about optimization or unnecessary advanced functionality.

We will generally use Python because it is widely adopted in the security industry and has a large selection of libraries that can help us quickly develop tools.

When we need to create a single portable application, such as emulated malware, we will use Go.

Other factors may influence the decision on which language to use, such as forking an existing project or a requirement to emulate a specific attack scenario.

To help ensure consistency, we have created a [project template](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-internal/templates/red-team-tooling-template) available internally. This template includes a standard set best practices for testing, building, and relasing new tools.

## Is This the Red Team?

### Why we don't answer this question

The goal of a Red Team operation is often to test our policies and procedures when reacting to an actual threat. This includes identifying suspicious activity and following the appropriate runbook to investigate and respond to that threat.

If any team member, at any time, could simply ask *"Hey, this looks suspicious. Is this our Red Team?"* then this opportunity would be lost. **Instead, all suspicious activity should be treated as potentially malicious and acted upon accordingly**.

We have private Slack channels in place where designated team members can ask the Red Team if a certain activity belongs to them. This helps us to provide realistic opportunities to practice detection and response without escalating too far. For example, we would not want an emulated attack to affect production operations or escalate to third parties.

You can read more about this process in the ["deconfliction" section]({{< ref "red-team-roe#deconfliction-process" >}}) of our rules of engagement.

### How the Red Team will respond to this question

If the Red Team is ever asked *"Is this you?"* by someone other than the designated team members mentioned above, they will respond with the following text:

> Thanks for your vigilance! Any suspicious activity should be treated as potentially malicious. If you'd like to contact security, you can follow the process here: [{{< ref "/handbook/security#contact-gitlab-security" >}}]({{< ref "/handbook/security#contact-gitlab-security" >}}).
>
> Red Team operations provide an opportunity to practice detecting and responding to real-world attacks, and revealing an operation early might mean we miss out on that opportunity. Because of this, we have a policy to neither confirm nor deny whether an activity belongs to us. You can read more about this policy here: [{{< ref ".#is-this-the-red-team" >}}]({{< ref ".#is-this-the-red-team" >}}).

### How others should respond to this question

Because we want to treat all activity as potentially malicious, anyone else receiving this question should also use a consistent response. Feel free to use your own words. The following can be a guide:

> We want to treat any suspicious activity as potentially malicious. Let's continue following our normal procedures to report and investigate this. Any Red Team operation will have controls in place to keep things from escalating too far. You can read more about this here: [{{< ref ".#is-this-the-red-team" >}}]({{< ref ".#is-this-the-red-team" >}}).

If the person receiving this question happens to be a Security Director or a trusted participant in an ongoing stealth operation, they can then use established channels to communicate with the Red Team.
