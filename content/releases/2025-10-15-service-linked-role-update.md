---
title: Service linked role update
date: '2025-10-15T19:00:00+00:00'
tags:
- eks
source: EKS Release Notes
external_url: https://docs.aws.amazon.com/eks/latest/userguide/using-service-linked-roles-eks-connector.html
post_kind: release
draft: false
tldr: Using roles to connect a Kubernetes cluster to Amazon EKS Service-linked role
  permissions for Amazon EKS Creating a service-linked role for Amazon EKS Editing
  a service-linked role for Amazon EKS Deleting a service-linked role for Amazon EKS
  Cleaning up a service-linked role Manually delete the service-linked role Help improve
  this page To contribute to this user guide, choose the Edit this page on GitHub
  link that is located in the right pane of every page. Amazon EKS uses AWS Identity
  and Access Management (IAM) service-linked roles.
summary: "Using roles to connect a Kubernetes cluster to Amazon EKS Service-linked\
  \ role permissions for Amazon EKS Creating a service-linked role for Amazon EKS\
  \ Editing a service-linked role for Amazon EKS Deleting a service-linked role for\
  \ Amazon EKS Cleaning up a service-linked role Manually delete the service-linked\
  \ role Help improve this page To contribute to this user guide, choose the Edit\
  \ this page on GitHub link that is located in the right pane of every page. Amazon\
  \ EKS uses AWS Identity and Access Management (IAM) service-linked roles. A service-linked\
  \ role is a unique type of IAM role that is linked directly to Amazon EKS. Service-linked\
  \ roles are predefined by Amazon EKS and include all the permissions that the service\
  \ requires to call other AWS services on your behalf. A service-linked role makes\
  \ setting up Amazon EKS easier because you donâ\x80\x99t have to manually add the\
  \ necessary permissions. Amazon EKS defines the permissions of its service-linked\
  \ roles, and unless defined otherwise, only Amazon EKS can assume its roles. The\
  \ defined permissions include the trust policy and the permissions policy, and that\
  \ permissions policy cannot be attached to any other IAM entity. You can delete\
  \ a service-linked role only after first deleting their related resources. This\
  \ protects your Amazon EKS resources because you canâ\x80\x99t inadvertently remove\
  \ permission to access the resources. For information about other services that\
  \ support service-linked roles, see AWS services that work with IAM and look for\
  \ the services that have Yes in the Service-linked role column. Choose a Yes with\
  \ a link to view the service-linked role documentation for that service. Amazon\
  \ EKS uses the service-linked role named AWSServiceRoleForAmazonEKSConnector."
---
Open the original post ↗ https://docs.aws.amazon.com/eks/latest/userguide/using-service-linked-roles-eks-connector.html
