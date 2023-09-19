---
title: "GitLab Handbook Usage"
weight: -10
---

## Flow structure

1. A (process) problem comes up, frequently in an issue or chat.
1. A proposal is made in a merge request to the handbook.
1. Once merged, the change is announced by linking to the diff in the MR or commit. Major ones are posted in the #whats-happening-at-gitlab slack channel. Medium ones are posted in the #handbook channel for visibility, with a one line summary of the change. If there was an issue, close it out with a link to the diff.

Sometimes you want to have real time editing of a proposal during a meeting and you need to use a Google Doc for that. When doing so the first item should be the URL of the handbook page this content will be moved to when the meeting is over.

## Why handbook first

Documenting in the handbook before taking an action may require more time initially because you have to think about where to make the change, integrate it with the existing content, and then possibly add to or refactor the handbook to have a proper foundation. But, it saves time in the long run, and this communication is essential to our ability to continue scaling and adapting our organization.

This process is not unlike writing tests for your software. Only communicate a (proposed) change via a change to the handbook; don't use a presentation, email, chat message, or another medium to communicate the components of the change. These other forms of communication might be more convenient for the presenter, but they make it harder for the audience to understand the context and the implications for other potentially affected processes.

Having a **"handbook first"** mentality ensures there is no duplication; the handbook is always up to date, and others are better able to contribute.

