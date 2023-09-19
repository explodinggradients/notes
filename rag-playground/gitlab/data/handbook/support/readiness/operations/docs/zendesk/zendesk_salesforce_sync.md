---
title: Zendesk-Salesforce Sync
description: Support Operations documentation page for our Zendesk<>Salesforce Sync
canonical_path: "/handbook/support/readiness/operations/docs/zendesk/zendesk_salesforce_sync"
---

## What is the Zendesk-Salesforce Sync?

The Zendesk-Salesforce Sync (ZD<>SFDC sync for short) is a set of scripts that
are run via GitLab CI/CD to handle the interaction between Zendesk and
Salesforce. What it does exactly depends on the project itself:

| Name                    | What it does |
|-------------------------|--------------|
| salesforce-cases        | Creates and updates Salesforce cases based on Zendesk tickets |
| zd-sfdc-sync-global     | Syncs Salesforce account data into Zendesk organizations      |
| zd-sfdc-sync-us-federal | Syncs Salesforce account data into Zendesk organizations      |
|                         | Syncs Salesforce contacts data into Zendesk users             |

## Zendesk Global organizations sync

This first gathers the data from Salesforce. This is done via the following SOQL
(Salesforce Object Query Language) query:

<details>
<summary>SOQL query used</summary>

```sql
SELECT
  Account.Account_ID_18__c,
  Account.Name,
  Account.CARR_This_Account__c,
  Account.Ultimate_Parent_Sales_Segment_Employees__c,
  Account.Account_Owner_Calc__c,
  Account.Number_of_Licenses_This_Account__c,
  Account.Type,
  Account.Technical_Account_Manager_Name__c,
  Account.Account_Demographics_Geo__c,
  Account.GS_Health_Score_Color__c,
  Account.Next_Renewal_Date__c,
  Account.Restricted_Account__c,
  Account.Partners_Partner_Status__c,
  Account.Partners_Partner_Type__c,
  Account.Partner_Track__c,
  (SELECT
     Current_Subscription_Status__c,
     Current_Term_End_Date__c,
     Current_Term_Start_Date__c,
     Entitled_Seats__c,
     Product_Tier_Name_Short__c,
     Plan_Name__c
   FROM Customer_Subscriptions__r
   WHERE Current_Subscription_Status__c = 'Active'),
  (SELECT
     Name,
     Zuora__Status__c,
     Zuora__SubscriptionEndDate__c,
     Zuora__SubscriptionStartDate__c,
     Support_Level__c,
     Zuora__OpportunityName__c,
     Zuora__SubscriptionNumber__c
   FROM Zuora__Subscriptions__r
   WHERE Zuora__Status__c = 'Active'),
  (SELECT
     Name,
     Zuora__SoldToWorkEmail__c
   FROM Zuora__R00N40000001kyLcEAI__r
   WHERE IsDeleted = false)
FROM Account
WHERE
  (Account.Type IN ('Customer', 'Former Customer') OR
   Account.Account_ID_18__c = '0014M00001sGJ8xQAG') OR
  (Account.Type = 'Partner' AND
   Account.Partners_Partner_Status__c IN ('Authorized', 'Former') AND
   Account.Partners_Partner_Type__c IN ('Alliance', 'Channel') AND
   Account.Partner_Track__c IN ('Open', 'Select', 'Technology')
  )
```

</details>

This data is then processed by the script to verify the account's subscriptions
(both Customer and Zuora). It also locates the sold-to emails of the
subscriptions to later attempt user creation (if it is a new organization in
Zendesk).

While doing this, it also locates accounts that are classified as "greatly
expired" (meaning they have been expired for 3 or more years). It puts these
into a separate object for use later.

From here, it then gathers all the organization data from Zendesk Global. This
does very little actual processing of the data, short of ignoring tags that
aren't related to the sync itself.

The scripts then compares the data from Salesforce and the data from Zendesk
Global. From this comparison, it locates Zendesk Global organizations that need
to be updated and ones that need to be created.

The scripts will then begin syncing this information to Zendesk Global, updating
organizations that need updating and creating the ones that need creation. For
organizations that need to be created, it will also attempt to create contacts
for them based off the information of the subscriptions (gathered earlier).

Once that is done, the scripts then remove all "greatly expired" organizations
from Zendesk Global in accordance with our data retention policy.

## Zendesk Global Salesforce cases sync

This is runs at two periods of time:

- whenever a ticket with an organization associated is created
- whenever a ticket with a matching Salesforce case is closed

For when a ticket is created, it will create a Salesforce case based off the
Zendesk Global ticket data.

For when a ticket is closed, it will update the corresponding case to indicate
it has been closed.

## Zendesk US Federal organizations sync

