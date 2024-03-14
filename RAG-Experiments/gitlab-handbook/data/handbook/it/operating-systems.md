---

title: Approved Team Member Endpoint Operating Systems
---

**The list below of operating systems page is for Team Member Endpoint Systems (Laptops)**.

Please see this [list](https://docs.gitlab.com/ee/administration/package_information/supported_os.html) for supported operating systems that can run the GitLab product.

## Approved Operating Systems for GitLab Team Member Endpoint Systems

*last updated 2023-01-12*

### macOS

macOS 13.4.0 or later

### Linux

If your work requires a Linux distro installed on your laptop (a team member endpoint system) by any means, including virtualization, that it must be on the below GitLab Approved List. It will be your responsibility to maintain your Linux environment with security patching and version upgrades to stay compliant with the list.

The list of Linux versions below is based on what our [EDR](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/endpoint-management/edr/) platform supports. Deployment of the EDR solution is required on team member endpoint systems and [virtual machines](https://about.gitlab.com/handbook/business-technology/team-member-enablement/onboarding-access-requests/endpoint-management/edr/#i-have-several-virtual-hosts-on-my-laptop-do-they-all-need-agent).

Linux versions are therefore limited to:

- Red Hat Enterprise Linux (RHEL) 8.0-8.6, 9.0, 9.1
- Ubuntu 20.04, 22.04
- Debian 11
- AlmaLinux 8.4, 8.5, 8.6, 9.0, 9.1
- RockyLinux 8.4, 8.5, 8.6, 9.0, 9.1
- Fedora 36, 37
- NixOS 23*
- Mint 21*
- Pop! OS 22.04*

**Note:** Mint, PopOS and NixOS are not officially supported by our EDR vendor, but team members have had success with getting the tools to run on those. As of 2023-02-15, new hires should not choose these distros and instead choose one of the officially supported Linux distros. We encourage all team members to migrate to an officially supported distro for long-term support.

Further details are available at the [Linux Tools & Tips](/handbook/tools-and-tips/linux/) page.

### Android

Android 12 or later

### iOS

iOS 16.5 or later

### Windows (For Customer Support and Product Development)

Windows for “Customer Support and Product Development” explicitly excludes other uses of Windows. For example, daily productivity such as email access, documentation writing or usage of Windows-only software titles for activities that are not directly related to supporting and developing GitLab for customers.

Windows Home edition is not allowed.

No matter how the Windows operating system is provisioned, it cannot be used to access GitLab Corporate services (e.g. Slack, G-Suite, GitLab.com); the Windows machine can only be used in addition to a GitLab-managed Mac machine.

##### Roles that qualify for Windows usage

- Engineers, Support Engineers, Technical Marketing Managers, Product Designers, UX Managers, Product Managers, Technical Writers and all Customer Success Technical roles are eligible to run virtualized Windows.
- The team member is responsible to ensure compliance with [all endpoint management policies](/handbook/it/operating-systems/) for virtualized Windows running on a GitLab Laptop. This includes installation and configruation of our [endpoint detection and response tool](https://about.gitlab.com/handbook/business-technology/end-user-services/onboarding-access-requests/endpoint-management/edr/).

##### Required manager approval and assurances

The team member’s manager is for:

- Responsible for approving the usage of each team member's use of Windows for support or development.
- Completely responsible to ensure Windows licensing compliance and license cost coverage.

##### Windows editions, licensing and environments

- The usage of virtualized Windows is highly preferred and should satisfy most every support and development need.
- The usage of cloud-based virtualized Windows instances is further strongly encouraged because:
  - all licensing is handled as a component of the Cloud’s time based charging, which dramatically simplifies licensing compliance. Clouds generally have Desktop versions through Desktop as a Service offerings. These are generally a substantially higher cost - so should only be used when a Desktop experience is truly required.
  - These environments are generally more isolated from inbound internet traffic by default than laptop virtualization environments.
- Microsoft developer oriented licensing for Windows can be leveraged - frequently development licensing is already bundled in certain Microsoft program, product and partnership licenses. In some cases, the development licensing allows usage of unactivated Windows for development (but the license must still be owned).
- Usage of personal licensing or other non-corporate licensing is not allowed (e.g. Visual Studio Dev Essentials).
- Instead of Windows desktop editions, the usage of Windows Server editions without Desktop Experience installed, is encouraged due to the lower level of default preinstalled APIs.
- Due to the substantial secure-by-default nature of newer Windows versions, using versions early than Windows Server 2019 or Windows 10 is discouraged unless there is a very specific customer requirement to support earlier versions in the specific support or development activity.

#### Windows on Laptop Hardware

Windows usage on laptop hardware is the least preferred option. If you have a legitimate business need to use a Windows operating system on laptop hardware, please see the [Exception Process](#exception-process) (which requires articulation of why virtualized Windows is not sufficient).

## Exception Process

Exceptions must follow the Exception Management process as outlined in the [GitLab Security Handbook page](https://about.gitlab.com/handbook/security/#information-security-policy-exception-management-process)