Beyond being "handbook first," we are also "public handbook first." When information is [internal-only](/handbook/communication/confidentiality-levels/#internal), it should be captured in the internal handbook, but we default to the public handbook for anything that can be [made public](/handbook/communication/confidentiality-levels/#not-public). This ensures that everyone has access to any information that can be [SAFEly](https://about.gitlab.com/handbook/legal/safe-framework/) shared. This supports the GitLab [values](/handbook/values/), including transparency, efficiency, and results. It also protects against the internal handbook becoming a home for information that should otherwise be public or a conflicting or duplicative source of truth.
<!-- blank line -->

<figure class="video_container">
  <iframe src="https://www.youtube.com/embed/EuGsen3FxXc?start=991" frameborder="0" allowfullscreen="true"> </iframe>
</figure>

<!-- blank line -->
When asked during an [INSEAD](http://insead.edu/) case study interview (shown above) about challenges related to being all-remote, GitLab co-founder and CEO Sid Sijbrandij provided the following reply.

> The biggest problem is GitLab not working handbook first. We have an amazing handbook that allows us to collaborate, onboard new people, and think collectively.
>
> However, it is counterintuitive to communicate changes to the handbook. The default of people, when they wish to communicate a change, is to send a Slack message, send an email, give a presentation, or tell people in a meeting — *anything* but make a change in the handbook.
>
> It's slower for them. It's quicker to use any other form. If they make a change in the handbook, they first have to find the relevant part of the handbook, they sometimes have to adjust the handbook to make sure their change will fit in, they have to go through a technical process and a review or two, and they have to wait a bit before it's deployed.
>
> It's slower than any other option. However, it allows people that commit a change after that to build upon a change. When they take that extra time, it's building a foundation for the next thing.
>
> I think of it as brick laying. Every piece of information is a brick. At GitLab, there is a well-structured house, and everyone adds to that one house. Because we're pretty particular on how we build it, it has a strong foundation and we can build it very high.
>
> In every other company, they send the brick into the hands of people. Everyone is receiving bricks daily that they have to add to the house they're building internally. They forget things and things are unclear. A lot of context has to be created because there is no context around where to place the bricks.
>
> So, you can end up with a thousand houses that look quite different, that are all hanging a bit, and each time you add a brick to the top one pops out at the bottom. — *GitLab co-founder and CEO Sid Sijbrandij*

## Handbook guidelines

Please follow these guidelines and remind others of them.

### How we use the guide every day

1. Most guidelines in this handbook are meant to help, and unless otherwise stated, are meant to help more than being absolute rules. Don't be afraid to do something because you don't know the entire handbook, nobody does. Be gentle when reminding people about these guidelines. For example say, "It is not a problem, but next time please consider the following guideline from the handbook."
1. If you ask a question and someone answers with a link to the handbook, they do this because they want to help by providing more information. They may also be proud that we have the answer documented. It doesn't mean that you should have read the entire handbook, nobody knows the entire handbook.
1. If you need to ask a team member for help, please realize that there is a good chance the majority of the community also doesn't know the answer. Be sure to **document** the answer to radiate this information to the whole community. After the question is answered, discuss where it should be documented and who will do it. You can remind other people of this request by asking "Who will document this?"
1. When you discuss something in chat always try to **link** to a URL where relevant. For example, the documentation you have a question about or the page that answered your question. You can remind other people of this by asking "Can you please link?"
1. Remember, the handbook is not what we hope to do, what we should formally do, or what we did months ago. **It is what we do right now.** Make sure you change the handbook in order to truly change a process. To propose a change to a process, make a merge request to change the handbook. Don't use another channel to propose a handbook change (email, Google Doc, etc.).
1. The handbook is the process. Any sections with names like 'process', 'policies', 'best practices', or 'standard operating procedures' are an indication of a deeper problem. This may indicate a duplication between a prose description of a process and a numbered list description of the same process that should be combined in one description of the process.
1. When communicating something always include a link to the relevant (and up-to-date) part of the **handbook** instead of including the text in the email/chat/etc. You can remind other people of this by asking "Can you please link to the relevant part of the handbook?"
1. Everyone should subscribe to the `#handbook` channel to stay up-to-date with changes to the handbook

### How to change or define a process

1. To change a guideline or process, **suggest an edit** in the form of a merge request.
1. When working to get your change merged quickly, make sure you are asking the appropriate team members with merge rights. Not sure who is responsible? Consult (and add to) the `CODEOWNERS` [repository](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/.gitlab/CODEOWNERS).

    - For example, CMO (Chief Marketing Officer) Staff members can approve any merge request that is specific to their function, while the CMO approves any merge request that is cross-functional marketing. Chief of Staff to the CEO/CEO approves any merge request that has cross-company impact, such as GitLab's [Values](/handbook/values/) page.

1. After it is merged you can post this in the `#whats-happening-at-gitlab` slack channel if applicable. You can remind other people of this by asking "Can you please send a merge request for the handbook?"
1. When substantially changing handbook layout, please leave a link to the specific page of the review app **that is directly affected by this MR**. Along with the link, include as much info as possible in the MR description. This will allow everyone to understand what is the purpose of the MR without looking at diffs.
1. Keeping up with changes to the Handbook can be difficult, please follow the [commit subject guidelines](https://docs.gitlab.com/ee/development/contributing/merge_request_workflow.html#commit-messages-guidelines) with a particular focus on your merge request's title, to ensure someone reading the [Handbook Changelog](/handbook/about/changelog/) can quickly understand the MR's content.
1. Communicate process changes by linking to the **merged diff** (a commit that shows the changes before and after). If you are communicating a change for the purpose of discussion and feedback, it is ok to link to an **unmerged diff**. Do not change the process first, and then view the documentation as a lower priority task. Planning to do the documentation later inevitably leads to duplicate work communicating the change and it leads to outdated documentation. You can remind other people of this by asking "Can you please update the handbook first?"
1. When feasible, introduce process changes iteratively. It is important that you contribute to the handbook by [making small merge requests](/handbook/values/#make-small-merge-requests). This will help gain adoption among the process's intended audience. We want to avoid significant process changes that are unnecessarily large, top-down, and disruptive. These types of process changes can disempower [DRIs](https://about.gitlab.com/handbook/people-group/directly-responsible-individuals/) and cause people to focus on process rather than results.
1. Like everything else, our processes are always in flux. Everything is always in draft, and the initial version should be in the handbook, too. If you are proposing a change to the handbook, whenever possible, **skip the issue and submit a merge request**. (Proposing a change via a merge request is preferred over an issue description). Mention the people that are affected by the change in the merge request. In many cases, merge requests are easier to collaborate on since you can see the proposed changes.
1. **If something is a limited test** to a group of users, add it to the handbook and note as such. Then remove the note once the test is over and every case should use the new process.
1. If someone inside or outside GitLab makes a good suggestion invite them to add it to the handbook. Send the person the URL of the relevant page and section and offer to do it for them if they can't. Having them make and send the suggestion will make the change and will reflect their knowledge.
1. When you submit a merge request, make sure that it gets merged quickly. Making single, small changes quickly will ensure your branch doesn't fall far behind master, creating merge conflicts. Aim to make and merge your update on the same day. Mention people in the merge request or reach them via Slack. If you get a suggestion for a large improvement on top of the existing one consider doing that separately. Create an issue, get the existing MR merged, then create a new merge request.
1. If you have to move content have a merge request that moves it and does nothing else. If you want to clean it up, summarize it, or expand on it do that after the moving MR is merged. This is much easier to review.
1. Try to **add the why of a handbook process**, what is the business goal, what is the inspiration for this section. Adding the why makes processes easier to change in the future since you can evaluate if the why changed.

### Style guide and information architecture

#### Single Source of Truth

Think about the information architecture to eliminate repetition and have a Single Source of Truth (SSoT). Instead of repeating content cross-link it (each text has a hyperlink to the other piece). If you copy content please remove it at the origin place and replace it with a link to the new content. Duplicate content leads to more work by having to update the content in multiple places as well as the need to remember where all of the out of date content lives. When you have a single source of truth it's only stored in a single system.
Make sure to always cross-link items if there are related items (elsewhere in the handbook, in docs, or in issues).

#### System of Record

A system of record (SoR) is the authoritative data source for a given data element or piece of information. It's worth noting that while it is possible to have a system of record that is also a single source of truth, simply just being a system of record doesn't directly imply it is the single source of truth.

#### Organized by Function and Results

The handbook is **organized by function and result** to ensure every item in it has a location and owner to keep it up to date.

- It's essential that we adhere to this hierarchy and that we not maintain separate structures for company training materials (e.g. onboarding materials, how-tos, etc.), videos, or other documentation.
- Adhering to this hierarchy is sometimes counter-intuitive.
We've learned over the years that keeping content in context helps to ensure consistency when making future updates.
- At times, a change of perspective may be desired.
In those cases, link to relevant sections of the handbook but don't include the content itself.
See the [onboarding template](https://gitlab.com/gitlab-com/people-group/employment-templates/-/blob/main/.gitlab/issue_templates/onboarding.md) as an example.
Or for example a list of [Key Performance Indicators](https://about.gitlab.com/company/kpis/) that links to performance indicators but doesn't duplicate definitions.

#### Avoid unstructured content

- **Avoid unstructured content based on formats like Learning Playbooks, [FAQs](https://idratherbewriting.com/2017/06/23/why-tech-writers-hate-faqs/), lists of links (such as quick links), resource pages, glossaries, courses, videos, tests, processes, standard operating procedure, training, or how-to's.**
These are very hard to keep up-to-date and are not compatible with organization per function and result. For example: Call it Contract Negotiation Handbook instead of Contract Negotiation Playbook
- Instead, put the answer, link, definition, course, video, or test in the most relevant place.
Use descriptive headings so that people can easily search for content.
- That said, please mix *formats* where and when appropriate in the handbook, even within a single page.
Utilizing multiple formats can be valuable, and different people may prefer certain formats over others.
- Worry only about the organization **per function and result**, not about how the page will look if you embed varying types and formats of content.
- Note: A weakness of [FAQs](/handbook/communication/#dont-use-faqs) is that questions are often asked in biased or leading ways. When possible, state facts as facts.

#### Use headings liberally

If a page includes more than two headings (especially if it's larger than a single "screen"), add an automatically generated Table of Contents (ToC) by copying [line 6 to 10 in this MR](https://gitlab.com/gitlab-com/www-gitlab-com/merge_requests/7141/diffs#f054d0f855ebef2a11559c362a356a2f9e010b99_6_6).
Headings should have normal capitalization: don't use [ALL CAPS](https://en.wikipedia.org/wiki/All_caps) or [TitleCase](http://www.grammar-monster.com/glossary/title_case.htm).
After a heading, leave one blank line; this is [not required in the standard](http://spec.commonmark.org/0.27/#example-46), but it is our convention.

#### Use contributable diagrams

Preference contributable diagrams over uploading images or other less contributable diagrams. This makes it easier for other people to suggest changes and contribute. Diagram options in Markdown include [Mermaid](/docs/markdown-guide/#mermaid) and [PlantUML](/docs/markdown-guide/#plantuml).

### Editing the handbook

Strongly consider learning how to edit the [handbook using git](https://about.gitlab.com/handbook/git-page-update) and/or via [the web IDE](https://about.gitlab.com/handbook/git-page-update/#webide-using-the-browser).
Please read through the [Writing Style Guidelines](/handbook/communication/#writing-style-guidelines) before contributing.

#### Fine points

- Keep your handbook pages short and succinct. Eliminate fluff and get right to the point with the shortest possible wording. Keep in mind that the biggest challenge cited by new employees is the vast amount of information to take in during on-boarding.
- We don't need [.gitkeep files](https://stackoverflow.com/questions/7229885/what-are-the-differences-between-gitignore-and-gitkeep) in our handbook, they make it harder to quickly open a file in editors. Don't add them, and delete them when you see them.
- When mentioning currency amounts that team members may need to convert to their local currency (e.g. benefits, expenses, or bonuses), link those amounts to our [Exchange Rates](https://about.gitlab.com/handbook/total-rewards/compensation/#exchange-rates) section (e.g. [500 USD](https://about.gitlab.com/handbook/total-rewards/compensation/#exchange-rates)).

### Scope of this handbook

- All documentation that also applies to code contributions from the wider community should be in the GitLab CE project (for example in [CONTRIBUTING](https://gitlab.com/gitlab-org/gitlab-ce/blob/master/CONTRIBUTING.md) or the [code review guidelines](https://docs.gitlab.com/ee/development/code_review.html)), not the Handbook, which is only for team members. Read more in the [Documentation](/handbook/documentation/) section of the Handbook.
- The handbook is for things concerning current and future GitLab team-members only. If something concerns users of GitLab, it should be documented in the [GitLab documentation](https://docs.gitlab.com/), the [GitLab Development Kit (GDK)](https://gitlab.com/gitlab-org/gitlab-development-kit), the [CONTRIBUTING file](https://gitlab.com/gitlab-org/gitlab-ce/blob/master/CONTRIBUTING.md) or the [PROCESS file](https://gitlab.com/gitlab-org/gitlab-ce/blob/master/PROCESS.md).

### Handbook First Competency

In an all-remote, asynchronous organization, each team member should practice handbook first. For more information on what it means to be handbook first, please refer to the [why handbook first](/handbook/handbook-usage/#why-handbook-first) section of this page.

**Skills and behaviors of handbook first as a Team Member**:

- Actively contributes to the handbook.
- [Start with a merge request](/handbook/communication/#start-with-a-merge-request)
- Provides links to information from the handbook when answering questions and if the information doesn't exist in the handbook, then the team member adds it.
- Understands which information is internal-only, but puts all public information in the public handbook.

**Skills and behaviors of handbook first as a People Leader**:

- Holds their team and others accountable for being handbook first.
- Demonstrates leadership in being public handbook first with all information that is not internal-only.
- Enables new team members and managers on how to leverage the handbook as a resource.
- Serves as a role model for what it means to be handbook first.

### The Staging handbook

#### Where can it be found?

[Private Project](https://gitlab.com/gitlab-com-private/www-gitlab-com)

**Note: If you don't have appropriate permission, you will get 404 error.**

#### Why is there a staging handbook?

For E-Group, information may need to be iterated on or MR branches may need to be created in staging before it is made public. Outside of E-Group, temporary access may be granted on a project-specific basis.

#### The process of using this handbook

- If adding to this handbook as part of a working group initiative, review the [process for working groups](https://about.gitlab.com/company/team/structure/working-groups/#process)
- From the [project](https://gitlab.com/gitlab-com-private/www-gitlab-com), creating a commit or MR is just like any other project.
- Any MR you make on this project will only be available for viewing by the members of the group (gitlab-com-private)
- When you are **ready** to make a merge request against the **public** repo do the following:
    - Open a MR in the [gitlab-com-private-repo](https://gitlab.com/gitlab-com-private).
    - Set the **Source Branch** to your branch on the private repo.
    - Set the **Target Branch** to be `gitlab-com/www-gitlab-com`.
    - Click `Compare Branch and Continue`.
    - Then `Submit Merge Request`.
    - Now the MR has been created against the [public fork](https://gitlab.com/gitlab-com/www-gitlab-com) and can be seen by the **public**.
    - Your MR will be available to the **public** now and after it has been merged in will be deployed to [about.gitlab.com](https://about.gitlab.com).

#### Accessing the private group.

If you require project-based access, you can request temporary developer access in the `#private_repo_auth_request` Slack channel. The CLO is DRI on approvals. Membership will be audited on a monthly basis by the Sr. EBA to the CLO to ensure accuracy.

#### Keeping the staging handbook up-to-date

[How to keep your Git-Fork up to date](https://stefanbauer.me/articles/how-to-keep-your-git-fork-up-to-date) is an easy tutorial to follow from the command line to keep the staging handbook up-to-date, until mirroring is working.

### The Internal handbook

#### Where can it be found?

- [Internal Handbook Project](https://gitlab.com/internal-handbook/internal-handbook.gitlab.io/-/tree/main/content)
- [Live Website](https://internal.gitlab.com)

#### Why is there a internal handbook?

As a company, we are [public by default](/handbook/values/#public-by-default), but there are things that we cannot discuss publicly. The Internal Handbook is a space where team members can share internal information. Anything that **is not** considered [internal only](/handbook/communication/confidentiality-levels/#internal), should be in GitLab's [public handbook](/handbook/). Anything that is [limited access](/handbook/communication/confidentiality-levels/#limited-access) **should not be added to the internal handbook** as the internal handbook is accessible by all team members.

#### The process of using this handbook

Only add items to the internal handbook that fall into the [not public](/handbook/communication/confidentiality-levels/#not-public) category. Everything else should be added to our [public company handbook](/handbook/).

#### Accessing the internal handbook group.

All team members will have this added to their Okta access when they join the company. Login to your Okta dashboard and click on the  `GitLab Internal Handbook` tile. You will have to authenticate with Okta first.
- [Internal Handbook Project](https://gitlab.com/internal-handbook/internal-handbook.gitlab.io/-/tree/master/source)
- [Website](https://internal.gitlab.com)

#### Updating the Internal Handbook

1. You are on the [live internal handbook website](https://internal.gitlab.com/)
1. Click "Open in Web IDE" on the top right of the page. It will take you to the [Internal Handbook Project](https://gitlab.com/internal-handbook/internal-handbook.gitlab.io/-/tree/master/source).
1. Make edits in the same way that you would with Web IDE on the public handbook site.
1. If there is already a section you want to add to, you can select that folder now, go into the appropriate folder, and edit. If the section you are needing has not been created yet, click on the "+" and create a "new file".

#### What if I have questions about the internal handbook or want to help with it?

- Questions about what should be in the internal handbook vs in the public handbook?  See the [safe framework](https://about.gitlab.com/handbook/legal/safe-framework/#safe) or ask in `#safe`.
- Questions about updating the internal handbook or volunteering to help with enhancing it?  Join the `#internal-handbook` channel.

## Moving Pages and Adding Redirects to the Handbook

The handbook is a living document and we'll occasionally need to change URLs or move pages. This is [the process Growth Marketing uses to set up and manage redirects](https://about.gitlab.com/handbook/marketing/inbound-marketing/search-marketing/#request-an-aboutgitlabcom-redirect) for about.gitlab.com.

When you rename a file/URL please remember to add a redirect to [`redirects.yml`](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/redirects.yml) by [following this process](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/doc/redirects_on_about_gitlab_com.md). You'll also want to ensure you find/replace all instances of the old URL/anchor with the new one, which can be accomplished using this [practical handbook edits example](https://about.gitlab.com/handbook/practical-handbook-edits/#find-and-replace-a-string-in-all-matching-files).

## Management

It is each department and team member's responsibility to ensure the handbooks (public handbook, internal handbook, and staging handbook) stay current. The content in the handbook should be accurate and follow the same format as outlined in the [Guidelines](/handbook/handbook-usage/#handbook-guidelines). For questions on who to submit a merge request to, or assistance with the handbook, please reach out on the `#handbook` Slack channel.

If you need permissions to directly merge changes to the handbook, please submit a [New Access Request](https://gitlab.com/gitlab-com/team-member-epics/access-requests) issue and follow the process for access approval. Request a 'Maintainer' role under www-gitlab-com. See [here](https://docs.gitlab.com/ee/user/permissions.html) for a full description of roles and permissions.

## KPI

The Engineering team and all sub-teams track Handbook Update Frequency as a [KPI](https://about.gitlab.com/company/kpis/#engineering-kpis), with varying targets per team. Currently, Engineering is the only Division tracking Handbook update frequency, so as to analyse and observe the effectiveness of this KPI.

## Screenshot the handbook instead of creating a presentation

Presentations are great for ephemeral content like [group conversations](https://about.gitlab.com/handbook/group-conversations/) and board presentations. [Evergreen content](https://www.thebalance.com/what-is-evergreen-content-definition-dos-and-don-ts-2316028) like a [leadership training](https://about.gitlab.com/handbook/leadership/#training) should be based on the handbook. This is an important element of [working handbook-first](https://about.gitlab.com/company/culture/all-remote/handbook-first-documentation/).

In the creation of presentations for evergreen content, please screenshot the handbook and provide links to displayed pages rather than copy and pasting content (or formatting a slide specifically to mirror handbook information). This approach shows a [bias towards asynchronous communication](/handbook/values/#bias-towards-asynchronous-communication), and rationale for this is below.

1. It saves you the effort of needing to both update the handbook and create content for a presentation; the handbook is checked and improved as part of the preparation instead of extra work
1. The handbook will stay up to date so people don't look at an outdated information in a presentation
1. Seeing screenshots will confirm to people the content is in the handbook and it is up to date there
1. People get used to the structure of the handbook and can more easily find the relevant handbook section later on
1. The content is open for everyone to contribute to when it is in the handbook
1. The content is integrated with the rest of our processes and shown in context
1. Many more people will consume the content on a webpage than a presentation because it is easier to search and link
1. You're helping other organizations and students around the work by giving them an example how we do it
1. Also see some of the [advantages of using our handbook](/handbook/handbook-usage/)

The presentation will look less polished, but the advantages outweigh that concern.

If a synchronous presentation is required, default to sharing your screen and viewing live handbook pages over a slide presentation.

## Make it worthwhile

Another company asked how we managed to work with the handbook because at their company it wasn't working: "There are many occasions where something is documented in the knowledge base, but people don't know about it because they never bothered to read or search. Some people have a strong aversion against what they perceive as a 'wall of text'."

We attempt to cover this in GitLab's [guide to embracing a handbook-first approach to documentation](https://about.gitlab.com/company/culture/all-remote/handbook-first-documentation/).

To ensure that people's time is well spent looking at the handbook we should follow the 'handbook guidelines' above, and also:

1. Follow the [writing style guide](/handbook/communication/#writing-style-guidelines)
1. Have a great search function (we use Algolia), plus make it public so you can [Google search](/handbook/tools-and-tips/searching/)
1. Test people on their [knowledge](https://about.gitlab.com/company/culture/all-remote/learning-and-development/) during onboarding
1. Give real examples
1. Avoid corporate speak, describe things like you're talking to a friend. For more, see our communications guide on [Simple Language](/handbook/communication/#simple-language).

## Wiki handbooks don't scale

Company handbooks [frequently start as wikis](https://about.gitlab.com/company/culture/all-remote/handbook-first-documentation/#tools-for-building-a-handbook).
This format is more comfortable for people to work in than a static website with GitLab Merge Requests and GitLab Pages.
However wikis tend to go stale over time, where they are badly organized and get out of date.

In wikis it is impossible to make proposals that touch multiple parts of a page and/or multiple pages. Therefore it is hard to reorganize the handbook. Because GitLab Merge Requests and GitLab Pages are based on distributed version control you can split the role of submitter and approver. This allows for a division of work that keeps the handbook up to date:

- Anyone who can read the handbook can make a proposal
- Leaders (who tend to be short on time) only have to approve such a proposal

Wikis also do not encourage collaboration on changes, because there is no way to discuss a proposed change like there is with merge requests.

Some wikis make it hard to view and/or link to diffs of changes, which is needed to communicate decisions.

### Sid and Paul Discussion on the benefits of markdown handbooks and limitations of wikis

<figure class="video_container">
  <iframe src="https://www.youtube.com/embed/eLc8PlD_ucw" frameborder="0" allowfullscreen="true"> </iframe>
</figure>

## External use of the Handbook

Remember that, like virtually everything we do, our handbook is [open source](https://about.gitlab.com/solutions/open-source/), and we expect that other companies may use it as inspiration for their own documentation and practices. That said, the handbook should always be specific on **what we do**, not **who we want to be**, and every company will need to fill out their own handbooks over time. Our handbook falls under the [Attribution-ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/).

### Inspired by GitLab

If your company has been inspired by GitLab's handbook, we would love to know what inspired you. Please see our [Inspired by GitLab page](/handbook/inspired-by-gitlab/).

## Searching the Handbook

Every GitLab Handbook page has a search field near the top of the page for searching.
See the [Searching GitLab like a pro](/handbook/tools-and-tips/searching/) page for tips on searching the handbook faster and more efficiently.

## Having Trouble Contributing to the Handbook?

If you run into trouble editing the GitLab Handbook there are various means of help available.

Team members, referred to as [MR Buddies](https://about.gitlab.com/handbook/people-group/general-onboarding/mr-buddies/), are available to help you create a merge request or debug any problems you might run into while updating the GitLab Handbook. Some common questions are covered in the videos in the [MR Buddies playlist](https://www.youtube.com/playlist?list=PL05JrBw4t0KrCVFOwSGW6M3k16yLtPO1M).

For [more serious problems](/handbook/about/on-call/#when-to-escalate-an-issue), especially ones that are time sensitive or prohibiting access to important information, there is an [escalation process](/handbook/about/on-call/) to reach out to team members who are on-call to help resolve the problem.

## Merge Rights Guidelines

You need [`maintainer` access](https://docs.gitlab.com/ee/user/permissions.html#project-members-permissions) to the [`www-gitlab-com` project](https://gitlab.com/gitlab-com/www-gitlab-com/) to be able to merge MRs for the handbook. If you want merge access, fill out an [access request](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/access-requests/). This page contains some tips and guidelines that you should keep in mind when you have `maintainer` access.

### Merge with confidence

Even if you are not a developer, you should feel confident merging any changes that pass the pipeline without worrying that you will break the handbook. The tests in the pipeline are designed to catch any major problems. The  `www-gitlab-com` project is configured so that changes cannot be merged unless the pipeline passes. When in doubt, feel free to loop in a technical reviewer. You can ask for help in the `#mr-buddies` slack channel. MR Buddies can provide a technical review or help you fix a broken pipeline. In the event that code is merged that does break the handbook in some way, follow the instructions for [reporting an issue to the Handbook on-call team](/handbook/about/on-call/).

### Do not use merge immediately

Do **not** use the [merge immediately](https://docs.gitlab.com/ee/ci/pipelines/merge_trains.html#immediately-merge-a-merge-request-with-a-merge-train) feature! Even if your MR is important and time-sensitive, using this feature will create a lot of pain for everyone else. This feature should only be used when critical public information needs to be sent live as quickly as possible and should be approved by PR or Legal. **If you don’t have PR or Legal approval, don’t use this feature**.

More context on the technical reasons behind this:

- We want to have a fast pipeline for the master branch, which minimizes the time needed for changes to be deployed and appear live on the production site.
- In order to achieve this, we do not run any tests or linters on the master branch, because these are long-running jobs which would block a fast deployment.
- Instead, we rely on the [Merge Train](https://docs.gitlab.com/ee/ci/pipelines/merge_trains.html) to ensure that all Merge Request changes have successfully passed all necessary test/lint jobs before being allowed to merge.
- So, if you use "merge immediately", ***none of the test/lint jobs will be run, which will result in a broken master branch if problems were introduced.***
- This means that **everyone who creates new MRs off of master after this point will experience confusing pipeline failures which are not their fault**, and this will continue until this situation is discovered and a fix is merged to master.

### When to get approval

Getting pinged to approve every small change to your page can be annoying, but someone changing a policy or procedure in the handbook without proper approval can have strong negative consequences. Use your best judgement on when to ask for approvals.

Whenever reasonable, practice [responsibility over rigidity](/handbook/values/#freedom-and-responsibility-over-rigidity). When you expect a page owner will appreciate your changes, go ahead and merge them without approval. Always ping the code owners with an @mention comment to inform them of the changes. They will be happy their page was made better and they didn’t need to waste time reviewing and approving the change. In the event that something isn’t an improvement, we practice [clean up over sign off](/handbook/values/#cleanup-over-sign-off).

Whenever appropriate, e.g. publishing a previously internal-only document, get approval from the [code owner](https://docs.gitlab.com/ee/user/project/codeowners/) using the [approval feature](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/settings.html) before merging changes. Each page in the handbook shows the code owner listed under “Maintained by”. This information is pulled from the [codeowners file](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/.gitlab/CODEOWNERS). The page’s code owner is the DRI for the page and has the final say for what appears in the handbook. When in doubt, get the DRI’s permission before changing their page. Don't worry if the DRI is a C-level person. You can still assign your MRs to them, even if you are an individual contributor. This is because we prefer to [communicate directly](/handbook/communication/#communicate-directly).

### Have a peer review your changes

Unless it’s a small change like a typo, always have another team member review your changes before you merge them.

### Access to the website, blog, and handbook

The [`www-gitlab-com` project](https://gitlab.com/gitlab-com/www-gitlab-com/) contains the blog, marketing website, and handbook. As a maintainer, you will have access to all three. In most cases, you should only merge changes to the handbook and loop in the marketing team for any MR related to the blog or marketing site.

For example, don’t merge blog posts without following the process outlined in the [Blog handbook](https://about.gitlab.com/handbook/marketing/blog/). Publishing on the marketing blog requires approval from the Editorial Team. Note, [anyone can write and publish](https://about.gitlab.com/handbook/marketing/blog/unfiltered/) a blog post for [GitLab’s Unfiltered Blog](https://about.gitlab.com/handbook/marketing/blog/unfiltered/).

Similarly, don't merge website updates without marketing in the loop. Follow the [instructions for updating the website](https://about.gitlab.com/handbook/marketing/digital-experience/website/#updating-the-marketing-website) or [requesting help from the marketing team](https://about.gitlab.com/handbook/marketing/digital-experience/#requesting-support).

### Broad Permissions

Being a maintainer gives you access to much more than just the ability to merge. You can see a [full list of permissions](https://docs.gitlab.com/ee/user/permissions.html#project-members-permissions) in the docs. Keep in mind that you’ll have access to a broad set of settings and configuration for the project. Don’t adjust any settings or make any structural changes without approval from the [marketing Digital Experience team](https://about.gitlab.com/handbook/marketing/digital-experience/).

### Granting others maintain access

Do not grant people maintainer access without an [Access Request](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/access-requests/). As a maintainer you have the ability to grant others maintainer access. Don’t do so without following the Access Request process to garner the appropriate approvals and create the necessary documentation.

### Description Templates for Issues and Merge Requests

The [description templates](https://docs.gitlab.com/ee/user/project/description_templates.html) for issues and merge requests in the `www-gitlab-com` project are respectively located in the [.gitlab/issue_templates](https://gitlab.com/gitlab-com/www-gitlab-com/-/tree/master/.gitlab/issue_templates) and [.gitlab/merge_request_templates](https://gitlab.com/gitlab-com/www-gitlab-com/-/tree/master/.gitlab/merge_request_templates) directories, and can be edited and changed with a new merge request.

Changes to the default templates in `Default.md` require review by the [Chief of Staff Team to the CEO](https://about.gitlab.com/handbook/ceo/chief-of-staff-team/) or the [CEO](https://about.gitlab.com/handbook/ceo/). See [.gitlab/CODEOWNERS](https://gitlab.com/gitlab-com/www-gitlab-com/-/tree/master/.gitlab/CODEOWNERS) for the current list of approvers.

- [Default merge request template](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/.gitlab/merge_request_templates/Default.md)
- [Default issue template](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/.gitlab/issue_templates/Default.md)

You can create a new issue with a specific description template using the following URL syntax:
- `https://gitlab.com/gitlab-com/www-gitlab-com/issues/new?issuable_template=name-of-template`
