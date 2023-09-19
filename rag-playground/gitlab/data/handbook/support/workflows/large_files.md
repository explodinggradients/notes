---
title: Support Uploader - Handling large files from Customers
description: "Support team workflow for using the Support Uploader to receive large files from customers"
category: Handling tickets
---

In the event that a customer wishes to share a large volume of data with us, we require a way to receive the information.
Please follow the steps below in order to create a unique user, and upload relevant information for review by the GitLab Support Team.

## Generating a FTP user for the customer

To generate the FTP credentials for a customer, navigate to the Zendesk Super
App:

1. Click the `Support Uploader` option.
1. Click on `Generate FTP user`.

This will trigger a pipeline to generate the user. Wait up
to 5 minutes for an internal comment to be posted containing the FTP
credentials.

If you do not see an update, please reach out to Support Operations via Slack
for assistance.

## Providing credentials to the customer

To provide the credentials to the customer, please use the
`General::Support Uploader` macro, as it contains both the formatting to use and
links to explain how to utilize it.

In the macro's output, ensure you replace `HOST`, `USERNAME` and `PASSWORD` with
the values from the internal comment (made via the Zendesk Super App).

## Accessing uploaded files

When the customer uploads files, an internal comment will be made on the ticket
the FTP user was generated for. To access the file, use the same credentials
generated previously.

### Windows users and archive files

If a customer using a Windows machine uploads any files, it's possible their FTP
client may change the file slightly. See
[here](https://unix.stackexchange.com/questions/203151/remove-special-pattern-m-from-script-which-got-appended-after-ftp-from-windows)

If the customer uploaded any archives, and you attempt to extract the archive,
it may come up with an invalid format error:

```text
$ tar --list -f gitlabsos.main-a_20230215115744.tar.gz

gzip: stdin: invalid compressed data--format violated
tar: Child returned status 1
tar: Error is not recoverable: exiting now
```

To resolve this, force `dos2unix` to run on the archive first:

```text
dos2unix -f gitlabsos.main-a_20230215115744.tar.gz
```

## File deletion

When the ticket the FTP user was generated for is closed, the FTP user (and
associated files) will automatically be removed completely.

## US Federal Support Uploader

There is not currently a US Federal Support Uploader. Please check back in the
future for more information on it when it becomes available.

## Usage

For details on using FTP to upload/download files, please see
[Support Uploader usage](https://about.gitlab.com/support/providing-large-files/#support-uploader-usage).
