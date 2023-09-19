---
title: GitLab Password Guidelines
---
<!-- markdownlint-disable MD051 -->
## Passwords at GitLab

Passwords are one of the primary mechanisms that protect GitLab information systems and other resources from unauthorized use. GitLab's [password standard]({{< ref "password-standard" >}}) is based, in part, on the recommendations by [NIST 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html). The password standard sets the requirements for constructing secure passwords and ensuring proper password management. GitLab utlizes 1Password for password management.


## 1Password

1Password is a password manager that can be used in two different ways - as a standalone application
(by purchasing a standalone license) or as a hosted service (by subscribing). GitLab uses 1Password for Teams which is a hosted service.

Ideally you memorize one strong password - hence the name - and let 1Password generate and manage strong, unique passwords
for every site for which you have a login.

GitLab requires all team members to use [Okta](https://about.gitlab.com/handbook/business-technology/okta/) as a primary entry and access point for SaaS and other company applications while utilizing 1Password for password management. GitLab utilizes Okta for SAML/SSO and passwordless authentication for many applications, so the need to store passwords in a password manager will diminish over time.

If you want to use 1Password for your private passwords not related to your work
at GitLab, [there are a few options](#1password-for-your-private-passwords).

Please note our 1Password for Business license agreement [includes the 1Password for Families feature](https://support.1password.com/link-family/), which you can share with up to 5 family members.

### Terminology

Following this guide, it will be helpful to understand a few terms we'll be
using throughout.

- **App:** A native 1Password application (macOS, iOS, Windows, Android).
- **Extension:** A web browser extension/plugin that communicates with the
  **App** to provide access to your passwords securely without leaving the
  browser.
- **Vault:** What 1Password calls any grouping of secure data, such as logins or
  secure notes. Sometimes called a "keychain".

### 1Password guidelines

1. If you install the macOS application, install 1Password via this link
[1Password](https://1password.com/downloads/mac/)
1. If you have a YubiKey, it can be added as a 2-factor
method to your 1Password account for convenience.
1. When traveling, consider using 1Password in "Travel Mode", see more on that [below](#travel-mode).
1. Do not share credentials via email, issue comments, chat etc. This includes
   email addresses to login and API keys. Use 1Password vaults for this.
1. If you do not have access to a vault that is part of the baseline entitlements
  for your role and team, mention `gitlab-com/business-ops/itops` in your onboarding
  issue or in #it-ops on slack. For all other access, create an
  [access request issue](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new).
1. Use Watchtower to find passwords that need to be changed. Watchtower tells
users about password breaches and other security problems on the websites they
have saved in 1Password Teams, so users can take action. This is not something
account administrators can review for team members, so it is up to you to enable!
Enable Watchtower by going to your 1Password app and then to **Preferences > Watchtower**.
1. Use the ["Security Audit"](https://i.agilebits.com/dt/Blank_Skitch_Document_18FB0234.png)
functionality of 1Password to meet the [password standard]({{< ref "password-standard" >}}).
It will report reused passwords, weak passwords, accounts that
are missing 2-factor authorization, and so forth that can then be fixed.
1. Do not copy passwords from inside a 1Password vault to a personal password
vault or other password store. 1Password should be the only password
vault used for teams. Team passwords should not be duplicated or placed in
personal password vaults where they can potentially be exposed to compromise.
1. When asked security questions (what is your favorite pet, etc.) do not answer
truthfully since that is easy to research. Make up an answer and write both the
question and answer in 1Password. Consider using the Password Generator function
in 1Password for this.
1. During offboarding, your 1Password account is deleted, which includes the
**Private** vault in the GitLab team account. If you want to keep your personal
passwords, please copy/move them to your **Primary** vault which you will have
if you signed up for an [individual account](#1password-for-your-private-passwords) before
joining the GitLab Team account.
1. **Deprecated** When documenting the location of shared credentials in the handbook refer to the items with NAME_OF_SITE credentials in VAULT_NAME. For example:
   "for access please see the AOL credentials in the Luddite vault".
   - Deprecation note: This is for existing accounts only. New accounts should
     be created by [creating an issue](https://gitlab.com/gitlab-com/business-ops/change-management/issues/new?issuable_template=change_management_okta)
     to add it to Okta.


### 1Password for teams

1Password for Teams stores all **Vaults** on the 1Password servers and allows
for sharing between multiple people on the same team. Every GitLab team member who needs access to a shared vault should consult their departments for any shared vault information.

Each member of the team has a vault called **Private** which *only you can see*, and allows you to store personal credentials *within the GitLab team's account*.

To really get the full benefit of 1Password, you'll need to hook our Teams
account up to one of the native apps.

#### Adding the GitLab team to a 1Password app

This guide will cover setting up the [macOS app]. It's their lead platform and is
the most up-to-date. These instructions may or may not work for the Windows
version. If you use 1Password 6 without a 1Password.com account, make note of
[this](#updating-1password-to-support-the-teams-feature).

1. Download and install the 1Password [macOS app].
1. Launch the app.
1. Click "Sign in to your 1Password account" button. If there is no such button
please follow the instructions for [updating 1Password](#updating-1password-to-support-the-teams-feature).

Now you'll need the **Emergency Kit** PDF that 1Password told you to save when
you registered your **Teams** account. Note: Store the Emergency Kit safely.
Store a copy of the Emergency Kit on a USB flash drive or print a copy and store
it in a vault at home or safe deposit box — somewhere not online or accessible
by anyone other than yourself.

If you saved it as a digital PDF file:

1. Open the PDF file
1. Click **Scan QR Code**
1. Open the PDF file with the scanner by clicking on the camera icon

<div style="text-align:center;">
  <img src="../1password-setup-open-file-dialog.png" alt="Open PDF file with scanner by clicking on camera icon" width="700"/>
</div>
<br>

If you printed the PDF:

1. Click **Sign In Manually**
1. For **Team URL** enter **gitlab.1password.com**
1. For **Account Key** enter the Account Key from your Emergency Kit
1. For **Email Address** enter your `@gitlab.com` email
1. For **Master Password** enter the password to your **Teams** account (*not*
   the password you created above when you chose "I'm a new user")

After the Team is added, you should see some notifications about vaults being
added to 1Password. By default you'll have the **Private** vault, but
may have access to others.

#### Updating 1Password to support the Teams feature {#1password-update}

*Read this section only if you could not follow the instructions in "Adding
the GitLab Team to a 1Password app" section.*

1. At the prompt, choose "I'm a new user". *Note:* This is one source of
   confusion. "I created my Teams account, I'm not new!" Just go with it.
1. Enter a master password, confirmation, and hint. This can (and should) be
   different from the password you used for our **Teams** account. This password
   gates access to your **local, private** Vault on your computer and/or phone.
1. Skip over the remaining dialogs (syncing, newsletter, etc.)
1. You should now have an empty vault called **Primary**.

Because the Teams feature is not available in your current version of 1Password,
we need to update the app to the latest version:

1. Go to **Preferences**
1. Go to **Updates**
1. Click **Check Now**
1. Install the update and relaunch
1. After relaunch, go to **Preferences** again
1. Go to **Accounts**
1. Click the **+** icon

#### Vaults

Click the **Vault Selector** in the upper-left corner of the window:

<div style="text-align:center;">
  <img src="../1password-vault-selector.png" alt="Vault Selector" width="700"/>
</div>
<br>

GitLab team members have access to a **Private** vault by default, which is your *hosted, private* vault that is part of the GitLab 1Password for Teams account. Since the Private vault is part of the
GitLab Teams account, it should be thought of as company property (like the
@gitlab.com email account), however the vault *can not* be viewed by anyone
else on the team, including admins. If you choose to store truly personal
information in the Private vault, it opens up the possibility that you would
be separated from this information if you offboard. Such truly personal
information is therefore better to store in your **Primary** vault, which is
associated with you instead of with the GitLab Teams account, assuming that you
added an [individual account](#1password-for-your-private-passwords).

People may request access to other vaults such as shared vaults that their teams/departments have created.

#### Browser extension

Go to [Browser extensions](https://agilebits.com/onepassword/extensions) and
install the extension for whatever browser you're using. You *should not* need a
beta version here.

With the extension installed, you should be able to go to a site that you have
credentials stored for in 1Password and log in:

<div style="text-align:center;">
  <img src="../1password-login.gif" alt="Mailchimp Login" width="450"/>
</div>

If you don't see the site listed in the results window, make sure you're using
the correct vault:

<div style="text-align:center;">
  <img src="../1password-vault-change.gif" alt="Vault switching" width="450"/>
</div>


#### Saving logins

When 1Password detects a login form submission, it may ask if you want to save
the login with a dialog like this:

<div style="text-align:center;">
  <img src="../1password-save-login.png" alt="Save login" width="600"/>
</div>

If you do want to save it, make sure the appropriate **Vault** is selected
first.

#### Managing SSH keys

Starting with version 8, 1Password can operate as the single source of truth for your SSH keys. This includes generating private keys, storing them securely, filling your public keys in to sites like GitLab.com, and unlocking the keys automatically when performing git operations.

More information is available [in the official documentation](https://developer.1password.com/docs/ssh/).

#### CLI integration

[1Password CLI integration](https://developer.1password.com/docs/cli) supports secure
handling of secrets used in command line tools, config files, and scripts executed on your laptop.
To setup the CLI integration, follow the [getting started guide](https://developer.1password.com/docs/cli/get-started/).

It is recommended to store secrets such as [personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
in 1Password. Avoid storing secrets in unencrypted files.

Example for configuring [glab](https://gitlab.com/gitlab-org/cli) with 1Password CLI (requires 1password version 8 or higher):

- Store your access token in 1Password. In the entry for your GitLab account, create a new section `pat`
 and add a field `api`. Insert the value of your PAT into the newly created field `api`.
<div style="text-align:center;">
  <img src="../1pass-pat-setup.png" alt="Save login" width="600"/>
</div>

- Store a secret reference to the access token in an `.env` file:

```sh
## format is op://vault-name/item-name/[section-name/]field-name
echo "GITLAB_TOKEN=op://Private/GitLab/pat/api" > $HOME/.gitlab-pat.env
```

- Define an alias in your shell profile to invoke `glab` with the PAT

```sh
alias glab="op run --env-file=$HOME/.gitlab-pat.env -- glab"
```

- To verify the configuration, run `glab api version`. This should print
the version of gitlab.com if the configuration succeeded.

```sh
glab api version
{"version":"15.4.0-pre","revision":"3e84f577d51"}
```

#### Several accounts and unlocking the app

Please refer to [1Password FAQ](https://support.1password.com/faq/#i-have-several-accounts-and-vaults-which-password-do-i-use-to-unlock-1password).

If you are planning to use both the GitLab team account and a separate
individual account you should first add your separate individual account to the
app first (Preferences > Accounts). By doing this you will be able to unlock
the 1Password app using the Master Password of the individual account.

If you were using 1Password before joining GitLab, and you receive a prompt
titled **Migrate To Account**, choose **I'll move later**. There is no harm in
doing this, and it is easy to move items between vaults.

#### 1Password for your private passwords{#1password-private-use}

You are encouraged to use 1Password for your private passwords, not related to
your work at GitLab.
This makes it less likely for a security breach to occur. You can purchase a
standalone license or start an individual subscription, or take advantage of the
[complimentary 1Password for Families feature](https://support.1password.com/link-family/),
which you can share with up to 5 family members.

#### Two factor authentication and time-based one time passwords

As stated in the [GitLab Password Standards]({{< ref "password-standard" >}}), the usage of 2FA is mandatory for all GitLab team members.

Okta is configured such that it only supports the use of WebAuthn. 1Password TOTP should only be used when WebAuthn is unavailable.

1Password provides an alternative solution that does not
require using your smartphone: 1Password Time-based One Time Passwords
(TOTP). 2FA codes are displayed directly in the 1Password app running on your
laptop (Note: this can not be set up via 1Password browser extension or 1Password web app).

To enable TOTP for a saved account:

1. Open 1Password app
1. Go to the item for which you want to set up TOTP
1. Click **Edit** in the bottom right corner
1. Add a new field by clicking on the field type dropdown (it offers a "Text field" by default)
1. Select **One-Time Password**

<div style="text-align:center;">
  <img src="../1password-otp.png" alt="One-time password field type" width="600"/>
</div>

1. Click QR code icon that appeared

<div style="text-align:center;">
  <img src="../1password-qrcode.png" alt="1password QR Code" width="600"/>
</div>

1. Scan QR code using the transparent window
1. Click **Save**
1. 2FA code should be displayed now

Please refer to demo video [1password TOTP setup](https://support.1password.com/one-time-passwords/)

Please refer to the [1Password blog] for more information on how TOTP works.

[1Password blog]: https://blog.agilebits.com/2015/01/26/totp-for-1password-users/

If scanning the QR code using the "transparent window" with the 1Password Mac
app fails on a recent macOS, please consider using the 1Password iOS app instead.
This mechanism works the same way, and supports Touch ID to login.

If unsure which mechanism to use, we require using WebAuthn (when possible) as a TOTP for 2FA.

Follow this [guideline](https://gizmodo.com/how-to-easily-switch-your-two-factor-security-to-a-new-1821808681) when getting a new mobile device, if you are using Google Authenticator as a TOTP mechanism.

There may be cases where TOTP might be used with a non-GitLab account. If you have any questions and need to speak with the Security Team, you can contact [Security]({{< ref "_index.md#-contacting-the-team" >}})


#### Example usage {#1password-example-usage}

This is an example of how <a href="https://gitlab.com/rspeicher">Robert</a>,
one of our developers, uses 1Password:

> Once you fully commit to using 1Password to manage all of your security
> information, it really does make life easier.
>
> I memorize one strong password and let the app generate
> everything else. Every site I use has a unique password that I can't
> compromise because I don't even know it, and a hacked site can't compromise
> it because the password is never re-used on another site.
>
> I store my shipping and credit card info in 1Password and use the browser
> extension to quickly fill out shipping and billing information on shopping
> sites.
>
> I store my passport data, along with a digital scan, in 1Password; driver's
> license info and scan; insurance info; software license keys; any important
> information that needs to be secure but still easily accessible when I need it,
> from anywhere. I sync my personal vault to my personal iCloud so it's
> available on my phone, tablet, laptop, and desktop.
>
> Even my 1Password for Teams account information is stored in my personal
> **Primary** vault, with the Emergency Kit PDF as a secure attachment.
> I have no idea what the password is. I've never actually typed it. And that's
> the idea:

  <div style="text-align:center;">
    <img src="../1password-teams-login.png" alt="Teams Login" width="560px"/>
  </div>

#### Traveling with 1Password{#travel-mode}

When traveling with a device that has access to the GitLab 1Password vaults, be
sure to [enable Travel Mode](https://support.1password.com/travel-mode/) in 1Password. Travel Mode removes copies of any
1Password vaults that are not tagged as "safe for travel" from your mobile devices.
None of the GitLab shared vaults are marked as safe for travel so you will need
to either create a dedicated travel vault or mark your Private vault as safe for
travel.

Once you have enabled Travel Mode open 1Password on each device you will be taking
with you so that it can sync with 1Password.com and remove any vaults that cannot
be used while traveling.

For more information on Travel Mode and how it works, see the [AgileBits blog].

[agilebits blog]: https://blog.agilebits.com/2017/05/18/introducing-travel-mode-protect-your-data-when-crossing-borders/
[macOS app]: https://agilebits.com/downloads

#### Securing Docker Registry User Credentials

Docker can store user credentials in an [external credential store](https://docs.docker.com/engine/reference/commandline/login/#credential-stores) as a more secure alternative to storing credentials in the Docker configuration file.

##### Using `osxkeychain` (macOS)

To configure Docker to use `osxkeychain` for secure credential storage, follow these steps:

1. Install the `docker-credential-osxkeychain` helper via Homebrew:

    ```sh
    brew install docker-credential-helper
    ```

1. Configure `~/.docker/config.json` to [use `osxkeychain` as your Docker credstore](https://docs.docker.com/engine/reference/commandline/login/#credential-stores):

    ```json
    {
        "credsStore": "osxkeychain"
    }
    ```

1. Log in using `docker login registry.gitlab.com`, and enter your email and password (PAT) when prompted.
1. Validate that the credentials were not saved as base64-encoded text in `~/.docker/config.json`.

##### Using `pass` (Linux)

**Prerequisites**

1. [Create a GPG key](https://docs.gitlab.com/ee/user/project/repository/signed_commits/gpg.html#create-a-gpg-key)
1. [Install `pass`](https://www.passwordstore.org/#download)

To configure Docker to use `pass` for secure credential storage, follow these steps:

1. Download the latest `docker-credential-pass` binary from [the releases page](https://github.com/docker/docker-credential-helpers/releases).
1. Make the `docker-credential-pass` binary executable with `chmod +x docker-credential-pass`.
1. Move the `docker-credential-pass` binary to your `$PATH` (e.g., `sudo mv docker-credential-pass-v0.8.0.linux-amd64 /usr/local/bin/docker-credential-pass`).
1. Obtain and copy the GPG key ID that `pass` will use for encryption via `gpg --list-secret-keys --keyid-format LONG`.
1. Initialize `pass` with `pass init <gpg-key-id>`.
1. Configure `~/.docker/config.json` to [use `pass` as a credstore](https://docs.docker.com/engine/reference/commandline/login/#credential-stores):

    ```json
    {
        "credsStore": "pass"
    }
    ```

1. Log in using `docker login registry.gitlab.com`, and enter your email and password (a valid [token](https://docs.gitlab.com/ee/user/packages/container_registry/authenticate_with_container_registry.html)) when prompted.
1. Validate that the credentials were not saved as base64-encoded text in `~/.docker/config.json`.
