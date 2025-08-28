---
title: 'Kubernetes v1.33: Fine-grained SupplementalGroups Control Graduates to Beta'
date: '2025-05-06T10:30:00-08:00'
tags:
- kubernetes
source: Kubernetes Blog
external_url: https://kubernetes.io/blog/2025/05/06/kubernetes-v1-33-fine-grained-supplementalgroups-control-beta/
post_kind: link
draft: false
tldr: 'Kubernetes v1.33: Fine-grained SupplementalGroups Control Graduates to Beta
  Motivation: Implicit group memberships defined in /etc/group in the container image
  What''s wrong with it? Fine-grained supplemental groups control in a Pod: supplementaryGroupsPolicy
  Attached process identity in Pod status Strict Policy requires newer CRI versions
  The behavioral changes introduced in beta Upgrade consideration Getting involved
  How can I learn more? The new field, supplementalGroupsPolicy , was introduced as
  an opt-in alpha feature for Kubernetes v1.31 and has graduated to beta in v1.33;
  the corresponding feature gate ( SupplementalGroupsPolicy ) is now enabled by default.
  This feature enables to implement more precise control over supplemental groups
  in containers that can strengthen the security posture, particularly in accessing
  volumes.'
summary: 'Kubernetes v1.33: Fine-grained SupplementalGroups Control Graduates to Beta
  Motivation: Implicit group memberships defined in /etc/group in the container image
  What''s wrong with it? Fine-grained supplemental groups control in a Pod: supplementaryGroupsPolicy
  Attached process identity in Pod status Strict Policy requires newer CRI versions
  The behavioral changes introduced in beta Upgrade consideration Getting involved
  How can I learn more? The new field, supplementalGroupsPolicy , was introduced as
  an opt-in alpha feature for Kubernetes v1.31 and has graduated to beta in v1.33;
  the corresponding feature gate ( SupplementalGroupsPolicy ) is now enabled by default.
  This feature enables to implement more precise control over supplemental groups
  in containers that can strengthen the security posture, particularly in accessing
  volumes. Moreover, it also enhances the transparency of UID/GID details in containers,
  offering improved security oversight. supplementalGroupsPolicy SupplementalGroupsPolicy
  Please be aware that this beta release contains some behavioral breaking change.
  See The Behavioral Changes Introduced In Beta and Upgrade Considerations sections
  for details. /etc/group Although the majority of Kubernetes cluster admins/users
  may not be aware, kubernetes, by default, merges group information from the Pod
  with information defined in /etc/group in the container image. /etc/group Let''s
  see an example, below Pod manifest specifies runAsUser=1000 , runAsGroup=3000 and
  supplementalGroups=4000 in the Pod''s security context. runAsUser=1000 runAsGroup=3000
  supplementalGroups=4000 apiVersion : v1 kind : Pod metadata : name : implicit-groups
  spec : securityContext : runAsUser : 1000 runAsGroup : 3000 supplementalGroups :
  [ 4000 ] containers : - name : ctr image : registry. k8s. io/e2e-test-images/agnhost:2.45
  command : [ "sh" , "-c" , "sleep 1h" ] securityContext : allowPrivilegeEscalation
  : false apiVersion : v1 kind : Pod metadata : name : implicit-groups spec : securityContext
  : runAsUser : 1000 runAsGroup : 3000 supplementalGroups : [ 4000 ] containers :
  - name : ctr image : registry. k8s. io/e2e-test-images/agnhost:2.45 command : [
  "sh" , "-c" , "sleep 1h" ] securityContext : allowPrivilegeEscalation : false What
  is the result of id command in the ctr container? The output should be similar to
  this: id ctr uid=1000 gid=3000 groups=3000,4000,50000 uid=1000 gid=3000 groups=3000,4000,50000
  Where does group ID 50000 in supplementary groups ( groups field) come from, even
  though 50000 is not defined in the Pod''s manifest at all? The answer is /etc/group
  file in the container image.'
---
Open the original post ↗ https://kubernetes.io/blog/2025/05/06/kubernetes-v1-33-fine-grained-supplementalgroups-control-beta/
