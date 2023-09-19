---
title: "Access Level Wristband Colors"
description: "We provision different levels of access to systems at GitLab based on your role and user type. Our Access Level Categories, also referred to as wristband colors (BLUE, PURPLE, BROWN, BLACK), provide an easy color reference of which level of access each account has, and allows us to easily audit and manage controls and processes for each category."
---

{{< panel header="**This is a Controlled Document**" header-color="white" header-bg="danger" >}}
Inline with GitLab's regulatory obligations, changes to <a href="https://about.gitlab.com/handbook/security/controlled-document-procedure.html">controlled documents</a> must be approved or merged by a code owner. All contributions are welcome and encouraged.
{{< /panel >}}

## Purpose

We provision different levels of access to systems at GitLab based on your role and user type.

You are likely familiar with our <a href="https://about.gitlab.com/handbook/security/data-classification-standard.html">Data Classification</a> color coding of <span style="color: #dc2626;">RED</span>, <span style="color: #ea580c">ORANGE</span>, <span style="color: #ca8a04">YELLOW</span>, and <span style="color: #16a34a">GREEN</span>.

We have completed the colors of the rainbow with our <strong>Access Level Categories</strong>, also referred to as <strong>wristband colors</strong>. The color of your wristband dictates which level of access each account has, and allows us to easily audit and manage controls and processes for each category.

<strong>Never heard of these wristband colors or access levels?</strong> It is safe to assume that all of your user accounts and access are <span style="color: #9333ea;">PURPLE</span> accounts, and you likely don't need to worry about any other access levels for your own user credentials unless you have elevated or admin access. If you're not sure, please ask for assistance in <code>#it_help</code>.

## Access Level Categories

<table>
    <thead>
        <tr>
            <th>Wristband Color</th>
            <th>Access Level</th>
            <th>Audience</th>
            <th>Account ID Formats</th>
        </tr>
    </thead>
    <tbody>
        <tr>
        <td><span style="color: #ffffff; background-color: #0284c7; padding: 3px;">BLUE</span></td>
        <td>Specific apps and roles</td>
        <td><ul>
            <li>Auditors</li>
            <li>Contractors</li>
            <li>Interns</li>
            <li>Service providers</li>
            <li>Vendors</li>
        </ul></td>
        <td>
            <code>{handle}-ext@gitlab.com</code><br />
            <code>{handle}-int@gitlab.com</code><br />
            <code>{handle}@blue.gitlab.com</code><br />
        </td>
    </tr>
    <tr>
        <td><span style="color: #ffffff; background-color: #9333ea; padding: 3px;">PURPLE</span></td>
        <td><ul>
            <li>Baseline entitlements</li>
            <li>Job role entitlements</li>
            <li>Access requests</li>
        </ul></td>
        <td><ul>
            <li><a href="https://about.gitlab.com/handbook/people-group/employment-solutions/#team-member-types-at-gitlab">Team members</a></li>
        </ul></td>
        <td>
            <code>{handle}@gitlab.com</code><br />
        </td>
    </tr>
    <tr>
        <td><span style="color: #808080; background-color: #3f3f46; padding: 3px;">GRAY</span></td>
        <td>
            Secondary account
        </td>
        <td><ul>
            <li>Certain SFDC Users</li>
            <li>Different permission/role level (non-admin) accounts</li>
            <li>Test user accounts</li>
        </ul></td>
        <td>
            <code>{handle}+sfdc2@gitlab.com</code><br />
            <code>{handle}+{role}@gitlab.com</code><br />
            <code>{handle}+test@gitlab.com</code><br />
            <code>{handle}+test-{purpose}@gitlab.com</code><br />
        </td>
    </tr>
    <tr>
        <td><span style="color: #ffffff; background-color: #854d0e; padding: 3px;">BROWN</span></td>
        <td>Specific app role(s) and permissions</td>
        <td><ul>
            <li>API Tokens</li>
            <li>Bots</li>
            <li>Service Accounts</li>
        </ul></td>
        <td>
            <code>service-{handle}@gitlab.com</code><br />
            <code>svc-{handle}@gitlab.com</code><br />
            <code>{handle}-service@gitlab.com</code><br />
            <code>{handle}@brown.gitlab.com</code><br />
            <small style="background-color: #e5e7eb; padding: 3px">Usually provisioned as a Google Group mailing list</small><br />
        </td>
    </tr>
    <tr>
        <td><span style="color: #ffffff; background-color: #1f2937; padding: 3px;">BLACK</span></td>
        <td>Admin, Elevated, Root</td>
        <td><ul>
            <li>Audit and Compliance Team Members (Read Only)</li>
            <li>Infrastructure Team Members</li>
            <li>IT Team Members</li>
            <li>Security Team Members</li>
            <li><a href="https://about.gitlab.com/handbook/business-technology/#cross-department-system-owners">Critical Tier System Owners</a></li>
        </ul></td>
        <td>
            <code>{handle}-admin@gitlab.com</code><br />
        </td>
    </tr>
