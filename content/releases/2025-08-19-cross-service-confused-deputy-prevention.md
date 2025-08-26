---
title: Cross-service confused deputy prevention
date: '2025-08-19T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/cross-service-confused-deputy-prevention.html
post_kind: release
draft: false
tldr: "Help improve this page To contribute to this user guide, choose the Edit this\
  \ page on GitHub link that is located in the right pane of every page. The confused\
  \ deputy problem is a security issue where an entity that doesnâ\x80\x99t have permission\
  \ to perform an action can coerce a more-privileged entity to perform the action."
summary: "Help improve this page To contribute to this user guide, choose the Edit\
  \ this page on GitHub link that is located in the right pane of every page. The\
  \ confused deputy problem is a security issue where an entity that doesnâ\x80\x99\
  t have permission to perform an action can coerce a more-privileged entity to perform\
  \ the action. In AWS, cross-service impersonation can result in the confused deputy\
  \ problem. Cross-service impersonation can occur when one service (the calling service\
  \ ) calls another service (the called service ). The calling service can be manipulated\
  \ to use its permissions to act on another customerâ\x80\x99s resources in a way\
  \ it should not otherwise have permission to access. To prevent this, AWS provides\
  \ tools that help you protect your data for all services with service principals\
  \ that have been given access to resources in your account. We recommend using the\
  \ aws:SourceArn , aws:SourceAccount global condition context keys in resource policies\
  \ to limit the permissions that Amazon Elastic Kubernetes Service (Amazon EKS) gives\
  \ another service to the resource. Use aws:SourceArn to associate only one resource\
  \ with cross-service access. Use aws:SourceAccount to let any resource in that account\
  \ be associated with the cross-service use. The most effective way to protect against\
  \ the confused deputy problem is to use the aws:SourceArn global condition context\
  \ key with the full ARN of the resource. If you donâ\x80\x99t know the full ARN\
  \ of the resource or if you are specifying multiple resources, use the aws:SourceArn\
  \ global context condition key with wildcard characters (*) for the unknown portions\
  \ of the ARN. For example, arn:aws:<servicename>:*:<123456789012>:*."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/cross-service-confused-deputy-prevention.html
