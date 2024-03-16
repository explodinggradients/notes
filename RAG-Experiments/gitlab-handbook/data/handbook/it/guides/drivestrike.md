---
title: "DriveStrike Guide"
description: "IT Self Service Guides provide team members with instructions for frequently asked questions for installing, configuration, and troubleshooting your laptop or our tech stack applications."
---

## Overview

DriveStrike is available for Linux operating systems, and also meets security needs for remote lock or wipe in emergencies. DriveStrike is a required security tool for all Linux devices, and is also used to wipe MacOS systems in the event Jamf is unable to do so.

DriveStrike installs for GitLab will have the ability to remotely lock or wipe hardware, for use in emergency or offboarding situations.
DriveStrike collects the following information:

- Usernames & Accounts present on the machine
- Machine Name, Make, Model, MAC, Serial #
- Hardware Specifications (CPU, RAM, HDD + % Used)
- Firewall status
- OS Version & Patch/Update status
- Disk encryption status
- Battery Health
- GPS location on devices the support GPS
- All nearby WiFi networks, including SSID, signal strength, channel, and MAC address. This is used for WiFi Triangulation and is not directly visibile within the console.
- IP Address

## Installation Process

If you are using a Linux device for work, the IT team may email you a link with Drivestrike to install. If you need a link to the installer, please request one in #it_help channel.

The subject line of the email is `Invitation to DriveStrike` and it comes from `support@drivestrike.com`.

1. Open the email on the device you want protected.
1. Click the [link provided in the email](https://app.drivestrike.com/instructions/linux/) to install
1. Use your `@gitlab.com` when installing if DriveStrike prompts you for a `registration code (email)`.

If you run into any errors or the email address is not found, please reach out in #it_help for assistance.
