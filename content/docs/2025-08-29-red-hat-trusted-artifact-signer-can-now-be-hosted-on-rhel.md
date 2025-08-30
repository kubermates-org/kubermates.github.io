---
title: Red Hat Trusted Artifact Signer can now be hosted on RHEL
date: '2025-08-29T00:00:00+00:00'
tags:
- kubernetes
source: Redhat Blog
external_url: https://www.redhat.com/en/blog/red-hat-trusted-artifact-signer-can-now-be-hosted-rhel
post_kind: link
draft: false
tldr: Red Hat Trusted Artifact Signer can now be hosted on RHEL Additional options
  without sacrificing functionality Simplified installation and configuration using
  Red Hat Ansible Automation Platform Red Hat Product Security About the author Andrew
  Block More like this Blog post Blog post Blog post Keep exploring Browse by channel
  Automation Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share Organizations looking to better understand the
  lineage of their software artifacts have begun to adopt signing as a way to improve
  their security posture. By applying digital signatures to software artifacts, trust
  can be established to verify that assets have not been substituted or tampered with
  through the software development and delivery process.
summary: 'Red Hat Trusted Artifact Signer can now be hosted on RHEL Additional options
  without sacrificing functionality Simplified installation and configuration using
  Red Hat Ansible Automation Platform Red Hat Product Security About the author Andrew
  Block More like this Blog post Blog post Blog post Keep exploring Browse by channel
  Automation Artificial intelligence Open hybrid cloud Security Edge computing Infrastructure
  Applications Virtualization Share Organizations looking to better understand the
  lineage of their software artifacts have begun to adopt signing as a way to improve
  their security posture. By applying digital signatures to software artifacts, trust
  can be established to verify that assets have not been substituted or tampered with
  through the software development and delivery process. Red Hat Trusted Artifact
  Signer , a key component of Red Hat’s Trusted Software Supply Chain portfolio ,
  provides a suite of tools that supports signing and verifying assets from first
  commit to deployment. Since Trusted Artifact Signer was first released, it has been
  available as a Day-2 operator on Red Hat OpenShift. With the release of version
  1.2, you can now also deploy the entire Trusted Artifact Signer suite onto a Red
  Hat Enterprise Linux (RHEL) machine, providing another option for where to run the
  service. An installation of Trusted Artifact Signer within an RHEL environment will
  feel familiar to those who have previously deployed the service on OpenShift. Linux
  containers continue to be the primary delivery vehicle and it relies on the same
  content source, enabling a consistent experience wherever the service is deployed.
  One of the goals associated with the design and implementation of Trusted Artifact
  Signer on RHEL was to include the same core components and to remain as feature-compatible
  as possible with the existing OpenShift-based deployment. This includes: The entire
  suite of Trusted Artifact Signer based services, including Fulcio, Rekor, TUF, and
  a Timestamp Authority The ability to expose each of the services using a set of
  provided TLS certificates The ability to utilize external instances of MySQL and/or
  Redis You can also now use Cockpit to monitor the deployment of Trusted Artifact
  Signer on RHEL. Once enabled, the management of container instances can all be governed
  within a single console using tooling that is familiar with most RHEL administrators.
  Ansible Automation Platform is the underlying engine behind the installation and
  configuration of Trusted Artifact Signer on RHEL. The new redhat.'
---
Open the original post ↗ https://www.redhat.com/en/blog/red-hat-trusted-artifact-signer-can-now-be-hosted-rhel
