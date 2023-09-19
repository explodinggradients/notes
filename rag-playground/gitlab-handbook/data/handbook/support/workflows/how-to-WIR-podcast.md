---

title: How to do a WIR Podcast
category: References
description: General guide for creating a Support Week-in-Review Podcast
---



### Overview

Use this workflow as a general guide when you want to record and publish a Support Week-in-Review Podcast.  

Much of this is done in the [Support Week in Review Project](https://gitlab.com/gitlab-com/support/readiness/support-week-in-review).  For more information about the CI/CD jobs used in this guide and what they do, refer to the project [readme](https://gitlab.com/gitlab-com/support/readiness/support-week-in-review/-/blob/main/README.md).

---

### Workflow

1. Check the Support Team Google calendar for the recording session (near the end of the week).
1. Determine who will be responsible for each of the following roles. One person can be responsible for them all.
   - Editor:
      - Before the Recording:
         - Prepare the SSAT input
            - view the SSAT issue in the [SWIR project](https://gitlab.com/gitlab-com/support/readiness/support-week-in-review/-/issues).  If there is no content, run `populate_ssat` pipeline - this will gather any open positive SSAT into the SSAT issue
            - review the content (automated or other) and make corrections and remove anything that is not actually positive. If there is a lot of content, consider reducing the number down by removing some that are short and not personalised - use your judgement here.
         - prepare the digest issue
            - run the `create_digest_issue` job.
            - edit the digest issue and add a phrase of the week
            - work with the Metrics Analyst (below) to ensure the metrics section is populated
      - After the recording
         - [Publish](#publishing-the-podcast) the podcast
         - [Update](#update-the-legacy-swir-gdoc) the legacy Support Week in Review gdoc
         - [Prepare SWIR for the next week](#prepare-swir-for-the-next-week)
   - Metrics analyst:
      - take screenshots of the key metrics from the [Support Metrics Dashboard - SWIR](https://gitlab.zendesk.com/explore/dashboard/36925DBD1F5E3C7BA541DB38D11AC51E0EAAFDD30DCB63FDE83CF1389E555D96/tab/10602202) and insert them into the SWIR digest issue. Change your profile timezone in Zendesk to Pacific Time before screen grabbing this so that it is comparable to previous week's graphs (in your Zendesk profile, look for "Time zone" in the left side bar)
      - in text, enter key metrics into the appropriate sections of the SWIR digest issue (US Fed stats are shared by a manager in the private channel spt_managers-internal - copy and paste these in if you have access. Alternatively ask a manager to copy these to you in Slack. It is also ok to proceed without them on occasion if necessary).
      - gather pairing data by observing the number of issues against the current [pairing milestone](https://gitlab.com/groups/gitlab-com/support/-/milestones?search_title=pairing&state=&sort=) and compare to the previous week's digest issue data for the week on week (WoW) metric
      - read and record this section during the recording call
   - Narrator(s):
      - analyze the content of the section you'll be narrating: click on each link and understand what is being expressed by the point
      - read and record the content of the point
      - by convention, we verbalize issue and MR links by reading out their project name and number, such as "Support Team Meta 1234", or "Handbook MR 4321". You can see these while narrating by hovering over the link. This is particularly important when the item has a "here-link" such as "see **this issue**".
1. Join the Zoom room
1. Determine speaking order for Narrators. A useful set of conventions is:

- Read in alphabetical order by your first initials.
- If you have an item and it comes up, you will read it which will reset the order.

1. When everyone is ready, begin recording. It's easiest for the Editor to "Record locally", as they'll have the audio on their computer for upload.
1. When finished recording, the Editor will [publish](#publishing-the-podcast) and prepare the project for the next week.

#### Publishing the Podcast

Once you have the compiled audio:

1. Optional: add the theme music to the recording if you have it
1. Upload it to the [Support Week in Review - Audio Edition](https://drive.google.com/drive/search?q=Support%20Week%20in%20Review%20-%20Audio%20Edition) folder
1. Change the Sharing Settings to "Anyone within GitLab can View"
1. Copy/paste the URL into the Digest Issue below the TOC (use the format: `:speaker: [Audio edition](url)`)
1. Share the final mix into Slack (there is a slackbot reminder in #support_team-chat at 23:00 UTC on a Thursday - you can share the audio link as a threaded reply to that conversation)

#### Update the legacy SWIR Gdoc

1. Copy the contents of the Digest issue starting from below the TOC
1. Paste it into the [legacy SWIR doc](https://drive.google.com/drive/u/0/search?q=support%20week%20in%20review%20SWIR)
1. Manually add the date and phrase of the week as a level 1 heading
1. Manually paste in the metrics graph

#### Prepare SWIR for the next week

1. Run the `close_week_and_create_new_milestone` pipeline
1. Check pagerduty or the [Support Team Page](https://gitlab-com.gitlab.io/support/team/oncall.html?search=ssat) to find the incoming SSAT manager (the one starting on the current Thursday) and reassign the new Positive SSAT issue to them.
1. You're done!
