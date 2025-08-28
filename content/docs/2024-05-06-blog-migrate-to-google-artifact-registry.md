---
title: 'Blog: Migrate to Google Artifact Registry'
date: '2024-05-06T00:00:00+00:00'
tags:
- jenkins-x
source: Jenkins X
external_url: https://jenkins-x.io/blog/2024/05/06/migrating-artifact-registry/
post_kind: link
draft: false
tldr: Migrate to Google Artifact Registry Google has announced that container registry
  will be shut down some time after March 18, 2025. For GKE clusters created with
  version 1.
summary: Migrate to Google Artifact Registry Google has announced that container registry
  will be shut down some time after March 18, 2025. For GKE clusters created with
  version 1. 12. 0 or later of terraform-google-jx it’s unlikely that anything needs
  to be done, but for older clusters you should upgrade your cluster while considering
  our advice regarding migration from container registry to artifact registry. If
  you are using a Google Service Account to run terraform you need to add the role
  requirement roles/artifactregistry. admin. See our guide regarding Google Service
  Account for details. ← Previous.
---
Open the original post ↗ https://jenkins-x.io/blog/2024/05/06/migrating-artifact-registry/
