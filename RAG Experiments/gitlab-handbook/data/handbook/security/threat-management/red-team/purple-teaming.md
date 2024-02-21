---
title: "Purple Teaming at GitLab"
description: "GitLab's processes for collaborative attack-emulation exercises to strengthen our organization's defensive capabilities."
---

The terms "Red Team" and "Blue Team" are used to describe the roles of attackers and defenders during planned security exercises. At GitLab, where collaboration and transparency are two of our [core values]({{< ref "values" >}}), we like to join forces and conduct what is commonly referred to as "Purple Teaming".

To us, a Purple Team operation is a planned exercise that involves team members from multiple security sub-departments in every aspect of the operation. This includes planning, attacking, detecting, and responding. We find that having more people involved from the very beginning ensures that we are all working towards a common goal.

You can contribute, comment, view, or interact with us on Slack in the `#purple-team-ops` channel where we discuss ongoing purple-team operations.

We also conduct more traditional Red Team operations, where only certain team members are aware of the details. These types of operations follow roughly the same workflow outlined below, only with less active participants.

## Goals of Purple Teaming

Purple Team operations are not penetration tests. They are not meant to deliver a list of vulnerabilities in a specific application or service. Instead, they are meant to better understand our organization's ability to detect and respond to real-world attacks. Given this deeper understanding, we can continue to strengthen these defenses based on the hands-on experience gained during *emulated* attacks, as opposed to the real thing.

At a high level, the goals of an operation generally fall into one of the following categories:

- To gauge the effectiveness of existing defensive capabilities (*Is our SIEM capable of detecting a compromised admin account?*)
- To practice and refine our procedures for responding to a breach (*Do our runbooks make sense? Can anything be automated?*)
- To understand our ability to detect and respond to a specific type of threat (*What would happen if we were targeted by a ransomware operator?*)

## Purple Team Workflow

### Overview

The diagram below shows our basic workflow for planning, executing, and completing an operation. Everyone is welcome to participate actively in all stages, but some stages are owned specifically by one group or another.

Operations will be tracked using [GitLab epics](https://docs.gitlab.com/ee/user/group/epics/). Each of the unique stages has a corresponding [issue template](https://docs.gitlab.com/ee/user/project/description_templates.html) that provides further detail on exactly what needs to be done. These templates are [shared publicly here](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-public/red-team-issue-templates).

As much as possible, our Purple Team operations should be performed [asynchronously](https://about.gitlab.com/company/culture/all-remote/asynchronous/). However, a few stages work best when done with live participants over a video conference with screen sharing. To include team members in all time zones, these stages can be conducted more than once. This is particularly beneficial when conducting the actual attacks and practicing detection. We will automate this work whenever possible, which makes repeating them easy.

![Purple Teaming Process](../purple-team-process.png)

### Attack Planning

- Brainstorming: Propose and discuss an initial idea. This might be inspired by threat intelligence, new systems or detection capabilities, or some other hypothesis requiring validation.
- Logistics: Clarify specifics like goals, roles & responsibilities, timelines, and visibility.
- Adversary Profiling: Detailed modeling of the adversary, including things like capabilities and intent, tactics/techniques/procedures (TTPs), Command & Control (C2) environment, Indicators of Compromise (IoCs), threat scenario, etc.
- Tabletop Exercise: Review the chosen TTPs and discuss the expected outcomes using Google Docs, and then log the final details inside Vectr.

### Attack Emulation

- Develop Capabilities: The Red Team will create and test the infrastructure and tooling required to execute each TTP. Whenever possible, these should be automated using either GitLab CI pipelines or MITRE Caldera.
- Emulate Attacks: Synchronous meeting to play and replay the attacks as necessary.
- Validate Detection & Response: Synchronous meeting to validate the expected outcomes. This may be run in tandem with the previous step.

### Operation Conclusion

- Deliver Final Report: Prepare and share the full report. This contains a detailed attack narrative with an attack flow diagram, a MITRE ATT&CK heatmap, Vectr diagrams on technique outcomes and tooling efficiency, and relevant observations. This is delivered via the issue itself.
- Retrospective: An asynchronous discussion on what went well, what could be improved, and what we would do differently next time around.

## Purple Team Resources

### Tools

- [Vectr](https://vectr.io/): A free, closed-source Purple Team planning and reporting tool.
- [MITRE CALDERA](https://caldera.mitre.org/): A free, open-source adversary emulation and automation tool.
- [MITRE ATT&CK Navigator](https://mitre-attack.github.io/attack-navigator/): A web application to visualize and manipulate matrices of attacker tactics and techniques.

### Training

- [Red Team Development and Operations](https://redteam.guide/): An excellent book by Joe Vest and James Tubberville.
- [Purple Teaming Execution Framework](https://github.com/scythe-io/purple-team-exercise-framework): Another great resource, this one by Scythe.
- [MITRE ATT&CK: Getting Started](https://attack.mitre.org/resources/getting-started/): A collection of resources realted to the ATT&CK framework, which is used as the foundation for much of our work.
