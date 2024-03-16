---
title: "Direction"
---

## Overview

The [GitLab Handbook](/handbook/) is the single source of truth for how we operate at GitLab, including processes, policies, and product direction. In keeping with our [value of transparency](/handbook/values/#transparency), the GitLab Handbook is entirely open to the world. We welcome feedback from the community and hope that it serves as [inspiration](/handbook/inspired-by-gitlab/) for other current or future companies. The GitLab Handbook is also an incredible talent acquisition tool, providing candidates with valuable insight into how GitLab runs as a company.

A sub-section of the [about.gitlab.com](https://about.gitlab.com) website, the GitLab Handbook specifically refers to content that is in the `/handbook/` namespace of the website. The overall user experience and architecture of the GitLab Handbook is a shared responsibility across groups, however specific feedback or questions can be directed to [Marshall Cottrell](https://gitlab.com/marshall007), Technical DRI for the [Content Sites](/handbook/content-websites/) and member of the [Chief of Staff Team to the CEO](https://about.gitlab.com/handbook/ceo/chief-of-staff-team/).

### Target Audience

**GitLab Team Members:** Every GitLab team member is responsible for using and updating our handbook. It is the central repository for process documentation and product direction.

**Leadership:** GitLab leadership uses the handbook like any other member of the team, but additionally needs to reference the content during presentations to stakeholders or investors. Since everything we do is open to the public, members of leadership teams outside of GitLab may also use the GitLab Handbook as reference or inspiration for their own team processes and policies.

**Potential Applicants:** Candidates for job opportunities at GitLab use the handbook to learn more about expectations for the role, compensation and benefits, GitLab's company values, and other policies. GitLab team members also use the handbook extensively to share specific, relevant information with potential applicants, making it a powerful talent acquisition tool in itself.

**Current and Potential Users:** GitLab's product direction, strategy, and vision are documented in the handbook alongside our product and engineering processes. This allows current users a glimpse into GitLab's future priorities and can help potential users make an informed decision related to adopting GitLab as a tool.

## Where we are Headed

At GitLab, we encourage everyone to work [handbook first](https://about.gitlab.com/handbook/handbook-usage/#why-handbook-first) in order to promote asynchronous collaboration and documentation. Working this way has its challenges, not the least of which is the time and effort involved in making a change. While this extra investment can encourage contributors to be more considered and deliberate with their changes, at a certain point it discourages meaningful collaboration and works against our goals.

Making a change to the GitLab Handbook requires either building and running the site locally or using the Web IDE, both of which can be intimidating for less technical users. Once a change has been made, the current build process for the GitLab Handbook makes it difficult to predict when a change will be deployed, often taking between 10 and 45 minutes.

Our hope is that the GitLab Handbook is something that others want to emulate. To facilitate that, we are investigating ways we can templatize the handbook itself and make it something that any user can install at a group level. To get there, we need to have:

- Incredible, organized, and up-to-date content
- Fast, predictable deployments within a couple of minutes of making a change to a single page
- Sharing tools for spreading the word about GitLab on social media
- A clean, scalable information architecture and modern codebase

### What's Next & Why

- **[Monorepo refactor:](https://gitlab.com/groups/gitlab-com/-/epics/282)** The [`www-gitlab-com`](https://gitlab.com/gitlab-com/www-gitlab-com/) project is home to multiple sub-sites including the blog, our marketing pages, and the GitLab Handbook which all deploy to the [about.gitlab.com](https://about.gitlab.com) domain. In order to ensure stability, accountability, and efficiency, we are working to separate and isolate these sub-sites into distinct projects within the main project. This will allow us to implement separate CI pipelines for each project, so that changes will only build, test, and deploy the relevant project.
  - Digital Experience has [completed their initial rearchitecture](https://about.gitlab.com/handbook/marketing/digital-experience/marketing-site-rearchitecture-project/), splitting the first batch of marketing pages to the [`gitlab-com/marketing/digital-experience/buyer-experience`](https://gitlab.com/gitlab-com/marketing/digital-experience/buyer-experience) project.
  - Migration of handbook content to [handbook.gitlab.com](https://handbook.gitlab.com/) is now underway.  You can read more details about this on our [handbook migration plan page](/handbook/about/roadmap/).
- **[Pipeline performance improvements:](https://gitlab.com/groups/gitlab-com/-/epics/255)** Getting the build and deploy time down to a reasonable level is one of the most important things we can do to encourage more collaboration among users already familiar with how to edit the handbook. Recent efforts have reduced the average build and deploy time by over 50% but there are still opportunities for further optimization, mostly around reducing the overall size of the project repository.
- **Evaluate Hugo as a replacement for Middleman:** We have already [ported the internal handbook to Hugo](https://gitlab.com/internal-handbook/internal-handbook.gitlab.io/-/merge_requests/549) and reduced build times by ~100x (from 3min to 16sec). The public handbook is significantly more complex and we will need to develop an incremental migration strategy.
- **[Improved reading and sharing experience:](https://gitlab.com/groups/gitlab-com/-/epics/326)** The content needs to remain the primary focus but it should be easier to search, navigate, and share the content.
- **[Freshness tools:](https://gitlab.com/groups/gitlab-com/-/epics/325)** To ensure that content is relevant, up-to-date, not duplicative, and to give readers the tools they need to flag content that doesn't meet those criteria.
- **[Leverage Workday for team member metadata](https://gitlab.com/gitlab-com/people-group/peopleops-eng/compensation-calculator/-/merge_requests/457#note_1039047670):** Workday is the SSoT for team member profile data. We will eliminate dependencies on YAML files in the git repos and instead rely on exports from Workday.
- **Improve Internal Communications:** create an internal "news feed" as the source of truth for internal communications. Currently we have multiple internal communication channels (email newsletters, various slack channels) making it difficult for team members to stay informed and cut through the noise.
- **Other Low-Priority Tasks:** see [this Google doc](https://docs.google.com/document/d/1jGhIzY6UgLnDsH6Nbb-Q8ioJWVD0L0ml0o59YEuUWco/edit) (internal only)

### What is Not Planned Right Now

We are not currently investigating a transition to a separate, external content management system or publishing platform.

The needs of the GitLab Handbook [have outgrown what can be handled in a wiki](https://about.gitlab.com/handbook/handbook-usage/#wiki-handbooks-dont-scale) (or similar) product, so we are not planning to migrate any content into that format.

Since the content is [changing quite literally every day](https://gitlab.com/gitlab-com/www-gitlab-com/-/commits/master/), we are not looking to generate a digital or printed book from the GitLab Handbook content.

The GitLab Handbook is not currently optimized for serving as a searchable Knowledge Base or FAQ repository similar to what you would find on [Quora](https://www.quora.com/) or [Stack Overflow](https://stackoverflow.com/). The problems to be solved in those areas are likely to be addressed by the [Knowledge group](https://about.gitlab.com/handbook/product/categories/#knowledge-group).
