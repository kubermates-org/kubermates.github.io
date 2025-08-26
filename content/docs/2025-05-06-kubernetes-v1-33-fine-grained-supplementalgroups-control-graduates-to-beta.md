---
title: 'Kubernetes v1.33: Fine-grained SupplementalGroups Control Graduates to Beta'
date: '2025-05-06T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/06/kubernetes-v1-33-fine-grained-supplementalgroups-control-beta/
post_kind: link
draft: false
tldr: The new field, supplementalGroupsPolicy , was introduced as an opt-in alpha
  feature for Kubernetes v1. 31 and has graduated to beta in v1.
summary: 'The new field, supplementalGroupsPolicy , was introduced as an opt-in alpha
  feature for Kubernetes v1. 31 and has graduated to beta in v1. 33; the corresponding
  feature gate ( SupplementalGroupsPolicy ) is now enabled by default. This feature
  enables to implement more precise control over supplemental groups in containers
  that can strengthen the security posture, particularly in accessing volumes. Moreover,
  it also enhances the transparency of UID/GID details in containers, offering improved
  security oversight. Please be aware that this beta release contains some behavioral
  breaking change. See The Behavioral Changes Introduced In Beta and Upgrade Considerations
  sections for details. Although the majority of Kubernetes cluster admins/users may
  not be aware, kubernetes, by default, merges group information from the Pod with
  information defined in /etc/group in the container image. Let''s see an example,
  below Pod manifest specifies runAsUser=1000 , runAsGroup=3000 and supplementalGroups=4000
  in the Pod''s security context. What is the result of id command in the ctr container?
  The output should be similar to this: Where does group ID 50000 in supplementary
  groups ( groups field) come from, even though 50000 is not defined in the Pod''s
  manifest at all? The answer is /etc/group file in the container image. Checking
  the contents of /etc/group in the container image should show below: This shows
  that the container''s primary user 1000 belongs to the group 50000 in the last entry.
  Thus, the group membership defined in /etc/group in the container image for the
  container''s primary user is implicitly merged to the information from the Pod.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/06/kubernetes-v1-33-fine-grained-supplementalgroups-control-beta/
