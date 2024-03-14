---
title: "Reproducible Vulnerabilities"
description: "Learn about GitLab, its security processes, and its historical security vulnerabilities"
---

## Introduction

GitLab is [transparent about the security bugs it has fixed](https://about.gitlab.com/blog/2022/02/17/how-gitlab-handles-security-bugs/). This transparency creates opportunities for learning, upskilling, and breaking into the InfoSec industry.

  - Anyone can learn how to identify and/or fix security issues in a real product.
  - AppSec job candidates and new team members get insight into the bugs we face, and our processes.

The reproducible vulnerabilities are structured with expandable hint sections so that you can adapt the content to your desired challenge level. We want it to be approachable to anyone.

If this sort of thing interests you, we encourage you to [check for open roles in our Security Team](https://about.gitlab.com/jobs/) and to [participate in our Bug Bounty program on HackerOne](https://hackerone.com/gitlab) (it pays real money!).

## Important Information & FAQ

### Warning

Installing software with known vulnerabilities carries inherent risk. Do not allow untrusted connections. Ideally run vulnerable instances locally or in a cloud environment allow-listed to your home IP only. Remove your practice instances when you have finished with them.

### Won't this page help attackers?

That is not the intent of this page. The intent of this page is to educate both team members and those in the community who are interested in learning about security.

GitLab's disclosure policy is to make patched vulnerabilities public after 30 days. See our [process for disclosing security issues]({{< ref "/handbook/security#process-for-disclosing-security-issues" >}}). These disclosed issues include steps to reproduce, often include videos or screenshots, and links to the code that patches the issue.

Disclosed vulnerabilities, including those listed here, are already publicly accessible [in our issue tracker](https://gitlab.com/groups/gitlab-org/-/issues/?sort=updated_desc&state=closed&label_name%5B%5D=bug%3A%3Avulnerability). This page will never give more assistance or more detail than already exists in those public issues.

### What if I find something odd?

If you discover a security issue that still affects current versions of GitLab, for example an incomplete fix, please follow the steps in our [Responsible Disclosure Policy](https://about.gitlab.com/security/disclosure/).

----

## Reproducible Vulnerabilities

### Stored XSS in 15.0

In GitLab 15.0 a malicious user could create a stored XSS payload. See if you can figure out how.

#### Installation

1. Follow [the steps to install a Docker version of GitLab](https://docs.gitlab.com/ee/install/docker.html). Depending on your setup, the command will look something like:

```shell
sudo docker run --detach \
  --hostname gitlab.example.com \
  --publish 8929:80 --publish 8922:22 \
  --name gitlab15.0.0 \
  --volume $GITLAB_HOME/config:/etc/gitlab \
  --volume $GITLAB_HOME/logs:/var/log/gitlab \
  --volume $GITLAB_HOME/data:/var/opt/gitlab \
  --shm-size 256m \
  gitlab/gitlab-ee:15.0.0-ee.0
```

After installation is complete you can get the `root` Administrator user password with `docker exec -it gitlab15.0.0 grep 'Password:' /etc/gitlab/initial_root_password`.

1. Register a user to be the attacker
1. Sign in as the Administrator and approve the new user. Sign out.
1. Sign in as the attacker
1. Good hunting!

#### Bug hunting

Cross-Site Scripting, or XSS, is an attack where attacker-defined javascript is injected into a page the victim is browsing. This can let an attacker impersonate a victim and click on things, submit forms, view data, watch what is typed, and more.

{{% details summary="Hint 1 - Where to start looking" %}}
This XSS vulnerability existed in our CRM feature.

> With customer relations management (CRM) you can create a record of contacts (individuals) and organizations (companies) and relate them to issues.

<https://docs.gitlab.com/ee/user/crm/>
{{% /details %}}

{{% details summary="Hint 2" %}}
One or more of the customer contact fields was susceptible to stored XSS.
{{% /details %}}

{{% details summary="Hint 3" %}}
Instead of giving a contact a real name, put some javascript in there. Can you find anywhere that fails to properly escape the javascript?
{{% /details %}}

{{% details summary="Hint 4" %}}
The contact fields pop up as previews in Issue description and comments when you use the `/add_contacts` quick action.
{{% /details %}}

{{% details summary="Just tell me how" %}}
Follow the steps to reproduce written by [cryptopone](https://hackerone.com/cryptopone) on our GitLab Issue: <https://gitlab.com/gitlab-org/gitlab/-/issues/363293>
{{% /details %}}

{{% details summary="Take it further" %}}
Once you've got a stored XSS payload executing, what can you can do?

Can you elevate your privileges to an administrator, if the victim of your XSS is an administrator?
{{% /details %}}

#### Vulnerability Details

{{% details summary="Click to expand" %}}
> An issue has been discovered in GitLab affecting all versions starting from 15.0 before 15.0.1. Missing validation of input used in quick actions allowed an attacker to exploit XSS by injecting HTML in contact details. This is a high severity issue (`CVSS:3.0/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:N`, 8.7). It is now mitigated in the latest release and is assigned [CVE-2022-1948](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1948).
>
> Thanks [cryptopone](https://hackerone.com/cryptopone) for reporting this vulnerability through our HackerOne bug bounty program.
{{% /details %}}

#### Remediation

Once you've reproduced the bug, have a go at fixing it locally.

Done that? Now compare your proposed change to our patch(es).

{{% details summary="The fix" %}}
We took multiple steps to holistically address this vulnerability:

- We escaped the first and last name in the following patch: <https://gitlab.com/gitlab-org/gitlab/-/commit/e61e9b9434e2198c4c1d5cf6b4531eb4323c3575>
- We made AppSec required approvers of subsequent changes to the affected files in <https://gitlab.com/gitlab-org/gitlab/-/merge_requests/88419>
- We added SemGrep rules to detect and comment on MRs which might introduce XSS with <https://gitlab.com/gitlab-com/gl-security/appsec/sast-custom-rules/-/blob/main/appsec-pings/rules.yml#L65-84>
{{% /details %}}

#### Links

- GitLab Issue: <https://gitlab.com/gitlab-org/gitlab/-/issues/363293>
- Patch: <https://gitlab.com/gitlab-org/gitlab/-/commit/e61e9b9434e2198c4c1d5cf6b4531eb4323c3575>
- Release Post: <https://about.gitlab.com/releases/2022/06/01/critical-security-release-gitlab-15-0-1-released>
- CVSS and Bounty: [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:N](https://gitlab-com.gitlab.io/gl-security/appsec/cvss-calculator/#vector=CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:N&range=new) (8.7 High / $13,950.00)
- CVE: <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-1948>
- Learn more about XSS:
  - <https://owasp.org/www-community/attacks/xss/>
  - <https://portswigger.net/web-security/cross-site-scripting>

### Denial of Service in 14.3.5

On GitLab installations before 14.3.6, a malicious actor could perform a Denial of Service attack by submitting crafted issues, MRs, or comments. See if you can figure out how.

#### Installation

1. Follow [the steps to install a Docker version of GitLab](https://docs.gitlab.com/ee/install/docker.html). Depending on your setup, the command will look something like:

```shell
sudo docker run --detach \
  --hostname gitlab.example.com \
  --publish 8929:80 --publish 8922:22 \
  --name gitlab14.3.5 \
  --volume $GITLAB_HOME/config:/etc/gitlab \
  --volume $GITLAB_HOME/logs:/var/log/gitlab \
  --volume $GITLAB_HOME/data:/var/opt/gitlab \
  --shm-size 256m \
  gitlab/gitlab-ee:14.3.5-ee.0
```

After installation is complete you can view the `root` user password with `docker exec -it gitlab14.3.5 grep 'Password:' /etc/gitlab/initial_root_password`. You can use this password to login to the root user on your GitLab instance.

Good hunting!

#### Bug hunting

Denial of service (DoS) attacks make websites unusable for other users. Typically this happens when a server is so busy dealing with attackers requests that it doesn't have capacity to respond to normal users.

When using GDK locally, open your CPU & Memory resource monitor and look for abnormally high and sustained usage, particularly of the `rails-web` and `rails-background-jobs` processes. If you're running GitLab in a docker container, try a tool like [`ctop`](https://github.com/bcicen/ctop#docker).

{{% details summary="Hint 1 - where to start looking" %}}
This DoS involved user content, for example issue descriptions or comments. These can be made via the user interface, or via the API.
{{% /details %}}

{{% details summary="Hint 2" %}}
This researcher found a [regex-based DoS](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS) by reading the code GitLab used to parse front-matter. <https://gitlab.com/gitlab-org/gitlab/-/blob/6f10f768c9cc2d131c056289f58519cf9cae79fa/lib/gitlab/front_matter.rb>
{{% /details %}}

{{% details summary="Hint 3" %}}
Search for a flaw called "Catastrophic Backtracking".
{{% /details %}}

{{% details summary="Hint 4" %}}
What happens when you use one of the front matter delimiters followed by content? What happens as that content grows in length? Keep an eye on your process monitor.
{{% /details %}}

{{% details summary="Just tell me how" %}}
Follow the steps to reproduce written by [hashkitten](https://hackerone.com/legit-security) on our GitLab Issue: <https://gitlab.com/gitlab-org/gitlab/-/issues/340449>
{{% /details %}}

#### Vulnerability Details

{{% details summary="Click to expand" %}}
> An issue has been discovered in GitLab CE/EE affecting all versions starting from 12.10 before 14.3.6, all versions starting from 14.4 before 14.4.4, all versions starting from 14.5 before 14.5.2. A regular expression used for handling user input (notes, comments, etc) was susceptible to catastrophic backtracking that could cause a DOS attack. This is a medium severity issue (`CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L`, 4.3). It is now mitigated in the latest release and is assigned [CVE-2021-39933](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-39933).
>
> Thanks [@hashkitten](https://hackerone.com/hashkitten?type=user) for reporting this vulnerability through our HackerOne bug bounty program.
{{% /details %}}

#### Remediation

Once you've reproduced the bug, have a go at fixing it locally. Then compare your proposed change to our patch(es).

{{% details summary="The fix" %}}
- We fixed the frontmatter regex: <https://gitlab.com/gitlab-org/gitlab/-/commit/8b30fedf2bea8713bc735638ae63a09f3e4faba1>
- We added timeouts to our rendering pipelines:
  - <https://gitlab.com/gitlab-org/gitlab/-/merge_requests/102819>
  - <https://gitlab.com/gitlab-org/gitlab/-/merge_requests/104779>
{{% /details %}}

#### Links

- GitLab Issue: <https://gitlab.com/gitlab-org/gitlab/-/issues/340449>
- Release Post: <https://about.gitlab.com/releases/2021/12/06/security-release-gitlab-14-5-2-released/#regular-expression-denial-of-service-via-user-comments>
- CVSS and Bounty: [CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L](https://gitlab-com.gitlab.io/gl-security/appsec/cvss-calculator/#vector=CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:L&range=old) (4.3 Medium / $610.00 / old bounty range)
- CVE: <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-39933>
- Learn more about Denial of Service:
  - <https://owasp.org/www-community/attacks/Denial_of_Service>

<!-- Additional reproducible vulnerabilities go above this line //-->

## Contributing

{{% alert color="danger" %}}
Contributions must only include information that is already publicly available.
{{% /alert %}}

Everyone can contribute to this page - that includes you! You can start by clicking "Open in Web IDE" in the sidebar on the right.

First, find an interesting publicly disclosed vulnerability by looking at our [public and closed vulnerability issue list](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=updated_desc&state=closed&label_name%5B%5D=bug%3A%3Avulnerability&first_page_size=20) or our [security release blog posts](https://about.gitlab.com/releases/categories/releases/). Choose a vulnerability that was fixed in any release *prior* to the latest security release.

Open a Merge Request to this page, mention `@gitlab-com/gl-security/appsec`. It should include:

- A title and non-revealing summary of the vulnerability
- Steps to install the vulnerable version
  - Ideally <https://docs.gitlab.com/ee/install/docker.html#install-gitlab-using-docker-engine> with a specific version number
  - More complex issues might require a specific installation method, like the Omnibus Linux package.
- A series of progressively revealing hints, so people can try to hunt for the bug themselves but get help if needed. (Remember GitLab is a big product!).
- A link to the GitLab issue, for those who want to follow the original HackerOne report's steps to reproduce.
- A link to the MR(s) that fixed it.

Here's a template you can use:

```markdown
### `Short title goes here`

On `Free/Premium/Ultimate` installations before `X.Y.Z`, a malicious user could `attack type`. See if you can figure out how.

#### Installation

<!--  Steps to install a vulnerable version //-->

#### Bug hunting

{{% details summary="Hint 1 - where to start looking" %}}
<!--  Something that gets people looking in the right place //-->
{{% /details %}}

{{% details summary="Hint 2" %}}
<!--  Another hint. Add as many hints as you want, using already public data. //-->
{{% /details %}}

{{% details summary="Just tell me how" %}}

Follow the steps to reproduce written by [HANDLE](https://hackerone.com/HANDLE) on our GitLab Issue: <https://gitlab.com/gitlab-org/gitlab/-/issues/XXXXXX>

{{% /details %}}

#### Vulnerability Details

{{% details summary="Click to expand" %}}

<!--  Paste the text from the security release post. Adapt if needed. //-->

{{% /details %}}

#### Remediation

Once you've reproduced the bug, have a go at fixing it locally.

Then compare your proposed change to our patch(es).

{{% details summary="The fix" %}}

<!--  Link to the patch, with optional description //-->

{{% /details %}}

#### Links

<!--  Links go here //-->

```
