---
title: Full request and response compliance logging on Amazon EKS
date: '2026-07-07T16:35:30+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/full-request-and-response-compliance-logging-on-amazon-eks/
post_kind: link
draft: false
tldr: 'Full request and response compliance logging on Amazon EKS Why enterprises
  need full request and response logging Alternative approaches to request and response
  logging Proxy-layer request and response capture with Envoy’s External Processing
  filter High-level architecture Request and response flow How the gRPC stream works
  Walkthrough Prerequisites Step 1: Clone the repository Step 2: Provision infrastructure
  with Terraform Step 3: Configure kubectl Step 4: Install the Istio Ingress Gateway
  Step 5: Enable Istio sidecar injection Step 6: Deploy the ext_proc server to Kubernetes
  Step 7: Configure Envoy with the EnvoyFilter Step 8: Deploy the test application
  Step 9: Test the setup Testing the solution Step 10: Verify audit logs Cleanup Step
  1: Delete application resources Step 2: Delete the Istio Ingress Gateway Step 3:
  Destroy infrastructure with Terraform Conclusion About the authors Compliance logging
  on Amazon Elastic Kubernetes Service (Amazon EKS) reveals its biggest gap at exactly
  the moment that it matters most. An auditor asks for the actual request and response
  data behind a transaction, not only the metadata around it.'
summary: 'Full request and response compliance logging on Amazon EKS Why enterprises
  need full request and response logging Alternative approaches to request and response
  logging Proxy-layer request and response capture with Envoy’s External Processing
  filter High-level architecture Request and response flow How the gRPC stream works
  Walkthrough Prerequisites Step 1: Clone the repository Step 2: Provision infrastructure
  with Terraform Step 3: Configure kubectl Step 4: Install the Istio Ingress Gateway
  Step 5: Enable Istio sidecar injection Step 6: Deploy the ext_proc server to Kubernetes
  Step 7: Configure Envoy with the EnvoyFilter Step 8: Deploy the test application
  Step 9: Test the setup Testing the solution Step 10: Verify audit logs Cleanup Step
  1: Delete application resources Step 2: Delete the Istio Ingress Gateway Step 3:
  Destroy infrastructure with Terraform Conclusion About the authors Compliance logging
  on Amazon Elastic Kubernetes Service (Amazon EKS) reveals its biggest gap at exactly
  the moment that it matters most. An auditor asks for the actual request and response
  data behind a transaction, not only the metadata around it. Imagine your security
  team needs every API transaction involving patient health records from last Tuesday.
  You pull up your observability dashboard, and it shows HTTP status codes, latency
  metrics, and request counts. But the auditor shakes their head, explaining that
  they need to see the actual data that was transmitted. This is the compliance gap
  that many enterprises running microservices on Amazon EKS face today. Service meshes
  like Istio and proxies like Envoy excel at capturing metadata, status codes, headers,
  and latency, but they don’t capture the actual request and response bodies. The
  very data that auditors, regulators, and compliance officers need to verify is the
  data that’s never recorded. For enterprises with stringent data governance and audit
  requirements, this represents an operational gap. Failed audits, regulatory fines,
  and the inability to reconstruct what happened during a security event are real
  consequences of this gap. In this post, we demonstrate how to use Envoy’s External
  Processing filter (ext_proc) to solve this challenge on Amazon EKS. This solution
  captures complete request and response data without modifying application code,
  providing the compliance-grade audit trails that regulators require.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/full-request-and-response-compliance-logging-on-amazon-eks/
