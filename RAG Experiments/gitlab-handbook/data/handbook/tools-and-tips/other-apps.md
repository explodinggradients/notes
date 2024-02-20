---
title: "Other apps"
description: This page lists various apps that may be useful for your workflow at GitLab.
---

### General security tip

Please review our [acceptable use policy](https://about.gitlab.com/handbook/people-group/acceptable-use-policy/).

Some tools and extensions integrate into your various work accounts and will
request certain permissions for them. Please always be cautious of the
permissions requested by the application. For example a GitLab integration that
only requests to be able to read your user profile can be appropriate, however
an integration shouldn't be able to have read or write access the API. Similarly,
you should not input a GitLab [Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
linked to your work account in a third-party tool.

Here are some non-exhaustive guidelines:

- If the application requires credentials (password, access token, etc.) to any of your work accounts (GitLab, Google, Okta, etc.) please do not enter the credentials and remove the application
- If the application uses OAuth, make sure to only allow access to your account if the permissions required by the application are very minimal (such as accessing your public profile)

    ![OAuth authorization screen with profile scope](/handbook/tools-and-tips/images/oauth1.png)

    If the application requires anything such as read-only access to the API or anything that could grant access to confidential data please do not continue the authentication process and remove the application

    ![OAuth authorization screen with profile and read_api scope](/handbook/tools-and-tips/images/oauth2.png)
- When installing something from an "app store" of some sort, look for the reviews, the number of downloads and especially for "badges" that show that the application was reviewed by the app store. For example the Chrome Web Store has a [featured badge](https://support.google.com/chrome_webstore/answer/1050673?visit_id=638011195121439702-999154480&p=cws_badges&rd=1#cws_badges&zippy=%2Cunderstand-chrome-web-store-badges) for popular trustworthy applications
- When in doubt, do not install the application

In any case, you are encouraged to use our [Individual Use Software Request](https://about.gitlab.com/handbook/finance/procurement/personal-use-software/#how-do-i-submit-a-request-for-new-individual-use-software) process prior to installing third party apps.

## Internet browsers

### Ad privacy

Sharing your screen to get your idea across can be very productive, but having personalized ads show up on a webpage may be undesirable.
Shut off interest based ads by setting your preferences.
[Google Ad Settings](https://adssettings.google.com/), [AdChoices](http://optout.aboutads.info)

### Browser extensions

In general, if a particular application or browser extension (sometimes called a plugin) is referenced in the handbook, it is considered "approved".
For example, [1Password](https://about.gitlab.com/handbook/security/#1password-guide) is centered around the browser extension.
Another application is [Zoom](/handbook/tools-and-tips/#zoom), which has a scheduler extension.
However, be sure to search for specific information about the application, in case the desktop version is recommended and the browser extension is not (e.g. [Grammarly](#grammarly)).

If you wish to use an extension not referenced in the handbook, consider the following before installing and using it:

- The extension should be work-related and help your overall productivity.
- The extension should be available from a reputable source, such as the browser's library of approved extensions.
- Ask. Feel free to ask your co-workers about good extensions, and if you have security or privacy concerns about an extension, ask the security team in #security on Slack.

Some browser extensions are listed below

#### Adblockers

Adblockers are browser extensions that can block advertising, prevent user tracking, and include other security-related features.
A popular one recommended by the Security Team is [uBlock Origin](https://github.com/gorhill/uBlock/) which can be installed by following the links below:

- [Chrome](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm)
- [Firefox](https://addons.mozilla.org/addon/ublock-origin/)
- [Edge](https://microsoftedge.microsoft.com/addons/detail/odfafepnkmbhccpbejgmiehpchacaeak)

#### One Tab

[One Tab (Free)](https://www.one-tab.com/) turns tabs into a list which can be sorted and exported.

#### SessionBox

[SessionBox](https://sessionbox.io/discover) is a browser extension that helps you deal with multiple sessions.
It binds a particular session to a tab.
This is particularly useful for testing with different users in the same browser.

#### RSS Feed Reader

If you would like to receive daily notifications on newly opened issues, the Chrome extension [RSS Feed Reader](https://chrome.google.com/webstore/detail/rss-feed-reader/pnjaodmkngahhkoihejjehlcdlnohgmp) is an excellent tool for accomplishing this task.
After installing the extension, access the project page you are interested in following, under the project issues click on the "Subscribe to RSS feed" button which you can find in the top right corner of the page.

### Flash (do NOT use)

**Flash**: Due to security flaws, we strongly recommend *not* using Adobe Flash.
Certainly do not install it on your local machine.
But even the Google Chrome plugin that lets you see embedded Flash content in websites can pose a security hazard.
If you have not already, go to your [Chrome Flash Settings](chrome://settings/content/flash) and disable Flash.
For further context, note that [Google Chrome is removing Flash support soon](https://nakedsecurity.sophos.com/2016/05/18/yet-more-bad-news-for-flash-as-google-chrome-says-goodbye-sort-of/), and while the [plugin is better than a local install of Flash](http://security.stackexchange.com/questions/98117/should-flash-be-disabled-or-are-sandboxes-secure-enough),
it still leaves vulnerabilities for [zero-day attacks](http://www.pctools.com/security-news/zero-day-vulnerability/).

### Prototyping in the browser

Sometimes you only need to capture small textual or visual changes in a web page as part of a bug report or a feature proposal.
You can use [development tools](https://en.wikipedia.org/wiki/Web_development_tools) that are usually built-in in most browsers which allow you to select and edit page element attributes as well as move around page elements like buttons or links.

You can also make the entire web page editable, using the [`designMode`](https://developer.mozilla.org/en-US/docs/Web/API/Document/designMode) attribute, by typing `document.designMode="on";` in the development tools console or creating a bookmarklet by dragging the button below to your Bookmarks Bar.

<a href="javascript:document.body.contentEditable='true'; document.designMode='on'; void 0" class="btn btn-primary">Edit page</a>

## Notes/writing

### Bear

[Bear (Free)](https://bear.app/) is a clean writing tool for notes and long-form writing.
[Ulysses $5/month](https://ulysses.app/) is also a great choice.

### Grammarly

[Grammarly](https://www.grammarly.com) is a good tool for those who want to feel more comfortable drafting written communication in English (American or British).
There is a free and premium version.

<div class="panel panel-gitlab-orange">
**IMPORTANT NOTE FOR GRAMMARLY**
{: .panel-heading}
<div class="panel-body">

Grammarly browser extensions are discouraged, Grammarly will have access to everything you type in your browser, and they have had [a security problem](https://gizmodo.com/grammarly-bug-let-snoops-read-everything-you-wrote-onli-1822740378). If you want to use it to check non-confidential text manually, you should download the [desktop version](https://www.grammarly.com/native/mac) instead. The desktop version is not available for Linux. Refer to [GitLab's Data Classification Standard](https://about.gitlab.com/handbook/security/data-classification-standard.html) for additional details on how data is classified across the organization.

</div>
</div>

### LanguageTool

As an alternative to [Grammarly](#grammarly), we can combine LanguageTool in the browser
with a local LanguageTool server .
This ensures that spell and grammar checking remains both convenient and confidential:

1. Install the [LanguageTool browser extension](https://www.languagetool.org/#firefox_chrome).
1. Either install [LanguageTool as a Homebrew service](https://formulae.brew.sh/formula/languagetool),
   or install [a Docker engine](/handbook/tools-and-tips/mac/#docker-desktop)
   and follow the setup instructions of any
   [LanguageTool Docker image provider](https://github.com/languagetool-org/languagetool#docker).
1. Configure the browser extension under `Experimental settings > Local server`.

### Simplenote

[Simplenote](https://simplenote.com/) is a free, open source note taking app which is cross platform, syncs across all devices, and supports markdown.

## Productivity

### Alfred

[Alfred](https://www.alfredapp.com/) is an application launcher and productivity tool for macOS.
The core app is free to download and use, but the paid [Powerpack](https://www.alfredapp.com/powerpack/) enables more powerful searching, a fantastic clipboard history feature, app integrations, easy access to shell commands, and more.
It's a great tool for developers and general productivity enthusiasts alike.
The clipboard history feature is nicely integrated with many tools, and for example will forget passwords copied from 1Password after they have been pasted.

Alfred adds the ability to create custom searches. Here are two to search the docs and the handbook.

```url
https://docs.gitlab.com/search/?q={query}
```

```url
https://about.gitlab.com/handbook/#stq={query}&stp=1
```

Read [Searching using Alfred](https://about.gitlab.com/handbook/tools-and-tips/searching/#searching-using-alfred-on-macos) to learn more and be able to automatically add them.

There is also [a repo maintained by GitLab team members](https://gitlab.com/gitlab-org/alfred) with GitLab related workflows.

### Brain.fm

[Brain.fm (free trial)](http://brain.fm) provides music specially designed to help you focus, relax, meditate, recharge, sleep (great for plane rides).
It's not just music though.
They use scientifically validated brainwave manipulations to get results.
It is AMAZING and really does work.
Make sure to use with headphones, and give it 10-15 minutes for your brain to get used to it.
($6.95/$15.99/$47.40 per month/quarter/year)

### Calendly

**Note**: Google Calendar has added support to [create appointment schedules](https://support.google.com/calendar/answer/10729749?hl=en),
which are similar to the functionality provided by Calendly.

[Calendly](https://calendly.com/) connects to your Google Calendar so people outside GitLab can easily book a time with you.
If you are scheduling a meeting with a GitLab team-member, please use Google Calendar and follow handbook guidance when [scheduling a meeting](/handbook/communication/#scheduling-meetings).

1. Set up a [Calendly](https://calendly.com/). First sign up with your GitLab email address, then accept the terms and conditions and then authentificate with your Google SSO.
1. Link it to your GitLab Google Calendar to make it possible for people to schedule a call with you.
1. Get your personal meeting room URL by going to [Zoom meeting settings](https://gitlab.zoom.us/meeting), selecting the *Personal Room* tab, and copying the value of *Invite Link* (do not use *Copy the invitation*).
1. If you are using the Basic Calendly Subscription (Unpaid) you will only be able to set-up one event type at a time i.e. either a 15, 30, 45 or 60 minute event - teams making use of one of the Paid Subsciption Tiers such as Customer Support will be able to set up more than one event type.
1. Set up the desired time slot with the following event description text (replacing text in `{}` with your information) we will be using 45 minutes for the illustration purposes below:

> This will be a Zoom Meeting at {Zoom personal meeting room URL}
>
> Question? Please email me. {your GitLab email}

1. Set the event name to `45 Minute Meeting`.
1. Change the event link to `45min`.
1. The event description needs to be copied to the 15, 30 and 60 minute meetings too.
1. If you intend to use any of the other event types, make sure to add this to their event descriptions as well.
1. For people outside of GitLab Inc, send them your Calendly link that links directly to the 45 minute time slot: "Are any of the times on <https://calendly.com/XXXXX/45min/> convenient for you? If so please book one, if not please let me know what times are good for you and we'll find an alternative."
1. Update your availability on [Calendy Event Types](https://calendly.com/event_types/) by clicking the action cog and then the edit option on an event type (For Example: 15 minute meeting) and in the event details clicking on the "When can people book this event?" section then clicking the "Availability" section.
   Here you can set your working hours during which you want to accept meetings, and on the "Advanced" tab you can set the minimum scheduling notice you want enforced.
   Although Calendy does synchronize with Google Calendar to show your availability you may wish to set extra restrictions in Calendy.
   You can use the "Copy Availability From" option on all the other events you have configured one event.

Keep in mind that unlike normal Google Calendar events, Calendly events are not automatically synchronized between both parties when changes are made.
If an event needs to be cancelled or modified, make sure to use Calendly to do so.

### Clockwise

[Clockwise](https://www.getclockwise.com/) is a tool for optimizing your schedule to free up time for you to focus. It will look for opportunities to reschedule meetings when it's most efficient for attendees, and give you uninterrupted time to work. Clockwise integrates with your [calendar](/handbook/tools-and-tips/#google-calendar), and when possible will move events automatically on your behalf.

<div class="panel panel-gitlab-orange">
**IMPORTANT NOTE FOR TEAM MEMBERS USING CLOCKWISE**
{: .panel-heading}
<div class="panel-body">

Clockwise requires specific permissions which allow it to read all calendar invitation data. Team Members who opt to utilize Clockwise should be cognizant about the meeting details (i.e. subject and meeting invite body) included in meetings that are sent from your calendar. Confidential data such as customer names, security specific information like discussion of incidents or bugs should not be included in a calendar title or body, and  instead be kept in a linked agenda, which Clockwise will not be able to read or download. Any data considered non-confidential per [GitLab's Data Classification Standard](https://about.gitlab.com/handbook/security/data-classification-standard.html) can be safely included in meeting invites.

Team Members should also note that by utilizing Clockwise, you inherently agree to providing Clockwise with the ability to view and download your Google Contacts saved to your gitlab.com email account. This will be limited to viewing and downloading information for contacts with an @gitlab.com email alias.

</div>
</div>

### Freedom

If you find yourself switching to websites you find distracting, especially during periods that require focus, and you worry it may affect your productivity, consider using [Freedom](https://freedom.to/why).
Their browser extensions, mobile apps, and desktop apps block distracting websites and apps for the duration of a configurable session.
If you find yourself typing `f` and hitting `enter` from muscle memory, you will not be scrolling through endless pages of photos of your friends' lunches.

### Paste

[Paste for macOS](https://pasteapp.me/) is a clipboard manager that stores everything you copy and optionally syncs across all your devices.
It allows you to organize frequently copied data in pinboards, so that you do not need to copy the same data over and over, provides search, multiple paste and has nice visual user interface.

### Pomodoro technique

The [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) is a simple time management process that can be used to boost productivity by dividing time into "work" and "break" intervals.
In brief, each half-hour block of time is divided into a 25 minute work session followed by a 5 minute break session.
Do this twice per hour until the day is done and marvel at how much you've finished.

Various [Chrome extensions](https://chrome.google.com/webstore/search/pomodoro "Chrome Web Store - pomodoro"), [Firefox add-ons](https://addons.mozilla.org/en-US/firefox/search/?q=pomodoro "Search results for \"pomodoro\" – Add-ons for Firefox (en-US)"), mobile apps, desktop apps, and even fancy physical alarm clocks are available to help you track your intervals, but you can use almost any timer you have on hand&mdash;even and especially that cute little tomato timer in your kitchen.

### Quitter

[Quitter (Free)](https://marco.org/apps) will switch off apps for you after some period of inactivity.
Consider using this to hide Slack after a while to reduce your urge to check new messages all the time. Quitter is only available for the Mac.

### Raycast

[Raycast](https://www.raycast.com/) is a productivity tool similar to [Alfred](#alfred) and Spotlight on macOS. Download the app and select your preferred shortcut. You can also replace spotlight entirely by choosing `cmd + space` as shortcut.

The core app provides many workflows built-in, extensions from the [store](https://www.raycast.com/store) can be installed either directly from the web, or by using the built-in [extension search](https://developers.raycast.com/basics/install-an-extension).

There is [an unofficial extension maintained by GitLab team members](https://www.raycast.com/saschaeggi/gitlab-docs) to search the GitLab documentation, the Handbook, and the Pajamas Design System.

**Please do not use extensions for GitLab using a personal access token (PAT) for security reasons.**

### TripMode

[TripMode ($7.99)](https://www.tripmode.ch/) lets you control which apps can use the internet.
This is especially useful when you're working on a cellular/metered connection. TripMode is only available for the Mac.

## Text editors

### GitHub Copilot

GitHub released [Copilot](https://copilot.github.com), an AI-powered tool for in-situ suggestions within VSCode, in 2021. It’s an interesting and exciting tool. However at this time it does not guarantee that the code being suggested is strictly sourced from codebases governed by [an open source license compatible with our own project](https://gitlab.com/gitlab-org/gitlab-foss/-/blob/master/LICENSE) which could lead to license conflicts. Until the licensing of the suggestions is established, please don't use Copilot.

## Video calling

### Krisp

[Krisp](https://krisp.ai/) will mute background noise when you're in a noisy environment so you can hear and be heard more easily on calls.

### Shush

[$4.99 tool for macOS](http://mizage.com/shush/) that lets you set a hotkey (e.g. `fn`) to mute your microphone ("push-to-talk" or "push-to-mute").
Never again will you have to switch your window focus to Google Hangouts or Zoom to speak or mute.
The icon will show the current state of your mic input (x means muted).
With a right click (or your configured hotkey) you can switch from push to talk to push to mute.
Don't forget to unblock your mic in Zoom/Google Hangouts immediately after joining.
Be warned that page up with fn+down arrow will activate it.
Use space for page down instead of fn+up arrow.
**Warning**: Check your [headset compatility](http://mizage.clarify-it.com/d/jv2enz) before purchase.
Many usb headsets are unmutable.

#### Shush alternative for Linux

If you use Linux (e.g. [Arch](https://www.archlinux.org/), [Ubuntu](https://www.ubuntu.com/) or [Fedora](https://getfedora.org/)) you can create a system-wide keyboard shortcut to mute/unmute your mic.
Please note that it only works for Linux distributions which use [ALSA](http://alsa-project.org) for sounds (most popular Linux distributions use ALSA).
All you need to do is go to your desktop environment's *Keyboard Settings* and create a custom shortcut with the command `amixer set Capture toggle` and assign a key combination of your choice (e.g. `Pause Break` key).
Once this is done, you can mute/unmute your mic using the assigned keyboard shortcut while you're in any application.
Refer to this original answer on [Askubuntu](http://askubuntu.com/a/13364/12242) to learn more.

### Webex

GitLab uses [Zoom](https://zoom.us/) as the primary video collaboration platform for internal and external communications. Some of our customers and partners have different preferred tools and to facilitate the communication with those parties, GitLab provides licenses for WebEx. This service is only provided to team members that have a business need to host meetings and where Zoom is not accepted.

- To request access to those tools, create an [access request](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=Individual_Bulk_Access_Request) and provide a justification for access.
- Consider installing their [native app](https://www.webex.com/downloads.html). Team members have reported issues when trying to use WebEx in Safari, so we recommend using other browsers such as Google Chrome when hosting or joining meetings.
- Before attending a Webex meeting you can test to ensure your Webex is setup correctly by joining a [test meeting](https://www.webex.com/test-meeting.html).
- The in-browser plugin the screen sharing sometimes doesn't work.

### Whereby

[Whereby](https://whereby.com/) allows you to instantly create a free video chat room for up to 4 participants with no login and no installation.
It also offers a free reliable mobile video conference app.

## Videos, GIFs, and screenshots

### Loom

[Loom (Free)](https://www.useloom.com/) is a handy Chrome plugin tool for video walkthroughs.
Nice tool for demo recordings and internal/external documentation. Note, Loom videos are public by default - ensure you are not exposing data that should remain private. GitLab does have a Loom workspace, for a license please follow the instructions on the [tech stack page](https://about.gitlab.com/handbook/business-technology/tech-stack/)

## Language and translation

### DeepL

The Gitlab handbook and most other content is written in English. Even if a non-native speaker's English is pretty good there might be times when the content is too sophisticated and a translation is welcome. Avoiding tedious copy and paste into another browser tab or app can easily be achieved by using the [DeepL translator](https://www.deepl.com/).
DeepL is available as a Web site but also as a Mac app for free. Using a shortcut on MacOS takes selected text from the handbook right into the app and starts translating. Linux users can only use a Chrome extension and right-click to open another tab for the Web version.
