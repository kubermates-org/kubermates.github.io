---
title: Enhance Amazon EKS network security posture with DNS and admin network policies
date: '2025-12-22T18:04:38+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/enhance-amazon-eks-network-security-posture-with-dns-and-admin-network-policies/
post_kind: link
draft: false
tldr: Enhance Amazon EKS network security posture with DNS and admin network policies
  Amazon EKS enhanced network policies Admin network policies DNS-based network policies
  Implementation across EKS deployment models Use cases 1. Enforcing cluster-level
  security with Admin network policies 2.
summary: Enhance Amazon EKS network security posture with DNS and admin network policies
  Amazon EKS enhanced network policies Admin network policies DNS-based network policies
  Implementation across EKS deployment models Use cases 1. Enforcing cluster-level
  security with Admin network policies 2. Securing access to AWS services in multi-tenant
  environments 3. Hybrid cloud integration Implementation best practices Building
  baseline security with deny-by-default rules Using label-based segmentation Combining
  DNS policies with traditional network policies Monitoring and audit Considerations
  Understanding policy evaluation order Applying the principle of least privilege
  Validating your DNS policies Interaction with Amazon Route 53 DNS firewall Conclusion
  About the authors Amazon Web Services (AWS) announced the availability of DNS-based
  and Admin network policies for Amazon Elastic Kubernetes Service (EKS) Auto mode
  and Admin network policies for both EKS Auto mode and EKS on Amazon Elastic Compute
  Cloud (EC2), providing enhanced capabilities to secure network traffic both within
  your clusters and to external endpoints. These new policy types enable you to implement
  stable, domain-based access controls for external services while centrally managing
  security policies across multiple namespaces, reducing operational complexity and
  strengthening your overall security posture. In this post, we explore practical
  use cases that demonstrate how these policies solve real-world challenges and remove
  the need to rely on third-party software across different deployment scenarios,
  from securing access to external services to hybrid cloud integration and multi-tenant
  environments. Application modernization drives demand for sophisticated network
  security that simplifies operations at scale. Modern containerized applications
  require granular control over external endpoint access, enabling teams to precisely
  manage which cluster-external services (such as AWS services, on-premises systems,
  and third-party APIs) their workloads can reach. Teams want to move beyond IP-based
  filtering to DNS-based access control, leveraging stable domain names rather than
  constantly changing IP addresses for more predictable and maintainable security
  policies. Organizations also need centralized policy management capabilities that
  enforce consistent security standards across multiple namespaces and workloads,
  ensuring uniform protection without requiring individual teams to implement policies
  independently. As these environments grow, there’s an increasing focus on operational
  simplicity, reducing the administrative overhead of managing network-level security
  while maintaining strong defensive postures that scale effectively with business
  growth. Admin network policies provide centralized, cluster-wide network access
  control that spans multiple namespaces.
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/enhance-amazon-eks-network-security-posture-with-dns-and-admin-network-policies/
