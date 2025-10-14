---
title: How to manage EKS Pod Identities at scale using Argo CD and AWS ACK
date: '2025-10-13T21:16:16+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/how-to-manage-eks-pod-identities-at-scale-using-argo-cd-and-aws-ack/
post_kind: link
draft: false
tldr: 'How to manage EKS Pod Identities at scale using Argo CD and AWS ACK What is
  GitOps? EKS Pod Identity: Simplifying IAM Permissions for Kubernetes Applications
  Overview of Amazon Controllers for Kubernetes (ACK) Prerequisites High-level overview
  of the steps Install Amazon EKS Pod Identity Agent Install the AWS Controllers for
  Kubernetes (ACK) 1. Creation of a role for our ACK controller and the EKS Pod Identity
  association 2.'
summary: 'How to manage EKS Pod Identities at scale using Argo CD and AWS ACK What
  is GitOps? EKS Pod Identity: Simplifying IAM Permissions for Kubernetes Applications
  Overview of Amazon Controllers for Kubernetes (ACK) Prerequisites High-level overview
  of the steps Install Amazon EKS Pod Identity Agent Install the AWS Controllers for
  Kubernetes (ACK) 1. Creation of a role for our ACK controller and the EKS Pod Identity
  association 2. Install the ACK controller for EKS with Helm, edit region as needed
  Accessing Argo CD Deploy the sample application highlighting the problem 1. Clone
  the code repository for the sample application project 2. Create the IAM role to
  be used by the application 3. Open application. yaml file, the following parameters
  can be replaced with your own 4. Create the Argo CD application 5. Confirm the role
  from inside our container Validate the correct role is passed via a job Alternative
  Solution: Changing ARGOCD_SYNC_WAVE_DELAY Cleanup Conclusion About the authors In
  today’s blog post, we’ll explore how to manage at scale the association of Kubernetes
  service accounts with IAM roles through the Amazon Elastic Kubernetes Service (EKS)
  Pod Identity association. We will be using Argo CD , a popular GitOps delivery tool,
  and the AWS Controllers for Kubernetes (ACK) to automate the association, but as
  we will see this sometimes causes a critical challenge: the EKS Pod Identity API
  is eventually consistent. We need to verify the association is available for the
  credentials before the application pods are deployed. Our focus will be on correct
  deployment, thus addressing that challenge, without causing side effects.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/how-to-manage-eks-pod-identities-at-scale-using-argo-cd-and-aws-ack/
