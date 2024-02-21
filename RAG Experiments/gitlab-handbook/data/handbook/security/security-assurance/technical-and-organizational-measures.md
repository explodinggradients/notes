---
title: "Technical and Organizational Security Measures for GitLab Cloud Services"
---

## Technical and Organizational Security Measures for GitLab Cloud Services

GitLab Cloud Services (including GitLab.com and GitLab Dedicated) meet the specific requirements of data protection, including, without limitation, Article 28 of the General Data Protection Regulation and which are listed as SOC 2 Type 2 (Security & Confidentiality).

At a minimum, GitLab has implemented for the GitLab Cloud Services the technical and organizational measures and maintains security practices within the production environments as follows:

## Confidentiality of processing systems

### Identity and Access Management

- Predefined security groups are utilized to assign role-based access privileges and segregate access to data to the production systems.
- Administrator access to the production systems is granted based on job roles and responsibilities and limited to authorized personnel.

### Audit Assurance: Compliance, Governance and Risk Management

- GitLab performs annual security operational risk assessments of production applications and services. Results from risk assessment activities are documented in a risk register and prioritized for treatment based on risk level.
- GitLab performs a vendor security review for third-party vendors whose services will store, process or transmit GitLab and/or GitLab customer data.
- GitLab performs risk-based continuous control monitoring throughout the year by performing control testing using a formal methodology. The testing results are documented and reviewed by management, including remediation plans for identified observations.
- Controlled documents are reviewed, approved by management, and communicated to relevant employees annually.

### Human Resources

- GitLab team members complete security awareness training upon hire and annually thereafter. The training includes relevant GitLab security policies, instructions for reporting security incidents and general industry security best practices.
- GitLab new hires are required to pass a background check as a condition of their employment.

## Integrity of processing systems

### Application & Infrastructure Security

- Infrastructure management and configuration management tools are used for security hardening and to ensure baseline configuration standards have been established for production servers.
- Network traffic to and from untrusted networks passes through a policy enforcement point; firewall rules are configured to prevent unauthorized access.
- An issue tracking system is in place to centrally maintain, manage, and monitor application and infrastructure changes from development through implementation.

### Threat and Vulnerability Management

- GitLab conducts scoped vulnerability scans against the production environment to identify threats and assess their potential impact to the system on a weekly basis. Results are evaluated and remediated according to severity level.
- GitLab executes a 3rd party application penetration test on an annual basis, a process which includes additional 3rd party remediation testing if any high or moderate risk vulnerabilities are identified.
- Monitoring tools are used to continuously monitor security events, latency, network performance, and virtual server performance.
- Incident response procedures are in place that outline the response procedures to security events and includes lessons learned to evaluate the effectiveness of the procedures.

## Availability of processing systems

### Resilience

- A business continuity plan is in place to guide personnel in procedures to protect against disruptions caused by an unexpected event. Tabletop exercises are completed on an annual basis.
- Enterprise monitoring applications are configured to monitor in scope system capacity levels and alert operations personnel when predefined thresholds have been met.

## Additional Considerations

- The GitLab application is designed to allow customers to delete their own data when no longer needed.
- Google (for GitLab.com) and AWS (for GitLab Dedicated) are responsible for implementing controls to manage physical and logical access to the servers and supporting infrastructure, underlying network and virtualization management software for its cloud hosting services where GitLab processing systems reside.
- Customers may elect to implement technical and organizational measures in relation to customer owned (Red) data.

## Resources

For additional details and supporting artifacts please see GitLab's [Customer Assurance Package.](https://about.gitlab.com/security/cap/)
