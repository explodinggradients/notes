---

title: Sentry
category: Infrastructure for troubleshooting
description: How to use Sentry to investigate GitLab.com errors
---



## Sentry

*Note*: Sentry organizes applications into "Sentry Teams". To investigate errors across different applications or environments, our primary teams used are `#gitlab` (for the production rails application) and `#gitlab-internal` (for non-production environments). By joining said Sentry Team, the application errors should be viewable.

1. Obtain the full URL the user was visiting when the error occurred along with their user ID, if needed for searching.
1. [Log in to Sentry](https://sentry.gitlab.net/gitlab/gitlabcom/).
1. Enter a query into the search field. For example, the following query would display any errors events encountered by the user with the ID `123456`:

```plaintext
is:unresolved user.id:123456
```

In addition to searching by user ID, you can also use `user.username:` and `url:` to search by GitLab.com username (case-sensitive) and specific page on GitLab.com, respectively. You can also select filtering values by clicking the "filter" button located directly to the right of the search bar.

At times a search will turn up a Sentry issue that appears to reference the information (user ID, URL, etc...) of another user and not the one that reported the issue. If this happens and you need to create an issue for that specific reporter, simply click the `Events` tab as seen below to view a list of all users affected by that issue.

![Sentry events tab](/images/support/sentry-events-tab.png)

You can then click a specific event to view the Sentry issue for that user.

See the [Sentry guide](https://docs.getsentry.com/hosted/learn/search/) and [this presentation](https://drive.google.com/drive/u/0/search?q=Sentry%20parent:1UT1VKASEzvCzWVX9fDLkYhDju35NxiLT) (GitLab internal only) for more information.

### Searching by Correlation ID

In most cases errors in Sentry can be found by searching using `user.id:`, but this won't always be the case. Sometimes, you may need to search Kibana first to locate the correlation ID that can then be searched for in Sentry.

In the following example, the customer is attempting to [change the notification email for one of their groups](https://docs.gitlab.com/ee/user/profile/notifications.html#group-notification-email-address) but receieves a `500` error when selecting the desired address from the dropdown list. Searching Sentry for their `user.id:` turns up nothing, so we need to do the following to find the `500` in Kibana to get the correlation ID that we'll then provide to Sentry.

1. Add positive filters in Kibana for `json.username` with their GitLab.com username, `json.controller` for `Profiles::NotificationsController`, and `json.status` with `500`.
1. Using the left-hand side menu add the `json.path`, `json.controller`, `json.status`, and `json.correlation_id` fields to your search results, which should give you results similar to the following if any errors ocurred within your set time range.

   ![Kibana search results](/images/support/correlationid_kibana_results.jpg)

1. Pick a correlation ID value and move over to Sentry to search for it using `correlation_id:`, which should give you a result.

   ![Sentry search results](/images/support/correlationid_sentry_results.jpg)
