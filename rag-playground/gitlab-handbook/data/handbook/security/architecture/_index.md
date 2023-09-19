---
title: "Security Architecture"
---

<link rel="stylesheet" type="text/css" href="/stylesheets/biztech.css" />

## Overview

[Security Architects]({{< ref "/job-families/security/security-engineer#security-architect" >}}) are the
trusted security advisors of GitLab Engineering. Security Architecture is a natural extension of the
greater [Architecture](https://about.gitlab.com/handbook/engineering/architecture/) initiative at GitLab. It is the
preliminary and necessary work to build software with security considerations.

## Objectives

Security Architecture protects the organization from cyber harm, and support present and future
business needs by:

- Preventing Security from being an afterthought
- Conducting [Security Architecture reviews](#security-architecture-reviews)
- Defining [Security Architecture Principles](#security-architecture-principles)
- Aligning with our [security sub-departments requirements and expectations](#security-architecture-requirements)
- Assisting other departments in the design and architect of new features, services, products.
- Identifying the right SMEs and DRIs on the security side
- Driving security initiatives and features

The process is designed with these constraints in mind:

- aligned with our [values]({{< ref "values" >}})
- asynchronous
- [self-service](https://about.gitlab.com/company/culture/all-remote/self-service/) as much as possible
- avoid being a bottleneck in the software development life cycle
- deliberately simple and concise
- automated as much as possible
- DRY with strong notes

## Scope of Security Architecture

Any change in our product offering (whether it is a feature, a service, or an acquisition), that
would impact our security posture. Our security posture is defined by:

- the components we build upon
- the components we embed
- everything infrastructure
- 3rd party services
- software architecture
- reference architectures

## Security Architecture Requirements

### Application Security

The Application Security team provides guidelines and requirements to follow during all the life
cycle of source code:

- [AppSec projects policies]

[AppSec projects policies]: {{< ref "../security-engineering/application-security/inventory#policies" >}}

### InfraSec

<!-- Using this page until infrasec requirements are in the handbook -->

- [Security Requirements for Development and Deployment]

[Security Requirements for Development and Deployment]: {{< ref "security-development-deployment-requirements" >}}

### Compliance

- [GitLab Audit Logging Policy]

[GitLab Audit Logging Policy]: {{< ref "audit-logging-policy" >}}

### Cryptography

- [Do not roll your own crypto] (also one of our [Security Architecture Principles](#security-architecture-principles)
)
- Reference our [GitLab Cryptography Standard]({{< ref "cryptographic-standard" >}})

<!-- Add FIPS and FedRamp requirements here when available -->

[Do not roll your own crypto]: {{< ref "encryption-policy#rolling-your-own-crypto" >}}

## Security Architecture Principles

The Security Architecture Principles are not requirements nor decisions, but something in between.

Our principles are based on two simple pillars:

1. **Least privilege**
1. **Network isolation**

They are detailed below with the principles taken from the book Software Systems Architecture (see
[references](#references)) and this [ACCU 2019 related
video](https://www.youtube.com/watch?v=YbjoaMN67Hw). These are very close to the [OWASP Security
Design Principles] but are easier to understand and apply.

[OWASP Security Design Principles]: https://github.com/OWASP/DevGuide/blob/master/02-Design/01-Principles%20of%20Security%20Engineering.md

<style>
.security-architecture-principle {
  display: inline-block;
}
</style>

<details>
<summary>

### Assign the least privilege possible{.security-architecture-principle}

</summary>

#### Why

Broad privileges allow malicious or accidental access to protected resources.

#### How

- Give only the minimum level of access rights (privileges) that is necessary to a user or service
  to complete an assigned operation. This right must be given only for a minimum amount of time that
  is necessary to complete the operation.
- Do not use administrative accounts for application access
- Use separate accounts for sensitive data

#### Examples

- Run service processes as their own users with exactly the set of privileges they require
- Grant read-only permissions when no updates are required
- When updates are required, limit to the scope to the target resource only

#### Links

- <https://owasp.org/www-community/Access_Control#principle-of-least-privilege>
- <https://csrc.nist.gov/glossary/term/least_privilege>
- <https://about.gitlab.com/handbook/security/access-management-policy.html#principle-of-least-privilege>

</details>

<details>
<summary>

### Separate responsibilities{.security-architecture-principle}

</summary>

#### Why

Limit the blast radius of successful attacks: When one part of the system is compromised, the whole
system is not.

Make attacks less attractive.

#### How

- Compartmentalize responsibilities and privileges
- Separation of duties: the successful completion of a single task is dependent upon two or more
  conditions
- Don't store secrets along with other non-sensitive data (like settings), even if secrets are
  filtered out

#### Examples

- A system/service that only needs to read git commits should not be able to access user data
- GitLab team members don't have access to billing data, nor anything else [classified red data]

[classified red data]: {{< ref "data-classification-standard" >}}

#### Links

- [OWASP Access Control
  Models](https://owasp.org/www-community/Access_Control#access-control-models)
- <https://en.wikipedia.org/wiki/Compartmentalization_%28information_security%29>

</details>

<details>
<summary>

### Trust cautiously{.security-architecture-principle}

</summary>

#### Why

- Many security problems caused by inserting malicious intermediaries in communication path

#### How

- Assume unknown entities are untrusted
- Have a clear process to establish trust
- Validate who or what is connecting
- Always use a kind of authentication (certificate, password, ...)
- Network controls
- Do not dynamically load 3rd party code

#### Examples

- Services can't be considered as secure as soon as they are not exposed to the Internet.
  [SSRF](https://en.wikipedia.org/wiki/Server-side_request_forgery) can let attackers freely access
  them.
- The best way to authenticate users is to apply this general security principle: Provide something
  you know (ex: password), and something you own (ex: certificate). This is what we apply with MFA,
  for example by providing a password you know, along with a
  [TOTP](https://en.wikipedia.org/wiki/Time-based_one-time_password) that is generated by an
  application.
- Downloading 3rd party libraries or scripts at runtime can lead to many security issues, including
  cache poisoning, XSS, and whatnot. Without checking the integrity of the external asset, malicious
  actors can tamper the files, like this example of [BGP
  Hijacking](https://medium.com/s2wblog/post-mortem-of-klayswap-incident-through-bgp-hijacking-en-3ed7e33de600)

#### Links

- [Zero Trust]({{< ref "../_index.md#zero-trust" >}}) at GitLab

</details>

<details>
<summary>

### Simplest solution possible{.security-architecture-principle}

</summary>

#### Why

- Simple solutions are easier to deploy, maintain, and secure
- Aligned with our [Iteration] and [Efficiency] values
- Security requires understanding of the design
- Complexity increases exponentially
- Attack-ability or attack surface of the software is reduced

[Iteration]: {{< ref "values#iteration" >}}
[Efficiency]: {{< ref "values#efficiency" >}}

#### How

- Avoid complex failure modes, implicit behaviours, unnecessary features
- Use well-known, tested, and proven components
- Avoid over-engineering and strive for [MVCs] instead

[MVCs]: https://about.gitlab.com/handbook/product/product-principles/#the-minimal-viable-change-mvc

#### Examples

- Introducing a new server in GitLab means updating Omnibus builds, Helm charts, our reference
  architectures, our docs, and so on. This is something to balance carefully against the benefits of
  adding a component which seem to be a perfect fit.

#### Links

- [Keep it simple, stupid](https://en.wikipedia.org/wiki/KISS_principle)
- [Complexity and exponential
  change](https://nextconf.eu/2020/02/complexity-and-exponential-change/)

</details>

<details>
<summary>

### Audit sensitive events{.security-architecture-principle}

</summary>

#### Why

- Provide record of activity
- Deter wrong doing
- Provide a log to construct that past
- Provide a monitoring point

#### How

- Record all security significant events in a tamper-resistant store
- Provide notifications for all sensitive events

#### Examples

- Enable [GuardDuty] in AWS or [Cloud Audit Logs] in GCP to record activity and detect malicious
  intent.
- Leverage [Panther] (for gitlab.com only) to collect, normalize, and analyze logs.
- Provide notifications to users when:
  - Changes to their accounts
  - New keys generated or added to their accounts
- Generate security events (could be Slack notifications) for unusual activity:
  - Signal passing a threshold (rate limiting in action)
  - Component signature not matching
  - Unauthorized access to sensitive resources

[GuardDuty]: https://aws.amazon.com/guardduty/
[Cloud Audit Logs]: https://cloud.google.com/logging/docs/audit?hl=en
[Panther]: /handbook/business-technology/tech-stack/#panther

#### Links

</details>

<details>
<summary>

### Fail securely & use secure defaults{.security-architecture-principle}

</summary>

#### Why

- Default passwords, ports and rules are "open doors"
- Failure and restart states often default to "insecure"

#### How

- Force changes to security sensitive parameters
- Think through failures - to be secure but recoverable
- Unless a subject is given explicit access to an object, it should be denied access to that object,
aka Fail Safe Defaults.

#### Examples

- Do not trust invalid/expired TLS certificates
- Some components like Grafana come with a [default `admin/admin`
  user/password](https://grafana.com/docs/grafana/v7.5/administration/configuration/#security).
- Related to above, some components might fail over to a plain user/password authentication (with
  default credentials) under certain conditions, like a service not reachable.
- Some frameworks tend to render error pages with details that should not be shared, like hostnames
  and paths, when they cannot connect to some resources.

#### Links

- https://owasp.org/www-community/Fail_securely

</details>

<details>
<summary>

### Never rely upon obscurity{.security-architecture-principle}

</summary>

#### Why

- Hiding things is difficult, someone is going to find them, accidentally or on purpose
- We're a very [transparent]({{< ref "values#transparency" >}}) company and are more likely to share
  implementation details, sometimes leaking something sensitive.
- Offboarded employees leave with sensitive knowledge. While tokens can be rotated, we can't ensure
  this knowledge won't leak

#### How

- Assume attacker with perfect knowledge

#### Examples

- Recon can help attackers find servers that are not publicly documented. These servers could expose
  vulnerable components, and lead to east-west movement.
- Changing the path to a admin section won't prevent attackers from finding it eventually.

#### Links

- <https://securitytrails.com/blog/security-through-obscurity>

</details>

<details>
<summary>

### Implement defense in depth{.security-architecture-principle}

</summary>

#### Why

- Systems do get attacked, breaches do happen, mistakes are made
- Minimize blast radius: One component compromised should not compromise the whole system
- Prevent [SSRF](https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/)

#### How

- Don't rely on a single point/layer of security:
  - Secure every level
  - Stop failures at one level propagating
- [Encrypt data at rest] and [in transit]
- Use vulnerability scanners
- Close unnecessary ports and disable unused features

[Encrypt data at rest]: {{< ref "encryption-policy#encryption-at-rest" >}}
[in transit]: {{< ref "encryption-policy#encryption-in-transit" >}}

#### Examples

- A resource is well protected when accessed via the UI, but could be more exposed via the API.
- Accounts are locked when too many attempts, in order to avoid brute-force attacks.
- OS execution can lead to bypass all application security layers, because the execution occurs
  outside of the application.
- Unnecessary open ports and enabled features may lead to authentication bypass and other weaknesses. They increase the exposure of an application.

#### Links

- <https://en.wikipedia.org/wiki/Defense_in_depth_(computing)>
- [Zero Trust]({{< ref "../_index.md#zero-trust" >}}) at GitLab

</details>

<details>
<summary>

### Never invent security technology{.security-architecture-principle}

</summary>

#### Why

- Security technology is difficult to create, and avoiding vulnerabilities is difficult
- It takes years to secure and mature new security technologies
- They are expected to be perfect (sort of)

#### How

- [Do not roll your own crypto]
- Use well-known and proven components
- In doubt, always involve the right SMEs

#### Examples

- Do not implement SSO from scratch

#### Links

- [Rainbow tables](https://en.wikipedia.org/wiki/Rainbow_table) are used to cache the output of
  cryptographic hash functions, which can be used
  for cracking password hashes.
- [Perils of the default bcrypt cost factor](https://labs.clio.com/bcrypt-cost-factor-4ca0a9b03966):
  Even when using a famous crypto library, its configuration can lead to weaknesses.

</details>

<details>
<summary>

### Find the weakest link{.security-architecture-principle}

</summary>

#### Why

- A system is just as secure as its weakest link
- Over time, new vulnerabilities are discovered, and a component might suddenly become the new
  weak link

#### How

- [Threat model]({{< ref "../threat-modeling" >}}) the system, repeat, iterate.
- Identify central components that
  - share more privileges than the others
  - have more connections to other components
  - are entrypoints (login modules, APIs, ...)
- Run [Dependency Scanning]
- Avoid weak ciphers and algorithms
- Sometimes consider the humans (users) as the weakest link. Phishing is still widely used for a
  good reason

[Dependency Scanning]: https://docs.gitlab.com/ee/user/application_security/dependency_scanning/

#### Examples

- Some resources are very well protected in the UI, and never exposed to unauthorized users. Yet, if
  the API is not correctly implementing security controls, these resources could be passed as raw
  models without filtering sensitive data.
- Data encrypted in transit but not at rest.
- The weakest link could also be a user. Not enforcing strong passwords and MFA could lead to
  sensitive data exposure, but users can also do harmful actions without being aware of it.
- OS (system) commands often leads to bypassing most, if not all, the security controls of an
  applicaton. It is a common vector for [RCEs] and should be avoided as much as possible.

[RCEs]: https://en.wikipedia.org/wiki/Arbitrary_code_execution

#### Links

- [RCE when removing metadata with ExifTool](https://gitlab.com/gitlab-org/gitlab/-/issues/327121)
- [Log4Shell: RCE 0-day exploit found in log4j 2, a popular Java logging package](https://www.lunasec.io/docs/blog/log4j-zero-day/)

</details>

## Security Architecture reviews

As part of the [Production Readiness Process], it is highly recommended to include a Security
Architecture review.

The Security Architecture review process is detailed in this [page]({{< ref "review." >}}).

[Production Readiness Process]: https://about.gitlab.com/handbook/engineering/infrastructure/production/readiness/

## Measuring results

Security Architecture, by nature, doesn't generate measurable data, apart from the number of
architecture diagrams and reviews. While this could be used as a metric, it's only reflecting work
load, and not achievements. Instead, we are measuring success in terms of maturity.

The [OWASP SAMM] framework is currently used, but this is subject to change (see discussions in this
[issue](https://gitlab.com/gitlab-com/gl-security/security-department-meta/-/issues/1315)).

We are targeting the Maturity Level 1 for FY23-Q1, and our roadmap is discussed in this
[issue](https://gitlab.com/gitlab-com/gl-security/security-architecture/general/-/issues/8).

[OWASP SAMM]: https://owaspsamm.org/about/

## Communication channels

- **Slack**: #security-architecture
- **GitLab namespace**: <https://gitlab.com/gitlab-com/gl-security/security-architecture>

## References

- [Software Systems Architecture](https://www.viewpoints-and-perspectives.info/) (ISBN-13: 978-0321718334)
- [SABSA](https://sabsa.org/)
- [TOGAF](https://publications.opengroup.org/g21i)
- [O-ESA](https://publications.opengroup.org/g112)
- [OSA](https://www.opensecurityarchitecture.org/cms/)
- [NIST CSF](https://www.nist.gov/cyberframework)
- [CIS Critical Security Controls](https://www.cisecurity.org/controls)
- [OWASP Cyber Defense Matrix](https://owasp.org/www-project-cyber-defense-matrix/)
- [AWS Well Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [OWASP Developer Guide Reboot](https://github.com/OWASP/DevGuide)
- [Google Cloud: Optimize your system design using Architecture Framework Principles](https://cloud.google.com/blog/topics/solutions-how-tos/optimize-your-system-design-using-architecture-framework-principles)
