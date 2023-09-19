---
title: "Handbook Support"
description: "How to get support when contributing to GitLab Handbook"
---

When contributing to the GitLab Handbook you might run into situations that requires some further support to resolve. The sections below cover common scenarios that team members run into and provides information on how to deal with it.

## How to solve a broken pipeline in a merge request

<figure class="video_container">
  <iframe src="https://www.youtube.com/embed/PeopYsoweGU" frameborder="0" allowfullscreen="true"> </iframe>
</figure>

*In the [GitLab Unfiltered](https://www.youtube.com/channel/UCMtZ0sc1HHNtGGWZFDRTh5A) video above, two colleagues share their screens and walk through the process detailed below.*

---

If you create a merge request during a period where there is an issue in master causing [pipelines to fail](https://about.gitlab.com/blog/2019/09/11/how-to-avoid-broken-master-with-pipelines-for-merge-requests/), you'll notice that failures will continue to occur even if you retry pipeline within the GitLab Web IDE interface.

Once the issue in master is fixed, you can solve this by using terminal to merge the latest version of master into your branch (which you can find in your [merge request](https://docs.gitlab.com/ee/user/project/merge_requests/)).

For those who primarily use Web IDE to interface with GitLab, it can feel foreign to engage [locally](https://about.gitlab.com/handbook/git-page-update/). Before diving in deeper, be sure to read our [*GitLab 101 – a primer for the non-technical*](https://about.gitlab.com/blog/2019/08/02/gitlab-for-the-non-technical/) blog post.

The process is fairly straightforward once you have completed the [necessary steps listed in the GitLab Handbook to edit locally](https://about.gitlab.com/handbook/git-page-update/).

Once you are properly equipped to edit locally, open a [terminal window](https://about.gitlab.com/handbook/git-page-update/) and execute the following.

1. Navigate to the appropriate project. If you've cloned the project to your root directory, try `cd www-gitlab-com`
1. `git checkout master`
1. `git pull` (This brings in the most recent changes from master to your local machine.)
1. `git checkout MYBRANCH` (Replace `MYBRANCH` with your branch from the merge request. This is easily copied by clicking the **Copy Branch Name** icon to the right of **Request to merge** at the top of your merge request page.)
1. `git merge master` (This takes the changes from master and merges them into your local `MYBRANCH` branch.)
1. `:q` (Entering `:q` followed by a **Return keystroke**  quits vim which is the editor your terminal opened when adding the stock commit message to the merge.)
1. `git push` (This takes local machine files and pushes to the cloud.)

Once this has been executed, you'll see new commits added to your merge request, and the pipeline will automatically begin to re-run. If completed correctly, the pipeline will pass now that the latest master was merged into your branch.

If you are a GitLab team member and you get stuck, please ask for help in the `#mr-buddies` Slack channel.

### Debugging a failed pipeline in the GitLab handbook

{{% youtube id="WlgH-6cX1k8" title="Debugging a failed pipeline on the Handbook" %}}

*In the [GitLab Unfiltered](https://www.youtube.com/channel/UCMtZ0sc1HHNtGGWZFDRTh5A) video above, Jean shares a quick overview of how to go about identifying why a pipeline might be failing for a merge request to the GitLab handbook.*

### Why is my pipeline failing?

If you've made a merge request, only to see that your pipeline has failed, a troubleshooting process begins.

You can learn more about why pipelines fail, what failures mean, and how to resolve conflicts by viewing this [explainer video](https://youtu.be/Qg0ICfs_Noo) hosted on GitLab Unfiltered.

### Where do I report handbook issues and request help?

#### Important Update

**See [Content Websites Responsibility](/handbook/content-websites/) for the latest information about the DRI and support processes for the about.gitlab.com site.**

#### Reporting handbook issues and requesting help

For those inside the GitLab organization, you can request help on individual merge requests via [Merge Request Buddies](https://about.gitlab.com/handbook/people-group/general-onboarding/mr-buddies/) in the `#mr-buddies` Slack channel.

If you suspect a systemic issue, inquire in the `#handbook-escalation` Slack channel, and check to see if others are reporting similar errors in `#is-this-known`. For more information refer to the [Handbook On-Call page](/handbook/about/on-call/).

The `#handbook-escalation` Slack channel is used for monitoring and responding to infrastructure and configuration related build issues with the `www-gitlab-com` project master branch. This is an excellent first stop to see if there is an ongoing issue impacting your pipeline.

General GitLab handbook discussion occurs in the `#handbook` channel, while an automated feed of merged handbook updates can be found in the `#handbook-updates` channel.

## Resolving linting errors

To the ensure consistency, quality and correctness of the GitLab Handbook we use various linting jobs that run as part of the pipeline. These jobs check that everything is as it should be, and if they detect something is wrong will cause the pipeline to fail.

### Handbook Links and Anchors

There is a special linter that validates links and anchors across the handbook. If your change accidentally breaks a link, then the pipeline job will fail with a similar error message.

![Link linter error](/handbook/about/images/link-linter-error.png)

1. It is a path to the file where the broken link was detected.
    (filepath - `sites/handbook/source/handbook/total-rewards/benefits/general-and-entity-benefits/pty-benefits-australia/index.html.md`, line number: 87)
1. It is an error message. An anchor `expense-reimbursement` is defined in the file path from step 1 but does not exist in the file path from step 3.
1. It is a path where the header `Expense Reimbursement` needs to be defined. (file path - `sites/handbook/source/handbook/spending-company-money/index.html.md`)

**How to fix the problem**

Double-check that header `Expense Reimbursement` exists in `sites/handbook/source/handbook/spending-company-money/index.html.md`.

If it was moved or renamed, then update the link with the anchor to point to the correct location.

## How to Find and Replace Content

{{% youtube id="lWBkNqxPxw8" title="How to Find and Replace Content in the Handbook using Terminal and a Code Editor" %}}

There are times when you need to find every instance of a word, phrase or link and searching in the handbook online search field is too cumbersome or does not return accurate results. With an code editor and your terminal, you can find and replace content easily and quickly.

**Terminal**

1. Navigate to the appropriate project. If you've cloned the project to your root directory, try `cd www-gitlab-com`
1. `git checkout master`
1. `git pull` or `git pull origin master` (This brings in the most recent changes from master to your local machine.)
1. `git checkout -b MYBRANCH` (Replace `MYBRANCH` with the name of the branch you will be using for your merge request.)
1. Keep your Terminal window open, and now open your code editor (in this example, Visual Studio Code).

**Visual Studio Code**

1. Go to the Search section (View -> Search).
1. Type in the word, phrase or link you are searching for.
1. Type in the word, phrase or link you wish to replace it with in the Replace field, under the Search field.
1. Press the Replace All symbol at the end of the Replace field (or Option-Command-Enter).
1. You will get a pop-up asking you to confirm that you indeed with to `Replace X occurence(s) accross X files with X ?`. If correct, press `Replace`.
*Please note that it is possible to click on a search result to see individual changes and replace only a subset of all occurrences by clicking the replace button next to a given search result only.*

    ![picture-of-vscode-replace](/handbook/about/images/vscode_employee.png)
1. Return to your Terminal.

**Terminal**

1. `git add .` (This will add all your current changes from VS Code.)
1. `git commit -m "Title of your MR"` (Ex. `"Update #peopleops Slack Channel to #people-connect"` and be sure to enter your Title within quotation marks.)
1. `git push`
1. You will get a message in terminal saying `To push the current branch and set the remote as upstream, use` and then there will be a sentence starting with `git push`. Copy and paste this sentence to your most current, active Terminal line, which ends in %.
1. You will see a line in Terminal containing `remote: https://gitlab.com/ ....`. Cut and paste the link starting with https:// to your browser. This will take you to your Create Merge Request page. Now you can continue in your browser as you would when creating a MR in Web IDE.
1. `git checkout master` (This will put you back on master in your Terminal.)

If you are a GitLab team member and you get stuck, please ask for help in the `#mr-buddies` Slack channel.
