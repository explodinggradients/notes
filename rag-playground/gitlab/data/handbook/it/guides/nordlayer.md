---
title: "NordLayer User Guide"
description: "IT Self Service Guides provide team members with instructions for frequently asked questions for installing, configuration, and troubleshooting your laptop or our tech stack applications."
---

## Overview

NordLayer is our supported VPN (Virtual Private Network) platform for GitLab Team Members.

The use of Nordlayer is optional, however it is recommended when working on guest networks or public Wi-Fi. In other words, you should connect to the VPN to secure your laptop's traffic anytime that you're not at home. That could be at a coworking location, an airport, a coffee shop or on a guest network at a customers office.

Some members may use a different VPN solution for these scenarios and we would recommend that they migrate to Nordlayer when it's convenient.

When we first approached the idea of a simple VPN for those times that our employees work away from home (coffee shops, trains, planes, etc.), we found a lot of options out there. While many VPN options exist, some are much more than we need, and some far less. When it comes to our decision on NordLayer, we had a number of things to look at: Is it secure? Is it easy to administer? Does it cover multiple Operating Systems? Are admin actions logged? We tested many options and while a number fit a few of these, NordLayer fit the most with security being our most important criteria.

#### System Owner and Support

- DRI: `@adamhuss`
- `#it_security_help` Slack channel
- [NordLayer Help Center Chat](https://help.nordlayer.com/)

#### Access Request

Please open an [Access Request](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/access-requests/) and add `/label ~"it-security-status::needs-review"`.

## NordLayer Installation

See the [IT Self Service](/handbook/it) page for more information about creating an access request for NordLayer.

### Activate your account

After your access request is provisioned, you will receive a signup email with a link to activate your account. Once activated, you will be redirected to a NordLayer landing page with a link to download the application.

### Initial Configuration

1. Enter `GitLab` as the Organization.
1. Sign in using your GitLab email and the password you just created with the sign up link.
1. Authenticate via Okta.
1. Mac users will be prompted to Allow an upcoming prompt, please do this.

### Adding Your Home Network to the Trusted List

> When you add a trusted network to the list, your laptop will keep NordLayer disconnected while at home. This allows you to use the internet at full speeds, and will automatically connect while you're on any untrusted network away from home.
>
> Please keep in mind that any trusted networks you add means that you are no longer protected through a VPN. Do not do this if you're at a hotel, on a guest newtork, or anywhere outside of your home network (unless needed to get through initial Wi-Fi portal terms and conditions captive portal screen).

1. Go to NordLayer Preferences and select the `Auto-Connect` tab.
1. Verify the Network listed under `Current Network` is your home network and click the `Trust` button.

## NordLayer Troubleshooting

### How to change the protocol on NordLayer application for Linux?

In case you are experiencing any issues with your NordLayer connection, the first course of action would be to change the VPN protocol. You can do so by entering the following command 'sudo nordlayer settings set' - you should see that the first option is to choose the VPN protocol.

### `Verify that you have sufficient privileges to start system services’ error on Windows 10

If you are getting an error 'Verify that you have sufficient privileges to start system services' on Windows 10 while installing the NordLayer application - please make sure that you are using an up-to date Windows 10 version.

### NordLayer application for Linux has hung and is not responsive

If you encounter this situation, you will need to force-close the application by entering the following command:
sudo systemctl kill -s SIGKILL nordlayer.service

### VPN Authentication errors on Mac using NordLayer

If the VPN authentication window is constantly popping up on your screen, go to System Preferences -> Network and select the NordLayer connection. Make sure that Connect on Demand is disabled, then click Cancel and it should not re-appear.

If you are still seeing the popup, restart your Mac and drag the NordLayer app to the trash. Once that is done, re-install NordLayer application directly from the AppStore.