**Note** This set of scripts also handles the
[Zendesk US Federal users sync](#zendesk-us-federal-users-sync). We have
separated it into its own section for ease of readability.

This first gathers the data from Salesforce. This is done via the following SOQL
(Salesforce Object Query Language) query:

<details>
<summary>SOQL query used</summary>

```sql
SELECT
  Account.Account_ID_18__c,
  Account.Name,
  Account.CARR_This_Account__c,
  Account.Ultimate_Parent_Sales_Segment_Employees__c,
  Account.Account_Owner_Calc__c,
  Account.Number_of_Licenses_This_Account__c,
  Account.Type,
  Account.Technical_Account_Manager_Name__c,
  Account.Support_Level__c,
  Account.Region__c,
  Account.GS_Health_Score_Color__c,
  Account.Next_Renewal_Date__c,
  Solutions_Architect_Lookup__r.Name,
  (SELECT
     Current_Subscription_Status__c,
     Current_Term_End_Date__c,
     Current_Term_Start_Date__c,
     Entitled_Seats__c,
     Product_Tier_Name_Short__c,
     Plan_Name__c
   FROM Customer_Subscriptions__r
   WHERE Current_Subscription_Status__c = 'Active'),
   (SELECT
      Name,
      Zuora__Status__c,
      Zuora__SubscriptionEndDate__c,
      Zuora__SubscriptionStartDate__c,
      Support_Level__c,
      Zuora__OpportunityName__c,
      Zuora__SubscriptionNumber__c
    FROM Zuora__Subscriptions__r
    WHERE Zuora__Status__c = 'Active')
FROM Account
WHERE
Type IN ('Customer', 'Former Customer', 'Prospect') AND
Account_Territory__c LIKE 'USPUB-FED%'
```

</details>

This data is then processed by the script to verify the account's subscriptions
(both Customer and Zuora).

From here, it then gathers all the organization data from Zendesk US Federal.
This does very little actual processing of the data, short of ignoring tags that
aren't related to the sync itself.

The scripts then compares the data from Salesforce and the data from Zendesk
US Federal. From this comparison, it locates Zendesk US Federal organizations
that need to be updated and ones that need to be created.

The scripts will then begin syncing this information to Zendesk US Federal,
updating organizations that need updating and creating the ones that need
creation.

## Zendesk US Federal Salesforce cases sync

This is runs at two periods of time:

- whenever a ticket with an organization associated is created
- whenever a ticket with a matching Salesforce case is closed

For when a ticket is created, it will create a Salesforce case based off the
Zendesk US Federal ticket data.

For when a ticket is closed, it will update the corresponding case to indicate
it has been closed.

## Zendesk US Federal users sync

**Note** This set of scripts also handles the
[Zendesk US Federal organizations sync](#zendesk-us-federal-organizations-sync).
We have separated it into its own section for ease of readability.

This first gathers the data from Salesforce. This is done via the following SOQL
(Salesforce Object Query Language) query:

<details>
<summary>SOQL query used</summary>

```sql
SELECT
  Contact.Name,
  Contact.Email,
  Account.Account_ID_18__c,
  Account.Name,
  Contact.Inactive_Contact__c
FROM Contact
WHERE
  Contact.Inactive_Contact__c = false AND
  Account.Type IN ('Customer', 'Former Customer', 'Prospect') AND
  Account.Account_Territory__c LIKE 'USPUB_FED%'
```

</details>

This data is then processed to remove any contacts with duplicate emails or
missing data.

From here, it then gathers all the user data from Zendesk US Federal. This does
very little actual processing of the data, short of ignoring tags that aren't
related to the sync itself.

The scripts then compare the data from Salesforce and the data from Zendesk US
Federal. From this comparison, it locates Zendesk US Federal users that need to
be updated and ones that need to be created. It will use the organization data
from the
[Zendesk US Federal organizations sync](#zendesk-us-federal-organizations-sync)
to determine the organization ID.

The scripts will then begin syncing this information to Zendesk US Federal,
updating users that need updating and creating the ones that need creation.

## Change management

As these are maintained via sync repositories, our standard change management
process applies to all Zendesk-Salesforce Sync. See
[standard change management](/handbook/support/readiness/operations/docs/change_management#standard-change-management)
for more information.

#### Labels to use

For all issues and MRs involving the Zendesk-Salesforce Sync, the label
`Support-Ops-Category::Sync` should be used.

#### Change criticality

Due to the nature and impact adding/editing/deleting the Zendesk-Salesforce Sync
imposes, all issues/MRs related to the Zendesk-Salesforce Sync will be
classified as either
[criticality 1](/handbook/support/readiness/operations/docs/change_criticalities#criticality-1)
or
[criticality 2](/handbook/support/readiness/operations/docs/change_criticalities#criticality-2)
