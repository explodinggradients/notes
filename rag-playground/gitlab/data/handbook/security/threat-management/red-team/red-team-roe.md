---
title: "Red Team Rules of Engagement"
---

This page outlines the general rules that apply to all work conducted by the Red Team. Individual operations may include additional rules defined during planning stages.

Please refer to [our general handbook page]({{< ref "_index.md" >}}) to learn more about our team and what we do.

## Systems in Scope

All systems managed by GitLab are in scope for all types of Red Team operations. No prior approval is required to conduct any activity that meets the rules documented on this page.

Third-party systems that are used by GitLab for official business purposes are also considered in scope, but these often require permission from the system owners. This permission will be obtained when necessary.

Team members can request that a system be excluded from our scope by [opening an issue here](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-internal/red-team-operations/-/issues/new).

## Stealth Operations

[Stealth Operations]({{< ref "_index.md#stealth-operations" >}}) are conducted without being widely announced. These operations require careful planning. We will use the same [logistics issue template](https://gitlab.com/gitlab-com/gl-security/threatmanagement/redteam/redteam-public/red-team-issue-templates/-/blob/main/.gitlab/issue_templates/02-logistics.md) used for Purple Team operations, but it will only be visible to trusted participants until the operation is disclosed.

The logistics phase will define detailed rules for each specific operation. The sections below contain general rules that apply to all stealth operations.

### Prior Approval

- Approval is required from at least one layer of SIRT leadership. This starts at the SIRT managers and goes up to the CISO.
- Approval is required from the Senior Manager of Threat Management.
- Approval is required from everyone defined as a "trusted participant" in the logistics phase.

### Deconfliction Process

- Active stealth operations will have a dedicated Slack channel where all trusted participants are invited.
- The private `#is-this-the-redteam` channel is always available for Security Directors and above to inqure about Red Team activities.
- If team members ask whether a specific activity or IoC belongs to the Red Team outside of these designated channels, we will follow the process documented in ["Is This The Red Team?"]({{< ref "_index.md#is-this-the-red-team" >}}).
- If asked in one of the designated Slack channels, the following will happen:
  - Any ongoing stealth activities will be paused until a definitive answer can be provided.
  - If it was not the Red Team, the requestor can still ask that all activities remain paused until the issue is resolved.
  - If it was the Red Team performing a stealth operation, there will be a documented plan (from the "logistics" phase) on what happens next. Some examples are:
    - The operation continues in stealth, with the trusted participant helping to ensure any escalation is in-line with the operation goals.
    - The operation is disclosed internally and continues in the open to further validate security controls and detection mechanisms. Incident response is discontinued for known Red Team activities.
    - The entire operation is not disclosed internally, but the trusted participant informs the team that a specific activity or IoC belongs to the Red Team. The systems involved are considered "virtually contained" and the Red Team relinquishes any access to those systems.
    - The operation ceases completely.
- We should always prioritize the security of the organization and the wellbeing of our team members. There may be times when we need to make a judgement call and answer these questions quickly, outside of the official channels.

### Engaging with SIRT

At GitLab, our Red Team and Blue Team have a long history of working collaboratively towards a common goal. Despite playing roles that are adversarial in nature, we want to maintain a very high level of trust and respect between the teams.

We define some specific rules below, but in general we want to remember to always be kind and compassionate in our work. If something feels like it conflicts with [GitLab's values]({{< ref "/handbook/values" >}}), we need to re-evaluate exactly what we are doing and why we are doing it.

- The Red Team will not intentionally distract or mislead SIRT using official company communication channels under the team's legitimate user accounts.
- The Red Team will make an effort to avoid triggering on-call incidents outside of normal business hours. In general, this means not conducting attack techniques during hours when it is a weekend or holiday globally.
- SIRT will not proactively monitor specific Red Team resources. If any alerts or standard incident response procedures lead to these resources, of course they may be investigated by SIRT. The intent of this rule is to avoid prematurely uncovering a Red Team operation in an unrealistic manner. These resources include:
  - Red Team members' laptops
  - Red Team's group project inside Google Cloud
  - Red Team's private projects on GitLab.com
  - Red Team's private Slack channels and direct messages

## General Safety Guidelines

The sections below outline general rules all Red Team operations.

### Team Member Privacy

As security professionals, we aim to be ethical in every engagement while maintaining the spirit of mimicking real-world attacks. We respect the privacy of the employees at GitLab and follow the guidelines mentioned in the [Employee Privacy Policy](https://about.gitlab.com/handbook/legal/privacy/employee-privacy-policy/) during our engagements.

### Critical Vulnerabilities and Exploits

The Red Team may discover and exploit vulnerabilities during an engagement. These will not always be reported immediately to SIRT, as we want to provide a realistic opportunity to detect and respond to that exploitation.

If a vulnerability is exposed that meets the following criteria, we will document the issue and follow [the process to engage SIRT]({{< ref "sec-incident-response#engaging-sirt" >}}) immediately:

- Vulnerability is exposed publicly
- Vulnerability is realistically exploitable
- Exploitation of the vulnerability would impact business operations and/or expose sensitive data

### Emergencies

Red Team operations are carefully planned to avoid impacting production systems and customer activities. However, accidents may occur and production systems may respond in an unpredictable manner.

If we ever suspect an impact to production, we will do the following:

1. Suspend any activities related to the impact
1. Immediately inform everyone defined as a "trusted participant" for the operation
1. If a security incident is required, [engage SIRT]({{< ref "sec-incident-response#engaging-sirt" >}})
1. If an infrastructure incident is required, [engage the on-call SRE](https://about.gitlab.com/handbook/engineering/infrastructure/incident-management/#reporting-an-incident)
1. Perform a proper [root cause analysis](https://about.gitlab.com/handbook/engineering/root-cause-analysis/) following resolution of the incident

## Common Techniques

This section describes techniques that are commonly used by the Red Team. These lists are not all inclusive, but are meant to provide team members reasonable expectations of things the Red Team may or may not do.

If any team members have questions or concerns about these operations, please contact us in the `#g_security_redteam` Slack channel.

### Opportunistic Attack Techniques

Techniques used in opportunistic attacks include:

- Port scanning.
- Web crawling and scraping.
- Manual or automated vulnerability scanning.
- Manual or automated exploit attempts on vulnerable software or infrastructure.
- Manual or automated attempts at abusing misconfigurations.
- Manually and programmatically querying the GitLab API.
- Accessing and cloning any public projects, issues, snippets, etc. on www.gitlab.com.
- Accessing other data intended to be open to the public, such as logging platforms.
- Attempting to log in to any publicly-exposed administrative interface with common and default credentials.
- Attempting to validate credential data such as GCP service accounts, SSH keys, and API keys found in public locations.
- Gathering open-source intelligence (OSINT) from an any source, including those not managed by GitLab.

### Stealth Operation Techniques

During a [stealth operation](#stealth-operations), the Red Team may:

- Begin an operation assuming a breach has occurred, meaning the team will have some level of access to resources that are not exposed publicly.
- Attempt to gain access to team member accounts on any GitLab-managed platform (GitLab.com, Google, Slack, Zoom, etc).
- Authenticate as any team member using credential data discovered on any GitLab-managed resource (passwords, access tokens, SSH keys, etc).
- Attempt to gain access to any resource in GitLab's cloud environments, and use those resources to escalate privileges and move laterally in the cloud.
- Exploit vulnerabilities and abuse insecure configurations in any system owned and managed by GitLab.
- Attempt digital social engineering (email, Slack, GitLab issues, etc) and attacks on the software supply chain.

If you are a team member at GitLab and suspect you have uncovered a stealth red team operation in the course of your daily work, please refer to our deconfliction process mentioned in the "[Is This Red Team?]({{< ref "_index.md/#is-this-the-red-team" >}})" section.

At this time, the Red Team **will not**:

- Attempt to gain access to team member laptops without prior consent.
- Attempt to access resources inside a GitLab team member's home (wireless networks, non-GitLab machines, etc).
- Attempt to socially engineer team members via phone calls.
- Attempt to socially engineer team members via channels not managed by GitLab (such as social networks, personal email addresses, etc).
- Attempt to gain access to anything that is not strictly work-related and managed/owned by GitLab.
