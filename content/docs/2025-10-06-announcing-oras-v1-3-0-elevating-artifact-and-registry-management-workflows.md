---
title: 'Announcing ORAS v1.3.0: Elevating artifact and registry management workflows'
date: '2025-10-06T17:07:15+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/10/06/announcing-oras-v1-3-0-elevating-artifact-and-registry-management-workflows/
post_kind: link
draft: false
tldr: 'Your registry’s safety net: Portable backup & restore Multi-platform image
  and artifact management Enable scripting and automation: Formatted output Stability
  & user experience polish Why this release matters Thanks to all contributors Posted
  on October 6, 2025 by Feynman Zhou CNCF projects highlighted in this post The ORAS
  community is thrilled to announce the release of ORAS CLI v1.3.0, a version packed
  with stability improvements and pioneering capabilities. In addition to strengthening
  existing functionality, this release introduces three major new features designed
  to enhance artifact and registry management workflows: Portable backup and restore
  of repositories and artifacts Multi-platform image and artifact management Rich
  formatted output for scripting and pipelines Moreover, ORAS is now fully compliant
  with OCI distribution-spec v1.1.1.'
summary: 'Your registry’s safety net: Portable backup & restore Multi-platform image
  and artifact management Enable scripting and automation: Formatted output Stability
  & user experience polish Why this release matters Thanks to all contributors Posted
  on October 6, 2025 by Feynman Zhou CNCF projects highlighted in this post The ORAS
  community is thrilled to announce the release of ORAS CLI v1.3.0, a version packed
  with stability improvements and pioneering capabilities. In addition to strengthening
  existing functionality, this release introduces three major new features designed
  to enhance artifact and registry management workflows: Portable backup and restore
  of repositories and artifacts Multi-platform image and artifact management Rich
  formatted output for scripting and pipelines Moreover, ORAS is now fully compliant
  with OCI distribution-spec v1.1.1. With oras backup and oras restore, ORAS now lets
  you save your registry content into local directories or tarballs (OCI image layout
  format) as a snapshot and restore to any registry. All manifests, along with any
  optional tags and referrers, will be included in the backup. Use cases include:
  Air-gapped environments: Organizations operating in isolated or high-security environments
  can use oras backup to export artifacts from a registry to the local filesystem,
  and oras restore to import them into an internal registry with restricted access.
  Disaster recovery and audit archival: Take periodic snapshots of repositories and
  store them off-site. In case of accidental deletions, outages, or long-term storage
  for regulatory audits, oras restore can quickly recover full registry content. Registry
  migration: When moving from one container registry provider to another, these commands
  enable a full repository export, preserving tags, manifests, layers, and referrers.
  Compliance and supply chain security: Back up and restore images along with their
  supply chain artifacts, such as SBOMs, signatures, and vulnerability scanning reports.
  Repository duplication or promotion: Move artifacts from dev to staging to production
  registries reliably using an intermediate backup file. Check out the user guide
  Backup and Restore of OCI Artifacts, Images, and Repositories for details. Multi-platform
  images are commonly used in IoT and Edge computing, particularly in heterogeneous
  deployments.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/10/06/announcing-oras-v1-3-0-elevating-artifact-and-registry-management-workflows/
