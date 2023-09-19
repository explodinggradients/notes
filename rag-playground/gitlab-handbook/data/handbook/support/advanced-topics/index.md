---

title: Advanced Support Topics
description: Training modules that Support team members can complete to gain expert skills.
---



### Support Training Modules

We have several training modules that Support team members can complete to gain expert skills.

#### Creating a Module Checklist

If a topic has a link to **Docs**, you will need to create and document the learning path as you go. Take a look at the [Geo Checklist](https://gitlab.com/gitlab-com/support/support-training/blob/master/.gitlab/issue_templates/Geo.md) for a complete example. Replace the link to the **Docs** with a link to the checklist and put a **(WIP)** after your link to let people know that they won't get the expert badge by finishing the list in its current state.

#### Picking a Topic

Try to pick what the team needs most, thinking back to recent tickets you were not able to answer is usually a good starting point. Inform your manager which one you will be working on, so that they can let you know if there is a different area where the team really needs expertise. Always try to answer tickets on other advanced topics, but when it is time to do some dedicated learning, focus on one area at a time.

#### Earn the Expert badge by completing any of these modules

- [Docker](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Docker)
- [Geo](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Geo)
- Kubernetes [Part 1](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Kubernetes%20Part%201) and [Part 2](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Kubernetes%20Part%202)
- [GitLab CI](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Continuous%20Integration)
- [GitLab API](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20API)
- [LDAP](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=LDAP)
- [High Availability](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=Scaled%20And%20High%20Availability)
- [Git LFS Docs](https://docs.gitlab.com/ee/topics/git/lfs/index.html)
- [Migrate from SVN to Git Docs](https://docs.gitlab.com/ee/user/project/import/index.html#import-from-subversion)
- [GitLab Pages Docs](https://docs.gitlab.com/ee/administration/pages/index.html)

### Deep Dives

The Engineering team, of which Support is a part, has [Deep Dives](/handbook/communication/deep-dives/) to share knowledge about particular topics. The Support team is also encouraged to organize and execute topical deep dives, usually with a support-centric focus.

#### Description

A **Deep Dive** is a session is to share knowledge about a particular topic, with the assumption that those participating already have some basic understanding or aptitude for the given subject. It will have a [Host](#the-host), an [Assistant](#assistant), and multiple [Participants](#participants), each with a role to play from its preparatory to its wind-down phases, but anyone else at GitLab is also welcome to contribute.

Some examples of deep dives would be:

- GitLab Geo on Omnibus (building off the [Geo module](https://gitlab.com/gitlab-com/support/support-training/blob/master/.gitlab/issue_templates/Geo.md))
- ElasticSearch with GitLab (building off [GitLab's ElasticSearch documentation](https://docs.gitlab.com/ee/integration/elasticsearch.html))
- Configure CI for an advanced use case (e.g., Configuring docker-in-docker, using it to build an image, and then optimizing the Docker image build time by utilizing Docker layer caching) (building off the [CI module](https://gitlab.com/gitlab-com/support/support-training/blob/master/.gitlab/issue_templates/CI.md))

#### Goals

The goals of a deep dive are to:

- Rapidly instill in participants a deep understanding of the topic.
- Find and strengthen weak spots in the existing training and/or the product.
- Create a recording that can be easily accessed and watched.

#### Roles and their Responsibilities

##### The Host

As a **host**, you'll lead this deep dive and are expected to have an above-average understanding of the topic. You'll help the [participants](#participants) bring their knowledge of the topic up to a prerequisite level and then build on that knowledge on the call. Afterwards, you'll get help from the [assistant](#assistant) and the other participants to [make some lasting improvements](#artifacts).

While the call itself can be structured as you think it would work best, the following structure for the overall process was created to help meet the [objectives of a deep dive](#goals).

Please start by [creating an issue](https://gitlab.com/gitlab-com/support/support-team-meta/issues) for the deep dive using [its template](https://gitlab.com/gitlab-com/support/support-team-meta/blob/master/.gitlab/issue_templates/Deep%20Dive.md), which will include your tasks. In summary, the issue template will ask that you do a few things:

- Find [participants](#participants) to be your audience
- Find [an assistant](#assistant) to help you with tasks during and after the call
- Give them a few tasks to complete before the call so they come in prepared to ask questions
- Create a Slack channel to communicate with them and help them with their tasks
- Create a Google doc for questions and notes for and from the call
- Record the call

During the call, mention the latest version of GitLab so the recording will have that context. GitLab is iterated upon fast so it's important for those who watch the video in the future to have the relevant context for what they're seeing. Set aside some time to answer questions (from the doc too) so everyone on the call gets a chance to clarify any points of confusion.

Once the call is over, future students of this topic should be able to easily find and watch this recording, so the issue will also ask that you link it in a few places. The participants will also work on [creating artifacts](#artifacts) so please help them where you can.

##### Participants

As **participants**, you are the students of the deep dive. Your ultimate goal is to learn as much as you possibly can from this entire process so you're better equipped to help customers and eventually become an expert.

A deep dive is not meant to be a lecture, but rather a round-table discussion. Everyone is encouraged to bring questions and thoughts on the topic and/or about their experience in going through the existing training. Ideas for improvement in the docs or handbook, spots where more clarity is required, ideas for feature improvements, etc. are all welcome. In order for this deeper level of participation to take place, participants are expected to already be familiar with the basics so this deeper dive into the topic can occur.

You'll have a few tasks to complete before and after the deep dive is complete. The tasks before the call are meant to quickly teach you the basics of the topic, while the tasks after the call are meant to turn your experience from and leading up to the call into lasting changes.

Suggestions:

- A deep dive is a great opportunity to learn a lot about a topic relatively fast. You will have plenty of people to work alongside and ask questions of. Take full advantage of this opportunity to level up.
- Learn as much as you can before the call using the tasks in the issue. This will help you get the most out of the deep dive.
- Ask lots of questions. Ask them in the Slack channel, the Google doc, or just elsewhere in GitLab.
- Keep track of anything lacking in the training materials or the documentation so you can use it to create artifacts later.
- Feel free to pair on any or all of your tasks.

##### Assistant

An **assistant** is a [participant](#participants) that's assigned to the deep dive issue alongside [the host](#the-host). Aside from your role as a participant, your objective is to set the other participants on the right path to [create artifacts](#artifacts).

In summary, the issue template will ask you to take detailed notes during the call and later convert those notes into tasks that the other participants can use to [create artifacts](#artifacts). Once those artifacts have been created and the contents of the Google doc has found its place in a more permanent location, you'll [deprecate it](/handbook/communication/#how-to-deprecate-a-google-doc).

#### Artifacts

To meet [its goal](#goals) of strengthening the product and its training, a deep dive is expected to result in a few artifacts.

The first and most important artifact it'll produce is the link to its recording, made easily accessible.

If it has a [related module](#earn-the-expert-badge-by-completing-any-of-these-modules), another artifact will be the merge request creating a step to watch the recording.

At the end of the deep dive, the resulting notes should be moved from the working Google doc to a more permanent location. This will take the form of issues and/or merge requests.  Here are some examples of what they can look like:

- Issues to create a new feature or file a bug report
- A merge request to clarify something or add some troubleshooting steps to the docs
- An issue to add a new documentation section
- A merge request to update, refine, split, or combine module(s)
