---
title: 'Data-driven Amazon EKS cost optimization: A practical guide to workload analysis'
date: '2025-11-26T17:32:47+00:00'
tags:
- eks
- aws
source: AWS Containers Blog (EKS)
external_url: https://aws.amazon.com/blogs/containers/data-driven-amazon-eks-cost-optimization-a-practical-guide-to-workload-analysis/
post_kind: link
draft: false
tldr: 'Data-driven Amazon EKS cost optimization: A practical guide to workload analysis
  Common pattern of resource waste The greedy workload caused oversized pod resources
  Problem: Impact: Resolution: Recommendations: Tools to help with this: The pet workload
  causes excessive replica counts Problem: Impact: Overly strict topology spread constraints:
  Recommendation: Overly strict Pod Distribution Budget (PDB): Recommendations: The
  isolated workloads configured with fragmented node pools Why the savings occur:
  Recommendations: Conclusion About the authors This post introduces some of the key
  considerations for optimizing Amazon Elastic Kubernetes Service (Amazon EKS) costs
  in production environments. Through detailed workload analysis and comprehensive
  monitoring, we demonstrate a proven best practice to maximize cost savings while
  maintaining performance and resilience supported by real-world examples and practical
  implementation guidelines.'
summary: 'Data-driven Amazon EKS cost optimization: A practical guide to workload
  analysis Common pattern of resource waste The greedy workload caused oversized pod
  resources Problem: Impact: Resolution: Recommendations: Tools to help with this:
  The pet workload causes excessive replica counts Problem: Impact: Overly strict
  topology spread constraints: Recommendation: Overly strict Pod Distribution Budget
  (PDB): Recommendations: The isolated workloads configured with fragmented node pools
  Why the savings occur: Recommendations: Conclusion About the authors This post introduces
  some of the key considerations for optimizing Amazon Elastic Kubernetes Service
  (Amazon EKS) costs in production environments. Through detailed workload analysis
  and comprehensive monitoring, we demonstrate a proven best practice to maximize
  cost savings while maintaining performance and resilience supported by real-world
  examples and practical implementation guidelines. In pursuing optimal performance
  and resilience, organizations often struggle to balance cost efficiency, as shown
  in the following figure. Figure 1: Strategic balance triangle showing trade-offs
  Through collaboration with application owners and developers, a clear pattern emerges:
  the primary driver of cloud cost waste is overprovisioned resources, justified by
  performance and resilience considerations that may no longer reflect actual needs.
  In this post we discuss three critical areas of waste: Greedy workload : oversized
  pod resources for performance Pet workload : excessive replica counts for resilience
  Isolated workload: fragmented node pools with stranded capacity for performance
  Each decision, made with good intentions, accumulates into unnecessary spending
  over time. The challenge is finding the optimal balance through data-driven rightsizing
  and architectural optimization. We can call them greedy workloads if a Pod’s requests
  are higher than what the application actually tries to use. resources: requests:
  memory: 3Gi cpu: 800m limits: memory: 3Gi resources: requests: memory: 3Gi cpu:
  800m limits: memory: 3Gi The application tries to actually use ~0. 2vCPU (200 m)
  and ~1 Gi of memory. Figure 2: Request and actual usage We can see that in total
  we’re actually only using ~400 m/1930 m (~21%) vCPU, and ~2 Gi/6.8 Gi (~29%) memory,
  as shown in the preceding figure. Despite having plenty of actual resources for
  more copies of this Pod, Kubernetes doesn’t place any more replicas on this node
  because the allocatable resources have been almost completely allocated. We adjust
  the requests to be 200 m CPU and 1 Gi of memory to match the application’s workload.'
---
Open the original post ↗ https://aws.amazon.com/blogs/containers/data-driven-amazon-eks-cost-optimization-a-practical-guide-to-workload-analysis/
