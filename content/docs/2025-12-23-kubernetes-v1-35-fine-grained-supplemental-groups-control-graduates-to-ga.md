---
title: 'Kubernetes v1.35: Fine-grained Supplemental Groups Control Graduates to GA'
date: '2025-12-23T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/12/23/kubernetes-v1-35-fine-grained-supplementalgroups-control-ga/
post_kind: link
draft: false
tldr: 'Kubernetes v1.35: Fine-grained Supplemental Groups Control Graduates to GA
  Motivation: Implicit group memberships defined in /etc/group in the container image
  What''s wrong with it? Fine-grained supplemental groups control in a Pod: supplementaryGroupsPolicy
  Attached process identity in Pod status Strict policy requires up-to-date container
  runtimes Getting involved How can I learn more? On behalf of Kubernetes SIG Node,
  we are pleased to announce the graduation of fine-grained supplemental groups control
  to General Availability (GA) in Kubernetes v1.35! The new Pod field, supplementalGroupsPolicy
  , was introduced as an opt-in alpha feature for Kubernetes v1.31, and then had graduated
  to beta in v1.33. Now, the feature is generally available.'
summary: 'Kubernetes v1.35: Fine-grained Supplemental Groups Control Graduates to
  GA Motivation: Implicit group memberships defined in /etc/group in the container
  image What''s wrong with it? Fine-grained supplemental groups control in a Pod:
  supplementaryGroupsPolicy Attached process identity in Pod status Strict policy
  requires up-to-date container runtimes Getting involved How can I learn more? On
  behalf of Kubernetes SIG Node, we are pleased to announce the graduation of fine-grained
  supplemental groups control to General Availability (GA) in Kubernetes v1.35! The
  new Pod field, supplementalGroupsPolicy , was introduced as an opt-in alpha feature
  for Kubernetes v1.31, and then had graduated to beta in v1.33. Now, the feature
  is generally available. This feature allows you to implement more precise control
  over supplemental groups in Linux containers that can strengthen the security posture
  particularly in accessing volumes. Moreover, it also enhances the transparency of
  UID/GID details in containers, offering improved security oversight. supplementalGroupsPolicy
  If you are planning to upgrade your cluster from v1.32 or an earlier version, please
  be aware that some behavioral breaking change introduced since beta (v1.33). For
  more details, see the behavioral changes introduced in beta and the upgrade considerations
  sections of the previous blog for graduation to beta. /etc/group Even though the
  majority of Kubernetes cluster admins/users may not be aware of this, by default
  Kubernetes merges group information from the Pod with information defined in /etc/group
  in the container image. /etc/group Here''s an example; a Pod manifest that specifies
  spec. securityContext. runAsUser: 1000 , spec. securityContext. runAsGroup: 3000
  and spec.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/12/23/kubernetes-v1-35-fine-grained-supplementalgroups-control-ga/