</tbody>
</table>

### BLUE

A <span style="color: #0284c7">BLUE</span> account is any human user that is not classified in the <a href="https://about.gitlab.com/handbook/people-group/employment-solutions/#team-member-types-at-gitlab">Team Member Types</a>. We only provide access to the applications and specific roles needed to based on job responsibilities (usually related to the scope of work for the contract).

See the <a href="https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/temporary-service-providers/">Temporary Service Provider</a> handbook page to learn more.

### PURPLE

When a <a href="https://about.gitlab.com/handbook/people-group/employment-solutions/#team-member-types-at-gitlab">team member</a> joins GitLab, there are several systems that are provisioned as part of the normal onboarding process including Okta, Google Workspace (ex. Gmail), and 1Password. We refer to these as your <code>PURPLE</code> wristband accounts.

Any processes and systems that use your <code>{handle}@gitlab.com</code> email address and are part of <a href="https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/access-requests/baseline-entitlements/">Baseline and Role Entitlements</a> or an access request are provisioned in your <span style="color: #9333ea">PURPLE</span> account.

For team members in Infrastructure, IT, Security, or other departments with elevated access, your elevated or admin access will usually be provisioned in your <a href="#black">BLACK Account</a>.

### GRAY

Gray accounts are secondary user accounts when required for a specific appllication function, different role, or test account.

The user must also have an active Blue or Purple account.

This is a corner case that is usually used by IT and Security team members for test accounts, or secondary accounts for Salesforce (SFDC).

### BROWN

A <span style="color: #854d0e">BROWN</span> account is for any system user that is used for API tokens, bots, service accounts, or other system related (non-human) credentials. The methodology will vary based on the system and we have a lot of legacy service accounts that may not comply with this policy. This standard is designed for new service accounts and any service accounts that get updated so we iteratively update and migrate legacy service accounts.

Most service accounts require an email address. If an Okta user account is not required, we usually create a Google Group email alias for the service account with DRI team members as members. All service account credentials are stored in a new 1Password Vault (per service) that the DRI team members for that Google Group are added to.

### BLACK

For IT Systems Engineers, IT Analysts, IT Security Engineers, Security Incident Response Team Engineers, Site Reliability Engineers, Audit/Compliance team members (read only), and other roles that require elevated or admin access to compliance in-scope or specifically identified <a href="https://about.gitlab.com/handbook/security/security-assurance/security-risk/storm-program/critical-systems.html">critical tier systems</a>, we provide an additional user account (<code>{firstInitial}{lastName}-admin@gitlab.com</code>) to securely distinguish and manage your elevated access to these systems. We refer to these as your BLACK wristband accounts. You will usually have both a <span style="color: #9333ea">PURPLE</span> and BLACK account for these systems.

Unlike your <span style="color: #9333ea;">PURPLE</span> Okta account or 1Password vault that you can access from your mobile device, your BLACK admin accounts have stricter policies and are restricted to a Chrome profile on your GitLab laptop with full separation from your normal PURPLE accounts that are stored in a separate 1Password account and vault and has YubiKey 5 FIPS MFA enforced for security and compliance reasons.

See <a href="/handbook/it/runbooks/okta/admin/onboarding">Okta Admin Account Onboarding Runbook</a> to learn more.

Please contact <a href="https://gitlab.com/jeffersonmartin">Jeff Martin</a> for questions or assistance with BLACK accounts.
