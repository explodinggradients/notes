---
title: "Domain Names and DNS Records"
description: "IT Self Service Guides provide team members with instructions for frequently asked questions for installing, configuration, and troubleshooting your laptop or our tech stack applications."
---

## Overview

We have a variety of domain names at GitLab for production, services, internal tools, and sandbox purposes. They are technically managed in a variety of ways.

The [Domain Name Registration and Maintenance Policy](https://about.gitlab.com/handbook/finance/expenses/#domain-name-registration-and-maintenance-policy) is designed to centralize the registration, legal management, and costs associated with domain names.

As of 2022-08-01, you can no longer submit an expense report for domain names that you use for demo and sandbox purposes. See the instructions below for IT to [purchase a trademark domain name](#trademark-domain-names), self service purchasing a [non-trademark domain with Sandbox Cloud](#non-trademark-domain-names) for demo and internal use cases, and [transferring an existing domain name](#transferring-domain-names) into GitLab IT managed infrastructure for ongoing renewals that are paid for by the company.

If you have any questions, please reach out to Jeff Martin or Vlad Stoianovici.

### Trademark Domain Names

The full list of GitLab IT and Infrastructure managed domain names can be found in the [GitLab Owned Domains](https://docs.google.com/spreadsheets/d/187C_xXgaR_L55PeaFVqd9C0E28qrCvmDZnGgQT_4eNI/edit#gid=0) spreadsheet. All recent purchase and transfer issues are linked to [gitlab/it/infra#117](https://gitlab.com/gitlab-com/it/infra/issue-tracker/-/issues/117).

If you want to purchase any domain name that includes any of our [trademarks](https://about.gitlab.com/handbook/marketing/brand-and-product-marketing/brand/brand-activation/trademark-guidelines/) (ex. `gitlab`, `gl`, `gtlb`, etc.) or any domain that will host RED or ORANGE data, please use the issue template to request a domain from IT. You do not need strong justification, it just needs to be managed by IT Infrastructure for compliance reasons.

[DNS Domain Purchase Request Issue Template](https://gitlab.com/gitlab-com/it/infra/issue-tracker/-/issues/new?issuable_template=dns_domain_purchase_request)

See [Transferring Domain Names](#transferring-domain-names) to learn more about how to transfer the domain name from a registrar you manage (ex. Namecheap, GoDaddy, etc.) to a GitLab IT Infrastructure managed registrar.

### Trademark Domain DNS Records

See the `tfvars.json` files in [config-mgmt](https://gitlab.com/gitlab-com/gl-infra/config-mgmt/-/tree/master/environments/dns) for a list of all current DNS records that are configured for our trademark domain names.

Our less popular and underutilized domain names are manually managed in the `dns-zones-4a589e31` AWS account or  `dns-zones-a1ce7e00` GCP project.

If you want to add or update an A, CNAME, TXT, etc record for a trademark domain name, please use the issue template to have IT Infrastructure update the record for you. We **do not** create subdomain records on trademark domains for demo/sandbox/test environments unless it is a staging environment for a production service.

[DNS Domain Record Update Issue Template](https://gitlab.com/gitlab-com/it/infra/issue-tracker/-/issues/new?issuable_template=dns_domain_record_update)

Please open the issue and ask questions in the comments if you need guidance.

### Non-Trademark Domain Names

> This covers demo, internal (non-production), and sandbox use cases.

You can self service purchase a domain name of your choice (without Gitlab trademarks) that is paid for by GitLab through your Sandbox Cloud AWS account or GCP project, and you can manage the DNS records yourself. You do not need to contact IT for non-trademark domain purchases, however you can ask in `#sandbox-cloud-questions` if you need assistance.

- [Domain Purchase Instructions for AWS Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html)
- [Domain Purchase Instructions for GCP Cloud Domains](https://cloud.google.com/domains/docs/register-domain)

**Do not purchase any domain names on Namecheap, GoDaddy, or other registrars. Only domain names purchased inside of your Sandbox Cloud AWS Account or GCP Project will be paid for by GitLab. No expense reports will be approved.** See the [Domain Name Registration and Maintenance Policy](https://about.gitlab.com/handbook/finance/expenses/#domain-name-registration-and-maintenance-policy) for details.

Please ask in `#sandbox-cloud-questions` if you need guidance.

#### Demo and Sandbox Subdomains

If you use [Sandbox Cloud Terraform Environments](/handbook/infrastructure-standards/realms/sandbox#terraform-environments), HackyStack will automatically create a DNS subdomain for you that is automatically configured to resolve (ex. `env-a1b2c3d4.gcp.gitlabsanbox.net`) without needing to buy a domain name for a quick test.

It is labor intensive (aka expensive) to manually manage subdomain records for different team members as a subdomain with NS records. We spent a lot of time cleaning up past records and consider it to be too expensive to manage.

We believe it is [more efficient](https://about.gitlab.com/handbook/values/#efficiency-for-the-right-group) to pay $10-20/yr for each team member to have their own domain name that they can manage how they see fit. By using the Sandbox Cloud, the costs are handled automatically without any extra work. See [Non-Trademark Domain Names](#non-trademark-domain-names) for instructions.

Please ask in `#sandbox-cloud-questions` if you need guidance.

### Transferring Domain Names

If you have a trademark domain already that is registered with another registrar not managed by IT (Gandi, AWS, GCP), please open an issue to have it transferred. You will continue to manage the name servers and domain records, however IT will manage the registrar side.

[DNS Domain Transfer Request Issue Template](https://gitlab.com/gitlab-com/business-technology/engineering/infrastructure/issue-tracker/-/issues/new?issuable_template=dns_domain_transfer_request)

If you have a non-trademark domain name (ex. `mycooldevopsdemo.io`) that you have been expensing in the past but can't anymore due to the policy changes, you can self-service transfer it to your GitLab Sandbox Cloud [AWS account](/handbook/infrastructure-standards/realms/sandbox#accessing-your-aws-account) (Route 53) or [GCP project](/handbook/infrastructure-standards/realms/sandbox#accessing-your-gcp-project) (Google Domains). We usually recommend GCP for most use cases, however it is your choice.

- [Domain Transfer Instructions for AWS Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53.html)
- [Domain Transfer Instructions for GCP Cloud Domains](https://cloud.google.com/domains/docs/transfer-domain-from-another-registrar)

### Domain Renewals

All trademark domain names are set to automatically renew. Any exceptions to this are documented in an issue for specific use cases, but are rare.

If a team member leaves GitLab, any non-trademark domain names that they purchased in their Sandbox Cloud AWS account or GCP project will not automatically renew since the parent AWS account or GCP project are shut down during offboarding.
