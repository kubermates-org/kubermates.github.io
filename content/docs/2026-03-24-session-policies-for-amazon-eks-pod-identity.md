---
title: Session policies for Amazon EKS Pod Identity
date: '2026-03-24T18:17:32+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/session-policies-for-amazon-eks-pod-identity/
post_kind: link
draft: false
tldr: 'Session policies for Amazon EKS Pod Identity What is changing in EKS Pod Identity
  APIs How to get started Prerequisites Setup Step 1: Create an EKS cluster with Pod
  Identity add-on Step 2: Create an IAM role with broad S3 permissions Step 3: Create
  a Pod Identity association without a session policy Step 4: Test the pod with full
  IAM role permissions Step 5: Add a session policy to restrict permissions Step 6:
  Verify the restricted permissions Step 7: Expand the session policy Understanding
  session policy validation Important considerations Session tags and session policies
  Permission intersection Session policy application Other considerations Cleaning
  up Conclusion Additional resources About the authors Today, we’re announcing the
  new session policies capability for Amazon Elastic Kubernetes Service (Amazon EKS)
  Pod Identity. With this new feature, you can dynamically scope down AWS Identity
  and Access Management (IAM) permissions for your Kubernetes pods without creating
  additional IAM roles.'
summary: 'Session policies for Amazon EKS Pod Identity What is changing in EKS Pod
  Identity APIs How to get started Prerequisites Setup Step 1: Create an EKS cluster
  with Pod Identity add-on Step 2: Create an IAM role with broad S3 permissions Step
  3: Create a Pod Identity association without a session policy Step 4: Test the pod
  with full IAM role permissions Step 5: Add a session policy to restrict permissions
  Step 6: Verify the restricted permissions Step 7: Expand the session policy Understanding
  session policy validation Important considerations Session tags and session policies
  Permission intersection Session policy application Other considerations Cleaning
  up Conclusion Additional resources About the authors Today, we’re announcing the
  new session policies capability for Amazon Elastic Kubernetes Service (Amazon EKS)
  Pod Identity. With this new feature, you can dynamically scope down AWS Identity
  and Access Management (IAM) permissions for your Kubernetes pods without creating
  additional IAM roles. Session policies give you a flexible alternative to creating
  separate IAM roles for each permission variation by specifying an inline IAM policy
  during Pod Identity association creation. This helps you to manage permissions at
  scale without multiplying your role count. This means that your Kubernetes applications
  can now operate with precisely the permissions required, following the principle
  of least privilege, while avoiding reaching IAM role limits in large-scale deployments.
  In this post, we demonstrate how to use session policies to dynamically scope down
  IAM permissions for your Kubernetes pods without creating additional IAM roles,
  and discuss important considerations when adopting this feature. At re:Invent 2023,
  Amazon EKS introduced the EKS Pod Identity feature. This feature helps users to
  configure Kubernetes applications running on Amazon EKS with fine-grained IAM permissions
  to access AWS resources such as Amazon Simple Storage Service (Amazon S3) buckets
  and Amazon DynamoDB tables. This feature addressed many of the existing challenges
  of IAM Roles for Service Accounts (IRSA) by removing the need to set up OpenID Connect
  (OIDC) providers for EKS clusters, streamlining IAM trust policies, and streamlining
  the experience through Amazon EKS APIs. Furthermore, it introduced support for IAM
  role session tags , so IAM administrators can author a single permissions policy
  that can work across roles by allowing access to AWS resources based on matching
  tags. Through nearly continuous user feedback, we learned that customers often face
  challenges when they need different permission levels for pods running the same
  application. Common scenarios include the following: Platform Engineering teams
  managing multi-tenant EKS clusters where different customer workloads need varying
  levels of access to the same AWS services.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/session-policies-for-amazon-eks-pod-identity/
