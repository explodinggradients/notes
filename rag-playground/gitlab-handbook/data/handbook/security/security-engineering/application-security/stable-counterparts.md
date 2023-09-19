---
title: "Application Security Stable Counterparts"
---

The overall goal of Application Security Stable Counterparts is to help
integrate security themes early in the development process. This is intending
to reduce the number of vulnerabilities released over the long term.
These Stable Counterparts can be found on the
[Product Categories page](https://about.gitlab.com/handbook/product/categories/#devops-stages),
next to the "Application Security Engineer" mentions.

## Technical Goals

- Assist in threat modeling features to identify areas of risk prior to
  implementation
- Code and [AppSec reviews]({{< ref "appsec-reviews" >}})
- Provide guidance on security best practices
- Improve security testing coverage
- Assistance in prioritizing security fixes
- Provide technical guidance on security fixes

## Non-technical Goals

- Enable development team to self-identify security risk early
- Help document and solve pain points when it comes to security process
- Identify vulnerability areas to target for training and/or automation
- Assist in cross-team communication of security-related topics
- Assist development teams with security related compliance and regulatory audits

## Adding & Updating Stable Counterparts

Stable Counterparts can be added or updated by following these steps:

- (Optional) Organise a 1:1 with the group(s) and App Sec engineer(s) involved to discuss handover, learning opportunities, upcoming priorities, and practicalities like links to GitLab Issue Boards and meeting invitations
- Open an MR to [gitlab-com/www-gitlab-com](https://gitlab.com/gitlab-com/www-gitlab-com/-/merge_requests/)
    - Add or update `data/stages.yml`, setting the `appsec_engineer` attribute to `Firstname Lastname` in each group
    - For each App Sec Engineer involved, update the `role` attribute in `data/team_members/person/DIVISION/LETTER/PERSON_NAME.yml` to include `STAGE_NAME (GROUP_A, GROUP_B)`

## Success Stories

There are cases where the Application Security team isn't involved as at the level that the
security team would like to, and many factors can lead to that situation. In cases where one
is the Stable Counterpart it can be even more difficult to stay up to date on what is happening
on each group.

One change in how to approach that for some team members was to **setup bi-weekly sync meetings
with a member of the engineer team and discuss security releated topics**. This has started to
work on the first meeting and enabled the Application Security to cover important issues that would
not necessarily be seen without this change.

On other cases setting up **regular meetings with a dedicated engineer on a very specific topic**
may also help in staying up to date. In doing that we were able to review issues on
new important planned features.

Here are some verbatim answers, capturing how AppSec does (or did) Stable Counterparts in May 2023.

### Vitor

- How do/did you get started with your stable counterpart groups?
  - For all the stable counterparts I had, I always started the first discussion with the Product Manager and/or the Engineering Manager. Usually I go for the EMs, but both should provide useful infos about upcoming features and important topics for us to be aware of.
- How do you maintain relationships with them?
  - I had a bi-weekly meeting where we do a sync on the current work, check on questions regarding ongoing reviews, upcoming work. While the first meeting is with the PMs/EMs, the bi-weekly I had a mix of it being with EMs or Senior/Staff engineers. This is really based on timezone availability where it helps to catchup live. In my opinion this is the most important aspects of our work with them and maintaining a good relationship really helps in being involved as if we were a team member.
- How do you keep track of the work they're doing?
  - I used my 1:1 with my manager to do a status update on the ongoing reviews if it was necessary (usually for important reviews, not for everything), as well as a file where I noted on what I was working (todo list). I could have use a repo on GitLab too with a MD file for example, or used issues to track what I needed to do too.
- How do you get involved in the work they're doing?
  - The bi-weekly syncs are really helpful because they allowed me to get to know the upcoming work and plan accordingly. That allowed me to do few threat models ahead of the review. Another thing is to check for issues using the group's labels combined with `Security` for example.
- How do you get familiar with the work they've done / their code?
  - It came with time. The more I spend doing reviews for a particular group the more I got comfortable with the code and was familiar with some particular functions. One thing to remember is to not be afraid to ask questions when we do code reviews if the code is not clear to us.
- How do you balance this with other work?
  - My proritisation was the following (by order of importance): Rotations, stable counterpart work, OKRs, other initiatives. If my manager asked me to jump on something top priority then this was obviously taking the priority over anything else (if not on rotation). Of course anything that comes from top management gets prioritised if they are asking us to jump on that with highest priority (examples: an acquisition security review, special ask from my manager and above).

### Dominic

- How do/did you get started with your stable counterpart groups?
    - I introduced myself in Slack and had coffee chats with EMs / PMs, though admittedly when the managers change on those teams I didn't do a good job of keeping that up
- How do you maintain relationships with them?
    - I don't do sync meetings at all, I keep an eye in their Slack channels and we talk a lot in issues because they happen to work on a lot of security-sensitive topics. The "maintenance" happens a bit by itself :sweat_smile:
- How do you keep track of the work they're doing?
    - Slack channel for the section, issues filtered by Milestone
- How do you get involved in the work they're doing?
    - Most of the time they ping me, but I keep an eye on issues and MRs I've already been pinged in and keep reading discussions and will often jump in without being re-pinged. I keep up with existing issues and MRs via my emails.
- How do you get familiar with the work they've done / their code?
    - When I'm pinged for a review I take whatever time needed to understand the context. If that means reviewing 5 other MRs that introduced the feature, setting up GDK to play with it and asking a few questions then so be it! I make it clear when I'm not familiar with something and I need ramping up so the expectations are clear.
- How do you balance this with other work?
    - I would say this is my highest priority "non-urgent" work. Incidents and time-sensitive requests will be handled first but other than that I'll do my SC work.

### Greg A

- How did you get started with your stable counterpart groups?
  - After taking on a SC, I read the handbook about their direction and what they're working on, and then added my name. From there, I typically set up a chat with the EM to discuss any questions I have, sore spots from a security perspective, and what they hope to gain from the SC program. We articulate expectations to each other and go from there.
- How do you maintain relationships with them?
  - Mostly through Slack. I try to be a constant presence in the smaller teams. For the larger teams, I just lurk in the Slack channel and then communicate one-on-one with the individual who pings me the most for MRs.
- How do you keep track of the work they're doing?
  - Again, mostly through Slack. I'm not incredibly in-tune with every group's work. I do keep tabs on them as most channels have some degree of announcement feature. If I notice that a group has gone completely dark on me, then I'll ping someone to figure out what is going on.
- How do you get involved in the work they're doing?
  - Mostly through pings. The relationship is heavily dependent on them looping me in and me providing a useful answer that will satisfy them for pinging me. Responses to pings are a huge determinant in how the relationship is forming.
- How do you get familiar with the work they've done / their code?
  - I typically don't dive into their work right from the beginning. Most of my familiarization happens during the first couple of MRs and reviews. I take time on my first couple of assignments to explore what they're working on and try to understand the boundaries of their group responsibilities. I ask lots of questions during the first couple of reviews.
- How do you balance this with other work?
  - I consider SC work as my "primary job." When I create a schedule for the day, I prioritize this type of work over other things and really do my best to ensure that I get approvals/comments out as efficiently as possible.

### Nikhil

- How do/did you get started with your stable counterpart groups?
  - I introduced myself in the slack channel and their team meeting(async) and scheduled a coffee chat with EM.
- How do you maintain relationships with them?
  - Monthly sync meeting with EM, slack and issue pings. I try to glance through their slack channels from time to time.
- How do you keep track of the work they're doing?
  - Planning issues, issue board and sync meetings.
- How do you get involved in the work they're doing?
  - Most of the time I get pings in issue/MR or slack.
- How do you get familiar with the work they've done / their code?
  - MR reviews and discussion in feature implementation issue.
- How do you balance this with other work?
  - I try to give priority to SC work unless there is an incident or I'm handling a security release.

### Nick

- How do/did you get started with your stable counterpart groups?
  - I set the expectation with my groups to please ping me with @ mentions proactively. This leads to MR reviews, epic/issue discussions, and occasionally threat modelling.
  - I ask to be added to team meetings, primarily to get access to the Google Doc.
- How do you maintain relationships with them?
  - At least once a month I'll try and talk to at least one person from my SCs where there is timezone overlap. Usually just a coffee chat that can veer into work if needed.
- How do you keep track of the work they're doing?
  - I join their slack channels, and skim read the conversations each day.
  - I bookmark each team's issue board. Once or twice a month I review the board. I pay particular attention to epics in the design phase (get in early), and to issues which are soon to be / have been merged (better late than never)
  - Each release I'll review their planning issue if they have one
  - On an ad-hoc basis I'll read/watch team meetings, watch demos on YouTube, etc
- How do you get involved in the work they're doing?
  - As above, via reactive pings or proactive board / Slack monitoring
- How do you get familiar with the work they've done / their code?
  - In MR reviews I am comfortable asking questions. I'll try to understand the code, but the team knows it best and asking "silly" questions up front can speed up getting a better understanding
  - After H1 issues, or MR reviews, I might have noticed "code smells". I put time in my calendar to dig into these later. This also helps build familiarity with the code.
  - If I see an opportunity for defense-in-depth, I'll create the MR myself. Again this builds familiarity with the code, and also with the release processes.
- How do you balance this with other work?
  - When on a rotation I largely ignore proactive Stable Counterpart work and solely rely on reactive responses to pings
  - When not on rotation, it's probably 50% SC and the other 50% on everything else (OKRs, handbook updates, working either on the main product or the handbook, G&D, etc)
