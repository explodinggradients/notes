---
title: Licensing & Renewals
description: Licensing & Renewals (L&R) comprises efforts to resolve problems customers face when they purchase or renew their GitLab subscription.
---

## Overview

L&R Support Engineers help resolve problems encountered by customers in the
process of purchasing or renewing a GitLab subscription.

L&R work generally involves collaborating with customers and other GitLab teams, primarily Sales and Fulfillment,
as well as checking internal GitLab systems and performing data validation. Some examples:

- Answering general queries from a user about purchasing and managing a subscription
- Troubleshooting license upload errors and subscription association issues
- Assisting Sales team members with requests related to L&R

### History

In July, 2020, [a decision was made](https://gitlab.com/gitlab-org/fulfillment-meta/-/issues/96#note_384760742)
for L&R work to be handled by Support for the foreseeable future. At the time,
[business-critical priorities](https://gitlab.com/gitlab-org/fulfillment-meta/-/issues/96#note_384808050)
prevented the [Fulfillment product section](https://about.gitlab.com/handbook/product/categories/#fulfillment-section)
from having sufficient capacity to address and resolve the major L&R-related issues.
And whereas creating an entirely new team for this work would have been
difficult, Support was already engaged and was in a position to scale up
quickly to meet customer needs.

## Contacts

### Support Management contacts

- Overall DRI: Shaun McCann
- Regional DRIs: Mike Dunninger, John Lyttle, Ket Slaats
- Coordinating Mechanizer maintenance: Ronnie Alfaro

### Support Stable Counterparts

See the [Fulfillment section description](https://about.gitlab.com/handbook/product/categories/#fulfillment-section)
in the Product Handbook to learn who our current Support Stable Counterparts are. If you are
interested in being an L&R SSC, please talk with your manager and one of the
[Regional DRIs](#support-management-contacts).

## Direction

In collaboration with Sales, Fulfillment and other teams we aim to improve the customer
experience related to managing subscriptions. We achieve this by:

- automating processes
- suggesting improvements to processes
- reporting and fixing bugs
- meeting our Service Level Objectives to external and internal customers

## Regional L&R Teams

- AMER Team [Page](amer-region.html)
- APAC Team Page
- EMEA Team Page

---

## Information for Support Engineers with L&R responsibilities

Before starting to work L&R tickets, be sure you complete the
[L&R / Subscriptions training module](https://gitlab.com/gitlab-com/support/support-training/-/blob/master/.gitlab/issue_templates/Subscriptions%20License%20and%20Renewals.md).

### Core Concepts

As an L&R Engineer, you will want to understand some core concepts of terms, expressions and
features we interact with every day. The next few paragraphs explain these concepts, which can also
be referred to in the [terminology table](#common-terminology).

**Subscription** is a term used to explain the purchase of a specific tier of features for a set
amount of time. There are two factors that comprise a subscription:

- **SaaS** or **Self-Managed**, which defines where the subscription is ‘applied’.
**GitLab Dedicated** is considered as Self-Managed for the purposes of how it is applied.
- The **Tier**, providing access to different features. This includes **Premium** or **Ultimate**.

A **License** is a *legacy* file that was previously required to activate a subscription on
Self-Managed instances. Since GitLab `14.1`, activations are now almost always handled by
**cloud activation codes**, with a few exceptions:

- [Offline cloud licensing](https://about.gitlab.com/pricing/licensing-faq/cloud-licensing/#offline-cloud-licensing)
allows for cloud licensing in an offline environment. The customer must manually download and send
periodic usage data via email. Requires at minimum GitLab `15.0`.
- For instances still on versions prior to GitLab `14.1`, customers must work with their GitLab
representative to request an exemption as part of the sales purchase or renewal process.
  - As noted on GitLab's [statement of support](https://about.gitlab.com/support/statement-of-support/#version-support),
  our Support team are (in almost all circumstances) unable to assist customers running below
  GitLab `14.x`, so this should provide further encouragement for customers to upgrade.
- [Post-sales exemptions for Cloud Licensing](https://about.gitlab.com/handbook/support/license-and-renewals/workflows/self-managed/cloud-licensing.html#post-sale-exemptions-support)
are rare and require an internal request and Sales VP approval.
- License files are still used for Self-Managed **Trials**.

A **Namespace** is a top-level group where users can collaborate in subgroups and projects, and is
considered a separate entity from other namespaces. SaaS customers purchase a subscription for a
namespace, which means the namespace has access to their purchased tier of features, such as
Premium or Ultimate. For example, company: `“Example Corporation”` has a namespace located
at: `gitlab.com/example-co`:

- All subgroups (`gitlab.com/example-co/marketing`) and projects
(`gitlab.com/example-co/development/webapp`) created under this path have access to the paid
features of the subscription.
- A separate namespace, also used by the company, `gitlab.com/example-net` is not included in the
subscription, and has no access to paid features.

A **Web Direct** customer has purchased a subscription or product *directly*, via GitLab.com and/or
customers.gitlab.com. A **Sales-assisted** customer has been assisted by Sales via *Salesforce* to
purchase the subscription or product, and is common in Enterprise organisations where a
contract is involved.

[**Cloud Licensing**](https://about.gitlab.com/pricing/licensing-faq/cloud-licensing/#what-is-cloud-licensing)
(also known as **Cloud Activation**, **Cloud License**) is the now-default and preferred method to
activate a subscription for Self-Managed instances. A Cloud License is a 24-digit alphanumeric code
that customers apply to their Self-Managed instance. Some benefits of a Cloud License:

- No need to re-apply a license file every year
- Allows for the ability to use **Quarterly Subscription Reconciliation (QSR)** to reconcile
Users over Subscription

[**Quarterly Subscription Reconciliation (QSR)**](./workflows/quarterly_subscription_reconciliations.html)
is a method to reconcile any additional usage over the subscription agreement, such as when there
are **Users over Subscription**. When enabled, QSR is performed each quarter (every three months)
and generates an invoice if seat usage has increased over the current maximum.

### Add-ons

The L&R team handles a lot of different types of purchases, and also assists with troubleshooting
one-off or recurring **add-ons**. While GitLab Self-Managed predominantly consists of just a
subscription purchase, GitLab.com provides a variety of add-ons for purchase including
**Compute Minutes** and **Storage and Transfer**.

#### Compute Minutes

Formerly known as "CI/CD Minutes" or "Compute Credits", Compute Minutes allow for usage of
GitLab-managed Runners (Shared Runners) on GitLab.com (SaaS). Different tiers receive units
as part of their subscription, which refresh every month:

- Free (No Subscription): `400`
- Premium: `10,000`
- Ultimate: `50,000`

Units **are not a 1-to-1 translation of minutes** and are subject to
[cost factors](https://docs.gitlab.com/ee/ci/pipelines/cicd_minutes.html#cost-factor),
including [the type of Runner being used](https://docs.gitlab.com/ee/ci/pipelines/cicd_minutes.html#additional-costs-on-gitlab-saas)
in a pipeline. A customer [can purchase additional units](https://docs.gitlab.com/ee/ci/pipelines/cicd_minutes.html#purchase-additional-cicd-minutes)
at any time.

#### Storage and Transfer

On GitLab.com (SaaS), [project storage limits](https://docs.gitlab.com/ee/user/usage_quotas.html#project-storage-limit),
are enforced. The default storage limit is 10 GB *per project*. Once a project reaches its storage limit, it is considered as
having [excess storage usage](https://docs.gitlab.com/ee/user/usage_quotas.html#excess-storage-usage)
and may enter into a read-only state until additional storage is purchased. Additional
storage [can be purchased at any time](https://docs.gitlab.com/ee/subscriptions/gitlab_com/index.html#purchase-more-storage-and-transfer).

Changes to how storage and transfer limits are considered at a
[namespace level](https://docs.gitlab.com/ee/user/usage_quotas.html#namespace-storage-limit) are
planned, but not currently enforced. See [the storage management improvements issue](https://gitlab.com/gitlab-org/gitlab/-/issues/375296)
and [Pricing FAQ](https://about.gitlab.com/pricing/faq-paid-storage-transfer/#q-what-is-changing-with-storage-and-transfer-limits)
for further information.

### What you'll be working on

- Tickets in the L&R queue (see
  [Zendesk Global Views](/handbook/support/readiness/operations/)
  for more information on locating these) in Zendesk. The queue will contain
  tickets from customers as well as from GitLab Team Members (Sales, CSMs,
  etc.). The tickets from team members are called "internal requests," and
  information about those is available on the
  [working internal requests workflow page](/handbook/support/license-and-renewals/workflows/working_internal_requests.html).
- Creating and/or updating [marketing pages](#marketing-pages),
  [product documentation](#product-documentation) and the
  [GitLab Handbook](#handbook-pages) and [workflows](#workflows) around
  subscriptions, licensing and renewal-related topics.
- Identifying product issues that are important to customers, Support or both,
  and coordinating with the entire L&R Support Team and the Fulfillment Product
  Management Team to prioritize them for Engineering.

### Systems you'll need access to

To be effective with this work, you'll need access to systems and tools which you
might not otherwise encounter working other Support problem types. This list
supplements the baseline entitlements for the Support Engineer job family.

#### CustomersDot

CustomersDot is the common name for the web application built by GitLab and found at
<https://customers.gitlab.com>. All license and subscription management is conducted
on this site. You will need access to this to generate, forward and modify customer
license and subscription information. When submitting [an access request (AR)](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=Individual_Bulk_Access_Request) for
CustomersDot, use this information:

- System name:
  > CustomersDot - admin
- Justification for this access:
  > L&R Support Engineers need CustomersDot admin access to work on customer licensing
  > and subscriptions issues and to debug issues on the application itself.

#### Salesforce

A Salesforce.com (SFDC) account makes collaboration with Sales team members more
efficient, primarily because you'll be able to receive notifications when you're
tagged in a Chatter message (see the [working with Sales workflow](/handbook/support/license-and-renewals/workflows/working_with_sales.html)).

When creating an [individual/bulk access request](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=Individual_Bulk_Access_Request), use the following information:

- System name:
  - If you are a US citizen:
    > SalesForce, Role: Executive - No View All, Profile: Read Only GitLab,
    > with US public sector record visibility
  - If you are not a US citizen:
    > SalesForce, Role: Executive - No View All, Profile: Read Only GitLab
- Justification for this access:
  > L&R Support Engineers need their own Salesforce accounts to better collaborate
  > with Sales team members as they work on customer licensing issues.

#### Slack

Discussion of Licensing & Renewals tickets and customer issues occurs in the
[#support_licensing-subscription](https://gitlab.slack.com/archives/C018C623KBJ)
channel in Slack. This ensures:

> - L&R team members will have one channel in which to collaborate
> - Increased visibility in queries and shared knowledge
> - Increased cohesion in the L&R team regardless of region

At the commencement of the APAC region's Support Hours (23:00 UTC) there is a
[Daily Stand-up Bot for Licensing and Renewals in APAC](/handbook/support/support-global-groups/#daily-stand-up-bot-for-licensing-and-renewals-in-apac)
post which tags all Support Engineers who have some responsibility for L&R
tickets. This thread notifies the team of who is away for the current week, and
allows team members to provide updates to each other about when they're working
on the queue. This helps ensure coverage reliability of the L&R tickets across
the APAC region's support hours.

#### Zuora

Zuora is considered the [single source of truth](/handbook/handbook-usage/#single-source-of-truth)
or [system of record](/handbook/handbook-usage/#system-of-record)
for many subscription and renewal-related items, such as product SKUs,
subscriptions and invoices. See the
[Transition to Zuora as the SSOT issue](https://gitlab.com/groups/gitlab-org/-/epics/4664)
for more information.

Having access to Zuora will help with troubleshooting in situations where a
customer's CustomersDot and Salesforce records present conflicting or confusing
information.

When creating an [individual/bulk access request](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=Individual_Bulk_Access_Request), use the following information:

- System name:
  > Zuora READ-ONLY access
- Justification for this access:
  > L&R Support Engineers need read-only Zuora access to troubleshoot Licensing and
  > Renewal customer issues and support requests.

### Workflows

- [License & renewals workflows](workflows/index.html)

### Useful tools

- [license decoder](https://gitlab.com/gitlab-com/support/toolbox/license-decoder)
  -- Ruby script to decode `.gitlab-license` files.
- [slic - Subscription and License Information Copier](https://gitlab.com/rverschoor/punk/-/tree/main/slic)
  -- browser userscript to copy and format CustomersDot information
  into internal notes.

### Teams you'll be working with

#### Product

As you work through the queue and on issues, if you spot something in the
[Fulfillment backlog](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=group%3A%3Afulfillment)
that would makes things better for customers and Support, please label it with
`Support Interest::Categorize`. See [Support's issue list for Fulfillment](./workflows/managing_product_issues.html#supports-issue-list-for-fulfillment) for more information.

##### Fulfillment stage

The [Fulfillment](https://about.gitlab.com/direction/fulfillment/) Stage manages
Purchasing and Provisioning, CustomersDot Usage, and Subscription Management.
These teams own responsibilities that align with the types of requests we
generally see in the queue.

`#s_fulfillment` channel in Slack

##### Growth stage

When we look at the product [Growth](https://about.gitlab.com/handbook/product/categories/#growth-stage)
stage, we can see that the team owns responsibilities that align with some of
the types of requests we generally see in the queue, in particular the
`Conversion` group.

- Activation Group: [New Group Namespace Verify Stage Adoption Rate](https://about.gitlab.com/handbook/product/performance-indicators/#new-group-namespace-verify-stage-adoption-rate)
- Adoption Group: [New Group Namespace Create Stage Adoption Rate](https://about.gitlab.com/handbook/product/performance-indicators/#new-group-namespace-create-stage-adoption-rate)
- Expansion Group: [New Group Namespace with at least two users added](https://about.gitlab.com/handbook/product/performance-indicators/#new-group-namespace-with-at-least-two-users-added)
- Conversion Group:[New Group Namespace Trial to Paid Conversion Rate](https://about.gitlab.com/handbook/product/performance-indicators/#new-group-namespace-trial-to-paid-conversion-rate)

## What is **not in the scope** of L&R work in Support?

The queue should not be used for the following:

- Billing related matters, such as payments, invoice generation, refunds, etc.
- Product related questions
- [New business requests](https://about.gitlab.com/sales/)
- Requests related to the
  [education program](https://about.gitlab.com/solutions/education/)
- Requests related to the
  [open source program](https://about.gitlab.com/solutions/open-source/join/)

## Useful links

### Product documentation

- [GitLab subscription](https://docs.gitlab.com/ee/subscriptions/)

### Marketing pages

- [Support SLAs for billing, purchasing, subscriptions or licenses](https://about.gitlab.com/support/#issues-with-billing-purchasing-subscriptions-or-licenses)
- [Licensing and subscription FAQ](https://about.gitlab.com/pricing/licensing-faq/)

### Handbook pages

- [CustomersDot Admin Docs](https://about.gitlab.com/handbook/product/fulfillment-guide)
- [Business Ops](https://about.gitlab.com/handbook/business-technology/)
  - [Business Systems: Enterprise Applications, Integrations, and Flow](https://about.gitlab.com/handbook/business-technology/enterprise-applications/integrations/)
  - [Troubleshooting: True Ups, Licenses + EULAs](https://about.gitlab.com/handbook/business-technology/enterprise-applications/quote-to-cash/troubleshooting/)
- [Sales](https://about.gitlab.com/handbook/sales/)
  - [Sales Segmentation](https://about.gitlab.com/handbook/sales/field-operations/gtm-resources/)
  - [Sales Territories](https://about.gitlab.com/handbook/sales/territories/)
- [Marketing](https://about.gitlab.com/handbook/marketing/)
  - [Sales Enablement: GitLab.com subscriptions](https://about.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/enablement/dotcom-subscriptions/)

### Issue trackers

| Issue tracker | Use Case                                                                                                                           |
| ------------- |------------------------------------------------------------------------------------------------------------------------------------|
| [GitLab Issue Tracker](https://gitlab.com/gitlab-org/gitlab/issues) | Issues related to self-managed or GitLab.com functionality or backend processing                                                   |
| [CustomersDot](https://gitlab.com/gitlab-org/customers-gitlab-com/issues) | Issues caused specifically by something within CustomersDot or affecting self-managed license generation, generated licenses |

## Common Terminology

|Term|Description|
|--|--|
|Add-on|An optional extra that can be purchased to increase the limits of what is available in GitLab. Common examples of this are a `Seat add-on` where additional seats are purchased during the subscription term, or an additional `Storage` or `Compute Minutes` purchase (on SaaS only).|
|[Cloud Licensing](https://about.gitlab.com/pricing/licensing-faq/cloud-licensing/) / Cloud Activation *(SM Only)* | The preferred method of activating a self managed subscription where [subscription data is synchronized daily](https://docs.gitlab.com/ee/subscriptions/self_managed/#subscription-data-synchronization) from the customer instance to Customers.gitlab.com.  Unlike a License File, a cloud activation code does not need to be re-applied when the subscription is modified or renewed.|
|Customers Portal / CustomersDOT / customers.gitlab.com|Available at [customers.gitlab.com](https://customers.gitlab.com), the customers portal allows customers to view, manage and purchase subscriptions. L&R Engineers can generate, modify and send subscription information from here.|
|[GitLab Dedicated](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/)|Provides the benefits of SaaS (fully managed maintenance and operations) with infrastructure-level isolation while the customer has access to Administrator account on their instance.|
|Legacy License File / License Key *(SM Only)*| License files are now a legacy option used to provide SM trials, or for customers subject to certain criteria. License files are necessary to activate a subscription prior to GitLab 14.1.  License files typically have a maximum validity of one year, and must be re-issued and uploaded again if a subscription is modified or renewed.|
|[Namespace](https://docs.gitlab.com/ee/user/namespace/#namespaces) *(SaaS Only)*|A top-level group on gitlab.com where a subscription is applied. The subscription plan is available to all subgroups and projects under the namespace|
|Offline Cloud Licensing *(SM Only)*| In situations where customers must maintain an instance without Internet access, an [Offline Cloud License](https://about.gitlab.com/pricing/licensing-faq/cloud-licensing/#offline-cloud-licensing)) provides the benefits of Cloud Licensing by generating a usage data file locally.  The customer is prompted to upload this file monthly.
|[Quarterly Subscription Reconciliation (QSR)](https://docs.gitlab.com/ee/subscriptions/quarterly_reconciliation.html)|Introduced as a “Pay as you Go” alternative to True-Ups. A QSR is processed quarterly and will deliver cost savings versus the annual approach of True-Ups.|
|Seat|A seat represents GitLab’s implementation of a ‘concurrent software license’, which means the maximum number of users who will use the GitLab application and access paid features at any one time. Customers can change the specific users working with a GitLab Seat, providing the total seats in use does not exceed the total number of seats purchased.
|Self-Managed (**SM**)|Instances of the GitLab application managed by the customers themselves. The customers retain complete access and administrative control over their environment.|
|Software-as-a-Service (**SaaS**)|GitLab.com is the Software as a Service (SaaS) offering for the GitLab product. GitLab team members handle the maintenance, operation and upgrading of GitLab.com.|
|Subscription|Typically, a 12-month agreement to receive access to a tier of features in GitLab.|
|Trial|A short trial (usually at most 30 days) of GitLab paid features with [some restrictions](https://about.gitlab.com/free-trial/#what-is-included-in-my-free-trial-what-is-excluded) when used on SaaS. Customers can initiate a trial directly for both SaaS and Self-Managed on gitlab.com.  Trials are often requested by GitLab Sales to extend subscriptions when a customer purchase has not been finalized.|
|True-Ups|A method of reconciling `Users over Subscription` after the subscription term has expired. True-Ups require the full subscription fee for Users over Subscription to cover the previous subscription term.|
|User|A user on the GitLab platform. Most users will occupy a seat, subject to [some exceptions](https://about.gitlab.com/pricing/licensing-faq/#GitLab.com). Users can include administrator accounts (on Self-Managed), as well as automated job or bot users.
|[Users over Subscription](https://docs.gitlab.com/ee/subscriptions/self_managed/index.html#users-over-subscription) (**SM**) / [Seats owed](https://docs.gitlab.com/ee/subscriptions/gitlab_com/index.html#seats-owed) (**SaaS**) |GitLab permits additional usage over the purchased seat agreement, ensuring more users can be added during the subscription term without unnecessary obstacles. This overage can be processed at any time by adding more seats to the current subscription (seats add-on), processing the overage annually (`True-Ups`) or quarterly (`Quarterly Subscription Reconciliation`).|
